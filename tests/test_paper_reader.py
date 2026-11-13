"""Offline tests: every Codex invocation is mocked; no model calls are made."""

import contextlib
import hashlib
import importlib.util
import io
import json
import os
from pathlib import Path
import signal
import subprocess
import tempfile
from types import SimpleNamespace
import unittest
from unittest import mock


MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "paper_reader.py"
SPEC = importlib.util.spec_from_file_location("paper_reader", MODULE_PATH)
reader = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(reader)


class PaperReaderTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix="paper-reader-test-")
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.notes = self.root / "notes.md"
        self.source = self.root / "source.txt"
        self.output = self.root / "artifacts" / "result.txt"
        self.receipt = self.root / "artifacts" / "receipt.json"
        self.notes.write_text("Draft notes: method, equations and evidence.", encoding="utf-8")
        self.source.write_text("Original source: the method and its supporting evidence.", encoding="utf-8")
        self.args = SimpleNamespace(
            stage="assess", notes=self.notes, source=self.source,
            output=self.output, receipt=self.receipt, scope="section 2, pages 3-5",
            timeout=1800, model=None, effort="high", dry_run=False,
        )

    def load_receipt(self):
        return json.loads(self.receipt.read_text(encoding="utf-8"))

    def succeed(self, command, prompt, cwd, timeout):
        result = Path(command[command.index("--output-last-message") + 1])
        self.assertEqual(result.parent, Path(cwd))
        self.assertNotEqual(Path(cwd), self.root)
        self.assertTrue(Path(cwd).is_dir())
        self.assertEqual(command[command.index("-s") + 1], "read-only")
        self.assertIn("--ephemeral", command)
        self.assertIn("--skip-git-repo-check", command)
        self.assertEqual(timeout, self.args.timeout)
        self.assertIn("Original source:", prompt)
        result.write_text(f"PAPER_{self.args.stage.upper()}_RESULT\nEvidence-supported advice.\n", encoding="utf-8")
        return 0, "model progress", ""

    def assert_failed(self, expected_status="failed"):
        report = self.load_receipt()
        self.assertEqual(report["status"], expected_status)
        self.assertFalse(report["ok"])
        self.assertFalse(report["stage_complete"])
        self.assertFalse(report["workflow_complete"])
        self.assertIn("error", report)
        self.assertGreaterEqual(report["elapsed_seconds"], 0)
        self.assertFalse(self.output.exists())
        return report

    def test_success_all_stages_defaults_hashes_scope_and_cleanup(self):
        for stage, model in reader.DEFAULT_MODELS.items():
            with self.subTest(stage=stage):
                self.args.stage = stage
                self.output = self.args.output = self.root / f"{stage}.txt"
                self.receipt = self.args.receipt = self.root / f"{stage}.json"
                with mock.patch.object(reader, "run_codex", side_effect=self.succeed) as run:
                    report = reader.execute_stage(self.args)
                run.assert_called_once()
                self.assertEqual(report, self.load_receipt())
                self.assertEqual(report["model"], model)
                self.assertEqual(report["effort"], "high")
                self.assertEqual(report["status"], "completed")
                self.assertTrue(report["stage_complete"])
                self.assertFalse(report["workflow_complete"])
                self.assertEqual(report["attempts"], 1)
                self.assertEqual(report["scope"], self.args.scope)
                self.assertGreaterEqual(report["elapsed_seconds"], 0)
                for name, path in (("notes", self.notes), ("source", self.source)):
                    self.assertEqual(report["inputs"][name]["sha256"],
                                     hashlib.sha256(path.read_bytes()).hexdigest())
                self.assertEqual(report["output_sha256"],
                                 hashlib.sha256(self.output.read_bytes()).hexdigest())
                self.assertEqual(len(report["prompt_sha256"]), 64)
                self.assertFalse(Path(run.call_args.args[2]).exists())

    def test_custom_model_effort_and_timeout_recorded(self):
        self.args.model = "custom-model"
        self.args.effort = "medium"
        self.args.timeout = 17
        with mock.patch.object(reader, "run_codex", side_effect=self.succeed) as run:
            report = reader.execute_stage(self.args)
        command = run.call_args.args[0]
        self.assertEqual(command[command.index("-m") + 1], "custom-model")
        self.assertIn('model_reasoning_effort="medium"', command)
        self.assertEqual(report["model"], "custom-model")
        self.assertEqual(report["effort"], "medium")
        self.assertEqual(report["timeout_seconds"], 17)

    def test_nonzero_failure_preserves_receipt_without_retry(self):
        with mock.patch.object(reader, "run_codex", return_value=(7, "partial", "backend failed")) as run:
            with self.assertRaises(reader.StageError):
                reader.execute_stage(self.args)
        run.assert_called_once()
        report = self.assert_failed()
        self.assertEqual(report["exit_code"], 7)
        self.assertEqual(report["stderr"], "backend failed")
        self.assertEqual(report["attempts"], 1)
        self.assertIn("sha256", report["inputs"]["source"])

    def test_timeout_preserves_receipt_without_retry(self):
        with mock.patch.object(reader, "run_codex", return_value=(124, "partial", "deadline")) as run:
            with self.assertRaises(reader.StageError):
                reader.execute_stage(self.args)
        run.assert_called_once()
        self.assertEqual(self.assert_failed("timeout")["exit_code"], 124)

    def test_missing_codex_preserves_failure_receipt(self):
        with mock.patch.object(reader, "run_codex", side_effect=FileNotFoundError("codex")) as run:
            with self.assertRaises(reader.StageError):
                reader.execute_stage(self.args)
        run.assert_called_once()
        self.assertIn("FileNotFoundError", self.assert_failed()["error"])

    def test_empty_and_whitespace_source_rejected(self):
        for content in ("", " \n\t"):
            with self.subTest(content=content):
                self.source.write_text(content, encoding="utf-8")
                self.receipt = self.args.receipt = self.root / f"empty-{len(content)}.json"
                with mock.patch.object(reader, "run_codex") as run:
                    with self.assertRaises(reader.StageError):
                        reader.execute_stage(self.args)
                run.assert_not_called()
                self.assertIn("Empty", self.assert_failed()["error"])

    def test_empty_notes_rejected(self):
        self.notes.write_text("", encoding="utf-8")
        with mock.patch.object(reader, "run_codex") as run:
            with self.assertRaises(reader.StageError):
                reader.execute_stage(self.args)
        run.assert_not_called()
        self.assertIn("Empty", self.assert_failed()["error"])

    def test_oversized_context_rejected_without_truncation(self):
        content = "x" * reader.MAX_CONTEXT_CHARS
        self.source.write_text(content, encoding="utf-8")
        with mock.patch.object(reader, "run_codex") as run:
            with self.assertRaises(reader.StageError):
                reader.execute_stage(self.args)
        run.assert_not_called()
        report = self.assert_failed()
        self.assertIn("nothing is truncated", report["error"])
        self.assertEqual(report["inputs"]["source"]["chars"], len(content))
        self.assertEqual(report["inputs"]["source"]["sha256"],
                         hashlib.sha256(content.encode()).hexdigest())

    def test_oversized_bytes_explicitly_records_incomplete_hash(self):
        with mock.patch.object(reader, "MAX_INPUT_BYTES", 48), mock.patch.object(reader, "run_codex") as run:
            with self.assertRaises(reader.StageError):
                reader.execute_stage(self.args)
        run.assert_not_called()
        report = self.assert_failed()
        self.assertIsNone(report["inputs"]["source"]["sha256"])
        self.assertEqual(report["inputs"]["source"]["hash_status"],
                         "not_computed_input_exceeds_byte_limit")

    def test_invalid_timeout_rejected_with_receipt(self):
        for timeout in (0, -1, 1801):
            with self.subTest(timeout=timeout):
                self.args.timeout = timeout
                self.receipt = self.args.receipt = self.root / f"timeout-{timeout}.json"
                with mock.patch.object(reader, "run_codex") as run:
                    with self.assertRaises(reader.StageError):
                        reader.execute_stage(self.args)
                run.assert_not_called()
                self.assert_failed()

    def test_existing_output_or_receipt_never_overwritten(self):
        for kind in ("output", "receipt"):
            with self.subTest(kind=kind):
                existing = getattr(self, kind)
                existing.parent.mkdir(exist_ok=True)
                existing.write_text("existing artifact", encoding="utf-8")
                with mock.patch.object(reader, "run_codex") as run:
                    with self.assertRaises(reader.StageError):
                        reader.execute_stage(self.args)
                run.assert_not_called()
                self.assertEqual(existing.read_text(), "existing artifact")
                # Remove only the test fixture before testing the other target.
                existing.unlink()

    def test_dangling_output_symlink_never_overwritten(self):
        self.output.parent.mkdir()
        self.output.symlink_to(self.root / "nonexistent")
        with mock.patch.object(reader, "run_codex") as run:
            with self.assertRaises(reader.StageError):
                reader.execute_stage(self.args)
        run.assert_not_called()
        self.assertTrue(self.output.is_symlink())

    def test_output_input_alias_rejected(self):
        self.args.output = self.source
        before = self.source.read_bytes()
        with mock.patch.object(reader, "run_codex") as run:
            with self.assertRaises(reader.StageError):
                reader.execute_stage(self.args)
        run.assert_not_called()
        self.assertEqual(self.source.read_bytes(), before)
        self.assertFalse(self.receipt.exists())

    def test_output_receipt_alias_rejected(self):
        self.args.output = self.receipt
        with mock.patch.object(reader, "run_codex") as run:
            with self.assertRaises(reader.StageError):
                reader.execute_stage(self.args)
        run.assert_not_called()
        self.assertFalse(self.receipt.exists())

    def test_output_creation_race_keeps_winner_and_failure_receipt(self):
        def race(*args):
            self.output.parent.mkdir()
            self.output.write_text("race winner", encoding="utf-8")
            return self.succeed(*args)
        with mock.patch.object(reader, "run_codex", side_effect=race):
            with self.assertRaises(reader.StageError):
                reader.execute_stage(self.args)
        self.assertEqual(self.output.read_text(), "race winner")
        self.assertFalse(self.load_receipt()["stage_complete"])
        self.assertEqual(self.load_receipt()["status"], "failed")

    def test_atomic_writer_refuses_existing_and_cleans_temporaries(self):
        reader.atomic_write_new(self.output, "complete artifact")
        with self.assertRaises(FileExistsError):
            reader.atomic_write_new(self.output, "replacement")
        self.assertEqual(self.output.read_text(), "complete artifact")
        self.assertEqual(list(self.output.parent.glob(".paper-reader-*")), [])

    def test_dry_run_writes_full_plan_and_never_completes_stage(self):
        self.args.dry_run = True
        with mock.patch.object(reader, "run_codex") as run, mock.patch.object(reader.subprocess, "Popen") as popen:
            report = reader.execute_stage(self.args)
        run.assert_not_called()
        popen.assert_not_called()
        plan = json.loads(self.output.read_text())
        self.assertTrue(report["ok"])
        self.assertEqual(report["status"], "dry_run")
        self.assertFalse(report["stage_complete"])
        self.assertFalse(report["workflow_complete"])
        self.assertFalse(report["model_called"])
        self.assertEqual(report["attempts"], 0)
        self.assertFalse(plan["stage_complete"])
        self.assertIn(self.source.read_text(), plan["prompt"])
        self.assertIn(self.notes.read_text(), plan["prompt"])
        self.assertIn(self.args.scope, plan["prompt"])
        self.assertEqual(plan["cwd"], "<FRESH_TEMP_DIRECTORY>")

    def test_missing_or_invalid_result_fails(self):
        for content in (None, "", "PAPER_ASSESS_RESULT", "Incorrect marker\nbody", "PAPER_ASSESS_RESULTgarbage\nbody"):
            with self.subTest(content=content):
                self.receipt = self.args.receipt = self.root / f"invalid-{len(list(self.root.glob('invalid-*')))}.json"
                def respond(command, *unused):
                    if content is not None:
                        Path(command[command.index("--output-last-message") + 1]).write_text(content)
                    return 0, "", ""
                with mock.patch.object(reader, "run_codex", side_effect=respond) as run:
                    with self.assertRaises(reader.StageError):
                        reader.execute_stage(self.args)
                run.assert_called_once()
                self.assert_failed()

    def test_pdf_extraction_page_markers_and_hash(self):
        self.args.source = self.root / "paper.pdf"
        raw = b"mock PDF bytes"
        self.args.source.write_bytes(raw)
        document = mock.MagicMock()
        document.__enter__.return_value = document
        document.__len__.return_value = 2
        document.__iter__.return_value = iter([
            SimpleNamespace(get_text=lambda: "First page scientific evidence"),
            SimpleNamespace(get_text=lambda: "Second page equations"),
        ])
        fitz = SimpleNamespace(open=mock.Mock(return_value=document))
        self.args.dry_run = True
        with mock.patch.object(reader.importlib, "import_module", return_value=fitz):
            report = reader.execute_stage(self.args)
        prompt = json.loads(self.output.read_text())["prompt"]
        self.assertIn("[PDF page 1]", prompt)
        self.assertIn("[PDF page 2]", prompt)
        self.assertEqual(report["inputs"]["source"]["pages"], 2)
        self.assertEqual(report["inputs"]["source"]["sha256"], hashlib.sha256(raw).hexdigest())
        fitz.open.assert_called_once_with(stream=raw, filetype="pdf")

    def test_empty_pdf_page_markers_do_not_count_as_text(self):
        self.args.source = self.root / "empty.pdf"
        self.args.source.write_bytes(b"mock PDF")
        document = mock.MagicMock()
        document.__enter__.return_value = document
        document.__iter__.return_value = iter([SimpleNamespace(get_text=lambda: " \n")])
        fitz = SimpleNamespace(open=mock.Mock(return_value=document))
        with mock.patch.object(reader.importlib, "import_module", return_value=fitz), mock.patch.object(reader, "run_codex") as run:
            with self.assertRaises(reader.StageError):
                reader.execute_stage(self.args)
        run.assert_not_called()
        self.assertIn("Empty extracted PDF", self.assert_failed()["error"])

    def test_pdf_missing_optional_dependency_has_failure_receipt(self):
        self.args.source = self.root / "paper.pdf"
        self.args.source.write_bytes(b"mock PDF")
        with mock.patch.object(reader.importlib, "import_module", side_effect=ImportError("fitz")), mock.patch.object(reader, "run_codex") as run:
            with self.assertRaises(reader.StageError):
                reader.execute_stage(self.args)
        run.assert_not_called()
        self.assertIn("optional PyMuPDF", self.assert_failed()["error"])

    def test_missing_input_preserves_receipt(self):
        self.args.source = self.root / "missing.txt"
        with mock.patch.object(reader, "run_codex") as run:
            with self.assertRaises(reader.StageError):
                reader.execute_stage(self.args)
        run.assert_not_called()
        self.assertIn("FileNotFoundError", self.assert_failed()["error"])

    def test_parser_required_arguments_and_defaults(self):
        parser = reader.make_parser()
        with contextlib.redirect_stderr(io.StringIO()):
            with self.assertRaises(SystemExit):
                parser.parse_args([])
            with self.assertRaises(SystemExit):
                parser.parse_args(["--stage", "other"])
        args = parser.parse_args([
            "--stage", "review", "--notes", "notes.md", "--source", "paper.txt",
            "--output", "out.txt", "--receipt", "receipt.json", "--scope", "full text",
        ])
        self.assertEqual(args.timeout, 1800)
        self.assertEqual(args.effort, "high")
        self.assertIsNone(args.model)

    def test_main_returns_nonzero_and_prints_error_on_failure(self):
        with mock.patch.object(reader, "execute_stage", side_effect=reader.StageError("failed")), contextlib.redirect_stderr(io.StringIO()) as stderr:
            code = reader.main([
                "--stage", "review", "--notes", "n", "--source", "s",
                "--output", "o", "--receipt", "r", "--scope", "full text",
            ])
        self.assertEqual(code, 1)
        self.assertFalse(json.loads(stderr.getvalue())["stage_complete"])


class ProcessTests(unittest.TestCase):
    def test_successful_subprocess_uses_stdin_fresh_cwd_and_one_communicate(self):
        process = mock.Mock(returncode=0)
        process.communicate.return_value = ("stdout", "stderr")
        with mock.patch.object(reader.subprocess, "Popen", return_value=process) as popen:
            result = reader.run_codex(["codex", "exec"], "prompt", "/tmp/fresh", 1800)
        self.assertEqual(result, (0, "stdout", "stderr"))
        process.communicate.assert_called_once_with("prompt", timeout=1800)
        self.assertTrue(popen.call_args.kwargs["start_new_session"])
        self.assertEqual(popen.call_args.kwargs["cwd"], "/tmp/fresh")
        self.assertEqual(popen.call_args.kwargs["stdin"], subprocess.PIPE)

    def test_timeout_kills_whole_group_and_reaps_without_retry(self):
        process = mock.Mock(pid=23456)
        process.communicate.side_effect = [
            subprocess.TimeoutExpired(cmd="codex", timeout=9),
            ("partial output", "partial error"),
        ]
        with mock.patch.object(reader.subprocess, "Popen", return_value=process) as popen, mock.patch.object(reader.os, "killpg") as kill:
            result = reader.run_codex(["codex"], "prompt", "/tmp/fresh", 9)
        popen.assert_called_once()
        kill.assert_called_once_with(23456, signal.SIGKILL)
        self.assertEqual(process.communicate.call_count, 2)
        self.assertEqual(result, (124, "partial output", "partial error"))

    def test_timeout_already_exited_process_still_reaped(self):
        process = mock.Mock(pid=23456)
        process.communicate.side_effect = [subprocess.TimeoutExpired(cmd="codex", timeout=1), ("", "")]
        with mock.patch.object(reader.subprocess, "Popen", return_value=process), mock.patch.object(reader.os, "killpg", side_effect=ProcessLookupError):
            self.assertEqual(reader.run_codex(["codex"], "prompt", "/tmp/fresh", 1)[0], 124)


if __name__ == "__main__":
    unittest.main()
