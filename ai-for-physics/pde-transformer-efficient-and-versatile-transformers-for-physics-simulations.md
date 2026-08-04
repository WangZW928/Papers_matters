# PDE-Transformer：面向物理模拟的高效通用 Transformer

# PDE-Transformer: Efficient and Versatile Transformers for Physics Simulations

**作者：** Benjamin Holzschuh, Qiang Liu, Georg Kohl, Nils Thuerey
**期刊：** 出处/版本：arXiv:2505.24717v1 [cs.LG]（无 DOI）；ICML 2025, PMLR 267
**arXiv：** [https://arxiv.org/abs/2505.24717](https://arxiv.org/abs/2505.24717)
**阅读状态：** 🔬 精读（Doctor 指定）
**流程状态：** ①元数据 ✓ | ②初稿 ✓ | ③评估 ✓(精读) | ④补充 ✓ | ⑤索引 ✓ | ⑥review ✓ | ⑦提交 ✓

---

## 摘要

### 中文翻译
提出 PDE-Transformer：面向规则网格上物理模拟代理建模的改进 Transformer 架构。结合扩散 Transformer 的近期架构改进与大规模模拟的专门调整，得到更可扩展、更通用的 Transformer 架构，可作为物理科学大规模基础模型的骨干。在 16 类 PDE 的大数据集上优于 SOTA 视觉 Transformer 架构。提出将不同物理通道分别嵌入为时空 token，通过通道间自注意力交互，在多类型 PDE 联合学习时保持 token 信息密度一致。预训练模型在多个下游任务上优于从零训练，也击败其他物理模拟基础模型架构。

### 原文
> We introduce PDE-Transformer, an improved transformer-based architecture for surrogate modeling of physics simulations on regular grids. We combine recent architectural improvements of diffusion transformers with adjustments specific for large-scale simulations to yield a more scalable and versatile general-purpose transformer architecture, which can be used as the backbone for building large-scale foundation models in physical sciences. We demonstrate that our proposed architecture outperforms state-of-the-art transformer architectures for computer vision on a large dataset of 16 different types of PDEs. We propose to embed different physical channels individually as spatio-temporal tokens, which interact via channel-wise self-attention. This helps to maintain a consistent information density of tokens when learning multiple types of PDEs simultaneously.

---

## 文章总结

### 1. 解决什么问题？
如何设计一个可扩展、通用的 Transformer 骨干，作为物理模拟大规模基础模型的底座？

### 2. 用了什么方法论？
融合扩散 Transformer（DiT）的架构改进（自适应归一化、token 化时空补丁等）+ 面向大规模模拟的调整；物理通道各自嵌入为时空 token，通道间自注意力交互；在 16 类 PDE 数据集上预训练并微调下游任务。

### 3. 主要结论是什么？
PDE-Transformer 在 16 类 PDE 数据集上超越 CV 领域 SOTA Transformer；通道独立 token 化保持信息密度一致；预训练基础模型在挑战性下游任务上优于从零训练与其他物理基础模型。

---

## 价值评估

Doctor 指定精读（跳过 Codex 价值评估）。

## 公式与代码梳理

### 1. 记号与任务形式

论文把一个物理系统记为 $S$，其状态是二维规则网格上的多物理量场：

$$
u(x,t): \Omega_S \times [0,T] \to \mathbb{R}^n,\qquad \Omega_S\subset \mathbb{R}^2
$$

离散后是一段时空序列：

$$
[u_0^S,u_{\Delta t}^S,\ldots,u_T^S]
$$

额外条件记为 $c$，包含 PDE 类型、物理通道类型、扩散时间、可选模拟参数等。模型为 $M_\Theta$。

核心实验是自回归一步预测，使用 $T_p=1$ 个历史快照：

$$
u_{\text{in}}=[u_{t-T_p\Delta t}^S,\ldots,u_{t-\Delta t}^S],\qquad
u_{\text{out}}=[u_t^S]
$$

但该定义可替换为其他任务：

$$
u_{\text{in}}=\varnothing,\quad u_{\text{out}}=[u_t^S]
$$

用于无条件生成；或

$$
u_{\text{in}}=[u_{t-\Delta t}^S,u_{t+\Delta t}^S],\quad u_{\text{out}}=[u_t^S]
$$

用于时间插值。

---

### 2. Tokenization：时空 patch 与通道 token

PDE-Transformer 直接作用于原始规则网格数据，而不是 DiT 常用的 VAE latent space。

单通道输入尺寸为：

$$
T\times H\times W
$$

（空间 patch 为非重叠切分，隐含 stride=$p$；时间维 $T$ / 实验中的历史帧整体并入每个 patch，不沿时间维再做滑窗切分。）

给定空间 patch size $p$，将输入切成：

$$
N=\frac{H}{p}\cdot \frac{W}{p}
$$

个时空 patch，每个 patch 大小为：

$$
T\times p\times p
$$

再通过线性层映射到 $d$ 维 token：

$$
z_i = W_{\text{patch}}\operatorname{vec}(u_i)+b,\qquad z_i\in\mathbb{R}^d
$$

论文定义 token expansion rate：

$$
E(p):=\frac{d}{p^2T}
$$

$p$ 越小，token 越多，表达更细，但注意力计算更贵；$p$ 越大，计算更省，但压缩更强。实验结论是 $p=4,w=8$ 在精度与计算之间最好。

多通道有两种方案。

**Mixed Channel, MC：**

设最大通道数为 $C_{\max}$，每个 patch 为：

$$
T\times C_{\max}\times p\times p
$$

不足的通道补零，然后一次性嵌入：

$$
z_i = W_{\text{MC}}\operatorname{vec}(u_i^{1:C_{\max}})+b
$$

问题是不同物理量被压进同一个 token，等效每个通道的 expansion rate 下降为：

$$
E_{\text{MC}}(p)=\frac{d}{C_{\max}p^2T}
$$

即每个物理通道的信息密度随 $C_{\max}$ 增大而降低。

**Separate Channel, SC：**

对每个物理通道 $c$ 单独 patchify 和嵌入：

$$
z_{i,c}=W_{\text{SC}}\operatorname{vec}(u_{i,c})+b,\qquad z_{i,c}\in\mathbb{R}^d
$$

token 数变为：

$$
N_{\text{SC}}=C\cdot \frac{H}{p}\cdot \frac{W}{p}
$$

优点是每个通道保持同样的信息密度：

$$
E_{\text{SC}}(p)=\frac{d}{p^2T}
$$

代价是计算量随通道数 $C$ 线性增加。论文后续更重视 SC，因为预训练权重迁移到 Well 下游任务时收益明显大于 MC（SC 预训练收益约为 MC 的 $2.7\times$ 到 $4.4\times$）。

---

### 3. 通道间自注意力机制

PDE-Transformer 的关键改动是把注意力拆成两类：

1. 空间窗口内注意力：只在同一物理通道内、局部空间窗口内做。
2. 通道轴注意力：在同一空间 patch 位置处，不同物理通道之间做 axial attention。

对某个通道 $c$ 的窗口 token 集合 $\mathcal{W}$，空间 shifted-window MHSA 可写为：

$$
Q= \operatorname{RMSNorm}(ZW_Q),\quad
K= \operatorname{RMSNorm}(ZW_K),\quad
V=ZW_V
$$

$$
\operatorname{Attn}(Z)=
\operatorname{softmax}\left(
\frac{QK^\top}{\sqrt{d_h}} + B_{\text{rel}}(\Delta x,\Delta y)
\right)V
$$

其中 $B_{\text{rel}}$ 不是绝对位置编码，而是基于 log-spaced relative position，再经小型前馈网络生成的相对位置偏置。论文强调这比绝对位置更适合 PDE，因为它提高 translation-invariance / 平移泛化倾向，并更容易跨窗口分辨率泛化（未声明严格的 translation equivariance）。

SC 版本中，空间窗口注意力不跨通道：

$$
\operatorname{Attn}_{\text{space}}(z_{i,c}, z_{j,c'})
=0,\qquad c\neq c'
$$

通道交互改由 channel-wise axial MHSA 完成。对固定空间 patch 位置 $i$，令：

$$
Z_i=[z_{i,1},z_{i,2},\ldots,z_{i,C}]
$$

则通道注意力为：

$$
\operatorname{Attn}_{\text{channel}}(Z_i)
=
\operatorname{softmax}\left(
\frac{Q_iK_i^\top}{\sqrt{d_h}}
\right)V_i
$$

这里 token 序列长度是通道数 $C$，所以它专门建模“密度、速度、涡量、压力”等物理量之间的耦合。论文图 2 中的 SC block 可理解为：

$$
Z
\to Z+\operatorname{SW\text{-}MHSA}_{\text{space}}(Z)
\to Z+\operatorname{MHSA}_{\text{channel}}(Z)
\to Z+\operatorname{MLP}(Z)
$$

---

### 4. DiT 相关组件

PDE-Transformer 继承 DiT 的几个关键设计，但针对 PDE 做了修改。

**adaLN-Zero conditioning：**

所有 conditioning embedding 相加后输入 MLP，生成归一化层的 scale、shift，以及残差门控参数。可抽象为：

$$
e_c = e_{\text{PDE}} + e_{\text{channel}} + e_{\text{diffusion-time}} + e_{\text{other}}
$$

$$
(\gamma,\beta,\alpha)=\operatorname{MLP}(e_c)
$$

对 block 输入 $x$：

$$
\operatorname{adaLN}(x,c)=\gamma(c)\odot \operatorname{LN}(x)+\beta(c)
$$

adaLN-Zero 将残差分支初始化为近似零，使整个 residual block 初始接近恒等映射：

$$
x_{\ell+1}=x_\ell+\alpha(c)\odot F(\operatorname{adaLN}(x_\ell,c))
$$

（$\alpha(c)$ 残差门控为解释性抽象：原文明确所有 conditioning embeddings 相加、经 FFN 回归 scale/shift，adaLN-Zero 初始化使 residual block 接近 identity；未将 $\alpha(c)$ 作为显式公式展开，可按 DiT adaLN-Zero 理解为 scale/shift 并可能包含 residual scaling/gating 的实现细节。）

条件标签使用 10% dropout，因此同一个模型既能做 conditional，也能做 unconditional。

**位置编码：**

与原始 DiT 不同，论文不把 absolute positional embedding 加到 token 上，而是在窗口注意力分数中使用相对位置偏置：

$$
A_{ij}=\frac{q_i^\top k_j}{\sqrt{d_h}}+B_{\text{rel}}(r_i-r_j)
$$

**多尺度结构：**

整体是 U-shaped transformer stages，用 PixelUnshuffle 下采样 token、PixelShuffle 上采样 token，并在相同分辨率 stage 之间使用 skip connection。这样兼顾局部细节和大尺度耦合，同时避免 DiT 全局注意力在 $256^2$ 及更高分辨率上的二次爆炸。

**边界条件：**

shifted window 默认通过 rolling token 模拟周期边界；非周期边界可通过 attention mask 禁止跨边界 token 交互。

---

### 5. 损失函数与训练目标

**监督式 PDE surrogate：**

用于确定性 PDE solver 的一步预测，损失为 MSE：

$$
L_S
=
\mathbb{E}\left[
\left\|
M_\Theta(u_{\text{in}},c)-u_{\text{out}}
\right\|_2^2
\right]
$$

推理时自回归 rollout：

$$
\hat u_{t+\Delta t}=M_\Theta(\hat u_t,c)
$$

**扩散 / flow matching 训练：**

用于后验不确定、可能多解的问题。设：

$$
x_0\sim p_0=\mathcal{N}(0,I),\qquad x_1\sim p_1
$$

其中 $p_1$ 是目标 posterior。论文采用 flow matching 的线性概率路径：

$$
x_t=t u_{\text{out}}+[1-(1-\sigma_{\min})t]\epsilon
$$

$$
t\in[0,1],\qquad \epsilon\sim\mathcal{N}(0,I),\qquad \sigma_{\min}=10^{-4}
$$

条件扩展为：

$$
c_t=[c,t],\qquad u_{\text{in}}^t=[u_{\text{in}},x_t]
$$

训练目标为速度场回归：

$$
L_{\text{FM}}
=
\mathbb{E}\left[
\left\|
M_\Theta(u_{\text{in}}^t,c_t)
-
u_{\text{out}}
+
(1-\sigma_{\min})\epsilon
\right\|_2^2
\right]
$$

采样时从 $x_0\sim\mathcal{N}(0,I)$ 出发，解 ODE：

$$
dx_t=M_\Theta(u_{\text{in}}^t,c_t)\,dt,\qquad t:0\to 1
$$

论文用显式 Euler：

$$
x_{t+\Delta t}=x_t+\Delta t\cdot M_\Theta(u_{\text{in}}^t,c_t)
$$

注意：这篇论文没有采用 PINN 式 PDE residual loss，即没有显式最小化

$$
\|\partial_t u-\mathcal{N}(u)\|^2
$$

它的“无监督/生成式”部分主要是 unconditional 或 conditional flow matching，而不是物理方程残差约束训练。

---

### 6. 评估指标

使用 normalized RMSE：

$$
\operatorname{nRMSE}
=
\frac{1}{M}
\sum_{i=1}^M
\sqrt{
\frac{
\operatorname{MSE}(\hat u_{\text{out}},u_{\text{out}})
}{
\operatorname{MSE}(0,u_{\text{out}})
}
}
$$

rollout 评估是在自回归生成整段轨迹后，对每个时间步比较 $\hat u_t^S$ 与 $u_t^S$，再跨系统平均。

---

### 7. 16 类 PDE 预训练数据集

数据来自 Exponax / 谱方法生成（基于 APEBench 设计思路但未直接使用 APEBench），统一用高分辨率谱方法生成，原始分辨率 $2048\times2048$，训练时下采样到 $256\times256$。每类通常 $600$ 条轨迹、每条 $30$ 帧；Gray-Scott 子集为每配置 $100$ 条。通道数为 1 或 2。

16 类包括：

- `diff`：扩散方程，1 通道 density，变化参数为 $x,y$ 方向 viscosity。
- `fisher`：Fisher-KPP reaction-diffusion，1 通道 concentration，变化 diffusivity/reactivity。
- `sh`：Swift-Hohenberg，1 通道 concentration，变化 reactivity/critical number。
- `gs-alpha`、`gs-beta`、`gs-gamma`、`gs-epsilon`：Gray-Scott 非稳态配置，2 通道 $c_a,c_b$。
- `gs-delta`、`gs-theta`、`gs-iota`、`gs-kappa`：Gray-Scott 稳态配置，2 通道 $c_a,c_b$。
- `burgers`：二维 Burgers，2 通道 velocity $(x,y)$，变化 viscosity。
- `kdv`：Korteweg-de Vries，2 通道 velocity $(x,y)$，变化 domain extent 和 viscosity。
- `ks`：Kuramoto-Sivashinsky，1 通道 density，变化 domain extent，长 rollout 测试混沌。
- `decay-turb`：Navier-Stokes decaying turbulence，1 通道 vorticity，变化 viscosity。
- `kolm-flow`：Kolmogorov flow，1 通道 vorticity，变化 viscosity，长时间混沌维持流。

下游任务来自 Well dataset：Active Matter、Rayleigh-Bénard Convection、Shear Flow。它们引入更复杂动力学、非周期边界、非方形区域和更多通道，用于检验预训练迁移。

---

### 8. 关键超参数与消融结论

默认架构超参数：

$$
p=4,\qquad w=8,\qquad \text{mlp ratio}=4.0
$$

模型尺寸：

$$
d_S=96,\qquad d_B=192,\qquad d_L=384
$$

训练设置：

$$
\text{batch size}=256,\qquad \text{lr}=4\times 10^{-5},\qquad \text{epochs}=100
$$

优化器为 AdamW，使用 bf16 mixed precision、DDP、权重 EMA decay $0.999$，以及 EMA gradient clipping。

PDE-Transformer 结构深度为：

$$
[2,4,4,6,4,4,2]
$$

注意力 head 数为 16，activation 为 GELU，class dropout probability 为 0.1，qkv bias 为 true。

主要消融结论：

- **PDE-S vs baseline：** 在 16 PDE 预训练集上，PDE-S 的 $nRMSE_{10}=0.36$，优于 DiT-S $0.78$、UDiT-S $0.39$、scOT-S $0.59$、FactFormer $0.65$、UNet $0.68$；且 PDE-S 训练时间 7h42m，明显快于 UDiT-S 18h30m。
- **模型放大：** $d=96\to192\to384$ 时，$nRMSE_1$ 从 0.045 降到 0.038、0.035，但 GFlops 从 19.62 到 76.55、302.34。
- **窗口大小：** 固定 $p=4$ 增大 $w$ 会降低训练 loss，但测试 nRMSE 没明显改善，说明更大窗口可能过拟合。
- **patch size：** 保持 $p\cdot w=32$ 时，较小 $p$ 精度更好但计算更贵；$p=4,w=8$ 是折中点。
- **SC vs MC：** 预训练集上 SC 不损害精度，但计算随通道数上升；下游迁移时 SC 明显更强。
- **监督 vs diffusion：** 单样本 nRMSE 下监督训练更好；flow matching 稍差但可采样 posterior，对不确定性和多解任务更有价值。
- **预训练迁移：** PDE-S pretrained 在 Active Matter、RBC、Shear Flow 上均优于从零训练；SC 预训练收益比 MC 高约 $2.7\times$ 到 $4.4\times$。

---

### 9. 训练 / 推理流程伪代码

监督训练流程：

```python
for batch in dataloader:
    u_in, u_out, cond = batch

    tokens = patchify(u_in, patch_size=p)

    if separate_channels:
        tokens = embed_each_channel(tokens)
    else:
        tokens = embed_mixed_channels(tokens)

    cond_emb = embed_pde_type(cond) + embed_channel_type(cond)

    pred = PDETransformer(tokens, cond_emb)

    loss = mse(pred, u_out)
    loss.backward()

    ema_gradient_clip()
    optimizer.step()
    optimizer.zero_grad()
    update_weight_ema()
```

flow matching 训练流程：

```python
for batch in dataloader:
    u_in, u_out, cond = batch

    eps = normal_like(u_out)
    t = uniform(0, 1)

    x_t = t * u_out + (1 - (1 - sigma_min) * t) * eps

    u_in_t = concat(u_in, x_t)
    cond_t = concat(cond, t)

    target_velocity = u_out - (1 - sigma_min) * eps

    pred_velocity = PDETransformer(u_in_t, cond_t)

    loss = mse(pred_velocity, target_velocity)
    loss.backward()
    optimizer.step()
```

自回归 rollout：

```python
u = initial_state
trajectory = []

for step in range(num_steps):
    u_next = PDETransformer(u, cond)
    trajectory.append(u_next)
    u = u_next
```

flow matching 采样：

```python
x = normal(shape=u_out_shape)

for k in range(num_euler_steps):
    t = k / num_euler_steps
    velocity = PDETransformer(concat(u_in, x), concat(cond, t))
    x = x + dt * velocity
```

---

### 10. 与本库其他论文的关联

- 与 `denoising-diffusion-probabilistic-models.md`：DDPM 学习反向去噪马尔可夫链，PDE-Transformer 的生成式版本采用 flow matching，把扩散建模写成连续 ODE 速度场回归。两者共同点是从噪声分布生成目标样本，区别是本文更接近 rectified flow / flow matching，并把条件输入设为 PDE 历史状态与物理标签。
- 与 Attention / Transformer 系列：本文继承 ViT/DiT 的 patch token + MHSA，但为 PDE 改成 shifted-window attention、relative position bias、RMSNorm(Q/K)、U-shaped token multiscale，并新增 channel-wise axial attention。
- 与 Neural Operator、FNO、GNO、DeepONet：Neural Operator 学习函数空间到函数空间的映射，强调 resolution-invariant；PDE-Transformer 目前仍限制在 2D regular grids，但通过相对位置、窗口注意力、多尺度结构和预训练增强跨分辨率/跨任务泛化。论文也把 GNO 作为未来扩展到非结构网格的接口。
- 与 PINN / NSFnets / physics-informed 系列：PINN 通过 PDE residual、边界条件 residual 和数据项共同训练；本文不是 physics-informed loss，而是纯数据驱动 surrogate/generative model。优势是可大规模利用模拟数据预训练，推理快；短板是没有显式保证守恒律、边界条件或 PDE 残差为零。
- 与物理扩散模型 / flow reconstruction：本文的 diffusion PDE-Transformer 可看作面向 PDE posterior sampling 的基础骨干，适合不确定重建、部分观测、数据同化等任务，但论文当前主要验证自回归预测与下游微调。
## Review Questions

1. 在 $T_p=1$ 的自回归一步训练下，PDE-Transformer 把时间维整体并入 $T\times p\times p$ patch；如果扩展到多历史帧、变步长 rollout 或 AMR 时间推进，token expansion rate、窗口 receptive field 和误差累积应如何重新权衡？
2. SC 方案让 shifted-window MHSA 只在同一物理通道内做空间注意力，再用 channel-wise axial attention 交换通道信息；对压力-速度投影、涡量-流函数或多物理强耦合系统，这种因子化在哪些情况下会限制跨通道长程耦合？
3. 本文没有 physics-informed residual loss，而是用 MSE / flow matching 从模拟数据学习；在部署到非周期边界、非结构网格或 HPC CFD 框架时，应如何设计守恒量、边界条件和分辨率外推测试，避免只用 nRMSE rollout 判断可靠性？
