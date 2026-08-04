# 深度平衡模型

# Deep Equilibrium Models

**作者：** Shaojie Bai, J. Zico Kolter, Vladlen Koltun
**期刊：** NeurIPS 2019（Spotlight/Oral；Advances in Neural Information Processing Systems 32, 2019）
**DOI：** 无（会议论文；arXiv 版为正式文本）
**arXiv：** [https://arxiv.org/abs/1909.01377](https://arxiv.org/abs/1909.01377)（v2, 2019-10-28）
**代码：** https://github.com/locuslab/deq
**阅读状态：** 🔬 精读（Doctor 指定）
**流程状态：** ①元数据 ✓ | ②初稿 ✓ | ③评估 ✓(精读) | ④补充 ✓ | ⑤索引 ✓ | ⑥review ✓(JARVIS 补) | ⑦提交 ⏳

---

## 摘要

### 中文翻译
我们提出一种序列数据建模的新方法：深度平衡模型（DEQ）。受"许多现有深度序列模型的隐层会收敛到某个不动点"这一观察的启发，DEQ 直接通过**求根（root-finding）**找到这些平衡点。该方法等价于运行一个无限深（权重共享）的前馈网络，但显著优势是可以用**隐式微分**解析地通过平衡点反向传播。由此，无论网络的"有效深度"是多少，训练与预测都只需**常数内存**。我们展示了 DEQ 如何应用于两种最先进的深度序列模型：自注意力 Transformer 与 trellis 网络。在 WikiText-103 等大规模语言建模任务上，DEQ 1) 在参数相近时往往超越这些最先进模型；2) 计算需求与现有模型相当；3) 大幅降低内存消耗（常是大规模序列模型训练的瓶颈），实验中内存最多降低 88%。

### 原文
> We present a new approach to modeling sequential data: the deep equilibrium model (DEQ). Motivated by an observation that the hidden layers of many existing deep sequence models converge towards some fixed point, we propose the DEQ approach that directly finds these equilibrium points via root-finding. Such a method is equivalent to running an infinite depth (weight-tied) feedforward network, but has the notable advantage that we can analytically backpropagate through the equilibrium point using implicit differentiation. Using this approach, training and prediction in these networks require only constant memory, regardless of the effective "depth" of the network. ...

---

## 文章总结

### 1. 解决什么问题？
深层序列模型（Transformer、trellis nets）层数越多表达力越强，但训练内存随深度线性增长（需保存每一层的激活用于反传），成为大模型瓶颈。本文要回答：能否把"堆很多层"替换为"求解一个隐式层的平衡点"，既保留无限深的表达力，又把内存降到常数、并用隐式微分高效训练？

### 2. 用了什么方法论？
- 核心观察：权重共享的深度网络迭代 $z_{i+1}=f_\theta(z_i,x)$ 会收敛到不动点 $z^*=f_\theta(z^*,x)$；与其迭代到收敛，不如直接用**求根算法**（Broyden 拟牛顿、Anderson 加速等）解 $g(z)=f_\theta(z,x)-z=0$。
- **隐式微分**：在平衡点 $z^*$ 上对损失 $L$ 关于参数 $\theta$ 求导，利用不动点方程隐式求导（含 $(I-J_{f})^{-1}$ 的逆或通过求解线性系统得到），**无需**沿迭代链展开反向传播——反传内存 O(1)。
- 将 DEQ 嵌入 Transformer（自注意力层做不动点层）与 trellis 网络，在 WikiText-103 语言建模上验证。
- 理论保证：证明隐式微分的 Jacobian 估计（通过 Neumann 级数/迭代近似 $(I-J)^{-1}$ 的收敛条件）。

### 3. 主要结论是什么？
DEQ 把隐式层（平衡点）作为一等公民：前向 = 求根，反向 = 隐式微分，内存 O(1) 而与"深度"无关；在 WikiText-103 上以相近参数量超越 Transformer/trellis 基线，内存最多降 88%。方法论上，DEQ 建立了"网络层 = 非线性方程求解"的范例，与数值分析中的 Newton-Krylov/JFNK、不动点迭代、隐式时间步进有深刻的心智对应——这对理解隐式 PDE 求解器与可微仿真（可微根求解、可微隐式层）有直接价值。

---

## 价值评估

Doctor 指定精读（跳过 Codex 价值评估）。

## 公式与代码梳理

（本小节由 Codex 精读补充，2026-08-04）

### 1. 不动点层：从“堆层”到“求根”

传统权重共享序列模型可以写成逐层迭代：

\[
z^{[i+1]}_{1:T}=f_\theta(z^{[i]}_{1:T};x_{1:T}),\qquad z^{[0]}_{1:T}=0 .
\]

若同一个变换 $f_\theta$ 被反复施加，并且隐藏状态逐渐稳定，则无限深极限满足：

\[
z^\star_{1:T}=f_\theta(z^\star_{1:T};x_{1:T}) .
\]

DEQ 的核心不是显式展开很多层，而是把最终隐藏状态定义为这个不动点。令

\[
g_\theta(z;x)=f_\theta(z;x)-z ,
\]

则平衡点等价于非线性方程的根：

\[
g_\theta(z^\star;x)=0 .
\]

朴素固定点迭代是

\[
z_{k+1}=f_\theta(z_k;x),
\]

它相当于用 $g(z)=f(z)-z$ 做最简单的松弛迭代。若 $f_\theta$ 是压缩映射，局部 Jacobian $J_f=\partial f_\theta/\partial z$ 的谱半径满足 $\rho(J_f)<1$，该迭代收敛。但深度网络中的 $f_\theta$ 通常高维、非线性强，朴素迭代可能振荡或收敛很慢。论文因此把前向传播改成 black-box root finding：

\[
z^\star=\operatorname{RootFind}(g_\theta;x).
\]

### 2. 前向求根：Broyden 与不动点加速

Newton 法求解 $g(z)=0$ 的理想更新为

\[
z_{k+1}=z_k-J_g(z_k)^{-1}g(z_k),
\qquad J_g(z)=\frac{\partial g}{\partial z}.
\]

但显式构造和求逆 $J_g$ 的代价通常不可接受。DEQ 使用 Broyden quasi-Newton 方法，用低秩更新维护 $J_g^{-1}$ 的近似。若 $B_k\approx J_g(z_k)^{-1}$，则更新形式为：

\[
z_{k+1}=z_k-\alpha_k B_k g_k,
\qquad g_k=g(z_k),
\]

其中 $\alpha_k$ 可理解为步长、阻尼或 line search 系数。令

\[
\Delta z_k=z_{k+1}-z_k,\qquad
\Delta g_k=g_{k+1}-g_k,
\]

若维护的是 Jacobian 近似 $A_k\approx J_g(z_k)$，常见 good Broyden 更新为：

\[
A_{k+1}
=
A_k+
\frac{(\Delta g_k-A_k\Delta z_k)\Delta z_k^\top}
{\Delta z_k^\top \Delta z_k}.
\]

论文实现上更关注 inverse-Jacobian 近似 $B_k\approx J_g^{-1}$，可用 Sherman-Morrison 型低秩更新避免矩阵求逆。其目标是满足 secant condition：

\[
B_{k+1}\Delta g_k\approx \Delta z_k .
\]

论文中初始化为

\[
B_0=-I .
\]

这是有数值直觉的：因为

\[
J_g=J_f-I .
\]

若初始阶段 $J_f$ 较小，则 $J_g\approx -I$，所以 $J_g^{-1}\approx -I$。此时一次 Newton-like 更新近似为

\[
z_{k+1}=z_k-(-I)(f(z_k)-z_k)=f(z_k),
\]

即退化为普通固定点迭代；随着 Broyden 更新积累曲率信息，它会比朴素迭代更快靠近平衡点。

Anderson acceleration 也是常见替代方案。它不显式近似 Jacobian，而是保留最近若干次残差 $r_i=f(z_i)-z_i$，通过小规模最小二乘组合历史迭代点，使新点残差尽量小。直觉上，朴素迭代只看当前方向，Broyden/Anderson 则利用历史残差信息估计局部非线性系统的几何结构，因此在隐式层上通常更快、更稳定。

### 3. 隐式微分：反向不穿过求根历史

DEQ 的关键公式来自平衡条件：

\[
g_\theta(z^\star,\theta,x)=f_\theta(z^\star,x)-z^\star=0 .
\]

对参数 $\theta$ 全微分：

\[
\frac{\partial g}{\partial z}\frac{d z^\star}{d\theta}
+
\frac{\partial g}{\partial \theta}
=0 .
\]

因此

\[
\frac{d z^\star}{d\theta}
=
-\left(\frac{\partial g}{\partial z}\right)^{-1}
\frac{\partial g}{\partial \theta}.
\]

由于

\[
\frac{\partial g}{\partial z}=J_f-I=-(I-J_f),
\qquad
\frac{\partial g}{\partial\theta}=\frac{\partial f_\theta}{\partial\theta},
\]

也可写成

\[
\frac{d z^\star}{d\theta}
=
(I-J_f)^{-1}
\frac{\partial f_\theta(z^\star,x)}{\partial\theta}.
\]

若损失为

\[
\ell=L(h(z^\star),y),
\]

则

\[
\frac{\partial \ell}{\partial \theta}
=
-\frac{\partial \ell}{\partial z^\star}
J_g^{-1}
\frac{\partial f_\theta(z^\star,x)}{\partial\theta}
=
\frac{\partial \ell}{\partial z^\star}
(I-J_f)^{-1}
\frac{\partial f_\theta(z^\star,x)}{\partial\theta}.
\]

这里最重要的工程含义是：反向传播不需要保存前向求根过程中的 $z_0,z_1,\ldots,z_k$，只需要平衡点 $z^\star$、输入 $x$ 和模块 $f_\theta$。这就是 DEQ 训练内存 $O(1)$ 的来源。

若 $\rho(J_f)<1$，则有 Neumann 展开：

\[
(I-J_f)^{-1}
=
\sum_{k=0}^{\infty}J_f^k .
\]

对应转置系统：

\[
(I-J_f^\top)^{-1}
=
\sum_{k=0}^{\infty}(J_f^\top)^k .
\]

这说明隐式梯度等价于“无限层反传”的闭式求和；谱半径小于 1 时级数收敛，梯度稳定。若 $\rho(J_f)$ 接近或大于 1，则求根和反向线性系统都会变难，表现为 Broyden 迭代数上升、残差下降慢、训练不稳定。

### 4. Jacobian-free 反向计算

实际反向不显式构造 $J_f$ 或 $J_g$。论文把核心项

\[
-\frac{\partial \ell}{\partial z^\star}J_g^{-1}
\]

改写为线性系统。设列向量 $u$ 满足

\[
J_g(z^\star)^\top u
+
\left(\frac{\partial \ell}{\partial z^\star}\right)^\top
=0 .
\]

等价地，

\[
(I-J_f(z^\star)^\top)u
=
\left(\frac{\partial \ell}{\partial z^\star}\right)^\top .
\]

解出 $u$ 后，参数梯度为一次 VJP：

\[
\frac{\partial \ell}{\partial\theta}
=
u^\top
\frac{\partial f_\theta(z^\star,x)}{\partial\theta}.
\]

代码心智模型是：

```text
forward:
    with no_grad:
        z_star = broyden(lambda z: f_theta(z, x) - z, z0)
    return z_star, but register implicit backward hook

backward:
    v = dL/dz_star
    solve u from (I - J_f(z_star)^T) u = v
    return grad_theta = VJP(f_theta(z_star, x), theta, u)
```

其中 $J_f^\top u$ 可由 autograd 的 vector-Jacobian product 得到；若需要 $J_f u$，也可由 JVP 得到。线性系统可用 Broyden、GMRES、fixed-point iteration 或截断 Neumann 级数近似：

\[
u_{m}
=
\sum_{k=0}^{m}(J_f^\top)^k v .
\]

这种计算是 matrix-free 的：只调用 $f_\theta$ 和自动微分提供的 JVP/VJP，不形成巨大 Jacobian。对长度 $T$、隐藏维度 $d$ 的序列，显式 Jacobian 尺寸约为 $(Td)\times(Td)$，不可行；matrix-free 只在向量尺度上工作。

### 5. DEQ-Transformer 与 Trellis 集成

DEQ 不规定 $f_\theta$ 的内部结构，只要求它把隐藏序列和输入序列映射回同形状隐藏序列。TrellisNet 实例中，输入注入为

\[
\tilde{x}_{1:T}=\operatorname{Conv1D}(x_{1:T};W_x),
\]

映射为

\[
f_\theta(z_{1:T};x_{1:T})
=
\psi\left(
\operatorname{Conv1D}([u,z_{1:T}];W_z)+\tilde{x}_{1:T}
\right),
\]

其中 $u$ 是历史 padding 或 zero padding，$\psi$ 通常是 LSTM-style gated activation。

DEQ-Transformer 中，$f_\theta$ 是权重共享的 self-attention block。论文写法可概括为：

\[
\tilde{x}_{1:T}=x_{1:T}W_x,
\]

\[
f_\theta(z_{1:T};x_{1:T})
=
\operatorname{LN}
\left(
\phi\left(
\operatorname{LN}
\left(
\operatorname{SelfAttention}(z_{1:T}W_{QKV}+\tilde{x}_{1:T};PE_{1:T})
\right)
\right)
\right).
\]

也就是说，隐藏状态 $z$ 生成 attention 的 $Q,K,V$，输入嵌入通过 input injection 加到注意力特征中，位置编码或 relative positional embedding 提供序列位置信息。求得平衡点后，模型输出使用

\[
\hat{y}_{1:T}=h(z^\star_{1:T}),
\]

其中 $h$ 是语言模型中的输出投影或分类头。

### 6. 稳定性、正则化与训练条件

DEQ 的数学理想条件是 $f_\theta$ 在相关区域内为 contraction：

\[
\|f_\theta(z_1,x)-f_\theta(z_2,x)\n\|\le c\|z_1-z_2\|,
\qquad 0<c<1 .
\]

Banach fixed-point theorem 保证不动点存在唯一，且朴素迭代收敛。局部线性化下，对应条件是

\[
\rho(J_f(z^\star))<1 .
\]

论文强调 $f_\theta$ 需要 stable and constrained，例如 TrellisNet 的 gating、Transformer 的 LayerNorm、weight normalization 都有助于控制输出范围和算子范数。更一般的 DEQ 训练还可加入 Jacobian regularization，例如 Frobenius penalty：

\[
\lambda\|J_f(z^\star)\|_F^2,
\]

或 spectral norm 约束，使 $J_f$ 的谱半径远离 1。weight tying 本身也有正则化效果：参数不会随深度增长，模型被迫学习一个可反复施加且仍稳定的变换。

### 7. 训练/推理伪代码流程

DEQ 推理流程：

```text
输入 x
初始化 z0 = 0 或上一段序列的平衡点
def g(z) = f_theta(z, x) - z
用 Broyden 求 z_star:
    while ||g(z)|| > eps and iter < max_iter:
        更新 z
        更新 inverse-Jacobian 近似 B
记录迭代次数、最终残差 ||g(z_star)||
输出 h(z_star)
```

DEQ 训练流程：

```text
前向:
    no_grad 下用 Broyden 解 g(z)=0
    得到 z_star
    只保存 z_star、x、theta 所需上下文

损失:
    loss = L(h(z_star), y)

反向:
    v = d loss / d z_star
    近似解 (I - J_f(z_star)^T) u = v
        可用 Broyden / GMRES / fixed-point / Neumann truncation
        J_f^T u 由 autograd VJP 提供
    用 u 对 f_theta(z_star, x) 做 VJP
    得到 theta 和 x 的梯度
```

数值注意点包括：$B_0=-I$ 的初始化、Broyden 步长阻尼或 line search、最大迭代数与容差 $\epsilon$ 的折中、训练时比推理时更严格的反向容差、长序列拆分为 subsequences、batch 内不同样本收敛速度不一致导致的 GPU 等待，以及 dropout 等随机扰动会让 equilibrium 更难求。

### 8. 与 JFNK/Newton-Krylov 的心智对应

DEQ 和 JFNK 的共同抽象都是：

\[
g(z)=0 .
\]

JFNK 通常外层使用 Newton：

\[
J_g(z_k)\Delta z_k=-g(z_k),
\qquad z_{k+1}=z_k+\Delta z_k,
\]

内层用 Krylov 方法近似解线性子问题，并用 Jacobian-vector product 避免显式形成 $J_g$。DEQ 论文中前向主要用 Broyden：它不解每一步 Newton 线性系统，而是用低秩 secant 更新近似 $J_g^{-1}$。两者的 matrix-free 精神一致：高维 Jacobian 不落地，只通过 $g(z)$、JVP 或 VJP 与向量相乘。

反向隐式微分中的

\[
(I-J_f^\top)u=v
\]

也正是一个线性 Krylov 子问题。若用 GMRES/CG-like 方法求它，DEQ 的 backward 就非常接近 Newton-Krylov 中的线性求解阶段。预条件在这里同样关键：好的 $B_0$、归一化、Jacobian regularization、历史低秩近似，都可理解为降低线性系统条件数。

从 PDE 角度看，DEQ 像一个稳态求解器。显式深层网络对应时间步进：

\[
z_{k+1}=f_\theta(z_k,x),
\]

DEQ 直接求稳态：

\[
\frac{dz}{dt}=f_\theta(z,x)-z=0 .
\]

这和隐式欧拉、稳态 CFD、非线性椭圆方程求解很像：前向是非线性残差求根，反向是伴随/隐式微分线性系统。可微根求解因此可用于物理仿真中的隐式时间步进、稳态流体、结构平衡、化学反应平衡和 equilibrium networks：只要模拟器输出由非线性方程定义，就可以通过隐式微分避免展开求解轨迹。

### 9. 与库内相关论文的关联

- `numerical-computation/jacobian-free-newton-krylov-methods-a-survey-of-approaches-and-applications.md`：这是 DEQ 最直接的数值算法对应。JFNK 的 Newton-Krylov、Jacobian-free JVP、预条件、非线性残差求解，分别对应 DEQ 的前向 root finding、反向隐式线性系统、Broyden inverse approximation 与稳定训练。

- `ai-for-physics/physics-informed-neural-networks-a-deep-learning-framework-for-solving-forward-a.md`：PINN 通过 PDE 残差训练网络，DEQ 则把网络层本身定义为残差方程 $g(z)=0$ 的解。二者都把学习问题和非线性方程残差耦合起来，但 PINN 的残差多在损失里，DEQ 的残差直接定义模型前向。

- `ai-model/denoising-diffusion-probabilistic-models.md`：扩散模型反向过程是离散步进或 ODE/SDE 求解，DEQ 是不动点/稳态求解。二者都把深度网络与数值求解器连接起来：扩散强调沿时间轨迹积分，DEQ 强调直接求 equilibrium。

- `ai-theory/neural-tangent-kernel-convergence-and-generalization-in-neural-networks.md`：DEQ 的训练稳定性与 $J_f$ 的谱性质密切相关；NTK 关注训练动力学的核化极限与谱条件。隐式层中的 $(I-J_f)^{-1}$ 会放大或抑制梯度，是分析 DEQ 泛化和收敛时绕不开的谱对象。

- `ai-theory/geometric-deep-learning-grids-groups-graphs-geodesics-and-gauges.md`：图神经网络中的 message passing 也可视为反复传播直到平衡。DEQ 思路自然对应图上的不动点传播、label propagation、能量最小化和 equivariant implicit layers。

- `HPC/` 下 AMReX、Berger-Colella AMR 等：AMR、多重网格、隐式时间步进和稳态求解器关心的是如何在大规模网格上高效解非线性/线性系统。DEQ 的隐式微分线性系统与这些 HPC 求解器中的 Krylov、multigrid、preconditioning 有直接工程类比：深度学习的“层”可被看成可微数值求解器接口。

因此，DEQ 位于“深度学习与隐式 PDE 求解器共同接口”的核心位置：它把神经网络层改写为非线性方程，把反向传播改写为伴随线性系统，把模型深度改写为数值收敛精度。这使得神经网络架构、root solver、Jacobian-free 自动微分和物理仿真求解器可以在同一套语言下讨论。

## Review Questions

> ⚠️ **Kimi review 未完成（上游故障）**：2026-08-04 23:57 起 zxcs99.cn 全模型不可用，重试仍失败；以下 3 问由 JARVIS 按 skill 要求自行补充（2026-08-04）。

1. 把 DEQ 用于物理仿真（隐式时间步进/稳态 PDE）时，$(I-J_f)^{-1}$ 的谱条件与物理刚性直接相关：高 Reynolds 数/快速化学反应等刚性问题的 $J_f$ 谱半径接近或超过 1，Broyden/Neumann 方法的收敛与梯度稳定性如何保障？能否借鉴 JFNK 的预条件（如 multigrid、物理算子分裂）改善隐式层的条件数？
2. DEQ 的隐式微分与可微仿真中的伴随法（adjoint method）在数学上是同一对象（都解伴随线性系统），但前者用 autograd VJP、后者常用手写伴随方程——在“学习 PDE 稳态解”的框架下（如 equilibrium 作为隐式层的 Neural Operator/物理网络），哪种梯度估计在噪声/不精确求解下更鲁棒？
3. 对库内 PINN/物理约束网络：能否把 PDE 求解器（如稳态 NS 的 Newton-Krylov 迭代）包装成 DEQ 式隐式层并端到端学习边界条件/参数？其可微性与收敛保证（不动点唯一性、谱半径约束）对训练稳定性意味着什么，与直接 PINN 残差训练相比优劣如何？
