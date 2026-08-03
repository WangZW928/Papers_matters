# AMReX: 面向多物理应用的块结构自适应网格细化框架 / AMReX: Block-structured adaptive mesh refinement for multiphysics applications

**作者：** Weiqun Zhang, Andrew Myers, Kevin Gott, Ann Almgren, John Bell
**期刊：** The International Journal of High Performance Computing Applications, Volume 35, Pages 508-526, 2021
**DOI：** [https://doi.org/10.1177/10943420211022811](https://doi.org/10.1177/10943420211022811)
**arXiv：** [https://arxiv.org/abs/2009.12009](https://arxiv.org/abs/2009.12009)
**阅读状态：** 🔬 精读（Doctor 指定）
**流程状态：** ①元数据 ✓ | ②初稿 ✓ | ③评估 ✓(精读) | ④补充 ✓ | ⑤索引 ✓ | ⑥review ✓ | ⑦提交 ⏳

---

## 摘要

### 中文翻译
块结构自适应网格细化（AMR）为多个 ECP（Exascale Computing Project）应用项目提供了时空离散化策略的基础，覆盖加速器设计、增材制造、天体物理、燃烧、宇宙学、多相流和风力发电厂建模等领域。AMReX 是一个软件框架，为这些及其他 AMR 应用提供统一的基础设施，使其能够在从笔记本到 Exascale 架构的各种机器上高效运行。AMR 在保持对复杂多物理算法中不同物理过程的精确描述的同时，相比均匀网格降低了计算成本和内存占用。AMReX 支持求解简单或复杂几何中的偏微分方程组，以及使用粒子和/或粒子-网格操作来表示组件物理过程。本文讨论了 AMReX 框架的核心元素，如数据容器和迭代器，以及满足应用项目需求的若干专门操作。此外，还重点介绍了 AMReX 团队为在多种基于加速器的架构上实现高性能代码所采取的策略。

### 原文
> Block-structured adaptive mesh refinement (AMR) provides the basis for the temporal and spatial discretization strategy for a number of Exascale Computing Project applications in the areas of accelerator design, additive manufacturing, astrophysics, combustion, cosmology, multiphase flow, and wind plant modeling. AMReX is a software framework that provides a unified infrastructure with the functionality needed for these and other AMR applications to be able to effectively and efficiently utilize machines from laptops to exascale architectures. AMR reduces the computational cost and memory footprint compared to a uniform mesh while preserving accurate descriptions of different physical processes in complex multiphysics algorithms. AMReX supports algorithms that solve systems of partial differential equations in simple or complex geometries and those that use particles and/or particle–mesh operations to represent component physical processes. In this article, we will discuss the core elements of the AMReX framework such as data containers and iterators as well as several specialized operations to meet the needs of the application projects. In addition, we will highlight the strategy that the AMReX team is pursuing to achieve highly performant code across a range of accelerator-based architectures for a variety of different applications.

---

## 文章总结

### 1. 解决什么问题？
为 Exascale 时代的多物理模拟提供统一的块结构 AMR 软件框架，使不同应用领域（天体物理、燃烧、多相流等）能够高效利用从笔记本到超算的各种计算资源。

### 2. 用了什么方法论？
- **块结构 AMR（Block-structured AMR）：** 在矩形块（Box）层级上管理网格细化，兼顾自适应精度与计算效率
- **统一数据容器与迭代器：** 提供 `BoxArray`、`MultiFab`、`FArrayBox` 等核心抽象，统一管理网格数据和粒子数据
- **MPI+OpenMP/GPU 混合并行：** 支持分布式内存（MPI）和共享内存/加速器（OpenMP/CUDA/HIP）的多级并行
- **粒子-网格耦合：** 支持粒子方法与网格方法的混合求解
- **嵌入式边界（EB）：** 处理复杂几何边界条件

### 3. 主要结论是什么？
AMReX 作为 ECP 项目的核心软件框架之一，成功为多个不同物理领域的应用提供了统一的 AMR 基础设施，通过精心设计的数据抽象和并行策略，实现了在多种加速器架构上的高性能移植。

---

## 价值评估
Doctor 指定精读

## 公式与代码梳理

## 第一节：公式推导

这篇 AMReX 论文不是一篇以新数值格式为核心的数学论文，而是一篇框架论文。因此显式公式很少，真正关键的是“AMR 层级、不变量、离散算子、通信/负载均衡算法”背后的数学结构。

### 1. 块结构 AMR 的层级表示

AMReX 的基本数学对象是一族按层组织的网格。第 $\ell$ 层由若干互不重叠的矩形块组成：

$$
\mathcal{G}^{\ell}=\{B_i^\ell\}_{i=1}^{N_\ell},\qquad
B_i^\ell\cap B_j^\ell=\varnothing,\quad i\neq j
$$

不同层使用不同分辨率，且在物理空间中可以重叠；因此不能把层级简单理解为互不相交集合的并集。若需要表示整套 AMR 覆盖，可写成层级有效区域的并集：

$$
\Omega_{\mathrm{AMR}}=\bigcup_{\ell=0}^{L}\Omega_{\mathrm{valid}}^\ell,
\qquad
\Omega_{\mathrm{valid}}^\ell=\Omega^\ell\setminus\Omega^{\ell+1}
$$

其中最后一层约定 $\Omega^{L+1}=\varnothing$。相邻层之间有细化比：

$$
r_\ell=\frac{\Delta x_\ell}{\Delta x_{\ell+1}}
$$

通常 $r_\ell=2$，但 AMReX 允许运行时指定不同层之间的细化比。物理坐标与整数索引之间由 `Geometry` 维护：

$$
x(i)=x_{\min}+\left(i+\frac{1}{2}\right)\Delta x
$$

cell-centered 数据用半整数位置表示，face-centered、edge-centered、node-centered 数据则通过 `IndexType` 区分。这里的关键是：AMReX 将几何坐标、索引拓扑、数据布局解耦，使同一个 `Box` 抽象可以表达 cell、face、edge、node 上的数据。

AMR 的 proper nesting 条件不能只用物理区域的集合包含来表达。对细化后的索引区域，通常要求细层在粗层内缩（至少留出由 `n_proper` 指定的粗网格缓冲）后仍被粗层覆盖，可抽象写成：

$$
\operatorname{coarsen}_{r_\ell}(\Omega^{\ell+1})
\oplus \mathcal{B}_{n_{\mathrm{proper}}}
\subseteq \Omega^\ell
$$

其中 $\mathcal{B}_{n_{\mathrm{proper}}}$ 表示索引方向上的缓冲带，具体实现还受物理边界、周期边界和 stencil 半径限制。该条件保证粗细层插值、限制和通量修正时有足够的 coarse-level 数据。

### 2. Berger-Rigoutsos 聚类算法

论文第 5.2 节说明 AMReX 用 Berger-Rigoutsos 算法把被标记的 cells 聚成矩形 patch。设误差估计为：

$$
E_i = \eta(U_i,\nabla U_i,\nabla^2 U_i,\text{physics heuristic})
$$

标记集合为：

$$
T=\{i\mid E_i>\varepsilon\}
$$

目标是用尽量少的矩形块覆盖 $T$，同时避免矩形块里包含太多未标记 cells。一个常见效率指标是：

$$
\mathrm{efficiency}(B)=\frac{|T\cap B|}{|B|}
$$

Berger-Rigoutsos 的思想不是求全局最优矩形覆盖，而是递归地寻找“应该切开”的方向和位置。对当前候选 box $B$，它会对候选区域内的 tagged cells 做方向投影：

$$
S_{d,B}(k)=\sum_{i\in T\cap B}\mathbf{1}(i_d=k),
\qquad k\in\operatorname{proj}_d(B)
$$

其中 $d$ 是坐标方向，$k$ 是该方向上的索引。若投影曲线 $S_{d,B}(k)$ 出现明显谷值，说明 tagged cells 在该方向上可分成两个聚簇，于是在谷值处切分 $B$；若没有明显谷值，则结合投影的边界/断点信息决定切分。投影必须限制在当前候选 box，否则递归切分时会把其他候选区域的标记错误地混入统计。

数学逻辑是：用高维点集在坐标轴方向上的投影，把矩形覆盖问题降成多个一维分割问题。它牺牲全局最优性，换取 AMR regridding 中更重要的性质：速度快、矩形块规整、利于 stencil 和 MPI 分发。

AMReX 之后还施加：

$$
\max_d |B_d|\le \texttt{max\_grid\_size}
$$

以及可选的方向尺寸约束：

$$
|B_d|\equiv 0\pmod{\texttt{blocking\_factor}}
$$

该整除条件只在启用相应 blocking 约束且尺寸允许时成立；边界 patch 或最后一次切分可能需要特殊处理。前者防止单个 patch 过大而无法并行，后者有助于 multigrid coarsening 时 box 尺寸持续整除。

### 3. SFC 负载均衡

AMReX 默认用 Morton-ordering space-filling curve 做初始 `DistributionMapping`。每个 box 有代价：

$$
w_i \approx |B_i|
$$

或运行时测得的代价：

$$
w_i = t_i
$$

其中 $t_i$ 可以来自 wall-clock timer、GPU CUPTI timer 或手写 kernel timer。

Morton SFC 把多维空间索引映射成一维序：

$$
m_i = \operatorname{Morton}(c_i)
$$

$c_i$ 是 box 中心或代表点。排序后得到：

$$
B_{\pi(1)},B_{\pi(2)},\ldots,B_{\pi(N)}
$$

再按累计代价切成 $P$ 个互不重叠且覆盖全部 box 的分区：

$$
\mathcal{P}_p\cap\mathcal{P}_q=\varnothing\ (p\neq q),\qquad
\bigcup_{p=1}^{P}\mathcal{P}_p=\{1,\ldots,N\},
$$

并尽量使

$$
\sum_{i\in \mathcal{P}_p}w_i \approx \frac{1}{P}\sum_{i=1}^{N}w_i.
$$

这里的近似误差受离散 box 权重和分段策略限制，并非对每个 $p$ 都能精确为零。SFC 的数学取舍是：它不追求最精确的负载均衡，而是保持空间局部性。相邻的 SFC 区间往往对应空间上相邻的 patch，因此 ghost exchange、coarse-fine boundary 通信更局部。

论文也提到 knapsack 算法。它更接近组合优化：

$$
\min_{\mathcal{P}_1,\ldots,\mathcal{P}_P}
\max_p \sum_{i\in \mathcal{P}_p}w_i
$$

knapsack 负载更均匀，但空间连续性可能更差；SFC 通信局部性更好，但负载均衡不一定最优。

### 4. AMR 时间推进与 subcycling

论文没有给出完整时间推进公式，但说明 AMReX 提供传统 subcycling-in-time 模板。若层 $\ell$ 和 $\ell+1$ 的细化比为 $r_\ell$，典型时间步满足：

$$
\Delta t_{\ell+1}=\frac{\Delta t_\ell}{r_\ell}
$$

一层推进可以抽象成有限体积更新：

$$
U_i^{n+1}=U_i^n-\frac{\Delta t}{\Delta V_i}
\sum_{f\in\partial i} A_f F_f + \Delta t\,S_i
$$

对于二阶 Runge-Kutta，可写成：

$$
U^{(1)}=U^n+\Delta t\,L(U^n)
$$

$$
U^{n+1}=\frac{1}{2}U^n+\frac{1}{2}\left(U^{(1)}+\Delta t\,L(U^{(1)})\right)
$$

subcycling 的粗细层时间同步逻辑是：

1. 粗层 $\ell$ 走一步 $\Delta t_\ell$。
2. 细层 $\ell+1$ 走 $r_\ell$ 步，每步 $\Delta t_{\ell+1}$。
3. 两层到达同一物理时间后，执行 restriction 和 reflux。

restriction 将细层平均回粗层：

$$
U_I^\ell
=
\frac{1}{r^D}
\sum_{i\in \mathcal{C}(I)} U_i^{\ell+1}
$$

其中 $D$ 是空间维数，$\mathcal{C}(I)$ 是粗 cell $I$ 覆盖的 $r^D$ 个细 cell。

reflux 修正粗细边界处的守恒误差。若粗层通量为 $F^\ell$，细层时间空间平均通量为 $\overline{F}^{\ell+1}$，则 flux register 存储差值：

$$
\delta F = F^\ell - \overline{F}^{\ell+1}
$$

对粗细边界邻近粗 cell 的修正可写为（假设 $F_f$ 已按粗 cell 外法向取向）：

$$
U_I^\ell \leftarrow U_I^\ell
-
\frac{\Delta t_\ell}{\Delta V_I}
\sum_{f\in\partial I\cap \Gamma_{\ell,\ell+1}}
A_f\,\delta F_f,
\qquad
\delta F_f=F_f^\ell-\overline{F}_f^{\ell+1}.
$$

若 flux register 使用相反的面法向或把“细减粗”定义为差值，修正式中的符号必须相应反转。这里的 $\overline{F}^{\ell+1}$ 还应包含 $r_\ell$ 个细时间步的时间平均，并在粗细面上完成面积加权/面片汇总。这个公式是 AMR 守恒性的核心：粗层自己算出的跨界面通量必须被细层更高分辨率的通量替换，否则全局守恒会被粗细界面破坏。

### 5. 粒子-网格插值与沉积

AMReX 支持 particle-mesh 方法，例如 PIC、tracer、drag coupling、gravity coupling。粒子位置为 $x_p$，网格量为 $U_i$。mesh-to-particle 插值一般为：

$$
U(x_p)=\sum_i W_i(x_p)U_i
$$

其中 $W_i$ 是由插值阶数决定的 shape function，满足：

$$
\sum_i W_i(x_p)=1
$$

particle-to-mesh deposition 则把粒子守恒量 $q_p$ 沉积到网格。若 $Q_i$ 表示 cell 中的总量，常用写法为：

$$
Q_i \leftarrow Q_i + \sum_p q_p W_i(x_p),
\qquad \sum_i W_i(x_p)=1.
$$

若 $Q_i$ 表示 cell-centered 密度，则应除以 cell 体积：

$$
Q_i \leftarrow Q_i + \frac{1}{\Delta V_i}\sum_p q_p W_i(x_p),
$$

相应的离散守恒条件为

$$
\sum_i Q_i\Delta V_i=\sum_p q_p.
$$

因此原沉积式与守恒式只有在 $Q_i$ 被定义为 cell 总量或 $W_i$ 已包含体积归一化时才可同时成立。

AMReX 的关键工程选择是：粒子-网格操作时优先通信 mesh ghost cells，而不是通信粒子。这是因为 mesh connectivity 可由 `BoxArray` 元数据确定，而粒子 connectivity 需要检查粒子位置，代价更不规则。

mesh-to-particle 前先做：

$$
\texttt{FillBoundary}(U)
$$

保证每个 patch 有足够 ghost cells。particle-to-mesh 后做：

$$
\texttt{SumBoundary}(Q)
$$

把 ghost 区域中的沉积贡献加回 valid cell，避免跨 patch 粒子贡献丢失。

### 6. Embedded Boundary 离散

EB 方法把复杂几何嵌入规则网格。每个 cell 有体积分数：

$$
\kappa_i=\frac{|V_i\cap \Omega|}{|V_i|}
$$

每个 face 有面积分数：

$$
\alpha_f=\frac{|A_f\cap \Omega|}{|A_f|}
$$

有限体积更新因此变为 cut-cell 形式（取流体区域外法向，并将 EB 通量按同一取向定义）：

$$
(\kappa_i \Delta V)\frac{dU_i}{dt}
=
-\sum_{f\in\partial i}\alpha_f A_f F_f
-
A_{EB,i}F_{EB,i}
+
(\kappa_i\Delta V)S_i.
$$

如果 $F_{EB,i}$ 定义为流入固体方向的通量，EB 项的符号应随之改变。小 cut-cell 的问题来自 $\kappa_i\ll 1$，对特征速度 $|\lambda_{\max}|$ 的显式局部 CFL 约束可抽象为：

$$
\Delta t \lesssim C_{\mathrm{CFL}}\,\kappa_i\frac{\Delta x}{|\lambda_{\max}|},
$$

其中常数和离散算子、维数及几何形状有关。当 $\kappa_i$ 很小时，时间步会极小。论文提到 AMReX 的 EB 算法可把小 cut-cell 的更新 redistribution 到邻居。若 $\delta M_i$ 表示该 cell 的守恒量增量而不是平均值，数学上可理解为：

$$
\Delta M_j \leftarrow \Delta M_j+w_{ij}\delta M_i,
\qquad
\sum_{j\in\mathcal{N}(i)}w_{ij}=1,
$$

并要求目标邻域、权重和同步时序与 EB 几何相容。若使用的是平均值 $\Delta U_i$，则必须同时携带体积权重（例如按 $\kappa_i\Delta V_i$ 转换为守恒量）才能保证守恒。

EB 几何由隐式函数表示：

$$
\phi(x)
\begin{cases}
>0, & x \text{ 在固体内}\\
<0, & x \text{ 在流体内}\\
=0, & x \text{ 在边界上}
\end{cases}
$$

CSG 操作可由隐式函数组合实现，例如 union、intersection、difference 分别可写成：

$$
\phi_{A\cup B}(x)=\max(\phi_A(x),\phi_B(x))
$$

$$
\phi_{A\cap B}(x)=\min(\phi_A(x),\phi_B(x))
$$

$$
\phi_{A\setminus B}(x)=\min(\phi_A(x),-\phi_B(x))
$$

具体符号方向依赖 AMReX 的 inside/outside 约定，但核心逻辑是用 level set 的符号组合构造复杂几何。

### 7. 多重网格与线性求解

论文第 10 节给出的代表性线性系统是变量系数 Poisson/Helmholtz 型：

$$
a\alpha \phi - b\nabla\cdot(\beta\nabla\phi)=\mathrm{rhs}
$$

其中 $\phi$ 是 cell-centered 未知量，$\alpha$ 在 cell center，$\beta$ 在 face 上。离散后得到：

$$
A_h \phi_h = f_h
$$

以 cell-centered 二阶有限体积为例，令 $n_{if}$ 为从 cell $i$ 指向相邻 cell 的面法向，且 $\phi_{i,f}$ 表示该面两侧中心值构成的差分梯度，则：

$$
(A_h\phi)_i
=
a\alpha_i\phi_i
-
b\frac{1}{\Delta V_i}
\sum_{f\in\partial i}
\beta_f A_f
\frac{\phi_{i,f}^{+}-\phi_{i,f}^{-}}{\Delta x_f}
$$

这里的 $+$ 和 $-$ 必须按同一个面法向定义；不能把 $\phi_{i^+}$、$\phi_{i^-}$ 当作对所有面固定的全局索引。对非均匀网格，$\Delta x_f$ 还应替换为面两侧中心到面的距离组合。

多重网格 V-cycle 的数学流程是：

$$
r_h=f_h-A_h\phi_h
$$

$$
r_{2h}=R r_h
$$

$$
A_{2h} e_{2h}=r_{2h}
$$

$$
\phi_h \leftarrow \phi_h + P e_{2h}
$$

然后做 smoother，例如 Jacobi/Gauss-Seidel 类松弛：

$$
\phi_i^{(k+1)}
=
\phi_i^{(k)}
+
\omega
\frac{f_i-(A\phi^{(k)})_i}{A_{ii}}
$$

AMReX 的特殊点在于它支持 single-level 和 multi-AMR-level geometric multigrid；也支持 CG、BiCG，以及 hypre/PETSc 作为 finest-level solve 或 bottom solve。aggregation 合并粗层 box，让 V-cycle 可以继续 coarsen；consolidation 减少粗层参与 MPI ranks 数量，降低粗网格通信占比。

EB 下 cell-centered solver 的 stencil 需要使用体积分数、面积分数、边界法向、边界质心等几何量；nodal solver 的离散则取决于具体 operator 和几何处理，不宜概括为“基于有限元”。在需要几何矩的离散中，stencil 构造可用预计算矩积分：

$$
\iiint x^\alpha y^\beta z^\gamma\,dx\,dy\,dz
$$

并用 algebraic multigrid 处理 operator coarsening。

## 第二节：代码与算法流程

### 1. 核心软件架构

AMReX 的核心数据链条是：

`IntVect` → `Box` → `BoxArray` → `DistributionMapping` → `FabArray<FAB>` → `MultiFab` / `FArrayBox`

各对象分工如下：

- `IntVect`：整数索引点，维度无关。
- `Box`：逻辑矩形区域，包含 lower/upper index 和 `IndexType`。
- `BoxArray`：同一 AMR level 上所有互不重叠的 `Box`。
- `DistributionMapping`：长度等于 `BoxArray` 的 rank 映射，说明每个 box 的数据归哪个 MPI rank。
- `FArrayBox`：单个 box 上的实际多维数组，含 valid region 和 ghost cells。
- `MultiFab`：一个 level 上所有 `FArrayBox` 的分布式集合，本质是 `FabArray<FArrayBox>`。
- `Array4<T>`：不拥有数据，只提供 device/host lambda 可捕获的数组视图。
- `MFIter`：owner-computes 迭代器，在当前 rank 上遍历本地 boxes 或 tiles。

数据组织可抽象为：

$$
\texttt{MultiFab}^{\ell}
=
\{ \texttt{FArrayBox}(B_i^\ell) \mid i=1,\ldots,N_\ell \}
$$

其中每个 `FArrayBox` 的数据是四维：

$$
U(i,j,k,n)
$$

前三维为空间，第四维为变量 component。默认布局为 SoA，即每个 component 是一块连续 3D 数组，适合 stencil 和 GPU coalescing；特殊算法也可通过 `BaseFab<T>` 使用 AoS 或混合布局。

### 2. 并行执行模型

AMReX 是三层并行：

1. MPI rank 之间分配 boxes。
2. CPU 上 `MFIter` 可按 tile 用 OpenMP 并行。
3. GPU 上 `ParallelFor` 把 cell/particle loop 转成 CUDA/HIP/DPC++ kernel。

CPU 路径大致是：

```cpp
for (MFIter mfi(mf, TilingIfNotGPU()); mfi.isValid(); ++mfi) {
    Box tile = mfi.tilebox();
    ParallelFor(tile, lambda);
}
```

CPU 编译时，`MFIter` 层负责 OpenMP tile 并行，`ParallelFor` 内部近似为 tile 内串行或 SIMD 循环。GPU 编译时，tiling 默认关闭，`ParallelFor` 变成 kernel launch。这个设计把 OpenMP 放在 `MFIter` 层，而不是塞进 `ParallelFor`，使同一段 loop body 可以跨 CPU/GPU 后端复用。

内存管理由 `Arena` 完成。核心原则是：大块预分配、复用、隐藏 host/device/pinned/managed memory 的差异。mesh 和 particle 浮点数据默认尽量留在 device 或 managed memory，metadata 留在 host，临时传输缓冲用 pinned memory。

### 3. Regridding 工作流

一次 regridding 可分为：

1. 在 level $\ell$ 上计算误差估计 $E_i$。
2. 标记 cells：$T=\{i:E_i>\varepsilon\}$。
3. 用 Berger-Rigoutsos 聚类 tagged cells，生成矩形 patches。
4. 按 `max_grid_size` 切分过大的 patches。
5. 按 `blocking_factor` 调整 patch 尺寸，便于 multigrid coarsening。
6. 对 patches refine，生成 level $\ell+1$ 的 `BoxArray`。
7. 检查 proper nesting。
8. 生成或更新 `DistributionMapping`，用 SFC、knapsack 或 runtime timers。
9. 广播新 `BoxArray` metadata 到所有 MPI ranks。
10. 为新网格分配 `MultiFab` / particle containers / EB metadata。
11. 对保留区域 copy 旧数据；对新增细层区域从粗层插值。
12. 对粒子执行 `Redistribute()`，重新归属到正确 level/grid/rank/tile。

这个流程体现了 AMReX 的设计重点：网格拓扑是全局可见 metadata，实际场数据是分布式拥有。

### 4. AMR subcycling-in-time 工作流

典型递归推进：

1. advance level $\ell$ 一步 $\Delta t_\ell$。
2. 若存在 level $\ell+1$，则推进 $r_\ell$ 个细步。
3. 每个细步前，用满足时间插值要求的粗层数据填充 coarse-fine ghost cells；若使用多层耦合，还需按 operator 的边界条件处理同步。
4. 细层推进后，执行 fine-fine ghost exchange。
5. 细层完成 $r_\ell$ 步并与粗层同一时间后，在被细层覆盖的粗 cells 上执行 restriction；随后在 coarse-fine boundary 上执行 reflux。
6. reflux：用细层时间、面积加权通量修正粗层 coarse-fine boundary；修正符号遵循 flux register 的面法向约定。
7. 若有隐式项或 projection，执行跨层同步或 multilevel solve。
8. 到达 regrid interval 时，重建更细层网格。

AMReX 提供的是“stubs + 数据结构 + 通信原语”，不是强制应用必须采用固定算法。Castro 这类代码使用 built-in subcycling，其他应用可以自己掌控时间推进。

### 5. 粒子-网格交互流程

粒子数据由 `ParticleContainer` 管理，其内部按 level、grid、tile 分桶。粒子移动后：

1. 更新粒子位置：
   $$
   x_p^{n+1}=x_p^n+\Delta t\,v_p
   $$
2. 调用 `Redistribute()`，根据位置重新确定 level/grid/rank/tile。
3. 若需要 mesh-to-particle，先对 mesh `FillBoundary()`。
4. 对每个粒子执行：
   $$
   U_p=\sum_i W_i(x_p)U_i
   $$
5. 更新粒子速度、力、状态或内部变量。
6. 若需要 particle-to-mesh deposition，执行：
   $$
   Q_i\leftarrow Q_i+\sum_p q_p W_i(x_p)
   $$
7. 调用 `SumBoundary()`，把 ghost 区的沉积贡献加回 valid cells。
8. 若有 particle-particle 操作，构造 neighbor list 或 collision partner list。
9. GPU 上常用 prefix scan、counting sort、binning 对粒子重排，提高局部性。

CPU deposition 用 tile-local buffer 避免细粒度 atomics，然后再原子加回 `MultiFab`；GPU deposition 直接使用 global atomic，并依赖粒子排序改善 memory hierarchy 使用。

### 6. 线性求解 / multigrid 工作流

AMReX 线性求解流程一般是：

1. 构造 operator，例如：
   $$
   A=a\alpha I-b\nabla\cdot(\beta\nabla)
   $$
2. 根据 cell-centered / nodal / EB / viscous tensor 选择 stencil。
3. 初始化 residual：
   $$
   r=f-A\phi
   $$
4. 在当前网格层做 smoothing。
5. restriction residual 到粗 multigrid level。
6. 粗层继续 V-cycle；必要时 aggregation 合并 boxes。
7. 粗层通信成本过高时 consolidation 减少参与 ranks。
8. bottom solve 可调用 native solver、hypre 或 PETSc。
9. prolongate correction 回细层：
   $$
   \phi_h\leftarrow \phi_h+P e_{2h}
   $$
10. 后平滑并检查残差范数：
    $$
    \|f-A\phi\| < \tau
    $$

GPU 上 multigrid 的瓶颈不是单点 flop，而是 coarse level communication 和同步。因此论文里的 scaling 结果显示：单节点 GPU 很快，但大规模 multigrid 加速比会被通信削弱。

### 7. 性能可移植抽象层

AMReX 的性能可移植不是依赖一个完全通用的抽象框架，而是用面向 block-structured AMR 的薄层：

- `ParallelFor`：统一 cell loop、particle loop、3D/4D loop。
- `ReduceTuple`：一次 kernel 做多个 reduction。
- `Arena`：统一内存池和不同 memory spaces。
- `MFIter` / `ParIter`：把 domain decomposition 和 loop body 分离。
- GPU-aware MPI + buffer aggregation：降低跨 rank 通信开销。
- kernel fusion：把大量小 packing/unpacking kernels 合并为少数 kernel，减少 launch overhead。
- runtime timers：用真实 kernel time 做动态负载均衡，而不是仅用 cell count 猜代价。

其核心设计模式是：

$$
\text{physics loop body} \perp \text{execution backend}
$$

应用开发者描述“对哪些 cells/particles 做什么”，AMReX 决定“在 CPU tile、OpenMP thread、CUDA/HIP/DPC++ kernel 上怎么执行”。

## 第三节：与 Doctor 研究方向的关联

从 `README.md` 和 `CODEX_DEEP_READ.md` 看，Doctor 的论文库核心方向包括 AI for Physics、Geometric Fluid、Numerical Computation、Vortex Dynamics、Quantum/PDE 计算，以及明确的 HPC 求解器路线：JFNK、GPU GMRES、AmgX、matrix-free multigrid。AMReX 与这些方向的关联主要在“高性能 PDE 框架底座”而非单一物理模型。

### 1. 对高性能框架工作的直接关联

AMReX 展示了一个成熟科学计算框架的分层抽象方式：

$$
\text{数学离散}
\rightarrow
\text{网格/粒子数据结构}
\rightarrow
\text{通信模式}
\rightarrow
\text{后端执行}
$$

这对 Doctor 的高性能框架研究很有参考价值。尤其是，如果研究目标涉及 PDE solver、physics-informed computation、GPU 上的隐式/显式混合算法，AMReX 的 `BoxArray + DistributionMapping + MultiFab + iterator` 体系是一个非常值得拆解的工程范式。

关键启发是：框架不要把“算法流程”硬编码死，而应稳定提供数据结构、通信、重分布、插值、restriction、reflux、linear solver、I/O 等基础能力。上层物理代码保留控制权。

### 2. 与数值计算方向的关联

`CODEX_DEEP_READ.md` 把 JFNK、matrix-free high-order FEM multigrid、AmgX、GPU GMRES 放入 HPC 求解器主线。AMReX 的第 10 节正好提供工程背景：真实 multiphysics code 中，隐式项、projection、Poisson/Helmholtz、viscous tensor solve 是核心瓶颈。

值得 Doctor 关注的是：

- multigrid 在 AMR 层级上的 operator coarsening 和通信代价；
- GPU 上 linear solver 的瓶颈从计算转向同步和通信；
- native geometric multigrid 与 hypre/PETSc bottom solve 的混合模式；
- EB cut-cell 几何下 stencil 构造和 multigrid coarsening 的复杂性。

这些内容可以和 JFNK、matrix-free GMRES、GPU AMG 论文形成互补：那些论文偏 solver 方法，AMReX 偏大规模应用框架承载方式。

### 3. 与几何流体、涡动力学、粒子方法的关联

Doctor 的库中有 Clebsch Maps、Schrödinger's Smoke、vortex segment clouds、Eulerian-Lagrangian coupling 等方向。AMReX 的 particle-mesh 支持正好对应 Eulerian-Lagrangian 混合模拟：

$$
\text{Eulerian mesh field} \leftrightarrow \text{Lagrangian particles}
$$

这对涡粒子、PIC、tracer、spray、多相流、暗物质 N-body 都是共同结构。特别值得研究的是 AMReX 没有把粒子强行绑定到 mesh grids，而是支持 dual grid：

$$
\texttt{BoxArray}_{mesh}\neq \texttt{BoxArray}_{particle}
$$

这是一种很成熟的负载均衡设计。对于粒子密度高度不均匀、但流体求解代价较均匀的问题，单一 domain decomposition 会失败；dual grid 通过额外 mesh copy 换取两类工作负载的独立均衡。

### 4. 与 AI for Physics / PDE 学习的关联

Doctor 的库中有 PINN、Neural Operator、PDE-Net、physics-constrained dynamics 等。AMReX 对这些方向的价值不是直接提供神经网络方法，而是提供一个可验证的高性能传统 solver 基准：

- 用作生成高分辨率训练数据；
- 用作 neural operator / surrogate model 的 ground truth；
- 用作 hybrid solver 中传统 PDE component；
- 用作比较 learned discretization 是否能保持守恒、稳定性和 AMR coarse-fine consistency 的参照。

尤其是 reflux、restriction、EB cut-cell redistribution 这些机制提醒：真实 PDE 框架里的“物理一致性”不只来自连续方程，还来自离散层面的守恒同步。

### 5. 值得重点学习的工程决策

第一，metadata 全局复制、field data 分布式存储。`BoxArray` 和 `DistributionMapping` 每个 rank 都有副本，使通信关系可本地计算和缓存；真正大的 `FArrayBox` 数据才分布式拥有。

第二，数据结构和算法流程解耦。AMReX 不要求应用必须使用某个时间推进器，而是提供 subcycling 所需原语。这对可扩展研究代码很重要。

第三，性能可移植层足够薄。AMReX 没有把所有后端细节都抽象成复杂运行时系统，而是用 `ParallelFor`、`Arena`、iterator、reduction 等最小核心抽象覆盖高频路径。

第四，通信优化是一级设计目标。hash-based box intersection、metadata caching、MPI buffer aggregation、GPU packing kernel fusion，都是框架级性能的关键，不是后期补丁。

第五，动态负载均衡基于真实时间。AMReX 支持从 cell count、user cost 到 GPU kernel timer 的逐步升级，这比固定启发式更适合 multiphysics。

第六，复杂几何以 EB 方式嵌入规则网格。这样可以复用结构网格上的数据布局、stencil、AMR、GPU kernel，但代价是 cut-cell 稳定性、守恒修正和 EB-aware solver 复杂化。

第七，I/O 和调试也被框架化。Async I/O、plotfile、checkpoint helper、TinyProfiler、debug mode、nightly regression tests 说明成熟 HPC 框架不只是 solver，还必须覆盖生产模拟的完整生命周期。

整体来看，AMReX 对 Doctor 最重要的价值是：它把 AMR、粒子、EB、multigrid、GPU portability、MPI 通信和工程维护放进同一个可运行框架里。对于研究高性能 PDE/流体/物理智能框架的人，这篇文章应当作为“如何把数学方法变成 exascale-ready 软件系统”的架构案例来读。


## Review Questions

### 1. 检查发现

- **公式与量纲**：已修正 AMR 层级集合与有效覆盖区域的定义，补充 proper nesting、边界和 stencil 缓冲条件；修正 Berger–Rigoutsos 投影统计的候选区域范围；为 SFC 分区补充分区互斥与完备约束，并说明离散 box 权重下只能近似均衡。
- **守恒同步**：已明确 reflux 需要统一粗 cell 外法向、粗细通量差值、细层 subcycling 的时间平均以及面面积加权；若法向或差值定义反向，reflux 符号也必须反向。restriction 仅作用于被细层覆盖的 coarse cells。
- **粒子与几何**：已区分粒子沉积中的 cell 总量和 cell-centered 密度，并补充密度形式的体积归一化条件；已补充 EB cut-cell CFL 约束、守恒量 redistribution 权重归一化和 cut-cell 体积权重要求。
- **线性求解**：已将有限体积 stencil 改为同一面的局部两侧值，并说明非均匀网格面距的处理；已避免把 nodal solver 一概归为有限元；流程中的变系数算子已统一写为 `A=a\alpha I-b\nabla\cdot(\beta\nabla)`。
- **算法流程**：已补充 coarse-fine ghost 的时间插值、物理边界条件、多层耦合限制，以及 subcycling 后 restriction/reflux 的顺序和通量寄存器的符号约定。同时明确 AMReX 提供这些数据结构与同步原语，并不规定所有应用使用同一个时间推进算法。
- **中文语法与 Markdown**：已检查并统一显示公式 `$$...$$` 与行内公式 `$...$` 的使用，修正中英文术语周围的标点和句号，使标题、列表、代码标记与公式块保持一致。
- **叙事连贯性**：文章目前按 AMR 数据结构、核心算法、同步机制、粒子/EB/求解器、工程流程和研究关联展开；摘要中的框架定位能与后文公式、代码流程及总结相互对应。抽象公式和伪代码描述均应理解为架构复述，而不是单一应用的完整实现。

### 2. 仍需注意的适用范围

本文公式是对 AMReX 常用机制的抽象化说明，不等于所有应用的唯一实现。具体 EB redistribution、reflux 符号、边界条件、operator 离散和多层求解器配置，仍取决于应用的守恒变量、几何表示、时间积分器和底层 solver；实际使用时应以对应 AMReX 版本的 API 文档和示例代码为准。

### 3. 深入问题

1. 结合 `CODEX_DEEP_READ.md` Tier 1 的 Hamiltonian ideal fluid、Inside Fluids Clebsch Maps，以及 Tier 2 的 Covector Fluids：如何在 AMReX block AMR、EB、reflux 和 restriction 组成的离散框架中设计 Lie–Poisson、Clebsch 或 covector 的结构保持离散，使 coarse-fine synchronization 不破坏 helicity、环量或不可压约束？在 GPU/MPI 并行下，应如何定义并验证离散 Casimir 的漂移？
2. 结合 Tier 1 的 JFNK Survey 与 Tier 2 的 Matrix-Free High-Order FEM Multigrid：如何为 AMReX 的 EB/AMR 变系数算子构造 matrix-free JFNK 预条件器，使 AMR coarse levels、EB cut cells、aggregation/consolidation 与 GPU 通信同时保持 Newton–Krylov 收敛性和可扩展性？应如何设计谱指标与残差指标，区分离散误差、几何误差和通信瓶颈？
3. 结合 Tier 1 的 PINN、`CODEX_DEEP_READ.md` 中的 Neural Operator 方向，以及 Tier 3 的 Vortex Segment Clouds/Lie–Poisson Neural Networks：如何让学习模型预测 regridding、particle-mesh deposition 或 coarse-grid correction，同时把 reflux、粒子守恒、EB redistribution 和 Hamiltonian/Casimir 约束设计成可验证接口，而不是只优化点态误差？如何构造跨分辨率、跨几何和跨硬件的基准？
