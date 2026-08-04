# 几何深度学习：网格、群、图、测地线与规范

# Geometric Deep Learning: Grids, Groups, Graphs, Geodesics, and Gauges

**作者：** Michael M. Bronstein, Joan Bruna, Taco Cohen, Petar Veličković
**期刊：** arXiv:2104.13478v2, 2021（综述；后发表于 IEEE TPAMI 2021, DOI 10.1109/TPAMI.2021.3072883，但笔记基于 arXiv v2 全文）
**arXiv：** [https://arxiv.org/abs/2104.13478](https://arxiv.org/abs/2104.13478)
**阅读状态：** 🔬 精读（Doctor 指定）
**流程状态：** ①元数据 ✓ | ②初稿 ✓ | ③评估 ✓(精读) | ④补充 ✓ | ⑤索引 ✓ | ⑥review ✓ | ⑦提交 ✓

---

## 摘要

### 中文翻译
过去十年见证了数据科学与机器学习的一场实验性革命，深度学习方法是其代表。深度学习本质建立在两个简单算法原理上：一是表示/特征学习（自适应的分层特征捕捉各任务的正则性），二是局部梯度下降型学习（通常以反向传播实现）。虽然在高维中学习一般函数是受诅咒的估计问题，但大多数任务并非一般函数，而是带有源于底层低维结构的先验正则性。本文用对称性（symmetry）与不变性（invariance）的几何语言统一描述这些先验——从网格、群、图、测地线到规范——为几何深度学习建立统一框架。

### 原文
> The last decade has witnessed an experimental revolution in data science and machine learning, epitomised by deep learning methods. ... the essence of deep learning is built from two simple algorithmic principles: first, the notion of representation or feature learning ... and second, learning by local gradient-descent type methods ... While learning generic functions in high dimensions is a cursed estimation problem, most tasks of interest are not generic, and come with essential pre-defined regularities arising from the underlying low-dimensional structure.

---

## 文章总结

### 1. 解决什么问题？
如何用一个统一框架解释网格、图、流形等不同数据结构的深度学习方法？

### 2. 用了什么方法论？
以对称群与不变性为核心公理（蓝图：信号在域上、群作用、等变/不变层），把 CNN（网格平移群）、GNN（图置换群）、深度几何学习（流形等距群）统一为同一设计原则的特例；覆盖群表示论、测地线距离、规范（gauge）等变。

### 3. 主要结论是什么？
几何深度学习的统一蓝图：所有结构数据学习都源于域对称群的先验；等变层由共享权重的群作用构造，不同的域（网格/图/流形/规范丛）给出不同架构族。

---

## 价值评估

Doctor 指定精读（跳过 Codex 价值评估）。

## 公式与代码梳理

**一、统一数学对象：域、信号、群作用**

论文的基本抽象是：数据不是无结构向量，而是定义在某个几何域 $\Omega$ 上的信号。若每个点 $u \in \Omega$ 上有 $C$ 值特征，则信号空间为

$$
X(\Omega, C)=\{x:\Omega \to C\}
$$

其中 $\Omega$ 可以是网格、集合、图、群、流形或纤维丛的基空间，$C$ 是通道/特征空间。若 $C$ 上有内积 $\langle \cdot,\cdot\rangle_C$，且 $\Omega$ 上有测度 $\mu$，则信号空间内积为

$$
\langle x,y\rangle
=
\int_{\Omega}\langle x(u),y(u)\rangle_C\,d\mu(u)
$$

离散图或网格上，积分退化为求和。

群 $G$ 描述域的对称性。群作用是映射

$$
(g,u)\mapsto g.u,\qquad g\in G,\ u\in \Omega
$$

满足

$$
g.(h.u)=(gh).u,\qquad e.u=u
$$

其中 $e$ 是单位元。群先作用在域 $\Omega$ 上，再诱导出对信号的作用：

$$
(g.x)(u)=x(g^{-1}u)
$$

或用表示 $\rho(g)$ 写成

$$
(\rho(g)x)(u)=x(g^{-1}u)
$$

这里必须出现 $g^{-1}$，否则信号变换无法满足群作用的结合律。直观地说：变换后的信号在位置 $u$ 的值，等于原信号在“被 $g$ 移到 $u$ 的那个旧位置”上的值。

群表示是把抽象群元素变成线性算子的映射：

$$
\rho:G\to \mathbb{R}^{n\times n},\qquad
\rho(gh)=\rho(g)\rho(h)
$$

若 $\rho(g)$ 都是正交或酉矩阵，则称为正交/酉表示。论文后面所有“输入如何变、输出如何跟着变”的条件，本质都依赖这个表示。

**二、不变性与等变性**

若任务输出不应随群作用改变，例如图分类不依赖节点编号、图像分类不依赖物体平移，则要求 $G$-不变：

$$
f(\rho(g)x)=f(x),\qquad \forall g\in G
$$

若任务输出应以同样方式变换，例如图像分割 mask 应随图像平移、节点表示应随节点重排，则要求 $G$-等变：

$$
f(\rho(g)x)=\rho'(g)f(x),\qquad \forall g\in G
$$

若输入输出在同一域、同一表示下，也常写作

$$
f(\rho(g)x)=\rho(g)f(x)
$$

不变性适合全局预测，等变性适合局部/结构化预测。论文的关键判断是：深度网络通常不直接堆叠不变层，而是先堆叠多个等变层，再用全局池化得到不变输出。原因是线性不变层表达力很弱。若 $f$ 是线性且 $G$-不变，则

$$
f(x)
=
\frac{1}{\mu(G)}
\int_G f(g.x)\,d\mu(g)
=
f\left(
\frac{1}{\mu(G)}
\int_G g.x\,d\mu(g)
\right)
$$

也就是说它只依赖群平均

$$
Ax=
\frac{1}{\mu(G)}
\int_G g.x\,d\mu(g)
$$

例如图像平移不变的线性函数只会保留全局平均颜色，无法表达复杂视觉结构。

**三、几何深度学习蓝图**

论文的统一蓝图可以写成：

$$
f
=
A\circ \sigma_J\circ B_J\circ P_{J-1}
\circ \cdots
\circ P_1\circ \sigma_1\circ B_1
$$

其中：

- $B_j:X(\Omega_j,C_j)\to X(\Omega_j',C_{j+1})$ 是局部线性 $G$-等变层；
- $\sigma_j$ 是逐点非线性，例如 ReLU；
- $P_j$ 是局部池化/粗化，把域 $\Omega_j$ 变成更粗的 $\Omega_{j+1}$；
- $A$ 是全局 $G$-不变读出层。

核心设计原则是：

$$
\text{局部性}+\text{权重共享}+\text{等变性}+\text{多尺度粗化}
\Rightarrow
\text{可学习且稳定的结构先验}
$$

局部等变层 $U$ 的局部性定义为：$(Ux)(u)$ 只依赖 $u$ 的邻域

$$
N_u=\{v:d(u,v)\le r\}
$$

多层局部等变映射的复合

$$
U_J\circ U_{J-1}\circ \cdots \circ U_1
$$

逐渐扩大感受野，同时保持等变结构；池化 $P$ 则提供尺度分离，使远程相互作用先局部处理、再向粗尺度传播。

**四、CNN：平移等变与卷积**

在一维周期网格 $\Omega=\mathbb{Z}_n$ 上，平移算子 $S$ 是循环移位。所有与 $S$ 可交换的线性算子都是循环矩阵，也就是离散卷积：

$$
(x\star \theta)_u
=
\sum_{v=0}^{n-1}
x_v\theta_{u-v \bmod n}
$$

平移等变性写作

$$
SC(\theta)x=C(\theta)Sx
$$

即先平移再卷积，等于先卷积再平移。这解释了 CNN 中“共享卷积核”的来源：权重共享不是经验技巧，而是平移等变性对线性层的结构约束。

二维单通道 CNN 的局部卷积为

$$
F(x)_{uv}
=
\sum_{a=1}^{H_f}
\sum_{b=1}^{W_f}
\alpha_{ab}x_{u+a,v+b}
$$

多通道形式为

$$
F(x)_{uvj}
=
\sum_{a=1}^{H_f}
\sum_{b=1}^{W_f}
\sum_{c=1}^{M}
\alpha_{jabc}x_{u+a,v+b,c},
\qquad j\in[N]
$$

其中 $M$ 是输入通道数，$N$ 是输出通道数，$\alpha_{jabc}$ 是共享卷积核参数。

一个标准 CNN 层可写成

$$
h=P(\sigma(F(x)))
$$

ResNet 则把层写成扰动形式：

$$
h=P(x+\sigma(F(x)))
$$

这可看作连续动力系统

$$
\dot{x}=\sigma(F(x))
$$

的前向 Euler 离散化。因此 ResNet 与 Neural ODE 在形式上共享“深度 = 时间演化”的观点。

**五、傅里叶、卷积与表示论**

离散傅里叶基是移位算子 $S$ 的特征向量：

$$
\phi_k=
\frac{1}{\sqrt n}
\left(
1,e^{2\pi i k/n},e^{4\pi i k/n},\ldots,e^{2\pi i(n-1)k/n}
\right)^\top
$$

DFT 和逆 DFT 为

$$
\hat{x}_k=
\frac{1}{\sqrt n}
\sum_{u=0}^{n-1}
x_u e^{-2\pi iku/n}
$$

$$
x_u=
\frac{1}{\sqrt n}
\sum_{k=0}^{n-1}
\hat{x}_k e^{2\pi iku/n}
$$

卷积定理：

$$
C(\theta)x
=
\Phi\,\mathrm{diag}(\hat{\theta})\,\Phi^*x
=
\Phi(\hat{\theta}\odot \hat{x})
$$

这说明卷积在傅里叶域中是逐频率乘法。更一般地，群傅里叶变换可理解为把信号投影到群的不可约表示矩阵元上。对 $SO(3)$，对应球谐函数与 Wigner $D$ 矩阵；对 $SE(3)$ 等旋转/平移群，等变网络常用不可约表示分解，把特征分成按不同表示块变换的部分。

不可约表示的直观含义是：无法再分解成更小不变子空间的基本表示块。很多 3D 等变网络把特征分解为标量、向量、高阶张量等不可约分量，再用满足 Clebsch-Gordan 规则的核进行等变映射。

**六、群卷积与齐性空间**

若群 $G$ 作用在域 $\Omega$ 上，则群卷积定义为

$$
(x\star \theta)(g)
=
\langle x,\rho(g)\theta\rangle
=
\int_\Omega x(u)\theta(g^{-1}u)\,du
$$

它的输出定义在群元素 $g\in G$ 上，而不一定还在原域 $\Omega$ 上。等变性来自：

$$
(\rho(h)x\star \theta)(g)
=
\langle \rho(h)x,\rho(g)\theta\rangle
=
\langle x,\rho(h^{-1}g)\theta\rangle
=
\rho(h)(x\star \theta)(g)
$$

若 $\Omega=G$，则群作用是左乘，信号上的作用

$$
(\rho(g)x)(h)=x(g^{-1}h)
$$

称为正则表示。

齐性空间是指任意两点可由某个群元素连接：

$$
\forall u,v\in \Omega,\ \exists g\in G,\quad g.u=v
$$

欧氏网格、平面、球面是典型例子。齐性空间上可自然“移动同一个滤波器”，因此权重共享明确；一般流形不具备全局齐性，所以需要测地线、局部坐标和规范等变来替代全局卷积。

**七、GNN：置换等变与消息传递**

对集合，节点特征堆成矩阵 $X\in\mathbb{R}^{n\times d}$，置换 $P$ 作用为行重排。置换不变函数满足

$$
f(PX)=f(X)
$$

Deep Sets 的典型形式是

$$
f(X)=\phi\left(\sum_{u\in V}\psi(x_u)\right)
$$

置换等变节点函数满足

$$
F(PX)=PF(X)
$$

最简单的共享节点变换为

$$
F_\Theta(X)=X\Theta
$$

对图 $G=(V,E)$，邻接矩阵为

$$
a_{uv}
=
\begin{cases}
1,&(u,v)\in E\\
0,&\text{otherwise}
\end{cases}
$$

置换会同步作用于特征与邻接矩阵：

$$
X\mapsto PX,\qquad A\mapsto PAP^\top
$$

图级不变与节点级等变分别为

$$
f(PX,PAP^\top)=f(X,A)
$$

$$
F(PX,PAP^\top)=PF(X,A)
$$

节点邻域定义为

$$
N_u=\{v:(u,v)\in E\ \text{or}\ (v,u)\in E\}
$$

邻域特征是多重集

$$
X_{N_u}=\{\{x_v:v\in N_u\}\}
$$

局部置换等变图层的一般形式：

$$
F(X,A)
=
\begin{bmatrix}
\phi(x_1,X_{N_1})\\
\phi(x_2,X_{N_2})\\
\vdots\\
\phi(x_n,X_{N_n})
\end{bmatrix}
$$

只要 $\phi$ 对邻域多重集置换不变，整个 $F$ 就对节点重排等变。

论文把常见 GNN 层分成三类：

卷积式 GNN：

$$
h_u=
\phi\left(
x_u,
\bigoplus_{v\in N_u}
c_{uv}\psi(x_v)
\right)
$$

注意力式 GNN：

$$
h_u=
\phi\left(
x_u,
\bigoplus_{v\in N_u}
a(x_u,x_v)\psi(x_v)
\right)
$$

消息传递式 GNN：

$$
h_u=
\phi\left(
x_u,
\bigoplus_{v\in N_u}
\psi(x_u,x_v)
\right)
$$

其中 $\bigoplus$ 是 sum/mean/max 等置换不变聚合。三者表达包含关系为：

$$
\text{convolutional GNN}
\subseteq
\text{attentional GNN}
\subseteq
\text{message-passing GNN}
$$

Transformer 可看作完整图 $A=\mathbf{1}\mathbf{1}^\top$ 上的注意力式 GNN：

$$
h_u=
\phi\left(
x_u,
\bigoplus_{v\in V}
a(x_u,x_v)\psi(x_v)
\right)
$$

注意力权重 $a(x_u,x_v)$ 相当于学习一个软邻接矩阵。位置编码则是在无序集合上额外注入序列/网格结构；图 Transformer 使用 Laplacian 特征向量作为位置编码时，本质是把图傅里叶基接入注意力架构。

**八、流形、测地线与等距不变**

流形上的信号可以是标量场

$$
x:\Omega\to \mathbb{R}
$$

也可以是向量场

$$
X:\Omega\to T\Omega,\qquad X(u)\in T_u\Omega
$$

标量场内积：

$$
\langle x,y\rangle
=
\int_\Omega x(u)y(u)\,du
$$

向量场内积：

$$
\langle X,Y\rangle
=
\int_\Omega g_u(X(u),Y(u))\,du
$$

其中 $g_u$ 是 Riemannian metric，即每个切空间 $T_u\Omega$ 上的内积。

曲线 $\gamma:[0,T]\to\Omega$ 的长度为

$$
\ell(\gamma)
=
\int_0^T
\|\gamma'(t)\|_{\gamma(t)}dt
=
\int_0^T
g_{\gamma(t)}^{1/2}(\gamma'(t),\gamma'(t))dt
$$

测地距离定义为最短曲线长度：

$$
d_g(u,v)
=
\min_\gamma \ell(\gamma)
\quad
\text{s.t.}\quad
\gamma(0)=u,\ \gamma(T)=v
$$

等距映射 $\eta:(\Omega,g)\to(\tilde{\Omega},h)$ 满足拉回度量相同：

$$
(\eta^*h)_u(X,Y)
=
h_{\eta(u)}(d\eta_u(X),d\eta_u(Y))
$$

$$
g=\eta^*h
$$

等价地，它保持测地距离：

$$
d_g(u,v)=d_h(\eta(u),\eta(v))
$$

近似等距可用 distortion 衡量：

$$
\mathrm{dis}(\eta)
=
\sup_{u,v\in\Omega}
|d_h(\eta(u),\eta(v))-d_g(u,v)|
$$

对应的稳定性条件为

$$
\|f(x,\Omega)-f(x\circ \eta^{-1},\tilde{\Omega})\|
\le
C\|x\|\mathrm{dis}(\eta)
$$

这与 PINN/物理建模中的“不变量/守恒量先验”相通：不是让网络任意拟合，而是把物理或几何结构作为函数类约束。

**九、Laplacian、谱卷积与 Neural Operator 关联**

流形上的梯度 $\nabla$ 与散度 $\nabla^*$ 满足伴随关系：

$$
\langle X,\nabla x\rangle
=
\langle \nabla^*X,x\rangle
$$

Laplace-Beltrami 算子定义为

$$
\Delta=\nabla^*\nabla
$$

Dirichlet 能量为

$$
c^2(x)
=
\|\nabla x\|^2
=
\int_\Omega
g_u(\nabla x(u),\nabla x(u))\,du
$$

Laplacian 特征分解：

$$
\Delta \phi_k=\lambda_k\phi_k,
\qquad
\langle \phi_k,\phi_l\rangle=\delta_{kl}
$$

流形 Fourier 展开：

$$
x(u)
=
\sum_{k\ge 0}
\langle x,\phi_k\rangle \phi_k(u)
$$

谱卷积定义为

$$
(x\star \theta)(u)
=
\sum_{k\ge 0}
(\hat{x}_k\hat{\theta}_k)\phi_k(u)
$$

更稳定的谱滤波写成 transfer function：

$$
(\hat{p}(\Delta)x)(u)
=
\sum_{k\ge 0}
\hat{p}(\lambda_k)\langle x,\phi_k\rangle\phi_k(u)
$$

也可写成空间核形式：

$$
(\hat{p}(\Delta)x)(u)
=
\int_\Omega
x(v)
\sum_{k\ge 0}
\hat{p}(\lambda_k)\phi_k(v)\phi_k(u)\,dv
$$

若 $\hat{p}$ 是 $r$ 阶多项式

$$
\hat{p}(\lambda)=\sum_{l=0}^r \alpha_l\lambda^l
$$

则

$$
\hat{p}(\Delta)x
=
\sum_{l=0}^r \alpha_l\Delta^l x
$$

这避免显式特征分解，也给出局部 $r$-hop 滤波。与本库 Neural Operator 相关论文的联系在这里最直接：FNO/Neural Operator 在函数空间中学习算子，常通过 Fourier 模式或核积分实现非局部映射；本文则解释了这些谱/核算子如何从域对称性、Laplacian 和几何稳定性中自然出现。对复杂几何的 operator learning，可把 $\Delta$、图 Laplacian 或 mesh Laplacian 看成几何域上的“可泛化 Fourier 基”。

**十、规范等变：局部坐标任意性**

在一般流形上，没有全局平移群，无法把一个滤波器无歧义地搬到每个点。必须选局部参考系，即 gauge：

$$
\omega_u:\mathbb{R}^s\to T_u\Omega
$$

同一个几何向量场 $X(u)$ 在 gauge $\omega_u$ 下有坐标 $x(u)$。若换 gauge

$$
\omega'_u=\omega_u\circ g_u,\qquad g:\Omega\to G
$$

则坐标必须反向变换：

$$
x'(u)=g_u^{-1}x(u)
$$

从而几何对象不变：

$$
X(u)
=
\omega'_u(x'(u))
=
\omega_u(g_ug_u^{-1}x(u))
=
\omega_u(x(u))
$$

若特征按表示 $\rho$ 变换，则 gauge transformation 对特征作用为

$$
x(u)\mapsto \rho(g_u^{-1})x(u)
$$

规范等变层要求坐标表达不依赖任意 gauge 选择：

$$
f\circ \rho_{\mathrm{in}}(g)
=
\rho_{\mathrm{out}}(g)\circ f
$$

对向量场卷积，必须先把邻居 $v$ 的向量平行移动到 $u$ 的切空间：

$$
(x\star \Theta)(u)
=
\int_\Omega
\Theta(u,v)\rho(g_{v\to u})x(v)\,dv
$$

其中 $g_{v\to u}\in G$ 表示沿测地线从 $v$ 到 $u$ 的平行运输。对非平凡表示的 mesh feature，需先 parallel transport 再卷积；滤波器须满足对逐点 gauge 场 $g(\cdot):\Omega\to G$ 的等变性，具体体现为 kernel constraints（用 basis kernels 参数化）+ transporter matrix，而不是泛称“滤波器与表示可交换”。

mesh 上的离散版本是

$$
h_u
=
\Theta_{\mathrm{self}}x_u
+
\sum_{v\in N_u}
\Theta_{\mathrm{neigh}}(\vartheta_{uv})
\rho(g_{v\to u})x_v
$$

其中 $\vartheta_{uv}$ 是邻居方向角，$\rho(g_{v\to u})$ 是 transporter matrix。约束为

$$
\Theta_{\mathrm{self}}\rho_{\mathrm{in}}(\vartheta)
=
\rho_{\mathrm{out}}(\vartheta)\Theta_{\mathrm{self}}
$$

$$
\Theta_{\mathrm{neigh}}(\vartheta_{uv}-\vartheta)\rho_{\mathrm{in}}(\vartheta)
=
\rho_{\mathrm{out}}(\vartheta)\Theta_{\mathrm{neigh}}(\vartheta_{uv})
$$

这些线性约束可通过等变核基展开实现：

$$
\Theta_{\mathrm{self}}=\sum_i \alpha_i\Theta^i_{\mathrm{self}},
\qquad
\Theta_{\mathrm{neigh}}=\sum_i \beta_i\Theta^i_{\mathrm{neigh}}
$$

**十一、算法/架构流程总结**

通用 GDL 架构流程：

1. 选定域 $\Omega$：网格、图、集合、流形、mesh、群或齐性空间。
2. 识别对称群 $G$：平移群、旋转群、置换群、等距群、gauge structure group。
3. 定义群在信号空间上的表示 $\rho(g)$。
4. 构造局部等变层 $B$：CNN 用卷积，GNN 用邻域聚合，流形用 Laplacian/测地 patch，gauge 网络用 transporter。
5. 加逐点非线性 $\sigma$，保持等变性。
6. 用 pooling/coarsening 扩大感受野并实现尺度分离。
7. 最后用全局不变读出 $A$ 做分类、回归或图级预测。

对应到代码层面，论文没有提供实现代码，但其“可编程接口”非常清晰：

- CNN：`Conv -> activation -> pooling -> global pooling`
- GNN：`message(x_u,x_v) -> permutation-invariant aggregate -> update`
- Transformer：`complete graph attention -> aggregate values -> update`
- Mesh CNN：`compute geodesic patch / Laplacian / transporter -> local filter -> aggregate`
- Gauge-equivariant CNN：`represent features by group reps -> constrain kernel basis -> parallel transport -> aggregate`

**十二、与本库其他论文的关联**

- 与 PINN/Physics-informed Neural Networks：PINN 通过 PDE residual、边界条件、守恒量约束函数空间；本文通过对称群、不变性、等变性约束函数空间。二者都是“用结构先验减少可学习函数类”。本库中的 `physics-informed-neural-networks-a-deep-learning-framework-for-solving-forward-a.md`、`nsfnets-navier-stokes-flow-nets-physics-informed-neural-networks-for-the-incompr.md`、`a-two-stage-physics-informed-neural-network-method-based-on-conserved-quantities.md` 可从本文角度理解为物理方程约束 + 几何/守恒不变量约束。
- 与 Neural Operator：本文的谱滤波 $\hat{p}(\Delta)$、核积分 $\int_\Omega \theta(u,v)x(v)dv$ 与 Neural Operator 的“函数到函数算子学习”高度相似。具体拆分：GNO/GKN 对应图结构、核积分与消息传递（`neural-operator-graph-kernel-network.md`）；复杂几何 DeepONet 对应几何编码（RBF）与分辨率不变性（`resolution-invariant-deep-operator-network-for-pdes-with-complex-geometries.md`）——不宜笼统说二者都推广了谱基。
- 与 Attention/Transformer：本文明确指出 Transformer 是完整图上的 attentional GNN，自注意力权重 $a(x_u,x_v)$ 是学习出的软邻接矩阵。`pde-transformer-efficient-and-versatile-transformers-for-physics-simulations.md` 可从 GDL 视角解释为在 complete/local token graph 上学习软边权（其实际机制是 2D 规则网格上的 shifted-window spatial attention + channel-wise axial attention，GNO 是未来扩展到非结构网格的接口），而非通用的 latent graph learning。
- 与 GNN/Message Passing：本文把 GNN 归纳为置换等变的局部消息传递。`iga-graph-net-基于图神经网络的等几何分析重用方法用于拓扑一致模型.md`、`probabilistic-graph-networks-for-learning-physics-simulations.md`、`tensor-network-message-passing.md` 与本文的公式 (33)-(35) 直接对应。
- 与物理等变网络：`roteqnet-rotation-equivariant-network-for-fluid-systems-with-symmetric-high-orde.md`、`approximately-equivariant-networks-for-imperfectly-symmetric-dynamics.md`、`physical-invariance-in-neural-networks-for-subgrid-scale-scalar-flux-modeling.md` 可视为本文 $E(3)$、旋转等变、近似等变稳定性思想在流体/物理系统中的专门实例。
## Review Questions

1. 在非结构网格、AMR 网格或 moving mesh PDE 求解器中，应如何选择图 Laplacian、mesh Laplacian、测地 patch 与 parallel transporter，使学习算子既跨分辨率稳定，又不破坏局部守恒和边界条件？
2. 将 Transformer 解释为 complete/local token graph 上的 attentional GNN 时，面对百万级网格点的 HPC PDE surrogate，应如何在全局注意力、局部 stencil attention、稀疏图消息传递和多重网格 coarsening 之间取舍？
3. 对速度、应力、磁场等向量/张量物理场，如何在离散 mesh 或有限元/有限体积基函数上实现 gauge-equivariant kernel constraint 与 parallel transport，并验证坐标系选择不会污染预测？
