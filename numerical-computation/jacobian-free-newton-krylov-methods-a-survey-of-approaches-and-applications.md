# Jacobian-free Newton-Krylov 方法：方法与应用综述

**作者：** D. A. Knoll、D. E. Keyes

**期刊：** Journal of Computational Physics, 193 (2004) 357–397

**DOI：** [10.1016/j.jcp.2003.08.010](https://doi.org/10.1016/j.jcp.2003.08.010)

**源 PDF：** `JFK.pdf`

---

## 摘要

_暂无_

## 总结

**核心问题：** Jacobian-free Newton-Krylov（JFNK）方法的全面综述——方法、应用和前沿

**方法：** 全面综述JFNK方法：从基本概念（Newton非线性迭代+Krylov线性迭代的嵌套）到关键技术（预条件、强制项选择、全局化策略），涵盖在流体力学、反应流、MHD、辐射输运等领域的应用。

**关键结果：**
- JFNK是解决大规模非线性PDE系统的最有效方法之一
- 预条件子的质量是JFNK性能的决定性因素
- 矩阵无关实现（通过有限差分近似Jacobian-向量积）避免存储Jacobian，适合超大规模问题

**与你工作的相关性：** JFNK方法是HPC框架中大规模非线性求解的核心技术，该综述提供了完整的方法论指导。

**状态：** ✅ 完整摘要

## 精读笔记

### 数学结构与核心公式

JFNK 的目标是求解离散 PDE 产生的非线性代数系统

\[
F(u)=0,\qquad F:\mathbb{R}^n\rightarrow\mathbb{R}^n.
\]

Newton 法从当前迭代 $u^k$ 处的多元 Taylor 展开出发：

\[
F(u^{k+1})=F(u^k)+F'(u^k)(u^{k+1}-u^k)+O(\|u^{k+1}-u^k\|^2).
\]

忽略高阶项并令右端为零，得到 Newton 修正方程

\[
J(u^k)\delta u^k=-F(u^k),\qquad u^{k+1}=u^k+\delta u^k,
\]

其中 $J=F'(u)$。终止准则通常包括非线性残差下降

\[
\frac{\|F(u^k)\|}{\|F(u^0)\|}<\mathrm{tol}_{res}
\]

以及更新量足够小

\[
\frac{\|\delta u^k\|}{\|u^k\|}<\mathrm{tol}_{update}.
\]

Krylov 子空间法求解线性系统 $Ax=b$ 时只需要矩阵向量积。给定初始线性残差 $r_0=b-Ax_0$，第 $j$ 步 Krylov 空间为

\[
\mathcal{K}_j(A,r_0)=\mathrm{span}\{r_0,Ar_0,A^2r_0,\ldots,A^{j-1}r_0\}.
\]

在 Newton 修正方程中，GMRES 在这个低维空间内最小化线性残差。若修正初猜 $\delta u_0=0$，则

\[
r_0=-F(u)-J\delta u_0=-F(u),
\]

并在

\[
\delta u_j=\delta u_0+\sum_{i=0}^{j-1}\beta_i J^i r_0
\]

中选择系数使 $\|J\delta u_j+F(u)\|_2$ 最小。

Jacobian-free 的核心是用 Fréchet 导数的有限差分近似 $Jv$：

\[
J(u)v \approx \frac{F(u+\varepsilon v)-F(u)}{\varepsilon}.
\]

这保留了当前非线性残差 $F$ 的真实离散算子，不显式形成和存储 $J$。对双变量例子，Taylor 展开

\[
F_i(u+\varepsilon v)=F_i(u)+\varepsilon\sum_j \frac{\partial F_i}{\partial u_j}v_j+O(\varepsilon^2)
\]

代回差商得

\[
\frac{F_i(u+\varepsilon v)-F_i(u)}{\varepsilon}
=\sum_j J_{ij}v_j+O(\varepsilon),
\]

所以误差由截断项 $O(\varepsilon)$ 和浮点消去误差共同决定。文中给出若干 $\varepsilon$ 选择公式，例如

\[
\varepsilon=\frac{1}{n\|v\|_2}\sum_{i=1}^n b|u_i|+b,
\]

或 Brown-Saad 型

\[
\varepsilon=
\frac{b}{\|v\|_2}\max\{|u^T v|,\mathrm{typ}u\,|v|\}\,\mathrm{sign}(u^T v),
\]

其中 $b$ 通常和机器精度平方根同量级；若残差评估本身只有相对精度 $\epsilon_{rel}$，则应取 $b\sim\sqrt{\epsilon_{rel}}$ 而不是盲目取 $\sqrt{\epsilon_{mach}}$。

### 关键推导/算法

JFNK 是四层嵌套结构：外层是 Newton 或 inexact Newton，中间是 GMRES/BiCGSTAB/TFQMR 等 Krylov 线性求解，Krylov 内部通常有预条件器，最外侧常配合全局化策略如伪瞬态延拓、线搜索、信赖域、物理参数延拓或网格序列。

Inexact Newton 的关键是线性系统不必精确求解，而是满足

\[
\|J(u^k)\delta u^k+F(u^k)\|_2
<\eta_k\|F(u^k)\|_2,
\]

其中 $\eta_k$ 是 forcing term。若 $\eta_k$ 过大，每步 Newton 方向太粗，非线性迭代数增加；若过小，早期会“oversolve”：花大量 Krylov 迭代精确求解一个还不可信的线性化模型，甚至导致更新质量变差。工程实现中应让 $\eta_k$ 随非线性收敛动态收紧，而不是固定到很小。

右预条件 JFNK 的代数结构是

\[
(JP^{-1})(P\delta u)=-F(u).
\]

令 $w=P\delta u$，先解

\[
JP^{-1}w=-F(u),
\]

再计算

\[
\delta u=P^{-1}w.
\]

在 Jacobian-free 场景中，Krylov 所需乘积变为

\[
JP^{-1}v
\approx
\frac{F(u+\varepsilon P^{-1}v)-F(u)}{\varepsilon}.
\]

因此每次 GMRES 迭代实际分两步：先近似解 $Py=v$ 得 $y=P^{-1}v$，再调用一次残差函数计算 $[F(u+\varepsilon y)-F(u)]/\varepsilon$。这也解释了 JFNK 的“多 Jacobian 表示”：外层前向作用使用真实残差的差分，内层逆作用 $P^{-1}$ 可以来自过时 Jacobian、低阶离散、分裂算法、多重网格或物理近似。

预条件是全文的中心。标准做法包括 stale/frozen Jacobian：预条件矩阵每隔若干 Newton 步才重建，但 $Jv$ 始终通过当前 $F$ 差分感知真实 Jacobian；这区别于 modified Newton，因为外层线性化没有冻结。对对流主导守恒律，可用高阶离散评估残差 $F_{high}$，用低阶 upwind 离散构造预条件：

\[
JP_{low}^{-1}v
\approx
\frac{F_{high}(u+\varepsilon P_{low}^{-1}v)-F_{high}(u)}{\varepsilon}.
\]

这样最终收敛到高阶离散解，但 ILU/Schwarz 处理的是更稳定、更稀疏、更便宜的低阶算子。

Newton-Krylov-Schwarz 把区域分解作为预条件器。标准 additive Schwarz 可写为

\[
P_{ASM}^{-1}=\sum_i R_i^T J_i^{-1}R_i,
\]

$R_i$ 将全局向量限制到子域，$J_i^{-1}$ 是子域近似求解，$R_i^T$ 把局部修正延拓回全局。Restricted ASM 改成

\[
P_{RASM}^{-1}=\sum_i R_i^{0T}J_i^{-1}R_i,
\]

通过限制延拓阶段的通信降低邻接通信，文中指出可减少约一半近邻通信并常有更好预条件效果。两层 Schwarz 添加粗网格项后，在理想椭圆问题上迭代数可从依赖 $N$ 或子域数 $P$ 改善到 $O(1)$。

物理预条件的推导最有代表性。浅水方程

\[
h_t+(uh)_x=0,\qquad
(uh)_t+(u^2h)_x=-gh h_x
\]

含刚性重力波。半隐式线性化只隐式处理快波：

\[
\frac{h^{n+1}-h^n}{\Delta t}+\partial_x(uh)^{n+1}=0,
\]

\[
\frac{(uh)^{n+1}-(uh)^n}{\Delta t}+\partial_x(u^2h)^n+g h^n\partial_x h^{n+1}=0.
\]

由动量式得

\[
(uh)^{n+1}=-\Delta t\,g h^n\partial_x h^{n+1}+S^n,
\qquad
S^n=(uh)^n-\Delta t\,\partial_x(u^2h)^n.
\]

代入质量方程，得到只关于 $h^{n+1}$ 的标量抛物型问题：

\[
\frac{h^{n+1}-h^n}{\Delta t}
-\partial_x\left(\Delta t\,g h^n\partial_x h^{n+1}\right)
=-\partial_x S^n.
\]

作为预条件器时写成 delta form，把残差 $(r_h,r_{uh})$ 映射到修正 $(\delta h,\delta uh)$：

\[
\frac{\delta h}{\Delta t}+\partial_x\delta(uh)=-r_h,
\qquad
\frac{\delta(uh)}{\Delta t}+g h^n\partial_x\delta h=-r_{uh}.
\]

消去 $\delta(uh)$ 得

\[
\frac{\delta h}{\Delta t}
-\partial_x\left(\Delta t\,g h^n\partial_x\delta h\right)
=-r_h+\partial_x(\Delta t\,r_{uh}),
\]

解一个标量抛物问题后再回代

\[
\delta(uh)=-\Delta t\,g h^n\partial_x\delta h-\Delta t\,r_{uh}.
\]

JFNK 的外层仍对完整非线性双曲系统求根，预条件器只需近似消除快波刚性；这正是“用便宜物理近似改善线性谱，而不改变最终离散方程”的思想。

### 对 HPC 框架的启示

JFNK 对高性能 CFD 框架的架构启示很直接：最核心的 API 是 `residual(u)`，其次是 `apply_preconditioner(v)`。只要残差函数可重入、可并行、可对扰动状态评估，就能获得 Jacobian-free 的 Newton-Krylov 外壳；Jacobian 装配应变成可选优化，而不是求解器正确性的前提。

预条件器必须是插件式和多层次的。框架应允许同一问题同时挂接低阶离散 ILU、block ILU、Schwarz/RASM、AMG/GMG、SIMPLE、半隐式快波消元、operator-split 旧代码、FFT Poisson solver 等。外层残差保持高阶、保守、完整耦合；内层预条件可低阶、冻结、分裂、局部化。这样可以复用 legacy solver，把原来的 Picard/SIMPLE/ADI/半隐式步骤改写成 delta form，作为 $P^{-1}$。

并行实现上，JFNK 的 $Jv$ 是一次或两次残差评估，天然继承残差 kernel 的 MPI/GPU 并行性；瓶颈转移到预条件和 GMRES 存储。GMRES 需要保存 Arnoldi 向量，restart 维度、正交化方式和通信规约成本必须可调。Schwarz 子域 solve 要考虑 overlap、粗网格、局部 ILU fill、cache blocking 和 GPU resident 数据；RASM 减少 prolongation 通信，对大规模分布式 CFD 很有吸引力。

全局化也应是一等公民。稳态 CFD、燃烧、等离子体边界层和激波问题不能只暴露 `newton_solve()`；应支持伪瞬态延拓、CFL/时间步演化律、网格序列、物理参数 continuation、低阶到高阶离散 continuation。FUN3D 案例说明，早期用一阶对流稳定 shock 位置、收敛后切到二阶残差，是求解策略的一部分，不只是数值通量选择。

### 待深入研究的问题

1. 如何自动选择有限差分扰动 $\varepsilon$，特别是在多物理变量量纲差异大、残差评估含 limiter/lookup/table 时？
2. 预条件器质量如何在线诊断：GMRES 迭代数上升时应重建 Jacobian、增加 overlap、切换 multigrid，还是收紧/放松 forcing term？
3. 对 GPU/异构架构，GMRES 正交化通信和预条件器不规则访存之间如何权衡？
4. 对含激波、相变、燃烧前沿的非光滑问题，ASPIN、伪瞬态、网格序列、低阶残差 continuation 如何组合成稳健 polyalgorithm？
5. 在 PDE 约束优化中，JFNK/LNK 需要 $J^T v$ 和二阶信息；有限差分 Jacobian-free 不够，如何在大型 CFD 代码中系统引入自动微分而不破坏性能和可维护性？

## Review Questions

### 复习问题
1. **问：** 为什么 inexact Newton 的 forcing term 需要动态调整而不是固定不变？在 Newton 早期迭代中，“过度求解”和“求解不足”分别会带来什么不同风险？
2. **问：** Jacobian-free 近似 $Jv \approx [F(u+\varepsilon v)-F(u)]/\varepsilon$ 为什么能在只使用近似 Jacobian 作用的同时保留原始非线性残差的离散结构？扰动 $\varepsilon$ 的选择为什么对截断误差和舍入误差的平衡至关重要？
3. **问：** 在 Newton-Krylov-Schwarz 中，restricted additive Schwarz（RASM）如何减少通信开销？为什么它有时会在只计算更少信息的情况下，仍比标准 ASM 取得更好的收敛速度？
