# 图神经网络：方法与应用的综述

# Graph Neural Networks: A Review of Methods and Applications

**作者：** Jie Zhou, Ganqu Cui, Shengding Hu, Zhengyan Zhang, Cheng Yang, Zhiyuan Liu, Lifeng Wang, Changcheng Li, Maosong Sun
**期刊：** AI Open 1: 57-81, 2020（2021-01-28 在线见刊；arXiv 预印本 2018-12）
**DOI：** [https://doi.org/10.1016/j.aiopen.2021.01.001](https://doi.org/10.1016/j.aiopen.2021.01.001)（CC-BY 4.0 开放获取）
**arXiv：** [https://arxiv.org/abs/1812.08434](https://arxiv.org/abs/1812.08434)（v6, 2021-10-06；标注 "Published at AI Open 2021"）
**阅读状态：** 🔬 精读（Doctor 指定）
**流程状态：** ①元数据 ✓ | ②初稿 ✓ | ③评估 ✓(精读) | ④补充 ✓ | ⑤索引 ✓ | ⑥review ✓ | ⑦提交 ⏳

---

## 摘要

### 中文翻译
大量学习任务需要处理含有元素间丰富关系信息的图数据：物理系统建模、分子指纹学习、蛋白质界面预测、疾病分类等都要求模型从图输入学习；在文本、图像等非结构化数据上，对抽取出的结构（句子的依存树、图像的场景图）进行推理也是重要研究课题，同样需要图推理模型。图神经网络（GNN）是通过节点间消息传递捕获图依赖关系的神经模型。近年来，GCN（图卷积网络）、GAT（图注意力网络）、GRN（图循环网络）等 GNN 变体在众多深度学习任务上取得了突破性性能。本综述提出 GNN 模型的通用设计流水线，讨论每个组件的变体，系统分类其应用，并提出四个未来研究的开放问题。

### 原文
> Lots of learning tasks require dealing with graph data which contains rich relation information among elements. Modeling physics systems, learning molecular fingerprints, predicting protein interface, and classifying diseases demand a model to learn from graph inputs. ... Graph neural networks (GNNs) are neural models that capture the dependence of graphs via message passing between the nodes of graphs. In recent years, variants of GNNs such as graph convolutional network (GCN), graph attention network (GAT), graph recurrent network (GRN) have demonstrated ground-breaking performances on many deep learning tasks. In this survey, we propose a general design pipeline for GNN models and discuss the variants of each component, systematically categorize the applications, and propose four open problems for future research.

---

## 文章总结

### 1. 解决什么问题？
GNN 文献爆炸式增长但缺乏系统梳理。本文要回答：GNN 模型的通用设计框架是什么？各组件（聚合、更新、读出、训练）有哪些变体？GNN 在哪些应用领域有效、如何分类？未来有哪些开放问题？

### 2. 用了什么方法论？
- 提出 GNN 统一设计流水线：**传播模块**（消息传递 + 节点更新，含卷积/循环/注意力等变体）→ **采样模块**（节点/层/子图采样）→ **池化模块**（读出/图池化）。
- 按传播方式分类：recurrent GNN（图循环，不动点迭代）、convolutional GNN（谱域 GCN/ChebNet + 空间域 GraphSAGE/GAT 等）、graph autoencoders（图嵌入/生成）、spatio-temporal GNN（时空图，交通/动力学预测）。
- 系统化应用分类：结点级/边级/图级任务；物理系统建模、化学分子、知识图谱、推荐、交通、视觉推理等。
- 理论方面：回顾 GNN 的表达力、与 Weisfeiler-Lehman 测试的关系、过平滑（over-smoothing）等局限。

### 3. 主要结论是什么？
GNN 以"消息传递 + 聚合"为核心，可用统一流水线组织其设计空间；谱域与空间域卷积在特定正则化下等价；GNN 已覆盖从物理系统建模到推荐系统的广泛应用，但存在表达力上限（WL 测试）、过平滑、异质图、动态图、可扩展性等开放问题——这些正是后来 Graph Transformers、等变 GNN、物理网格学习（MeshGraphNet 类）发展的动机。

---

## 价值评估

Doctor 指定精读（跳过 Codex 价值评估）。

## 公式与代码梳理

（本小节由 Codex 精读补充，2026-08-04）

### 1. GNN 分类体系与核心公式

Zhou et al. 的主线是把 GNN 归纳为统一流水线：**传播模块（propagation）→ 采样模块（sampling）→ 池化/读出模块（pooling/readout）**。传播模块负责局部消息传递和节点状态更新；采样模块解决大图中的 neighbor explosion；池化模块把节点级表示压缩成子图/图级表示。一般可写成：

\[
m_v^{(t+1)}=\sum_{u\in \mathcal N(v)}M_t(h_v^{(t)},h_u^{(t)},e_{vu}),
\qquad
h_v^{(t+1)}=U_t(h_v^{(t)},m_v^{(t+1)})
\]

图级任务再用置换不变读出：

\[
\hat y=R(\{h_v^{(T)}\mid v\in G\})
\]

其中 $M$ 是 message function，$U$ 是 update function，$R$ 是 readout。采样可在节点、层、子图三个层面进行：GraphSAGE 固定采样邻居，FastGCN/LADIES 做 layer-wise sampling，ClusterGCN/GraphSAINT 做 subgraph sampling。池化则分为直接池化（sum/mean/max/attention/Set2Set/SortPooling）与层次池化（graph coarsening、DiffPool 等）：

\[
S^{(t)}=\operatorname{softmax}(\operatorname{GNN}^{(t)}_{\text{pool}}(A^{(t)},H^{(t)})),
\qquad
A^{(t+1)}=(S^{(t)})^\top A^{(t)}S^{(t)}
\]

**Recurrent GNN** 是早期 GNN 的原型。每个节点状态由自身特征、边特征、邻居状态和邻居特征共同决定：

\[
h_v=f(x_v,x_{\operatorname{co}[v]},h_{\mathcal N(v)},x_{\mathcal N(v)}),
\qquad
o_v=g(h_v,x_v)
\]

堆叠全图节点状态后：

\[
H=F(H,X),\qquad O=G(H,X_N)
\]

原始 GNN 假设 $F$ 是 contraction map，因此 $H$ 是唯一不动点，可用迭代求解：

\[
H^{(t+1)}=F(H^{(t)},X)
\]

更局部地看，也可写成：

\[
h_v^{(t+1)}=\sum_{u\in\mathcal N(v)} f(h_u^{(t)},x_u,x_v,x_{v,u})
\]

当 $t\to\infty$ 时收敛到 $H^\star=F(H^\star,X)$。这与 Deep Equilibrium Model 的思想直接相通：显式展开许多传播步等价于求一个隐式层平衡点。Almeida-Pineda 隐式微分的核心是：若

\[
g_\theta(H,X)=F_\theta(H,X)-H=0
\]

则对参数 $\theta$ 有：

\[
\frac{dH^\star}{d\theta}
=
-\left(\frac{\partial g_\theta}{\partial H}\right)^{-1}
\frac{\partial g_\theta}{\partial \theta}
=
\left(I-\frac{\partial F_\theta}{\partial H}\right)^{-1}
\frac{\partial F_\theta}{\partial \theta}
\]

反向传播不必保存所有迭代轨迹，而是解一个线性系统。这正是库内 `ai-model/deep-equilibrium-models.md` 中 DEQ 的“前向求根、反向隐式微分”范式。

**谱域 Convolutional GNN** 从 graph signal processing 出发。给定邻接矩阵 $A$、度矩阵 $D$，归一化图拉普拉斯为：

\[
L=I-D^{-1/2}AD^{-1/2}
\]

由于 $L$ 是实对称半正定矩阵，可特征分解：

\[
L=U\Lambda U^\top
\]

图 Fourier 变换与逆变换为：

\[
\mathcal F(x)=U^\top x,
\qquad
\mathcal F^{-1}(x)=Ux
\]

谱卷积定义为：

\[
g_\theta * x
=
U g_\theta(\Lambda) U^\top x
\]

直接学习 $g_\theta(\Lambda)$ 代价高且不局部。ChebNet 用 Chebyshev 多项式近似滤波器：

\[
g_\theta * x
\approx
\sum_{k=0}^{K}\theta_k T_k(\tilde L)x,
\qquad
\tilde L=\frac{2}{\lambda_{\max}}L-I
\]

其中

\[
T_k(x)=2xT_{k-1}(x)-T_{k-2}(x),
\qquad
T_0(x)=1,\quad T_1(x)=x
\]

$K$ 阶多项式意味着 $K$-hop localized convolution，避免显式特征分解。

GCN 是 ChebNet 的一阶近似。令 $K=1$、$\lambda_{\max}\approx 2$，并施加参数约束，可得：

\[
g_\theta * x
\approx
\theta\left(I+D^{-1/2}AD^{-1/2}\right)x
\]

Kipf-Welling 的 renormalization trick 加入自环：

\[
\tilde A=A+I,
\qquad
\tilde D_{ii}=\sum_j \tilde A_{ij}
\]

最终层更新为：

\[
H^{(l+1)}
=
\sigma\left(
\tilde D^{-1/2}\tilde A\tilde D^{-1/2}
H^{(l)}W^{(l)}
\right)
\]

这个公式也可被解释为空间域的一阶邻居平均：谱滤波的低通性质对应 Laplacian smoothing。

**空间域 Convolutional GNN** 直接在邻域上定义聚合。GraphSAGE 的核心是“采样邻居 + 聚合 + concat + 归一化”：

\[
h_{\mathcal N(v)}^{(t+1)}
=
\operatorname{AGG}^{(t+1)}(\{h_u^{(t)}:u\in\mathcal N(v)\})
\]

\[
h_v^{(t+1)}
=
\sigma\left(W^{(t+1)}[h_v^{(t)}\Vert h_{\mathcal N(v)}^{(t+1)}]\right)
\]

随后常做：

\[
h_v^{(t+1)}
\leftarrow
\frac{h_v^{(t+1)}}{\|h_v^{(t+1)}\|_2}
\]

GAT 则把邻居权重改为可学习注意力。对边 $(i,j)$：

\[
e_{ij}
=
\operatorname{LeakyReLU}
\left(a^\top[Wh_i\Vert Wh_j]\right)
\]

\[
\alpha_{ij}
=
\frac{\exp(e_{ij})}
{\sum_{k\in\mathcal N(i)}\exp(e_{ik})}
\]

\[
h_i'
=
\sigma\left(\sum_{j\in\mathcal N(i)}\alpha_{ij}Wh_j\right)
\]

多头注意力用 concat 或 average 稳定训练：

\[
h_i'
=
\mathbin\Vert_{k=1}^{K}
\sigma\left(\sum_{j\in\mathcal N(i)}\alpha_{ij}^{k}W^{k}h_j\right)
\]

MPNN 把这些空间方法统一为 message passing + readout：

\[
m_v^{(t+1)}
=
\sum_{u\in\mathcal N(v)}
M_t(h_v^{(t)},h_u^{(t)},e_{vu}),
\qquad
h_v^{(t+1)}
=
U_t(h_v^{(t)},m_v^{(t+1)})
\]

\[
\hat y=R(\{h_v^{(T)}\mid v\in G\})
\]

**Graph Autoencoder** 把 GNN 作为 encoder，decoder 重构图结构或特征。GAE 的典型形式是：

\[
Z=\operatorname{GCN}(X,A),
\qquad
\hat A=\sigma(ZZ^\top)
\]

邻接矩阵重构损失可写成二元交叉熵：

\[
\mathcal L_{\text{rec}}
=
-\sum_{i,j}
\left[
A_{ij}\log \hat A_{ij}
+
(1-A_{ij})\log(1-\hat A_{ij})
\right]
\]

VGAE 进一步学习后验分布：

\[
q_\phi(Z\mid X,A)
=
\prod_i q_\phi(z_i\mid X,A)
=
\prod_i \mathcal N(z_i\mid \mu_i,\operatorname{diag}(\sigma_i^2))
\]

目标函数是 ELBO：

\[
\mathcal L
=
\mathbb E_{q_\phi(Z\mid X,A)}[\log p_\theta(A\mid Z)]
-
\operatorname{KL}(q_\phi(Z\mid X,A)\Vert p(Z))
\]

**Spatio-temporal GNN** 处理随时间变化的图信号。可写成：

\[
G_t=(V_t,E_t,A_t,X_t),
\qquad
X_t\in\mathbb R^{|V_t|\times F}
\]

STGCN 类模型通常组合图卷积与时间卷积：

\[
H_t^{(l+1)}
=
\operatorname{TCN}
\left(
\sigma(\operatorname{GCN}(A,H_t^{(l)}))
\right)
\]

DCRNN 则把扩散图卷积放入循环单元，用有向随机游走矩阵刻画交通网络传播；ST-GCN/Structural-RNN 则显式加入时间边，把静态图扩展为时空图，在空间边和时间边上同时传递消息。

理论限制方面，消息传递 GNN 的表达力不超过 1-WL。若两个节点在 Weisfeiler-Lehman color refinement 中不可区分，标准 MPNN 往往也难以区分：

\[
\operatorname{MPNN}\preceq 1\text{-WL}
\]

过平滑来自反复低通传播。多层 GCN 近似反复作用传播矩阵：

\[
H^{(K)}
\approx
\left(\tilde D^{-1/2}\tilde A\tilde D^{-1/2}\right)^K XW
\]

当 $K$ 增大，节点表示趋向图拉普拉斯低频子空间，同一连通分量内表示变得相似，节点区分性下降。异质图需要关系类型特定参数，动态图需要随时间更新 $A_t,E_t,V_t$，大规模图还受采样方差、邻居爆炸、分布式训练和内存带宽限制。

### 2. 算法流程：把 GNN 用于物理网格学习

> 注：本节的建图、前向与训练流程是笔记作者基于 MeshGraphNet 类工作（库内尚无该文）面向 AMReX 场景的**方法扩展**，不是 Zhou et al. 综述的原文内容；综述原文只到分类体系与基础公式为止。

把不规则物理网格输入 GNN，可按以下流程理解：

1. **不规则网格 → 图构建。** 节点可取网格单元 cell、顶点 vertex、面 face 或粒子；边可取面邻接、拓扑连接、半径邻域、接触关系或边界耦合。节点特征包括坐标、体积、面积、法向、材料参数、速度、压力、密度、温度、守恒量等；边特征包括相对位移、距离、面面积、法向、通量方向、粗细层关系等：

\[
x_i=[q_i,\Delta x_i,V_i,b_i,\text{material}_i],
\qquad
e_{ij}=[x_j-x_i,\|x_j-x_i\|,n_{ij},S_{ij},\text{type}_{ij}]
\]

2. **GNN 前向。** 典型 MeshGraphNet 使用 encoder-processor-decoder：先把物理/几何特征编码到 latent space，再运行多步 message passing，最后解码出下一步增量或物理量：

\[
h_i^0=\phi_{\text{enc}}^v(x_i),
\qquad
g_{ij}^0=\phi_{\text{enc}}^e(e_{ij})
\]

\[
m_{ij}^{k}=\phi_e(h_i^k,h_j^k,g_{ij}^k),
\qquad
\bar m_i^k=\sum_{j\in\mathcal N(i)}m_{ij}^{k}
\]

\[
h_i^{k+1}=\phi_v(h_i^k,\bar m_i^k),
\qquad
\hat q_i^{t+1}=q_i^t+\phi_{\text{dec}}(h_i^K)
\]

它在 Zhou et al. 的分类体系中属于**空间域 message passing GNN**，带有图网络 GN/MPNN 风格的 encoder-processor-decoder 结构，而不是谱域 GCN。

3. **训练目标。** 监督项可预测下一步物理量或时间导数：

\[
\mathcal L_{\text{sup}}
=
\sum_i
\|\hat q_i^{t+1}-q_i^{t+1}\|_2^2
\]

结构保持可加入守恒/约束损失：

\[
\mathcal L
=
\mathcal L_{\text{sup}}
+
\lambda_c\|\sum_i V_i\hat q_i-\sum_i V_i q_i\|^2
+
\lambda_b\mathcal L_{\text{bc}}
+
\lambda_r\mathcal L_{\text{residual}}
\]

其中 residual 可来自离散 PDE、通量平衡或边界条件。

对 AMR 网格，Berger-Colella/AMReX 的层次结构可自然映射成多关系图：同层 cell 用面邻接边连接；粗细层之间加入 prolongation/restriction 边；ghost cell、embedded boundary、particle-mesh coupling 可作为特殊边或特殊节点类型。动态细化时，图结构随 regridding 更新：

\[
G_t=(V_t,E_t,X_t)
\quad\to\quad
G_{t+\Delta t}=(V_{t+\Delta t},E_{t+\Delta t},X_{t+\Delta t})
\]

关键工程问题是保持物理场从旧图到新图的 conservative transfer，并更新 edge features 中的层级、尺度、面积/体积权重。等变和几何先验可嵌入消息函数：例如让 $M$ 依赖相对坐标、距离、法向和张量特征；在三维场中用 SE(3)-equivariant message passing 保证旋转/平移下速度、力、通量等向量量按正确表示变换：

\[
M_{ij}=M(h_i,h_j,\|r_{ij}\|,\hat r_{ij},e_{ij})
\]

这与 Geometric DL 的“域对称性决定网络结构”一致。

### 3. 与库内相关论文的关联

- `ai-for-physics/learning-mesh-based-simulation-with-graph-networks.md`：库内尚无，建议补。这篇 MeshGraphNets 应作为本综述在物理网格学习方向的直接后继：它把 MPNN/GN 框架落到可变拓扑 mesh simulation。
- `ai-theory/geometric-deep-learning-grids-groups-graphs-geodesics-and-gauges.md`：提供更高层的 5G 纲领。GNN 是图置换群下的等变网络；物理网格上若加入欧氏群或 SE(3) 对称性，就从普通 MPNN 走向 geometric/equivariant GNN。
- `ai-for-physics/neural-operator-graph-kernel-network.md`：Graph Kernel Network 把图上的迭代核积分/消息传递用于 PDE 解算子学习，是 GNN 与 neural operator 的交叉点；它强调 mesh/discretization independence，比节点标签预测更接近 Doctor 的物理主线。
- `ai-theory/neural-tangent-kernel-convergence-and-generalization-in-neural-networks.md`：谱滤波、图核、NTK 可共同解释 GNN 训练动力学、低频偏置和过平滑。GNN 的传播矩阵谱结构会进入有效核，影响收敛速度与泛化。
- `ai-model/deep-equilibrium-models.md`：原始 recurrent GNN 的不动点传播是 DEQ 的早期图结构版本；Almeida-Pineda 隐式微分与 DEQ 反向传播共享同一数学骨架。
- `HPC/amrex-block-structured-amr-for-multiphysics-applications.md`、`HPC/boxlib-with-tiling-amr-software-framework.md`：AMReX/BoxLib 的 Box、MultiFab、tiling、ghost cells、regridding、Berger-Rigoutsos 聚类提供了“物理网格如何变成图”的工程基底。GNN 图构建不应脱离这些真实数据结构。
- 总体上，Zhou et al. 这篇综述在 Doctor “物理网格学习 + 不规则 AMR 网格 + 结构保持”主线中是方法分类的地基：它定义了 message passing、sampling、pooling、autoencoding、spatio-temporal modeling 和表达力限制；后续 MeshGraphNet、Graph Kernel Network、Geometric DL、DEQ、AMReX 都可视为在这个地基上分别向物理仿真、算子学习、对称先验、隐式求解和高性能 AMR 数据结构延伸。

## Review Questions

1. 这篇笔记里把 GNN 的分类写成 recurrent / convolutional / graph autoencoder / spatio-temporal，这个分法与原文和后续主流综述相比，是否需要补一层“message passing / spectral / spatial”维度来避免概念混用？
2. 在物理网格建模那几段里，AMReX / BoxLib / MeshGraphNet 的关联是“方法对应”还是“实现启发”？是否需要把边界条件、守恒量和多尺度网格重映射的假设写得更硬一点？
3. 这篇笔记把 GCN、GraphSAGE、GAT、DEQ、NTK 串成一条演化线时，哪些部分是原文明确结论，哪些只是跨文献的解释性延伸？是否要显式标注分界？
