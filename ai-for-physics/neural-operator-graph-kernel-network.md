# Neural Operator: Graph Kernel Network

**Source PDF:** `2003.03485v1.pdf`

**阅读状态：** 🔬 精读
**流程状态：** ①元数据 ✓ | ②初稿 ✓ | ③评估 ✓(精读) | ④补充 ✓ | ⑤索引 ✓ | ⑥review ✓ | ⑦提交 ⏳

---

## 摘要

### 中文翻译

本文提出图核网络（GKN）：把神经算子从有限维网格映射推广到函数空间映射 G†:a↦u，用可离散化的核积分算子参数化（图消息传递实现），获得离散化不变性（resolution invariance）与跨网格泛化能力。

## 价值评估

Doctor 指定精读。GKN 将有限维网格映射提升为函数空间算子近似，并以可离散化的核积分层处理不规则点集。所谓分辨率泛化依赖于坐标、测度权重与边界编码在训练和测试间表示同一连续问题；它不是无条件的跨网格保证。

## 公式与代码梳理

### 数学结构与核心公式

论文的基本对象是参数化 PDE 的解算子，而不是单个离散网格上的函数拟合。设有紧区域 $D\subset \mathbb{R}^d$，输入函数 $a\in \mathcal{A}$ 描述系数、初值、源项或几何参数，输出函数 $u\in \mathcal{U}$ 是 PDE 解。真实目标写作

$$
G^\dagger:\mathcal{A}\to\mathcal{U},\qquad u=G^\dagger(a).
$$

GKN 的关键不是学习某个固定维度向量映射 $\mathbb{R}^n\to\mathbb{R}^n$，而是学习一个可以在不同离散点集上评估的参数化算子 $G_\theta$。这也是它和普通 CNN/MLP 的分界：CNN 的卷积核绑定规则网格，GKN 的核函数 $\kappa_\phi$ 直接接受坐标与函数值，因此天然适合图离散。

连续层写成提升、核积分迭代、投影三步。首先把低维物理输入提升到通道空间：

$$
v_0(x)=P_\theta(a(x),x),\qquad v_0:D\to\mathbb{R}^{d_v}.
$$

其中 $P_\theta$ 通常是点态 MLP，输入可包含 $a(x)$、坐标 $x$、边界标记或局部几何特征。第 $t$ 层神经算子采用

$$
v_{t+1}(x)=\sigma\left(
W v_t(x)+
\int_D \kappa_\phi(x,y,a(x),a(y))v_t(y)\,dy
+b(x)
\right).
$$

这里 $W$ 是点态线性变换，负责 channel mixing；$\kappa_\phi$ 是可学习核，负责非局部传播；$\sigma$ 是非线性激活。若 PDE 的解有 Green 函数表示

$$
u(x)=\int_D G_a(x,y)f(y)\,dy,
$$

则 GKN 可理解为用神经核 $\kappa_\phi$ 近似参数依赖 Green kernel，并通过多层组合表达非线性或复杂边界效应。

离散化时，点集 $\{x_i\}_{i=1}^n$ 形成图 $\mathcal{G}=(V,E)$，节点特征为 $v_i^t=v_t(x_i)$。核积分被图消息传递近似：

$$
v_i^{t+1}=\sigma\left(
Wv_i^t+
\frac{1}{|\mathcal{N}(i)|}
\sum_{j\in \mathcal{N}(i)}
\kappa_\phi(x_i,x_j,a_i,a_j)v_j^t
+b_i
\right).
$$

也可写作边消息

$$
m_{ij}^t=\kappa_\phi(e_{ij})v_j^t,\qquad
e_{ij}=(x_i,x_j,a_i,a_j,x_i-x_j),
$$

再聚合

$$
m_i^t=\operatorname{Agg}_{j\in\mathcal{N}(i)}m_{ij}^t,\qquad
v_i^{t+1}=\sigma(Wv_i^t+m_i^t).
$$

最后输出由点态投影给出：

$$
u_\theta(x_i)=Q_\theta(v_i^T).
$$

从代码角度看，GKN 的核心 kernel 是三类算子：`lift`、`message_passing`、`project`。其中 `message_passing` 是最重部分，复杂度约为 $O(|E|d_v^2)$ 或 $O(|E|d_vd_k)$，取决于 $\kappa_\phi$ 输出矩阵还是低秩向量权重。若图为全连接，则 $|E|=O(n^2)$；若采用半径图或 kNN，则 $|E|=O(kn)$。这直接决定 GPU 上是 memory-bound gather/scatter，还是 dense small-matmul dominated。

### 关键推导

第一步是从 PDE 解映射到算子学习。传统监督学习把网格解看成

$$
\mathbf{u}=G_h(\mathbf{a}),\qquad \mathbf{a},\mathbf{u}\in\mathbb{R}^n,
$$

但这会把训练分辨率 $h$ 固化进模型。GKN 改成先定义连续算子层，再在任意点集上求积：

$$
\int_D \kappa(x,y)v(y)\,dy
\approx
\sum_{j=1}^n w_j\kappa(x_i,x_j)v_j.
$$

若点云近似均匀，$w_j$ 可吸收到归一化因子；若是 AMR 或非均匀网格，$w_j$ 应显式使用 cell volume、quadrature weight 或 control-volume area。

第二步是把核积分解释为图消息传递。对每个目标节点 $i$，邻域 $\mathcal{N}(i)$ 取代全域积分，边特征编码空间相对关系和局部系数：

$$
K_\phi v_i
=
\sum_{j\in\mathcal{N}(i)}
\kappa_\phi(x_i,x_j,a_i,a_j)v_j.
$$

这一步提供了离散化不变性的来源：参数 $\phi$ 与节点数 $n$ 无关，只要输入坐标和权重表达同一个物理域，模型可在不同图上复用。

第三步是多层组合产生非线性算子。单层核积分近似线性 Green operator，多层结构

$$
G_\theta=Q_\theta\circ \mathcal{L}_{T-1}\circ\cdots\circ\mathcal{L}_0\circ P_\theta
$$

通过激活函数表达非线性 PDE、参数依赖边界、非局部耦合和多尺度效应。这里 $\mathcal{L}_t$ 表示第 $t$ 个核积分更新层。

### 对 HPC 框架的启示

GKN 对 Doctor 的框架启示主要在 mesh abstraction。它要求框架把 field、coordinate、connectivity、cell volume、boundary tag 作为一等数据，而不是只暴露 dense tensor。这与仓库中 FNO 文档形成互补：FNO 适合周期或规则网格上的 FFT 加速，GKN 更适合 AMR、非结构网格和复杂几何。

第二个结合点是 matrix-free operator interface。GKN 的消息传递可以看成一个可学习 sparse matrix-free stencil：

$$
(K_\phi v)_i=\sum_{j\in\mathcal{N}(i)}K_{ij}(\theta,a,x)v_j.
$$

这和 JFNK、matrix-free GPU solver 的算子调用模式一致，可把 learned preconditioner、learned flux correction 或 learned closure 写成同一类 `apply(y, x)` 接口。

第三个结合点是 AMR。若在多层 patch 上使用 GKN，必须处理 coarse-fine interface 的求积权重、ghost cell、mask 和 prolongation/restriction。相比直接把 AMR 数据 padding 成图像，GKN 更自然，但 GPU 性能会受不规则访存制约，需要 edge sorting、cell-local batching 和 fused message kernels。

### 待深入研究

1. 如何把 GKN 的核积分权重从经验归一化提升为真正的有限体积/有限元 quadrature，使变分辨率推理保持守恒？
2. 对理想流体、MHD、GPE 等 Hamiltonian PDE，能否让 $\kappa_\phi$ 同时满足反对称、能量交换局部守恒或 Poisson 结构？
3. GKN 与 FNO 的混合结构是否能在 AMR 中实现：patch 内 FFT，patch 间图消息传递？

## Review Questions

1. 如果把 GKN 的消息传递层解释为可学习 Green operator，它和传统 multigrid coarse-grid correction 或 Schur complement 近似有什么结构相似性？
2. 在 AMR 框架中，图核网络的边权应由几何邻接决定，还是由物理传播速度、特征线和局部 CFL 条件决定？
3. 对 Hamiltonian ideal fluid，GKN 若直接学习 $u^{n+1}=G_\theta(u^n)$，怎样避免长期 rollout 中能量、环量和 Casimir 漂移？
