# 用 Execution-Cache-Memory 模型量化 stencil 计算性能瓶颈 / Quantifying Performance Bottlenecks of Stencil Computations Using the Execution-Cache-Memory Model

**作者：** Holger Stengel, Jan Treibig, Georg Hager, Gerhard Wellein（FAU Erlangen-Nürnberg, RRZE）
**期刊：** Proceedings of the 29th ACM International Conference on Supercomputing (ICS '15), pp. 209-219, 2015
**DOI：** [https://doi.org/10.1145/2751205.2751240](https://doi.org/10.1145/2751205.2751240)
**arXiv：** [1410.5010](https://arxiv.org/abs/1410.5010)（2014-10-18 首发，v2 2015-01-17）
**阅读状态：** 🔬 精读（Doctor 指定）
**流程状态：** ①元数据 ✓ | ②初稿 ✓ | ③评估 ✓(精读) | ④补充 ✓ | ⑤索引 ✓ | ⑥review ✓ | ⑦提交 ✓

---

## 摘要

### 中文翻译
规则网格上的 stencil 算法出现在计算科学的许多领域，人们投入了大量精力做优化实现。这类工作通常没有性能模型的指导来提供预期加速比的估计。通过性能建模理解性能特性与瓶颈，能对有希望的优化方向给出清晰视野。本文精化了新近发展的 Execution-Cache-Memory（ECM）模型，并用它量化 stencil 算法在一款当代 Intel 处理器上的性能瓶颈。这包括应用模型对典型"边角情形"stencil 循环内核给出单核性能与可扩展性预测。在 ECM 模型指导下，我们精确量化了"layer condition"（估计内存层次数据流量所需条件）的意义，并研究空间分块、强度削减、时间分块等典型优化手段的预期收益。

### 原文
> Stencil algorithms on regular lattices appear in many fields of computational science, and much effort has been put into optimized implementations. Such activities are usually not guided by performance models that provide estimates of expected speedup. Understanding the performance properties and bottlenecks by performance modeling enables a clear view on promising optimization opportunities. In this work we refine the recently developed Execution-Cache-Memory (ECM) model and use it to quantify the performance bottlenecks of stencil algorithms on a contemporary Intel processor. This includes applying the model to arrive at single-core performance and scalability predictions for typical "corner case" stencil loop kernels. Guided by the ECM model we accurately quantify the significance of "layer conditions," which are required to estimate the data traffic through the memory hierarchy, and study the impact of typical optimization approaches such as spatial blocking, strength reduction, and temporal blocking for their expected benefits.

---

## 文章总结

### 1. 解决什么问题？
stencil 计算（低计算强度 + 迭代性）是计算科学的核心循环模式，但其优化（SIMD、cache blocking、并行化）通常缺乏定量模型指导，难以预估优化收益、判断瓶颈在计算还是在内存层次。本文要解决：如何用 ECM 模型在当代多核处理器上**精确量化** stencil 内核的单核性能与扩展性瓶颈，并**预测**各类优化（空间分块/强度削减/时间分块）的收益。

### 2. 用了什么方法论？
- **ECM 模型（Execution-Cache-Memory）**：把单核执行时间分解为纯计算/指令发射部分与各级内存层次（L1/L2/L3/DRAM）数据传递部分；通过对 stencil 循环的数据流量建模，按非重叠规则累加各层传输贡献，并与可重叠的 core 时间取 max，给出单核运行时间的解析预测；
- **Layer condition（层条件）**：精化用于估计 stencil 数据流量的关键条件——数据在内存层次中"驻留层"的判定，决定流量按哪一层计算（这是 ECM 对 stencil 应用时的核心精化点）；
- **可扩展性预测**：结合 socket 带宽上限与共享 L3 下的 LC 修正，预测多核扩展曲线；
- **验证与优化评估**：在当代 Intel 处理器上用"边角情形"stencil 内核验证，并定量评估 spatial blocking、strength reduction（本文案例中主要是除法替换为乘法）、temporal blocking 的收益。

### 3. 主要结论是什么？
- ECM 模型能**准确量化** stencil 单核性能瓶颈与多核扩展行为，预测与实测吻合良好；
- **layer condition 是关键**：流量估计必须基于正确的驻留层假设，否则模型误差显著；文中精确刻画了各内核满足/违背 layer condition 的情形；
- 优化收益可**事前预测**：例如 temporal blocking 在单核与全 socket 场景下的收益、空间分块的最优块大小、强度削减的量化收益——模型为"是否值得优化"提供判断依据；
- 为 stencil 这类低计算强度循环提供了一条"建模 → 定位瓶颈 → 选择优化"的完整方法论，弥补了纯试错式优化的空白。

---

## 价值评估
Doctor 指定精读

## 公式与代码梳理

### 1. ECM 模型逐项拆解

ECM（Execution-Cache-Memory）模型的目标不是给一个抽象上界，而是预测某个循环内核完成一个固定“工作单元”需要多少 CPU cycles。对 64B cache line 和 double precision stride-1 访问，一个自然工作单元通常是 8 次标量迭代；stencil 场景中论文用 LUP（lattice site update）作为性能单位。

核心分解是：

$$
T_{\mathrm{core}}=\max_i T_{u_i}
$$

其中 $T_{u_i}$ 是各执行资源/端口完成该循环体指令所需周期数。然后把 core 时间拆成两部分：

$$
T_{\mathrm{core}}=\max(T_{\mathrm{nOL}},T_{\mathrm{OL}})
$$

- $T_{\mathrm{OL}}$：overlapping core time，可与 cache/memory 数据传输重叠的执行部分，例如算术指令、部分 store、前端气泡等；
- $T_{\mathrm{nOL}}$：non-overlapping core time，不可与数据传输重叠的执行部分。本文在 Intel Sandy Bridge 上把 load retire 对 L1 的占用视为主要 $T_{\mathrm{nOL}}$；
- $T_{\mathrm{L1L2}}$：L1 与 L2 之间传输所需周期；
- $T_{\mathrm{L2L3}}$：L2 与 L3 之间传输所需周期；
- $T_{\mathrm{L3Mem}}$：L3 与 DRAM 之间传输所需周期；
- $T_{\mathrm{data}}$：从目标驻留层一路到 L1 的数据传输总时间；内存驻留时含 L1-L2、L2-L3、L3-Mem 三项，L2/L3 驻留时只累加到相应层为止。

ECM 的关键合并规则是：load 相关 core 部分与 cache line 传输不重叠，各层数据传输彼此串行；但 $T_{\mathrm{OL}}$ 可以与这些传输重叠。因此：

$$
T_{\mathrm{data}} =
T_{\mathrm{L1L2}}+
T_{\mathrm{L2L3}}+
T_{\mathrm{L3Mem}}
$$

$$
T_{\mathrm{ECM}}=
\max(T_{\mathrm{nOL}}+T_{\mathrm{data}},T_{\mathrm{OL}})
$$

论文使用简写：

$$
\{T_{\mathrm{OL}}\parallel T_{\mathrm{nOL}}
\mid T_{\mathrm{L1L2}}
\mid T_{\mathrm{L2L3}}
\mid T_{\mathrm{L3Mem}}\}
$$

例如 DAXPY 在 Sandy Bridge 上为：

$$
\{4\parallel4\mid6\mid6\mid13\}\ \mathrm{cy}
$$

如果数据在 L1/L2/L3/内存中，对应预测写成：

$$
T_{\mathrm{ECM}}=\{4\rceil10\rceil16\rceil29\}\ \mathrm{cy}
$$

含义是：

$$
T_{\mathrm{L1}}=\max(4,4)=4
$$

$$
T_{\mathrm{L2}}=\max(4,4+6)=10
$$

$$
T_{\mathrm{L3}}=\max(4,4+6+6)=16
$$

$$
T_{\mathrm{Mem}}=\max(4,4+6+6+13)=29
$$

单核性能由工作量除以预测时间：

$$
P_{\mathrm{ECM}}=\frac{W f}{T_{\mathrm{ECM}}}
$$

其中 $f$ 为时钟频率，$T_{\mathrm{ECM}}$ 以周期计；若 $T_{\mathrm{ECM}}$ 已换算为秒，则为 $W/T_{\mathrm{ECM}}$。

若工作量 $W$ 用 LUP 表示，则得到 LUP/s；若用 flops 表示，则得到 flop/s。

这与 Roofline 的本质区别是：Roofline 把性能限制写成一个全局上界：

$$
P \le \min(P_{\max}, B_{\mathrm{mem}}\cdot I)
$$

或用 code balance $B_C=1/I$ 写成：

$$
P \le \min(P_{\max}, \frac{B_{\mathrm{mem}}}{B_C})
$$

Roofline 只看“计算峰值”和“DRAM 带宽”两条屋顶线，适合判断宏观的 compute-bound / bandwidth-bound。ECM 则把执行时间拆成可加的层级贡献，显式区分 $T_{\mathrm{nOL}}$、$T_{\mathrm{OL}}$、L1-L2、L2-L3、L3-DRAM。它不是严格上界，实测值可以略高于 ECM 预测；但它能回答 Roofline 不擅长回答的问题：性能为什么在相同 DRAM code balance 下仍随 layer condition 改变？瓶颈到底在 load port、L2/L3 传输，还是 DRAM？

### 2. Layer Condition 精读

Layer condition（LC）是 stencil 流量估计的前提。stencil 不是简单 streaming kernel：同一网格层上的数据会被相邻迭代重复使用。如果需要复用的“层”能驻留在某级 cache 中，则下一层内存层次看到的流量会显著下降；如果放不下，则这些复用退化成 cache miss，流量上升。

以 2D five-point Jacobi 为例：

```c
for (j=1; j<Nj-1; ++j)
  for (i=1; i<Ni-1; ++i)
    b[j][i] = (a[j][i-1] + a[j][i+1]
             + a[j-1][i] + a[j+1][i]) * s;
```

沿 $i$ 方向连续访问，$a[j][i-1]$ 通常已经在 L1，因为它在前两次 inner-loop 迭代中作为 $a[j][i+1]$ 被加载过。真正决定 cache 层流量的是 $j$ 方向的三行：

$$
a[j-1][:],\quad a[j][:],\quad a[j+1][:]
$$

若 cache level $k$ 的容量为 $C_k$，按经验假设其中约一半可用于 layer 存储，因此 five-point Jacobi 的 LC 为：

$$
3\cdot N_i\cdot 8B < \frac{C_k}{2}
$$

更一般地，对外层方向 stencil 半径 $r$：

$$
(2r+1)\cdot N_i\cdot s < \frac{C_k}{2}
$$

其中 $s$ 是单个网格值字节数。若有 blocking（对 2D Jacobi 的 inner blocking 情形），把完整 leading dimension $N_i$ 替换为 inner block size $b_i$：

$$
3\cdot b_i\cdot 8B < \frac{C_k}{2}
$$

若 cache 是多线程共享的 L3，还要乘以线程数 $n$：

$$
3\cdot b_i\cdot n\cdot 8B < \frac{C_3}{2}
$$

流量估计按“LC 在哪一层满足”逐层变化。对 2D Jacobi，一个工作单元是 8 LUP，double precision，cache line 为 64B：

- 输出数组 $b$：store miss 触发 write-allocate，加上最终 evict，共 2 条 stream；
- 输入数组 $a$：若 LC 满足，则外层只需持续加载新的一行，相当于 1 条 stream；
- 因此 LC 满足时，下一层看到 3 条 stream：

$$
B_C^{\mathrm{LC}} = 3\cdot 8B = 24B/\mathrm{LUP}
$$

- 若 LC 不满足，除 $a[j][i-1]$ 的 L1 复用外，其余需要从下一层取，合计 5 条 stream：

$$
B_C^{\neg\mathrm{LC}} = 5\cdot 8B = 40B/\mathrm{LUP}
$$

把它转成每个工作单元的 cache line 数：

$$
V^{\mathrm{LC}}_{8\mathrm{LUP}}=8\cdot24B=192B=3\ \mathrm{CL}
$$

$$
V^{\neg\mathrm{LC}}_{8\mathrm{LUP}}=8\cdot40B=320B=5\ \mathrm{CL}
$$

Sandy Bridge 上 L1-L2、L2-L3 每传输 1 CL 约 2 cycles；DRAM 传输时间按实测带宽 $b_S=40GB/s$ 与频率 $f=2.7GHz$ 计算：

$$
T_{\mathrm{L3Mem}}=\frac{V\cdot f}{b_S}
$$

所以 3 CL 对应：

$$
T_{\mathrm{L3Mem}}=\frac{192B\cdot2.7GHz}{40GB/s}\approx13\ \mathrm{cy}
$$

5 CL 对应：

$$
T_{\mathrm{L3Mem}}=\frac{320B\cdot2.7GHz}{40GB/s}\approx22\ \mathrm{cy}
$$

LC 满足/违背的后果非常直接：

- LC 在 L1 满足：每一层级都只看到 24B/LUP 的最小流量，2D Jacobi 模型为 $\{6\parallel8\mid6\mid6\mid13\}$，内存预测 $33$ cy，即 $659$ MLUP/s；
- LC 在 L2 满足：L1-L2 仍有 40B/LUP，但 L2 以下降为 24B/LUP，模型为 $\{6\parallel8\mid10\mid6\mid13\}$，内存预测 $37$ cy，即 $587$ MLUP/s；
- LC 在 L3 满足：L1-L2、L2-L3 都按 40B/LUP，DRAM 按 24B/LUP，模型为 $\{6\parallel8\mid10\mid10\mid13\}$，内存预测 $41$ cy，即 $529$ MLUP/s；
- LC 完全不满足：DRAM 也变成 40B/LUP，模型为 $\{6\parallel8\mid10\mid10\mid22\}$，内存预测 $50$ cy，即 $438$ MLUP/s。

这解释了论文 Fig. 3 的核心现象：即使 DRAM code balance 在某些区间相同，性能仍会随 $N_i$ 改变，因为 ECM 还看 L2/L3 上方的数据传输贡献；Roofline 单看 DRAM 带宽无法区分这些层级差异。

### 3. 三个“边角情形” stencil 内核

#### 3.1 2D five-point Jacobi：典型低强度 stencil，但单核并非简单 DRAM-bound

2D Jacobi 的 AVX 工作单元为 8 LUP。论文给出 core 部分：

$$
T_{\mathrm{nOL}}=8\ \mathrm{cy},\qquad T_{\mathrm{OL}}=6\ \mathrm{cy}
$$

瓶颈来自 load pipeline，而不是算术。根据 LC 所在层级，Table III 给出：

$$
\begin{array}{c|c|c|c|c}
\mathrm{LC} & \mathrm{ECM\ model} & T_{\mathrm{ECM}} & P_{\mathrm{mem}} & N_i\ \mathrm{threshold}\\
\hline
L1 & \{6\parallel8\mid6\mid6\mid13\} & \{8\rceil14\rceil20\rceil33\} & 659\ \mathrm{MLUP/s} & N_i<683\\
L2 & \{6\parallel8\mid10\mid6\mid13\} & \{8\rceil18\rceil24\rceil37\} & 587\ \mathrm{MLUP/s} & N_i<5461\\
L3 & \{6\parallel8\mid10\mid10\mid13\} & \{8\rceil18\rceil28\rceil41\} & 529\ \mathrm{MLUP/s} & N_i<436900\\
\mathrm{none} & \{6\parallel8\mid10\mid10\mid22\} & \{8\rceil18\rceil28\rceil50\} & 438\ \mathrm{MLUP/s} & \mathrm{N/A}
\end{array}
$$

实测与预测在三个区间内基本吻合，误差通常在 10% 内；硬件计数得到的实际 DRAM code balance 也在预测值 5% 以内。瓶颈定位是：单核下并不是“DRAM 一条线”解释全部，而是 $T_{\mathrm{nOL}}$ 加上 L1/L2/L3/DRAM 传输共同决定；多核时才逐渐转为 socket DRAM 带宽饱和。

#### 3.2 uxx stencil：看似 divide 昂贵，实则内存路径隐藏了 divide 收益

`uxx` 来自动破裂与地震波传播代码，结构上是 3D stencil，并且 inner loop 中有除法：

```c
d = 0.25*(d1[k][j][i] + d1[k][j-1][i]
        + d1[k-1][j][i] + d1[k-1][j-1][i]);

u1[k][j][i] = u1[k][j][i] + (dth/d) * (...);
```

直觉上会先优化 divide，但 ECM 显示这不是主要收益点。DP 版本中，`vdivpd` throughput 很慢，导致：

$$
T_{\mathrm{OL}}=84\ \mathrm{cy},\qquad T_{\mathrm{nOL}}=38\ \mathrm{cy}
$$

SP 版本编译器用 `vrcpps` 加 Newton-Raphson 和 multiply 近似除法，核心瓶颈下降（overlapping arithmetic 部分约 $T_{\mathrm{OL}}=35$ cy；IACA 报告 frontend bottleneck，整体 core time 取 45 cy，Table IV 使用 $\{45\parallel38\mid20\mid20\mid26\}$）。Table IV 为：

$$
\begin{array}{c|c|c}
\mathrm{version} & \mathrm{ECM\ model} & T_{\mathrm{ECM}}\\
\hline
DP & \{84\parallel38\mid20\mid20\mid26\} & \{84\rceil84\rceil84\rceil104\}
$$

这里 $\{a\rceil b\rceil c\rceil d\}$ 是 ECM 层级预测记号（$\rceil$ 分隔各级预测时间，$\parallel$ 表示可与传输重叠的 core 部分）。\\
SP & \{45\parallel38\mid20\mid20\mid26\} & \{45\rceil58\rceil78\rceil104\}\\
DP\ noDIV & \{41\parallel38\mid20\mid20\mid26\} & \{41\rceil58\rceil78\rceil104\}
\end{array}
$$

关键不等式是：

$$
T_{\mathrm{data}}+T_{\mathrm{nOL}}>T_{\mathrm{OL}}
$$

对 DP：

$$
38+20+20+26=104>84
$$

所以即使去掉 divide，内存层次传输加 load port 的不可重叠时间仍主导内存驻留情形。论文实测确认：DP、SP、DP noDIV 在内存端预测都是 104 cy/工作单元，三者都约在 4 cores 饱和；noDIV 只在未饱和区间有轻微收益，因为它缩短了很长的 critical path，但不是决定 socket 端吞吐的主瓶颈。

#### 3.3 3D long-range stencil：DRAM 流量低了，但 cache 层压力成为主项

长程 stencil 半径为 4，单精度，访问 $V$ 的 $\pm1,\pm2,\pm3,\pm4$ 邻居：

```c
float lap = c0 * V[k][j][i]
          + c1 * (V[k][j][i+1] + V[k][j][i-1])
          + ...
          + c4 * (V[k+4][j][i] + V[k-4][j][i]);

U[k][j][i] = 2.f * V[k][j][i] - U[k][j][i]
           + ROC[k][j][i] * lap;
```

相关 LC 只针对 $V$，因为 $U$ 和 $ROC$ 是线性 streaming。半径 $r=4$，需要 9 个 $k$ 方向 layer 驻留。对 L3 blocking：

$$
9\cdot N\cdot b_j\cdot n\cdot4B < \frac{C_3}{2}
$$

IACA 给出：

$$
T_{\mathrm{OL}}=68\ \mathrm{cy},\qquad T_{\mathrm{nOL}}=64\ \mathrm{cy}
$$

L3 blocking 后，DRAM 只有 4 条 stream：

$$
B_C^{\mathrm{mem}}=16B/\mathrm{LUP}
$$

但 L3 cache 会承受 12 条 stream，因此 cache 层传输很重：

$$
\{68\parallel64\mid24\mid24\mid17\}
$$

$$
T_{\mathrm{ECM}}=\{68\rceil88\rceil112\rceil129\}
$$

其中 DRAM 贡献只占：

$$
\frac{17}{129}\approx13\%
$$

这就是该“边角情形”的意义：即便 DRAM code balance 已经降到 16B/LUP，瓶颈也没有消失，而是转移到 $T_{\mathrm{nOL}}$ 和 L1-L2/L2-L3 传输。论文 Fig. 8 显示，$N=480^3$ 时单线程即使不 blocking 也能满足 LC，所以 blocked/unblocked 单核性能相近；但两核以上共享 L3 压力出现，不 blocking 会破坏多线程 LC，L3 blocking 才能让性能按 ECM 预测接近扩展到全 socket。

### 4. 优化评估逐个推导

#### 4.1 Spatial blocking：最优块大小来自 LC 阈值，而不是经验调参

对 2D Jacobi，blocking 后 LC 变成：

$$
3\cdot b_i\cdot8B < \frac{C_k}{2}
$$

因此可直接解出不同 cache level 的最大 $b_i$：

$$
b_i < \frac{C_k}{48B}
$$

Sandy Bridge cache 为 L1 32KB、L2 256KB、L3 20MB，因此论文 Table III 给出阈值：

$$
b_i^{L1}<683
$$

$$
b_i^{L2}<5461
$$

$$
b_i^{L3}<436900
$$

文中实验使用的代表性 block size 是：

$$
b_i=2.3\times10^5\quad(\mathrm{L3\ blocking})
$$

$$
b_i=4.3\times10^3\quad(\mathrm{L2\ blocking})
$$

$$
b_i=800,\quad b_j=300\quad(\mathrm{L1\ blocking})
$$

单纯看 LC，L1 blocking 似乎只需要限制 $b_i$。但实测发现 pure inner blocking 的内存 code balance 高于 24B/LUP，原因是硬件 prefetcher 不知道短 inner block 何时结束，会把 block 末端之外的 cache line 预取进来；这些数据在下一个 inner block 使用前已被逐出，形成额外流量。论文通过 outer blocking 修正：

```c
for (js=1; js<Nj-1; js+=bj)
  for (is=1; is<Ni-1; is+=bi)
    for (j=js; j<min(Nj-1,js+bj-1); ++j)
      for (i=is; i<min(Ni-1,is+bi-1); ++i)
        b[j][i] = (...);
```

在 $b_i=800$、$N_i=3.5\times10^4$、$N_j=1.2\times10^4$ 下，论文 Fig. 5 显示：

$$
b_j\approx300
$$

能把 prefetcher 造成的额外流量压回接近最低的 24B/LUP。由测得额外流量还可反推该机器上的 prefetch distance 约为 33 CL。

空间分块的收益上限也很清楚：一旦所有层级都达到最低 code balance：

$$
B_C=24B/\mathrm{LUP}
$$

继续 spatial blocking 已经不能再减少流量。此时若想提升单核性能，只能减少 core 项。论文举例：若通过 register blocking 等方法把 $T_{\mathrm{nOL}}$ 从 8 cy 降到 4 cy，则 L1 blocking 的内存预测从

$$
T_{\mathrm{old}}=33
$$

变为近似：

$$
T_{\mathrm{new}}=33-4=29
$$

单核加速仅为：

$$
\frac{33}{29}\approx1.14
$$

也就是说，在这个 Jacobi 内核上，空间分块主要价值是把 DRAM 流量降到 24B/LUP，并使多核饱和点提前；它不是无限提升单核性能的手段。

#### 4.2 Strength reduction：去掉 divide 不一定有收益

`uxx` 的 DP divide 很慢，直觉优化是 strength reduction：把 inner loop 中的除法替换为乘法。论文专门构造 `DP noDIV` 版本，模型为：

$$
\mathrm{DP}:\{84\parallel38\mid20\mid20\mid26\}
$$

$$
\mathrm{DP\ noDIV}:\{41\parallel38\mid20\mid20\mid26\}
$$

对 L1/L2/L3 驻留数据，noDIV 确实能改善：

$$
\{84\rceil84\rceil84\rceil104\}
$$

这里 $\{a\rceil b\rceil c\rceil d\}$ 是 ECM 层级预测记号（$\rceil$ 分隔各级预测时间，$\parallel$ 表示可与传输重叠的 core 部分）。
\rightarrow
\{41\rceil58\rceil78\rceil104\}
$$

但对大问题内存驻留：

$$
T_{\mathrm{mem}}=104\ \mathrm{cy}
$$

完全不变。原因是去掉 divide 只降低 $T_{\mathrm{OL}}$，而实际内存情形受下面这项限制：

$$
T_{\mathrm{nOL}}+T_{\mathrm{L1L2}}+T_{\mathrm{L2L3}}+T_{\mathrm{L3Mem}}
=
38+20+20+26=104
$$

只要：

$$
T_{\mathrm{nOL}}+T_{\mathrm{data}}>T_{\mathrm{OL}}
$$

就算 $T_{\mathrm{OL}}$ 中的 divide 很慢，也能被数据路径“盖住”。这给 stencil 优化一个重要判断准则：昂贵指令是否值得消除，不能看指令 latency/throughput 的绝对值，要看它是否落在 ECM 的最终 max 项里。

#### 4.3 Temporal blocking：收益条件是消除 DRAM 项后是否暴露新瓶颈

Temporal blocking 的思想是在数据离开 cache 前完成多个时间步，从而减少 DRAM 流量。ECM 可用来给它的收益上界：理想 L3 temporal blocking 等价于削掉 $T_{\mathrm{L3Mem}}$。

对 `uxx`：

$$
T_{\mathrm{old}}=104\ \mathrm{cy}
$$

理想 temporal blocking 去掉：

$$
T_{\mathrm{L3Mem}}=26\ \mathrm{cy}
$$

DP 的下一瓶颈是 divide：

$$
T_{\mathrm{new,DP}}=\max(84,38+20+20)=84
$$

所以单核加速为：

$$
S_{\mathrm{DP}}=\frac{104}{84}\approx1.24
$$

论文写作 24% speedup。SP 的下一瓶颈是 L3 传输路径：

$$
T_{\mathrm{new,SP}}=\max(45,38+20+20)=78
$$

$$
S_{\mathrm{SP}}=\frac{104}{78}\approx1.33
$$

论文写作 33% speedup。真正收益不只在单核，而是移除 DRAM bandwidth bottleneck 后，多核扩展上限可超过 2000 MLUP/s，即使 DP 仍保留 divide。

对 3D long-range stencil，blocked 后模型为：

$$
\{68\parallel64\mid24\mid24\mid17\}
$$

$$
T_{\mathrm{old}}=129
$$

理想 temporal blocking 去掉 DRAM 项后：

$$
T_{\mathrm{new}}=\max(68,64+24+24)=112
$$

加速只有：

$$
\frac{129}{112}\approx1.15
$$

由于 DRAM 只占约 13%，temporal blocking 对当前版本收益有限。论文指出真正应优化的是主项 $T_{\mathrm{nOL}}$ 和 core/load 压力。若能把所有 core contribution 包括 $T_{\mathrm{nOL}}$ 降低 50%，模型变为：

$$
\{34\parallel32\mid24\mid24\mid17\}
$$

$$
T_{\mathrm{ECM}}=\{34\rceil56\rceil80\rceil97\}
$$

单核加速为：

$$
\frac{129}{97}\approx1.33
$$

并且饱和点会降到 6 cores，此时 temporal blocking 才重新变成值得考虑的优化。

### 5. 可扩展性预测公式

ECM 的多核外推采用一个简单但有解释力的假设：单核性能线性扩展，直到共享瓶颈出现。对现代 Intel Sandy Bridge（本文的 SNB，L3 可扩展架构），主要共享瓶颈是 socket DRAM 带宽。若单核内存驻留 ECM 性能为 $P_{\mathrm{ECM}}^{\mathrm{mem}}$，STREAM/update 类基准得到 socket 带宽 $b_S$，内存 code balance 为 $B_C$，则：

$$
P(n)=\min\left(nP_{\mathrm{ECM}}^{\mathrm{mem}},\frac{b_S}{B_C}\right)
$$

饱和核数为：

$$
n_S=
\left\lceil
\frac{b_S/B_C}{P_{\mathrm{ECM}}^{\mathrm{mem}}}
\right\rceil
$$

由于：

$$
P_{\mathrm{ECM}}^{\mathrm{mem}}=\frac{W f}{T_{\mathrm{ECM}}^{\mathrm{mem}}}
$$

且：

$$
\frac{b_S}{B_C}=\frac{W f}{T_{\mathrm{L3Mem}}}
$$

（两式均以周期计，频率因子 $f$ 在相除时抵消，故 $n_S$ 表达式不变。）

所以可写成论文中的等价形式：

$$
n_S=
\left\lceil
\frac{T_{\mathrm{ECM}}^{\mathrm{mem}}}{T_{\mathrm{L3Mem}}}
\right\rceil
$$

这条公式很重要：慢代码需要更多核才能填满内存带宽，快代码反而更早饱和。2D Jacobi 的 Table III 给出饱和点：

$$
n_S=3\quad(\mathrm{L1\ LC})
$$

$$
n_S=3\quad(\mathrm{L2\ LC})
$$

$$
n_S=4\quad(\mathrm{L3\ LC})
$$

$$
n_S=3\quad(\mathrm{no\ LC})
$$

多线程下还要修正共享 L3 的 LC。对 2D Jacobi：

$$
3\cdot b_i\cdot n\cdot8B < \frac{C_3}{2}
$$

因此 L3 blocking 的 $b_i$ 不能只按单线程选。论文 Fig. 6b 展示：$b_i=2.3\times10^5$ 单核有效，但多核饱和后表现像 40B/LUP；$b_i=1.1\times10^5$ 可改善到 4 cores；真正稳定的做法是：

$$
b_i=\frac{2.3\times10^5}{n_{\mathrm{threads}}}
$$

这保证每个线程的三层数据都能留在共享 L3 中，使多核性能达到 24B/LUP 对应的饱和水平。

### 6. 与库内论文关联

#### 6.1 与 Roofline：互补而非替代

同批入库的 Roofline 是“洞见型上界图”，适合快速回答：

$$
P\le \min(P_{\max},B_{\mathrm{mem}}\cdot I)
$$

也就是程序大体受计算峰值还是 DRAM 带宽限制。它的优势是简单、可视、跨架构沟通成本低。

ECM 则是“分层可加预测模型”。它把 Roofline 中被压缩成一个 $B_{\mathrm{mem}}$ 的内存系统展开为：

$$
T_{\mathrm{L1L2}}+T_{\mathrm{L2L3}}+T_{\mathrm{L3Mem}}
$$

并把计算峰值展开成：

$$
T_{\mathrm{OL}},\quad T_{\mathrm{nOL}}
$$

因此它能解释 Roofline 容易误判的 stencil 情形：相同 DRAM code balance 下，性能仍可能因为 LC 在 L2/L3 的满足情况不同而变化；去掉昂贵 divide 也不一定提升内存端性能；DRAM 流量已经很低时，cache 层传输和 load port 可能成为主瓶颈。

可以把二者作为两级工具：

$$
\mathrm{Roofline}:\ \text{先判断宏观上界与优化方向}
$$

$$
\mathrm{ECM}:\ \text{再拆解单核路径、LC、饱和点与优化收益}
$$

#### 6.2 对 Doctor 高性能框架/stencil/AMR 研究的迁移

AMReX 这类 block-structured AMR 框架中，大量核心 kernel 本质上是 stencil、flux、restriction/prolongation、ghost fill 后的局部规则网格更新。ECM 的可迁移价值在于：它给每个 AMR box 内核提供了一个可落地的性能诊断流程。

对一个 AMR stencil kernel，可按以下顺序建模：

$$
\text{确定工作单元}
\rightarrow
\text{数 load/store/算术指令}
\rightarrow
(T_{\mathrm{OL}},T_{\mathrm{nOL}})
\rightarrow
\text{分析 layer condition}
\rightarrow
(T_{\mathrm{L1L2}},T_{\mathrm{L2L3}},T_{\mathrm{L3Mem}})
\rightarrow
P(n),n_S
$$

AMR 框架里 box size、tile size、ghost width、stencil radius 直接进入 LC：

$$
(2r+1)\cdot b_{\mathrm{fast}}\cdot s < \frac{C_k}{2}
$$

三维 tile 则类似：

$$
N_{\mathrm{layers}}\cdot b_i\cdot b_j\cdot s\cdot n_{\mathrm{shared}} < \frac{C_k}{2}
$$

其中 $n_{\mathrm{shared}}$ 为共享该 cache 的线程数（私有 L1/L2 取 1，共享 L3 才乘线程数）。
$$

这能把“tile 多大合适”从经验参数变成可解释约束。对 AMReX 的 `MFIter` tiling、GPU/CPU 后端分块、AMR level 上不同 patch shape 的性能差异，ECM 的 layer condition 思路都可以迁移：不是只看总网格规模，而是看一个线程/一个 tile 在 cache 中需要同时保留多少层。

对 Doctor 的高性能 PDE/AMR 框架方向，本文最值得保留的方法论是：优化前先问瓶颈项是否在最终 max 里。若优化减少的是 $T_{\mathrm{OL}}$，但最终由 $T_{\mathrm{nOL}}+T_{\mathrm{data}}$ 主导，收益会很小；若优化减少的是 DRAM code balance，但 $T_{\mathrm{L3Mem}}$ 只占 13%，收益也有限。真正可迁移的不是 Sandy Bridge 的具体数字，而是这种“从 layer condition 到分层流量，再到多核饱和”的分析路径。


## Review Questions

1. 如何把 ECM 的 layer condition 从单一规则 stencil 推广到 AMReX block-structured AMR 中不规则的 box size、ghost width、EB/cut-cell，以及 MFIter tiling 的自动 tile-size 选择？
2. 对流体/PDE 求解器，哪些 kernel（flux reconstruction、Riemann solver、restriction/prolongation、ghost fill、matrix-free operator）应先用 Roofline 粗筛，哪些需要 ECM 细拆到 L1/L2/L3，并如何建立统一的 profiling 协议？
3. 在 GPU/HBM、多级 cache、SIMT execution 下，ECM 的 $T_{\mathrm{nOL}}/T_{\mathrm{OL}}$ 与串行 cache transfer 假设哪些仍成立，哪些应改写为 occupancy、warp scheduling、shared memory/register pressure 模型，才能服务 AMReX/WarpX 类性能可移植框架？

## Kimi Code Review 结论（2026-08-04）

- 核心公式/数值总体可靠：DAXPY、2D Jacobi Table III、uxx Table IV、3D long-range stencil、spatial blocking、strength reduction、temporal blocking 与多核饱和点的数值均与论文一致，未发现实质性表格数值错误。
- 已修正 13 处：
  1. ECM 合并规则表述：改为"按非重叠规则累加传输贡献，并与可重叠 core 时间取 max"（非简单取瓶颈层）；
  2. 多核外推收窄为"socket 带宽上限 + 共享 L3 的 LC 修正"，去掉 NUMA/同步的过度泛化；
  3. strength reduction 案例限定为"除法替换为乘法"；
  4. temporal blocking 收益表述改为"单核与全 socket 场景"；
  5. $T_{\mathrm{data}}$ 补充：内存驻留三项全加、L2/L3 驻留只加到相应层；
  6. $P_{\mathrm{ECM}}$ 补频率因子（$W f/T_{\mathrm{ECM}}$，周期计）并注明秒制形式；
  7. $C_k$ 表述严谨化（容量 $C_k$，经验约一半可用于 layer 存储）；
  8. blocking LC 限定为"2D Jacobi inner blocking 情形"；
  9. uxx SP 补注：$T_{\mathrm{OL}}=35$ cy、IACA frontend bottleneck、core time 45 cy、Table IV 用 $\{45\parallel38\mid20\mid20\mid26\}$；
  10. 多核公式 $P_{\mathrm{ECM}}^{\mathrm{mem}}$ 与 $b_S/B_C$ 补频率因子并说明 $n_S$ 中抵消；
  11. "socket DRAM 带宽瓶颈"限定为 SNB 这类 L3 可扩展架构；
  12. 三维 tile 公式 $n\to n_{\mathrm{shared}}$（私有 L1/L2 取 1，共享 L3 乘线程数）；
  13. ECM 层级预测记号 $\{a\rceil b\rceil c\rceil d\}$ 加说明（$\rceil$ 分隔各级，$\parallel$ 表示可重叠 core 部分）。
- Markdown 结构整体连贯，显示数学定界符未发现破损；C 代码块中 blocking 边界已是补全形式 $\min(N_i-1, i_s+b_i-1)$。
