# CODEX_DEEP_READ Tier 独立审查与重新分层

审查口径：Doctor 的主线是高性能 AMR/PDE 求解器框架、几何流体/结构保持方法、AI for Physics、量子计算与量子多体、相对论与几何。Tier 1 原则上只保留“不读就缺少领域骨架”的源头文献；唯一明确例外是能汇集该骨架的**方法论入口综述**，目前仅限 JFNK Survey，作为隐式 PDE 求解器与可微隐式层的共同术语、算法和预条件接口，不据此泛化为一般综述准入规则。Tier 2 是值得系统精读、能直接改造研究路线或工程架构的论文；Tier 3 是扩展阅读或了解核心思想即可的论文。

## 第一部分：调整摘要

只列出 Tier 发生变化的论文。

| 论文 | 原 Tier | 新 Tier | 一句话理由 |
|---|---:|---:|---|
| Geometric hydrodynamics via Madelung transform | 1 | 2 | 重要桥梁，但更像专题入口；不如 Morrison-Greene / Hamiltonian ideal fluid 对几何流体骨架基础。 |
| Inside Fluids: Clebsch Maps for Visualization and Processing | 1 | 4 | 对涡拓扑和可视化很有启发，但偏图形学方法论文，不应压过 AMR/HPC 和非正则 Hamiltonian 源头文献。 |
| Schrödinger's Smoke | 2 | 3 | 与 Madelung/Clebsch 主线相关，但主要是应用型图形学构造，全文精读性价比低于源头几何文献。 |
| Lie-Poisson Neural Networks (LPNets) | 3 | 2 | 直接连接非正则 Hamiltonian/Lie-Poisson 结构与可学习求解器，是 Doctor 结构保持 AI 主线的关键论文。 |
| Discrete variational calculus for double-bracket dissipation | 3 | 2 | “耗散仍保持几何约束”的思想对结构保持离散化很关键，值得从 Tier 3 上调。 |
| Local Adaptive Mesh Refinement for Shock Hydrodynamics | 3 | 1 | Berger-Colella AMR 是块结构 AMR 谱系源头；对 AMReX/BoxLib/AMR 求解器框架是骨架级论文。 |
| BoxLib with Tiling: An AMR Software Framework | 3 | 2 | 不是源头理论，但对 AMReX 式框架分层和 cache/thread tiling 设计有直接工程价值。 |
| AMReX: Block-structured AMR for multiphysics applications | 3 | 2 | 现代成熟框架代表，对 Doctor 正在构建的框架有直接架构参照，应深读。 |
| Roofline: An Insightful Visual Performance Model for Multicore Architectures | 3 | 2 | HPC 性能分析共同语言；对 stencil/AMR kernel 优化判断非常实用。 |
| Quantifying Performance Bottlenecks of Stencil Computations Using the ECM Model | 3 | 2 | stencil 性能预测比 Roofline 更细，可直接服务 PDE kernel 优化。 |
| I/O Complexity: The Red-Blue Pebble Game | 3 | 2 | memory/communication lower bound 的理论源头，能解释分块和通信避免算法的必要性。 |
| Noncanonical Hamiltonian Density Formulation of Hydrodynamics and Ideal MHD | 3 | 1 | Morrison-Greene 是非正则 Hamiltonian 流体/MHD 括号源头；原 Tier 3 明显低估。 |
| PDE-Transformer: Efficient and Versatile Transformers for Physics Simulations | 3 | 2 | 前沿 PDE foundation model 代表，虽非源头但与 AI4PDE 规模化方向高度相关。 |
| Geometric Deep Learning: Grids, Groups, Graphs, Geodesics, and Gauges | 3 | 2 | 是等变/几何 AI 的统一纲领，能支撑结构保持网络和规范几何学习。 |
| The Madelung Transform as a Momentum Map | 3 | 2 | 比一般 Madelung 综述更接近几何机制本身，应与 Madelung hydrodynamics 同层阅读。 |
| Deep Equilibrium Models | 3 | 2 | 隐式层、不动点、Jacobian-free 反传与 JFNK/PDE 隐式求解器天然同构。 |
| Hamiltonian Neural Networks | 3 | 2 | 结构保持神经网络的正则 Hamiltonian 起点，应作为 LPNets 前置深读。 |
| Hamiltonian Structure of Water Waves (Benjamin-Olver) | 3 | 2 | 自由边界水波 Hamiltonian 化的源头型文献，对几何流体分支价值高。 |
| Fourier Neural Operator | 3 | 1 | 算子学习主流骨干，直接对应 PDE 代理模型/分辨率泛化；原 Tier 3 明显低估。 |
| Machine Learning-Accelerated CFD | 3 | 2 | 比纯 PINN 更贴近“把 ML 嵌入传统求解器”的工程路线，应深读。 |
| Conservation Laws and Correlation Functions (Baym-Kadanoff 1961) | 3 | 2 | 守恒近似/响应函数的源头，对量子多体与结构约束构造有高价值。 |
| Force-Free Fields are Conformally Geodesic | 3 | 4 | 几何味道强但与 AMR/PDE 框架、AI4Physics、量子多体主线关系偏弱。 |
| A Geometric Derivation of the Einstein Equations from the Causal Action Principle | 3 | 4 | 前沿理论物理专题，不是相对论/几何基础原典，也不直接服务求解器主线。 |
| On the Relativity Principle and the Conclusions Drawn from It (Einstein 1907) | 3 | 4 | 历史意义强，但读 1905 后了解等效原理核心即可。 |
| Physics-Informed Diffusion Model for Flow Field Reconstruction | 3 | 4 | 应用价值存在，但源头价值弱于 DDPM/PINN/FNO。 |
| Universal Anomalous Diffusion of Quantized Vortices | 3 | 4 | 量子湍流专题论文，和通用结构保持/HPC 框架主线间接。 |
| Diffusion Equation Is Compatible with Special Relativity | 3 | 4 | 相对论扩散边缘专题，除非专攻协变耗散 PDE，否则不必列入核心精读。 |
| Text2PDE: Latent Diffusion Models for Physics Simulation | 3 | 4 | 前沿但未稳定成源头范式，了解 conditioning 和生成设定即可。 |

## 第二部分：重新分层后的完整清单

## Tier 1 — 必读（6 篇）

1. **Hamiltonian description of the ideal fluid** — geometric-fluid
   - 文件：[`geometric-fluid/hamiltonian-description-of-the-ideal-ﬂuid.md`](geometric-fluid/hamiltonian-description-of-the-ideal-ﬂuid.md)
   - 数理基础：理想流体的非正则 Hamiltonian/Poisson 结构、Lie-Poisson 约化、Casimir、不变量与能量-Casimir 稳定性。
   - 为什么精读：这是几何流体、结构保持神经网络、辛/Poisson 离散的共同母体。Doctor 若要把流体方程写成可学习、可离散、可保持结构的形式，这篇是骨架文献。关联：Morrison-Greene 1980、LPNets、Covector Fluids。

2. **Noncanonical Hamiltonian Density Formulation of Hydrodynamics and Ideal MHD** — geometric-fluid
   - 文件：[`geometric-fluid/noncanonical-hamiltonian-density-formulation-of-hydrodynamics-and-ideal-magnetohydrodynamics.md`](geometric-fluid/noncanonical-hamiltonian-density-formulation-of-hydrodynamics-and-ideal-magnetohydrodynamics.md)
   - 数理基础：非正则 Poisson 括号三形式（物理变量式/守恒密度式/Fourier 系数式）、Jacobi 恒等式、\(\nabla\cdot B=0\) 条件（含 Errata 修正）、Lie-Poisson 结构原型。
   - 为什么精读：Morrison-Greene 1980 是流体+MHD 统一非正则哈密顿表述的源头级论文；它比后续综述更能解释结构从哪里来、为什么括号这样写。关联：Hamiltonian ideal fluid、LPNets、Covector Fluids、Yang-Mills。

3. **Local Adaptive Mesh Refinement for Shock Hydrodynamics** — HPC
   - 文件：[`HPC/local-adaptive-mesh-refinement-for-shock-hydrodynamics.md`](HPC/local-adaptive-mesh-refinement-for-shock-hydrodynamics.md)
   - 数理基础：块结构 AMR 源头框架：嵌套矩形网格层级、空间/时间同比例细化（subcycling）、守恒 reflux 修正（\(\delta F\) 通量寄存器）、Richardson 局部截断误差估计、bisection+merge 聚类、proper nesting 不变量。
   - 为什么精读：Berger-Colella 1989 是 AMReX/BoxLib 块结构 AMR 谱系的源头；reflux、average-down、subcycling、tagging、聚类等核心概念都绕不开。对 Doctor 的 AMR/PDE 框架主线，这篇应从 Tier 3 直接升为 Tier 1。关联：AMReX、BoxLib with Tiling、WarpX GPU 移植。

4. **Jacobian-free Newton-Krylov Methods: A Survey** — numerical-computation
   - 文件：[`numerical-computation/jacobian-free-newton-krylov-methods-a-survey-of-approaches-and-applications.md`](numerical-computation/jacobian-free-newton-krylov-methods-a-survey-of-approaches-and-applications.md)
   - 数理基础：Newton-Krylov、Jacobian-vector product、Krylov 子空间、预条件、非线性全局化、隐式 PDE 求解器。
   - 为什么精读：这是上述 Tier 1 方法论入口例外，而非源头论文：它为大规模隐式 PDE 求解器提供共同语言。AMR 多物理求解、非线性稳态问题、隐式时间步进和可微隐式层都会回到这套语言。关联：Deep Equilibrium Models、Matrix-Free Multigrid、AmgX。

5. **Physics-informed neural networks (PINN)** — ai-for-physics
   - 文件：[`ai-for-physics/physics-informed-neural-networks-a-deep-learning-framework-for-solving-forward-a.md`](ai-for-physics/physics-informed-neural-networks-a-deep-learning-framework-for-solving-forward-a.md)
   - 数理基础：PDE 残差、初边值条件、反问题、自动微分、软约束优化。
   - 为什么精读：PINN 是 AI for Physics 的共同语言，即使工程上并非最高效，它定义了“把 PDE 写进损失函数”的标准范式。Doctor 需要理解其能力边界，才能判断 neural operator、混合 CFD、约束生成模型的改进点。关联：Parallel PINN、NTK、Physics-Informed Diffusion。

6. **Fourier Neural Operator** — ai-for-physics
   - 文件：[`ai-for-physics/fourier-neural-operator-for-parametric-partial-differential-equations.md`](ai-for-physics/fourier-neural-operator-for-parametric-partial-differential-equations.md)
   - 数理基础：谱域核积分算子、Fourier layer \(v_{t+1}=\sigma(\mathcal F^{-1}(R_\phi\cdot\mathcal F v_t)+Wv_t)\)、函数空间映射、分辨率不变性、FFT/GPU 实现。
   - 为什么精读：FNO 是算子学习的主流骨干，比 GKN 更应进入 Tier 1。它直接回答“神经网络学习 PDE 解算子而非单个解”的核心问题，是 PDE surrogate、weather/CFD foundation model、Text2PDE/PDE-Transformer 的重要前置。关联：GKN、PDE-Transformer、PINN。

## Tier 2 — 深度阅读（22 篇）

7. **Geometric hydrodynamics via Madelung transform** — geometric-fluid
   - 文件：[`geometric-fluid/geometric-hydrodynamics-via-madelung-transform.md`](geometric-fluid/geometric-hydrodynamics-via-madelung-transform.md)
   - 数理基础：Euler 流、Madelung 变换、波函数几何、量子流体、Schrödinger/Gross-Pitaevskii 表示。
   - 为什么精读：这是“经典流体 = 几何/量子表象”的重要桥梁，但不是整个领域的最底层源头；适合与 momentum map 论文成组深读。关联：Schrödinger's Smoke、Inside Fluids、NS-GP coupling。

8. **The Madelung Transform as a Momentum Map** — geometric-fluid
   - 文件：[`geometric-fluid/the-madelung-transform-as-a-momentum-map.md`](geometric-fluid/the-madelung-transform-as-a-momentum-map.md)
   - 数理基础：波函数空间实 Hermite 内积与 NLS Poisson 括号、半直积群 \(Diff(\mathbb R^n)\ltimes H^\infty\) 作用、动量映射、Lie-Poisson 可压流体括号、量子压、Clebsch/symplectic realization。
   - 为什么精读：把 Madelung 变换从代数代换提升为 Poisson/动量映射机制，是量子-经典流体对应的几何解释核心。关联：Geometric hydrodynamics via Madelung transform、Morrison-Greene 1980、Clebsch Maps。

9. **Covector Fluids** — geometric-fluid
   - 文件：[`geometric-fluid/covector-fluids.md`](geometric-fluid/covector-fluids.md)
   - 数理基础：速度/动量一形式、余切提升、Euler-Poincare/Lie-Poisson 离散化、结构保持流体表示。
   - 为什么精读：它把几何力学语言转成可计算的流体模拟表示，是 Hamiltonian ideal fluid 到图形学/数值算法之间的重要桥梁。关联：Hamiltonian ideal fluid、LPNets、Schrödinger's Smoke。

10. **Lie-Poisson Neural Networks (LPNets)** — ai-for-physics
    - 文件：[`ai-for-physics/liepoisson-neural-networks-lpnets-data-based-computing-of-hamiltonian-systems-wi.md`](ai-for-physics/liepoisson-neural-networks-lpnets-data-based-computing-of-hamiltonian-systems-wi.md)
    - 数理基础：Lie-Poisson 括号、余伴随轨道、Casimir 保持、Hamiltonian 学习、非正则结构先验。
    - 为什么精读：这是把 Morrison-Greene/Hamiltonian fluid 一类结构真正接到神经网络上的关键论文，适合作为 Doctor 结构保持 AI 路线的核心样板。关联：Hamiltonian Neural Networks、Hamiltonian ideal fluid、Discrete double-bracket。

11. **Hamiltonian Neural Networks** — ai-for-physics
    - 文件：[`ai-for-physics/hamiltonian-neural-networks.md`](ai-for-physics/hamiltonian-neural-networks.md)
    - 数理基础：Hamiltonian 向量场 \(\dot x=J\nabla H\)、能量守恒、辛结构、正则坐标、结构先验学习。
    - 为什么精读：HNN 是结构保持神经网络的正则坐标起点；理解它的优点和局限，才能看清 LPNets 为什么需要非正则 Poisson 结构。关联：LPNets、NTK、Hamiltonian ideal fluid。

12. **Discrete variational calculus for double-bracket dissipation** — differential-geometry
    - 文件：[`differential-geometry/discrete-variational-calculus-for-double-bracket-dissipation.md`](differential-geometry/discrete-variational-calculus-for-double-bracket-dissipation.md)
    - 数理基础：forced Euler-Poincare / forced Lie-Poisson 系统、double-bracket dissipation、离散变分积分器、余伴随轨道保持、能量耗散。
    - 为什么精读：核心启发是“耗散不必破坏几何约束”。这对构造带耗散但仍保持 Casimir/轨道约束的 PDE 离散和神经模型很有价值。关联：Hamiltonian ideal fluid、LPNets、Covector Fluids。

13. **SINDy: Sparse Identification of Nonlinear Dynamics** — ai-for-physics
    - 文件：[`ai-for-physics/discovering-governing-equations-from-data-by-sparse-identification-of-nonlinear-.md`](ai-for-physics/discovering-governing-equations-from-data-by-sparse-identification-of-nonlinear-.md)
    - 数理基础：稀疏回归、候选函数库、动力系统识别、PDE/ODE 结构发现、可解释模型选择。
    - 为什么精读：SINDy 是从数据发现控制方程的源头级方法，和 PINN/neural operator 形成互补：不是拟合解，而是识别方程结构。关联：Koopman/DMD、Machine Learning Hidden Symmetries、Quantum Closure。

14. **Spectral analysis of nonlinear flows (Koopman/DMD)** — fluid-mechanics
    - 文件：[`fluid-mechanics/spectral-analysis-of-nonlinear-flows.md`](fluid-mechanics/spectral-analysis-of-nonlinear-flows.md)
    - 数理基础：Koopman 算子、动态模态分解、谱分解、流场降维、非线性系统线性提升。
    - 为什么精读：DMD/Koopman 是流体数据分析和 ROM 的共同基础，能帮助 Doctor 连接高维 PDE 状态、低维相干结构和可学习动力学。关联：SINDy、Machine Learning-Accelerated CFD、Quantum Closure。

15. **Neural Operator: Graph Kernel Network** — ai-for-physics
    - 文件：[`ai-for-physics/neural-operator-graph-kernel-network.md`](ai-for-physics/neural-operator-graph-kernel-network.md)
    - 数理基础：图核积分算子、mesh/point cloud 上的算子学习、函数空间映射、分辨率外推。
    - 为什么精读：GKN 是 neural operator 谱系的重要早期节点，对非规则网格和 AMR 图结构有启发；但整体影响和工程通用性弱于 FNO。关联：FNO、GNN Review、AMReX。

16. **PDE-Transformer: Efficient and Versatile Transformers for Physics Simulations** — ai-for-physics
    - 文件：[`ai-for-physics/pde-transformer-efficient-and-versatile-transformers-for-physics-simulations.md`](ai-for-physics/pde-transformer-efficient-and-versatile-transformers-for-physics-simulations.md)
    - 数理基础：DiT 式 Transformer、物理通道独立时空 token 嵌入、通道间自注意力、16 类 PDE 联合预训练、基础模型迁移。
    - 为什么精读：这是 PDE foundation model 的代表性架构论文；不是源头理论，但对“多 PDE 统一训练”和生成式模拟路线很相关。关联：DDPM、FNO、Text2PDE。

17. **Geometric Deep Learning: Grids, Groups, Graphs, Geodesics, and Gauges** — ai-theory
    - 文件：[`ai-theory/geometric-deep-learning-grids-groups-graphs-geodesics-and-gauges.md`](ai-theory/geometric-deep-learning-grids-groups-graphs-geodesics-and-gauges.md)
    - 数理基础：对称群与不变性公理、G-等变/不变层、域 \(\Omega\) 与信号空间 \(X(\Omega)\)、群表示论、CNN/GNN/流形/规范等变统一蓝图。
    - 为什么精读：这是几何深度学习的统一纲领，能把网格、图、流形、规范场学习放在同一原则下理解。对结构保持 AI 和物理等变模型很关键。关联：PINN、GNN Review、Yang-Mills。

18. **Deep Equilibrium Models** — ai-model
    - 文件：[`ai-model/deep-equilibrium-models.md`](ai-model/deep-equilibrium-models.md)
    - 数理基础：不动点/求根、Broyden 拟牛顿、Anderson 加速、隐式微分、Jacobian-free 反向线性系统、内存 \(O(1)\) 训练。
    - 为什么精读：DEQ 把“网络层 = 非线性方程求解”范例化，和 JFNK、隐式时间步进、稳态 PDE 求解存在直接同构。关联：JFNK Survey、PINN、NTK。

19. **Multigrid for Matrix-Free High-Order FEM on GPUs** — numerical-computation
    - 文件：[`numerical-computation/multigrid-for-matrix-free-high-order-finite-element-computations-on-graphics-pro.md`](numerical-computation/multigrid-for-matrix-free-high-order-finite-element-computations-on-graphics-pro.md)
    - 数理基础：高阶 FEM、matrix-free operator evaluation、几何/代数多重网格、GPU kernel、算术强度与内存带宽权衡。
    - 为什么精读：这是高阶 PDE 求解器在 GPU 上做 matrix-free multigrid 的核心工程-数值结合样板，和 Doctor 的高性能求解器方向高度贴合。关联：JFNK、Roofline、AmgX。

20. **AMReX: Block-structured AMR for multiphysics applications** — HPC
    - 文件：[`HPC/amrex-block-structured-amr-for-multiphysics-applications.md`](HPC/amrex-block-structured-amr-for-multiphysics-applications.md)
    - 数理基础：Block-structured AMR、Berger-Rigoutsos 聚类、Morton SFC 负载均衡、subcycling/reflux 守恒、particle-mesh 插值沉积、cut-cell EB、geometric multigrid、性能可移植抽象层。
    - 为什么精读：展示成熟 HPC 框架如何把 AMR、粒子、EB、multigrid、GPU portability 和 MPI 通信统一起来。对 Doctor 构建框架有直接架构参考价值。关联：Berger-Colella AMR、BoxLib、WarpX。

21. **BoxLib with Tiling: An AMR Software Framework** — HPC
    - 文件：[`HPC/boxlib-with-tiling-amr-software-framework.md`](HPC/boxlib-with-tiling-amr-software-framework.md)
    - 数理基础：MFIter/tilebox 逻辑切分、OpenMP tile 调度、thread-private memory arena、cache/TLB/NUMA 性能模型、SMC 8 阶 stencil 性能实测。
    - 为什么精读：BoxLib 是 AMReX 的直接前身；它把数据结构、执行粒度、内存分配和应用接口一起设计，体现了框架层优化的真实取舍。关联：AMReX、Berger-Colella AMR、WarpX。

22. **Roofline: An Insightful Visual Performance Model for Multicore Architectures** — HPC
    - 文件：[`HPC/roofline-an-insightful-visual-performance-model-for-multicore-architectures.md`](HPC/roofline-an-insightful-visual-performance-model-for-multicore-architectures.md)
    - 数理基础：操作强度 \(I\)、Roofline 不等式 \(P\le \min(P_{peak},B\cdot I)\)、ridge point、3C 缓存模型、STREAM/LINPACK 实测屋顶。
    - 为什么精读：Roofline 是 HPC 性能分析事实标准，能快速判断 AMR/stencil kernel 是算力受限还是带宽受限。关联：ECM 模型、WarpX、Matrix-Free Multigrid。

23. **Quantifying Performance Bottlenecks of Stencil Computations Using the ECM Model** — HPC
    - 文件：[`HPC/quantifying-performance-bottlenecks-of-stencil-computations-using-the-execution-cache-memory-model.md`](HPC/quantifying-performance-bottlenecks-of-stencil-computations-using-the-execution-cache-memory-model.md)
    - 数理基础：ECM 可加预测模型、L1/L2/L3/DRAM 数据传输、layer condition、空间/时间分块、多核扩展外推。
    - 为什么精读：ECM 比 Roofline 更适合解释 stencil 内核瓶颈；对 AMR block kernel、halo 访问、cache blocking 的调优有直接价值。关联：Roofline、AMReX、Berger-Colella AMR。

24. **I/O Complexity: The Red-Blue Pebble Game** — HPC
    - 文件：[`HPC/io-complexity-the-red-blue-pebble-game.md`](HPC/io-complexity-the-red-blue-pebble-game.md)
    - 数理基础：红蓝鹅卵石博弈、S-partitioning 下界、FFT \(\Omega(n\log n/\log S)\)、矩阵乘法 \(\Omega(n^3/\sqrt S)\)、I/O 复杂度理论。
    - 为什么精读：这是 memory wall 和 communication lower bound 的理论源头，能解释为什么分块、循环变换、communication-avoiding 算法不是工程技巧而是复杂度必然。关联：Roofline、ECM、JFNK。

25. **Quantum Simulation of PDEs via Schrödingerization** — quantum-computing
    - 文件：[`quantum-computing/quantum-simulation-of-partial-differential-equations-via-schrödingerization.md`](quantum-computing/quantum-simulation-of-partial-differential-equations-via-schrödingerization.md)
    - 数理基础：PDE 到 Schrödinger 型系统嵌入、线性化/酉化、量子算法复杂度、输运/扩散/波动方程量子模拟。
    - 为什么精读：对“量子计算如何求 PDE”这条线最直接；比拓扑量子计算源头更贴近 Doctor 的 PDE 求解器主线。关联：Quantum Mechanical Closure、Kitaev Anyons、Feynman path integral。

26. **Hamiltonian Structure of Water Waves (Benjamin-Olver)** — geometric-fluid
    - 文件：[`geometric-fluid/hamiltonian-structure-symmetries-and-conservation-laws-for-water-waves.md`](geometric-fluid/hamiltonian-structure-symmetries-and-conservation-laws-for-water-waves.md)
    - 数理基础：Zakharov 正则变量、Dirichlet-Neumann 算子、水波 Hamiltonian 结构、对称性与守恒律、自由边界变分结构。
    - 为什么精读：自由面水波 Hamiltonian 化的奠基工作，是几何流体方法进入自由边界 PDE 的典范。关联：Hamiltonian ideal fluid、Madelung transform、Extended Lagrangian SGN。

27. **Machine Learning-Accelerated CFD** — ai-for-physics
    - 文件：[`ai-for-physics/machine-learning-accelerated-computational-fluid-dynamics.md`](ai-for-physics/machine-learning-accelerated-computational-fluid-dynamics.md)
    - 数理基础：learned correction / learned interpolation、可微求解器（jax-cfd）、粗网格湍流精度恢复、DNS/LES 加速、数值格式与 ML 组件耦合。
    - 为什么精读：这篇比纯替代式神经 PDE 求解更贴近工程现实：把 ML 嵌入传统求解器内部。对 Doctor 构建高性能 PDE 框架的 AI 扩展层有直接参考。关联：PINN、FNO、AMReX、Roofline。

28. **Conservation Laws and Correlation Functions (Baym-Kadanoff 1961)** — quantum-mechanics
    - 文件：[`quantum-mechanics/conservation-laws-and-correlation-functions.md`](quantum-mechanics/conservation-laws-and-correlation-functions.md)
    - 数理基础：有限温度格林函数、外场生成泛函、线性响应、守恒近似、Ward 型恒等式、Bethe-Salpeter 型方程、\(\Phi\)-derivable 泛函先驱。
    - 为什么精读：这是“近似必须由守恒结构生成”的源头文献之一。对量子多体、输运、闭包模型，以及结构保持近似的哲学都很重要。关联：Quantum Mechanical Closure、Feynman QED、Yang-Mills。

## Tier 3 — 扩展阅读（17 篇）

29. **Schrödinger's Smoke** — geometric-fluid
    - 文件：[`geometric-fluid/schrödingers-smoke.md`](geometric-fluid/schrödingers-smoke.md)
    - 数理基础：Schrödinger/Gross-Pitaevskii 表示、涡量重构、波函数相位缺陷、不可压流体近似。
    - 为什么精读：适合了解量子表象如何服务涡动力学模拟；但源头思想主要来自 Madelung/Clebsch/Hamiltonian 结构，不必放在 Tier 2。关联：Madelung transform、Inside Fluids、Covector Fluids。

30. **Incompressible Flow Simulation on Vortex Segment Clouds** — vortex-dynamics
    - 文件：[`vortex-dynamics/incompressible-flow-simulation-on-vortex-segment-clouds.md`](vortex-dynamics/incompressible-flow-simulation-on-vortex-segment-clouds.md)
    - 数理基础：涡段离散、Biot-Savart 诱导速度、Lagrangian 涡方法、不可压流体拓扑结构。
    - 为什么精读：对涡方法实现有启发，适合作为几何涡动力学扩展；但不是主线源头。关联：Inside Fluids、Schrödinger's Smoke、Hamiltonian fluid。

31. **Extended Lagrangian approach for multidimensional dispersive waves** — wave-mechanics
    - 文件：[`wave-mechanics/extended-lagrangian-approach-for-the-numerical-study-of-multidimensional-dispers.md`](wave-mechanics/extended-lagrangian-approach-for-the-numerical-study-of-multidimensional-dispers.md)
    - 数理基础：扩展 Lagrangian、色散波、Serre-Green-Naghdi 类模型、变分数值方法。
    - 为什么精读：对变分 PDE 离散和水波模型有局部价值；建议作为 Benjamin-Olver 水波 Hamiltonian 结构之后的专题补充。关联：Hamiltonian water waves、Discrete variational calculus。

32. **The log-conformation formulation for viscoelastic flows** — fluid-mechanics
    - 文件：[`fluid-mechanics/粘弹性流体/the-log-conformation-formulation-for-single--and-multi-phase-axisymmetric-viscoe.md`](fluid-mechanics/粘弹性流体/the-log-conformation-formulation-for-single--and-multi-phase-axisymmetric-viscoe.md)
    - 数理基础：粘弹性本构方程、构象张量、矩阵对数变量、正定性保持、高 Weissenberg 数稳定化。
    - 为什么精读：这是结构保持变量变换在复杂流体中的好例子，但方向较窄，适合扩展阅读。关联：PDE solver stability、structure-preserving discretization。

33. **Denoising Diffusion Probabilistic Models** — ai-model
    - 文件：[`ai-model/denoising-diffusion-probabilistic-models.md`](ai-model/denoising-diffusion-probabilistic-models.md)
    - 数理基础：前向加噪 Markov 链、反向去噪生成、ELBO、score matching、采样过程。
    - 为什么精读：DDPM 是生成式模型源头之一，读核心推导即可；对 PDE 生成只作为 Text2PDE/Physics-Informed Diffusion 的背景。关联：PDE-Transformer、Text2PDE、Physics-Informed Diffusion。

34. **Porting WarpX to GPU-accelerated platforms** — HPC
    - 文件：[`HPC/porting-warpx-to-gpu-accelerated-platforms.md`](HPC/porting-warpx-to-gpu-accelerated-platforms.md)
    - 数理基础：电磁 PIC、AMReX ParallelFor 性能可移植层、MultiFab/ParticleContainer 数据布局、kernel 融合、memory arena、粒子排序、SFC/knapsack 负载均衡。
    - 为什么精读：这是 AMReX 生态 GPU 落地样板，工程细节值得参考；但它依赖 AMReX/BoxLib/性能模型，适合放在 Tier 3 做案例读。关联：AMReX、BoxLib、Roofline。

35. **Scheduling Multithreaded Computations by Work Stealing** — HPC
    - 文件：[`HPC/scheduling-multithreaded-computations-by-work-stealing.md`](HPC/scheduling-multithreaded-computations-by-work-stealing.md)
    - 数理基础：fully strict 多线程 DAG、\(T_1/T_\infty\)、随机化工作窃取、busy-leaves property、时间界 \(T_1/P+O(T_\infty)\)、空间界 \(S_1P\)。
    - 为什么精读：任务并行调度理论基石；对 AMR 框架调度层有帮助，但 Doctor 近期更需要先读 AMR 和 kernel 性能模型。关联：AMReX、WarpX、ECM。

36. **Quantum Mechanical Closure of PDEs with Symmetries** — quantum-mechanics
    - 文件：[`quantum-mechanics/quantum-mechanical-closure-of-partial-differential-equations-with-symmetries.md`](quantum-mechanics/quantum-mechanical-closure-of-partial-differential-equations-with-symmetries.md)
    - 数理基础：密度算子表示未解析自由度、量子测量预测反馈、保正离散化、对称性不变压缩表示、核方法/延迟嵌入/迁移算子、浅水方程闭包。
    - 为什么精读：思想新颖，适合作为“量子算子语言组织统计闭包”的扩展；但不是 Doctor 当前 PDE 框架的基础构件。关联：Schrödingerization、SINDy/Koopman、Baym-Kadanoff。

37. **On the Electrodynamics of Moving Bodies (Einstein 1905)** — relativity
    - 文件：[`relativity/on-the-electrodynamics-of-moving-bodies.md`](relativity/on-the-electrodynamics-of-moving-bodies.md)
    - 数理基础：相对性原理、光速不变、同时性操作定义、洛伦兹变换、速度合成、长度收缩/时间膨胀、电动力学协变性。
    - 为什么精读：狭义相对论源头文献，物理骨架价值极高；但对 AMR/PDE/AI4Physics 主线不是优先全文精读对象。关联：Einstein 1907、Diffusion Equation Compatible with SR。

38. **Neural Tangent Kernel: Convergence and Generalization in Neural Networks** — ai-theory
    - 文件：[`ai-theory/neural-tangent-kernel-convergence-and-generalization-in-neural-networks.md`](ai-theory/neural-tangent-kernel-convergence-and-generalization-in-neural-networks.md)
    - 数理基础：无限宽极限、NNGP/NTK 核递推、核梯度流、lazy training、谱偏置、训练动力学。
    - 为什么精读：NTK 对理解 PINN 训练失败和多尺度刚性有帮助；但 Doctor 不是以深度学习理论为主线，读核心结论和 PINN 相关部分即可。关联：PINN、HNN、Geometric DL。

39. **Graph Neural Networks: A Review of Methods and Applications** — ai-model
    - 文件：[`ai-model/graph-neural-networks-a-review-of-methods-and-applications.md`](ai-model/graph-neural-networks-a-review-of-methods-and-applications.md)
    - 数理基础：消息传递、谱域 GCN/ChebNet、空间域 GraphSAGE/GAT/MPNN、GAE/VGAE、时空 GNN、1-WL 表达力与过平滑。
    - 为什么精读：作为 GNN 背景综述足够有用，支撑 mesh/AMR 图学习；但不必全文精读，优先读 Geometric DL 与具体物理图网络。关联：Geometric DL、GKN、AMReX。

40. **Machine Learning Hidden Symmetries** — ai-for-physics
    - 文件：[`ai-for-physics/machine-learning-hidden-symmetries.md`](ai-for-physics/machine-learning-hidden-symmetries.md)
    - 数理基础：对称变换群、可逆神经变换、守恒量发现、\(\mathcal A(\theta)=|\mathcal L_\xi T_\theta|^2\) asymmetry loss。
    - 为什么精读：对隐藏对称性发现有启发，但成熟度和源头价值低于 HNN/LPNets/Geometric DL；作为方法补充即可。关联：Geometric DL、HNN、SINDy。

41. **AmgX: GPU-Accelerated Algebraic Multigrid** — numerical-computation
    - 文件：[`numerical-computation/amgx-a-library-for-gpu-accelerated-algebraic-multigrid-and-preconditioned-iterat.md`](numerical-computation/amgx-a-library-for-gpu-accelerated-algebraic-multigrid-and-preconditioned-iterat.md)
    - 数理基础：AMG 粗化、Galerkin 粗层算子 \(A_c=RAP\)、V/W/K-cycle、GPU 稀疏线性代数、预条件迭代。
    - 为什么精读：对 GPU 上 AMG 工程范式有参考；但若时间有限，先读 JFNK 和 matrix-free multigrid。关联：JFNK、Matrix-Free FEM Multigrid。

42. **Fault-tolerant quantum computation by anyons** — quantum-computing
    - 文件：[`quantum-computing/fault-tolerant-quantum-computation-by-anyons.md`](quantum-computing/fault-tolerant-quantum-computation-by-anyons.md)
    - 数理基础：toric code、拓扑序、量子双 \(D(G)\)、Hopf 代数、ribbon 算子、R-矩阵、Yang-Baxter 方程、辫子群表示。
    - 为什么精读：拓扑量子计算源头价值极高，但与 PDE/AMR 主线距离较远；作为量子计算分支深读候选，不应挤占 Tier 1/2 的 PDE/HPC 位置。关联：Schrödingerization、Feynman path integral。

43. **Conservation of Isotopic Spin and Isotopic Gauge Invariance (Yang-Mills 1954)** — quantum-mechanics
    - 文件：[`quantum-mechanics/conservation-of-isotopic-spin-and-isotopic-gauge-invariance.md`](quantum-mechanics/conservation-of-isotopic-spin-and-isotopic-gauge-invariance.md)
    - 数理基础：同位旋 SU(2) 局域化、协变导数、非阿贝尔场强、自相互作用非线性项、守恒流、质量项困境。
    - 为什么精读：非阿贝尔规范场论开山之作；对“局域对称性决定相互作用形式”的几何物理观极重要，但和当前求解器主线是远场关联。关联：Geometric DL、Baym-Kadanoff、Einstein 1905。

44. **Space-Time Approach to Quantum Electrodynamics (Feynman 1949)** — quantum-mechanics
    - 文件：[`quantum-mechanics/space-time-approach-to-quantum-electrodynamics.md`](quantum-mechanics/space-time-approach-to-quantum-electrodynamics.md)
    - 数理基础：传播子、费曼规则、电子线/光子线/顶点、回路积分、自能、真空极化、质量/电荷重正化、Feynman 参数。
    - 为什么精读：费曼图和传播子方法的源头，量子多体图技术背景价值很高；但对 AMR/PDE 框架不构成第一优先。关联：Baym-Kadanoff、Feynman 1948、Yang-Mills。

45. **Space-Time Approach to Non-Relativistic Quantum Mechanics (Feynman 1948)** — quantum-mechanics
    - 文件：[`quantum-mechanics/space-time-approach-to-non-relativistic-quantum-mechanics.md`](quantum-mechanics/space-time-approach-to-non-relativistic-quantum-mechanics.md)
    - 数理基础：路径积分公设、传播子时间细分、泛函积分极限、Chapman-Kolmogorov 组合律、Schrödinger 方程等价性、驻相经典极限。
    - 为什么精读：路径积分量子化奠基文献；对量子模拟和多体方法有底层价值，但应在 PDE/HPC 主线之后阅读。关联：Schrödingerization、Feynman QED、Kitaev Anyons。

## Tier 4 — 专题/兴趣阅读（8 篇）

46. **Force-Free Fields are Conformally Geodesic** — differential-geometry
    - 文件：[`differential-geometry/force-free-fields-are-conformally-geodesic.md`](differential-geometry/force-free-fields-are-conformally-geodesic.md)
    - 数理基础：force-free field、共形几何、测地线表述、磁场线几何。
    - 为什么精读：几何味道很强，但与 Doctor 的 AMR/PDE 框架、AI4Physics 和量子多体主线关系偏弱。作为 Tier 4 专题/兴趣阅读保留。关联：Yang-Mills、geometric mechanics。

47. **A Geometric Derivation of the Einstein Equations from the Causal Action Principle** — differential-geometry
    - 文件：[`differential-geometry/a-geometric-derivation-of-the-einstein-equations-from-the-causal-action-principle.md`](differential-geometry/a-geometric-derivation-of-the-einstein-equations-from-the-causal-action-principle.md)
    - 数理基础：因果变分原理、因果费米子系统、osculating vacua、Euler-Lagrange 到 Einstein 方程、正则化长度与修正项。
    - 为什么精读：前沿理论物理价值存在，但不是相对论/几何的基础原典，也不直接服务 PDE/HPC 框架。作为 Tier 4 保留，除非 Doctor 特别进入因果费米子系统。关联：Einstein 1905、Yang-Mills。

48. **On the Relativity Principle and the Conclusions Drawn from It (Einstein 1907)** — relativity
    - 文件：[`relativity/on-the-relativity-principle-and-the-conclusions-drawn-from-it.md`](relativity/on-the-relativity-principle-and-the-conclusions-drawn-from-it.md)
    - 数理基础：SR 系统化、加速系时间、等效原理、引力红移、能量引力质量。
    - 为什么精读：历史源头意义强，但对 Doctor 当前主线而言，读 1905 后了解等效原理核心即可；列入 Tier 4 专题阅读即可。关联：Einstein 1905、GR。

49. **Physics-Informed Diffusion Model for Flow Field Reconstruction** — ai-for-physics
    - 文件：[`ai-for-physics/a-physics-informed-diffusion-model-for-high-fidelity-flow-field-reconstruction.md`](ai-for-physics/a-physics-informed-diffusion-model-for-high-fidelity-flow-field-reconstruction.md)
    - 数理基础：条件扩散模型、PDE residual guidance、物理场重建、去噪采样、超分辨率。
    - 为什么精读：应用方向贴近流场重建，但源头价值弱于 DDPM/PINN/FNO；建议读实验设置和 guidance 设计，不必全文精读。关联：DDPM、PINN、Text2PDE。

50. **Universal Anomalous Diffusion of Quantized Vortices** — fluid-mechanics
    - 文件：[`fluid-mechanics/universal-anomalous-diffusion-of-quantized-vortices-in-ultraquantum-turbulence.md`](fluid-mechanics/universal-anomalous-diffusion-of-quantized-vortices-in-ultraquantum-turbulence.md)
    - 数理基础：GPE 涡线动力学、MSD 输运统计、重联事件、Kelvin 波、反常扩散指数。
    - 为什么精读：量子湍流专题价值明确，但对 AMR/PDE 框架和通用结构保持方法的贡献间接。作为 Tier 4 专题阅读保留。关联：Inside Fluids、Vortex Segment Clouds。

51. **Diffusion Equation Is Compatible with Special Relativity** — wave-mechanics
    - 文件：[`wave-mechanics/diffusion-equation-is-compatible-with-special-relativity.md`](wave-mechanics/diffusion-equation-is-compatible-with-special-relativity.md)
    - 数理基础：相对论动理论 lift、Vlasov-Fokker-Planck、因果稳定解类、扩散方程协变性。
    - 为什么精读：问题有趣，但属于相对论扩散的边缘专题；除非 Doctor 专门研究协变耗散 PDE，否则归入 Tier 4 专题阅读。关联：Einstein 1905、DDPM。

52. **Text2PDE: Latent Diffusion Models for Physics Simulation** — ai-for-physics
    - 文件：[`ai-for-physics/text2pde-latent-diffusion-models-for-accessible-physics-simulation.md`](ai-for-physics/text2pde-latent-diffusion-models-for-accessible-physics-simulation.md)
    - 数理基础：潜空间扩散（VAE+DDPM）、physics-field/text/shape conditioning、推理期 guidance、多 PDE 联合生成。
    - 为什么精读：前沿方向新，但源头价值和可复用数理结构仍不稳定；建议了解问题设定和 conditioning 方式，作为 Tier 4 专题阅读保留。关联：DDPM、PDE-Transformer、FNO。

53. **Inside Fluids: Clebsch Maps for Visualization and Processing** — vortex-dynamics
    - 文件：[`vortex-dynamics/inside-fluids-clebsch-maps-for-visualization-and-processing.md`](vortex-dynamics/inside-fluids-clebsch-maps-for-visualization-and-processing.md)
    - 数理基础：Clebsch 势、相位缺陷、涡结构表示、螺旋度、环量、拓扑守恒、Schrödinger 演化。
    - 为什么精读：这是“涡拓扑 + 量子表象 + 可视化”的好论文，但它是应用构造而非骨架源头。建议从 Tier 1 降到 Tier 4：读核心表示和算法思想即可，不应压过 Morrison-Greene、Berger-Colella、FNO 等源头文献。关联：Schrödinger's Smoke、Madelung transform、Clebsch free-surface。
## 阅读路线图

1. **几何/变分基础先行** → Hamiltonian ideal fluid → Madelung transform → Schrödinger's Smoke → Inside Fluids
2. **结构保持与涡方法** → Covector Fluids → Vortex Segment Clouds → Lie-Poisson Neural Networks
3. **PDE 学习主线** → PINN → Neural Operator（GKN → FNO）→ SINDy → DMD/Koopman → DDPM → Text2PDE / Physics-Informed Diffusion（生成式模拟）
4. **HPC 求解器主线** → JFNK Survey → Matrix-Free High-Order FEM Multigrid → Berger-Colella AMR (1989) → BoxLib with Tiling (2016) → AMReX → WarpX GPU 移植 → AmgX → GPU GMRES
    - 支撑：Roofline（性能上界）→ ECM 模型（可加预测）→ Hong-Kung I/O 复杂度（理论底座）→ Work-Stealing 调度（任务并行）
5. **前沿交叉补强** → Schrödingerization PDE → Force-Free Fields → Extended Lagrangian → Log-conformation viscoelastic
6. **几何耗散系统** → Double-Bracket Dissipation（刚体 → 未来理想流体推广）
7. **量子计算与容错基础** → Kitaev Anyons（拓扑容错/量子双表示论）→ Quantum Simulation of PDEs（Schrödingerization）→ 量子流体算法（Lattice Boltzmann / Navier-Stokes）
8. **量子多体与输运基础** → Baym–Kadanoff 守恒近似（有限温度格林函数 + 线性响应 + 三条件）→ 未来可延展：Keldysh 非平衡格林函数、Φ-derivable 自洽近似、动力学平均场

---

*覆盖 13 个分类 | 每篇均关联库内至少 1 篇其他论文 | 53/53 文件已链接*
