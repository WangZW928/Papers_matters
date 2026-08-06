# Schrödinger's Smoke

**作者：** Albert Chern, Felix Knöppel, Ulrich Pinkall, Peter Schröder, Steffen Weißmann

**DOI：** [http:](https://doi.org/http:)

**源 PDF：** `SchrodingersSmoke.pdf`

**阅读状态：** 🔬 精读
**流程状态：** ①元数据 ✓ | ②初稿 ✓ | ③评估 ✓(精读) | ④补充 ✓ | ⑤索引 ✓ | ⑥review ✓ | ⑦提交 ⏳

---

## 摘要

### 中文翻译

本文提出 Schrödinger's Smoke：把不可压流体状态表示为 C² 波函数，速度由 Berry connection 恢复，压力投影对应相位/gauge 修正，涡旋结构由波函数相位缺陷（涡丝）自然表达。时间步进为酉 Schrödinger 演化 + 归一化 + 投影，无需显式追踪涡线拓扑。

## 价值评估

**Doctor 指定精读。** 按 6 级标准，这篇应按 **5/6：高优先级精读** 处理：idea 极清晰，把不可压流体状态表示为 $\mathbb C^2$ 波函数并用 Schrödinger 演化处理涡结构；计算结果强，图形学案例展示了细涡结构、涡丝相互作用和障碍物烟流；预言能力偏中等，主要目标是稳定视觉模拟而非严格 DNS；方法新颖性很高，连接 Madelung、Landau-Lifshitz 能量、Clebsch/spin map 与 FFT projection；来源为 ACM TOG/SIGGRAPH 2016。精读判断：它与 `Madelung transform`、`Clebsch Maps`、量子涡/GPE 和结构保持 HPC 流体求解高度相关。另需校正文档元数据：正确 DOI 是 `10.1145/2897824.2925868`，论文主页也给出 ACM TOG 35(4), Article 77, 2016。

## 公式与代码梳理

#### 数学结构与核心公式

本文的状态变量不是速度 $u$ 或涡量 $\omega$，而是二分量复波函数

$$
\Psi=(\psi_1,\psi_2)^T\in\mathbb C^2,\qquad \Psi^\dagger\Psi=1 .
$$

这里 $\dagger$ 表示 Hermitian transpose。速度一形式由 Berry connection 给出：

$$
u=\hbar\,\operatorname{Im}(\Psi^\dagger d\Psi).
$$

在向量记号中，

$$
\mathbf u=\hbar\,\operatorname{Im}(\Psi^\dagger\nabla\Psi).
$$

若做局部相位变换

$$
\Psi\mapsto e^{-i\phi/\hbar}\Psi,
$$

则速度变为

$$
\mathbf u\mapsto \mathbf u-\nabla\phi .
$$

这正好对应不可压投影中的 pressure/gauge correction。不可压约束为

$$
\nabla\cdot\mathbf u=0,\qquad |\Psi|^2=1 .
$$

波函数还定义一个 spin map

$$
\mathbf S=\Psi^\dagger\boldsymbol\sigma\Psi\in S^2,
$$

其中 $\boldsymbol\sigma=(\sigma_1,\sigma_2,\sigma_3)$ 是 Pauli 矩阵。涡量二形式可由 $\mathbf S$ 的球面面积形式 pullback 表示；向量形式可写作

$$
\boldsymbol\omega
=\nabla\times\mathbf u
=\frac{\hbar}{2}\epsilon_{abc}S_a\nabla S_b\times\nabla S_c .
$$

这与 `Clebsch Maps` 中的球面 Clebsch map 是同一个几何机制：涡线是 $\mathbf S:M\to S^2$ 的等值线，涡管是球面区域的原像。

能量结构由两部分组成。第一部分是不可压流体动能：

$$
E_{\rm kin}=\frac12\int_M|\mathbf u|^2\,dV .
$$

第二部分是 Landau-Lifshitz 型 spin 能量：

$$
E_{\rm LL}=\frac{\hbar^2}{4}\int_M|\nabla\mathbf S|^2\,dV .
$$

总能量可理解为

$$
E[\Psi]=E_{\rm kin}+E_{\rm LL}.
$$

$E_{\rm LL}$ 对细涡丝很重要：它给 spin map 的空间变化惩罚，相当于为涡管核心提供可解析的宽度尺度，避免涡量在网格上被普通速度平流抹掉。

时间推进采用 splitting。自由 Schrödinger 步可写为

$$
i\hbar\partial_t\Psi=-\frac{\hbar^2}{2}\Delta\Psi .
$$

在周期盒上，Fourier 模式满足

$$
\widehat\Psi_{\mathbf k}(t+\Delta t)
=\exp\left(-i\frac{\hbar|\mathbf k|^2}{2}\Delta t\right)\widehat\Psi_{\mathbf k}(t).
$$

所以代码上是 FFT、逐模相位乘法、inverse FFT。随后做归一化

$$
\Psi\leftarrow\frac{\Psi}{|\Psi|}
$$

保持 $\Psi^\dagger\Psi=1$。再做不可压投影：先由 $\Psi$ 计算 $\mathbf u$，解

$$
\Delta\phi=\nabla\cdot\mathbf u,
$$

再更新

$$
\Psi\leftarrow e^{-i\phi/\hbar}\Psi,\qquad
\mathbf u\leftarrow\mathbf u-\nabla\phi .
$$

障碍物可通过 penalty 或 mask 处理，把固体内部速度约束为目标边界速度。其本质仍是相位/gauge 修正，只是 Poisson 或 Helmholtz 问题带有障碍物系数。

#### 关键推导

第一步是 Berry connection 到不可压投影。由

$$
\mathbf u=\hbar\operatorname{Im}(\Psi^\dagger\nabla\Psi)
$$

和 $\Psi' = e^{-i\phi/\hbar}\Psi$，有

$$
\nabla\Psi'=e^{-i\phi/\hbar}\left(\nabla\Psi-\frac{i}{\hbar}\Psi\nabla\phi\right).
$$

因此

$$
{\Psi'}^\dagger\nabla\Psi'
=\Psi^\dagger\nabla\Psi-\frac{i}{\hbar}\nabla\phi .
$$

取虚部并乘以 $\hbar$ 得到

$$
\mathbf u'=\mathbf u-\nabla\phi .
$$

令 $\nabla\cdot\mathbf u'=0$，就得到 Poisson 方程 $\Delta\phi=\nabla\cdot\mathbf u$。这说明 incompressible projection 在波函数表象里只是相位规范变换。

第二步是 spin map 与涡量。$u=\hbar\operatorname{Im}(\Psi^\dagger d\Psi)$ 是 Hopf fibration 上的联络一形式。取外微分：

$$
du=\frac{\hbar}{2}\mathbf S^*dA_{S^2}.
$$

在三维中经 Hodge 对偶得到

$$
\nabla\times\mathbf u
=\frac{\hbar}{2}\epsilon_{abc}S_a\nabla S_b\times\nabla S_c .
$$

因此涡量不是从速度差分中被动恢复，而是由 $S^2$ 值映射的面积拉回给出。相位奇点和 spin map 拓扑自然编码涡丝。

第三步是 Schrödinger 步为什么适合 FFT。自由 Schrödinger 方程在 Fourier 空间对角化：

$$
i\hbar\partial_t\widehat\Psi_{\mathbf k}
=\frac{\hbar^2}{2}|\mathbf k|^2\widehat\Psi_{\mathbf k}.
$$

所以精确时间步为纯相位旋转。该步是酉的，保持 $L^2$ 范数；归一化和投影再把状态拉回 $|\Psi|=1$、$\nabla\cdot u=0$ 的约束流形。这解释了算法稳定性的主要来源（整体分裂格式的稳定性还依赖子步间的相容性）。

#### 对 HPC 框架的启示

这篇对 Doctor 的框架价值很直接：它把涡动力学从“速度-压力 PDE”转成“复波函数 + FFT + 投影”的算子链。对于周期域或规则盒，核心 kernel 是 FFT、spectral Laplacian、pointwise normalization、Pauli spin reconstruction、Poisson projection，非常适合 GPU 和多节点 FFT。对非周期/复杂边界，需要把 FFT 换成 Helmholtz/Poisson solver，或用嵌入边界 mask 与 penalty。

与 `Madelung Transform as a Momentum Map` 的关系是：Madelung 把标量波函数映到密度和势速度，而 Schrödinger's Smoke 用 $\mathbb C^2$ spinor 处理有涡量的不可压流。标量 Madelung 在多值相位和非零涡量处会遇到奇点；二分量 spinor 通过 Hopf fibration 给出更强的涡拓扑表达。与 `Clebsch Maps` 的关系更近：后者把 $\psi:M\to S^3$ 和 $s:M\to S^2$ 用于涡结构可视化，本文把类似结构变成时间演化求解器。

对 AI4Physics，可把 $\Psi$ 作为学习变量而不是 $\mathbf u$。神经算子若直接学习速度，容易损失 $\nabla\cdot u=0$ 和涡线拓扑；若学习 spinor 或 spin map，再由固定公式恢复速度/涡量，结构约束更硬。DDPM/score-based 模型也可在 $\Psi$ 或 $\mathbf S$ 空间生成涡结构，但必须处理 $|\Psi|=1$ 和 $U(1)$ gauge 冗余。

#### 待深入研究

1. $\hbar$ 同时控制涡核尺度和 Schrödinger 色散尺度；如何在 AMR 中随网格层级自适应选择 $\hbar$，避免涡核过宽或欠解析？
2. 对非周期边界，FFT 优势减弱；是否可用 matrix-free Helmholtz/Poisson、AMG 或 JFNK 保持投影效率？
3. 波函数表示自然允许重联，但经典 Euler 涡线冻结不允许无黏重联；如何区分数值重联、物理黏性重联和量子/GPE 型重联？

## Review Questions

1. Schrödinger's Smoke 的 $\mathbb C^2$ spinor 表示相比标量 Madelung 变量，究竟多编码了哪些涡拓扑自由度？
2. 若把该方法嵌入 AMR/GPU 框架，FFT splitting、projection、障碍物 penalty 哪一步最容易破坏 Hamiltonian 或 gauge 结构？
3. 能否训练等变神经算子直接预测 $\Psi$ 的短时演化，同时用固定 Berry connection 恢复 $\mathbf u$，从而保证不可压和涡量结构？

4. 该方法中的 `U(1)` gauge、点态单位范数约束与不可压投影之间，哪个才是真正承载流体几何结构的核心约束？
5. 对非周期域和固壁边界，如何构造既保留 Berry connection 解释、又不破坏投影结构的离散 Schrödinger 步？
6. 若把 `\Psi` 作为 AI4Physics 的学习变量，怎样处理 gauge 冗余，避免网络学到物理等价但数值不稳定的表示？

---

---
