# Formula Review Summary — 2026-07-29

| # | Paper | Topic | Files Read | $$→\[\] Fixes | Questions Added | Notes |
|---|-------|-------|-----------|---------------|-----------------|-------|
| 1 | Hamiltonian description of the ideal fluid | geometric-fluid | ✓ | 27 blocks | Y (3 Qs) | Lie-Poisson bracket, Casimir, stability |
| 2 | Geometric hydrodynamics via Madelung transform | geometric-fluid | ✓ | 31 blocks | Y (3 Qs) | 1 \[\] block pre-existing, rest fixed |
| 3 | PINN (Raissi 2019) | ai-for-physics | ✓ | 21 blocks | Y (3 Qs) | Strong-form PDE residual framework |
| 4 | Jacobian-free Newton-Krylov: A Survey | numerical-computation | ✓ | 29 blocks | Y (3 Qs) | JFNK, preconditioning, globalisation |
| 5 | Inside Fluids: Clebsch Maps | vortex-dynamics | ✓ | 31 blocks | Y (3 Qs) | S³→S² Clebsch, helicity quantisation |
| 6 | Covector Fluids | geometric-fluid | ✓ | 0 (clean) | Y (3 Qs) | Lie advection of 1-forms |
| 7 | Neural Operator: Graph Kernel Network | ai-for-physics | ✓ | 0 (clean) | Y (3 Qs) | Discretisation-invariant operator learning |
| 8 | SINDy (Brunton 2016) | ai-for-physics | ✓ | 0 (clean) | Y (3 Qs) | Sparse identification of dynamics |
| 9 | Spectral analysis of nonlinear flows | fluid-mechanics | ✓ | 0 (clean) | Y (3 Qs) | Koopman/DMD spectral theory |
| 10 | Multigrid for Matrix-Free High-Order FEM on GPUs | numerical-computation | ✓ | 0 (clean) | Y (3 Qs) | Sum-factorisation, p+h multigrid |
| 11 | Schrödinger's Smoke | geometric-fluid | ✓ | 0 (clean) | Y (3 Qs) | GP→Euler, vortex topology conservation |
| 12 | Quantum Simulation of PDEs via Schrödingerization | quantum-computing | ✓ | 0 (clean) | Y (3 Qs) | Warped phase, unitary evolution |
| 13 | Lie-Poisson Neural Networks (LPNets) | ai-for-physics | ✓ | 0 (clean) | Y (3 Qs) | Structure matrix, Jacobi identity |
| 14 | Force-Free Fields are Conformally Geodesic | differential-geometry | ✓ | 0 (clean) | Y (3 Qs) | Beltrami fields, conformal geometry |
| 15 | Incompressible Flow Simulation on Vortex Segment Clouds | vortex-dynamics | ✓ | 0 (clean) | Y (3 Qs) | Lagrangian vortex method, FMM |
| 16 | Extended Lagrangian approach for dispersive waves | wave-mechanics | ✓ | 0 (clean) | Y (3 Qs) | Hyperbolisation, IMEX for SGN |
| 17 | Log-conformation formulation for viscoelastic flows | fluid-mechanics | ✓ | 0 (clean) | Y (3 Qs) | HWNP solution, axisymmetric extension |
| 18 | Denoising Diffusion Probabilistic Models | ai-model | ✓ | 0 (clean) | Y (3 Qs) | Variational bound, score matching |

## Totals

- **Files reviewed:** 18/18 ✅
- **Files with $$→\[\] conversions:** 5 (papers 1–5)
- **Total display-math blocks fixed:** 139 (27+31+21+29+31)
- **Files with no $$ issues:** 13
- **Files with review questions:** 18/18 (3 questions each, 54 total)
- **Markdown syntax issues found:** 0

## Verification

- ✅ Zero remaining `$$` display math in all 18 files
- ✅ `\[` / `\]` brackets perfectly balanced in all files
- ✅ No unbalanced code fences (backticks)
- ✅ All headings properly formatted
- ✅ All review questions appended under `## Review Questions` heading

## Reviewer Notes

- Papers 1–5 (Tier 1 + Inside Fluids) contained extensive display math using `$$...$$` LaTeX convention; all converted to GitHub MathJax-compatible `\[...\]`.
- Papers 6–18 were either abstract-only or already had limited math content; no `$$` issues found.
- Paper 2 (Madelung transform) had one `\[...\]` block pre-existing alongside `$$...$$` blocks — the latter were all converted.
- Questions focus on conceptual understanding, geometric/mathematical insight, and HPC/numerical implications.
- No push performed — commit only, as instructed.
