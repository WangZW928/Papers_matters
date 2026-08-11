# Cross-Review: CODEX_DEEP_READ.md × 学习路线规划.md

Date: 2026-08-11  
Reviewer: Codex

## Summary (3-5 sentences)

两份文档的显式 Markdown 相对文件链接均可解析到现有文件：`CODEX_DEEP_READ.md` 共 49 个相对文件链接，`学习路线规划.md` 共 25 个相对文件链接，未发现 broken file link。`CODEX_DEEP_READ.md` 的 Tier 正文计数准确：Tier 1=5、Tier 2=7、Tier 3=37、总计 49；但同一文件头部的“审查范围：321 篇”无法由当前仓库文件树直接验证。`学习路线规划.md` Part 2 共 38 个编号推荐项，其中 25 项可对应到 `CODEX_DEEP_READ.md` 的 Tier 条目，13 项没有 deep-read index 条目。主要问题是路线规划状态过期：FNO、ML-Accelerated CFD、Text2PDE 已经入库并进入 Tier 3，但文档仍写“待入库”。

## Critical issues

1. `学习路线规划.md` 多处“待入库”状态已经过期。  
   Evidence: `学习路线规划.md:126` 写 `Fourier Neural Operator... 待入库`，但 `CODEX_DEEP_READ.md:214-215` 已列为 Tier 3 #46，且文件 `ai-for-physics/fourier-neural-operator-for-parametric-partial-differential-equations.md` 存在，文件头 `:1-8` 显示“阅读状态：精读 / 流程状态...提交”。`学习路线规划.md:228` 写 `Machine Learning-Accelerated Computational Fluid Dynamics` 待入库，但 `CODEX_DEEP_READ.md:219-220` 已列为 Tier 3 #47，文件头 `ai-for-physics/machine-learning-accelerated-computational-fluid-dynamics.md:1-8` 同样显示精读完成。`学习路线规划.md:391` 写 `Text2PDE...` 待入库，但 `CODEX_DEEP_READ.md:224-225` 已列为 Tier 3 #48，文件头 `ai-for-physics/text2pde-latent-diffusion-models-for-accessible-physics-simulation.md:1-8` 显示精读完成。

2. `学习路线规划.md` Part 2 的推荐清单与 deep-read index 覆盖不一致。  
   Evidence: Part 2 编号 1-38 连续，其中至少 13 项没有 `CODEX_DEEP_READ.md` Tier 条目：`Vortex Line and Ring Dynamics...` (`学习路线规划.md:77`), `Physics-informed Machine Learning` (`:109`), `Neural Operator: Learning Maps...` (`:129`), `Learning Mesh-Based Simulation with Graph Networks` (`:179`), `Attention Is All You Need` (`:233`), `Score-Based Generative Modeling through Stochastic Differential Equations` (`:263`), `Quantum Transport...Tracy-Widom Distribution` (`:325`), `An Unstructured Block-Based AMR...DG Method` (`:344`), `Parthenon-VIBE` (`:354`), `Warped Spacelike Singularities...` (`:394`) 等。反向看，`CODEX_DEEP_READ.md` 的若干 Tier 2 核心条目没有作为 Part 2 推荐项出现，例如 `Covector Fluids` (`CODEX_DEEP_READ.md:38`), `SINDy` (`:44`), `Spectral analysis...Koopman/DMD` (`:47`), `Schrödinger's Smoke` (`:53`), `Quantum Simulation...Schrödingerization` (`:56`)。

3. 仓库规模数字互相冲突，且均不能直接由当前文件树验证。  
   Evidence: `CODEX_DEEP_READ.md:3` 写“审查范围：321 篇”；`学习路线规划.md:3` 写“仓库当前覆盖约 318 篇论文”；`CODEX_REVIEW.md:3` 写“318 篇有摘要的论文”；`README.md:376` 写“总计: 317 篇论文”。当前文件系统计数为：`find . -type f -name '*.md' | wc -l` = 371；排除 README、CODEX/审查文档、docs 后的论文 Markdown 约 362。除非另有隐藏的“有摘要/已审查/已跳过”口径，321/318/317 都无法由当前仓库状态直接复现。

4. `学习路线规划.md:24` 对 `Hamiltonian description of the ideal fluid` 写“建议继续精读”，但该论文已是 `CODEX_DEEP_READ.md:11-12` Tier 1 #1。  
   这不一定是事实错误，如果“继续精读”表示反复研读；但作为状态词，它容易被读成尚未完成精读，和 deep-read index 的已精读定位冲突。

## Broken links

| Paper title | doc | link as written | status |
|---|---|---|---|
| 无 | `CODEX_DEEP_READ.md` | 49 个相对文件链接全部存在 | OK |
| 无 | `学习路线规划.md` | 25 个相对文件链接全部存在 | OK |

Filename mismatch notes:

- 未发现“链接路径不存在但相近文件存在”的 filename mismatch。
- 有重复/平行副本但不是 broken link：`Inside Fluids` 同时存在 `vortex-dynamics/inside-fluids-clebsch-maps-for-visualization-and-processing.md` 与 `geometric-fluid/clebsch-maps-for-visualization-and-processing/inside-fluids-clebsch-maps-for-visualization-and-processing.md`；文档链接到前者，路径有效。
- `Schrödinger's Smoke` 也有多个副本路径，`CODEX_DEEP_READ.md:53-54` 链接的 `geometric-fluid/schrödingers-smoke.md` 存在。

## Coverage gaps

Part 2 recommended papers mapped against `CODEX_DEEP_READ.md`:

| # | Recommended paper | Status in CODEX_DEEP_READ |
|---:|---|---|
| 1 | Hamiltonian description of the ideal fluid | Tier 1 #1 (`CODEX_DEEP_READ.md:11`) |
| 2 | Noncanonical Hamiltonian Density Formulation of Hydrodynamics and Ideal Magnetohydrodynamics | Tier 3 #28, title shortened as `...Ideal MHD` (`:123`) |
| 3 | Geometric Hydrodynamics via Madelung Transform | Tier 1 #2 (`:16`) |
| 4 | The Madelung Transform as a Momentum Map | Tier 3 #34 (`:153`) |
| 5 | Inside Fluids: Clebsch Maps for Visualization and Processing | Tier 1 #5 (`:31`) |
| 6 | Hamiltonian Structure, Symmetries and Conservation Laws for Water Waves | Tier 3 #43, title shortened as `Hamiltonian Structure of Water Waves` (`:199`) |
| 7 | Vortex Line and Ring Dynamics in Trapped Bose-Einstein Condensates | MISSING entirely |
| 8 | Universal Anomalous Diffusion of Quantized Vortices in Ultraquantum Turbulence | Tier 3 #42, title shortened (`:194`) |
| 9 | Physics-informed Neural Networks... | Tier 1 #3, title shortened as `Physics-informed neural networks (PINN)` (`:21`) |
| 10 | Physics-informed Machine Learning | MISSING as Karniadakis et al. 2021 review; repo has same-prefix but different papers |
| 11 | Fourier Neural Operator for Parametric PDEs | Tier 3 #46 (`:214`); stale “待入库” in plan |
| 12 | Neural Operator: Learning Maps Between Function Spaces... | MISSING; CODEX has GKN #7 and FNO #46, not this JMLR theory paper |
| 13 | Hamiltonian Neural Networks | Tier 3 #39 (`:179`) |
| 14 | Machine Learning Hidden Symmetries | Tier 3 #40 (`:184`) |
| 15 | Denoising Diffusion Probabilistic Models | Tier 3 #18 (`:76`) |
| 16 | A Physics-informed Diffusion Model... | Tier 3 #41, title shortened (`:189`) |
| 17 | Learning Mesh-Based Simulation with Graph Networks | MISSING entirely |
| 18 | Jacobian-free Newton-Krylov Methods... | Tier 1 #4 (`:26`) |
| 19 | AmgX... | Tier 3 #45, title shortened (`:209`) |
| 20 | Multigrid for Matrix-Free High-Order FEM on GPUs | Tier 2 #10 (`:50`) |
| 21 | Machine Learning-Accelerated CFD | Tier 3 #47 (`:219`); stale “待入库” in plan |
| 22 | Attention Is All You Need | Listed only as relation text (`CODEX_DEEP_READ.md:131`), no Tier entry |
| 23 | Neural Tangent Kernel... | Tier 3 #35 (`:158`) |
| 24 | Deep Equilibrium Models | Tier 3 #36 (`:163`) |
| 25 | Score-Based Generative Modeling through SDEs | MISSING entirely |
| 26 | Graph Neural Networks: A Review... | Tier 3 #37 (`:168`) |
| 27 | Geometric Deep Learning... | Tier 3 #30 (`:133`) |
| 28 | On the Electrodynamics of Moving Bodies | Tier 3 #32 (`:143`) |
| 29 | On the Relativity Principle... | Tier 3 #38 (`:173`) |
| 30 | Diffusion Equation Is Compatible with Special Relativity | Tier 3 #44 (`:204`) |
| 31 | Quantum Transport...Tracy-Widom Distribution | MISSING entirely |
| 32 | An Unstructured Block-Based AMR Approach for DG Method | MISSING entirely |
| 33 | Characterizing AMR on Heterogeneous Platforms with Parthenon-VIBE | MISSING entirely |
| 34 | Quantum Mechanical Closure of PDEs with Symmetries | Tier 3 #31, title shortened (`:138`) |
| 35 | PDE-Transformer... | Tier 3 #29 (`:128`) |
| 36 | Text2PDE... | Tier 3 #48 (`:224`); stale “待入库” in plan |
| 37 | Warped Spacelike Singularities... | MISSING entirely |
| 38 | A Geometric Derivation of the Einstein Equations... | Tier 3 #33 (`:148`) |

Coverage gaps that are “recommended but missing from deep-read index”:

- `Vortex Line and Ring Dynamics in Trapped Bose-Einstein Condensates` (`学习路线规划.md:77-85`)
- `Physics-informed Machine Learning` / Karniadakis et al. 2021 Nat Rev Phys (`:109-117`)
- `Neural Operator: Learning Maps Between Function Spaces with Applications to PDEs` (`:129-137`)
- `Learning Mesh-Based Simulation with Graph Networks` (`:179-187`)
- `Attention Is All You Need` (`:233-241`) — mentioned in CODEX relation text only, not a Tier entry
- `Score-Based Generative Modeling through Stochastic Differential Equations` (`:263-271`)
- `Quantum Transport in Interacting Spin Chains: Exact Derivation of the Tracy-Widom Distribution` (`:325-333`)
- `An Unstructured Block-Based Adaptive Mesh Refinement Approach for Discontinuous Galerkin Method` (`:344-352`)
- `Characterizing Adaptive Mesh Refinement on Heterogeneous Platforms with Parthenon-VIBE` (`:354-362`)
- `Warped Spacelike Singularities and the C^0-Inextendibility of Birmingham-Kottler Spacetimes` (`:394-402`)

## Minor issues / suggestions

- `CODEX_DEEP_READ.md` Tier counts are correct only if parsing stops before `## 阅读路线图`; a naive numbered-list parser counts roadmap items too and gets 56. This is not a rendering bug, but if machine parsing matters, consider using non-numbered bullets in the roadmap or adding a clearer metadata block.
- `README.md:3` still says “Codex 精读排名 — 18 篇推荐” while `CODEX_DEEP_READ.md:1` is now “49 篇论文排名”。This is outside the two target docs but is part of the repository state and will mislead navigation.
- `学习路线规划.md:483` says “把 `CODEX_DEEP_READ.md` 的 18 篇重新打标签”，but `CODEX_DEEP_READ.md` currently contains 49 Tier entries. This near-term checklist is stale.
- Part 4 Foundation (`学习路线规划.md:451`) includes `Attention` even though it is neither in repo nor in the deep-read Tier list, while several Tier 2 backbone papers (`Covector Fluids`, `SINDy`, `Spectral analysis`, `Schrödingerization`) are not explicitly scheduled there. If Part 4 is meant to implement the deep-read priority structure, it should either explain this deliberate override or align phases with Tier 1/2 first.
- `学习路线规划.md:335-342` lists “Physical Review Letters Collection of the Year 2025” as an unnumbered front-edge index between numbered papers #31 and #32. It renders, but it is neither a paper nor part of the 1-38 count; mark it explicitly as “非论文索引，不纳入 Part 2 编号/coverage 统计” to avoid count ambiguity.
- Content-quality check: `Physics-informed Machine Learning` is ambiguous against actual repo state. The repository has `ai-for-physics/physics-informed-machine-learning-approach-for-augmenting-turbulence-models-a-co.md` and `ai-for-physics/physics-informed-machine-learning-of-the-lagrangian-dynamics-of-velocity-gradien.md`, but their headers show Wu 2018 and Tian 2021 PR Fluids papers, not Karniadakis et al. 2021 Nat Rev Phys. The plan should either add the exact target file after import or avoid treating the phrase as if it uniquely identifies a repo document.
- Formatting check: neither target document contains fenced code blocks, so no unbalanced code fence was found. Part 2 numbering is continuous 1-38. No broken markdown table was found in the two target docs.

## Verdict

Needs fixes.

Must-do fixes:

1. Update stale “待入库” statuses for FNO (`学习路线规划.md:126`), ML-Accelerated CFD (`:228`), and Text2PDE (`:391`) to reflect that they are now Tier 3 deep-read entries with existing files.
2. Reconcile repository/paper count claims: `CODEX_DEEP_READ.md:3` 321, `学习路线规划.md:3` 318, `CODEX_REVIEW.md:3` 318, and `README.md:376` 317 currently use inconsistent and unverifiable counts.
3. Fix the near-term checklist item `学习路线规划.md:483` from “18 篇” to the current 49-entry reality, or explicitly scope it to an older 18-paper subset.
4. Decide whether Part 2 is allowed to recommend papers not yet in `CODEX_DEEP_READ.md`; if yes, label them consistently as “待入库/待精读”； if no, add missing entries or remove them from the deep-read-aligned roadmap.

Approve only after the stale statuses and count/scope inconsistencies are corrected.
