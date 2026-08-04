# Roofline：多核架构的洞见型可视性能模型 / Roofline: An Insightful Visual Performance Model for Multicore Architectures

**作者：** Samuel Williams, Andrew Waterman, David Patterson（UC Berkeley, Parallel Computing Laboratory）
**期刊：** Communications of the ACM, Vol. 52, No. 4, pp. 65-76, April 2009
**DOI：** [https://doi.org/10.1145/1498765.1498785](https://doi.org/10.1145/1498765.1498785)
**arXiv：** 无（LBNL 技术报告版：OSTI [10.2172/1407078](https://doi.org/10.2172/1407078)）
**阅读状态：** 🔬 精读（Doctor 指定）
**流程状态：** ①元数据 ✓ | ②初稿 ✓ | ③评估 ✓(精读) | ④补充 ✓ | ⑤索引 ✓ | ⑥review ✓ | ⑦提交 ⏳

---

## 摘要

### 中文翻译
我们提出一个易于理解、可视化的性能模型，为程序员和架构师改进浮点计算的并行软件与硬件提供洞察。该模型（"Roofline"）把浮点峰值性能与内存系统（DRAM）的峰值带宽置于一张二维图中，横轴为操作强度（每字节 DRAM 流量的浮点操作数），纵轴为可实现性能。Roofline 模型把 3C 缓存模型（强制/容量/冲突失效）与局部性优化联系起来，回答了一个基本问题：给定一个优化，代码将（或不会）在什么位置触碰 roofline？我们通过分析四个代表性 kernel（LBMHD、Stencil、3-D FFT、SpMV）的优化，以及 GPU/Larrabee 的多级 memory roof 扩展来说明模型的运用。Roofline 模型还给程序员一个重要的（重新）教育工具，并给架构师提出一个本质问题：芯片应如何平衡浮点峰值与 DRAM 带宽？

### 原文
> We propose an easy-to-understand, visual performance model that offers insights to programmers and architects on improving parallel software and hardware for floating point computations. The model, which we call the "Roofline," plots floating-point peak performance and the peak memory system (DRAM) bandwidth on a single two-dimensional graph, with operational intensity (floating-point operations per byte of DRAM traffic) on the x-axis and achievable performance on the y-axis. The Roofline model ties together the 3Cs cache model (compulsory, capacity, conflict misses) with locality optimizations and answers a fundamental question: given an optimization, where will a code touch (or not touch) the roofline? We illustrate the use of the model by analyzing three optimizations of a numerical method, a sparse linear algebra routine, and three optimizations targeted at GPUs. The Roofline model also provides an important (re)educational tool for programmers and poses an essential question for architects: how should a chip balance floating-point peak and DRAM bandwidth?

---

## 文章总结

### 1. 解决什么问题？
浮点计算程序的性能瓶颈到底是"计算不够快"还是"数据喂不饱"？程序员需要直观判断：优化应该往提高计算效率方向（SIMD、ILP、降低指令开销）还是改善数据局部性方向（cache blocking、数据布局）走；架构师需要知道芯片的浮点峰值与内存带宽如何平衡。缺乏一个把硬件能力与程序特征统一起来的简单可视模型。

### 2. 用了什么方法论？
- **Roofline 二维图**：x 轴 = 操作强度 $I$（flops/byte，程序特征），y 轴 = 可实现性能（flops/s）；天花板：水平线 = 峰值浮点性能 $P$，斜线 = 峰值带宽 $B \times I$；可实现性能 $\le \min(P, B\cdot I)$，即图中两条线形成的"屋顶"；
- **3C 模型对接**：把强制/容量/冲突失效与操作强度的关系讲清——cache blocking 改变有效操作强度——容量/冲突失效的直接作用是增加 $Q_{\mathrm{DRAM}}$、降低 $I$，从而把"优化"翻译成"在图上移动点的位置"；
- **案例分析**：四个代表性 kernel——稀疏 SpMV（操作强度低的典型，roofline 显示其受带宽限制）、LBMHD、Stencil、3-D FFT；另以 GPU/Larrabee 为扩展案例说明多级 memory roofs（后者为结合 WarpX 姊妹篇的扩展解释，非原文独立分类）；
- **硬件特征测量**：用硬件规格或浮点 microbenchmark 测峰值性能，用 STREAM/专门 streaming microbenchmark 测可持续 DRAM 带宽——roofline 的"屋顶"由实测而非纸面规格决定。

### 3. 主要结论是什么？
- Roofline 直观回答"计算受限 vs 带宽受限"：点落在斜线上=带宽受限（应提高局部性/操作强度），落在水平线下=计算效率受限（应提高 SIMD/ILP）；
- 3C 模型与操作强度的对接使优化效果可预测：spatial blocking 等优化把点沿 x 轴右移；
- 稀疏矩阵 SpMV 等低强度应用**本质带宽受限**，单纯优化计算无法突破；
- 给架构师的启示：芯片浮点峰值与 DRAM 带宽的平衡（如"每 flop 配多少字节带宽"）决定可支撑的操作强度上限；该模型成为此后十余年 HPC 性能分析的事实标准（并被扩展为 cache-aware roofline、instruction roofline 等）。

---

## 价值评估
Doctor 指定精读

## 公式与代码梳理

### 1. 模型数学逐项推导

Roofline 的核心变量是操作强度 $I$，定义为：

$$
I=\frac{W}{Q_{\mathrm{DRAM}}}
$$

其中 $W$ 是完成某个 kernel 所执行的“有用操作数”，在本文主线中就是 double precision floating-point operations；$Q_{\mathrm{DRAM}}$ 是经过 cache hierarchy 过滤后，真正发生在 cache 与 DRAM 之间的数据流量，单位 bytes。因此本文不用传统的 arithmetic intensity / machine balance 定义：

$$
\frac{\mathrm{flops}}{\mathrm{bytes\ between\ processor\ and\ cache}}
$$

而是使用：

$$
\frac{\mathrm{flops}}{\mathrm{bytes\ between\ cache\ hierarchy\ and\ DRAM}}
$$

原因是：cache 命中、prefetch、blocking、no-allocate store、memory affinity 等优化的效果，最终都体现为 DRAM 流量减少或有效 DRAM 带宽提高。如果把流量计在 processor-cache 边界，cache blocking 并不会改变 $I$；而本文正是要把“局部性优化”翻译成 roofline 图上的位置变化。

给定硬件实测浮点峰值 $P_{\mathrm{peak}}$ 与可持续内存带宽 $B_{\mathrm{mem}}$，kernel 可达到性能 $P$ 满足：

$$
P \le P_{\mathrm{peak}}
$$

以及

$$
P \le B_{\mathrm{mem}} I
$$

合并得到 roofline 上界：

$$
P \le \min(P_{\mathrm{peak}}, B_{\mathrm{mem}} I)
$$

在 log-log 图上，$P_{\mathrm{peak}}$ 是水平 roof；$B_{\mathrm{mem}}I$ 是斜率为 1 的 memory roof。两者交点称为 ridge point，其横坐标为：

$$
I_{\mathrm{ridge}}
=
\frac{P_{\mathrm{peak}}}{B_{\mathrm{mem}}}
$$

含义是“达到浮点峰值所需的最低操作强度”。若 kernel 的 $I<I_{\mathrm{ridge}}$，则即使计算单元足够快，DRAM 也喂不饱计算，性能受限于：

$$
P \approx B_{\mathrm{mem}} I
$$

若 $I>I_{\mathrm{ridge}}$，则内存带宽足以支撑峰值计算，性能上限转为：

$$
P \approx P_{\mathrm{peak}}
$$

例如 Opteron X2 的实测参数约为：

$$
P_{\mathrm{peak}}=17.6\ \mathrm{GFlop/s},\qquad
B_{\mathrm{mem}}=15\ \mathrm{GB/s}
$$

所以：

$$
I_{\mathrm{ridge}}\approx \frac{17.6}{15}\approx 1.17\ \mathrm{Flop/Byte}
$$

文中图示近似把 ridge 放在 $1$ 附近。Opteron X4 浮点峰值提高约四倍而内存带宽近似不变，ridge 从约 $1$ 右移到 $4.4$，说明同样的内存系统被更多浮点单元“稀释”后，程序必须有更高 $I$ 才能吃满芯片。

### 2. 3C 模型对接

把总 DRAM 流量分解成 3C 模型对应的部分：

$$
Q_{\mathrm{DRAM}}
=
Q_{\mathrm{compulsory}}
+
Q_{\mathrm{capacity}}
+
Q_{\mathrm{conflict}}
$$

则：

$$
I
=
\frac{W}{
Q_{\mathrm{compulsory}}
+
Q_{\mathrm{capacity}}
+
Q_{\mathrm{conflict}}
}
$$

Compulsory misses 给出最小不可避免 DRAM 流量，因此给出理论最高操作强度：

$$
I_{\max}
=
\frac{W}{Q_{\mathrm{compulsory}}}
$$

Capacity misses 和 conflict misses 会增加额外 DRAM 流量，使实际操作强度下降：

$$
I_{\mathrm{actual}}
\le
I_{\max}
$$

cache blocking 的数学作用不是直接提高 $W$，而是减少 $Q_{\mathrm{capacity}}$：

$$
Q_{\mathrm{capacity}}^{\mathrm{blocked}}
<
Q_{\mathrm{capacity}}^{\mathrm{unblocked}}
$$

因此：

$$
I_{\mathrm{blocked}}
=
\frac{W}{
Q_{\mathrm{compulsory}}
+
Q_{\mathrm{capacity}}^{\mathrm{blocked}}
+
Q_{\mathrm{conflict}}
}
>
I_{\mathrm{unblocked}}
$$

图上的表现是点向右移动。如果右移跨过 ridge point，优化性质会从“继续做内存优化”变为“开始需要 ILP/SIMD/FMA/指令混合优化”。

padding 的作用是减少 conflict misses：

$$
Q_{\mathrm{conflict}}^{\mathrm{padded}}
<
Q_{\mathrm{conflict}}^{\mathrm{unpadded}}
$$

no-allocate store 的作用是避免把马上要覆盖的数据先读入 cache，从而减少 write-allocate 流量：

$$
Q_{\mathrm{DRAM}}^{\mathrm{no\ alloc}}
<
Q_{\mathrm{DRAM}}^{\mathrm{write\ alloc}}
$$

这同样把点向右移动。文中特别强调：加大 cache 不必然提高 $I$。如果 autotuning 已经接近 compulsory traffic，则：

$$
Q_{\mathrm{capacity}}\approx 0,\qquad Q_{\mathrm{conflict}}\approx 0
$$

再增大 cache 对 $I$ 几乎无效。只有像 3-D FFT 这种工作集可因更大 cache 捕获整个 plane 的情形，cache size 才会明显改变 $Q_{\mathrm{capacity}}$ 与 $I$。

### 3. 案例分析：三种数值方法与 SpMV

#### LBMHD

LBMHD 的初始操作强度约为：

$$
I\approx 0.70\ \mathrm{Flop/Byte}
$$

使用 no-allocate store 后，可减少写分配导致的额外 DRAM traffic，使操作强度提高到：

$$
I\approx 1.07\ \mathrm{Flop/Byte}
$$

图上移动是向右移动。结论是：LBMHD 不像 SpMV 那样极端低强度，它处在 memory roof 与 compute ceilings 都相关的区域；因此既需要内存优化，也需要计算优化。对 T2+，因为 ridge point 只有约 $0.33$，LBMHD 的 $I$ 已经高于 ridge，主要转向计算 ceiling；对 Xeon/X4，则仍常受 memory ceiling 约束。

#### Stencil

文中 stencil 来自 3-D explicit heat equation，在 $256^3$ 均匀网格上使用 7-point stencil。每个点更新使用中心点和 6 个邻点，计算量为 8 flops。write-allocate 架构下 compulsory traffic 约为 24 bytes，因此：

$$
I_{\mathrm{stencil}}
=
\frac{8}{24}
\approx 0.33\ \mathrm{Flop/Byte}
$$

若 cache blocking / time blocking 能复用邻近平面或时间步数据，则 $Q_{\mathrm{capacity}}$ 下降，点向右移动。但在本文四台机器的实测中，stencil 仍多处在 memory-bound 区域，尤其对 Xeon/X4 这类 ridge 很高的机器，$0.33$ 到 $0.50$ 的强度远远不够触及浮点峰值。

#### 3-D FFT

3-D FFT 的 $I$ 随问题规模与 cache 可容纳的工作集变化。文中给出：

$$
I_{128^3}\approx 1.09,\qquad
I_{512^3}\approx 1.41
$$

在 Xeon/X4 上，如果 $128\times128$ plane 能装入 cache，temporal locality 改善，$128^3$ 的操作强度可提高到：

$$
I_{128^3,\mathrm{cached\ plane}}\approx 1.64
$$

图上表现仍是向右移动。FFT 的结论比 stencil 更微妙：它不是固定低强度 kernel，而是 cache capacity 与问题规模会显著改变其位置。对 Xeon/X4，周围 ceilings 多为 memory；对 T2+/Cell，FFT 更可能被 compute ceiling 夹住。

#### SpMV

SpMV 为：

$$
y = A x
$$

每个非零元通常做一次乘法加一次加法：

$$
W_{\mathrm{per\ nnz}}\approx 2\ \mathrm{flops}
$$

但至少要读取矩阵值、列索引、向量 $x$ 的间接访问，还要读写或累加 $y$。以 CSR 粗略估计：

$$
Q_{\mathrm{per\ nnz}}
\gtrsim
8\ \mathrm{bytes\ value}
+
4\ \mathrm{bytes\ index}
+
8\ \mathrm{bytes\ x}
+
\mathrm{amortized\ y/row\ traffic}
$$

因此：

$$
I_{\mathrm{SpMV}}
\approx 0.17\sim 0.25\ \mathrm{Flop/Byte}
$$

文中指出 register blocking 可把 SpMV 从约 $0.17$ 提高到约 $0.25$。即便如此，它仍低于四台 multicore 的 ridge point，所以本质是 bandwidth-bound。图上优化主要是轻微右移和提高有效 memory ceiling，例如压缩 index、压缩 nonzero subblocks、改善 locality；单纯追求 SIMD/FMA 无法突破：

$$
P_{\mathrm{SpMV}}
\lesssim
B_{\mathrm{mem}}\times 0.25
$$

这解释了为什么传统 SpMV 常低于峰值浮点性能的 10%。

### 4. GPU 三类优化的 roofline 解释

全文技术报告版在“Roofline 是否必须用 DRAM 带宽”小节中把 GPU/Larrabee 作为扩展案例：同一个模型可同时画 L1、L2、DRAM 多条 memory roofs（在现代 GPU 上可对应扩展到 L1/L2/HBM）。对 GPU 来说，关键不是只问“算力峰值多高”，而是问某个 kernel 的 working set 会落在哪一级 memory roof 上。

第一类是 working set 能装入 L1 的隐式 PDE solver。此时横轴不再必须是：

$$
I_{\mathrm{DRAM}}=\frac{W}{Q_{\mathrm{DRAM}}}
$$

而可改为：

$$
I_{\mathrm{L1}}=\frac{W}{Q_{\mathrm{L1}}}
$$

若 L1 bandwidth 足以支撑峰值计算，则图上的点已经触及或接近 compute roof，结论是无需优先做 blocking。

第二类是 working set 太大、不能装入 cache 的显式 PDE solver。此时点按 DRAM 流量计量，通常落在斜 roof 下方。cache blocking 的作用是通过减少 capacity/conflict traffic 提高 $I$（部分情形还能改善可持续带宽 ceiling）：

$$
Q_{\mathrm{DRAM}}^{\mathrm{blocked}}
<
Q_{\mathrm{DRAM}}^{\mathrm{unblocked}}
$$

从而：

$$
I_{\mathrm{blocked}}>I_{\mathrm{unblocked}}
$$

图上向右移动，并可能同时从 DRAM roof 受限转向 L2/L1 roof 或 compute roof。

第三类是使用多级 roofline 判断 cache reuse 是否真实发生。若同一 kernel 用 L1、L2、HBM 流量计算出的 $I$ 基本重合，说明 cache reuse 很差；若（注意：这里的 $I$ 是按各级实际流量分别计算的 apparent arithmetic intensity，与主线的单一 DRAM 操作强度是不同口径）：

$$
I_{\mathrm{HBM}} > I_{\mathrm{L2}} > I_{\mathrm{L1}}
$$

则说明大量访问被 cache 层吸收，越靠近处理器的层级承担了更多复用。这个思路在 WarpX 论文中被直接使用：粒子排序后，current deposition 的点接近 L2 streaming limit；fused gather+push 虽有 cache reuse，但仍更可能受 HBM bandwidth 限制。

### 5. 硬件测量方法

Roofline 的 roof 应优先使用实测值，而不是纸面规格。浮点峰值可从硬件规格估算，也可用 microbenchmark 测得：

$$
P_{\mathrm{peak}}
\approx
\mathrm{cores}
\times
\mathrm{frequency}
\times
\mathrm{SIMD\ lanes}
\times
\mathrm{flops/cycle}
$$

但真实可达上限还受 FMA、add/mul mix、ILP、SIMD 编译质量限制。因此文中加入 computational ceilings：没有 ILP/SIMD、add/mul 不平衡、不能充分发射 FP 指令时，实际水平 roof 会低于理论峰值。

内存带宽可用 STREAM 或专门写的 streaming microbenchmarks 测量。文中强调的 $B_{\mathrm{mem}}$ 是 sustained DRAM bandwidth，而不是 DRAM pin bandwidth：

$$
B_{\mathrm{usable}}
\ne
B_{\mathrm{pin\ spec}}
$$

原因包括 prefetch 是否有效、访问是否 unit stride、NUMA memory affinity、cache line 写分配、coherency traffic、TLB miss、软件预取和数据对齐等。Roofline 用“实测屋顶”更可靠，因为它描述的是程序真正能长期利用的 steady-state bandwidth。

### 6. 架构平衡问题

ridge point 也可以看成芯片的“浮点峰值 / 内存带宽”比例：

$$
I_{\mathrm{ridge}}
=
\frac{P_{\mathrm{peak}}}{B_{\mathrm{mem}}}
$$

其倒数是每 flop 可分到的 DRAM 带宽配额：

$$
\mathrm{bytes/flop}
=
\frac{B_{\mathrm{mem}}}{P_{\mathrm{peak}}}
=
\frac{1}{I_{\mathrm{ridge}}}
$$

若 Xeon ridge point 为 $6.7$，则：

$$
\frac{1}{6.7}
\approx
0.149\ \mathrm{Byte/Flop}
$$

即每个 flop 只有约 $0.149$ byte DRAM 供应；换成 double operand：

$$
6.7\ \mathrm{Flop/Byte}
\times
8\ \mathrm{Byte}
\approx
54\ \mathrm{Flops/operand}
$$

文中总结为：x86 两台机器的 ridge point 为 $4.4$ 与 $6.7$，意味着每个 8-byte DRAM operand 需要约 35 到 55 flops 才能触及峰值；但 16 个 kernel-machine 组合的操作强度范围只有 $0.25$ 到 $1.64$，中位数约 $0.60$。这说明当代多核芯片的浮点峰值增长快于 DRAM 带宽增长，架构越来越“不平衡”。作者对未来的判断是：如果架构师希望真实程序更容易达到峰值，就必须把 ridge point 作为设计指标，而不能只提高 peak flop/s。

### 7. 与库内论文关联

Roofline 在 WarpX GPU 移植中的角色，是为“少存、少搬、必要时重算”提供定量语言。gather+push 融合前，粒子上持久保存插值场值，内存流量可抽象为：

$$
Q_{\mathrm{old}}
=
Q_{\mathrm{gather}}
+
Q_{\mathrm{store\ fields}}
+
Q_{\mathrm{load\ fields}}
+
Q_{\mathrm{push}}
$$

融合后去掉粒子场值的存储与再读取：

$$
Q_{\mathrm{new}}
\approx
Q_{\mathrm{gather}}
+
Q_{\mathrm{push}}
$$

必要的重复 gather 主要增加 flops：

$$
F_{\mathrm{new}}
=
F_{\mathrm{old}}
+
F_{\mathrm{regather}}
$$

因此：

$$
AI_{\mathrm{fused}}
=
\frac{F_{\mathrm{new}}}{Q_{\mathrm{new}}}
>
\frac{F_{\mathrm{old}}}{Q_{\mathrm{old}}}
=
AI_{\mathrm{separate}}
$$

这正是 Roofline 的典型判断：在 memory-bound GPU kernel 中，减少字节通常比节省少量 flops 更重要。WarpX 报告该优化使 memory footprint 降低约 $1.6\times$，整体 runtime 提升约 $25\%$；粒子排序进一步通过 cache reuse 改变 L1/L2/HBM 三个层级上的 apparent arithmetic intensity。

ECM 论文则是 Roofline 的细化版本。Roofline 给出芯片级 light-speed 上界：

$$
P_{\mathrm{Roofline}}
=
\min(P_{\mathrm{peak}},B_{\mathrm{mem}}I)
$$

ECM 把单核执行时间拆为 in-core execution 与 cache/memory transfer：

$$
T_{\mathrm{core}}
=
\max(T_{\mathrm{nOL}},T_{\mathrm{OL}})
$$

$$
T_{\mathrm{ECM}}
=
\max(T_{\mathrm{nOL}}+T_{\mathrm{data}},T_{\mathrm{OL}})
$$

其中 $T_{\mathrm{nOL}}$ 是不可与数据传输重叠的 core 时间，$T_{\mathrm{OL}}$ 是可重叠部分，$T_{\mathrm{data}}$ 是 L1/L2/L3/DRAM 各层 cache line transfer 时间之和。ECM 的多核饱和预测写为：

$$
P(n)
=
\min\left(
nP_{\mathrm{ECM}}^{\mathrm{mem}},
\frac{b_S}{B_C}
\right)
$$

其中 $B_C$ 是 code balance，即 computational intensity 的倒数：

$$
B_C=\frac{Q_{\mathrm{mem}}}{W}=\frac{1}{I}
$$

所以 ECM 与 Roofline 的关系是：Roofline 用 $P_{\mathrm{peak}}$ 近似 core 侧上限；ECM 用真实单核执行与各级 cache transfer 预测替代这个粗略上限，尤其适合 stencil 这种 L1/L2/L3 传输不可忽略的 kernel。

对 Doctor 的高性能框架，直接用法是把每个核心 kernel 都放进同一个诊断模板：

$$
I_k=\frac{W_k}{Q_{k,\mathrm{DRAM}}},\qquad
P_k\le \min(P_{\mathrm{peak}},B_{\mathrm{mem}}I_k)
$$

然后按图上位置决定优化优先级：

- 若 $I_k<I_{\mathrm{ridge}}$：优先减少流量，做 blocking、fusion、SoA/layout、压缩索引、减少临时数组、NUMA affinity、particle sorting；
- 若 $I_k>I_{\mathrm{ridge}}$ 但性能仍低：优先查 SIMD、FMA、ILP、分支、寄存器压力、occupancy、指令 mix；
- 若同一 kernel 在 L1/L2/DRAM roofline 上位置差异很大：说明 cache reuse 已经发生，应进一步看哪一级 bandwidth 成为新瓶颈；
- 若 Roofline 判断过粗，特别是 stencil、long-range stencil、matrix-free operator：接 ECM，逐层估算 cache line traffic 与 single-core saturation point。

这套方法可以作为框架级性能分析规范：每个新算子不仅报告 wall time，还报告 $W$、$Q_{\mathrm{DRAM}}$、$I$、达到的 $P$、相对 roof 的距离，以及优化后点在图上的移动方向。


## Review Questions

1. 对 AMR/流体框架，能否为 stencil、projection/Poisson、particle-mesh gather/deposition、reflux/ghost fill 等核心算子统一记录 $W$、$Q_{\mathrm{DRAM}}$、$I$ 与 roof 利用率，形成类似 AMReX/WarpX 的自动性能诊断流水线？
2. 在高阶/矩阵自由 PDE 或几何流体离散中，算子融合、重计算、临时数组消除会提高 $I$，但可能增加寄存器压力或降低 occupancy；如何用 Roofline + ECM 判断“多算少搬”何时真的优于分阶段计算？
3. 对多级存储 GPU 和 AMR 非均匀 workload，单一 DRAM roofline 难以解释 cache reuse、原子写、MPI/ghost communication；性能模型是否应扩展为 hierarchical roofline + communication roofline，并与粒子排序、box size、负载均衡策略联动？

## Kimi Code Review 结论（2026-08-04）

- 主公式与核心数值基本正确：$I=W/Q_{\mathrm{DRAM}}$、$P\le\min(P_{\mathrm{peak}}, B_{\mathrm{mem}}I)$、ridge point、Opteron X2/X4、SpMV、Stencil、FFT、Xeon/T2+/Cell ridge 等均与技术报告主线一致。
- 已修正 7 处：
  1. 冲突失效表述改为“容量/冲突失效增加 $Q_{\mathrm{DRAM}}$、降低 $I$”；
  2. 案例分析改为与原文一致的四个 kernel（SpMV、LBMHD、Stencil、3-D FFT），GPU 部分标注为结合 WarpX 姊妹篇的扩展解释；
  3. 删去 LINPACK 提法，改为“硬件规格或浮点 microbenchmark 测峰值、STREAM/streaming microbenchmark 测持续带宽”；
  4. cache blocking 表述补充“减少 capacity/conflict traffic 提高 $I$（部分情形改善带宽 ceiling）”；
  5. “DRAM/HBM”改为“L1/L2/DRAM（现代 GPU 扩展到 HBM）”，消除时代错置；
  6. 多级 $I$ 标注为 apparent arithmetic intensity，与主线单一 DRAM 口径区分；
  7. 摘要中译同步更新为四个 kernel + 多级 memory roof 扩展。
- Markdown/语法检查未发现 $...$、$$...$$ 不成对或标题层级异常。
