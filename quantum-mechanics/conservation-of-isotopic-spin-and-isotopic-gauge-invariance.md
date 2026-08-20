# 同位旋守恒与同位规范不变性

# Conservation of Isotopic Spin and Isotopic Gauge Invariance

**作者：** C. N. Yang（杨振宁）, R. L. Mills（米尔斯）
**期刊：** Physical Review 96, 191–195 (1954)
**DOI：** [https://doi.org/10.1103/PhysRev.96.191](https://doi.org/10.1103/PhysRev.96.191)
**arXiv：** 无（1954 年 APS 论文，全文取自 harvest.aps.org PDF）
**阅读状态：** 🔬 精读（Doctor 指定）
**流程状态：** ①元数据 ✓ | ②初稿 ✓ | ③评估 ✓(精读) | ④补充 ✓ | ⑤索引 ⏳ | ⑥review ✓ | ⑦提交 ⏳

---

## 摘要

### 中文翻译
本文指出：通常的同位旋旋转不变性原理与局域场（localized fields）的概念不相容。文章探索了在局域同位旋旋转下保持不变的可能性，由此提出同位规范不变性（isotopic gauge invariance）原理，并预言存在一个 b 场——它与同位旋的关系，正如电磁场与电荷的关系。b 场满足非线性微分方程。b 场的量子是自旋为 1、同位旋为 1、电荷为 ±e 或 0 的粒子。

### 原文
> It is pointed out that the usual principle of invariance under isotopic spin rotation is not consistant with the concept of localized fields. The possibility is explored of having invariance under local isotopic spin rotations. This leads to formulating a principle of isotopic gauge invariance and the existence of a b field which has the same relation to the isotopic spin that the electromagnetic field has to the electric charge. The b field satisfies nonlinear differential equations. The quanta of the b field are particles with spin unity, isotopic spin unity, and electric charge ±e or zero.

---

## 文章总结

### 1. 解决什么问题？
20 世纪 50 年代初，同位旋守恒已被实验充分支持（p-p 与 n-p 相互作用的近似相等、π 介子的三种电荷态等），其数学表述是相互作用在全局同位旋旋转（SU(2)，与电荷无关的常数旋转）下不变。但作者指出：**全局对称性与局域场的概念不相容**——若相互作用是局域的（定域场论），那么在一个时空点做同位旋旋转、在另一个点做不同旋转，物理应当不受影响（局域场的因果结构与定域性要求）。电磁学提供了先例：电荷守恒与规范不变性（相位旋转）相关，而电磁规范变换可以局域化——这正是通过引入电磁场 A_μ 实现的。问题：**能否把同位旋旋转也局域化？需要引入什么样的新场？**

### 2. 用了什么方法论？
1. **类比电磁学**：电荷守恒 ↔ 整体相位旋转 U(1)；同位旋守恒 ↔ 整体同位旋旋转 SU(2)。电磁理论中让旋转局域化（相位依赖时空点）→ 必须引入矢量场 A_μ 与协变导数 ∂_μ − ieA_μ。把同一逻辑搬到同位旋：让同位旋旋转依赖时空点 → 必须引入矢量场 b_μ（同位旋三重态，三个分量 b_μ¹, b_μ², b_μ³），构造同位协变导数。
2. **局域规范原理**：要求拉氏量在局域同位旋旋转下不变。由于导数项会破坏局域不变性，需用协变导数替换普通导数；协变导数中含 b 场，且 b 场本身必须按非平凡方式变换（吸收旋转的空间导数项）。
3. **场强与非线性**：定义同位场强张量 f_μν = ∂_μb_ν − ∂_νb_μ − 2εb_μ×b_ν（含非线性项），它按同位规范变换协变地变换。由此 b 场满足非线性微分方程（与 Maxwell 方程的线性形成鲜明对比）——非线性来自 b 场自身携带同位旋荷（自相互作用）。
4. **守恒流**：总流 j_μ = J_μ + 2ε b_μ×f_μν（物质流 + b 场自身贡献），满足连续性方程，保证总同位旋守恒在局域理论中依然成立。

### 3. 主要结论是什么？
- **局域同位旋不变性 → 必须存在 b 场**：这是规范原理的第一个非阿贝尔例子——对称性的局域化自动"催生"传递相互作用的规范场。
- **b 场量子性质**：自旋 1、同位旋 1、电荷 ±e 或 0（三个分量对应同位旋三重态：两个带电 + 一个中性，类比 π 介子三重态）。
- **b 场方程是非线性的**：因为 b 场自身携带同位旋荷，方程含 b_μ×b_ν 项——这是与电磁场的本质区别（光子不带电荷，Maxwell 方程线性）。
- **质量问题的悬而未决**：作者尝试在拉氏量中加入 b 场质量项，但发现质量项会破坏规范不变性（局域旋转下质量项无法保持不变），最终未能确定 b 量子质量。文中坦承：无法断定 b 量子质量，而这是与实验对照的关键（质量必须大于 π 介子，否则会被大量产生而早该被观测到）。
- **历史意义**：这是非阿贝尔规范场论的开山之作，直接催生 20 年后的电弱统一（Weinberg-Salam，SU(2)×U(1)）与量子色动力学（QCD，SU(3) 色规范），也是"局域对称性决定相互作用形式"这一现代粒子物理核心思想的源头。文中关于质量问题的困难后来由 Higgs 机制（对称性自发破缺 + 规范场获得质量）解决。

---

## 价值评估

Doctor 指定精读（跳过 Codex 价值评估）。

## 公式与代码梳理

### 1. 从 global isotopic spin 到 local gauge invariance

Yang 和 Mills 的起点不是数学抽象，而是核物理经验事实：Heisenberg 1932 年把质子、 neutron 看成同一 nucleon 的两个 charge states；Breit、Condon、Present 1936 年指出 $p-p$ 与 $n-p$ 相互作用近似相同；Wigner 1937 年引入 total isotopic spin $T$。这些经验被整理为：强相互作用在同位旋空间的 $SU(2)$ 旋转下不变。

通常的 isotopic spin conservation 只要求 global rotation：

\[
\psi(x)\mapsto \psi'(x)=S\psi(x),\qquad S\in SU(2)
\]

其中 $S$ 与时空点无关。但 Yang 和 Mills 指出，这与 localized field concept 有张力：如果同位旋方向本身只是命名约定，那么为什么只能在全宇宙一次性选定 proton/neutron 方向，而不能在每个时空点独立选择？

于是他们要求更强的 local isotopic gauge invariance：

\[
\psi(x)\mapsto \psi'(x)=S(x)\psi(x),\qquad S(x)\in SU(2)
\]

问题随即出现：普通导数不协变，因为

\[
\partial_\mu \psi'(x)
=
S(x)\partial_\mu\psi(x)+(\partial_\mu S(x))\psi(x)
\]

多出的 $(\partial_\mu S)\psi$ 项破坏了不变性。这正是电磁规范不变性中 $\partial_\mu-ieA_\mu$ 的非阿贝尔推广动机。

### 2. Covariant Derivative 与 $b_\mu$ 场

类比 QED 中

\[
\partial_\mu \rightarrow \partial_\mu-ieA_\mu
\]

Yang 和 Mills 引入同位旋规范场 $\mathbf b_\mu$。对任意同位旋表示 $T^a$，协变导数写作

\[
D_\mu
=
\partial_\mu-2i\epsilon\,\mathbf b_\mu\cdot\mathbf T
\]

对 nucleon doublet，即 isotopic spin $1/2$ 表示，$T^a=\tau^a/2$，所以

\[
D_\mu\psi
=
\left(\partial_\mu-i\epsilon\,\boldsymbol{\tau}\cdot\mathbf b_\mu\right)\psi
\]

这里 $\epsilon$ 是文中的耦合常数；OCR 中有时会误成 $e$。$\mathbf b_\mu$ 是同位旋空间三维向量：

\[
\mathbf b_\mu=(b_\mu^1,b_\mu^2,b_\mu^3)
\]

因此它不是一个单独的 photon-like 场，而是三个 spin-1 vector fields，构成 isotopic spin triplet。

文中先写矩阵场

\[
B_\mu=2\,\mathbf b_\mu\cdot\mathbf T
\]

并要求

\[
D_\mu'\psi'=S(x)D_\mu\psi
\]

这迫使 $B_\mu$ 作带有非齐次项的 gauge transformation：

\[
B_\mu'
=
S^{-1}B_\mu S+\frac{i}{\epsilon}S^{-1}\partial_\mu S
\]

无穷小变换 $S=1-2i\mathbf T\cdot\delta\boldsymbol{\omega}$ 下，对应

\[
\mathbf b_\mu'
=
\mathbf b_\mu
+
2\,\mathbf b_\mu\times\delta\boldsymbol{\omega}
+
\frac{1}{\epsilon}\partial_\mu\delta\boldsymbol{\omega}
\]

最后一项正是用来吸收 $\partial_\mu S(x)$ 的“补偿项”；这就是 $b$ field 的必要性。

### 3. Field Strength 与非线性

电磁学中场强是线性的：

\[
F_{\mu\nu}^{\mathrm{em}}
=
\partial_\mu A_\nu-\partial_\nu A_\mu
\]

Yang-Mills 理论中，场强来自协变导数对易子：

\[
[D_\mu,D_\nu]
=
-2i\epsilon\,\mathbf f_{\mu\nu}\cdot\mathbf T
\]

文中得到

\[
\mathbf f_{\mu\nu}
=
\partial_\mu\mathbf b_\nu
-
\partial_\nu\mathbf b_\mu
-
2\epsilon\,\mathbf b_\mu\times\mathbf b_\nu
\]

符号会随 $D_\mu$ 和 $F_{\mu\nu}$ 定义约定改变，但关键结构不变：多出

\[
-2\epsilon\,\mathbf b_\mu\times\mathbf b_\nu
\]

这是非阿贝尔规范场的核心。因为 $SU(2)$ 生成元不对易：

\[
[T^a,T^b]=i\epsilon^{abc}T^c
\]

所以规范场本身携带 isotopic spin charge。换言之，$b$ 场不仅传递同位旋相互作用，它自己也是同位旋荷的源。这导致三规范玻色子、四规范玻色子自相互作用；而 Maxwell 场不带 electric charge，所以真空 Maxwell 方程是线性的。

### 4. Lagrangian、场方程与总流

文中公式 (11) 附近给出规范不变拉氏量。用现代记号，可写成

\[
\mathcal L
=
-\frac14\,\mathbf f_{\mu\nu}\cdot\mathbf f^{\mu\nu}
+
\bar\psi
\left(
i\gamma^\mu D_\mu-m
\right)
\psi
\]

其中

\[
D_\mu\psi
=
\left(
\partial_\mu-i\epsilon\,\boldsymbol{\tau}\cdot\mathbf b_\mu
\right)\psi
\]

文中采用 $x_4=ict$ 的 Euclidean-like 约定，所以原式中的 $i$、符号和 $\gamma_\mu$ 位置与现代 Minkowski 记号略有差异；物理结构就是 gauge kinetic term 加 matter coupling。

对 $\mathbf b_\mu$ 变分，得到 Yang-Mills 方程。按现代紧凑写法：

\[
(D_\mu\mathbf f_{\mu\nu})
=
\partial_\mu\mathbf f_{\mu\nu}
+
2\epsilon\,\mathbf b_\mu\times\mathbf f_{\mu\nu}
=
\mathbf J_\nu
\]

等价地，也可移项写成

\[
\partial_\mu\mathbf f_{\mu\nu}
=
\mathbf J_\nu
-
2\epsilon\,\mathbf b_\mu\times\mathbf f_{\mu\nu}
\]

具体整体符号取决于拉氏量和场强定义。$\mathbf J_\nu$ 是 nucleon spinor field 的 isotopic spin current，结构上正比于

\[
\mathbf J_\nu
\sim
\epsilon\,\bar\psi\gamma_\nu\boldsymbol{\tau}\psi
\]

但 Yang 和 Mills 特别强调：$\mathbf J_\nu$ 本身并不满足普通连续性方程。由 matter equation 可得

\[
\partial_\nu\mathbf J_\nu
=
-2\epsilon\,\mathbf b_\nu\times\mathbf J_\nu
\]

真正守恒的是 matter current 加上 $b$ field 自身携带的同位旋流：

\[
\mathbf j_\nu
=
\mathbf J_\nu
+
2\epsilon\,\mathbf b_\mu\times\mathbf f_{\mu\nu}
\]

并满足

\[
\partial_\nu\mathbf j_\nu=0
\]

这就是非阿贝尔理论里“源也包括规范场本身”的最早清楚表述。

### 研究者复核：一次无穷小变换与守恒的精确含义

Let \(B_\mu=2b_\mu^aT^a\), \(D_\mu=\partial_\mu-i\epsilon B_\mu\), and choose \(\psi'=S\psi\). Covariance \(D'_\mu S=SD_\mu\) gives
\[
B'_\mu=SB_\mu S^{-1}+\frac{i}{\epsilon}(\partial_\mu S)S^{-1},\qquad
F'_{\mu\nu}=SF_{\mu\nu}S^{-1},\quad
F_{\mu\nu}=\partial_\mu B_\nu-\partial_\nu B_\mu-i\epsilon[B_\mu,B_\nu].
\]
The inverse-conjugation formula printed earlier belongs to the opposite convention for the transformed matter field; the two conventions cannot be mixed. Using \([T^a,T^b]=i\epsilon^{abc}T^c\) then yields the stated cross-product term. The 1954 \(x_4=ict\) notation must not be read as a literal modern Minkowski-sign equation.

The field equation implies covariant conservation \(D_\nu J^\nu=0\), not ordinary conservation of the matter current. A “matter plus gauge-field” ordinary current is a convention- and gauge-dependent split; local gauge invariance alone does not supply a gauge-invariant local isospin charge without specifying boundary conditions and residual gauge transformations.

### 5. 守恒律与 Gauge Invariance 的关系

在 QED 中，电磁场 $A_\mu$ 不带 electric charge。电子场方程本身就给出 charge conservation，因此可以独立证明 photon 质量为零的 Ward-type 约束。

Yang-Mills 情形不同。$b$ field 本身携带 isotopic spin，所以 matter current $\mathbf J_\mu$ 的普通散度不为零；只有包含规范场贡献的总流 $\mathbf j_\mu$ 才守恒。论文脚注 25 正是在说：电磁学中 charge conservation 可由 electron field equation 单独推出，独立于 electromagnetic field；但这里 $b$ field carries isotopic spin，并破坏这种“一般守恒律”的直接类比。

因此，local gauge invariance 保证的是 covariant conservation 与 total isotopic spin conservation，而不是 matter sector 单独的普通守恒。

### 6. 质量问题的困境

若直接给 $b$ 场加 Proca 型质量项：

\[
\Delta\mathcal L_m
=
\frac12 M^2\,\mathbf b_\mu\cdot\mathbf b^\mu
\]

它在 local gauge transformation 下不变，因为 $\mathbf b_\mu$ 有非齐次项 $\epsilon^{-1}\partial_\mu\delta\boldsymbol{\omega}$。所以显式质量项会破坏 isotopic gauge invariance。

Yang 和 Mills 因而无法在理论内部给出 $b$ quantum 的质量。他们讨论了一个可能的 dimensional argument：若没有 nucleon field，拉氏量中没有质量维度参数，似乎暗示 $b$ quantum 质量为零；但他们立刻指出量子场论有 divergences，不能依赖这种量纲论证。他们坦承：

\[
\text{the mass of the } b \text{ quantum is undetermined}
\]

实验上，若 $b$ quanta 质量小于 pion，它们应在高能实验中大量产生，带电态还应活得足够久以被观测到；这与当时实验不符。因此他们认为质量若存在，至少应大于 pion 质量，并可能迅速衰变为 pions 和 photons 而逃过探测。

### 7. 历史影响

这篇 1954 年论文的真正突破，不在于成功描述强相互作用，而在于确立了 non-Abelian gauge theory 的基本模板：

\[
\text{symmetry group}
\rightarrow
\text{local gauge invariance}
\rightarrow
\text{covariant derivative}
\rightarrow
\text{gauge field}
\rightarrow
\text{nonlinear field strength}
\rightarrow
\text{self-interacting vector bosons}
\]

后来 electroweak theory 使用 $SU(2)_L\times U(1)_Y$，QCD 使用 $SU(3)_c$。Yang-Mills 的 $SU(2)$ isotopic gauge invariance 成为这些理论的原型。

1954 年留下的质量难题，后来由 spontaneous symmetry breaking 与 Higgs mechanism 解决：规范对称性不被显式破坏，质量来自真空结构和 Higgs field 的协变导数项。于是 $W^\pm,Z$ 可有质量，photon 仍无质量；QCD 中 gluons 形式上无质量，但 confinement 使自由 gluon 不出现。Yang-Mills 理论由此从一个核物理猜想，变成现代 Standard Model 的数学骨架。

## Review Questions

1. 如果把 Yang-Mills 的 $SU(2)$ 同位规范结构迁移到量子多体体系里的赝自旋或多组分序参量，哪些项会对应“规范场自相互作用”，哪些只会停留在外加联络的层面？
2. 对流体力学或 PDE 机器学习中的守恒律建模来说，局域对称性要求引入联络的思想，能否帮助构造更稳健的数值格式或可解释的神经算子？
3. 若把非阿贝尔规范场的“总流守恒”与 HPC 上的大规模并行守恒通量格式对照，是否能设计出更适合强耦合多场问题的离散守恒框架？
