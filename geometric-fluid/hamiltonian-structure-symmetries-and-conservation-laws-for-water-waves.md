# Hamiltonian structure, symmetries and conservation laws for water waves

**Authors:** T. Brooke Benjamin and P. J. Olver

**DOI:** [10.1017/S0022112082003292](https://doi.org/10.1017/S0022112082003292)

**Source PDF:** `hamiltonian-structure-symmetries-and-conservation-laws-for-water-waves.pdf`
**阅读状态：** 🔬 精读
**流程状态：** ①元数据 ✓ | ②初稿 ✓ | ③评估 ✓(精读) | ④补充 ✓ | ⑤索引 ⏳ | ⑥review ✓ | ⑦提交 ⏳

---

## 摘要

本文系统研究了水波方程的哈密顿结构、对称性与守恒律之间的关系。通过将水波问题表述为无穷维哈密顿系统，作者利用变分原理和Lie群方法，严格推导了水波方程所对应的一族守恒律（如质量、动量、能量及高阶不变量），并揭示了这些守恒律与方程对称性之间的内在联系。关键结果包括：建立了水波方程在哈密顿框架下的系统的对称性与守恒律分析，并证明了某些守恒律对应于特定的时空对称性。

## 结论

本文的主要结论是：水波方程具有丰富的哈密顿结构和无穷维对称性，这些对称性直接导致了多个独立的守恒律，从而为水波问题的可积性和稳定性分析提供了严格的数学基础。

## 价值评估

Doctor 指定精读（学习路线规划推荐）。本文是把完整自由边界水波问题放入 Hamiltonian/Noether 框架的经典论文，对理解几何流体中的正则变量、对称群、守恒量以及近似模型应保留哪些结构具有基础价值。对 Doctor 的方向而言，它比单纯水波模型更重要的是其“从变分结构到可计算守恒诊断”的方法论。

## 公式与代码梳理

### 数学结构与核心公式

水波问题考虑理想、不可压、无旋流体。速度势 $\phi$ 在流体区域内满足

$$
\Delta \phi = 0,
$$

自由面可写成 $y=\eta(x,t)$，表面势为

$$
\xi(x,t)=\phi(x,\eta(x,t),t).
$$

在 Zakharov 变量 $(\eta,\xi)$ 中，水波系统具有正则 Hamiltonian 形式

$$
\eta_t = \frac{\delta H}{\delta \xi}, \qquad
\xi_t = -\frac{\delta H}{\delta \eta}.
$$

其数学含义是：自由面高度 $\eta$ 与表面速度势 $\xi$ 是一对正则共轭变量，水波演化不是任意自由边界 PDE，而是由总能量泛函 $H$ 生成的无穷维 Hamiltonian 流。

用 Dirichlet-Neumann 算子 $G(\eta)$ 表示流体域内 Laplace 问题对自由面的法向导数映射时，Hamiltonian 可写为

$$
H(\eta,\xi)
=\frac{1}{2}\int \xi\,G(\eta)\xi\,dx
+\frac{g}{2}\int \eta^2\,dx
+\sigma\int\left(\sqrt{1+|\nabla\eta|^2}-1\right)dx.
$$

三项分别是动能、重力势能和表面张力能。若不考虑表面张力，则令 $\sigma=0$。这个表达式的关键点是：体内势流自由边界问题被压缩为自由面上的非局部 Hamiltonian 系统，非局部性全部进入 $G(\eta)$。

Poisson 括号对应正则辛结构：

$$
\{F,G\}
=\int\left(
\frac{\delta F}{\delta \eta}\frac{\delta G}{\delta \xi}
-\frac{\delta F}{\delta \xi}\frac{\delta G}{\delta \eta}
\right)dx.
$$

于是任意泛函 $F$ 的演化满足

$$
\frac{dF}{dt}=\{F,H\}.
$$

对称性与守恒律通过 Hamiltonian 版 Noether 定理联系起来：若一参数变换生成元 $X$ 保持 Hamiltonian 结构并使 $H$ 不变，则存在相应守恒量。典型守恒量包括质量/体积 $\int \eta\,dx$、能量 $H$、水平动量（自由面变量中常写成 $\int \xi\nabla\eta\,dx$ 的等价形式）以及由空间旋转、时间平移、Galilean 变换等产生的量。论文的重要贡献不是发明一个单一公式，而是系统分类完整水波问题的允许对称性，并解释每类守恒量的物理含义。

### 关键推导/算法

For a graph free surface take \(\Omega_\eta=\{(x,y):-h<y<\eta(x)\}\), impose \(\partial_n\phi=0\) at a rigid bottom (or decay at infinite depth), and define
\[
G(\eta)\xi=\sqrt{1+|\nabla\eta|^2}\,\partial_n\phi\big|_{y=\eta}.
\]
Green's identity gives \(\int_{\Omega_\eta}|\nabla\phi|^2=\int\xi G(\eta)\xi\,dx\), explaining both the kinetic term and the self-adjoint nonnegative character of \(G(\eta)\). At fixed \(\eta\), \(\delta_\xi H=\int\delta\xi\,G(\eta)\xi\,dx\), so \(\eta_t=G(\eta)\xi\) is the kinematic condition. The shape derivative \(-\delta H/\delta\eta=\xi_t\) is Bernoulli's condition in graph coordinates; its component formula depends on the normal/sign convention. This also states the boundary assumptions under which the canonical reduction is valid.

1. 建立势流自由边界问题：体内 Laplace 方程，加上自由面运动学条件、动力学 Bernoulli 条件、底边界条件和表面张力项。
2. 选取自由面变量 $(\eta,\xi)$，将体内势函数由边界数据唯一确定，从而把问题化为自由面上的 Hamiltonian 演化。
3. 用变分导数计算 $\delta H/\delta \xi$ 与 $\delta H/\delta \eta$，验证它们恢复运动学与动力学自由面边界条件。
4. 构造水波方程的无穷维相空间和正则 Poisson 括号。
5. 对候选时空变换做无穷小生成元分析，筛选保持方程、边界条件和 Hamiltonian 结构的对称群。
6. 对每个一参数对称群应用广义 Noether 定理，得到对应守恒量，再回到流体变量解释其物理意义。

可计算化时，最核心的算法对象是 $G(\eta)$：数值框架需要在每个时间步求解体内 Laplace 边值问题，或用边界积分/谱方法近似 Dirichlet-Neumann 算子，然后通过辛时间推进保持 Hamiltonian 结构。

### 对 HPC 框架的启示

1. 自由边界 PDE 的核心瓶颈常常是隐式几何算子（如 $G(\eta)$），框架需要把“几何更新”和“椭圆子问题求解”设计成一等公民。
2. Hamiltonian 结构提供了比局部残差更强的回归测试：能量、动量、质量漂移应作为长期模拟的标准诊断量。
3. 对称性分类可以反向指导离散化：网格、边界处理和时间积分如果破坏平移/旋转/Galilean 对称性，就会直接污染相应守恒量。
4. 非局部自由面算子适合抽象为 matrix-free operator，便于在谱法、边界元、FEM 和 GPU 后端之间复用时间推进器。
5. 对水波、Euler、MHD 等几何流体系统，框架 API 应显式表达变量配对、Poisson 结构和守恒泛函，而不仅是 RHS 回调。

### 待深入研究的问题

1. 如何为非平坦自由面上的 Dirichlet-Neumann 算子构造高阶、GPU 友好且保持离散对称性的近似？
2. 对波破碎这类光滑 Hamiltonian 演化终止现象，能否设计兼容结构守恒与拓扑变化的数值事件处理？
3. 是否能把 Noether 守恒量自动生成机制嵌入 Doctor 的 PDE DSL，用于自动产生 diagnostics 与 structure-preserving tests？

## Review Questions

1. 在自由面变量 $(\eta,\xi)$ 中，Dirichlet-Neumann 算子 $G(\eta)$ 承担了哪些几何信息？若离散 $G(\eta)$ 不自伴，会怎样破坏 Hamiltonian 结构和能量守恒？
2. Benjamin-Olver 的 Noether 分析如何帮助判断一个近似水波模型是否“结构可信”？对长波、浅水或弱非线性模型应检查哪些对称性和守恒量？
3. 若将该框架推广到有涡量流体或量子涡自由边界问题，正则 Poisson 结构会遇到哪些障碍？是否需要非正则 Poisson 括号或 Casimir 约束？
