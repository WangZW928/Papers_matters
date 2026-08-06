# Machine Learning–Accelerated Computational Fluid Dynamics（机器学习加速计算流体力学）

**作者：** Dmitrii Kochkov, Jamie A. Smith, Ayya Alieva, Qing Wang, Michael P. Brenner, Stephan Hoyer
**期刊：** Proceedings of the National Academy of Sciences (PNAS), 118(21), 2021
**DOI：** [https://doi.org/10.1073/pnas.2101784118](https://doi.org/10.1073/pnas.2101784118)
**arXiv：** [https://arxiv.org/abs/2102.01010](https://arxiv.org/abs/2102.01010)
**阅读状态：** 🔬 精读
**流程状态：** ①元数据 ✓ | ②初稿 ✓ | ③评估 ✓(精读) | ④补充 ✓ | ⑤索引 ✓ | ⑥review ✓ | ⑦提交 ✓

---

## 摘要

### 中文翻译

流体数值模拟在天气、气候、空气动力学和等离子体物理等许多物理现象的建模中起着重要作用。流体由 Navier-Stokes 方程很好地描述，但大规模求解仍困难重重，受限于解析最小时空特征的计算成本，导致精度与可行性之间难以兼顾。本文用端到端深度学习改进计算流体力学（CFD）内部的近似，针对二维湍流建模：无论是直接数值模拟（DNS）还是大涡模拟（LES），结果都与基线求解器在**每个空间维度细化 8–10 倍**时同样精确，带来 **40–80 倍**的计算加速。该方法在长时间模拟中保持稳定，并能泛化到训练分布之外的强迫函数与雷诺数——这与黑箱机器学习方法形成对比。

### 原文

> Numerical simulation of fluids plays an essential role in modeling many physical phenomena, such as weather, climate, aerodynamics, and plasma physics. Fluids are well described by the Navier–Stokes equations, but solving these equations at scale remains daunting, limited by the computational cost of resolving the smallest spatiotemporal features. This leads to unfavorable trade-offs between accuracy and tractability. Here we use end-to-end deep learning to improve approximations inside computational fluid dynamics for modeling two-dimensional turbulent flows. For both direct numerical simulation of turbulence and large-eddy simulation, our results are as accurate as baseline solvers with 8 to 10× finer resolution in each spatial dimension, resulting in 40- to 80-fold computational speedups. Our method remains stable during long simulations and generalizes to forcing functions and Reynolds numbers outside of the flows where it is trained, in contrast to black-box machine-learning approaches.

---

## 文章总结

### 1. 解决什么问题？

湍流模拟中"解析最小空间特征"的成本决定了精度-计算量的两难：加密网格能提升精度但代价高昂，粗网格便宜但耗散过大。如何在粗网格上保持高精度？

### 2. 用了什么方法论？

在传统 CFD 求解器**内部**嵌入端到端学习的修正项（learned corrections / learned interpolation），而非将求解器整体替换为黑箱模型。用可微物理模拟器（jax-cfd）端到端训练，让网络学会修正粗网格离散化误差；模型在训练中通过求解器反向传播，使修正与数值格式协同优化（注意：修正项嵌入求解器内部、随 rollout 展开训练，并非简单的后处理残差加和）。

### 3. 主要结论是什么？

- 二维湍流 DNS/LES：粗网格 + 学习修正 ≈ 8–10× 细网格基线的精度，速度提升 40–80×
- 长时间积分稳定，无累积漂移
- 对未见过的强迫函数和雷诺数泛化良好
- 思想源头可追溯到 Bar-Sinai et al. 2019（learning data-driven discretizations），本文将其推广到非线性湍流与端到端可微框架

---


## 价值评估

Doctor 指定精读（跳过 Codex 价值评估）。按 6 级标准看，本文 idea 清晰度很高：不是用神经网络替代 CFD，而是在传统求解器内部学习最受粗网格影响的离散化环节。计算结果强，在二维湍流 DNS 与 LES 中达到约 $8$-$10\times$ 每空间维等效加密，并报告 $40$-$80\times$ 速度收益。预言能力中高：长时间模拟稳定，并能推广到更大区域、无强迫衰减湍流和更高 Reynolds 数，但主要证据仍在二维规则 staggered mesh。方法新颖性高，来源为 PNAS 2021/arXiv 2102.01010；精读判断：非常适合 Doctor 的数值格式、可微求解器和 HPC 框架主线。

## 公式与代码梳理

### 数学结构与核心公式

论文的物理对象是二维不可压 Navier-Stokes 方程。原文采用无量纲形式：

$$
\frac{\partial\mathbf{u}}{\partial t}
=
-\nabla\cdot(\mathbf{u}\otimes\mathbf{u})
+
\frac{1}{Re}\nabla^2\mathbf{u}
-
\frac{1}{\rho}\nabla p
+
\mathbf{f},
$$

$$
\nabla\cdot\mathbf{u}=0.
$$

其中 $\mathbf{u}$ 是速度场，$\mathbf{f}$ 是外力，$\rho$ 为常密度，$p$ 是用于 enforce incompressibility 的 Lagrange multiplier，$Re$ 控制对流与扩散的相对强度。二维诊断常用涡量

$$
\omega=\partial_x u_y-\partial_y u_x,
$$

以及能谱

$$
E(\mathbf{k})=\frac{1}{2}|\mathbf{u}(\mathbf{k})|^2.
$$

LES 情形中，速度替换为滤波速度 $\overline{\mathbf{u}}$，动量方程右端增加 sub-grid 项

$$
-\nabla\cdot\boldsymbol{\tau},
$$

其中

$$
\boldsymbol{\tau}
=
\overline{\mathbf{u}\otimes\mathbf{u}}
-
\overline{\mathbf{u}}\otimes\overline{\mathbf{u}}.
$$

附录中基线 LES 使用 Smagorinsky-Lilly SGS：

$$
\tau_{ij}
=
-2(C_s\Delta)^2|\overline{S}|\overline{S}_{ij},
$$

$$
\overline{S}_{ij}
=
\frac{1}{2}
(\partial_i u_j+\partial_j u_i),
\qquad
|\overline{S}|
=
2\sqrt{\sum_{i,j}\overline{S}_{ij}\overline{S}_{ij}},
$$

其中 $C_s=0.2$，$\Delta$ 是网格间距。

数值框架是 staggered-square mesh 上的有限体积法。速度分量放在 cell edges，压力放在 cell centers。一个时间步可抽象为

$$
\mathbf{u}^{*}
=
\mathbf{u}^{n}
+
\Delta t
\left[
\mathcal{C}_h(\mathbf{u}^{n})
+
\mathcal{D}_h(\mathbf{u}^{n})
+
\mathbf{f}^{n}
\right],
$$

$$
\mathbf{u}^{n+1}
=
\Pi_h(\mathbf{u}^{*}),
$$

其中 $\mathcal{C}_h$ 是离散对流项，$\mathcal{D}_h$ 是离散扩散项，$\Pi_h$ 是压力投影，用 Poisson solve enforce

$$
\nabla_h\cdot\mathbf{u}^{n+1}=0.
$$

本文的核心判断是：粗网格误差主要来自对流通量 $\mathbf{u}\otimes\mathbf{u}$ 的 face value 近似。因此 learned interpolation 不直接预测下一帧，而是替换有限体积通量构造中的插值算子。对某个 face 或插值目标 $x$，从局部 stencil $\{u_i\}_{i=1}^{n}$ 构造

$$
u(x)\approx\sum_{i=1}^{n}a_i u_i.
$$

不同于固定 polynomial interpolation，系数 $a_i$ 来自卷积神经网络对局部流场的输出。为保证至少一阶一致性，约束

$$
\sum_{i=1}^{n}a_i=1.
$$

实现上，网络先输出无约束向量 $\mathbf{x}\in\mathbb{R}^{n-1}$，再经仿射映射生成满足约束的插值系数：

$$
\mathbf{a}=A\mathbf{x}+\mathbf{b}.
$$

其中 $A$ 是全 1 约束矩阵零空间的一组基，$\mathbf{b}$ 是任意满足 $\sum_i b_i=1$ 的基准系数，例如最近源位置的线性插值。论文使用以 unit-cell 右上角为中心的 $4\times4$ patch，因此 $n=16$，需要 $15$ 个无约束输出生成一组插值系数。由于二维中每个速度分量和每个通量方向都要处理，对 $d$ 维空间有 $d^2$ 个 convective flux module；二维时为 $4$ 类通量，实际网络输出包含多个插值点的系数集合。

learned correction 是更接近 LES closure 的替代路线。它先用粗网格传统求解器得到未修正速度 $\mathbf{u}^{*}_t$，再加残差网络：

$$
\mathbf{u}_t
=
\mathbf{u}^{*}_t+\mathrm{LC}(\mathbf{u}^{*}_t).
$$

该式既可理解为 temporally discretized closure，也可理解为粗网格离散化误差修正。与 LI 相比，LC inductive bias 更弱，解释性与稳定性较差，但实现简单。

训练损失把神经模块放在完整求解器内部反传。给定高分辨率 DNS/LES 轨迹下采样后的 ground truth $\mathbf{u}(t_i)$，以及粗网格 learned solver 的 rollout $\widetilde{\mathbf{u}}(t_i)$，损失为

$$
L(x,y)
=
\sum_{t_i}^{t_T}
\mathrm{MSE}
\left(
\mathbf{u}(t_i),
\widetilde{\mathbf{u}}(t_i)
\right).
$$

关键不是单步 a priori fitting，而是 model-consistent training：网络在 unroll 后看到自己的输出作为下一步输入。论文中常用 32 步 unroll（需配合梯度截断/checkpointing 控制反向传播的显存与稳定性），并通过 gradient checkpoint 降低显存。

精度-分辨率等价可写为：若传统 solver 在网格 $h/K$ 上的误差与 learned coarse solver 在网格 $h$ 上相当，

$$
\mathrm{Err}_{\mathrm{ML}}(h)
\approx
\mathrm{Err}_{\mathrm{DNS}}\left(\frac{h}{K}\right),
$$

则 $K$ 是有效粗化因子。二维显式流体中，空间两个维度和 CFL 时间步共同带来近似 $K^{d+1}$ 的规模收益；考虑神经网络相对基线的单格点成本，论文给出运行时间估计

$$
T
\sim
(C_{\mathrm{ML}}+C_{\mathrm{physics}})
\left(\frac{N}{K}\right)^{d+1}.
$$

其中 $C_{\mathrm{ML}}$ 是每网格点 ML 推理成本，$C_{\mathrm{physics}}$ 是基线数值方法成本，$N$ 是 resolved grid 每维点数，$d$ 是空间维数，$K$ 是有效 coarse graining factor。实验中 $C_{\mathrm{ML}}/C_{\mathrm{physics}}\approx 12$，若 $K\approx10$ 且 $d=2$，速度比约为 $10^3/12\approx80$。

### 关键推导

第一步是把对流项写成有限体积通量问题。连续对流项

$$
-\nabla\cdot(\mathbf{u}\otimes\mathbf{u})
$$

在 cell average 上通过 Gauss 定理变成 face flux 求和。于是粗网格误差的关键不是直接拟合 $\partial_t\mathbf{u}$，而是更准确地估计 face 上的 $\mathbf{u}\otimes\mathbf{u}$。LI 用神经网络生成局部插值系数 $a_i$，但仍把通量放回守恒形式，因此局部动量守恒结构由 divergence operator 保留。

第二步是一致性约束。若真实局部场为常数 $u_i=c$，则

$$
\sum_i a_i u_i
=
c\sum_i a_i
=
c.
$$

只要 $\sum_i a_i=1$，插值至少能精确再现常数场，即一阶一致性的基础。通过 $\mathbf{a}=A\mathbf{x}+\mathbf{b}$，网络无论输出什么 $\mathbf{x}$，都落在约束仿射子空间里。这比在 loss 中惩罚 $\sum_i a_i-1$ 更硬，也更适合长期积分稳定性。

第三步是压力投影把 learned flux 的结果拉回不可压流形。粗步得到 $\mathbf{u}^{*}$ 后，解离散 Poisson 方程

$$
\nabla_h^2 p
=
\frac{\rho}{\Delta t}\nabla_h\cdot\mathbf{u}^{*},
$$

再投影

$$
\mathbf{u}^{n+1}
=
\mathbf{u}^{*}
-
\frac{\Delta t}{\rho}\nabla_h p.
$$

这说明神经网络没有负责所有物理约束；它只改善对流近似，而不可压约束仍由经典 projection method 强制执行。

### 对 HPC 框架的启示

这篇论文与 Doctor 的框架最贴近之处是 learned correction/learned interpolation 与数值格式融合。它给出的不是“神经 surrogate 取代 solver”，而是“solver 内部可插拔 learned stencil”。对 AMR 框架，可把每个 patch 的 face reconstruction、flux limiter、subgrid closure 抽象成 operator hook：默认实现是 WENO/Van Leer/central scheme，learned 实现输出 constrained stencil coefficients 或 residual flux。这样能保留守恒更新、边界处理、CFL 控制和 pressure projection。

可微求解器方面，论文说明端到端训练需要把 time stepper、projection、下采样、loss 全部放进 AD 图。但工程上并不一定要让所有线性求解器全量反传；可采用 checkpoint、custom VJP、implicit differentiation 或局部 unroll。对 matrix-free Poisson/Helmholtz solver，关键接口是让 projection 可微、可替换，并能在训练时控制显存。

性能模型方面，learned stencil 往往增加 FLOPs，但更适合 TPU/GPU dense tensor core；传统 CFD kernel 可能 memory-bound、stencil gather/scatter-heavy。Roofline 分析不能只比较 FLOPs，需要比较 effective resolution。若 learned solver 在同等误差下把 $N$ 降到 $N/K$，则即使单点成本高一个数量级，总体仍可能获益。对 3D 问题，潜在收益按 $K^{4}$ 放大，但通信、halo exchange、projection solve 和 AMR 负载均衡可能成为新瓶颈。

仓库关联上，本篇可与 `physics-informed-machine-learning-approach-for-augmenting-turbulence-models-a-co.md` 对照：后者更偏 turbulence closure，本文更偏 discretization correction。也可与 FNO 文档对照：FNO 学全局解算子，Kochkov 学局部数值算子。与 PINN 文档的关系是：PINN 把 PDE residual 放进训练目标，本文把 PDE 结构放进 time stepper 本身。

### 待深入研究

1. learned interpolation 在复杂边界、非结构网格和 AMR coarse-fine interface 上如何保持守恒、一致性与稳定性？是否需要约束通量而不是约束插值值？
2. 对三维湍流，局部 learned stencil 是否能表示 vortex stretching 主导的亚格子动力学？还是必须引入旋涡结构、应变率张量、不变量或等变网络？
3. 如何把 learned correction 与结构保持积分结合，例如保持不可压 Euler 的 Lie-Poisson 结构、能量/环量/Casimir，避免长期统计漂移？

## Review Questions

4. learned interpolation 若迁移到 AMR coarse-fine 接口，如何保证守恒、一致性和长期稳定？
5. 该方法主要修正对流通量近似；对高 Reynolds 数三维湍流，是否还需要显式建模亚格子应力？
6. 在 GPU/TPU 上，如何把 stencil 网络、projection solve 和 AD 反传放进统一成本模型？

1. 本文的 learned interpolation 保留了有限体积守恒和压力投影，但没有显式保持能量或 enstrophy；在二维不可压 Euler 极限下，应如何修改网络输出或 time stepper 来减少结构漂移？
2. 对 AMR 框架，learned stencil 的输入邻域跨越不同 refinement level 时，系数约束 $\sum_i a_i=1$ 是否足够？还需要哪些 moment constraints 才能保证 coarse-fine flux consistency？
3. 从 HPC 角度，单点 ML 成本 $C_{\mathrm{ML}}$ 高于传统 stencil，但等效分辨率 $K$ 降低；在 GPU/TPU 上应如何建立包含 halo、projection solve、checkpoint 和 AD 反传的真实成本模型？
