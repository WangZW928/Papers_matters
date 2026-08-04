# Codex 精读推荐 — 27 篇论文排名

**日期：** 2026-08-03（2026-08-04 追加：Berger-Colella AMR +70,977、WarpX GPU 移植 +81,317、ECM 模型 +81,101、Roofline +89,794、Hong-Kung I/O +65,718、Work-Stealing +83,820 tokens、BoxLib with Tiling 精读收尾（Token 未单独记录，见 2026-08-03 commit 6b0ff70）） | **审查范围：** 321 篇 | **Token：** 768,000

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

## Tier 3 — 扩展阅读（15 篇）

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
    - 文件：[`differential-geometry/discrete-variational-calculus-for-double-bracket-dissipation.md`](differential-geometry/discrete-variational-calculus-for-double-bracket-dissipation.md)
    - 数理基础：forced Euler-Poincaré / forced Lie-Poisson 系统的离散变分积分器，几何积分器精确保守伴随轨道 + 能量耗散
    - 为什么精读：在"几何耗散系统 + Lie-Poisson 结构 + 保结构算法"三者交叉点，核心启发——耗散不必破坏几何约束，只要耗散项写成余伴随方向，轨道可保持而能量可下降。离散层面把每步更新设计为精确 \(Ad^*\) 作用。关联：Hamiltonian ideal fluid、LPNets、Covector Fluids

20. **Local Adaptive Mesh Refinement for Shock Hydrodynamics** — HPC
    - 文件：[`HPC/local-adaptive-mesh-refinement-for-shock-hydrodynamics.md`](HPC/local-adaptive-mesh-refinement-for-shock-hydrodynamics.md)
    - 数理基础：块结构 AMR 源头框架——嵌套矩形网格层级、空间/时间同比例细化（subcycling）、守恒 reflux 修正（δF 通量寄存器）、Richardson 局部截断误差估计、bisection+merge 聚类、proper nesting 不变量
    - 为什么精读：Berger-Colella 1989 是 AMReX/BoxLib 整个块结构 AMR 谱系的奠基论文，reflux、average-down、subcycling、tagging、Berger-Rigoutsos 聚类的思想均源于此，对 HPC/AMR 框架设计与冲击动力学模拟有直接价值。关联：AMReX、BoxLib with Tiling、JFNK Survey

21. **BoxLib with Tiling: An AMR Software Framework** — HPC
    - 文件：[`HPC/boxlib-with-tiling-amr-software-framework.md`](HPC/boxlib-with-tiling-amr-software-framework.md)
    - 数理基础：tiling 循环变换下沉到框架层——MFIter/tilebox 逻辑切分（不改变 FArrayBox 布局）、OpenMP tile 静态调度、thread-private memory arena、cache/TLB/NUMA 性能模型、TiDA regional tiling（NUMA-aware，future work）、SMC 8 阶 stencil 跨 9 cells 性能实测
    - 为什么精读：AMReX 的直接前身（作者高度重叠）——展示"数据结构、执行粒度、通信模式、内存分配、应用接口"一起设计的框架哲学，tiling 经验直接演化进 AMReX 的 MFIter + GPU backend；对高性能 PDE 框架设计有架构参考价值。关联：AMReX、Berger-Colella AMR、WarpX GPU 移植
22. **AMReX: Block-structured AMR for multiphysics applications** — HPC
    - 文件：[`HPC/amrex-block-structured-amr-for-multiphysics-applications.md`](HPC/amrex-block-structured-amr-for-multiphysics-applications.md)
    - 数理基础：Block-structured AMR、Berger-Rigoutsos 聚类、Morton SFC 负载均衡、AMR subcycling/reflux 守恒、particle-mesh 插值沉积、cut-cell EB 离散、geometric multigrid、性能可移植抽象层
    - 为什么精读：展示成熟 HPC 框架的分层抽象范式——把 AMR、粒子、EB、multigrid、GPU portability、MPI 通信放进统一框架；对高性能 PDE/流体计算框架设计有直接架构参考价值。关联：JFNK Survey、Matrix-Free Multigrid、AmgX

23. **Porting WarpX to GPU-accelerated platforms** — HPC
    - 文件：[`HPC/porting-warpx-to-gpu-accelerated-platforms.md`](HPC/porting-warpx-to-gpu-accelerated-platforms.md)
    - 数理基础：电磁 PIC 的 GPU 移植——AMReX ParallelFor 性能可移植层（CUDA/HIP/DPC++）、MultiFab/ParticleContainer 数据布局、gather+push kernel 融合（footprint 1.6×、+25%）、memory arena、粒子排序、SFC/knapsack 动态负载均衡、KPP-1 FOM 基准（2.2e10 → 2.5e12）
    - 为什么精读：AMReX 生态应用落地的样板——单代码库性能可移植如何实现、GPU 内存足迹优先的优化方法论、以整机 FOM 为准的调优观；对高性能框架设计有直接工程价值。关联：AMReX、BoxLib with Tiling、Berger-Colella AMR

24. **Roofline: An Insightful Visual Performance Model for Multicore Architectures** — HPC
    - 文件：[`HPC/roofline-an-insightful-visual-performance-model-for-multicore-architectures.md`](HPC/roofline-an-insightful-visual-performance-model-for-multicore-architectures.md)
    - 数理基础：操作强度 I（flops/byte DRAM 流量）、roofline 不等式 P ≤ min(P_peak, B·I)、ridge point、3C 缓存模型对接、SpMV 带宽受限分析、实测 STREAM/LINPACK 屋顶
    - 为什么精读：HPC 性能分析事实标准——一张图回答“计算受限 vs 带宽受限”，为 WarpX/ECM/AMR 内核优化提供统一判断框架。关联：WarpX GPU 移植、ECM 模型、Berger-Colella AMR

25. **Quantifying Performance Bottlenecks of Stencil Computations Using the ECM Model** — HPC
    - 文件：[`HPC/quantifying-performance-bottlenecks-of-stencil-computations-using-the-execution-cache-memory-model.md`](HPC/quantifying-performance-bottlenecks-of-stencil-computations-using-the-execution-cache-memory-model.md)
    - 数理基础：ECM 可加性预测模型（执行部分 + L1/L2/L3/DRAM 数据部分）、layer condition 流量判定、空间/时间分块与强度削减的收益预测、多核扩展外推
    - 为什么精读：从“上界图”（Roofline）到“可加预测”的进阶——stencil/AMR 内核优化前先建模，避免试错；layer condition 思想对数据流量分析有通用价值。关联：Roofline、AMReX、Berger-Colella AMR

26. **I/O Complexity: The Red-Blue Pebble Game** — HPC
    - 文件：[`HPC/io-complexity-the-red-blue-pebble-game.md`](HPC/io-complexity-the-red-blue-pebble-game.md)
    - 数理基础：红蓝鹅卵石博弈形式化、S-partitioning 下界技术、FFT Ω(n log n/log S)、矩阵乘法 Ω(n³/√S)、下界可达性；I/O 复杂度理论奠基
    - 为什么精读：memory wall 的理论根基——分块/循环变换为何最优的严格答案；与 Aggarwal-Vitter I/O 模型、communication-avoiding 算法一脉相承，是性能模型主线的理论底座。关联：Roofline、ECM 模型、JFNK Survey

27. **Scheduling Multithreaded Computations by Work Stealing** — HPC
    - 文件：[`HPC/scheduling-multithreaded-computations-by-work-stealing.md`](HPC/scheduling-multithreaded-computations-by-work-stealing.md)
    - 数理基础：fully strict 多线程 DAG、T1/T∞ 测度、随机化工作窃取、busy-leaves property、recycling game、时间界 T1/P+O(T∞)、空间界 S1P、通信界 O(PT∞(1+nd)Smax)
    - 为什么精读：任务并行调度理论基石（Cilk/TBB/OpenMP tasking）——动态负载均衡的最优性论证，与 AMReX SFC/knapsack 静态均衡互补，为高性能框架的并行调度层提供理论依据。关联：AMReX、WarpX GPU 移植

## 阅读路线图

1. **几何/变分基础先行** → Hamiltonian ideal fluid → Madelung transform → Schrödinger's Smoke → Inside Fluids
2. **结构保持与涡方法** → Covector Fluids → Vortex Segment Clouds → Lie-Poisson Neural Networks
3. **PDE 学习主线** → PINN → Neural Operator → SINDy → DMD/Koopman → DDPM
4. **HPC 求解器主线** → JFNK Survey → Matrix-Free High-Order FEM Multigrid → Berger-Colella AMR (1989) → BoxLib with Tiling (2016) → AMReX → WarpX GPU 移植 → AmgX → GPU GMRES
    - 支撑：Roofline（性能上界）→ ECM 模型（可加预测）→ Hong-Kung I/O 复杂度（理论底座）→ Work-Stealing 调度（任务并行）
5. **前沿交叉补强** → Schrödingerization PDE → Force-Free Fields → Extended Lagrangian → Log-conformation viscoelastic
6. **几何耗散系统** → Double-Bracket Dissipation（刚体 → 未来理想流体推广）

---

*覆盖 10 个分类 | 每篇均关联库内至少 1 篇其他论文 | 27/27 文件已链接*
