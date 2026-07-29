# Codex 精读推荐 — 18 篇论文排名

**日期：** 2026-07-29 | **审查范围：** 318 篇 | **Token：** 108,002

---

## Tier 1 — 必读（5 篇）

1. **Hamiltonian description of the ideal fluid** — geometric-fluid
   - 文件：`geometric-fluid/hamiltonian-description-of-the-ideal-ﬂuid.md`
   - 数理基础：理想流体非正则 Hamiltonian/Poisson 结构的核心源头，是理解 Lie-Poisson、Casimir、不变量和稳定性理论的底座。
   - 为什么精读：几何流体、结构保持神经网络、辛/Poisson 离散的母体。关联：Lie-Poisson Neural Networks。

2. **Geometric hydrodynamics via Madelung transform** — geometric-fluid
   - 文件：`geometric-fluid/geometric-hydrodynamics-via-madelung-transform.md`
   - 数理基础：Euler 流 + Madelung 变换 + 波函数几何 + 量子流体，是"经典流体 = 几何/量子表象"的关键桥梁。
   - 为什么精读：几何流体与 Schrödinger/Gross-Pitaevskii 表示的理论入口。关联：Schrödinger's Smoke、NS-GP coupling。

3. **Physics-informed neural networks (PINN)** — ai-for-physics
   - 文件：`ai-for-physics/physics-informed-neural-networks-a-deep-learning-framework-for-solving-forward-a.md`
   - 数理基础：PDE 残差、初边值条件、反问题统一进神经网络优化。
   - 为什么精读：物理约束学习的共同语言。关联：Parallel PINN、BEACONS。

4. **Jacobian-free Newton-Krylov Methods: A Survey** — numerical-computation
   - 文件：`numerical-computation/jacobian-free-newton-krylov-methods-a-survey-of-approaches-and-applications.md`
   - 数理基础：Newton-Krylov、Jacobian-vector product、预条件、非线性全局化。
   - 为什么精读：大规模隐式 PDE 求解器基础方法论。关联：GPU GMRES、AmgX。

5. **Inside Fluids: Clebsch Maps for Visualization and Processing** — vortex-dynamics
   - 文件：`vortex-dynamics/inside-fluids-clebsch-maps-for-visualization-and-processing.md`
   - 数理基础：Clebsch 势 + 波函数相位缺陷表示涡结构，天然连接螺旋度、环量、拓扑守恒和 Schrödinger 演化。
   - 为什么精读："涡拓扑 + 量子表象 + 可视化"的方法奠基论文。关联：Schrödinger's Smoke、Clebsch free-surface。

## Tier 2 — 深度阅读（7 篇）

6. **Covector Fluids** — geometric-fluid
7. **Neural Operator: Graph Kernel Network** — ai-for-physics
8. **SINDy: Sparse Identification of Nonlinear Dynamics** — ai-for-physics
9. **Spectral analysis of nonlinear flows (Koopman/DMD)** — fluid-mechanics
10. **Multigrid for Matrix-Free High-Order FEM on GPUs** — numerical-computation
11. **Schrödinger's Smoke** — geometric-fluid
12. **Quantum Simulation of PDEs via Schrödingerization** — quantum-computing

## Tier 3 — 扩展阅读（6 篇）

13. **Lie-Poisson Neural Networks (LPNets)** — ai-for-physics
14. **Force-Free Fields are Conformally Geodesic** — differential-geometry
15. **Incompressible Flow Simulation on Vortex Segment Clouds** — vortex-dynamics
16. **Extended Lagrangian approach for multidimensional dispersive waves** — wave-mechanics
17. **The log-conformation formulation for viscoelastic flows** — fluid-mechanics
18. **Denoising Diffusion Probabilistic Models** — ai-model

## 阅读路线图

1. **几何/变分基础先行** → Hamiltonian ideal fluid → Madelung transform → Schrödinger's Smoke → Inside Fluids
2. **结构保持与涡方法** → Covector Fluids → Vortex Segment Clouds → Lie-Poisson Neural Networks
3. **PDE 学习主线** → PINN → Neural Operator → SINDy → DMD/Koopman → DDPM
4. **HPC 求解器主线** → JFNK Survey → Matrix-Free High-Order FEM Multigrid → AmgX → GPU GMRES
5. **前沿交叉补强** → Schrödingerization PDE → Force-Free Fields → Extended Lagrangian → Log-conformation viscoelastic

---

*覆盖 10 个 topic | 每篇均关联库内至少 1 篇其他论文*
