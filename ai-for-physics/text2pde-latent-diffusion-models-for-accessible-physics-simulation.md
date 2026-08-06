# Text2PDE: Latent Diffusion Models for Accessible Physics Simulation（Text2PDE：面向易用物理仿真的潜空间扩散模型）

**作者：** Anthony Zhou, Zijie Li, Michael Schneier, John R Buchanan, Amir Barati Farimani
**期刊：** ICLR 2025（arXiv 预印本 2024）
**DOI：** 无（会议论文）
**arXiv：** [https://arxiv.org/abs/2410.01153](https://arxiv.org/abs/2410.01153)
**阅读状态：** 🔬 精读
**流程状态：** ①元数据 ✓ | ②初稿 ✓ | ③评估 ✓(精读) | ④补充 ✓ | ⑤索引 ✓ | ⑥review ✓ | ⑦提交 ✓

---

## 摘要

### 中文翻译

深度学习的近期进展催生了许多数据驱动的 PDE 问题求解工作。这些神经 PDE 求解器通常比数值方法快得多；然而每种方法都有各自的局限，一般需要在训练成本、数值精度和对不同问题设置的易用性之间权衡。为解决这些局限，本文提出将潜空间扩散模型应用于物理仿真的若干方法：首先，提出一种带物理场条件（physics-field conditioning）的潜空间扩散架构，在潜空间对 PDE 解进行降噪采样；其次，加入文本编码器（text conditioning），使模型能够根据文本提示生成 PDE 解；第三，引入一个带形状条件的引导模块，在推理时通过引导（guidance）把解的时空几何约束纳入生成过程。最终训练出一个单一模型，可直接依据文本描述和/或边界几何生成多样的 PDE 解，无需重新训练。在标准数据集（包括 2D 达西流、2D/3D 时间相关 NS 方程、浅水方程等）上评估，Text2PDE 在相似或更低训练成本下达到与当前最优神经求解器相当或更好的精度，并能泛化到未见过的文本提示。

### 原文

> Recent advances in deep learning have inspired numerous works on data-driven solutions to partial differential equation (PDE) problems. These neural PDE solvers can often be much faster than their numerical counterparts; however, each presents its unique limitations and generally balances training cost, numerical accuracy, and ease of applicability to different problem setups. To address these limitations, we introduce several methods to apply latent diffusion models to physics simulation. First, we propose a latent diffusion architecture with physics-field conditioning to denoise PDE solutions in the latent space. Second, we add a text encoder for conditioning, enabling the model to generate PDE solutions conditioned on text prompts. Third, we introduce a shape-conditioned guidance module to incorporate the geometry of the solutions' spatiotemporal domain into the generation process through guidance at inference time. The resulting model can generate diverse PDE solutions directly from textual descriptions and/or boundary geometries without retraining. Evaluated on standard datasets, including 2D Darcy flow, 2D/3D time-dependent Navier-Stokes equations, and the shallow-water equations, Text2PDE achieves comparable or better accuracy than state-of-the-art neural solvers at similar or lower training costs and generalizes to unseen text prompts.

---

## 文章总结

### 1. 解决什么问题？

现有神经 PDE 求解器在训练成本、精度和易用性之间难以兼顾，且大多针对单一问题设置（固定方程、固定几何、固定边界），用户门槛高。能否用自然语言描述直接生成 PDE 解？

### 2. 用了什么方法论？

潜空间扩散（latent diffusion）三件套：
1. **physics-field conditioning**：在潜空间对 PDE 解降噪，条件为物理场（如初始/边界/参数场）
2. **text conditioning**：文本编码器把提示词嵌入生成条件
3. **shape-conditioned guidance**（论文的补充机制，主实验主要使用 vanilla conditional generation）：推理期引导，把解的时空域几何（边界形状）约束纳入采样

单一模型在数据集与条件集合覆盖范围内支持多方程/多几何/多文本提示，无需重训。

### 3. 主要结论是什么？

在达西流、2D/3D 时变 NS、浅水方程上达到或超过 SOTA 神经求解器精度，训练成本相当或更低，并能泛化到未见文本提示；把"用户友好"（自然语言驱动）带进神经 PDE 求解。

---


## 价值评估

Doctor 指定精读（跳过 Codex 价值评估）。按 6 级标准看，本文 idea 清晰度中高：把 PDE 全时空轨迹压缩到潜空间，再用条件扩散一次生成 rollout，目标是降低自回归误差并提供文本接口。计算结果较强：在 cylinder flow、buoyancy-driven smoke、3D turbulence 等数据集上与 FNO、GINO、MGN、OFormer、ACDM 等比较，并报告参数量与 FLOPs。预言能力中等：文本条件能生成合理样本，但文本本身欠定，first-frame conditioning 更精确；推理成本仍受 denoising steps 影响。方法新颖性高，来源为 ICLR 2025/arXiv 2410.01153；精读判断：值得精读，尤其适合连接 DDPM、PDE-Transformer、Neural Operator 与可用性导向的 PDE 数据接口。

## 公式与代码梳理

### 数学结构与核心公式

论文考虑一维时间与多维空间上的时间相关 PDE。设空间坐标

$$
x=[x_1,x_2,\ldots,x_D]^T\in\Omega,
$$

物理场为

$$
u:[0,T]\times\Omega\to\mathbb{R}^{d_p}.
$$

通用 PDE 写成

$$
\partial_t u
=
F(t,x,u,\partial_x u,\partial_{xx}u,\ldots),
\qquad
t\in[0,T],\ x\in\Omega.
$$

初值与边界条件为

$$
u(0,x)=u_0(x),
\qquad x\in\Omega,
$$

$$
B[u](t,x)=0,
\qquad t\in[0,T],\ x\in\partial\Omega.
$$

传统神经 PDE solver 多学习一步或多步自回归映射

$$
u(t,x_m)\mapsto u(t+\Delta t,x_m),
$$

而 Text2PDE 把完整时空轨迹作为生成对象，建模条件分布

$$
p\left(
u(t_0:T,x_{1:M})
\mid
u_0,\ B
\right).
$$

论文为了避免物理空间维度过高，在 learned latent space 中做扩散。设完整解离散为

$$
u\in\mathbb{R}^{T\times M\times d_p},
$$

编码器 $E$ 与解码器 $D$ 给出

$$
z=E(u),\qquad
\hat{u}=D(z),
$$

其中

$$
z\in\mathbb{R}^{T_l/f\times M_l/f\times d_l}
$$

是压缩后的 spatio-temporal latent，$T_l,M_l$ 是 latent grid 的时间和空间分辨率，$f$ 是 CNN encoder 的下采样因子，$d_l$ 是 latent dimension。

对非结构 mesh，论文用 kernel aggregation 把任意物理坐标映射到规则 latent grid。令时空坐标 $y=(t,x)$，latent coordinate 为 $y_l$，局部球为 $B_r(y_l)$。连续形式可写为

$$
q(y_l)
=
\int_{B_r(y_l)}
\kappa_\theta(y_l,y)u(y)\,\mathrm{d}y.
$$

离散 Riemann sum 为

$$
q(y_l)
\approx
\sum_{y_b\in B_r(y_l)}
\kappa_\theta(y_l,y_b)u(y_b)\mu(y_b),
$$

其中 $\mu(y_b)$ 是 Riemann 权重。这里 $q$ 是规则 latent grid 上的中间场，随后由 CNN autoencoder 压缩为 $z$。mesh decoder 反向执行局部聚合；给定 decoded latent grid $q_d$，在物理查询点 $y$ 上重建

$$
u_d(y)
=
\sum_{y_b\in B_r(y)}
\kappa_\theta(y,y_b)q_d(y_b)\mu(y_b),
$$

其中此处 $y_b$ 表示落入 $B_r(y)$ 的 latent grid 点。这个结构使模型可在任意 mesh query points 上解码，因此 geometry/shape 信息可以通过 query coordinates、boundary mesh 与局部球邻域进入解码过程。若数据本来是均匀网格，可省略 kernel integration，直接用 CNN autoencoder。

latent DDPM 部分采用标准 Gaussian noising。为避免与 PDE 物理时间 $t$ 混淆，扩散步记为 $n=1,\ldots,N$。给定 clean latent $z_0$，前向过程为

$$
q(z_n\mid z_0)
=
\mathcal{N}
\left(
z_n;\sqrt{\bar{\alpha}_n}z_0,
(1-\bar{\alpha}_n)I
\right),
$$

等价采样为

$$
z_n
=
\sqrt{\bar{\alpha}_n}z_0
+
\sqrt{1-\bar{\alpha}_n}\epsilon,
\qquad
\epsilon\sim\mathcal{N}(0,I).
$$

去噪网络预测噪声：

$$
\epsilon_\theta(z_n,n,c),
$$

其中 $c$ 是条件，可来自 physics field、text 或 geometry/shape。训练损失为

$$
\mathcal{L}
=
\mathbb{E}_{z,\epsilon\sim\mathcal{N}(0,I),n}
\left[
\left\|
\epsilon-\epsilon_\theta(z_n,n,c)
\right\|_2^2
\right].
$$

推理时，从

$$
z_N\sim\mathcal{N}(0,I)
$$

开始反向采样，近似

$$
p_\theta(z_{n-1}\mid z_n,c)
=
\mathcal{N}
\left(
z_{n-1};
\mu_\theta(z_n,n,c),
\Sigma_n
\right).
$$

常见 DDPM 噪声参数化下，均值可写为

$$
\mu_\theta(z_n,n,c)
=
\frac{1}{\sqrt{\alpha_n}}
\left(
z_n
-
\frac{1-\alpha_n}{\sqrt{1-\bar{\alpha}_n}}
\epsilon_\theta(z_n,n,c)
\right).
$$

physics-field conditioning 对应 first-frame conditioning。论文用初始帧作为 $u_0$ 与边界 $B$ 的 proxy，定义 domain-specific encoder

$$
c_{\mathrm{phys}}
=
E_{\mathrm{phys}}(u_0).
$$

对非结构数据，该 encoder 可复用 mesh aggregation，把 first frame 映射为 conditioning sequence：

$$
C_{\mathrm{phys}}\in\mathbb{R}^{L_c\times d_c}.
$$

text conditioning 则先 tokenization 并嵌入 prompt $s$：

$$
e_{1:L}=E_{\mathrm{tok}}(s),
$$

再用 pretrained/fine-tuned transformer encoder，例如 RoBERTa，得到

$$
C_{\mathrm{text}}
=
E_{\mathrm{text}}(e_{1:L})
\in\mathbb{R}^{L_c\times d_c}.
$$

DiT backbone 的条件注入有两种：mean pooling 后用于 adaLN-Zero，

$$
\bar{c}
=
\frac{1}{L_c}\sum_{\ell=1}^{L_c}C_\ell,
$$

以及在 DiT self-attention 后插入 cross-attention：

$$
\mathrm{Attn}(H,C,C)
=
\mathrm{softmax}
\left(
\frac{(HW_Q)(CW_K)^T}{\sqrt{d}}
\right)
CW_V.
$$

shape/geometry guidance 可以按论文架构理解为 mesh-conditioned decoding 与推理期条件约束。几何输入 $s_{\mathrm{geo}}$ 包含边界、障碍物、query mesh 或 domain mask，经 shape encoder 得到

$$
C_{\mathrm{shape}}=E_{\mathrm{shape}}(s_{\mathrm{geo}}).
$$

若使用 classifier-free guidance，条件噪声预测可写为

$$
\tilde{\epsilon}_\theta(z_n,n,c)
=
\epsilon_\theta(z_n,n,\varnothing)
+
w\left[
\epsilon_\theta(z_n,n,c)
-
\epsilon_\theta(z_n,n,\varnothing)
\right],
$$

其中 $w$ 是 guidance strength。若同时有 physics、text、shape 三种条件，可合并为

$$
c=(C_{\mathrm{phys}},C_{\mathrm{text}},C_{\mathrm{shape}}),
$$

或用加权形式

$$
\tilde{\epsilon}_\theta
=
\epsilon_\theta(z_n,n,\varnothing)
+
w_p\Delta\epsilon_p
+
w_t\Delta\epsilon_t
+
w_s\Delta\epsilon_s.
$$

若 shape guidance 以外部约束能量实现，可定义

$$
\mathcal{L}_{\mathrm{shape}}(z_n)
=
\left\|
M_{\mathrm{out}}\odot D(\hat{z}_0(z_n))
\right\|_2^2
+
\left\|
M_{\partial\Omega}\odot B[D(\hat{z}_0(z_n))]
\right\|_2^2,
$$

并在采样时修正

$$
z_n
\leftarrow
z_n
-
\lambda_n\nabla_{z_n}\mathcal{L}_{\mathrm{shape}}(z_n).
$$

这里 $M_{\mathrm{out}}$ 表示域外 mask，$M_{\partial\Omega}$ 表示边界 mask，$\hat{z}_0(z_n)$ 是由当前噪声 latent 估计的 clean latent。需要注意：论文主实验报告 classifier-free guidance 对 PDE 精度帮助有限，主要结果倾向使用 vanilla conditional generation；shape/mesh 信息更多通过 autoencoder 的坐标条件与 decoder query 进入，而不是像图像生成那样依赖强 CFG。

### 关键推导

第一步是从自回归 rollout 改为全轨迹生成。传统模型近似

$$
p(u_{1:T}\mid u_0)
=
\prod_{i=1}^{T}
p(u_i\mid u_{i-1}),
$$

误差会随 rollout 累积。Text2PDE 直接学习

$$
p(u_{1:T}\mid c),
$$

并在潜空间一次采样完整 $T$ 帧。这牺牲了任意长时间外推的灵活性，但减少了逐步 feedback error。

第二步是非结构 mesh 到规则 latent grid 的算子化。kernel aggregation

$$
q(y_l)
\approx
\sum_{y_b\in B_r(y_l)}
\kappa_\theta(y_l,y_b)u(y_b)\mu(y_b)
$$

可视为从物理函数 $u(y)$ 到 latent 函数 $q(y_l)$ 的局部积分算子。它比直接把 mesh 点塞进 CNN 更合理，也比纯 GNN autoencoder 更容易利用 CNN/DiT 的成熟 scaling 经验。

第三步是条件扩散。DDPM 学的是 score/噪声方向，条件 $c$ 通过 encoder 进入

$$
\epsilon_\theta(z_n,n,c).
$$

若 $c=u_0$，模型近似确定性 PDE 条件分布；若 $c=$ text prompt，问题欠定，模型输出的是文本描述下的 plausible solution distribution。这个差别解释了为什么 first-frame conditioning 通常更准，而 text conditioning 更像可用性接口。

### 对 HPC 框架的启示

Text2PDE 对 HPC 框架的启示首先是数据接口：PDE 数据不应只保存为 dense tensor，还应显式保存坐标、mesh connectivity、boundary tags、physical channels、时间采样、单位和 prompt/caption metadata。其 mesh autoencoder 相当于一个可学习的 gather/scatter operator，可被框架抽象为 `encode(mesh_field -> latent_grid)` 与 `decode(latent_grid, query_mesh -> mesh_field)` 两个 kernel。对 AMR 数据，类似接口可把多层 patch、cell-centered/face-centered variables、ghost zones 和 boundary masks 统一编码到 latent grid。

第二是潜空间采样成本。完整物理空间 DDPM 对 3D 时空场几乎不可接受；latent diffusion 的压缩比在 cylinder flow、smoke、3D turbulence 中非常关键。HPC 实现要分别评估 autoencoder 编解码、DiT denoising steps、cross-attention conditioning、DDIM 减步采样的成本。推理时间大致为

$$
T_{\mathrm{infer}}
\approx
T_{\mathrm{enc\_cond}}
+
S\cdot T_{\mathrm{DiT}}
+
T_{\mathrm{dec}},
$$

其中 $S$ 是采样步数。若加入 shape/PDE residual guidance，还要增加

$$
S\cdot T_{\nabla \mathcal{L}_{\mathrm{guide}}},
$$

这可能需要每步 decoder 或近似 decoder，成本很高。

第三是与已有文档的连接。`denoising-diffusion-probabilistic-models.md` 提供 DDPM 基础公式；`a-physics-informed-diffusion-model-for-high-fidelity-flow-field-reconstruction.md` 可对照 residual guidance 与 observation consistency；`pde-transformer-efficient-and-versatile-transformers-for-physics-simulations.md` 可对照 DiT/Transformer 在 PDE 时空 token 上的用法；FNO 与 Neural Operator 文档则用于比较“确定性 operator regression”与“生成式 conditional distribution modeling”。

### 待深入研究

1. 文本条件 PDE 解是欠定问题。如何给出 uncertainty quantification，使模型输出的不只是一个 rollout，而是满足同一 prompt 的后验分布、置信区间和物理残差统计？
2. 全轨迹 latent diffusion 固定时间窗口。如何结合 autoregressive LDM、multirate time stepping 或 symplectic/structure-preserving integrator，使长时间物理结构不漂移？
3. 对复杂几何与 AMR，mesh autoencoder 的 kernel aggregation 是否能保持守恒量、边界通量和拓扑结构？是否需要把 finite-volume flux、discrete exterior calculus 或 differential forms 纳入 latent representation？

## Review Questions

4. 文本条件在 PDE 场景下高度欠定，模型应如何输出不确定性而非单一 rollout？
5. 对 Hamiltonian 或守恒系统，latent diffusion 如何避免破坏能量面、Casimir 或相位结构？
6. 若部署到 HPC 流水线，主要瓶颈是 DiT 采样、mesh decoder 还是 guidance 反传，如何做步数与缓存优化？

1. Text2PDE 把 PDE 求解从确定性 operator learning 改成条件生成；对 Hamiltonian 或 Lie-Poisson 系统，扩散采样得到的分布应如何约束在固定能量面、Casimir level set 或辛流形附近？
2. 文本 prompt 是紧凑但欠定的条件。对于工程 CFD，哪些物理量必须继续作为 field/mesh condition 输入，哪些可以安全地交给 text condition 表达？
3. 若在 HPC 框架中部署 Text2PDE，推理瓶颈会在 DiT denoising、mesh decoder、还是 guidance gradient？如何设计缓存、低步 DDIM/consistency sampling 和多 GPU 分块来使 3D rollout 可用？
