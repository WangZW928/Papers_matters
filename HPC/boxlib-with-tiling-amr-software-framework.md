# BoxLib with Tiling: 一种块结构 AMR 软件框架 / BoxLib with Tiling: An AMR Software Framework

**作者：** Weiqun Zhang, Ann Almgren, Marcus Day, Tan Nguyen, John Shalf, Didem Unat
**期刊：** SIAM Journal on Scientific Computing, 2016
**arXiv：** [https://arxiv.org/abs/1604.03570](https://arxiv.org/abs/1604.03570)
**DOI：** [https://doi.org/10.48550/arXiv.1604.03570](https://doi.org/10.48550/arXiv.1604.03570)
**阅读状态：** 🔬 精读（Doctor 指定）
**流程状态：** ①元数据 ✓ | ②初稿 ✓ | ③评估 ✓(精读) | ④补充 ✓ | ⑤索引 ✓ | ⑥review △(部分完成) | ⑦提交 ⏳

---

## 摘要

### 中文翻译
本文介绍了一个引入 tiling（一种经典的循环变换技术）的块结构自适应网格细化（AMR）软件框架。BoxLib 中构建的多尺度、多物理代码旨在以高分辨率求解复杂系统，在当前和下一代架构上的性能至关重要。随着下一代架构上每个节点的核心数大幅增加，在节点内有效利用线程的能力变得必不可少，而当前的并行化模型不足以应对这一挑战。我们描述了一个新版 BoxLib，其中 tiling 构造被嵌入框架内部，使得基于 BoxLib 的应用程序无需应用开发者额外努力即可获得预期的性能提升。我们还讨论了利用 TiDA 可移植库使未来版本 BoxLib 能够利用 NUMA-aware 优化的路径。

### 原文
> In this paper we introduce a block-structured adaptive mesh refinement (AMR) software framework that incorporates tiling, a well-known loop transformation. Because the multiscale, multiphysics codes built in BoxLib are designed to solve complex systems at high resolution, performance on current and next generation architectures is essential. With the expectation of many more cores per node on next generation architectures, the ability to effectively utilize threads within a node is essential, and the current model for parallelization will not be sufficient. We describe a new version of BoxLib in which the tiling constructs are embedded so that BoxLib-based applications can easily realize expected performance gains without extra effort on the part of the application developer. We also discuss a path forward to enable future versions of BoxLib to take advantage of NUMA-aware optimizations using the TiDA portable library.

---

## 文章总结

### 1. 解决什么问题？
在多核/众核架构上，BoxLib AMR 框架原有的 MPI-only 或粗粒度并行模式无法充分利用节点内的大量核心。需要一种框架级别的 tiling 机制来自动提升线程级并行效率。

### 2. 用了什么方法论？
- **Tiling（分块循环变换）：** 将大循环嵌套切分成小 tile，提升 cache 局部性和并行粒度
- **框架级嵌入：** 在 BoxLib 的数据结构和迭代器层面集成 tiling，对应用开发者透明
- **TiDA 库：** 面向 NUMA-aware 优化的可移植抽象层
- **MPI + OpenMP 混合并行：** tiles 作为 OpenMP 线程的工作单元

### 3. 主要结论是什么？
通过在 BoxLib 框架层面嵌入 tiling 支持，应用代码无需修改即可在多核架构上获得显著的性能提升，为后续 AMReX 的 GPU 性能可移植策略奠定了基础。

---

## 价值评估
Doctor 指定精读

### 与 AMReX 论文的关系
BoxLib with Tiling (2016) 是 AMReX (2021) 的直接前身，作者高度重叠（Weiqun Zhang, Ann Almgren 等）。本论文的 tiling 机制和 NUMA-aware 策略直接演化为 AMReX 中的 `MFIter` + tiling 框架和 GPU 性能可移植抽象层。两篇论文构成 BoxLib → AMReX 的演化脉络。

---

## 公式与代码梳理

## 第一节：公式推导与算法原理

### 1. tiling 的循环变换

BoxLib 原始的计算模式是“每个 grid 调一次 kernel”，即对一个三维 Box

$$
B=[i_0,i_1]\times[j_0,j_1]\times[k_0,k_1]
$$

执行完整区域上的嵌套循环：

$$
\text{for } k\in[k_0,k_1],\quad
\text{for } j\in[j_0,j_1],\quad
\text{for } i\in[i_0,i_1].
$$

tiling 后，把 $B$ 划分为若干子 Box：

$$
B=\bigcup_{q=1}^{N_T} T_q,\qquad T_p\cap T_q=\varnothing\quad(p\neq q)
$$

其中每个 tile 为

$$
T_q=[i_q^0,i_q^1]\times[j_q^0,j_q^1]\times[k_q^0,k_q^1].
$$

若 tile 尺寸为

$$
\tau=(\tau_x,\tau_y,\tau_z),
$$

则理想情况下 tile 数约为

$$
N_T(B)\approx
\left\lceil\frac{n_x}{\tau_x}\right\rceil
\left\lceil\frac{n_y}{\tau_y}\right\rceil
\left\lceil\frac{n_z}{\tau_z}\right\rceil,
$$

其中 $n_x=i_1-i_0+1$、$n_y=j_1-j_0+1$、$n_z=k_1-k_0+1$ 是按闭区间计数的 cell 数。原来的 grid-level 迭代

$$
\sum_{B\in\mathcal{G}} \mathcal{K}(B)
$$

变成 tile-level 迭代：

$$
\sum_{B\in\mathcal{G}}\sum_{T\in\mathcal{T}(B)} \mathcal{K}(T).
$$

关键点是：BoxLib 论文采用的是 **logical tiling**，即 tile 只改变 iteration space，不改变 `FArrayBox` 的数据布局。数据仍然是一块连续数组；kernel 仍然拿同一个 `double*`；唯一变化是传入 kernel 的工作区域从 `validbox()` 变成 `tilebox()`。

因此 tiling 的数学本质不是改变离散方程，而是改变算子应用的遍历分解：

$$
L(U)|_B
\quad\Rightarrow\quad
\{L(U)|_{T_q}\}_{q=1}^{N_T(B)}.
$$

只要每个 tile 覆盖互不重叠且并集等于原 valid region，且 ghost / stencil 所需数据已填充，离散结果与未 tiling 版本应保持一致。

### 2. tile size 的约束

设 stencil 半径为 $s$，变量 component 数为 $n_c$，每个 double 为 $b=8$ 字节。若 kernel 对 $m$ 个数组读写，并需要 $n_{\mathrm{tmp}}$ 个临时数组，则 tile 的工作集可粗略估计为

$$
W(\tau)
\approx
b\,n_c\,(m+n_{\mathrm{tmp}})
(\tau_x+2s)(\tau_y+2s)(\tau_z+2s).
$$

这是把所有数组都按完整 stencil 扩展区域计入的保守估计；实际工作集还取决于数组布局、读写方向、缓存层级、写分配策略以及临时量是否可复用。为了让一个线程的工作集尽量留在目标 cache 层级中，理想约束是

$$
W(\tau)\le C_{\mathrm{eff}},
$$

其中 $C_{\mathrm{eff}}$ 是可被单线程有效使用的 cache 容量，而不是整个 socket 的理论 cache 容量。

同时 tile 不能太小，否则 tile 边界和调度开销占比变大。若每个 tile 的计算量为

$$
F(\tau)\approx c_{\mathrm{op}}\tau_x\tau_y\tau_z,
$$

tile 调度、函数调用和边界处理开销为 $O_{\mathrm{tile}}$，则希望

$$
F(\tau)\gg O_{\mathrm{tile}}.
$$

所以 tile size 的实际选择是两类约束的折中：

$$
O_{\mathrm{tile}}\ll c_{\mathrm{op}}\prod_d \tau_d
$$

且

$$
b\,n_c\,(m+n_{\mathrm{tmp}})\prod_d(\tau_d+2s)\le C_{\mathrm{eff}}.
$$

论文热方程实验使用 $128\times4\times4$，这体现了结构网格 stencil 中常见的选择：保留 $x$ 方向连续长循环以利于内存连续访问和向量化，在 $y,z$ 方向切小以缩小 cache footprint。

### 3. cache、TLB 与 NUMA 性能模型

未 tiling 时，一个大 grid 的工作集可粗略写为

$$
W_B\approx b\,n_c\,(m+n_{\mathrm{tmp}})
(n_x+2s)(n_y+2s)(n_z+2s).
$$

若 $W_B\gg C_{\mathrm{eff}}$，则多次 stencil loop 之间难以复用 cache 数据。热方程测试中，二阶导数被写成多个 loop：先算各方向 flux，再算 divergence。未 fusion 的多 loop 模式会造成数组反复从内存流入 cache。tiling 后，每个 tile 内的多 loop 更可能复用局部数据，但内存流量不能只由 tile 体积决定。用每个数组在一个 loop 中的读写字节数 $q_r$ 表示其流量、用 $H_T$ 表示所有 tile halo 的重复加载和边界访问，则更稳妥的近似是

$$
Q_{\mathrm{mem}}^{\mathrm{untiled}}
\approx \sum_{r=1}^{N_{\mathrm{loop}}} q_r|B|,
$$

$$
Q_{\mathrm{mem}}^{\mathrm{tiled}}
\approx \sum_{r=1}^{N_{\mathrm{loop}}}q_r
\left(|B|+H_{T,r}\right),
$$

其中 $H_{T,r}$ 由 tile 形状、stencil 半径、数组布局、缓存容量和 loop fusion 决定。只有在未 tiling 的跨 loop 复用很差、而 tile 内复用有效时，第二式才可能明显小于第一式；tiling 并不必然减少 DRAM 流量。

cache miss 率可以抽象为（需明确统计的 cache 层级和访问次数）

$$
r_{\mathrm{miss}}
=
\frac{M_{\mathrm{cache}}}{A_{\mathrm{mem}}},
$$

tiling 的目标是降低不必要的 cache miss 和内存流量，不是降低总算术操作数。对于 memory-bound stencil，运行时间可用 roofline 式上界近似为

$$
T\approx
\max\left(
\frac{F}{P_{\mathrm{flop}}},
\frac{Q_{\mathrm{mem}}}{B_{\mathrm{mem}}}
\right),
$$

而此类 stencil 往往由第二项主导。因此当 tiling 确实减少有效 DRAM 流量或 miss penalty 时，才会直接带来加速。

TLB 方面，若页面大小为 $P_{\mathrm{page}}$，工作集跨越页面数可用下式估计上界：

$$
N_{\mathrm{page}}(\tau)
\lesssim
\left\lceil
\frac{W(\tau)}{P_{\mathrm{page}}}
\right\rceil
+
N_{\mathrm{stride}},
$$

其中 $N_{\mathrm{stride}}$ 表示由多数组、非连续切片、页边界对齐和访问步长带来的额外页跨度。若 $N_{\mathrm{page}}(\tau)$ 超过 TLB 可覆盖页数，频繁跨页会增加 TLB miss。tiling 通过减小线程局部工作集，使

$$
N_{\mathrm{page}}(\tau)\le N_{\mathrm{TLB}}
$$

更容易成立。论文还指出，kernel 内动态分配临时数组会导致 allocator lock contention、TLB miss，甚至 page fault。BoxLib 的 thread-private memory arena 正是为减少这些问题。

NUMA 方面，设一个节点有 $R$ 个 NUMA domain。若线程 $p$ 访问本地内存的带宽/延迟为 $(B_{\mathrm{loc}},L_{\mathrm{loc}})$，访问远端内存为 $(B_{\mathrm{rem}},L_{\mathrm{rem}})$，通常

$$
B_{\mathrm{rem}}<B_{\mathrm{loc}},\qquad
L_{\mathrm{rem}}>L_{\mathrm{loc}}.
$$

logical tiling 只改变访问次序，不改变 grid 数据分配。如果一个 `FArrayBox` 被单块连续分配，它可能被放在某个 NUMA domain 或按 first-touch 分散，tile 执行线程却可能位于另一个 NUMA domain，于是远端访问比例

$$
\rho_{\mathrm{remote}}
=
\frac{Q_{\mathrm{remote}}}{Q_{\mathrm{local}}+Q_{\mathrm{remote}}}
$$

可能偏高。若把带宽限制和未被带宽项吸收的远端访问延迟分开建模，总访存时间可估为

$$
T_{\mathrm{mem}}
\approx
\frac{Q_{\mathrm{local}}}{B_{\mathrm{loc}}}
+
\frac{Q_{\mathrm{remote}}}{B_{\mathrm{rem}}}
+
N_{\mathrm{remote}}\Delta L_{\mathrm{rem}},
$$

其中 $\Delta L_{\mathrm{rem}}$ 是相对本地访问的额外延迟，$N_{\mathrm{remote}}$ 应理解为不能被连续带宽传输摊销的远端访存事件数，而不是所有远端字节数。TiDA 的 regional tiling 则把 grid 切成 region，每个 region 的数据独立连续分配，并尽量放置在对应 NUMA domain。目标是降低 $\rho_{\mathrm{remote}}$，使大部分 tile 的主访问变成本地访问。

### 4. BoxLib 数据结构与 tiling 的交互

BoxLib 的核心数据结构链条是：

`Box` → `FArrayBox` / `Fab` → `MultiFab` → `MFIter`

它们的含义如下。

`Box` 是整数索引空间中的矩形区域。三维 Box 可由六个整数描述：

$$
B=(i_{\min},i_{\max},j_{\min},j_{\max},k_{\min},k_{\max}).
$$

`FArrayBox` 是单个 Box 上的浮点数组。它内部是一维连续内存，但可以按 Fortran 多维数组视图解释：

$$
a(i,j,k,n),\qquad n=1,\ldots,n_c.
$$

`FArrayBox` 的数据区域可以大于 valid region，因为它包含 ghost cells：

$$
B_{\mathrm{fab}}
=
\operatorname{grow}(B_{\mathrm{valid}}, n_{\mathrm{ghost}}).
$$

`MultiFab` 是一个 AMR level 上多个 `FArrayBox` 的分布式集合：

$$
\mathrm{MultiFab}^{\ell}
=
\{ \mathrm{FArrayBox}(B_i^\ell)\}_{i=1}^{N_\ell}.
$$

每个 MPI rank 只拥有部分 `FArrayBox`，但每个 rank 保存所有 grid 的 metadata，以便计算通信关系和 coarse-fine 交互。

tiling 主要嵌入 `MFIter`。未 tiling 时：

```cpp
for (MFIter mfi(mf); mfi.isValid(); ++mfi) {
    Box vbox = mfi.validbox();
    FArrayBox& fab = mf[mfi];
    f(vbox, fab);
}
```

tiling 后：

```cpp
for (MFIter mfi(mf, true); mfi.isValid(); ++mfi) {
    Box tbox = mfi.tilebox();
    FArrayBox& fab = mf[mfi];
    f(tbox, fab);
}
```

这说明 BoxLib 的设计选择是把 tiling 放在 iterator 层，而不是侵入每个物理 kernel。`FArrayBox` 不变，kernel 数据指针不变，只有工作 Box 改变。

`growntilebox(nghost)` 用于 stencil 需要 ghost 区域时返回扩展 tile。它的关键语义不是保证所有 grown boxes 互不重叠，而是在 tile 内部边界处避免不必要扩展、在 grid 边界处提供所需 ghost/邻域访问；相邻 grown tile 仍可能因 stencil halo 而重叠。因此并行 kernel 应把写入限制在 `tilebox()` 对应的唯一覆盖区域，或对需要写 grown 区域的算法显式处理同步和归约。`nodaltilebox(direction)` 则为有限体积 flux 计算提供 face-type tile。

### 5. AMR time-stepping / subcycling 与 tiling

BoxLib 支持多种 AMR time-subcycling。对相邻层 $\ell$ 和 $\ell+1$，细化比为

$$
r_\ell=\frac{\Delta x_\ell}{\Delta x_{\ell+1}},
$$

典型 subcycling 时间步为

$$
\Delta t_{\ell+1}=\frac{\Delta t_\ell}{r_\ell}.
$$

有限体积更新可写为

$$
U_i^{n+1}
=
U_i^n
-
\frac{\Delta t}{\Delta V_i}
\sum_{f\in\partial i} A_f F_f
+
\Delta t S_i.
$$

AMR subcycling 的递归结构是：

$$
\operatorname{Advance}(\ell,\Delta t_\ell)
\rightarrow
r_\ell \text{ 次 } \operatorname{Advance}(\ell+1,\Delta t_{\ell+1})
\rightarrow
\operatorname{Sync}(\ell,\ell+1).
$$

同步包括 restriction 和 reflux。restriction 把细层平均回粗层：

$$
U_I^\ell
\leftarrow
\frac{1}{r^D}
\sum_{i\in\mathcal{C}(I)} U_i^{\ell+1}.
$$

reflux 用细层更准确的通量修正粗细边界：

$$
U_I^\ell
\leftarrow
U_I^\ell
-
\frac{\Delta t_\ell}{\Delta V_I}
\sum_{f\in\Gamma_{\ell,\ell+1}}
A_f
\left(
F_f^\ell-\overline{F}_f^{\ell+1}
\right).
$$

tiling 不改变 subcycling 的数学顺序。它改变的是每一层内部 operator 的执行粒度：

$$
L^\ell(U^\ell)|_{B_i^\ell}
\quad\Rightarrow\quad
\{L^\ell(U^\ell)|_{T_{iq}}\}_q.
$$

因此 tiling 必须满足两个条件：第一，tile 之间不能破坏 valid region 的唯一覆盖；第二，stencil、ghost fill、flux register、restriction/reflux 所需数据必须在 tile kernel 进入前或局部扩展区域内可见。

### 6. TiDA 抽象层设计

TiDA 引入两个概念：regional tiling 和 logical tiling。

logical tiling 是 BoxLib 论文中已经实现的部分。每个 grid 只有一个 region，数据仍然整块连续分配：

$$
G \rightarrow R_1,\qquad R_1=G,
$$

然后在 iteration space 上切成 tile：

$$
R_1=\bigcup_q T_q.
$$

regional tiling 更一般。一个 grid 先切成多个 region：

$$
G=\bigcup_{r=1}^{N_R} R_r,
$$

每个 region 独立连续分配内存，再把 region 切成 logical tiles：

$$
R_r=\bigcup_{q=1}^{N_T(r)} T_{rq}.
$$

其设计目标是让 region 对应 NUMA domain 或 memory locality domain：

$$
\operatorname{place}(R_r)=\operatorname{NUMA}(r),
\qquad
\operatorname{execute}(T_{rq})\approx \operatorname{NUMA}(r).
$$

这样 memory placement 和 computation placement 可以由框架或 TiDA 管理，而不是由应用开发者手写。论文中的未来方向是：BoxLib 保持应用层 API 尽量稳定，底层通过 TiDA 改变数据布局和执行映射，从 logical tiling 走向 NUMA-aware regional tiling。

---

## 第二节：代码与算法流程

### 1. 原始 BoxLib 架构

未 tiling 的 BoxLib 以 AMR level 为单位组织数据。一个 level 是若干互不重叠的 rectangular grids，每个 grid 对应一个 `FArrayBox`。多个 `FArrayBox` 组成 `MultiFab`，并通过 MPI 分布在多个进程上。

原始执行流程是：

1. 每个 MPI rank 拥有一部分 grids。
2. 需要远端数据时，通过 `FillBoundary()` 填充 ghost cells。
3. 应用代码通过 `MFIter` 遍历本地 `FArrayBox`。
4. 每次迭代调用一个 Fortran kernel，kernel 处理整个 grid。
5. OpenMP 通常写在 Fortran kernel 的 cell loop 内部。

这种模式在传统多核 CPU 上可行，但在 many-core / NUMA 节点上有三个问题。

第一，grid 数量未必足够多，grid-level 并行粒度太粗。第二，loop-level OpenMP 在许多小 kernel 中反复进入 parallel region，线程创建、同步和调度开销高。第三，大 grid 的工作集超出 cache，内存带宽成为瓶颈。

### 2. tiling 如何嵌入 BoxLib

论文的关键工程贡献是把 tiling 嵌入 `MFIter`，而不是要求每个应用 kernel 手写 tiled loop。

新的 `MFIter` 支持三种构造方式：

```cpp
MFIter(const MultiFab& mf);
MFIter(const MultiFab& mf, bool do_tiling);
MFIter(const MultiFab& mf, const int tilesize[]);
```

第一种保持旧行为，每个 grid 一个 tile。第二种启用运行时默认 tile size。第三种允许不同算法阶段指定不同 tile size。

代码变化非常小。原来传入 kernel 的是

```cpp
const Box& vbox = mfi.validbox();
```

tiling 后传入的是

```cpp
const Box& tbox = mfi.tilebox();
```

`FArrayBox& fab = mf[mfi]` 和 `double* a = fab.dataPtr()` 都不变。也就是说，tiling 对应用开发者暴露为“更小的 work region”，而不是新的数组类型。

### 3. MPI + OpenMP 混合并行模型

BoxLib 的分布式并行仍然由 MPI 管理：

$$
\mathcal{G}=\bigcup_{p=0}^{P-1}\mathcal{G}_p,
$$

其中 $\mathcal{G}_p$ 是 rank $p$ 拥有的 grids。tiling 后，每个 rank 的工作集进一步分成 tiles：

$$
\mathcal{T}_p
=
\bigcup_{B\in\mathcal{G}_p}\mathcal{T}(B).
$$

OpenMP 线程在 rank 内分配 tiles：

$$
\mathcal{T}_p
=
\bigcup_{q=0}^{Q-1}\mathcal{T}_{p,q},
$$

其中 $Q$ 是该 rank 内线程数。

论文中的 tiled 写法是在 `MFIter` 外部开一个 OpenMP parallel region：

```cpp
#pragma omp parallel
for (MFIter mfi(mf,true); mfi.isValid(); ++mfi) {
    const Box& tbox = mfi.tilebox();
    FArrayBox& fab = mf[mfi];
    f(tbox, fab);
}
```

`MFIter` 检测到自己处于 OpenMP parallel region 后，把 tile iteration 静态分配给线程。这样 OpenMP 不再散落在各个 Fortran kernel 中，而是在框架迭代层统一管理。

它的优点是：

- tile 数通常远多于 grid 数，线程并行度更充足；
- 避免每个小 kernel 反复创建 OpenMP region；
- 减少应用开发者写 OpenMP pragma 的错误概率；
- 小 grid 或 multigrid V-cycle 底层 coarse grid 上仍可能有足够 tile 并行度；
- 不需要为了增加并行度而人为把 AMR grids 切得很小。

最后一点很重要。AMR 中用许多小 grids 增加并行度会带来副作用：metadata 增多、box-box intersection 变贵、ghost cells 体积比例增加、跨层 copy 和 ghost fill 成本上升。tiling 达到的是“小执行单元”，而不是“小 AMR grid”，因此避免把算法结构和并行粒度绑死。

### 4. TiDA portable library 集成思路

TiDA 的角色不是替换 BoxLib 的 AMR 抽象，而是在数据布局和 locality 管理层提供可移植接口。它隐藏：

- region 如何构造；
- region 如何映射到 NUMA domain；
- tile 如何在 region 内生成；
- 线程如何靠近数据执行；
- region 内数据如何独立连续分配。

BoxLib 论文中的 logical tiling 是低侵入版本；TiDA regional tiling 是面向未来 NUMA 架构的增强版本。抽象层次可以写成：

$$
\text{AMR level}
\rightarrow
\text{grid}
\rightarrow
\text{region}
\rightarrow
\text{tile}
\rightarrow
\text{cell loop}.
$$

其中 grid 是 AMR 几何/通信单位，region 是 NUMA 数据放置单位，tile 是线程执行单位。这三个层次不应混淆。

### 5. 性能实验与结果

论文做了两类 benchmark。

第一类是显式 heat equation solver。设置为单层、单 grid、$128^3$ cells、三维周期边界、forward Euler 时间推进、二阶中心差分。实验刻意没有融合 flux 和 divergence loops，以便观察 tiling 对 memory-bound stencil 的影响。

串行结果显示，即使没有线程并行，logical tiling 也能显著加速。Gnu 编译器下，$128\times4\times4$ tile 从未 tiling 的 28.6 秒降到 8.5 秒，约 $3.4\times$。Intel 编译器下，从 15.5 秒降到 8.7 秒，约 $1.8\times$。这说明 tiling 的收益不只是线程并行，也来自 cache locality。

Edison 的 12-core Intel Ivy Bridge 上，$128\times4\times4$ tile 的 12-thread tiled run 相对单线程 untiled run 达到 $16.5\times$ speedup；相对单线程 tiled run 是 $9.6\times$。同样 12 线程下，tiled 比 untiled 快超过 $5.3\times$。

Babbage 的 60-core Intel Knights Corner 上，heat equation kernel 的 120-thread tiled run 相对单线程 tiled run 为 $69\times$，相对单线程 untiled run 为 $86\times$。继续增加到 180 或 240 线程没有带来 kernel 加速，240 线程还比 120 线程慢约 20%，说明 tile 并行也会受硬件线程、带宽、cache 竞争和调度开销限制。

论文还测试了 ghost cell filling。即使没有 MPI，周期边界 ghost fill 也涉及本地数据 copy。KNC 上 240-thread tiled ghost fill 相对单线程 untiled run 达到 $126\times$。未 tiling 的 120-thread run 中，ghost fill 时间占 fill + kernel 总时间超过 40%，这是 Amdahl 定律的典型体现：

$$
S(N)=\frac{1}{(1-f)+f/N}.
$$

如果 ghost fill 这类“看似辅助”的部分不并行化，主 kernel 再快也会被串行或低效部分限制。

第二类 benchmark 是 SMC miniapp。SMC 求解多组分、反应、可压缩 Navier-Stokes，使用 9-species $H_2/O_2$ 机制、三阶 Runge-Kutta、八阶 stencil，stencil 跨 9 个 cells。KNC 上，$128^3$ 单 grid、$128\times4\times4$ tile 的 180-thread tiled run 相对单线程 tiled run 达到 $86\times$，相对单线程 untiled run 达到 $92\times$。最佳 tiled run 比最佳 untiled run 快 $2.4\times$。

TiDA regional tiling 的原型实验在 Trestles 上运行 SMC。单 NUMA domain，即 4 cores 时，logical tiling 和 regional tiling 性能接近；随着 NUMA domain 增多，regional tiling 超过 logical tiling，且差距扩大。32 cores 上 regional tiling 达到相对单线程约 $32\times$ 的性能。原因是 regional tiling 把 region 分配到不同 NUMA node，减少远端小粒度访存，把边界通信转化为 ghost exchange，从而更好摊销 latency。

### 6. tiling 对负载均衡的影响

tiling 改善的是 node 内线程负载均衡，而不是直接替代 MPI 级负载均衡。

未 tiling 时，线程若按 grid 分配，负载近似为

$$
W(B_i)\approx |B_i|\,c_i.
$$

AMR grids 大小不一，且不同物理区域代价可能不同，所以 grid-level threading 容易出现

$$
\max_q W_q \gg \frac{1}{Q}\sum_q W_q.
$$

tiling 后，grid 被切成更细的 tile，线程负载变成

$$
W_q=\sum_{T\in\mathcal{T}_q} |T|\,c_T.
$$

当 tile 数远大于线程数时，静态分配也能获得更好的均衡：

$$
N_T \gg Q.
$$

但 tiling 不是万能的。论文特别指出，对于化学反应这类 cell-wise 代价高度不均匀的工作，例如每个 cell 内用 VODE 做隐式反应积分，传统 fine-grained loop-level threading 加 dynamic scheduling 可能更合适。也就是说，tile-level static scheduling 适合 stencil、ghost copy、规则局部计算；对强非均匀局部工作负载，仍需要动态调度或更细粒度任务模型。

---

## 第三节：与 AMReX 演化的关系

### 1. BoxLib with Tiling 与 AMReX 的连续性

BoxLib with Tiling 是 AMReX 的直接前史。两者保持下来的核心思想包括：

- block-structured AMR；
- `Box` / `BoxArray` / `FArrayBox` / `MultiFab` 风格的数据结构；
- `MFIter` 作为遍历和执行策略的入口；
- MPI 负责跨节点分布式内存；
- tile 负责节点内并行和局部性；
- ghost cell fill、copy、coarse-fine synchronization 作为框架原语；
- 应用 kernel 与数据布局、执行后端解耦。

BoxLib 论文的核心设计公式可以概括为：

$$
\text{physics kernel}
+
\text{work box}
+
\text{data pointer}
\quad
\text{分离于}
\quad
\text{parallel execution policy}.
$$

AMReX 继续保留这一思想，只是把 execution policy 从 CPU OpenMP tiling 扩展到了 GPU backend。

### 2. 从 tiling 到 GPU performance portability

BoxLib tiling 的思想是：应用代码只描述“对一个 Box 做什么”，框架决定这个 Box 是整个 grid 还是 tile。

AMReX GPU 化后，这个思想演化为：应用代码只描述“对一个 Box 内的 cells 做什么”，框架决定它变成 CPU loop、OpenMP tile loop，还是 CUDA/HIP/DPC++ kernel。

AMReX 中典型写法是：

```cpp
for (MFIter mfi(mf, TilingIfNotGPU()); mfi.isValid(); ++mfi) {
    Box bx = mfi.tilebox();
    auto arr = mf.array(mfi);
    ParallelFor(bx, [=] AMREX_GPU_DEVICE (int i, int j, int k) {
        ...
    });
}
```

这里的演化关系很清楚：

$$
\text{BoxLib: } \mathrm{MFIter}\rightarrow \mathrm{tilebox}\rightarrow \mathrm{Fortran\ kernel}
$$

变成

$$
\text{AMReX: } \mathrm{MFIter}\rightarrow \mathrm{Box}\rightarrow \mathrm{ParallelFor}\rightarrow \mathrm{backend\ kernel}.
$$

在 CPU 上，tiling 仍然有意义，因为它提升 cache locality 和 OpenMP 粒度。在 GPU 上，通常不再用 CPU 风格 tile 作为并行单位，而是由 GPU kernel 内部的 thread/block 层次完成细粒度并行。因此 AMReX 常见策略是 `TilingIfNotGPU()`：CPU 开 tile，GPU 不开传统 tile，避免把 GPU kernel launch 切得过碎。

### 3. 延续的架构决策

最重要的延续是 **iterator-centered execution abstraction**。BoxLib 没有让每个应用手写 tile loop，AMReX 也没有让每个应用手写 CUDA launch 配置。框架控制遍历与后端，应用控制物理公式。

第二个延续是 **metadata 与数据分离**。`BoxArray`、`DistributionMapping` 等 metadata 可以全局复制并缓存；实际场数据分布式存储。这对 MPI 通信、ghost fill、负载均衡、GPU kernel packing 都是基础。

第三个延续是 **局部 kernel 接口稳定**。BoxLib 中 Fortran kernel 接收 lo/hi 和数组指针；AMReX 中 lambda 接收 $(i,j,k)$ 和 `Array4` 视图。二者都避免把 AMR 全局复杂性暴露给局部 physics kernel。

第四个延续是 **性能优化进入框架层**。BoxLib 把 tiling、ghost fill threading、memory arena 放进框架；AMReX 进一步把 GPU memory arena、pinned memory、managed memory、GPU-aware MPI、kernel fusion、runtime timers 放进框架。

### 4. 被弱化、放弃或重设计的部分

BoxLib 论文中的 TiDA regional tiling 是面向 NUMA CPU 的路径，但在 AMReX 时代，主要硬件压力转向 GPU 和异构节点。因此 TiDA 式 regional tiling 的思想没有作为 AMReX 最显眼的主抽象出现；其“数据 locality 由框架管理”的思想则被 `Arena`、GPU memory spaces、tile/particle binning、backend-aware execution 继承。

BoxLib 中大量应用 kernel 仍是 Fortran subroutine，OpenMP 从 Fortran loop 移到 `MFIter` 层。AMReX 则进一步鼓励 C++ lambda + `ParallelFor`，因为 GPU 需要 device-callable kernel body。也就是说，旧的 “C++ iterator + Fortran kernel” 模型在 GPU portability 上不够自然。

BoxLib 的 tile-level threading 是解决 many-core CPU 的主方案；AMReX 对 GPU 的主方案不是“更多 CPU tile”，而是把 cell loop 提升为后端 kernel。tile 从唯一核心抽象变成多种执行策略之一。

---

## 第四节：与 Doctor 研究方向的关联

### 1. 对 HPC 框架工作的直接启发

Doctor 的论文库主线包含高性能 PDE 求解器、AMR、matrix-free multigrid、JFNK、GPU GMRES、AMReX、几何流体和 AI for Physics。BoxLib with Tiling 对这条线最重要的启发是：高性能框架不能只优化单个 kernel，而要把数据结构、执行粒度、通信模式、内存分配和应用接口一起设计。

BoxLib 的经验可以概括为：

$$
\text{算法正确性}
+
\text{数据局部性}
+
\text{并行粒度}
+
\text{应用可维护性}
$$

必须同时满足。手工 tiling 一个 SMC 应用可以证明性能潜力，但只有把 tiling 下沉到 BoxLib，整个 AMR 生态才真正受益。

对于 Doctor 的高性能 PDE solver framework，这意味着不应让每个物理模块分别处理 OpenMP、CUDA、NUMA、ghost copy、tile size、memory pool。更稳健的做法是建立统一的数据容器和迭代抽象，让物理代码只表达局部离散算子。

### 2. 对 PDE solver 框架的设计原则

第一，执行粒度应独立于数学网格粒度。AMR grid 是负载均衡、通信和元数据管理单位；tile 是 cache 和线程调度单位；GPU thread/block 是设备执行单位。这些层次应解耦：

$$
\text{AMR patch}
\neq
\text{CPU tile}
\neq
\text{GPU block}
\neq
\text{数学控制体}.
$$

第二，tile size 应成为 runtime / algorithm-dependent 参数。不同 kernel 的最优 tile size 不同：低阶 stencil、八阶 stencil、reaction solve、EB cut-cell update、particle deposition、multigrid smoother 都不应强制使用同一 tile shape。

第三，通信和局部计算要共同优化。BoxLib 的 ghost fill 实验证明，随着主 kernel 加速，ghost copy 这类辅助操作会迅速变成瓶颈。PDE 框架应从一开始把 ghost fill、restriction、reflux、packing/unpacking、boundary exchange 纳入并行化和性能模型。

第四，memory allocator 是框架核心组件，不是附属工具。thread-private arena、NUMA-aware region allocation、GPU arena、pinned buffer 本质上都在解决同一个问题：

$$
\text{减少昂贵分配}
+
\text{提高 locality}
+
\text{降低同步竞争}.
$$

### 3. tiling 到 GPU portability 的设计启示

BoxLib 到 AMReX 的演化说明，一个成功的 HPC 抽象不应绑定某一代硬件。tiling 最初服务于 CPU cache 和 OpenMP；后来同一套 “Box + iterator + local kernel” 思想可以演化成 GPU `ParallelFor`。

对 Doctor 如果设计高性能 PDE 框架，建议把核心接口设计成：

$$
\mathcal{K}: (U,\mathrm{Box},\mathrm{Geometry},\mathrm{BC})\mapsto L(U)|_{\mathrm{Box}},
$$

而不是写成固定后端的 loop。然后由框架选择：

$$
\mathrm{execute}(\mathcal{K},B)
=
\begin{cases}
\text{serial loop},\\
\text{OpenMP tile loop},\\
\text{CUDA/HIP/SYCL kernel},\\
\text{task graph node}.
\end{cases}
$$

这样未来从 CPU 到 GPU、从 GPU 到多 GPU、从规则网格到 AMR/EB，都不需要重写物理离散本身。

### 4. 对结构保持流体 / 几何算法的提醒

Doctor 的研究方向中有 Hamiltonian ideal fluid、Clebsch maps、Covector Fluids、Lie-Poisson Neural Networks 等结构保持主题。BoxLib/AMReX 这条线提醒：连续层面的几何结构必须在 AMR 同步和并行执行层面继续成立。

例如如果一个流体算法希望保持质量、环量、helicity 或 Casimir，不能只检查单个 uniform grid kernel。还必须检查：

- tile 分解是否改变浮点归约顺序并影响守恒误差；
- ghost fill 是否与边界条件一致；
- coarse-fine restriction 是否保持目标不变量；
- reflux 是否只修正质量/动量/能量，还是也影响几何约束；
- EB cut-cell redistribution 是否破坏局部结构；
- GPU atomic / reduction 是否引入不可忽略的非确定性漂移。

这可以抽象为一个离散不变量检验：

$$
I_h(U^{n+1})-I_h(U^n)
=
\epsilon_{\mathrm{time}}
+
\epsilon_{\mathrm{space}}
+
\epsilon_{\mathrm{AMR}}
+
\epsilon_{\mathrm{parallel}}.
$$

高质量框架应能把这些误差来源分开测量，而不是只给总误差。

### 5. 对 AI for Physics 的关联

BoxLib with Tiling 不是 AI 论文，但它对 AI for Physics 很关键，因为神经 PDE 模型需要高质量传统 solver 作为数据生成器、基准和混合求解组件。尤其是 neural operator、PINN、learned discretization 如果要进入真实多物理模拟，就必须面对 AMR、ghost cells、coarse-fine synchronization、复杂几何和异构硬件。

一个有价值的研究接口不是只让网络预测点态场值

$$
U_\theta(x,t),
$$

而是让学习模型嵌入框架级算子：

$$
L(U)
=
L_{\mathrm{physics}}(U)
+
L_{\theta}(U),
$$

并要求它满足离散守恒或同步约束，例如

$$
\sum_i U_i^{n+1}\Delta V_i
=
\sum_i U_i^{n}\Delta V_i
+
\Delta t\sum_i S_i\Delta V_i.
$$

BoxLib 的 tiling 经验说明：即使 learned kernel 本身很快，如果它不能适配 tile、ghost、AMR level、GPU backend 和 communication pipeline，也难以成为可用的高性能 PDE 框架组件。

### 6. 总体判断

这篇论文的核心价值不是提出新的 AMR 数学格式，而是展示一个成熟科学计算框架如何把经典 loop transformation 提升为框架级抽象。它解决了三个深层问题：

$$
\text{如何暴露更多并行度？}
$$



## Review Questions
## 公式与代码梳理：Kimi Review 注释

Kimi Code review 进行中但未完成全部任务。已修正：
1.  重叠语义更正
2. Cache/TLB 性能模型补充假设说明
3. NUMA 内存时间公式补充带宽模型
4. OpenMP/MFIter 代码块改写

**剩余工作：** Review Questions 未追加，格式差异检查未执行。

## Review Questions
⏳ 待补充 Kimi Code review
