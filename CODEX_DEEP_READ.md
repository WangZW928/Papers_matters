# Codex 精读推荐 — 49 篇论文排名

**日期：** 2026-08-03（2026-08-04 追加：Berger-Colella AMR +70,977、WarpX GPU 移植 +81,317、ECM 模型 +81,101、Roofline +89,794、Hong-Kung I/O +65,718、Work-Stealing +83,820 tokens、BoxLib with Tiling 精读收尾（Token 未单独记录）、2026-08-04 六篇精读：Morrison-Greene 1980 / PDE-Transformer / Geometric DL / 量子闭包 / Einstein 1905 / Causal Action；2026-08-04 学习路线规划精读批次 5 篇：Madelung Transform as a Momentum Map / Neural Tangent Kernel / Deep Equilibrium Models / GNN Review (Zhou et al.) / Einstein 1907 相对性原理与推论；2026-08-07 学习路线规划批次 9 篇补精读 + FNO / ML-Accelerated CFD / Text2PDE；2026-08-07 空壳补精读 11 篇（Covector Fluids / Schrödinger's Smoke / Spectral Analysis / Log-Conformation / Vortex Segment Clouds / Extended Lagrangian SGN / GKN / SINDy / LPNets / Force-Free Fields / Schrödingerization）；2026-08-10 精读：Kitaev 任意子容错量子计算（Codex 精读补充 106,276 tokens）） | **审查范围：** 321 篇（截至 2026-08-03） | **当前仓库：** 362 篇论文（2026-08-11 实测，主题目录下论文 Markdown 数） | **Token：** 874,276

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

## Tier 3 — 扩展阅读（37 篇）

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

28. **Noncanonical Hamiltonian Density Formulation of Hydrodynamics and Ideal MHD** — geometric-fluid
    - 文件：[`geometric-fluid/noncanonical-hamiltonian-density-formulation-of-hydrodynamics-and-ideal-magnetohydrodynamics.md`](geometric-fluid/noncanonical-hamiltonian-density-formulation-of-hydrodynamics-and-ideal-magnetohydrodynamics.md)
    - 数理基础：非正则 Poisson 括号三形式（物理变量式/守恒密度式/Fourier 系数式）、Jacobi 恒等式、∇·B=0 条件（含 Errata 修正）、Lie-Poisson 结构原型
    - 为什么精读：Lie-Poisson 括号与 Casimir 理论的最早源头之一（1980），流体+MHD 统一非正则哈密顿表述的范式论文；与 Hamiltonian ideal fluid（1998）构成母女篇，是 LPNets、Covector Fluids 等结构保持方法的物理母体。关联：Hamiltonian ideal fluid、LPNets、Covector Fluids

29. **PDE-Transformer: Efficient and Versatile Transformers for Physics Simulations** — ai-for-physics
    - 文件：[`ai-for-physics/pde-transformer-efficient-and-versatile-transformers-for-physics-simulations.md`](ai-for-physics/pde-transformer-efficient-and-versatile-transformers-for-physics-simulations.md)
    - 数理基础：DiT 式 Transformer 架构、物理通道独立时空 token 嵌入、通道间自注意力、16 类 PDE 联合预训练、基础模型迁移
    - 为什么精读：物理模拟基础模型的 Transformer 骨干设计——"通道独立 token + 通道间注意力"解决多 PDE 联合学习的信息密度失衡；对 PDE 代理模型与生成式模拟（DDPM 类）的规模化有直接参考。关联：DDPM、Attention Is All You Need、Neural Operator

30. **Geometric Deep Learning: Grids, Groups, Graphs, Geodesics, and Gauges** — ai-theory
    - 文件：[`ai-theory/geometric-deep-learning-grids-groups-graphs-geodesics-and-gauges.md`](ai-theory/geometric-deep-learning-grids-groups-graphs-geodesics-and-gauges.md)
    - 数理基础：对称群与不变性公理、G-等变/不变层、域 Ω 与信号空间 X(Ω)、群表示论、CNN/GNN/流形/规范等变统一蓝图
    - 为什么精读：几何深度学习的统一纲领——把网格、图、流形、规范丛上的架构统一为"域对称群 + 权重共享"原理；为等变 PINN、SE(3) 等变模型、规范场学习方法提供理论框架。关联：PINN、Attention、GNN Review

31. **Quantum Mechanical Closure of PDEs with Symmetries** — quantum-mechanics
    - 文件：[`quantum-mechanics/quantum-mechanical-closure-of-partial-differential-equations-with-symmetries.md`](quantum-mechanics/quantum-mechanical-closure-of-partial-differential-equations-with-symmetries.md)
    - 数理基础：量子力学嵌入（密度算子表示未解析自由度）、量子测量预测反馈、保正离散化、对称性不变压缩表示、核方法/延迟嵌入/迁移算子、浅水方程闭包
    - 为什么精读：用量子密度算子语言做动力系统统计闭包的新范式——与 Schrödingerization（量子算法求解 PDE）互补，偏"量子算子语言组织统计闭包"；对湍流/大气/海洋参数化有方法论价值。关联：Schrödingerization、SINDy/Koopman、PINN

32. **On the Electrodynamics of Moving Bodies (Einstein 1905)** — relativity
    - 文件：[`relativity/on-the-electrodynamics-of-moving-bodies.md`](relativity/on-the-electrodynamics-of-moving-bodies.md)
    - 数理基础：相对性原理 + 光速不变公设、同时性操作定义、洛伦兹变换推导（φ(v)φ(-v)=1）、速度合成、长度收缩/时间膨胀、光能变换、电子纵/横质量
    - 为什么精读：狭义相对论奠基原文——从操作定义到全部运动学/电动力学推论的自洽推导链；为理解协变方程结构（如扩散方程的洛伦兹不变性讨论）提供第一性视角。关联：Diffusion Equation Compatible with SR、Hamiltonian ideal fluid（协变性）

33. **A Geometric Derivation of the Einstein Equations from the Causal Action Principle** — differential-geometry
    - 文件：[`differential-geometry/a-geometric-derivation-of-the-einstein-equations-from-the-causal-action-principle.md`](differential-geometry/a-geometric-derivation-of-the-einstein-equations-from-the-causal-action-principle.md)
    - 数理基础：因果变分原理、因果费米子系统、osculating vacua、Lagrangian 诱导 Lorentz 度量、Euler-Lagrange → Einstein 方程推导链、引力常数 = 正则化长度²、修正项程序
    - 为什么精读：从底层量子变分原理几何推导宏观引力——连接几何与物理前沿；变分原理推导场方程的完整范例，与 Hamiltonian 变分原理、Force-Free Fields 的几何方法呼应。关联：Force-Free Fields、Einstein 1905、Geometric DL（规范几何）

34. **The Madelung Transform as a Momentum Map** — geometric-fluid
    - 文件：[`geometric-fluid/the-madelung-transform-as-a-momentum-map.md`](geometric-fluid/the-madelung-transform-as-a-momentum-map.md)
    - 数理基础：波函数空间实 Hermite 内积与 NLS Poisson 括号、半直积群 Diff(Rⁿ)⋉H^∞ 作用、动量映射定义与无穷小等变性、Lie-Poisson 可压流体括号、量子压 Δ√ρ/(2√ρ)、Clebsch/symplectic realization
    - 为什么精读：把 Madelung 变换从“代数代换”提升为动量映射/Poisson 映射——量子-经典流体对应的几何力学机制，为 HNN/LPNets 双坐标（辛波函数 vs Lie-Poisson 流体）学习提供结构桥。关联：Geometric hydrodynamics via Madelung transform、Morrison-Greene 1980、Clebsch Maps、Schrödinger's Smoke

35. **Neural Tangent Kernel: Convergence and Generalization in Neural Networks** — ai-theory
    - 文件：[`ai-theory/neural-tangent-kernel-convergence-and-generalization-in-neural-networks.md`](ai-theory/neural-tangent-kernel-convergence-and-generalization-in-neural-networks.md)
    - 数理基础：无限宽极限、NNGP 核递推、NTK 定义与层递推（Θ=Σ̇Θ+Σ）、核梯度流 ∂ₜf=-Θ∇C、训练中核不变、正定性（球面+非多项式激活）、谱分解 e^{-ηΛt} 与谱偏置、lazy training 线性化
    - 为什么精读：训练动力学与泛化的核语言统一框架——直接解释 PINN 多尺度/刚性 PDE 的收敛失败与 NTK 自适应加权，为物理约束网络提供诊断工具。关联：PINN、NSFnets、HNN/LPNets、Geometric DL、DDPM

36. **Deep Equilibrium Models** — ai-model
    - 文件：[`ai-model/deep-equilibrium-models.md`](ai-model/deep-equilibrium-models.md)
    - 数理基础：不动点/求根（Broyden 拟牛顿、Anderson 加速）、隐式微分 dz*/dθ = (I-J_f)^{-1}∂f/∂θ、Neumann 级数与谱半径条件、Jacobian-free 反向线性系统 (I-J_f^T)u=v、内存 O(1)
    - 为什么精读：把“网络层 = 非线性方程求解”范例化——与 JFNK/Newton-Krylov、隐式时间步进/稳态 PDE 求解直接对应，是可微隐式求解器与深度学习的共同接口。关联：JFNK Survey、PINN、DDPM、NTK、Geometric DL

37. **Graph Neural Networks: A Review of Methods and Applications** — ai-model
    - 文件：[`ai-model/graph-neural-networks-a-review-of-methods-and-applications.md`](ai-model/graph-neural-networks-a-review-of-methods-and-applications.md)
    - 数理基础：消息传递/传播-采样-池化流水线、谱域（Laplacian 特征分解、ChebNet、GCN 一阶近似）与空间域（GraphSAGE、GAT、MPNN）、GAE/VGAE、时空 GNN、1-WL 表达力上限与过平滑
    - 为什么精读：GNN 分类体系的地基综述——直接支撑 MeshGraphNet/物理网格学习（不规则网格→图、AMR 层次图、conservative transfer），并与 Geometric DL 等变、NTK 谱、DEQ 不动点传播衔接。关联：Geometric DL、Graph Kernel Network、DEQ、NTK、AMReX/BoxLib

38. **On the Relativity Principle and the Conclusions Drawn from It (Einstein 1907)** — relativity
    - 文件：[`relativity/on-the-relativity-principle-and-the-conclusions-drawn-from-it.md`](relativity/on-the-relativity-principle-and-the-conclusions-drawn-from-it.md)
    - 数理基础：洛伦兹变换与 SR 系统化（收缩/膨胀/速度叠加/多普勒/纵横质量）、加速系时间 σ=τ(1+ax'/c²)、等效原理 Φ=ax'、引力红移 Δν/ν=-GM/(c²r)、能量引力质量 E/c²
    - 为什么精读：从 SR 通往 GR 的过渡枢纽——等效原理、引力红移、能量有重量的原始出处；与库内 Einstein 1905 篇直接衔接，为相对论协变性建模知识链补上关键一环。关联：Einstein 1905、SR 流体 Hamilton 原理、Einstein 方程几何推导


39. **Hamiltonian Neural Networks** — ai-for-physics
    - 文件：[`ai-for-physics/hamiltonian-neural-networks.md`](ai-for-physics/hamiltonian-neural-networks.md)
    - 数理基础：Hamiltonian 向量场 $\dot x=J\nabla H$ 的结构先验、能量守恒、辛积分器、正则坐标
    - 为什么精读：结构保持神经网络的代表——把 Hamiltonian 结构作为网络架构约束而非软惩罚，与 LPNets、Covector Fluids、Hamiltonian ideal fluid 直接衔接。关联：LPNets、Hamiltonian ideal fluid、NTK

40. **Machine Learning Hidden Symmetries** — ai-for-physics
    - 文件：[`ai-for-physics/machine-learning-hidden-symmetries.md`](ai-for-physics/machine-learning-hidden-symmetries.md)
    - 数理基础：对称变换群、可逆神经变换、守恒量发现、$\mathcal A(\theta)=|\mathcal L_\xi T_\theta|^2$ asymmetry loss
    - 为什么精读：把隐藏对称性发现形式化为可逆坐标变换学习——与 Geometric DL 等变、Clebsch 变量、Hamiltonian 结构学习交叉。关联：Geometric DL、HNN、Clebsch Maps

41. **Physics-Informed Diffusion Model for Flow Field Reconstruction** — ai-for-physics
    - 文件：[`ai-for-physics/a-physics-informed-diffusion-model-for-high-fidelity-flow-field-reconstruction.md`](ai-for-physics/a-physics-informed-diffusion-model-for-high-fidelity-flow-field-reconstruction.md)
    - 数理基础：条件扩散模型、PDE residual guidance、物理场重建、去噪采样
    - 为什么精读：把扩散模型的生成能力与物理残差约束结合的范式——DDPM 的物理约束版，对湍流场重建、超分有直接价值。关联：DDPM、Text2PDE、PINN

42. **Universal Anomalous Diffusion of Quantized Vortices** — fluid-mechanics
    - 文件：[`fluid-mechanics/universal-anomalous-diffusion-of-quantized-vortices-in-ultraquantum-turbulence.md`](fluid-mechanics/universal-anomalous-diffusion-of-quantized-vortices-in-ultraquantum-turbulence.md)
    - 数理基础：GPE 涡线动力学、MSD 输运统计、重联事件、Kelvin 波、反常扩散指数
    - 为什么精读：量子湍流涡线输运的核心实验/数值工作——连接 Doctor 的量子涡与统计物理主线。关联：Inside Fluids、Vortex Segment Clouds

43. **Hamiltonian Structure of Water Waves (Benjamin-Olver)** — geometric-fluid
    - 文件：[`geometric-fluid/hamiltonian-structure-symmetries-and-conservation-laws-for-water-waves.md`](geometric-fluid/hamiltonian-structure-symmetries-and-conservation-laws-for-water-waves.md)
    - 数理基础：Zakharov 正则变量、Dirichlet-Neumann 算子、水波 Hamiltonian 结构、对称性与守恒律
    - 为什么精读：自由面水波 Hamiltonian 化的奠基工作——几何流体方法在自由边界问题的典范。关联：Hamiltonian ideal fluid、Madelung transform

44. **Diffusion Equation Is Compatible with Special Relativity** — wave-mechanics
    - 文件：[`wave-mechanics/diffusion-equation-is-compatible-with-special-relativity.md`](wave-mechanics/diffusion-equation-is-compatible-with-special-relativity.md)
    - 数理基础：相对论动理论 lift、Vlasov-Fokker-Planck、因果稳定解类、扩散方程协变性
    - 为什么精读：从动理论视角重新审视抛物方程因果性——连接相对论（Einstein 1905）与扩散/耗散系统。关联：Einstein 1905、DDPM（扩散视角）

45. **AmgX: GPU-Accelerated Algebraic Multigrid** — numerical-computation
    - 文件：[`numerical-computation/amgx-a-library-for-gpu-accelerated-algebraic-multigrid-and-preconditioned-iterat.md`](numerical-computation/amgx-a-library-for-gpu-accelerated-algebraic-multigrid-and-preconditioned-iterat.md)
    - 数理基础：AMG 粗化、Galerkin 粗层算子 $A_c=RAP$、V/W/K-cycle、GPU 稀疏线性代数
    - 为什么精读：GPU 上代数多重网格与预条件迭代库的工程范式——与 JFNK、Matrix-Free Multigrid、GPU GMRES 构成求解器主线。关联：JFNK Survey、Matrix-Free FEM Multigrid

46. **Fourier Neural Operator** — ai-for-physics
    - 文件：[`ai-for-physics/fourier-neural-operator-for-parametric-partial-differential-equations.md`](ai-for-physics/fourier-neural-operator-for-parametric-partial-differential-equations.md)
    - 数理基础：谱域核积分算子、Fourier layer $v_{t+1}=\sigma(\mathcal F^{-1}(R_\phi\cdot\mathcal F v_t)+W v_t)$、分辨率不变性
    - 为什么精读：算子学习的主流架构——谱域参数化 + GPU FFT，连接 PDE-Transformer、Neural Operator、Text2PDE。关联：Neural Operator、PDE-Transformer、PINN

47. **Machine Learning–Accelerated CFD** — ai-for-physics
    - 文件：[`ai-for-physics/machine-learning-accelerated-computational-fluid-dynamics.md`](ai-for-physics/machine-learning-accelerated-computational-fluid-dynamics.md)
    - 数理基础：learned correction / learned interpolation、可微求解器（jax-cfd）、粗网格湍流精度恢复、DNS/LES 加速
    - 为什么精读：把 ML 嵌入传统求解器内部而非替代——工程化 AI4CFD 的标杆，与 ML-Accelerated CFD、AMR、Roofline 性能视角衔接。关联：PINN、AMReX、Roofline

48. **Text2PDE: Latent Diffusion Models for Physics Simulation** — ai-for-physics
    - 文件：[`ai-for-physics/text2pde-latent-diffusion-models-for-accessible-physics-simulation.md`](ai-for-physics/text2pde-latent-diffusion-models-for-accessible-physics-simulation.md)
    - 数理基础：潜空间扩散（VAE+DDPM）、physics-field/text/shape conditioning、推理期 guidance、多 PDE 联合生成
    - 为什么精读：扩散模型进入 PDE 生成的最前沿——文本驱动、几何引导、零重训泛化，与 DDPM、PDE-Transformer、FNO 构成生成式模拟主线。关联：DDPM、PDE-Transformer、FNO

49. **Fault-tolerant quantum computation by anyons** — quantum-computing
    - 文件：[`quantum-computing/fault-tolerant-quantum-computation-by-anyons.md`](quantum-computing/fault-tolerant-quantum-computation-by-anyons.md)
    - 数理基础：toric code 稳定子码与拓扑序、量子双 D(G) 表示论（共轭类=磁荷/中心化子表示=电电荷）、Hopf 代数对偶（ribbon 算子代数 F ↔ 局域算子代数 D）、R-矩阵与 Yang-Baxter 方程、辫子群表示、S₅ 模型普适计算
    - 为什么精读：拓扑量子计算与拓扑量子纠错奠基之作——物理本质容错（编织/融合天然免疫局域噪声），与量子模拟（Schrödingerization、量子流体算法）构成量子计算主线两翼；数学上连通群论、Hopf 代数与量子纠错。关联：Quantum Simulation of PDEs via Schrödingerization、Efficient quantum algorithm for transport equation

## 阅读路线图

1. **几何/变分基础先行** → Hamiltonian ideal fluid → Madelung transform → Schrödinger's Smoke → Inside Fluids
2. **结构保持与涡方法** → Covector Fluids → Vortex Segment Clouds → Lie-Poisson Neural Networks
3. **PDE 学习主线** → PINN → Neural Operator（GKN → FNO）→ SINDy → DMD/Koopman → DDPM → Text2PDE / Physics-Informed Diffusion（生成式模拟）
4. **HPC 求解器主线** → JFNK Survey → Matrix-Free High-Order FEM Multigrid → Berger-Colella AMR (1989) → BoxLib with Tiling (2016) → AMReX → WarpX GPU 移植 → AmgX → GPU GMRES
    - 支撑：Roofline（性能上界）→ ECM 模型（可加预测）→ Hong-Kung I/O 复杂度（理论底座）→ Work-Stealing 调度（任务并行）
5. **前沿交叉补强** → Schrödingerization PDE → Force-Free Fields → Extended Lagrangian → Log-conformation viscoelastic
6. **几何耗散系统** → Double-Bracket Dissipation（刚体 → 未来理想流体推广）
7. **量子计算与容错基础** → Kitaev Anyons（拓扑容错/量子双表示论）→ Quantum Simulation of PDEs（Schrödingerization）→ 量子流体算法（Lattice Boltzmann / Navier-Stokes）

---

*覆盖 13 个分类 | 每篇均关联库内至少 1 篇其他论文 | 49/49 文件已链接*
