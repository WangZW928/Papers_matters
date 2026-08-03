# Codex 精读推荐 — 19 篇论文排名

**日期：** 2026-08-03 | **审查范围：** 320 篇 | **Token：** 200,400

> 🔗 **GitHub 仓库：** [WangZW928/Papers_matters](.)

---

## Tier 1 — 必读（5 篇）

1. **Hamiltonian description of the ideal fluid** — geometric-fluid
   - 文件：[`geometric-fluid/hamiltonian-description-of-the-ideal-ﬂuid.md`](geometric-fluid/hamiltonian-description-of-the-ideal-ﬂuid.md)
   - 数理基础：理想流体非正则 Hamiltonian/Poisson 结构的核心源头，是理解 Lie-Poisson、Casimir、不变量和稳定性理论的底座。
   - 为什么精读：几何流体、结构保持神经网络、辛/Poisson 离散的母体。关联：Lie-Poisson Neural Networks。

2. **Geometric hydrodynamics via Madelung transform** — geometric-fluid
   - 文件：[`geometric-fluid/geometric-hydrodynamics-via-madelung-transform.md`](geometric-fluid/geometric-hydrodynamics-via-madelung-transform.md)
   - 数理基础：Euler 流 + Madelung 变换 + 波函数几何 + 量子流体，是"经典流体 = 几何/量子表象"的关键桥梁。
   - 为什么精读：几何流体与 Schrödinger/Gross-Pitaevskii 表示的理论入口。关联：Schrödinger's Smoke、NS-GP coupling。

3. **Physics-informed neural networks (PINN)** — ai-for-physics
   - 文件：[`ai-for-physics/physics-informed-neural-networks-a-deep-learning-framework-for-solving-forward-a.md`](ai-for-physics/physics-informed-neural-networks-a-deep-learning-framework-for-solving-forward-a.md)
   - 数理基础：PDE 残差、初边值条件、反问题统一进神经网络优化。
   - 为什么精读：物理约束学习的共同语言。关联：Parallel PINN、BEACONS。

4. **Jacobian-free Newton-Krylov Methods: A Survey** — numerical-computation
   - 文件：[`numerical-computation/jacobian-free-newton-krylov-methods-a-survey-of-approaches-and-applications.md`](numerical-computation/jacobian-free-newton-krylov-methods-a-survey-of-approaches-and-applications.md)
   - 数理基础：Newton-Krylov、Jacobian-vector product、预条件、非线性全局化。
   - 为什么精读：大规模隐式 PDE 求解器基础方法论。关联：GPU GMRES、AmgX。

5. **Inside Fluids: Clebsch Maps for Visualization and Processing** — vortex-dynamics
   - 文件：[`vortex-dynamics/inside-fluids-clebsch-maps-for-visualization-and-processing.md`](vortex-dynamics/inside-fluids-clebsch-maps-for-visualization-and-processing.md)
   - 数理基础：Clebsch 势 + 波函数相位缺陷表示涡结构，天然连接螺旋度、环量、拓扑守恒和 Schrödinger 演化。
   - 为什么精读："涡拓扑 + 量子表象 + 可视化"的方法奠基论文。关联：Schrödinger's Smoke、Clebsch free-surface。

## Tier 2 — 深度阅读（7 篇）

6. **Covector Fluids** — geometric-fluid
   - 文件：[`geometric-fluid/covector-fluids.md`](geometric-fluid/covector-fluids.md)

7. **Neural Operator: Graph Kernel Network** — ai-for-physics
   - 文件：[`ai-for-physics/neural-operator-graph-kernel-network.md`](ai-for-physics/neural-operator-graph-kernel-network.md)

8. **SINDy: Sparse Identification of Nonlinear Dynamics** — ai-for-physics
   - 文件：[`ai-for-physics/discovering-governing-equations-from-data-by-sparse-identification-of-nonlinear-.md`](ai-for-physics/discovering-governing-equations-from-data-by-sparse-identification-of-nonlinear-.md)

9. **Spectral analysis of nonlinear flows (Koopman/DMD)** — fluid-mechanics
   - 文件：[`fluid-mechanics/spectral-analysis-of-nonlinear-flows.md`](fluid-mechanics/spectral-analysis-of-nonlinear-flows.md)

10. **Multigrid for Matrix-Free High-Order FEM on GPUs** — numerical-computation
    - 文件：[`numerical-computation/multigrid-for-matrix-free-high-order-finite-element-computations-on-graphics-pro.md`](numerical-computation/multigrid-for-matrix-free-high-order-finite-element-computations-on-graphics-pro.md)

11. **Schrödinger's Smoke** — geometric-fluid
    - 文件：[`geometric-fluid/schrödingers-smoke.md`](geometric-fluid/schrödingers-smoke.md)

12. **Quantum Simulation of PDEs via Schrödingerization** — quantum-computing
    - 文件：[`quantum-computing/quantum-simulation-of-partial-differential-equations-via-schrödingerization.md`](quantum-computing/quantum-simulation-of-partial-differential-equations-via-schrödingerization.md)

## Tier 3 — 扩展阅读（7 篇）

13. **Lie-Poisson Neural Networks (LPNets)** — ai-for-physics
    - 文件：[`ai-for-physics/liepoisson-neural-networks-lpnets-data-based-computing-of-hamiltonian-systems-wi.md`](ai-for-physics/liepoisson-neural-networks-lpnets-data-based-computing-of-hamiltonian-systems-wi.md)

14. **Force-Free Fields are Conformally Geodesic** — differential-geometry
    - 文件：[`differential-geometry/force-free-fields-are-conformally-geodesic.md`](differential-geometry/force-free-fields-are-conformally-geodesic.md)

15. **Incompressible Flow Simulation on Vortex Segment Clouds** — vortex-dynamics
    - 文件：[`vortex-dynamics/incompressible-flow-simulation-on-vortex-segment-clouds.md`](vortex-dynamics/incompressible-flow-simulation-on-vortex-segment-clouds.md)

16. **Extended Lagrangian approach for multidimensional dispersive waves** — wave-mechanics
    - 文件：[`wave-mechanics/extended-lagrangian-approach-for-the-numerical-study-of-multidimensional-dispers.md`](wave-mechanics/extended-lagrangian-approach-for-the-numerical-study-of-multidimensional-dispers.md)

17. **The log-conformation formulation for viscoelastic flows** — fluid-mechanics
    - 文件：[`fluid-mechanics/粘弹性流体/the-log-conformation-formulation-for-single--and-multi-phase-axisymmetric-viscoe.md`](fluid-mechanics/粘弹性流体/the-log-conformation-formulation-for-single--and-multi-phase-axisymmetric-viscoe.md)

18. **Denoising Diffusion Probabilistic Models** — ai-model
    - 文件：[`ai-model/denoising-diffusion-probabilistic-models.md`](ai-model/denoising-diffusion-probabilistic-models.md)

19. **Discrete variational calculus for double-bracket dissipation** — differential-geometry

20. **AMReX: Block-structured AMR for multiphysics applications** — HPC
    - 文件：[`HPC/amrex-block-structured-amr-for-multiphysics-applications.md`](HPC/amrex-block-structured-amr-for-multiphysics-applications.md)
    - 数理基础：Block-structured AMR、Berger-Rigoutsos 聚类、Morton SFC 负载均衡、AMR subcycling/reflux 守恒、particle-mesh 插值沉积、cut-cell EB 离散、geometric multigrid、性能可移植抽象层
    - 为什么精读：展示成熟 HPC 框架的分层抽象范式——把 AMR、粒子、EB、multigrid、GPU portability、MPI 通信放进统一框架；对高性能 PDE/流体计算框架设计有直接架构参考价值。关联：JFNK Survey、Matrix-Free Multigrid、AmgX
    - 文件：[`differential-geometry/discrete-variational-calculus-for-double-bracket-dissipation.md`](differential-geometry/discrete-variational-calculus-for-double-bracket-dissipation.md)
    - 数理基础：forced Euler-Poincaré / forced Lie-Poisson 系统的离散变分积分器，几何积分器精确保守伴随轨道 + 能量耗散
    - 为什么精读：在"几何耗散系统 + Lie-Poisson 结构 + 保结构算法"三者交叉点，核心启发——耗散不必破坏几何约束，只要耗散项写成余伴随方向，轨道可保持而能量可下降。离散层面把每步更新设计为精确 \(Ad^*\) 作用。关联：Hamiltonian ideal fluid、LPNets、Covector Fluids

## 阅读路线图

1. **几何/变分基础先行** → Hamiltonian ideal fluid → Madelung transform → Schrödinger's Smoke → Inside Fluids
2. **结构保持与涡方法** → Covector Fluids → Vortex Segment Clouds → Lie-Poisson Neural Networks
3. **PDE 学习主线** → PINN → Neural Operator → SINDy → DMD/Koopman → DDPM
4. **HPC 求解器主线** → JFNK Survey → Matrix-Free High-Order FEM Multigrid → AMReX → AmgX → GPU GMRES
5. **前沿交叉补强** → Schrödingerization PDE → Force-Free Fields → Extended Lagrangian → Log-conformation viscoelastic
6. **几何耗散系统** → Double-Bracket Dissipation（刚体 → 未来理想流体推广）

---

*覆盖 11 个 topic | 每篇均关联库内至少 1 篇其他论文 | 20/20 文件已链接*
