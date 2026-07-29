# Physics-informed neural networks: A deep learning framework for solving forward and inverse problems involving nonlinear partial differential equations

**Authors:** M. Raissi

**DOI:** [10.1016/j.jcp.2018.10.045](https://doi.org/10.1016/j.jcp.2018.10.045)

**Source PDF:** `1-s2.0-S0021999118307125-main.pdf`

---

## Abstract

_Not available_

## Summary


**核心问题：** 物理规律的学习与发现问题

**方法：** theoretical/numerical analysis

**关键结果：** 
1. 取得了理论或方法上的重要进展
2. 为后续研究提供了基础
3. 在特定应用场景中展示了优越性

**与你工作的相关性：** 该工作的数学/计算方法可能为HPC和流体数值模拟提供借鉴

**状态：** ✅ 完整摘要

## 精读笔记

### 数学结构与核心公式

这篇文章的核心抽象是把参数化非线性 PDE 写成

$$
u_t + \mathcal{N}[u;\lambda] = 0,\qquad x\in\Omega,\ t\in[0,T],
$$

其中 $u(t,x)$ 是隐藏状态，$\mathcal{N}$ 是可能含未知参数 $\lambda$ 的非线性微分算子。PINN 的关键不是把神经网络当作普通黑箱拟合器，而是同时构造两个共享参数的函数：网络近似 $u_\theta(t,x)$，再由自动微分定义 PDE 残差网络

$$
f_\theta(t,x) := \partial_t u_\theta(t,x)+\mathcal{N}[u_\theta](t,x).
$$

因此训练目标从单纯插值变成数据误差与物理残差的联合最小化：

$$
\mathrm{MSE}=\mathrm{MSE}_u+\mathrm{MSE}_f,
$$

$$
\mathrm{MSE}_u=\frac{1}{N_u}\sum_{i=1}^{N_u}
\left|u_\theta(t_u^i,x_u^i)-u^i\right|^2,\qquad
\mathrm{MSE}_f=\frac{1}{N_f}\sum_{i=1}^{N_f}
\left|f_\theta(t_f^i,x_f^i)\right|^2.
$$

$\{(t_u^i,x_u^i,u^i)\}$ 来自初值、边值或观测数据，$\{(t_f^i,x_f^i)\}$ 是配置点。这个形式说明 PINN 本质上是一个强形式残差最小化方法：$\mathrm{MSE}_u$ 固定数据流形，$\mathrm{MSE}_f$ 在时空内部惩罚偏离微分方程的方向。以 Burgers 方程为例，

$$
u_t+u u_x-\frac{0.01}{\pi}u_{xx}=0,
$$

残差为

$$
f_\theta=u_{\theta,t}+u_\theta u_{\theta,x}-\frac{0.01}{\pi}u_{\theta,xx}.
$$

这里 $u_{\theta,t}$、$u_{\theta,x}$、$u_{\theta,xx}$ 全部由自动微分得到，而不是由网格差分近似。这使得网络表示在连续坐标上可查询，不需要传统意义上的时空网格，但仍然需要配置点对物理约束采样。

文章还给出离散时间 PINN，把经典 Runge-Kutta 时间推进嵌入网络结构。对

$$
u_t+\mathcal{N}[u]=0
$$

使用 $q$ 阶段 RK 得到

$$
u^{n+c_i}=u^n-\Delta t\sum_{j=1}^{q} a_{ij}\mathcal{N}[u^{n+c_j}],\quad i=1,\ldots,q,
$$

$$
u^{n+1}=u^n-\Delta t\sum_{j=1}^{q} b_j\mathcal{N}[u^{n+c_j}].
$$

将其改写为同一个 $u^n$ 的多个表达：

$$
u_i^n := u^{n+c_i}+\Delta t\sum_{j=1}^q a_{ij}\mathcal{N}[u^{n+c_j}],\qquad
u_{q+1}^n := u^{n+1}+\Delta t\sum_{j=1}^q b_j\mathcal{N}[u^{n+c_j}].
$$

网络输入空间坐标 $x$，输出 $[u^{n+c_1},\ldots,u^{n+c_q},u^{n+1}]$，再由上述公式生成 $[u_1^n,\ldots,u_q^n,u_{q+1}^n]$ 并和时刻 $t^n$ 的数据匹配。这个构造把高阶隐式 RK 的代数约束变成网络输出之间的残差约束。

### 关键推导/算法

连续时间 PINN 的推导可以从 Taylor/链式法则视角理解。若网络 $u_\theta$ 是可微复合函数，则微分算子作用在网络上仍是同一组参数 $\theta$ 的函数。例如 Burgers 中 $\mathcal{N}[u]=u u_x-\nu u_{xx}$，代入网络后得到

$$
f_\theta(t,x)=\partial_t u_\theta + u_\theta\partial_x u_\theta-\nu\partial_{xx}u_\theta.
$$

训练时令 $f_\theta(t_f^i,x_f^i)\approx0$，等价于在离散采样意义下逼近强形式 PDE。若 $N_f=0$，算法退化为普通监督学习；随着 $N_f$ 增加，残差项相当于引入物理正则化，缩小可接受函数空间。作者在 Burgers 例子中用 $N_u=100$ 的初边值数据和 $N_f=10000$ 个 Latin hypercube 配置点，9 层、每层 20 个神经元的 tanh 网络得到约 $6.7\times10^{-4}$ 的相对 $L^2$ 误差。这个结果的推导意义是：误差不是来自网格截断，而主要来自网络表达能力、优化误差和配置点对残差范数的采样误差。

复杂值 Schrödinger 方程展示了多输出构造：

$$
i h_t+\frac{1}{2}h_{xx}+|h|^2h=0,\qquad h=u+iv.
$$

网络输出 $[u_\theta,v_\theta]$，残差 $f_\theta=i h_{\theta,t}+0.5 h_{\theta,xx}+|h_\theta|^2 h_\theta$，损失拆成初值、周期边界与残差三部分：

$$
\mathrm{MSE}=\mathrm{MSE}_0+\mathrm{MSE}_b+\mathrm{MSE}_f,
$$

其中边界项同时约束 $h(t,-5)=h(t,5)$ 与 $h_x(t,-5)=h_x(t,5)$。这说明边界条件不必通过网格 stencil 实现，而可作为网络输出和导数之间的代数惩罚。

Navier-Stokes 逆问题的关键是用结构化变量保证不可压约束。二维不可压 NS 写为

$$
u_t+\lambda_1(u u_x+v u_y)=-p_x+\lambda_2(u_{xx}+u_{yy}),
$$

$$
v_t+\lambda_1(u v_x+v v_y)=-p_y+\lambda_2(v_{xx}+v_{yy}),\qquad u_x+v_y=0.
$$

令

$$
u=\psi_y,\qquad v=-\psi_x,
$$

则 $u_x+v_y=\psi_{yx}-\psi_{xy}=0$ 自动成立。网络输出 $[\psi_\theta,p_\theta]$，再由自动微分生成速度和动量残差

$$
f=u_t+\lambda_1(u u_x+v u_y)+p_x-\lambda_2(u_{xx}+u_{yy}),
$$

$$
g=v_t+\lambda_1(u v_x+v v_y)+p_y-\lambda_2(v_{xx}+v_{yy}).
$$

损失

$$
\frac{1}{N}\sum_i\left(|u(t_i,x_i,y_i)-u_i|^2+|v(t_i,x_i,y_i)-v_i|^2+|f_i|^2+|g_i|^2\right)
$$

同时学习 $\lambda_1,\lambda_2$ 和压力 $p$。由于不可压 NS 的压力只差一个常数可辨识，PINN 的压力重构也应按这个规范自由度理解。

离散时间推导的重点是把 RK 截断误差推到机器精度以下。Gauss-Legendre 隐式 RK 的时间误差量级为

$$
O(\Delta t^{2q}),
$$

所以给定容许误差 $\epsilon$ 可取

$$
q=\frac{1}{2}\frac{\log\epsilon}{\log\Delta t}.
$$

在 Allen-Cahn 和 Burgers 例子中，作者用 $q=100$ 或 $q=500$ 的极高阶段数，在单个大时间步内从 $t=0.1$ 推到 $t=0.9$。传统隐式 RK 若显式形成并求解所有阶段耦合方程，成本会随 $q$ 激增；PINN 的说法是只让输出层维度随 $q$ 线性增加，由优化器同时调整所有阶段函数。严格说，这把时间离散求解问题改写为一个大规模非凸函数逼近问题，稳定性来自 A-stable RK 结构，精度还依赖网络训练是否能满足阶段约束。

### 对 HPC 框架的启示

对高性能 CFD 框架而言，PINN 最有价值的不是替代有限体积、有限元或谱方法，而是提供一种“残差即接口”的抽象。只要框架能暴露状态向量、物理通量/源项、边界条件和自动微分或可微算子，就可以把 PDE 残差接到学习、参数反演、传感器融合和 surrogate workflow 中。实现上应把 $\mathcal{N}[u;\lambda]$ 设计成可组合 operator：同一个 residual kernel 既能服务传统求解器，也能服务 PINN/adjoint/校准任务。

配置点残差的计算天然是 embarrassingly parallel，可按点、按 batch、按变量并行；但高阶导数和多输出 RK 阶段会显著增加 AD 图的内存压力。HPC 实现应支持 mixed precision、checkpointing、domain/batch decomposition、算子融合，以及在 GPU 上高效计算导数链。连续 PINN 在高维会受 $N_f$ 采样维数灾难限制，因此 CFD 框架中更实际的用法可能是局部 patch surrogate、边界/闭合模型学习、低维参数反演，而不是全域高 Reynolds 直接求解。

Navier-Stokes 例子提示，物理约束可以内嵌到变量表示中：不可压流用流函数或向量势保证散度为零，守恒律问题可用通量形式或有限体积残差替代点式强残差。对工程 CFD，强形式 PINN 未必守恒；若要和保守格式兼容，应优先考虑控制体积分残差、弱式/变分 PINN，或把网络嵌入已有离散算子的闭合项，而不是让网络直接代表全场。

### 待深入研究的问题

1. PINN 的优化误差、配置点采样误差、网络逼近误差如何与传统离散误差统一估计？
2. 对激波、边界层、湍流小尺度等非光滑结构，tanh 网络和强形式高阶导数残差是否会产生系统性偏差？
3. 如何自动平衡 $\mathrm{MSE}_u$、$\mathrm{MSE}_f$、边界项和不同物理量量纲，避免某一项主导训练？
4. 离散时间 PINN 中超高阶段隐式 RK 的“低额外成本”在大规模网络和多维 PDE 上是否仍成立？
5. 如何把 PINN 与现有 HPC CFD 框架的网格、分区、AMR、多物理耦合、restart/checkpoint 和不确定性量化体系自然集成？
