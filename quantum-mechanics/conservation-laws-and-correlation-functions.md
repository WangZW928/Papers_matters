# 守恒定律与关联函数

# Conservation Laws and Correlation Functions

**作者：** Gordon Baym, Leo P. Kadanoff
**期刊：** Physical Review 124, 287–299 (1961)
**DOI：** [https://doi.org/10.1103/PhysRev.124.287](https://doi.org/10.1103/PhysRev.124.287)
**arXiv：** 无（1961 年 APS 论文，全文取自 harvest.aps.org PDF）
**阅读状态：** 🔬 精读（Doctor 指定）
**流程状态：** ①元数据 ✓ | ②初稿 ✓ | ③评估 ✓(精读) | ④补充 ✓ | ⑤索引 ✓ | ⑥review ✓ | ⑦提交 ⏳

---

## 摘要

### 中文翻译
在描述输运现象时，必须把数、能量、动量、角动量守恒律构建到用于确定热力学多粒子格林函数的近似结构之中。本文发展了一套生成守恒近似（conserving approximations）的方法：在有限温度下考察单粒子传播子 G 的运动方程，其中 G 在非局域外部标量场 U 存在下定义；将运动方程中出现的 G₂(U) 替换为 G(U) 的各种泛函即得到近似。若 G₂(U) 的近似满足若干简单对称性条件，则如此定义的 G(U) 满足全部守恒律；进一步，由 δG/δU 生成的双粒子关联函数 L（线性输运皆可由其描述）也满足全部守恒律及若干关键求和规则，如纵向 f-sum rule。

文中给出多个守恒近似实例：Hartree 近似 G₂(U)=G(U)G(U) 生成随机相位近似（RPA）；Hartree–Fock 近似给出 RPA 的自然推广（求和空穴-粒子阶梯图）；把自能展开到多粒子散射矩阵 T(U) 一阶得到 T 近似（所得 L 方程类比线性化 Boltzmann 方程）；最后，为描述等离子体中的碰撞，自能展开到动态屏蔽势 V_s(U) 一阶，所得 L 方程结构类似碰撞截面正比于 |V_s|² 的 Boltzmann 方程。

### 原文
> In describing transport phenomena, it is vital to build the conservation laws of number, energy, momentum, and angular momentum into the structure of the approximation used to determine the thermodynamic many-particle Green's functions. A method for generating conserving approximations has been developed. This method is based on a consideration, at finite temperature, of the equations of motion obeyed by the one-particle propagator G, defined in the presence of a nonlocal external scalar field U. Approximations for G(U) are obtained by replacing the G₂(U) which appears in these equations by various functionals of G(U). If the approximation for G₂(U) satisfies certain simple symmetry conditions, then the G(U) thus defined obeys all the conservation laws. Furthermore, the two-particle correlation function, generated as (δG/δU)₀, in terms of which all linear transport can be described, will obey all the conservation laws as well as several essential sum rules, such as the longitudinal f-sum rule.
>
> Several examples of conserving approximations are described. The Hartree approximation, G₂(U)=G(U)G(U), generates the random-phase approximation for L. The Hartree–Fock approximation for G(U) leads to a natural generalization of the random-phase approximation in which hole-particle ladder diagrams are summed. Another conserving approximation for G(U) is obtained by expanding the self-energy to first order in the many-particle scattering matrix T(U). This T is obtained by summing ladder diagrams in which the sides of the ladder are composed of G(U)'s. The resulting L equation, which involves coefficients proportional to (T)², is analogous to the linearized version of the usual Boltzmann equation. Finally, in order to obtain a description of collisions in a plasma, the self-energy is expanded to first order in a dynamically shielded potential, V_s(U). This potential is obtained by summing bubbles composed of two G(U)'s. The resulting L equation is similar in structure to a Boltzmann equation in which the collision cross section is proportional to |V_s|².

---

## 文章总结

### 1. 解决什么问题？
量子多体输运理论中，大多数常见近似不满足守恒律——例如 BCS–Bogoliubov 对超导体双粒子关联函数的计算不满足微分电荷守恒，导致 Anderson 预言的纵向集体振荡在密度-密度关联函数中缺失。因此无法从这些近似正确描述输运的定性特征。**问题：如何系统构造"自动满足全部守恒律"的格林函数近似？**

### 2. 用了什么方法论？
1. **外场驱动框架**：在有外场 U（非局域标量势，可推广为粒子数/动量/能量/角动量密度耦合）下定义单粒子格林函数 G(U)，其运动方程（含伴随方程）中含双粒子函数 G₂(U)。
2. **生成近似**：把 G₂(U) 替换为 G(U) 的泛函（Hartree / Hartree–Fock / Bethe–Goldstone 阶梯 / 屏蔽势 V_s），代入运动方程确定 G(U)。
3. **守恒判据**：证明只要近似满足三个条件——(A) G(U) 同时满足运动方程与伴随方程（等价于 G(G₀⁻¹−U)G 的两种求值一致）；(B) 对称性 G₂(13,1⁺3⁺;U)=G₂(31,3⁺1⁺;U)；(C) 顶点对称 (35,46)=(53,64)——则 G(U) 自动满足数、动量、角动量、能量全部守恒律。
4. **生成 L**：L(12,1′2′)=δG(1,1′)/δU(2′,2)，对守恒 G 取变分导数得到 L 的守恒积分方程（G 与 L 的近似被守恒律紧密耦合：L 的近似唯一确定 G）。

### 3. 主要结论是什么？
- **三条件充分性定理**：满足 (A)(B)(C) 的 G₂ 近似 → G(U) 与 L 自动满足全部守恒律（数/动量/角动量/能量）及 f-sum rule 等求和规则。对局域源耦合，源耦合构造在相应局域相位（规范）变换下的不变性给出 Ward/连续性恒等式；在响应、边界和正则性等附加条件下，它们再导出有关的纵向求和规则。数守恒本身既不等同于规范不变性，也不与纵向求和规则互为等价表述。
- **四个守恒近似**：Hartree → RPA（等离子振荡）；Hartree–Fock → 含交换 RPA 推广；T 近似（Bethe–Goldstone 阶梯图）→ 含碰撞，长波极限线性化 Boltzmann 方程（碰撞截面 ∝ |T|²）；V_s 屏蔽相互作用近似 → 高密度电子气 / 双组分等离子体金属模型（碰撞截面 ∝ |V_s|²）。
- **方法学意义**：G 与 L 的近似必须配套（"改进"L 而不守恒等于没有改进）；从非守恒的 G₂ 出发可得到完全守恒的 G₂（L+GG）。

---

## 价值评估

Doctor 指定精读（跳过 Codex 价值评估）。

## 公式与代码梳理

### 1. 有限温度格林函数与边界条件

Baym-Kadanoff 的起点不是直接写实时间响应，而是在有限温度虚时区间 $0\le i t\le \beta$ 上定义带外场的单粒子格林函数 $G(U)$。平衡格林函数由巨正则迹定义，时间演化中已把 $-\mu N$ 吸收到 $H$ 中。由于迹的循环性，虚时端点满足周期/反周期边界条件：

\[
G(\mathbf r_1,-i\beta;\mathbf r_1',t_1')
=
\pm G(\mathbf r_1,0;\mathbf r_1',t_1') ,
\]

其中上号为玻色子、下号为费米子。笔记中写作周期条件时，本质是说：有限温度格林函数不是初值问题，而是带虚时边界条件的边值问题；正是这个边界条件使运动方程可在 $[0,-i\beta]$ 上闭合求解。

为了让 $G$ 同时生成密度、动量、角动量、能量等响应，论文把外场从局域标量势 $U(2)n(2)$ 推广成非局域源：

\[
S[U]
=
T\exp\left[
-i\int d2\,d2'\,
\psi^\dagger(2)\,U(2,2')\,\psi(2')
\right].
\]

非局域 $U(2,2')$ 的物理意义是：在点 $2$ 移除一个粒子、在点 $2'$ 加入一个粒子。因此 $G(U)$ 是四点函数的生成泛函：

\[
L(12,1'2')
=
\left[
G_2(12,1'2')-G(1,1')G(2,2')
\right]_{U=0}
=
\left[
\frac{\delta G(1,1';U)}{\delta U(2',2)}
\right]_{U=0}.
\]

这里 $L$ 是线性输运的核心对象。真实的因果响应可由虚时结果解析延拓得到；论文的策略是先在虚时中构造满足守恒律的 $G(U)$，再用变分得到满足守恒律的 $L$。

### 2. 运动方程 (18a)/(18b) 与三个条件

哈密顿量含有动能与瞬时中心相互作用：

\[
V(1-3)=\delta(t_1-t_3)\,V(|\mathbf r_1-\mathbf r_3|).
\]

单粒子格林函数满足左右两个等价的精确运动方程。用 $G_0^{-1}$ 表示自由逆传播子：

\[
G_0^{-1}(1,1')
=
\left(i\frac{\partial}{\partial t_1}
+\frac{\nabla_1^2}{2m}\right)\delta(1-1'),
\]

则 (18a) 可理解为左作用的 Dyson-Schwinger 方程：

\[
\int d\bar 1\,
\left[
G_0^{-1}(1,\bar 1)-U(1,\bar 1)
\right]
G(\bar 1,1';U)
=
\delta(1-1')
+
i\int d\bar 3\,
V(1-\bar 3)\,
G_2(1\bar 3,1'\bar 3^+;U).
\]

(18b) 是伴随方程，即逆传播子从右侧作用：

\[
\int d\bar 1\,
G(1,\bar 1;U)
\left[
G_0^{-1}(\bar 1,1')-U(\bar 1,1')
\right]
=
\delta(1-1')
+
i\int d\bar 3\,
G_2(1\bar 3,1'\bar 3^+;U)
V(1'-\bar 3).
\]

两式精确时当然等价；但一旦把 $G_2(U)$ 替换成 $G(U)$ 的近似泛函，左右方程不一定还相容。因此论文提出守恒近似的三个条件。

**条件 (A)：左右运动方程相容。**

给定近似 $G_2[G;U]$ 后，由 (18a) 求出的 $G(U)$ 必须同时满足 (18b)。数学上，这保证从左、右两个方向定义的自能/逆传播子一致：

\[
G^{-1}=G_0^{-1}-U-\Sigma[G].
\]

它是数守恒的充分条件。

**条件 (B)：等时二粒子函数的交换对称性。**

\[
G_2(13,1^+3^+;U)
=
G_2(31,3^+1^+;U).
\]

这个条件说，在相互作用项中交换两粒子标签 $1\leftrightarrow 3$ 后，等时二粒子关联的近似不变。它保证内力成对抵消，因此动量、角动量、能量证明中的相互作用项不会产生伪源项。

**条件 (C)：有效二体相互作用核的顶点对称性。**

定义

\[
\mathcal I(35,46)
=
\left[
\frac{\delta \Sigma(3,4;G)}{\delta G(6,5)}
\right]_{U=0}.
\]

要求

\[
\mathcal I(35,46)=\mathcal I(53,64).
\]

这个条件保证由 $\delta G/\delta U$ 生成的 $L$ 在两对外腿之间具有正确交换对称：

\[
L(12,1'2')=L(21,2'1').
\]

因此 $L$ 不只在 $1,1'$ 变量上守恒，也在 $2,2'$ 变量上守恒；对电输运而言，这正是规范不变性与纵向 $f$-sum rule 的关键。

### 3. 守恒律证明的数学链条

核心操作是从 (18a) 减去 (18b)。二者相减得到类似连续性方程的 Ward 恒等式：

\[
\left(
\frac{\partial}{\partial t_1}
+
\frac{\partial}{\partial t_1'}
\right)iG(1,1';U)
+
\frac{\nabla_1+\nabla_1'}{2m}
\cdot
(\nabla_1-\nabla_1')iG(1,1';U)
=
\text{外场项}
+
\text{相互作用项}.
\]

在 $1'=1^+$ 后，左边变为密度期望值与流密度期望值的连续性结构：

\[
\frac{\partial}{\partial t_1}\langle n(1)\rangle_U
+
\nabla_1\cdot\langle \mathbf j(1)\rangle_U.
\]

若条件 (A) 成立，论文得到数守恒式 (22)：

\[
\frac{\partial}{\partial t_1}\langle n(1)\rangle_U
+
\nabla_1\cdot\langle \mathbf j(1)\rangle_U
=
i\int d2\,
\left[
U(1,2)G(2,1^+;U)
-
G(1,2;U)U(2,1^+)
\right].
\]

右端表示非局域外场通过“移除/加入粒子”造成的粒子源。若外场局域：

\[
U(2,2')=U(2)\delta(2-2'),
\]

则右端为零，于是得到普通连续性方程 (23)：

\[
\frac{\partial}{\partial t}\langle n\rangle_U
+
\nabla\cdot\langle \mathbf j\rangle_U
=
0.
\]

动量守恒的证明是在同一个基本恒等式上作用动量算符 $-(i/2)(\nabla_1-\nabla_1')$，然后令 $1'=1^+$ 并对 $\mathbf r_1$ 积分。相互作用项含有

\[
\int d\mathbf r_1\,d\mathbf r_3\,
\nabla_1 V(|\mathbf r_1-\mathbf r_3|)
G_2(13,1^+3^+;U).
\]

由于中心势满足

\[
\nabla_1 V(|\mathbf r_1-\mathbf r_3|)
=
-\nabla_3 V(|\mathbf r_1-\mathbf r_3|),
\]

再用条件 (B) 交换 $1$ 与 $3$，内力项成对抵消。于是得到 (25)：总动量的时间导数只等于外场施加的总力。局域外场下：

\[
\frac{d}{dt}\langle \mathbf P\rangle_U
=
-\int d\mathbf r\,
\nabla U(\mathbf r,t)\,
\langle n(\mathbf r,t)\rangle_U.
\]

角动量守恒完全平行，只是对恒等式作用

\[
\mathbf r_1\times\left[-\frac{i}{2}(\nabla_1-\nabla_1')\right],
\]

得到 (26)。中心势内力沿 $\mathbf r_1-\mathbf r_3$ 方向，结合 $G_2$ 的交换对称性，内力矩抵消。局域外场下：

\[
\frac{d}{dt}\langle \mathbf L\rangle_U
=
-\int d\mathbf r\,
\mathbf r\times\nabla U(\mathbf r,t)\,
\langle n(\mathbf r,t)\rangle_U.
\]

能量守恒稍复杂，因为能量密度同时包含动能与相互作用能。论文先把外场中能量期望写成

\[
\langle H(t)\rangle_U
=
\text{动能}[G]
+
\frac{1}{2}\int d1\,d3\,
V(1-3)G_2(13,1^+3^+;U)
+
\text{外场耦合项}.
\]

附录证明的关键是构造恒等式 (A.1)：把 (18a) 右乘 $G_0^{-1}$，把 (18b) 左乘 $G_0^{-1}$，相减并令 $1'=1^+$。这把时间导数中出现的 $G_2$ 项改写成 $G_0^{-1}G$ 与 $GG_0^{-1}$ 的差。随后利用条件 (B) 使相互作用能时间导数中的对称部分消失，最终得到 (28)：

\[
\frac{d}{dt}\langle H(t)\rangle_U
=
\int d1\,d2\,
\left[
\frac{\partial U(1,2)}{\partial t_1}
\,iG(2,1;U)
+
iG(1,2;U)
\frac{\partial U(2,1)}{\partial t_1}
\right].
\]

若外场采用局域密度耦合 $H_{\mathrm{ext}}=\int d\mathbf r\,U(\mathbf r,t)n(\mathbf r,t)$，则 (28) 给出的是全 Hamiltonian 的显式时间依赖功率：

\[
\frac{d}{dt}\langle H(t)\rangle_U
=
\int d\mathbf r\,
\frac{\partial U(\mathbf r,t)}{\partial t}
\langle n(\mathbf r,t)\rangle_U.
\]

力--电流形式说的是无外场部分 $H_0=H-H_{\mathrm{ext}}$，而不是上式中的全 $H(t)$。由连续性方程 $\partial_t n+\nabla\cdot\mathbf j=0$，并假定边界通量 $\int_{\partial D}U\,\mathbf j\cdot d\mathbf S=0$，有

\[
\frac{d}{dt}\langle H_0\rangle_U
=
\int d\mathbf r\,
\left[-\nabla U(\mathbf r,t)\right]\cdot
\langle \mathbf j(\mathbf r,t)\rangle_U.
\]

因此无外场时总能量守恒；对于静态局域外场，全 $H(t)$ 守恒，而 $H_0$ 与外场耦合能可按上式交换能量。

### 4. 从 \(G\) 到 \(L\)：积分方程 (43) 的推导

论文强调：不能随意给 $G$ 一个近似、再给 $L$ 另一个“更好”的近似。若 $L$ 要守恒，它必须由同一个 $G(U)$ 泛函变分生成。

先写 Dyson 形式：

\[
G^{-1}(1,1';U)
=
G_0^{-1}(1,1')
-
U(1,1')
-
\Sigma(1,1';G).
\]

从恒等式

\[
GG^{-1}=1
\]

取 $U$ 的变分，得

\[
\frac{\delta G}{\delta U}
=
-G
\frac{\delta G^{-1}}{\delta U}
G.
\]

即论文的 (38)：

\[
\frac{\delta G(1,1')}{\delta U(2',2)}
=
-\int d3\,d4\,
G(1,3)
\frac{\delta G^{-1}(3,4)}{\delta U(2',2)}
G(4,1').
\]

再由 Dyson 方程取变分：

\[
\frac{\delta G^{-1}(3,4)}{\delta U(2',2)}
=
-\delta(3-2')\delta(2-4)
-
\frac{\delta \Sigma(3,4)}{\delta U(2',2)}.
\]

因此有 (39) 的结构：

\[
L(12,1'2')
=
\pm G(1,2')G(2,1')
+
\int d3\,d4\,
G(1,3)
\frac{\delta\Sigma(3,4)}{\delta U(2',2)}
G(4,1').
\]

自能的 $U$ 依赖只通过 $G(U)$ 进入，所以用链式法则得到 (40)：

\[
\frac{\delta\Sigma(3,4)}{\delta U(2',2)}
=
\int d5\,d6\,
\frac{\delta\Sigma(3,4)}{\delta G(6,5)}
\frac{\delta G(6,5)}{\delta U(2',2)}.
\]

定义有效相互作用核 (41)：

\[
\mathcal I(35,46)
=
\left[
\frac{\delta\Sigma(3,4)}{\delta G(6,5)}
\right]_{U=0}.
\]

例如 Hartree-Fock 自能的变分给出 (42)：

\[
\mathcal I_{\mathrm{HF}}(35,46)
=
i\delta(3-4)\delta(5-6)V(3-5)
+
i\delta(3-6)\delta(5-4)V(3-5),
\]

第一项是 Hartree 直接项，第二项是 Fock 交换项。把 (39)、(40)、(41) 合并，就得到 Bethe-Salpeter 型方程 (43)：

\[
L(12,1'2')
=
\pm G(1,2')G(2,1')
+
\int d3\,d4\,d5\,d6\,
G(1,3)G(4,1')
\mathcal I(35,46)
L(62,52').
\]

这个方程的逻辑很重要：$G$ 必须是同一个自能 $\Sigma[G]$ 自洽求出的传播子，$\mathcal I$ 必须是同一个 $\Sigma$ 对 $G$ 的泛函导数。否则 Ward 恒等式、连续性方程和求和规则会被破坏。

### 5. 四种守恒近似

**Hartree 近似 $\rightarrow$ RPA**

Hartree 近似取

\[
G_2(13,1'3^+;U)
=
G(1,1';U)G(3,3^+;U).
\]

相应自能是局域平均场：

\[
\Sigma_H(1,1';U)
=
i\delta(1-1')
\int d3\,V(1-3)G(3,3^+;U).
\]

于是

\[
G^{-1}
=
G_0^{-1}
-
U
-
\Sigma_H.
\]

对 $\Sigma_H$ 取变分，只得到直接相互作用核：

\[
\mathcal I_H(34,3'4')
=
i\delta(3-3')\delta(4-4')V(3-4).
\]

因此 $L$ 满足泡图求和方程：

\[
L
=
L_0
+
L_0 V L,
\]

展开即为 RPA 泡图级数。这里泡图的两条线是自洽 Hartree 格林函数，而不是裸 $G_0$。

**Hartree-Fock 近似**

本文沿用原文有限温度时间有序 Green 函数及其 $G_2$ 记号；在这一约定下，原文式 (20) 的交换项带正号。这个正号不能脱离该定义被改写为通常等时四算符 Wick 记号中的符号。Hartree-Fock 近似取

\[
G_2(13,1'3';U)
=
G(1,1';U)G(3,3';U)
+
G(1,3';U)G(3,1';U),
\]

相应自能为

\[
\Sigma_{HF}(1,1')
=
i\delta(1-1')
\int d3\,V(1-3)G(3,3^+)
-
iV(1-1')G(1,1').
\]

第一项是直接平均场，第二项是交换场。其 $L$ 方程比 RPA 多出交换顶点：

\[
L
=
L_0
+
L_0 V_{\mathrm{direct}} L
+
L_0 V_{\mathrm{exchange}} L.
\]

图像上，这是带交换的 RPA 推广；等价于在粒子-空穴通道求和梯形图，梯子的线是 Hartree-Fock 格林函数。

**\(T\) 近似**

Hartree 与 Hartree-Fock 描述的是无碰撞的平均场输运。为纳入短程碰撞，论文从 Bethe-Goldstone 方程构造二粒子散射矩阵 $T[G]$：

\[
T
=
V
+
VGG T.
\]

更具体地说，$T$ 是由两条自洽 $G(U)$ 作为梯边的粒子-粒子梯形图求和。对应自能取一阶 $T$：

\[
\Sigma_T(1,1')
=
i\int d3\,d3'\,
\langle 13|T|1'3'\rangle
G(3',3).
\]

对 $\Sigma_T$ 取变分时有两类项：一类来自显式的末端 $G$，给出一个 $T$ 顶点；另一类来自 $T[G]$ 内部对 $G$ 的变分，产生两个 $T$ 夹住两条 $G$ 的结构。因此 $L$ 方程 schematically 为

\[
L
=
L_0
+
GG\,T\,L
+
GG\,T\,GG\,T\,L.
\]

第二个碰撞核含有 $T^2$。论文指出，在长波极限下，该方程可化为线性化 Boltzmann 方程，其碰撞截面正比于 $|T|^2$。这说明守恒近似不仅给出 Ward 恒等式，也自然生成输运碰撞项。

**动态屏蔽相互作用 \(V_s\) 近似**

对长程库仑系统，短程 $T$ 矩阵不是最自然的组织方式，因为极化屏蔽很重要。论文改用 RPA 型屏蔽势：

\[
V_s
=
V
+
VGG V_s,
\]

但这里泡图中的线是自洽 $G(U)$，不是简单 Hartree 线。自能取

\[
\Sigma_s(1,1')
=
i\delta(1-1')
\int d3\,V(1-3)G(3,3^+)
-
iV_s(1,1')G(1,1').
\]

这类似 Hartree-Fock，但把交换相互作用 $V$ 替换为动态屏蔽相互作用 $V_s$。对 $\Sigma_s$ 取变分时，除 Hartree 与屏蔽交换顶点外，还要变分 $V_s[G]$。为保留原文式 (66) 的两种不同收缩，下式仅记录指标结构并省略约定相关的整体因子；它不是完整的泛函导数定义：

\[
\frac{\delta V_s(1,1')}{\delta G(2',2)}
\sim
V_s(1-2')V_s(2-1')G(2-2')
+
V_s(1-2)V_s(2'-1')G(2'-2).
\]

因而原文式 (68) 的响应方程含两种不同的屏蔽相互作用收缩。以下仅是省略积分和外部指标的示意结构，不能作为由上式逐项完成的推导：

\[
L
=
L_0
+
GG\,V\,L
+
GG\,V_s\,L
+
GGGG\,\bigl(V_s(3-4')V_s(4-3')+V_s(3-4)V_s(4'-3')\bigr)\,L.
\]

最后一项具有类似 Boltzmann 碰撞项的 $|V_s|^2$ 结构；原文将其长波极限与相应的 Boltzmann 形式联系起来。这正适合高密度电子气、等离子体以及电子-离子双组分金属模型，因为 $V_s$ 的极点包含等离激元，也可在双组分情形中包含声波型集体模。

### 研究者复核：源约定与 Ward 链条

All signs in the response equations depend on the paper's definition of the time-ordered \(G\), \(G_2\), and source coupling. Consequently the free term in the Bethe--Salpeter equation should be read as the derivative \(\delta G/\delta U\) in that convention, rather than as a convention-free \(\pm GG\) identity. The Hartree--Fock exchange sign is likewise fixed only after those definitions are retained. The compact \(T\)- and \(V_s\)-equations in this note are diagrammatic/index-suppressed summaries, not equations safe for direct numerical implementation.

The logically precise chain is
\[
\text{compatible left/right equations for }G(U)
\;\Longrightarrow\;\text{continuity identity for }G
\;\xrightarrow{\,\delta/\delta U\,}\;\text{Ward identity for }L.
\]
Exchange symmetry of \(G_2\) cancels internal forces in momentum, angular-momentum, and energy balances; the vertex symmetry organizes the corresponding exchange/reciprocity properties of the response. These are complementary hypotheses, not interchangeable one-line proofs. For a local scalar source, integration by parts using \(\partial_t n+\nabla\cdot\mathbf j=0\) and vanishing boundary flux gives \(d\langle H_0\rangle/dt=\int(-\nabla U)\cdot\langle\mathbf j\rangle\), whereas the total explicitly time-dependent Hamiltonian obeys \(d\langle H\rangle/dt=\int(\partial_tU)\langle n\rangle\). Keeping these two energies distinct resolves the apparent sign/power ambiguity.

### 6. 与 Kadanoff-Baym 方程和非平衡格林函数的历史联系

这篇 1961 年论文是后来 “conserving approximation” 和 “Baym-Kadanoff formalism” 的核心前身。它的关键思想可以概括为：

\[
\Sigma[G]\quad\Longrightarrow\quad
G\quad\Longrightarrow\quad
\mathcal I=\frac{\delta\Sigma}{\delta G}
\quad\Longrightarrow\quad
L.
\]

也就是说，单粒子传播子、自能、响应顶点必须来自同一个泛函结构。后来 Baym 在 1962 年进一步发展出 $\Phi$-derivable approximation：若存在一个闭合骨架图泛函 $\Phi[G]$，使得

\[
\Sigma=\frac{\delta \Phi}{\delta G},
\]

则由该自能自洽得到的 $G$ 自动满足粒子数、动量、角动量、能量守恒。这就是现代很多体理论中“守恒近似”的标准表述。

Kadanoff-Baym 方程则把这种思想推进到实时间非平衡问题。平衡虚时中的 Dyson 方程被推广到 Keldysh 闭合时间路径上的双时格林函数方程：

\[
\left[
i\partial_{t_1}-h_0(1)
\right]G(1,1')
=
\delta(1-1')
+
\int_{\mathcal C} d\bar 1\,
\Sigma(1,\bar 1)G(\bar 1,1').
\]

这里 $\mathcal C$ 是 Keldysh 时间轮廓。碰撞积分、记忆核、谱函数和分布函数都由同一个自能 $\Sigma[G]$ 生成。只要 $\Sigma$ 来自守恒的 $\Phi[G]$，非平衡演化中的连续性方程与能量动量守恒就不会被破坏。

因此，本文的历史地位在于：它把“响应函数必须满足守恒律”从事后检查变成了构造原则。后来的 Kadanoff-Baym 方程、Keldysh 非平衡格林函数、量子输运中的自洽 Born 近似、GW 近似、T-matrix 近似、屏蔽相互作用近似，本质上都继承了这里的逻辑：不能孤立近似 $G$、$\Sigma$ 或顶点，必须让它们由同一个自洽泛函链条生成。

## Review Questions

⏳ 待 Kimi Code review

---

## Kimi Code 审查

审查结论如下。

整体上，这篇笔记的主线是对的：它准确抓住了 Baym–Kadanoff 1961 这篇文章的中心，即用外场 \(U\) 下的 \(G(U)\) 运动方程来构造守恒近似，并由 \(\delta G/\delta U\) 生成满足守恒律的两体关联函数 \(L\)。文档结构也基本连贯，`markdown` 公式环境使用了 `\[` `\]` 与 `$...$`，没有发现 `$$` 的用法，这一点合格。

但从“精读笔记”的标准看，当前稿件仍有几处需要明确指出的问题，其中有些是表述不严谨，有些是物理内容上容易误导读者。

1. 公式与物理上的主要问题

- `conservation-laws-and-correlation-functions.md:36`
  条件 (A) 的括号内解释“等价于 `G(G₀⁻¹−U)G` 的两种求值一致”表述不对，也不够清楚。这里真正的要点是：给定近似的 \(G_2[G;U]\) 后，由左运动方程与右运动方程定义出来的 \(G\) 必须相容，也即同一个 \(G\) 同时满足 (18a) 和 (18b)。你后文 `:144-148` 的说法更接近原意；这里这句压缩表述反而会把读者带偏。建议审查时把它视为“需要改写的歧义点”。

- `conservation-laws-and-correlation-functions.md:150`
  “它是数守恒的充分条件”这个判断偏强。更准确地说，在本文的证明链条里，(A) 用来保证由 (18a) 与 (18b) 相减得到的连续性方程成立；因此它是该构造框架下数守恒证明所需的关键条件。单独把 (A) 抽成一个脱离全文语境的“充分条件”会显得过度概括。

- `conservation-laws-and-correlation-functions.md:180-186`
  条件 (C) 的后果被写成“保证 \(L(12,1'2')=L(21,2'1')\)，因此 \(L\) 不只在 \(1,1'\) 变量上守恒，也在 \(2,2'\) 变量上守恒”。这个逻辑顺序不严谨。顶点核的交换对称性确实是保证变分生成的 \(L\) 具备正确交换/互易结构的重要条件，但“对第二对变量也守恒”本质上仍来自 \(L=\delta G/\delta U\) 与 \(G\) 的守恒结构，而不是单由这个交换式就能直接推出。这里有一点把“对称性”和“守恒性”混写了。

- `conservation-laws-and-correlation-functions.md:302-325`
  能量守恒部分最后一句“局域外场时，这化为功率输入
  \[
  \frac{d}{dt}\langle H(t)\rangle_U
  =
  \int d\mathbf r\,
  \left[-\nabla U(\mathbf r,t)\right]\cdot
  \langle \mathbf j(\mathbf r,t)\rangle_U
  \]
  ”
  这个写法值得警惕。对标量势耦合，常见的局域能量注入项更自然写成与 \(\partial_t U\) 或 \(U\,\partial_t n\) 相关，再用连续性方程改写后才可能转成 \(-\nabla U\cdot \mathbf j\) 一类形式。你这里直接把 (28) 写成这一结果，但中间缺少一步分部积分/连续性方程处理的说明，因此从“审查”角度应判为推导跳步过大。不是一定错，但现在这版不足以自证正确。

- `conservation-laws-and-correlation-functions.md:385-392`
  (39) 中非齐次项前面的 `\pm` 号不够可靠。对费米体系常规定义下，
  \[
  L(12,1'2')=\frac{\delta G(1,1')}{\delta U(2',2)}
  \]
  产生的自由项符号依赖你对时间序、源项和 \(G\) 定义里整体 \(i\) 因子的约定；这里直接写成“\(\pm G(1,2')G(2,1')\)”过于口语化，容易掩盖符号约定问题。对精读笔记来说，这里应固定一种约定，而不是留一个“\(\pm\)”糊过去。

- `conservation-laws-and-correlation-functions.md:418-423`
  HF 核 \(\mathcal I_{\mathrm{HF}}\) 的结构写法大体合理，但全文没有交代这里的核是“不可约粒子-空穴核”还是仅仅自能对 \(G\) 的泛函导数的坐标表达；对初学者来说，后面 `:528` 直接说“等价于在粒子-空穴通道求和梯形图”会略显跳跃。不是硬错误，但有概念压缩过度的问题。

- `conservation-laws-and-correlation-functions.md:498-503`
  Hartree–Fock 近似的二粒子分解写成
  \[
  G_2 = GG + GG
  \]
  且第二项前是正号。若采用标准费米子 Wick 分解，交换项通常带负号，差别只可能来自你前面对 \(G\)、\(G_2\) 的 \(i\) 因子定义约定。当前笔记没有把约定讲清，所以这里看起来像是错号。作为审查意见，这一处必须标记为“需要核对原文定义，否则读者会默认是符号错误”。

- `conservation-laws-and-correlation-functions.md:552-564` 与 `:589-613`
  对 \(T\) 近似和 \(V_s\) 近似的 \(L\) 方程，你用了大量 schematic 写法，如 `GG T L`、`GGGG(V_sV_s+V_sV_s)L`。这对口头报告可以，但对“精读补充（公式与代码梳理）”来说过于粗略，尤其原任务明确要求检查“四种近似的自能与 \(L\) 方程”。这里最多只能算方向正确，不能算公式层面已经讲清。特别是 `\delta V_s/\delta G \sim V_s G V_s + V_s G V_s` 这一行，本身就没有说明两个项的指标区别，写成同一个式子重复两次，形式上不严谨。

2. 历史与物理表述的准确性

- `conservation-laws-and-correlation-functions.md:40`
  “数守恒还可推出规范不变性（与纵向电导求和规则等价）”这句说重了。更稳妥的说法应是：在本文框架中，局域连续性方程与由 \(\delta G/\delta U\) 生成的响应函数结构共同保证了相应 Ward 恒等式，并由此导出纵向和规则。直接说“数守恒推出规范不变性”容易把局域对称性、Ward 恒等式、sum rule 三者压成一句话。

- `conservation-laws-and-correlation-functions.md:627-633`
  关于 \(\Phi\)-derivable 的历史联系基本正确，但需要更谨慎一点：Baym 1962 的结果不是简单重复 1961 的三个条件，而是把“守恒近似”组织成骨架泛函 \(\Phi[G]\) 的变分结构。你现在的写法没有错，但略显“把 1961 直接升级成 1962 形式”的线性叙述。建议在审查意见中指出：这是“后见之明式总结”，不是本文原始表述。

- `conservation-laws-and-correlation-functions.md:635-650`
  Kadanoff–Baym 历史联系写得总体不错，没有明显事实错误。但这部分最好提醒读者：1961 论文本身还是平衡虚时/热力学格林函数框架，不是已经写成后来的 Keldysh 轮廓方程。你文中用了“核心前身”这个词，这个分寸是合适的。

3. 逻辑与行文问题

- 文档总体逻辑顺序是通的：摘要 → 问题/方法/结论 → 公式梳理 → 历史联系。
- 但“文章总结”与“公式与代码梳理”之间存在少量重复，尤其对四种近似的总结在 `:41` 与 `:440-613` 处重复度较高，而后者又没有比前者精细很多。对精读文档来说，这会让读者预期“后面有更细公式”，结果看到的仍是 schematic 说明。
- 标题“公式与代码梳理”里的“代码”并无实际代码内容，名称不够贴切。若严格审查，可认为标题与内容不完全匹配。

4. Markdown 与格式

- 未发现 `$$` 数学环境，符合要求。
- 中英文混排总体正常。
- 存在一处风格不统一：三级标题用了普通 LaTeX 括号 `\(G\)`、`\(V_s\)`，而多数地方是 `$G$`、`$V_s$`。这不算错误，但风格上可统一。

结论

这篇笔记“可以作为高质量概要”，但“还不够稳到精读定稿”。最主要的问题不是方向错，而是若干关键处把严格的原文公式论证压缩成了口头化总结，导致：

- 条件 (A)(B)(C) 的逻辑关系有轻微混淆；
- \(L\) 方程 (43) 的自由项符号与核定义不够严格；
- HF 两体分解的交换项符号存在明显待核对点；
- \(T\) 与 \(V_s\) 两类近似的 \(L\) 方程写得过于 schematic，离“公式梳理”还有距离；
- 能量守恒局域化那一步推导跳得太快。

如果按审稿口径给判断，我会给：

- 物理主旨：准确
- 公式严谨性：中等，关键处需回原文核对
- 文档结构：良好
- 可提交程度：需要一轮修订后再入库定稿

**Review Questions**

1. Baym–Kadanoff 的守恒近似可由 \(\Sigma[G]\) 与 \(\mathcal I=\delta\Sigma/\delta G\) 的自洽链条生成。这个结构与现代 PDE/科学机器学习中的“把守恒律直接编码进模型或损失函数”有什么本质异同？能否构造一个类比：把 Ward identity 当作 PINN 中的硬约束，而把 \(\Phi\)-derivable 结构当作更强的生成原则？

2. 在高性能计算语境下，若要数值求解自洽的 \(G\)-\(\Sigma\)-\(L\) 方程组，最主要的计算瓶颈是什么：双时间/双频卷积、顶点核 \(\mathcal I\) 的存储、还是自洽迭代的收敛性？对比今天的 GW、T-matrix、Bethe-Salpeter 求解器，这篇 1961 文章的框架在哪些部分最适合并行化，哪些部分最难扩展到大规模 HPC？

3. 对等离子体与流体/动理学之间的联系，文中说 \(T\) 近似与 \(V_s\) 近似在长波极限下会导向类似线性化 Boltzmann 方程的碰撞结构。能否进一步追问：从 conserving approximation 到量子动理学，再到经典流体闭合，这条链上哪些守恒量是“自动继承”的，哪些额外闭合关系则必须另行假设？
