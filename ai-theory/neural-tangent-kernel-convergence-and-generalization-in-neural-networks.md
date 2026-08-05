# 神经正切核：神经网络的收敛与泛化

# Neural Tangent Kernel: Convergence and Generalization in Neural Networks

**作者：** Arthur Jacot, Franck Gabriel, Clément Hongler
**期刊：** NeurIPS 2018（Advances in Neural Information Processing Systems 31, pp. 8571-8580, 2018）
**DOI：** 无（会议论文；arXiv 版为正式文本）
**arXiv：** [https://arxiv.org/abs/1806.07572](https://arxiv.org/abs/1806.07572)（v4, 2020-02-10）
**阅读状态：** 🔬 精读（Doctor 指定）
**流程状态：** ①元数据 ✓ | ②初稿 ✓ | ③评估 ✓(精读) | ④补充 ✓ | ⑤索引 ✓ | ⑥review ✓ | ⑦提交 ⏳

---

## 摘要

### 中文翻译
初始化时，人工神经网络（ANN）在无限宽极限下等价于高斯过程，从而与核方法联系起来。本文证明 ANN 在训练过程中的演化也可以由核来描述：在参数梯度下降过程中，网络函数 $f_\theta$（把输入向量映到输出向量）沿**函数代价**（是凸的，与参数代价不同）关于一个新核——**神经正切核（NTK）**——的核梯度演化。该核是刻画 ANN 泛化特征的核心。虽然 NTK 在初始化时是随机的、训练中会变化，但在无限宽极限下它收敛到一个显式的极限核，并在训练期间保持不变。这使得可以在函数空间而非参数空间研究 ANN 的训练。训练的收敛性可归结为极限 NTK 的正定性：本文证明当数据支撑在球面上且非线性非多项式时，极限 NTK 正定。随后聚焦最小二乘回归，证明无限宽极限下网络函数 $f_\theta$ 在训练中满足线性微分方程；收敛沿输入数据关于 NTK 的最大核主成分方向最快，从而为早停（early stopping）提供了理论动机。最后数值研究 NTK 在宽网络上的行为，并与无限宽极限比较。

### 原文
> At initialization, artificial neural networks (ANNs) are equivalent to Gaussian processes in the infinite-width limit, thus connecting them to kernel methods. We prove that the evolution of an ANN during training can also be described by a kernel: during gradient descent on the parameters of an ANN, the network function $f_θ$ (which maps input vectors to output vectors) follows the kernel gradient of the functional cost (which is convex, in contrast to the parameter cost) w.r.t. a new kernel: the Neural Tangent Kernel (NTK). This kernel is central to describe the generalization features of ANNs. While the NTK is random at initialization and varies during training, in the infinite-width limit it converges to an explicit limiting kernel and it stays constant during training. ...

---

## 文章总结

### 1. 解决什么问题？
深度网络的训练动力学（梯度下降如何使网络函数演化、为何能收敛、如何泛化）长期缺乏理论刻画。本文要回答：在无限宽极限下，能否把"参数空间的非凸优化"转化为"函数空间的凸优化"，从而用核方法语言精确描述训练过程与泛化？

### 2. 用了什么方法论？
- 无限宽极限 + 高斯过程对应：初始化时网络输出是高斯过程（NNGP 核）。
- 定义神经正切核 $\Theta(x,x')=\langle \nabla_\theta f_\theta(x),\nabla_\theta f_\theta(x')\rangle$（参数梯度的内积），证明训练中 $f_\theta$ 的演化是 NTK 的核梯度流：$\partial_t f = -\Theta \nabla_f C$（或离散版本的对应）。
- 证明无限宽极限下 NTK 收敛到显式极限核且训练中不变（"lazy training" 机制），从而函数空间的梯度流是线性的。
- 正定性分析：数据在球面上、激活非多项式 ⇒ 极限 NTK 正定 ⇒ 收敛到全局最小。
- 最小二乘下推导 $f_\theta$ 的线性微分方程，谱分解显示收敛速度沿核 PCA 主方向分层（谱偏置的雏形）。

### 3. 主要结论是什么？
无限宽 ANN 的训练等价于带 NTK 的核回归：函数演化由线性微分方程控制、收敛由 NTK 正定性保证、泛化由核的特征结构决定；收敛沿核主成分方向最快，为早停提供理论依据。NTK 由此成为理解"过参数化网络为何可训练、如何泛化、以及为何偏向低频（谱偏置）"的统一框架——这也直接解释了 PINN 等物理约束网络在多尺度/刚性 PDE 上的收敛困难。

---

## 价值评估

Doctor 指定精读（跳过 Codex 价值评估）。

## 公式与代码梳理

（本小节由 Codex 精读补充，2026-08-04）

### 1. 逐公式梳理数学逻辑

本文研究的是宽度趋于无穷的全连接网络。原文采用 NTK 参数化：第 $0$ 层为输入，第 $L$ 层为输出，隐藏层宽度为 $n_1,\dots,n_{L-1}$，参数包含权重 $W^{(\ell)}$ 与偏置 $b^{(\ell)}$。网络函数写作 $f_\theta(x)=\tilde\alpha^{(L)}(x;\theta)$，前向递推为

\[
\alpha^{(0)}(x)=x,\qquad
\tilde\alpha^{(\ell+1)}(x)=\frac{1}{\sqrt{n_\ell}}W^{(\ell)}\alpha^{(\ell)}(x)+\beta b^{(\ell)},\qquad
\alpha^{(\ell)}(x)=\sigma(\tilde\alpha^{(\ell)}(x)).
\]

原文初始化为参数 iid $N(0,1)$，等价于把 $1/\sqrt{n_\ell}$ 缩放写进前向传播；常见 He/LeCun 写法则可理解为 $W^{(\ell)}_{ij}\sim N(0,c_\sigma/n_\ell)$，例如 ReLU 常用 $2/n_\ell$。关键不是常数本身，而是方差随 fan-in 缩放，使每层 preactivation 在宽度增大时保持 $O(1)$。

初始化处，无限宽网络输出收敛到 Gaussian process。其协方差核，也就是 NNGP kernel，按层递推：

\[
\Sigma^{(1)}(x,x')=\frac{1}{n_0}x^\top x'+\beta^2,
\]

\[
\Sigma^{(L+1)}(x,x')=
\mathbb E_{f\sim N(0,\Sigma^{(L)})}
\left[\sigma(f(x))\sigma(f(x'))\right]+\beta^2.
\]

这里期望只需理解为二维高斯向量 $(f(x),f(x'))$ 上的期望。这个结论说明随机宽网络在初始化时已定义了一个函数空间先验，因此自然连接到 Gaussian process、SVM 与 kernel regression 等核方法。

NTK 则刻画训练动力学，而不是只刻画初始化函数分布。对参数向量 $\theta=(\theta_p)_{p=1}^P$，NTK 定义为网络输出对参数梯度的内积：

\[
\Theta^{(L)}(\theta)
=
\sum_{p=1}^{P}
\partial_{\theta_p}F^{(L)}(\theta)\otimes
\partial_{\theta_p}F^{(L)}(\theta),
\]

标量输出时即

\[
\Theta^{(L)}_\theta(x,x')
=
\sum_{p=1}^{P}
\frac{\partial f_\theta(x)}{\partial \theta_p}
\frac{\partial f_\theta(x')}{\partial \theta_p}.
\]

多输出时有矩阵核；无限宽极限下各输出通道解耦，形式为 $\Theta_\infty^{(L)}\otimes I_{n_L}$。原文证明初始化 NTK 收敛到确定性核，其递推为

\[
\Theta^{(1)}_\infty(x,x')=\Sigma^{(1)}(x,x'),
\]

\[
\Theta^{(L+1)}_\infty(x,x')
=
\Theta^{(L)}_\infty(x,x')\dot\Sigma^{(L+1)}(x,x')
+
\Sigma^{(L+1)}(x,x'),
\]

其中

\[
\dot\Sigma^{(L+1)}(x,x')
=
\mathbb E_{f\sim N(0,\Sigma^{(L)})}
\left[\dot\sigma(f(x))\dot\sigma(f(x'))\right].
\]

递推的两项有清楚含义：$\Sigma^{(L+1)}$ 来自最后一层线性读出参数的学习；$\Theta^{(L)}\dot\Sigma^{(L+1)}$ 来自更低层参数经链式法则传递到输出的贡献。

训练部分把参数梯度下降转写为函数空间的 kernel gradient flow。若代价泛函为 $C(f)$，训练集为 $\{x_i\}_{i=1}^N$，则有限宽网络满足

\[
\partial_t f_t(x)
=
-\frac{1}{N}\sum_{i=1}^{N}
\Theta_t(x,x_i)\,
\partial_{f(x_i)}C\big|_{f=f_t}.
\]

这不是近似，而是由链式法则得到的连续时间精确动力学；有限宽时 $\Theta_t$ 随训练变化。离散梯度下降对应

\[
\theta_{k+1}=\theta_k-\eta\nabla_\theta C(f_{\theta_k}),
\]

其函数增量的一阶形式为

\[
f_{\theta_{k+1}}(x)-f_{\theta_k}(x)
\approx
-\eta\frac{1}{N}\sum_i
\Theta_{\theta_k}(x,x_i)\,
\partial_{f(x_i)}C.
\]

无限宽极限的第二个核心结论是 training 中 NTK 保持常数：

\[
\Theta_t^{(L)}\to \Theta_\infty^{(L)}\otimes I_{n_L},
\qquad t\in[0,T].
\]

于是非线性参数优化在函数空间中退化为固定核的线性动力系统：

\[
\partial_t f_t
=
-\Theta_\infty\nabla_f C(f_t).
\]

对最小二乘

\[
C(f)=\frac{1}{2}\|f-f^\ast\|_{p_{\rm in}}^2,
\]

有

\[
\partial_t f_t=\Phi_K(\langle f^\ast-f_t,\cdot\rangle_{p_{\rm in}}),
\qquad
f_t=f^\ast+e^{-t\Pi}(f_0-f^\ast),
\]

其中 $\Pi(f)=\Phi_K(\langle f,\cdot\rangle_{p_{\rm in}})$。在训练集 Gram 矩阵记号下（有限维训练集表示、线性化/核化设定），可写成

\[
f_t(X)=y+e^{-\eta \Theta t}(f_0(X)-y),
\]

若 $\Theta=U\Lambda U^\top$，则

\[
f_t(X)-y
=
Ue^{-\eta\Lambda t}U^\top(f_0(X)-y).
\]

> 注：上述含 $\Theta$ 的等式仅在无限宽极限（核在训练中恒定）下严格成立；有限宽时 $\Theta_t$ 会漂移，等式只是近似。

所以特征值 $\lambda_i$ 大的方向以 $e^{-\eta\lambda_i t}$ 快速衰减，特征值小的方向慢。这就是本文谱偏置结论的核心：训练优先拟合 NTK kernel PCA 的大主成分；“低频、平滑”是对该谱偏置的直观类比（在平移不变的平滑核下成立），并非普适定理；高频或噪声方向落在小特征值子空间，收敛慢，也为 early stopping 提供理论动机。

正定性保证收敛。若数据支撑在球面 $S^{d-1}$，激活 $\sigma$ 是非多项式 Lipschitz 函数，则 $L\ge 2$ 时 $\Theta_\infty^{(L)}$ 在球面上正定。证明思路是：先把 $\Theta^{(L+1)}=\dot\Sigma^{(L+1)}\Theta^{(L)}+\Sigma^{(L+1)}$ 分解为正半定项加 NNGP 项；再证明 $\Sigma^{(2)}$ 在球面上正定；最后利用 Hermite 展开与 Schoenberg 型定理。若

\[
\mu=\sum_{i=0}^{\infty}a_i h_i,
\]

则 dual activation kernel 满足

\[
\hat\mu(\rho)=\sum_{i=0}^{\infty}a_i^2\rho^i.
\]

非多项式激活带来无限多个非零系数，经过球面内积核 $K(x,x')=\nu(x^\top x')$ 的幂级数判别，可得正定性。因此核梯度流的代价严格下降，凸损失下收敛到全局最优。

这也解释了 lazy training / 线性化网络。无限宽时单个隐藏神经元 activation 的变化趋于零，参数只在初始化附近小幅移动，因此

\[
f_\theta(x)\approx f_{\theta_0}(x)+
\nabla_\theta f_{\theta_0}(x)^\top(\theta-\theta_0).
\]

训练等价于这个随机特征线性模型的核回归；NTK 就是这些切向特征 $\nabla_\theta f_{\theta_0}$ 的 Gram 核。其代价是：理论上获得了可解动力学，但表示学习能力被压到初始化附近，不能完全描述有限宽网络中 feature learning 的变化。

### 2. 算法/代码流程梳理

本文无代码，但可直接推出 NTK 的实用计算路径。给定 MLP 与一批输入 $X=\{x_i\}_{i=1}^N$，empirical NTK 的最直接实现是对每个样本计算输出对全部参数的 Jacobian：

\[
J_i=\nabla_\theta f_\theta(x_i),
\qquad
\Theta_{ij}=J_iJ_j^\top.
\]

多输出时 $\Theta_{ij}$ 是输出维度之间的块矩阵。自动微分实现中，可用 JAX 的 `jacrev`/`vmap`，或 PyTorch `functorch`/`torch.func` 的 `functional_call + jacrev + vmap`，先把参数展平成 PyTree Jacobian，再对所有参数叶子做 contraction。显式拼接全 Jacobian 简单但内存大；更实用的路径是逐层累加

\[
\Theta(x,x')=\sum_{\ell}
\left\langle
\partial_{\theta^{(\ell)}}f(x),
\partial_{\theta^{(\ell)}}f(x')
\right\rangle,
\]

避免一次性展开全部参数。若只需要无限宽理论核，可按 $\Sigma,\dot\Sigma,\Theta$ 的层递推计算；对 ReLU 还可用闭式 arc-cosine kernel。

用 NTK 做 kernel regression 时，先构造训练 Gram 矩阵 $\Theta(X,X)$，再对测试点计算 $\Theta(x_\ast,X)$。零正则极限预测为

\[
\hat f(x_\ast)
=
\Theta(x_\ast,X)\Theta(X,X)^{-1}y,
\]

数值上通常加入 ridge：

\[
\hat f(x_\ast)
=
\Theta(x_\ast,X)
\left(\Theta(X,X)+\lambda I\right)^{-1}y.
\]

验证“无限宽下训练中 $\Theta$ 不变”的实验也直接：取宽度 $n=100,1000,10000$ 的同构 MLP；在 $t=0,t_1,t_2$ 计算 empirical NTK；记录相对漂移

\[
\frac{\|\Theta_t-\Theta_0\|_F}{\|\Theta_0\|_F}.
\]

若 NTK 理论成立，宽度越大漂移越小，函数轨迹越接近固定核梯度流；较窄网络可能出现 kernel inflation 或 feature learning。

对 PINN 类网络，NTK 视角尤其有诊断价值。PINN 损失通常由数据项、边界项、初值项、PDE residual 项组成：

\[
\mathcal L
=
\lambda_u\mathcal L_u+
\lambda_b\mathcal L_b+
\lambda_r\mathcal L_r.
\]

不同项对应不同微分算子作用后的 NTK 块，例如 residual kernel 近似为

\[
\Theta_{rr}(x,x')
=
\mathcal D_x\mathcal D_{x'}\Theta_{uu}(x,x'),
\]

其中 $\mathcal D$ 是 PDE 残差算子。多尺度 PDE、高阶导数、边界层和高频解会把目标分量投到 NTK 小特征值方向，导致 residual 长期不降或局部收敛失败。物理约束一方面能排除不守恒、不满足边界的函数；另一方面也可能把优化重点压到刚性高频方向，使谱不平衡更严重。因此 Wang-Yu-Perdikaris 类 NTK adaptive weighting 可以理解为重标定不同损失块的特征值尺度，让数据、边界、残差项以更接近的速度收敛。

### 3. 与库内相关论文的关联

> 注：以下关联均为 NTK 视角下的诊断性解读，用于理解训练动力学，并非姊妹论文自身的结论。

- `ai-for-physics/physics-informed-neural-networks-a-deep-learning-framework-for-solving-forward-a.md`：PINN 的训练失败可用 NTK 谱解释。多尺度 PDE residual、边界条件和观测数据对应不同核块；若 residual 块小特征值占主导，网络会先拟合低频/数据项，迟迟不能满足 PDE。NTK 加权方案正是沿这个方向修正损失尺度。

- `ai-for-physics/nsfnets-navier-stokes-flow-nets-physics-informed-neural-networks-for-the-incompr.md`：NSFnets 面向不可压 Navier-Stokes，压力、速度、连续性约束与动量残差共同训练。NTK 视角可解释高 Reynolds 数、涡结构、边界层下的慢收敛：高频流动结构通常落在小特征值方向。

- `ai-for-physics/hamiltonian-neural-networks.md` 与 `ai-for-physics/liepoisson-neural-networks-lpnets-data-based-computing-of-hamiltonian-systems-wi.md`：HNN/LPNets 是结构保持学习。NTK 视角下，Hamiltonian、Poisson tensor、Casimir、对称性约束会改变可学习函数空间与切向特征，从而改变核的谱；结构约束可能减少无物理意义方向，但也可能让某些守恒相关方向更难优化。

- `ai-model/denoising-diffusion-probabilistic-models.md`：DDPM 学的是 score/noise prediction 的时间族函数。它不是典型 NTK 论文，但可从函数空间动力学联系：若把 score network 线性化，训练也对应某个时间条件 NTK 上的核回归；不过实际 diffusion 依赖强 feature learning，纯 lazy NTK 只适合局部诊断。

- `ai-theory/geometric-deep-learning-grids-groups-graphs-geodesics-and-gauges.md`：等变/不变架构会把函数空间限制到满足群作用约束的子空间。对应 NTK 也会变成 group-averaged 或 equivariant NTK，核的特征函数按群表示分解；这为“结构先验如何改变谱偏置”提供理论语言。

因此，NTK 在“ML 基础理论 → PINN/物理学习应用”主线中起承上启下作用：它把训练动力学、泛化、early stopping、谱偏置统一成核谱问题。对 Doctor 的价值在于，可用核语言诊断物理约束网络为什么某些残差项慢、为什么高频/多尺度解难、以及为什么结构约束与自适应损失权重能改变收敛路径。

## Review Questions

1. 这篇 NTK 笔记里把“训练动力学 → 固定核梯度流 → 谱偏置”串成一条主线；如果把同样的 NTK 视角放到 PINN 上，哪些慢收敛现象是核谱本身导致的，哪些其实来自损失构造或采样策略？能否给出可验证的区分标准？
2. HNN / LPNets 通过结构约束缩小可学习函数空间；从 NTK 角度看，这种约束是主要在“改核的谱”，还是在“改可达表示子空间”？二者对守恒量学习和优化速度的影响是否能分开测量？
3. 如果把 NTK 的谱偏置类比到几何深度学习或等变网络，群对称性到底是在提升泛化，还是在重排特征值分布、改变早停偏好？这和普通 MLP 的 kernel PCA 解释相比，哪里是同构的，哪里不是？
