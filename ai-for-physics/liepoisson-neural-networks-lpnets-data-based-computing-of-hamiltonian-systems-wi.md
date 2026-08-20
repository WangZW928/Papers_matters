# Lie–Poisson Neural Networks (LPNets): Data-based computing of Hamiltonian systems with symmetries

**Authors:** Christopher Eldred

**DOI:** [10.1016/j.neunet.2024.106162](https://doi.org/10.1016/j.neunet.2024.106162)

**Source PDF:** `1-s2.0-S0893608024000868-main.pdf`

**阅读状态：** 🔬 精读
**流程状态：** ①元数据 ✓ | ②初稿 ✓ | ③评估 ✓(精读) | ④补充 ✓ | ⑤索引 ✓ | ⑥review ✓ | ⑦提交 ⏳

---

## 摘要

### 中文翻译

LPNets（Eldred 等）：把对称性诱导的 Lie-Poisson bracket 视为已知硬结构，用神经网络学习未知/近似的 Hamiltonian，网络层按 Lie 代数结构实例化，从而自动保持 Casimir 等结构不变量，实现数据驱动的结构保持哈密顿系统建模。

## 价值评估

Doctor 指定精读。本文把对称性诱导的 Lie--Poisson bracket 视为已知硬结构，把未知或近似的 Hamiltonian 交给数据学习。其 Casimir 保持是由层映射的结构而非训练误差保证；能量或相位精度则仍须独立评估，尤其当训练轨迹来自非结构保持离散时。

## 公式与代码梳理

### 数学结构与核心公式

Lie-Poisson 系统定义在 Lie 代数 $\mathfrak{g}$ 的对偶空间 $\mathfrak{g}^{*}$ 上。设状态为 $\mu\in\mathfrak{g}^{*}$，Hamiltonian 为 $h:\mathfrak{g}^{*}\to\mathbb{R}$，函数 $F,G:\mathfrak{g}^{*}\to\mathbb{R}$ 的 Lie-Poisson bracket 写作

$$
\{F,G\}_{\pm}(\mu)
=
\pm\left\langle
\mu,
\left[
\frac{\delta F}{\delta\mu},
\frac{\delta G}{\delta\mu}
\right]
\right\rangle.
$$

动力学为

$$
\frac{dF}{dt}=\{F,h\}_{\pm},
\qquad
\dot{\mu}
=
\mp\operatorname{ad}^{*}_{\delta h/\delta\mu}\mu.
$$

符号正负取决于左/右不变约定。论文的重点不是从数据学习任意向量场 $\dot{\mu}=f_\theta(\mu)$，而是学习保持 Poisson bracket 的离散映射

$$
\mu_{n+1}=\Phi_\theta(\mu_n),
\qquad
\{F\circ\Phi_\theta,G\circ\Phi_\theta\}
=
\{F,G\}\circ\Phi_\theta.
$$

Casimir 是 Poisson tensor 的退化方向对应的不变量：

$$
\{C,F\}=0
\quad \text{for all } F,
\qquad
\dot{C}(\mu)=0.
$$

例如刚体在 $\mathfrak{so}(3)^{*}$ 上的 bracket 为

$$
\{F,G\}(\Pi)
=
-\Pi\cdot
\left(
\frac{\partial F}{\partial \Pi}
\times
\frac{\partial G}{\partial \Pi}
\right),
$$

Hamiltonian 为

$$
H(\Pi)=\frac{1}{2}\Pi\cdot I^{-1}\Pi,
$$

方程为

$$
\dot{\Pi}
=
-I^{-1}\Pi\times \Pi.
$$

Casimir 是角动量模长：

$$
C(\Pi)=\frac{1}{2}\|\Pi\|^2.
$$

LPNets 的核心构造是使用由简单测试 Hamiltonian 生成的精确 Poisson map。若测试 Hamiltonian 取线性形式

$$
H_{\alpha}(\mu)=\langle \alpha,\mu\rangle,
\qquad
\alpha\in\mathfrak{g},
$$

则其 Hamiltonian flow 是 coadjoint action：

$$
\mu(t)=\operatorname{Ad}^{*}_{\exp(\mp t\alpha)}\mu(0).
$$

这个映射天然保持 Lie-Poisson bracket 和所有 Casimir。LPNets 用神经网络从状态预测局部参数

$$
\bar{\alpha}=NN_\theta(\mu),
$$

再用对应 Poisson map 推进一步：

$$
\mu_{n+1}=T_{\bar{\alpha}(\mu_n)}(h)\mu_n.
$$

G-LPNets 则把多个显式 Poisson map 作为网络层组合：

$$
\Phi_\theta
=
T_M(a_M,\alpha_M,b_M,h/M)
\circ\cdots\circ
T_1(a_1,\alpha_1,b_1,h/M).
$$

训练损失是轨迹点对的均方误差：

$$
\mathcal{L}(\theta)
=
\frac{1}{N}
\sum_{i=1}^{N}
\left\|
\Phi_\theta(\mu_i^0)-\mu_i^f
\right\|^2.
$$

但与普通 MSE 网络不同，$\Phi_\theta$ 的每一层都是 Poisson map，所以在该 map 精确实现、变量确实处于同一 Lie--Poisson 流形的前提下，训练参数取何值都不会把状态带离 Casimir 叶面；浮点和 map 实现误差仍需量测。

### 关键推导

第一步是从 Hamiltonian vector field 到 coadjoint orbit。对线性 Hamiltonian $H_\alpha(\mu)=\langle\alpha,\mu\rangle$，有 $\delta H_\alpha/\delta\mu=\alpha$，故

$$
\dot{\mu}
=
\mp\operatorname{ad}^{*}_{\alpha}\mu.
$$

其解是

$$
\mu(t)=\operatorname{Ad}^{*}_{\exp(\mp t\alpha)}\mu(0).
$$

这说明一个简单可积 Hamiltonian 就能生成沿 coadjoint orbit 的精确结构保持移动。

第二步是局部完备性。真实一步流映射 $\varphi_h$ 若也是同一 Poisson 结构上的 Hamiltonian flow，则局部可以由若干这种基本 Poisson map 组合近似：

$$
\varphi_h(\mu)
\approx
T_{\alpha_s}(h_s)\circ\cdots\circ T_{\alpha_1}(h_1)(\mu).
$$

神经网络不直接输出 $\mu_{n+1}$，而是输出这些结构保持变换的参数。

第三步是 Casimir 守恒。若 $C$ 是 Casimir，任意 Poisson map $\Phi$ 都保持 symplectic leaf / coadjoint orbit，因此

$$
C(\Phi(\mu))=C(\mu)
$$

在数值上只受浮点误差影响。这比在 loss 中添加 $\lambda |C(\mu_{n+1})-C(\mu_n)|^2$ 更强，因为后者只是软约束。

### 对 HPC 框架的启示

LPNets 的核心启示是：对物理系统，learned time-stepper 应优先保持几何结构，再谈拟合误差。Doctor 的 Hamiltonian ideal fluid、MHD、GPE/量子涡都不是 canonical $(q,p)$ 系统，直接套 HNN 会遗漏非典范 Poisson bracket。LPNets 提供了把已知 bracket 固化为算子层的范式。

对 HPC 框架，可把结构保持 map 做成 `PoissonMap` 接口：

$$
\texttt{state_next = poisson_map.apply(state, parameters, dt)}.
$$

神经网络只产生低维参数或 Hamiltonian correction，而不是直接覆盖 solver。这样更容易与现有辛积分器、JFNK、matrix-free residual、AMR time stepping 结合。

与仓库里的 `hamiltonian-neural-networks.md` 相比，LPNets 是非典范推广；与 `hamiltonian-description-of-the-ideal-fluid.md` 相比，它提供数据驱动近似流映射；与 `noncanonical-hamiltonian-density-formulation...` 相比，它提示未来可学习 density-level Hamiltonian，但保留 bracket。

### 待深入研究

1. 对理想流体和 MHD 的无限维 Lie-Poisson bracket，如何构造有限维、Casimir 保持、GPU 友好的 Poisson map？
2. LPNets 保 Casimir 但不严格保能量，是否应与 discrete gradient、variational integrator 或 learned Hamiltonian splitting 结合？
3. 对 AMR 网格，coadjoint orbit 的离散表示会随 refinement 改变，如何定义跨网格 Poisson transfer？

## Review Questions

1. LPNets 把 Poisson bracket 当作已知硬结构；对 Doctor 的量子涡/GPE 问题，哪些变量选择能让 bracket 最简单？
2. 若训练数据来自非结构保持求解器，LPNets 保 Casimir 到机器精度是否可能“纠正”数据，还是会造成相位误差？
3. G-LPNets 的 Poisson map composition 能否看作一种 learned geometric integrator，并与传统 splitting method 建立误差阶分析？
