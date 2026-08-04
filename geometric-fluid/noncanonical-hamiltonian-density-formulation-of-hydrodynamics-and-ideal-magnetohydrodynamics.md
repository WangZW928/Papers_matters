# 非正则哈密顿密度表述：流体力学与理想磁流体力学

# Noncanonical Hamiltonian Density Formulation of Hydrodynamics and Ideal Magnetohydrodynamics

**作者：** P. J. Morrison, J. M. Greene
**期刊：** Physical Review Letters 45(10): 790-794, 1980（含 Errata: PRL 48: 569, 1982）
**DOI：** [https://doi.org/10.1103/PhysRevLett.45.790](https://doi.org/10.1103/PhysRevLett.45.790)
**阅读状态：** 🔬 精读（Doctor 指定）
**流程状态：** ①元数据 ✓ | ②初稿 ✓ | ③评估 ✓(精读) | ④补充 ✓ | ⑤索引 ✓ | ⑥review ✓ | ⑦提交 ⏳

---

## 摘要

### 中文翻译
提出了完美流体（含或不含磁场）的哈密顿密度新表述。与以往工作不同，动力学变量是物理变量 ρ、v、B、s，构成非正则集合。定义了满足 Jacobi 恒等式的 Poisson 括号，并将该表述变换为以流体变量空间 Fourier 系数为动力学变量的哈密顿系统。

### 原文
> A new Hamiltonian density formulation of a perfect fluid with or without a magnetic field is presented. Contrary to previous work the dynamical variables are the physical variables, ρ, v, B, and s, which form a noncanonical set. A Poisson bracket which satisfies the Jacobi identity is defined. This formulation is transformed to a Hamiltonian system where the dynamical variables are the spatial Fourier coefficients of the fluid variables.

---

## 文章总结

### 1. 解决什么问题？
如何把理想流体（含 MHD）的全部方程（动量、质量、感应、熵对流）统一纳入哈密顿框架？

### 2. 用了什么方法论？
直接以物理变量 (ρ,v,B,s) 作为非正则动力学变量构造 Poisson 括号（三种等价形式：物理变量、守恒密度、Fourier 系数），验证 Jacobi 恒等式，Hamiltonian 取能量密度；磁场上需要 ∇·B=0 初始条件保证括号 Jacobi 性（Errata 修正）。

### 3. 主要结论是什么？
确立了非正则哈密顿结构（Lie-Poisson 括号）的范式：所有流体方程对等地位于括号中，熵对流与 Maxwell 感应方程可纳入；为后续 Lie-Poisson 理论、Casimir 不变量与稳定性分析奠基。

---

## 价值评估

Doctor 指定精读（跳过 Codex 价值评估）。

## 公式与代码梳理

本文的核心是把理想流体/理想 MHD 写成非正则 Hamilton 系统：

$$
\dot X^i=[X^i,H],\qquad X=(\rho,s,\mathbf v,\mathbf B)
$$

（原文记号：bracket 作用在 Hamiltonian 泛函 $H$ 上，严格推导需对动力学变量做 smear 处理；此处沿用论文的简化记号。）

其中 $\rho$ 是密度，$\mathbf v$ 是速度，$\mathbf B$ 是磁场，$s$ 是单位质量熵。论文考虑的 MHD 方程组为

$$
\partial_t\mathbf v
= -\nabla\left(\frac{|\mathbf v|^2}{2}\right)
+\mathbf v\times(\nabla\times\mathbf v)
-\rho^{-1}\nabla(\rho^2U_\rho)
+\rho^{-1}(\nabla\times\mathbf B)\times\mathbf B ,
\tag{1}
$$

$$
\partial_t\rho=-\nabla\cdot(\rho\mathbf v),
\tag{2}
$$

$$
\partial_t\mathbf B=\nabla\times(\mathbf v\times\mathbf B),
\tag{3}
$$

$$
\partial_t s=-\mathbf v\cdot\nabla s .
\tag{4}
$$

这里内能为单位质量内能 $U(\rho,s)$，热力学关系是

$$
p=\rho^2U_\rho,\qquad T=U_s .
$$

Hamiltonian 密度就是总能量密度：

$$
\mathcal H(\rho,s,\mathbf v,\mathbf B)
=\frac12\rho|\mathbf v|^2+\rho U(\rho,s)+\frac12|\mathbf B|^2 ,
$$

对应泛函

$$
H[\rho,s,\mathbf v,\mathbf B]
=\int_V\left(\frac12\rho|\mathbf v|^2+\rho U(\rho,s)+\frac12|\mathbf B|^2\right)\,d^3x .
$$

对该 Hamiltonian 的变分导数为

$$
H_{\mathbf v}=\rho\mathbf v,\qquad
H_{\mathbf B}=\mathbf B,\qquad
H_s=\rho U_s=\rho T,
$$

$$
H_\rho=\frac12|\mathbf v|^2+U+\rho U_\rho .
$$

第一种括号是物理变量 $(\rho,s,\mathbf v,\mathbf B)$ 下的非正则 Poisson 括号。用 $F_\rho=\delta F/\delta\rho$ 等记号，可写成

$$
\begin{aligned}
[F,G]=-\int_V \Big\{&
F_\rho\nabla\cdot G_{\mathbf v}
+F_{\mathbf v}\cdot\nabla G_\rho
-\rho^{-1}(\nabla\times\mathbf v)\cdot(F_{\mathbf v}\times G_{\mathbf v})\\
&+\rho^{-1}\nabla s\cdot(F_sG_{\mathbf v}-G_sF_{\mathbf v})\\
&+\rho^{-1}\left[
F_{\mathbf v}\cdot\mathbf B\times(\nabla\times G_{\mathbf B})
-G_{\mathbf v}\cdot\mathbf B\times(\nabla\times F_{\mathbf B})
\right]\Big\}\,d^3x .
\end{aligned}
\tag{6}
$$

把 $G=H$ 代入并令 $F$ 分别取测试形式 $\int f\rho\,d^3x$、$\int f s\,d^3x$、$\int \mathbf f\cdot\mathbf v\,d^3x$、$\int \mathbf f\cdot\mathbf B\,d^3x$，经分部积分和 Du Bois-Reymond 引理，就恢复 (1)-(4)。边界项假设消失；论文用测试函数在边界为零来避免额外边界条件讨论。

第二种等价形式改用守恒密度变量

$$
\sigma=\rho s,\qquad \mathbf M=\rho\mathbf v ,
$$

状态写为

$$
z=(\rho,\sigma,\mathbf M,\mathbf B).
$$

Hamiltonian 变为

$$
H[\rho,\sigma,\mathbf M,\mathbf B]
=\int_V\left(
\frac{|\mathbf M|^2}{2\rho}
+\rho U(\rho,\sigma/\rho)
+\frac12|\mathbf B|^2
\right)\,d^3x .
$$

这时括号没有 $\rho^{-1}$ 分母，更适合谱方法或离散实现：

$$
\begin{aligned}
[F,G]=-\int_V\Big\{&
\rho\left(F_{\mathbf M}\cdot\nabla G_\rho
-G_{\mathbf M}\cdot\nabla F_\rho\right)\\
&+\mathbf M\cdot\left(F_{\mathbf M}\cdot\nabla G_{\mathbf M}
-G_{\mathbf M}\cdot\nabla F_{\mathbf M}\right)\\
&+\sigma\left(F_{\mathbf M}\cdot\nabla G_\sigma
-G_{\mathbf M}\cdot\nabla F_\sigma\right)\\
&+\mathbf B\cdot\left(F_{\mathbf M}\cdot\nabla G_{\mathbf B}
-G_{\mathbf M}\cdot\nabla F_{\mathbf B}\right)\\
&+\mathbf B\cdot\left((\nabla F_{\mathbf M})\cdot G_{\mathbf B}
-(\nabla G_{\mathbf M})\cdot F_{\mathbf B}\right)
\Big\}\,d^3x .
\end{aligned}
\tag{9}
$$

这一形式显式表现为 Lie-Poisson 型：$\mathbf M$ 生成空间微分同胚作用，$\rho,\sigma,\mathbf B$ 是被平流的 advected quantities。代码实现上应优先采用这组变量，因为状态、Hamiltonian 梯度和 Poisson operator 都可以局部写成一阶微分算子。

第三种形式是 Fourier 系数形式。周期单位立方体上取

$$
\rho(\mathbf x,t)=\sum_{\mathbf k\in\mathbb Z^3}\rho_{\mathbf k}(t)
\exp(2\pi i\mathbf k\cdot\mathbf x),
$$

同理展开 $\sigma,\mathbf M,\mathbf B$。令

$$
Z_{\mathbf k}=(\rho_{\mathbf k},\sigma_{\mathbf k},
M^1_{\mathbf k},M^2_{\mathbf k},M^3_{\mathbf k},
B^1_{\mathbf k},B^2_{\mathbf k},B^3_{\mathbf k}),
$$

则泛函导数满足

$$
\frac{\delta F}{\delta\rho}
=\sum_{\mathbf k}\frac{\partial F}{\partial\rho_{\mathbf k}}
\exp(-2\pi i\mathbf k\cdot\mathbf x),
$$

其他变量类似。代入 (9) 得到无限维矩阵形式

$$
[F,G]=
\sum_{\mathbf k,\mathbf l}
\frac{\partial F}{\partial Z_{\mathbf k}}
\,\Omega_{\mathbf k\mathbf l}(Z)\,
\frac{\partial G}{\partial Z_{\mathbf l}},
\tag{13}
$$

（示意写法：原文 $Z_{\mathbf k}$ 为八分量（octuple），矩阵 $\Omega_{\mathbf k\mathbf l}$ 的块结构见原文 Fig. 1，且含 $Z_{-\mathbf k}$ 型索引约定，此处从简。）

或统一编号后写成

$$
[F,G]=\frac{\partial F}{\partial z_i}
J^{ij}(z)
\frac{\partial G}{\partial z_j},
\qquad J^{ij}=-J^{ji}.
\tag{14}
$$

这里 $J$ 是无限阶、状态依赖的反对称矩阵；矩阵元由 Fourier 卷积给出，例如 $\rho$-$\mathbf M$ 块含有 $\rho_{\mathbf k+\mathbf l}$ 与波矢 $\mathbf k,\mathbf l$，$\mathbf M$-$\mathbf M$ 块含有 $\mathbf M_{\mathbf k+\mathbf l}$，磁场块含有 $\mathbf B_{\mathbf k+\mathbf l}$。这就是把 PDE 的 Poisson operator 转成谱空间中的结构矩阵，形式上与有限维非正则 Hamilton 系统一致。

Jacobi 恒等式的目标是证明任意泛函 $F,G,H$ 满足

$$
[F,[G,H]]+[G,[H,F]]+[H,[F,G]]=0 .
$$

论文声明已证明一个足够覆盖动力学变量的情形：$F,G,H$ 的积分密度只依赖 $\mathbf x,t,X$，不依赖空间导数；完整的 Jacobi 恒等式证明未在本文展开（另文发表）。验证思路是把括号写成

$$
[F,G]=\int \frac{\delta F}{\delta X^i}\,\mathcal J^{ij}(X)\,
\frac{\delta G}{\delta X^j}\,d^3x ,
$$

然后检查 $\mathcal J$ 的反对称性和由结构函数诱导的 Jacobi 条件。反对称性依赖分部积分和边界项消失；Jacobi 性本质上来自 Lie 代数的余伴随结构。后来的语言会说：这是半直积 Lie-Poisson 括号，$\mathbf M$ 对密度、熵密度和磁通量的作用共同给出 Jacobi 恒等式。

1982 年 Errata 的重点是磁场部分。原文 (6)、(9) 的磁场括号在 Jacobi 恒等式上隐含使用了

$$
\nabla\cdot\mathbf B=0 .
$$

也就是说，原括号若离开无散磁场子流形，Jacobi 不再完全成立。Errata 指出可加入与 $\nabla\cdot\mathbf B$ 成正比的附加项，使括号在一般 $\nabla\cdot\mathbf B$ 下也满足 Jacobi。注意：此处展示的是 Errata 修正后的磁场相关结果，Errata 对 Eq. (6)、Eq. (9) 末项的具体修改形式（含 $\nabla\cdot\mathbf B$ 附加项）未逐项抄录。修正后的速度变量方程可写为

$$
\partial_t\mathbf v
=-\nabla\left(\frac12|\mathbf v|^2\right)
+\mathbf v\times(\nabla\times\mathbf v)
-\rho^{-1}\nabla(\rho^2U_\rho)
-\rho^{-1}\nabla\cdot\left(\frac12|\mathbf B|^2I-\mathbf B\mathbf B\right),
$$

$$
\partial_t\mathbf B
=-\mathbf B\,\nabla\cdot\mathbf v
+\mathbf B\cdot\nabla\mathbf v
-\mathbf v\cdot\nabla\mathbf B .
$$

当 $\nabla\cdot\mathbf B=0$ 时，磁力项回到熟悉的 $(\nabla\times\mathbf B)\times\mathbf B/\rho$，感应方程也等价于 $\nabla\times(\mathbf v\times\mathbf B)$。代码上这很重要：若离散磁场不能严格保持 $\nabla_h\cdot\mathbf B=0$，应使用 Errata 后的 bracket/force 形式，或显式采用 constrained transport 保证无散约束。

与 KdV 的关系在于括号中都出现空间导数作为 Poisson operator。KdV 的典型 Hamiltonian 括号是

$$
[F,G]=\int \frac{\delta F}{\delta u}\,
\partial_x\frac{\delta G}{\delta u}\,dx .
$$

Gardner 用 Fourier 变换把 $\partial_x$ 对角化，再缩放 Fourier 系数得到正则形式；Zakharov-Faddeev 则用谱变换走向正则变量。Morrison-Greene 的 Fourier 形式 (14) 明显继承了这个动机，但 MHD 的 $J(z)$ 是状态依赖且含卷积的无限维矩阵，不能简单对角化为常系数辛矩阵。

与 Arnold 力学的关系是概念层面的：Arnold 把不可压 Euler 解释为体积保持微分同胚群上的测地线；Morrison-Greene 则在 Euler 变量中直接给出该几何结构的非正则 Poisson 表达。这里的 $\mathbf M$ 是 Lie 代数对偶变量，$\rho,\sigma,\mathbf B$ 是随流携带的量；括号的退化性对应 Casimir 与辛叶片，而不是普通正则坐标中的完整相空间。

与本库 `Hamiltonian description of the ideal fluid` 的关系：那篇综述把材料坐标正则 Hamiltonian、Euler 变量非正则 Lie-Poisson 括号、Clebsch 正则化和能量-Casimir 稳定性系统化；本文是该传统中最早、最核心的 MHD 版本之一。可以把本文视为 “Euler 守恒变量括号 + 磁场 advected 结构” 的原始模板。

与 `LPNets` 的关系：LPNets 学习的是

$$
\dot z=J(z)\nabla H(z),
$$

并把反对称性、Jacobi 恒等式和 Casimir 守恒作为结构先验。本文的 Fourier 形式 (14) 正是理想流体/MHD 的无限维 $J(z)$ 原型；若做数据驱动流体模型，关键不是只学 $\dot z=f(z)$，而是学习或离散化满足 Lie-Poisson 约束的 $J(z)$ 与 $H(z)$。

与 `Covector Fluids` 的关系：Covector Fluids 强调速度余向量的一形式平流，避免直接平流速度向量带来的几何结构损失。本文括号中的 $\mathbf M$ 与 $\mathbf v$ 项正对应动量一形式在微分同胚作用下的 Lie 平流；因此图形学里的 covector advection 可以看作对 Arnold/Morrison 非正则结构的一种数值投影。

实现时建议抽象成三个层次：`State = (rho, sigma, M, B)`，`gradH(State)` 返回 $(H_\rho,H_\sigma,H_M,H_B)$，`poisson_apply(State, grad)` 实现 (9) 或 Errata 修正版的 $\mathcal J(z)\nabla H$。测试不应只比较时间步误差，还应检查

$$
[ F,G ] + [ G,F ] =0,
$$

能量守恒

$$
\frac{dH}{dt}=[H,H]=0,
$$

以及在无散磁场离散空间中

$$
\nabla_h\cdot\mathbf B=0
$$

是否被保持。对于谱代码，(14) 提供直接路线；对于网格代码，重点是离散梯度、散度、curl 与分部积分恒等式要成对设计，否则反对称性和 Jacobi 性会在离散层面被破坏。
## Review Questions

1. 对高性能 PDE/流体框架而言，如何把 Morrison-Greene 的守恒变量括号 $(\rho,\sigma,\mathbf M,\mathbf B)$ 实现成 GPU/AMR 友好的 matrix-free `poisson_apply`，同时在 coarse-fine 边界保持能量守恒、反对称性和 $\nabla\cdot\mathbf B=0$？
2. 若离散网格上无法严格满足连续 Jacobi 恒等式，应优先保证哪些结构条件：离散分部积分、curl-div 相容、Casimir 诊断，还是 Errata 后的 $\nabla\cdot\mathbf B$ 非零兼容 bracket？
3. LPNets 若用于学习理想流体/MHD 的 Fourier 或有限体积离散动力学，怎样参数化状态依赖的 $J(z)$，才能同时满足反对称性、Jacobi 恒等式、Casimir 守恒和磁场无散约束？
