# Fourier Neural Operator for Parametric Partial Differential Equations（参数偏微分方程的傅里叶神经算子）

**作者：** Zongyi Li, Nikola Kovachki, Kamyar Azizzadenesheli, Burigede Liu, Kaushik Bhattacharya, Andrew Stuart, Anima Anandkumar
**期刊：** ICLR 2021（arXiv 预印本 2020）
**DOI：** 无（会议论文）
**arXiv：** [https://arxiv.org/abs/2010.08895](https://arxiv.org/abs/2010.08895)
**阅读状态：** 🔬 精读
**流程状态：** ①元数据 ✓ | ②初稿 ✓ | ③评估 ✓(精读) | ④补充 ✓ | ⑤索引 ✓ | ⑥review ✓ | ⑦提交 ✓

---

## 摘要

### 中文翻译

神经网络的传统发展主要关注有限维欧氏空间之间的映射学习。最近这被推广到神经算子（neural operator），即学习函数空间之间的映射。对于偏微分方程（PDE），神经算子直接学习从任意函数参数依赖到解的映射，从而学习一族 PDE，而经典方法只求解方程的单个实例。本文提出傅里叶神经算子（FNO）：在傅里叶空间中进行参数化，实现对分辨率不变的神经算子学习。在 Burgers 方程、达西渗流（Darcy flow）和 Navier-Stokes 方程上验证，FNO 比现有深度学习方法快约一个数量级，且在达西问题上比传统数值求解器快三个数量级，同时保持泛化能力。

### 原文

> The classical development of neural networks has primarily focused on learning mappings between finite-dimensional Euclidean spaces. Recently, this has been generalized to neural operators that learn mappings between function spaces. For partial differential equations (PDEs), neural operators directly learn the mapping from any functional parametric dependence to the solution. Thus, they learn an entire family of PDEs, in contrast to classical methods which solve one instance of the equation. In this work, we formulate a new neural operator architecture, the Fourier neural operator, that directly learns the mapping from parametric PDEs to their solutions. The Fourier neural operator combines a neural network architecture with Fourier transformation to learn a resolution-invariant operator. We validate the Fourier neural operator on Burgers' equation, Darcy flow, and the Navier-Stokes equation. The Fourier neural operator achieves state-of-the-art performance compared to existing neural network methods and up to three orders of magnitude faster than traditional PDE solvers.

---

## 文章总结

### 1. 解决什么问题？

经典神经网络只能学习有限维空间之间的映射；对参数化 PDE 族，传统方法每个参数实例都要重新求解。需要一种能学习"从 PDE 参数/系数到解"的算子级映射、且对网格分辨率不变的方法。

### 2. 用了什么方法论？

在谱域参数化积分核：将核积分算子 $\mathcal{K}$ 的卷积作用改为傅里叶空间中的逐点相乘，学习频率域权重矩阵 $R_\phi$，配合提升/投影层（lifting/projection）与逐点激活，构成迭代的算子层（Fourier layer），实现分辨率不变的架构。

### 3. 主要结论是什么？

FNO 在 Burgers、Darcy、NS 三个基准上达到 SOTA；训练后单次推理比传统求解器快 1–3 个数量级；对不同分辨率网格具有结构上的泛化能力（zero-shot 超分/降采样），但实际仍依赖训练分布覆盖与模态截断，为学习 PDE 解算子提供了高效谱域参数化范式。

---


## 价值评估

Doctor 指定精读（跳过 Codex 价值评估）。按 6 级标准看，本文 idea 清晰度为高：把神经算子的核积分层约束为卷积，并直接在 Fourier 空间学习有限个谱模态，核心机制非常干净。计算结果强：Burgers、Darcy、Navier-Stokes 三类基准均优于当时 CNN/GNO/低秩算子方法，并展示 zero-shot super-resolution。预言能力中高：它学习的是参数化 PDE 的解算子 $G^\dagger:a\mapsto u$（正文中 $G_\theta$ 表示参数化近似，$G(a,\theta)$ 为显式依赖写法，三者为同一对象的三种记法），对同一方程族的新参数实例可快速推理，但仍依赖训练分布覆盖。方法新颖性高，来源为 ICLR 2021/arXiv 2010.08895，已成为 Neural Operator 方向的基础论文；精读判断：必须精读，尤其应关注其谱截断、分辨率不变性与 GPU FFT 代价模型。

## 公式与代码梳理

### 数学结构与核心公式

论文的起点是算子学习，而不是单个 PDE 实例求解。设 $D\subset\mathbb{R}^{d}$，输入函数空间与输出函数空间分别为

$$
\mathcal{A}=\mathcal{A}(D;\mathbb{R}^{d_a}),\qquad
\mathcal{U}=\mathcal{U}(D;\mathbb{R}^{d_u}),
$$

真实 PDE 解算子为

$$
G^\dagger:\mathcal{A}\to\mathcal{U}.
$$

训练数据为 $\{a_j,u_j\}_{j=1}^{N}$，其中 $a_j\sim\mu$，$u_j=G^\dagger(a_j)$。目标是学习参数化算子

$$
G:\mathcal{A}\times\Theta\to\mathcal{U},\qquad
G_\theta:\mathcal{A}\to\mathcal{U},
$$

并最小化

$$
\min_{\theta\in\Theta}
\mathbb{E}_{a\sim\mu}
\left[
C(G(a,\theta),G^\dagger(a))
\right].
$$

这里的核心记号约定是：$a$ 是 PDE 参数、系数、初值或外力等函数输入，$u$ 是解函数；$v_t$ 是隐藏通道函数，不是物理时间。FNO 的网络结构为 lifting、若干 Fourier layer、projection：

$$
v_0(x)=P(a(x)),\qquad
u(x)=Q(v_T(x)).
$$

一般神经算子层写成

$$
v_{t+1}(x)
=
\sigma\left(
Wv_t(x)+(\mathcal{K}(a;\phi)v_t)(x)
\right),
\qquad x\in D,
$$

其中 $W:\mathbb{R}^{d_v}\to\mathbb{R}^{d_v}$ 是局部线性变换，$\sigma$ 是逐点非线性，$\mathcal{K}$ 是非局部核积分算子。一般核积分形式为

$$
(\mathcal{K}(a;\phi)v_t)(x)
=
\int_D
\kappa(x,y,a(x),a(y);\phi)v_t(y)\,\mathrm{d}y.
$$

FNO 的关键限制是去掉显式 $a(x),a(y)$ 依赖，并令核只依赖位移：

$$
\kappa(x,y,a(x),a(y);\phi)=\kappa_\phi(x-y).
$$

于是核积分变成卷积。由卷积定理，

$$
(\mathcal{K}(\phi)v_t)(x)
=
\mathcal{F}^{-1}
\left(
\mathcal{F}(\kappa_\phi)\cdot\mathcal{F}(v_t)
\right)(x).
$$

论文进一步直接参数化 Fourier 空间中的核：

$$
(\mathcal{K}(\phi)v_t)(x)
=
\mathcal{F}^{-1}
\left(
R_\phi\cdot(\mathcal{F}v_t)
\right)(x),
$$

其中对每个 Fourier mode $k$，

$$
(\mathcal{F}v_t)(k)\in\mathbb{C}^{d_v},\qquad
R_\phi(k)\in\mathbb{C}^{d_v\times d_v}.
$$

实际实现只保留低频集合 $Z_{k_{\max}}$。若 $v_t\in\mathbb{R}^{n\times d_v}$，则

$$
\mathcal{F}(v_t)\in\mathbb{C}^{n\times d_v},
$$

截断后只对 $k\in Z_{k_{\max}}$ 施加复数权重矩阵：

$$
\left(R\cdot(\mathcal{F}v_t)\right)_{k,l}
=
\sum_{j=1}^{d_v}
R_{k,l,j}(\mathcal{F}v_t)_{k,j}.
$$

在均匀网格 $s_1\times\cdots\times s_d=n$ 上，用 FFT 近似 Fourier 变换：

$$
(\hat{\mathcal{F}}f)_l(k)
=
\sum_{x_1=0}^{s_1-1}\cdots\sum_{x_d=0}^{s_d-1}
f_l(x_1,\ldots,x_d)
\exp\left(
-2\pi i\sum_{j=1}^{d}\frac{x_jk_j}{s_j}
\right).
$$

逆变换为

$$
(\hat{\mathcal{F}}^{-1}f)_l(x)
=
\frac{1}{n}
\sum_{k_1=0}^{s_1-1}\cdots\sum_{k_d=0}^{s_d-1}
f_l(k_1,\ldots,k_d)
\exp\left(
2\pi i\sum_{j=1}^{d}\frac{x_jk_j}{s_j}
\right).
$$

截断模态集合在实现中常取 Fourier 张量的低频角块：

$$
Z_{k_{\max}}
=
\left\{
(k_1,\ldots,k_d):
\min\{k_j,s_j-k_j\}\leq k_{\max,j}
\ \text{for every }j=1,\ldots,d
\right\}.
$$

因此一个 Fourier layer 的代码结构可写为：

```text
v_hat = FFT(v)
out_hat = zeros_like(v_hat)
out_hat[low_modes] = complex_matmul(R, v_hat[low_modes])
k_v = IFFT(out_hat)
v_next = activation(W(v) + k_v)
```

FNO 的 resolution invariance 来自两个事实。第一，学习参数 $R(k)$ 定义在连续 Fourier 基函数 $e^{2\pi i\langle x,k\rangle}$ 的有限低频集合上，而不是定义在某个固定网格索引空间上。第二，更换物理分辨率只改变函数在物理空间的采样与 FFT 的离散实现；当训练和测试使用相同的定义域、边界表示与 Fourier 参数化，且保留低频在两种网格上均被充分解析时，同一组 $R(k)$ 可作用于不同 $s_1,\ldots,s_d$ 的网格。这是条件性的跨分辨率迁移，不消除离散化/求积、aliasing、谱截断、边界表示或未解析高频带来的误差；除 operator approximation error 与训练分布误差外，这些误差也需单独评估。

### 关键推导

第一步是从一般核积分到卷积。一般神经算子用 $\kappa(x,y,a(x),a(y))$ 表示任意非局部相互作用，表达力强但代价接近稠密积分。FNO 令核平移不变：

$$
\kappa(x,y)=\kappa(x-y),
$$

于是

$$
(\mathcal{K}v)(x)
=
\int_D\kappa(x-y)v(y)\,\mathrm{d}y
=
(\kappa*v)(x).
$$

这一步牺牲了显式位置依赖，但换来了谱域对角化。

第二步是用 Fourier 乘法替代物理空间积分：

$$
\mathcal{F}(\kappa*v)(k)
=
\mathcal{F}(\kappa)(k)\mathcal{F}(v)(k).
$$

对多通道场，标量乘法变成每个频率上的通道混合矩阵 $R(k)$。这解释了为什么 FNO 同时具有全局感受野与相对低的复杂度：非局部传播由 FFT 完成，通道耦合由小矩阵乘完成。

第三步是谱截断。设保留 $k_{\max}$ 个模态，谱乘法成本近似为 $O(k_{\max}d_v^2)$，FFT 成本为 $O(n\log n)$。因为 $k_{\max}\ll n$，主要成本在 FFT；这与普通卷积的局部 stencil 计算不同，也与稠密 kernel operator 的 $O(n^2)$ 不同。对高维 PDE，性能瓶颈会转向 FFT 通信、内存布局与复数矩阵乘的吞吐。

### 对 HPC 框架的启示

FNO 对 Doctor 的 HPC 框架最直接的启示是：Neural Operator 可以被实现为一类谱方法 kernel，而不是普通深度学习模块。核心算子是 batched FFT、低频复数矩阵乘、inverse FFT、逐点 MLP/激活；在 GPU 上应把数据布局设计为有利于 channel-last 或 mode-major 的 batched complex GEMM，并明确 FFT 的 roofline 位置。FFT 通常不是纯 compute-bound，跨 GPU 3D FFT 还涉及 all-to-all 通信，因此 FNO 在单卡上漂亮的 $O(n\log n)$ 不等于分布式强扩展自然成立。

与 Roofline/ECM 结合时，可以把一层 Fourier layer 拆成三类 kernel：FFT memory/communication dominated，谱权重乘法 compute dominated，逐点 $1\times1$ 线性层 bandwidth 或 tensor-core dominated。若框架已有 matrix-free 求解器，FNO 可作为 learned preconditioner、coarse propagator 或 surrogate operator 插入，而不是替代所有数值求解。对 AMR 而言，标准 FNO 依赖均匀 FFT 网格，直接处理局部细化并不自然；更可行的接口是 block-structured uniform patches、multilevel spectral blocks，或与 GNO/GINO 结合处理不规则区域。

仓库已有 `neural-operator-graph-kernel-network.md` 可与 FNO 对比：GNO 保留几何图上的局部积分核，FNO 则把核压到全局 Fourier 模态。`resolution-invariant-deep-operator-network-for-pdes-with-complex-geometries.md` 可作为复杂几何路线的对照。`physics-informed-neural-networks-a-deep-learning-framework-for-solving-forward-a.md` 则代表单实例函数拟合路线，正好解释 FNO 为什么强调一次训练、多参数推理。

### 待深入研究

1. 如何把 FNO 的谱截断与 AMR 的局部高频结构结合？是否应在 coarse global Fourier basis 之外加入局部 wavelet、patch FFT 或 mortar 接口？
2. FNO 对 Hamiltonian/Lie-Poisson 系统没有内置辛结构或 Casimir 守恒；能否构造谱域的 structure-preserving neural operator，使 learned operator 保持能量、动量或不可压约束？
3. 对三维湍流和量子涡，低频截断能否保留拓扑事件、涡线重联和相位奇点？若不能，输入/输出变量应从速度场改为涡量、Clebsch 变量、密度-相位还是复波函数 $\psi$？

## Review Questions

1. FNO 的平移不变卷积核假设与复杂边界、非均匀介质、AMR patch 接口之间的冲突在哪里？如何设计一个既保留 FFT 高吞吐又能处理几何局部性的混合算子？
2. 若把 FNO 用作 Hamiltonian PDE 的时间推进器，它学习的 $G^\dagger$ 应是一步流映射、有限时间 flow map，还是 Poisson tensor 与 Hamiltonian 的分解？不同选择对长期守恒误差有什么影响？
3. 从 Roofline 角度看，FNO 的真实性能瓶颈是 FFT、复数低模态乘法还是逐点通道混合？在多 GPU 3D 问题中，$O(n\log n)$ 的算法复杂度是否仍是正确的工程指标？
