# Hamiltonian Neural Networks

**arXiv:** [1906.01563](https://arxiv.org/abs/1906.01563)
**会议：** NeurIPS 2019

**Source PDF:** `NeurIPS-2019-hamiltonian-neural-networks-Paper.pdf`
**阅读状态：** 🔬 精读
**流程状态：** ①元数据 ✓ | ②初稿 ✓ | ③评估 ✓(精读) | ④补充 ✓ | ⑤索引 ⏳ | ⑥review ✓ | ⑦提交 ⏳

---

## 摘要

本文提出 Hamiltonian 神经网络（HNN），通过学习系统的 Hamiltonian 函数而非直接拟合状态导数，保证学习到的动力学满足能量守恒。在理想弹簧、摆、三体问题等物理系统上，HNN 相比标准神经网络在长时间预测中显着降低了能量漂移。

## 结论

HNN 通过将 Hamiltonian 力学的辛结构和能量守恒先验嵌入神经网络，实现了数据驱动的物理守恒律学习，为物理约束学习提供了新范式。

## 价值评估

Doctor 指定精读（学习路线规划推荐）。HNN 是 AI4Physics 中把 Hamiltonian 结构直接写入神经网络归纳偏置的代表性工作。它的价值不在于网络规模，而在于展示了“学习能量泛函，再由几何结构生成动力学”的范式，非常贴近几何力学、守恒数值方法和可解释物理学习。

## 公式与代码梳理

### 数学结构与核心公式

经典 Hamiltonian 系统以正则坐标 $x=(q,p)$ 表示：

$$
\frac{d}{dt}
\begin{pmatrix}
q\\
p
\end{pmatrix}
=
\begin{pmatrix}
0 & I\\
-I & 0
\end{pmatrix}
\nabla H(q,p)
=J\nabla H(q,p).
$$

展开即 Hamilton 方程：

$$
\dot{q}=\frac{\partial H}{\partial p},\qquad
\dot{p}=-\frac{\partial H}{\partial q}.
$$

HNN 用神经网络 $H_\theta(q,p)$ 参数化 Hamiltonian，而不是直接学习向量场 $f_\theta(q,p)\approx \dot{x}$。预测的动力学为

$$
\dot{x}_\theta = J\nabla_x H_\theta(x).
$$

训练损失比较观测导数与由 Hamiltonian 梯度生成的导数：

$$
\mathcal{L}_{\mathrm{HNN}}
=\left\|
\frac{dx}{dt}
-J\nabla_x H_\theta(x)
\right\|_2^2.
$$

由于 $J$ 反对称，沿模型轨道有

$$
\frac{dH_\theta}{dt}
=\nabla H_\theta^\top J\nabla H_\theta=0.
$$

这在连续时间模型层面解释了 HNN 为什么在无耗散系统中比普通 MLP 更能抑制长期能量漂移：能量守恒来自网络输出结构，而不是损失函数中的软惩罚（实际数值积分时需配合辛积分器才能在离散轨道上近似保持能量）。

论文还讨论了非正则坐标或只观测部分变量时的扩展：若输入不是标准 $(q,p)$，需要学习或指定坐标变换，否则 $J\nabla H$ 的结构假设可能失配。

### 关键推导/算法

1. 收集轨迹样本 $x(t)$，用数值差分或模拟器得到监督信号 $\dot{x}(t)$。
2. 前向传播得到标量 $H_\theta(x)$。
3. 用自动微分计算 $\nabla_x H_\theta(x)$。
4. 左乘固定辛矩阵 $J$ 得到 $\dot{x}_\theta$。
5. 最小化 $\|\dot{x}-\dot{x}_\theta\|^2$，而不是最小化下一步状态误差。
6. 推理阶段将 $\dot{x}_\theta=J\nabla H_\theta(x)$ 交给 ODE integrator，生成长时间轨迹。

伪代码结构：

```text
for batch x, xdot:
    H = neural_scalar(x)
    gradH = autograd(H, x)
    xdot_pred = J @ gradH
    loss = mean_square(xdot - xdot_pred)
    update(theta)
```

实现重点是让网络输出标量能量，并保证 autograd 对输入求导；这与普通 residual network 直接输出向量场有本质区别。

### 对 HPC 框架的启示

1. 框架中的物理学习模块应支持“标量泛函 + 几何算子”的组合，而不是只支持黑箱 RHS。
2. 对 Hamiltonian PDE，可把离散能量 $H_h$、Poisson 矩阵/算子 $J_h$ 和时间积分器解耦，方便替换神经近似的闭合项。
3. 自动微分是结构学习的关键基础设施；HPC 代码若希望接入 AI4Physics，需要清晰区分对状态求导、对参数求导和对网格/几何求导。
4. HNN 提醒我们：长期预测误差常来自结构错误而非单步拟合误差，benchmark 应包含能量漂移和相空间几何诊断。
5. 对有耗散或外力的流体系统，不能硬套 HNN；应扩展为 GENERIC、metriplectic 或 port-Hamiltonian 结构。

### 待深入研究的问题

1. 如何把 HNN 从有限维 ODE 推广到非正则 Poisson PDE，例如不可压 Euler 或 Vlasov 系统？
2. 当训练数据来自非辛数值积分器时，HNN 学到的是物理 Hamiltonian 还是数值修正 Hamiltonian？
3. 对量子涡/GPE 系统，是否可以学习能量泛函中的未知闭合项，同时保持相位规范对称性和粒子数守恒？

## Review Questions

1. HNN 中 $J\nabla H_\theta$ 的结构为什么自动保证模型能量守恒？如果 $J$ 依赖状态变量或存在 Casimir，这一论证需要怎样修改？
2. 对 Hamiltonian PDE 离散系统，学习 $H_h$ 与学习连续 $H$ 后再离散化分别有什么优缺点？它们对 HPC 框架中的网格无关性有何影响？
3. 在流体和量子涡问题中，真实系统常含耗散、驱动或拓扑事件。HNN 应如何与耗散结构、事件检测和守恒投影结合？
