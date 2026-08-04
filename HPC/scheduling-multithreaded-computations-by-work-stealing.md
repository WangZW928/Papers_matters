# 用工作窃取调度多线程计算 / Scheduling Multithreaded Computations by Work Stealing

**作者：** Robert D. Blumofe（UT Austin）, Charles E. Leiserson（MIT CSAIL）
**期刊：** Journal of the ACM, Vol. 46, No. 5, pp. 720-748, September 1999
**DOI：** [https://doi.org/10.1145/324133.324234](https://doi.org/10.1145/324133.324234)
**arXiv：** 无（早期版本：FOCS '94, pp. 356-368）
**阅读状态：** 🔬 精读（Doctor 指定）
**流程状态：** ①元数据 ✓ | ②初稿 ✓ | ③评估 ✓(精读) | ④补充 ✓ | ⑤索引 ✓ | ⑥review ✓ | ⑦提交 ✓

---

## 摘要

### 中文翻译
本文研究在并行计算机上高效调度 fully strict（即结构良好）多线程计算的问题。一种流行且实用的调度方法是"工作窃取"（work stealing）：需要工作的处理器从其他处理器窃取计算线程。本文给出第一个**可证明优**的、面向带依赖多线程计算的工作窃取调度器。具体地，我们的分析表明：用我们的工作窃取调度器在 $P$ 个处理器上执行一个 fully strict 计算的期望时间为 $T_1/P + O(T_\infty)$，其中 $T_1$ 是该多线程计算的最小串行执行时间，$T_\infty$ 是在无穷多处理器下的最小执行时间。此外，执行所需空间至多为 $S_1 P$，其中 $S_1$ 是最小串行空间需求。我们还证明算法的期望总通信量至多为 $O(P T_\infty (1+n_d) S_{\max})$，其中 $S_{\max}$ 是任意线程最大激活记录的大小，$n_d$ 是任意线程与其父线程同步次数的最大值。这一通信界证明了"工作窃取调度器比工作共享调度器通信效率更高"的经验之谈。这三个界在常数因子内都是存在性最优的（existentially optimal）。

### 原文
> This paper studies the problem of efficiently scheduling fully strict (i.e., well-structured) multithreaded computations on parallel computers. A popular and practical method of scheduling this kind of dynamic MIMD-style computation is "work stealing," in which processors needing work steal computational threads from other processors. In this paper, we give the first provably good work-stealing scheduler for multithreaded computations with dependencies. Specifically, our analysis shows that the expected time to execute a fully strict computation on P processors using our work-stealing scheduler is T1/P + O(T∞), where T1 is the minimum serial execution time of the multithreaded computation and T∞ is the minimum execution time with an infinite number of processors. Moreover, the space required by the execution is at most S1P, where S1 is the minimum serial space requirement. We also show that the expected total communication of the algorithm is at most O(PT∞(1+nd)Smax), where Smax is the size of the largest activation record of any thread and nd is the maximum number of times that any thread synchronizes with its parent. This communication bound justifies the folk wisdom that work-stealing schedulers are more communication efficient than their work-sharing counterparts. All three of these bounds are existentially optimal to within a constant factor.

---

## 文章总结

### 1. 解决什么问题？
动态 MIMD 多线程计算（如 Cilk 风格的分治/递归程序）在 $P$ 处理器上的调度：如何保证接近线性加速（$T_1/P$）同时不丢失关键路径（$T_\infty$）？工作窃取在实践中流行（如 Cilk、后来的 TBB/OpenMP 任务并行），但此前缺乏严格的性能保证——尤其是与工作共享（work sharing，集中式任务队列）相比的通信效率论证。

### 2. 用了什么方法论？
- **计算模型**：fully strict 多线程计算 = 带依赖的 DAG（threads + spawn/sync 边），$T_1$（work）、$T_\infty$（关键路径/critical path）；
- **算法**：每处理器维护双端队列（deque）；本地线程 LIFO 栈式执行（利于缓存）；空闲处理器随机选一个受害者（victim），从其 deque 顶部（FIFO 端）窃取最老的 ready thread——保证被窃取线程通常是"最有可能产生大量新工作"的；
- **分析工具**：busy-leaves property（叶子忙性质：任意时刻每个活跃 spawn subtree 的叶线程都有某个处理器正在执行它——活跃叶数至多 $P$，直接支撑空间界 $S_1P$）、recycling game（把"原子访问共享 deque"的竞争建模为博弈，用于导出通信界）；
- **复杂度证明**：期望时间、空间（$S_1P$）、通信（$O(PT_\infty(1+n_d)S_{\max})$）三界；并证明存在性最优。

### 3. 主要结论是什么？
- **时间界** $\mathbb{E}[T_P] = O(T_1/P + T_\infty)$：实现线性加速（work 项）+ 关键路径项，随机 work stealing 在期望意义上达到与最优下界 $\max(T_1/P,\ T_\infty)$ 同阶的时间界；
- **空间界** $\le S_1 P$：本地 LIFO 执行保持"深度优先"空间轮廓，论文称该界优于此前 work-sharing scheduler 的相关结果；
- **通信界** $O(P T_\infty (1+n_d) S_{\max})$：窃取次数受关键路径与同步次数控制，因此工作窃取在通信上优于集中式工作共享——"每个窃取都是一次通信，但窃取总数被 $T_\infty$ 约束"；
- 三界均存在性最优（existentially optimal）：对任意计算都存在常数因子内不可改进的实例；
- 工程影响：为 Cilk 运行时（及后来的 TBB、OpenMP tasking、Java ForkJoin）提供了理论基础，成为任务并行调度的事实标准。

---

## 价值评估
Doctor 指定精读

## 公式与代码梳理

### 1. 计算模型形式化

论文把一次多线程程序在给定输入上的实际执行展开成一个指令级 DAG：

$$
G=(V,E)
$$

其中每个顶点 $v\in V$ 是一个单位时间指令。线程不是操作系统线程，而是一段顺序指令链：

$$
\Gamma=(v_1,v_2,\ldots,v_k)
$$

同一线程内相邻指令之间有 continue edge：

$$
(v_i,v_{i+1})\in E
$$

当父线程 $\Gamma_a$ 的某条指令 $u$ 创建子线程 $\Gamma_b$ 时，加入 spawn edge：

$$
(u,\operatorname{first}(\Gamma_b))\in E
$$

所有线程按 spawn 关系形成 spawn tree。若子线程产生的结果被父线程或祖先线程消费，则通过 join edge 表示数据/同步依赖：

$$
(v_{\mathrm{producer}},v_{\mathrm{consumer}})\in E
$$

一个指令 ready 当且仅当它在 DAG 中的所有前驱都已执行。线程可能处于 ready，也可能因为 join 依赖未满足而 stalled。

fully strict 的限制是：任何 join edge 都只能从某个线程指向它的父线程，而 strict 只要求 join edge 指向祖先线程。形式上，若线程 $\Gamma$ 的某条指令通过 join edge 指向 $\Gamma'$，则 fully strict 要求：

$$
\Gamma'=\operatorname{parent}(\Gamma)
$$

这正是 Cilk 风格 fork-join 分治程序的结构：子任务只把结果返回给直接调用者，不任意唤醒旁支或远祖先。该限制让调度器可以用局部 deque 维护出接近深度优先的空间结构。

计算量 work 定义为 DAG 顶点数：

$$
T_1=|V|
$$

关键路径 critical-path length 定义为 DAG 中最长有向路径长度：

$$
T_\infty=\max_{\pi\subseteq G}|\pi|
$$

任意 $P$ 处理器调度时间 $T_P$ 至少满足两个下界：

$$
T_P\ge \frac{T_1}{P}
$$

$$
T_P\ge T_\infty
$$

前者来自总工作量，后者来自依赖链不可并行。并行度定义为：

$$
\frac{T_1}{T_\infty}
$$

当 $T_1/T_\infty=\Omega(P)$ 时，理论上存在接近线性加速空间。

空间测度不是全局堆，而是 activation frame。线程被 spawn 时分配 frame，线程死亡并且其子线程都已死亡后释放。一个线程的 stack depth 是从根到该线程路径上所有 frame 大小之和：

$$
\operatorname{depth}(\Gamma)=\sum_{\Gamma'\in \operatorname{ancestors}(\Gamma)\cup\{\Gamma\}} S(\Gamma')
$$

串行最小空间 $S_1$ 等于整个计算的最大 stack depth：

$$
S_1=\max_\Gamma \operatorname{depth}(\Gamma)
$$

### 2. 工作窃取算法精确描述

每个处理器 $p$ 维护一个 ready deque。deque 有 bottom 和 top 两端：

- 本地处理器只从 bottom push/pop，表现为 LIFO 栈。
- 窃取者只从 victim 的 top 取线程，表现为 FIFO 取最老 ready 线程。
- 初始时 root thread 放入某个处理器的 deque，其余处理器开始窃取。

处理器执行当前线程 $\Gamma_a$，直到出现四类事件：

1. **spawn**：$\Gamma_a$ spawn 子线程 $\Gamma_b$。处理器把 $\Gamma_a$ push 到本地 deque bottom，然后立即执行 $\Gamma_b$。这相当于串行深度优先调用：先进入子任务，把 continuation 留在本地 deque bottom（行为上近似串行深度优先执行轮廓）。

2. **stall**：$\Gamma_a$ 因 join 依赖阻塞。处理器尝试从本地 bottom pop 一个 ready 线程；若本地 deque 为空，则成为 thief，随机选择 victim。

3. **die**：$\Gamma_a$ 完成。处理逻辑同 stall：先本地 pop，空则 steal。

4. **enable**：$\Gamma_a$ 满足某个 stalled 线程 $\Gamma_b$ 的 join 依赖。fully strict 下，$\Gamma_b$ 必为 $\Gamma_a$ 的父线程。调度器把 $\Gamma_b$ push 到当前处理器的 bottom。

窃取协议为：

$$
\operatorname{victim}\sim \operatorname{Uniform}\{1,\ldots,P\}
$$

若 victim deque 非空，偷取 topmost thread；否则重新随机选择 victim。终止条件为所有线程已死亡且无未满足依赖；论文核心分析不依赖具体终止检测机制，实践实现可用 root continuation、join counter 或全局计数完成检测。

“窃取最老线程”的直觉很重要。bottom 端的新线程靠近当前递归深处，通常粒度小、局部性强、还适合由本地处理器继续深度优先执行；top 端的老线程更靠近 spawn tree 根部，代表更大的尚未展开子树。偷 top 等价于把一个大子问题迁移出去，既减少偷窃频率，也保留本地 cache locality。

### 3. busy-leaves property 与时间界直觉

busy-leaves property：在任意时刻，当前 alive spawn subtree 的每个叶线程都有某个处理器正在执行它。

严格计算中，一个叶线程不会因为等待后代而 stall，因为它没有 alive 后代。若某线程 spawn 子线程，子线程成为新叶且由当前处理器继续执行；若线程死亡，它的父线程可能变成叶，调度器会继续处理父线程或使其 ready；若线程 stall，则 fully strict/strict 结构意味着它等待的是后代结果，因此它不是叶。于是可以归纳证明每个叶保持 busy。

该性质直接给空间界。任意时刻 spawn subtree 的叶子数不超过忙处理器数，因此不超过 $P$。每个叶到根路径的 frame 总和最多 $S_1$，所以总活跃空间满足：

$$
S_P\le P S_1
$$

时间方面，先看理想 greedy scheduler：若 ready 指令数至少 $P$，就执行 $P$ 条；若少于 $P$，就执行全部 ready 指令。Brent/Graham 定理给出：

$$
T_P\le \frac{T_1}{P}+T_\infty
$$

工作窃取不是显式 greedy，因为空闲处理器可能偷失败，也可能在同一 victim 上竞争。论文的核心是证明随机窃取导致的额外失败/等待次数只和 $P T_\infty$ 同阶，而不会和 $T_1$ 同阶。

### 4. recycling game：原子访问竞争模型

论文采用很保守的 atomic-access model：多个 thief 同时访问同一个 victim deque 时，只有一个请求被服务，其余请求被 adversary 排队；adversary 甚至可以选择服务顺序，但只要队列非空，每步必须服务一个。

为分析这种竞争，作者构造 $(P,M)$-recycling game：

- $P$ 个球对应 $P$ 个处理器的 outstanding steal request。
- $P$ 个箱子对应 $P$ 个 deque。
- 球在 reservoir 中表示处理器当前没有未完成请求。
- adversary 每步可选择若干 reservoir 中的球，把它们独立均匀随机投入 $P$ 个箱子。
- 每个非空箱子每步移出一个球回 reservoir。
- 总投球次数为 $M$，总 delay 为所有球在箱中等待的累计时间。

结论是：即使 adversary 选择最坏投球时刻和服务顺序，总等待延迟的期望仍至多线性于请求数：

$$
\mathbb{E}[D]\le M
$$

高概率地：

$$
D=O\left(M+P\log P+P\log\frac{1}{\epsilon}\right)
$$

这说明 atomic contention 不会把随机窃取的开销放大到不可控；排队等待可以摊还到 steal attempt 数量上。

### 5. 三个核心界的证明要点

#### 5.1 期望时间界

论文把每个时间步的每个处理器收一枚“dollar”，分到三个桶：

- WORK：执行真实指令。
- STEAL：发起一次 steal attempt。
- WAIT：等待已排队的 steal request 被服务。

真实工作恰好为：

$$
\#\mathrm{WORK}=T_1
$$

难点是界定 steal attempt。作者引入 augmented DAG $G'$：对每个 spawn 指令 $u$，若 $u$ spawn 子线程首指令 $v$，而父线程中 $u$ 的后继为 $w$，则添加 deque edge：

$$
(w,v)\in E(G')
$$

这些边不参与真实执行，只用于分析 deque 中线程的相对“年龄”。由于每条 spawn 最多引入一条 deque edge，且原 DAG 关键路径为 $T_\infty$，有：

$$
T_\infty(G')\le 2T_\infty
$$

定义 critical instruction：在 $G'$ 中所有前驱都已执行的未执行指令。若 steal attempt 很多，就能构造一条 delay sequence，使某条 $G'$ 路径上的 critical instructions 长时间保持 critical。另一方面，ready deque 结构引理说明：任意 critical instruction 所在线程在某个 deque 中时，其上方最多只有一个线程。于是若若干 steal attempt 随机命中该处理器，critical instruction 很快会被偷走或被本地执行。

把 steal attempt 按 round 分组，每轮约 $3P$ 到 $4P$ 次偷窃。对任意给定的 round 集合（$r\ge 2$，delay-sequence 分析中），一个 critical instruction 连续跨过 $r$ 轮仍未执行的概率指数下降，论文给出形如：

$$
\Pr[\text{某指令跨 }r\text{ 轮保持 critical}]\le e^{-2r+3}
$$

对所有可能 delay sequence 做 union bound，得到期望 steal attempt 数：

$$
\mathbb{E}[\#\mathrm{STEAL}]=O(P T_\infty)
$$

再由 recycling game：

$$
\mathbb{E}[\#\mathrm{WAIT}]\le \mathbb{E}[\#\mathrm{STEAL}]
$$

所以总期望时间为：

$$
\mathbb{E}[T_P]
=
\frac{\mathbb{E}[\#\mathrm{WORK}+\#\mathrm{STEAL}+\#\mathrm{WAIT}]}{P}
=
\frac{T_1}{P}+O(T_\infty)
$$

高概率版本为：

$$
T_P
=
\frac{T_1}{P}
+
O\left(T_\infty+\log P+\log\frac{1}{\epsilon}\right)
$$

“随机窃取不劣于贪心”的精髓是：贪心调度的空闲时间由关键路径控制；随机工作窃取虽然会出现失败偷窃，但一个 critical thread 总在某个 deque 顶部附近，随机命中它所在处理器的概率为 $1/P$，每 $O(P)$ 次偷窃就有常数概率推进关键路径。因此额外开销仍是 $O(P T_\infty)$，除以 $P$ 后成为 $O(T_\infty)$。

#### 5.2 空间界

空间界依赖本地 LIFO 与 fully strict 结构，而不是概率。

ready deque 结构引理说：若处理器正在执行 $\Gamma_0$，其 deque 从 bottom 到 top 为：

$$
\Gamma_1,\Gamma_2,\ldots,\Gamma_k
$$

则：

$$
\Gamma_i=\operatorname{parent}(\Gamma_{i-1}),\qquad i=1,\ldots,k
$$

并且除 topmost 线程外，deque 中线程自从 spawn 子线程后没有再被执行。这说明每个处理器的本地状态近似一条串行调用栈：正在向 spawn tree 深处走，continuation 留在 bottom/top 链上。

因此 work stealing 维持 busy-leaves property，任意时刻 alive spawn subtree 的叶子数至多 $P$。总空间由每个叶到根路径覆盖：

$$
S_P\le \sum_{\ell\in \operatorname{leaves}} S_1\le P S_1
$$

这个界的意义是：并行执行只把串行深度优先栈复制到最多 $P$ 条活跃路径上，没有把整个宽度优先前沿全部物化。

#### 5.3 通信界

设：

- $S_{\max}$：任意 activation frame 的最大字节数。
- $n_d$：任意线程到其父线程的 join edge 最大数量。

每次成功偷取线程，最坏需要迁移其 activation frame：

$$
O(S_{\max})
$$

若某个父线程被偷走，子线程通过 join edge 向父线程返回结果会产生远程通信。这里应区分两类成本：join edge resolution 本身每条至多常数字节（每线程与父线程最多同步 $n_d$ 次，故每次偷窃相关的 join 通信为 $O(n_d)$ 字节）；按 $S_{\max}$ 计的是被偷线程 activation frame 的迁移，以及 child enable 被偷走的 parent 时可能移动的 parent frame 成本。故每次偷窃的通信量为：

$$
O(n_d)+O(S_{\max})
$$

结合偷窃次数：

$$
\mathbb{E}[\#\mathrm{steals}]=O(P T_\infty)
$$

得到总通信：

$$
\mathbb{E}[C]
=
O\left(P T_\infty (1+n_d)S_{\max}\right)
$$

高概率形式为：

$$
C
=
O\left(P\left(T_\infty+\log\frac{1}{\epsilon}\right)(1+n_d)S_{\max}\right)
$$

当 $n_d=O(1)$ 且 $P=O(T_1/T_\infty)$ 时：

$$
C=O(T_1 S_{\max})
$$

若 $P\ll T_1/T_\infty$，则：

$$
P T_\infty S_{\max}\ll T_1 S_{\max}
$$

也就是说通信显著少于“每个任务/每段工作都可能被分发一次”的 work sharing 风格上界。

### 6. 与 work sharing 的对比

work sharing 是生产者主动把新产生的线程分发给其他处理器。它的问题是：迁移发生在“产生工作”时，而不是“确实缺工作”时。若所有处理器本来都有活干，work sharing 仍可能迁移新线程，导致不必要的 frame 移动、队列操作和远程同步。

work stealing 反过来：只有空闲处理器主动找工作。因此迁移次数被 steal attempt/critical path 分析约束，而不是被 spawn 总数直接约束。定量差别可以理解为：

$$
\text{work sharing 通信} \approx \Theta(T_1 S_{\max}) \quad \text{或接近每份工作一次迁移}
$$

而 work stealing 为：

$$
\text{work stealing 通信}
=
O(P T_\infty(1+n_d)S_{\max})
$$

当程序并行度高，即 $T_1/T_\infty\gg P$ 时，二者差距很大。work sharing 还容易破坏深度优先空间轮廓：过早暴露大量 sibling/subtree，使同时 alive 的 frontier 扩大；work stealing 的本地 LIFO 则让每个处理器沿一条深路径推进，只有老的、大的 continuation 被偷走。

### 7. existentially optimal 的含义

existentially optimal 不是说算法对每个具体 DAG 都达到该 DAG 的绝对最优常数，而是说这些渐近界在常数因子内无法被普遍改进：存在某些 fully strict 计算实例，使任何想达到线性加速的调度都必须付出同阶时间、空间或通信成本。

时间方面，任意调度都绕不过：

$$
\Omega\left(\frac{T_1}{P}+T_\infty\right)
$$

空间方面，某些计算确实需要 $P$ 条并行活跃调用链，因此：

$$
\Omega(S_1P)
$$

通信方面，Wu-Kung 对 divide-and-conquer 的下界适用于 fully strict 的特例（此时 $n_d=1$），说明达到线性加速时存在实例需要：

$$
\Omega(P T_\infty S_{\max})
$$

即 $n_d=1$ 时 $\Omega(P T_\infty(1+n_d)S_{\max})$ 等价于 $\Omega(P T_\infty S_{\max})$，与 Theorem 14 的一般式一致。

因此论文的三个主界分别匹配对应下界到常数因子。

### 8. 工程影响与 Doctor 框架启发

Cilk 的运行时设计基本就是这篇论文的工程化：spawn 时继续执行 child，把 continuation 压入本地 deque；worker 空闲时随机偷别人的 top continuation。后来的 Intel TBB、OpenMP tasking、Java ForkJoinPool 都继承了相同核心范式：本地 LIFO 保局部性，远端 FIFO 偷粗粒度老任务，随机或近似随机 victim 选择降低中心瓶颈。

对 Doctor 高性能框架，最可迁移的不是“照搬 Cilk 线程模型”，而是三条原则：

1. **动态任务并行用 work stealing，静态网格分发用 SFC/knapsack。**  
   AMReX 的 SFC/knapsack 适合已知 box 权重的 AMR level 分配：

   $$
   \sum_{i\in \mathcal{P}_p} w_i \approx \frac{1}{P}\sum_i w_i
   $$

   它是 timestep 或 regrid 阶段的静态/半静态负载均衡。work stealing 更适合运行时不确定的递归任务、adaptive search、局部时间步、多物理耦合中耗时突变的 task graph。

2. **任务队列应避免中心化。**  
   单全局队列容易成为 atomic/MPI contention 热点；每 worker 一个 deque 可以把常见路径变成本地 push/pop，只有空闲时才跨 worker 通信。

3. **偷“大而老”的任务，保“小而新”的局部性。**  
   对 PDE/AMR 框架可解释为：本地继续处理刚生成、cache/数据驻留更热的 tile/subtask；跨线程或跨 rank 迁移时优先迁移更粗粒度、更靠近任务树上层的 continuation。这样通信次数由“缺活次数”而不是“任务生成次数”控制。

在 AMReX/WarpX 语境里，SFC+knapsack 解决的是 box 到 rank/GPU 的初始平衡；work stealing 可以作为 rank 内 CPU task、GPU kernel batching、异步边界填充、粒子局部重排、AMR 层间细粒度任务的补充机制。尤其当单个 box 内部任务耗时不均、粒子数剧烈波动或物理模块分支复杂时，静态权重 $w_i$ 会滞后，work stealing 的动态性可以补上尾部负载不均。

但迁移到 GPU/AMR 框架时要保留论文的边界条件：任务粒度不能太细，否则 steal overhead 与 kernel launch overhead 会吃掉收益；任务依赖最好接近 fully strict，否则 $S_1P$ 与通信界不再自动成立；跨 MPI rank 窃取要非常谨慎，因为 $S_{\max}$ 此时可能包含大块 mesh/particle buffer，通信代价远高于共享内存 deque。


## Review Questions

1. 在 AMReX/WarpX 这类 SFC/knapsack 静态或半静态 box 分配之外，哪些 rank 内任务可以近似建模为 fully strict DAG（ghost fill、boundary fill、AMR subcycling、particle rebin、局部时间步或 multiphysics coupling）？哪些跨层、跨物理模块、跨 rank 依赖会破坏 fully strict 假设，使 $T_1/P + O(T_\infty)$ 与 $S_1P$ 不再直接适用？
2. 在 GPU/PIC/AMR 场景中，$S_{\max}$ 可能不只是 activation frame，而是 tile 数据、MultiFab buffer、particle buffer、pack/unpack buffer 或 kernel batching 状态。如何定义可迁移任务粒度，才能让 $PT_\infty(1+n_d)S_{\max}$ 的通信/迁移成本低于静态负载不均造成的尾部等待？
3. 能否把 work stealing 的随机 victim、偷 top-oldest continuation 原则与 AMReX 的 SFC locality 结合成 locality-aware stealing（先同 worker/NUMA/GPU/rank 内偷，再跨节点偷）？这种策略能否用 Roofline、ECM 或 Hong-Kung I/O 模型量化 cache miss、memory traffic 与 MPI 通信代价？

## Kimi Code Review 结论（2026-08-04）

- 核心公式与三界（$T_1/P+O(T_\infty)$、$S_1P$、$O(PT_\infty(1+n_d)S_{\max})$）与论文一致，DAG 模型、deque 协议、recycling game 与存在性最优的表述基本正确。
- 已修正 9 处：
  1. busy-leaves property 定义改为“活跃 spawn subtree 的每个叶线程被某处理器执行 → 活跃叶数至多 $P$ → 空间界 $S_1P$”（原表述“每个处理器要么忙要么 deque 非空”不准确）；
  2. 删除“比 work sharing 的 $S_1P$ 更优”的自相矛盾表述；
  3. “随机窃取不劣于最优调度”弱化为“期望意义上达到与最优下界 $\max(T_1/P,T_\infty)$ 同阶”；
  4. “work sharing 可能 $O(S_1P\log P)$”弱化为“优于此前 work-sharing scheduler 的相关结果”（原句非本文直接结论）；
  5. continuation 表述改为“留在本地 deque bottom，形成本地 LIFO 深度优先执行轮廓”；
  6. 终止条件弱化为实现层细节（root continuation/join counter/全局计数），论文分析不依赖具体检测机制；
  7. 概率陈述补条件“对任意给定 round 集合（$r\ge 2$，delay-sequence 分析中）”；
  8. 通信界局部解释拆分：join edge resolution 为 $O(n_d)$ 字节，$S_{\max}$ 对应 activation frame 迁移，每次偷窃通信量 $O(n_d)+O(S_{\max})$；
  9. 通信下界 $\Omega(PT_\infty S_{\max})$ 标注为 $n_d=1$ 时与 Theorem 14 一般式等价。
- Markdown/语法：通读未发现未闭合 $\$$ 定界符或标题层级异常；关于 skill 中 display math 建议使用 $\[\ldots\]$ 的规范，因库内全部现有论文统一采用 $\$\$$\ldots\$\$$ 且 GitHub 渲染正常，本次保持库内约定一致（若 Doctor 希望切换全部存量文档格式，可另行安排）。
