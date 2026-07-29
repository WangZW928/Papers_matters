# Hamiltonian description of the ideal ﬂuid *

**Source PDF:** `RevModPhys.70.467.pdf`

---

## 摘要

这篇 55 页的综述系统地阐述了理想流体在不同变量描述下的 Hamiltonian 结构：从材料坐标的正则 Hamilton 描述，到 Euler 变量的非正则 Lie-Poisson 括号，再到 Clebsch 变量的正则化。Morrison 推导了理想流体 Euler 方程的非正则 Poisson 括号、Casimir 不变量（如二维涡度泛函、三维 helicity），以及能量-Casimir 稳定性理论。核心结论是：流体 Hamilton 结构的选择取决于变量选取，不同的变量给出不同的约束（Casimir）和稳定性判据。

**状态：** ✅ 已精读
## 精读笔记

### 数学结构与核心公式

Morrison 的主线是：理想流体不是“近似地像 Hamilton 系统”，而是其自然变量选择决定了 Hamilton 结构的显式形式。材料坐标 $q(a,t)$ 给出正则 Hamilton 描述，Euler 变量 $(M,\rho,\sigma)$ 给出非正则 Lie-Poisson 描述。这里 $a$ 是流体粒子标签，$r=q(a,t)$ 是空间位置，$J=\det(\partial q^i/\partial a^j)$，质量、熵、动量密度由 Lagrange-Euler 映射给出

\[
\rho(r,t)=\int_D \rho_0(a)\delta(r-q(a,t))\,d^3a,\quad
\sigma(r,t)=\int_D \sigma_0(a)\delta(r-q(a,t))\,d^3a,
\]

\[
M(r,t)=\int_D p(a,t)\delta(r-q(a,t))\,d^3a,\quad
v=M/\rho .
\]

正则材料变量中的 Hamiltonian 是

\[
H[q,p]=\int_D\left(\frac{|p|^2}{2\rho_0}+\rho_0 U(s_0,\rho_0/J)\right)d^3a ,
\]

正则 Poisson 括号为

\[
\{F,G\}=\int_D\left(\frac{\delta F}{\delta q}\cdot\frac{\delta G}{\delta p}
-\frac{\delta G}{\delta q}\cdot\frac{\delta F}{\delta p}\right)d^3a .
\]

变到 Euler 守恒变量后，Hamiltonian 变为

\[
H[M,\rho,\sigma]=\int_D\left(\frac{|M|^2}{2\rho}+\rho U(\rho,\sigma/\rho)\right)d^3r .
\]

核心非正则括号是

\[
\begin{aligned}
\{F,G\}=-\int_D\Big[
&M_i\left(\frac{\delta F}{\delta M_j}\partial_j\frac{\delta G}{\delta M_i}
-\frac{\delta G}{\delta M_j}\partial_j\frac{\delta F}{\delta M_i}\right)\\
&+\rho\left(\frac{\delta F}{\delta M}\cdot\nabla\frac{\delta G}{\delta\rho}
-\frac{\delta G}{\delta M}\cdot\nabla\frac{\delta F}{\delta\rho}\right)\\
&+\sigma\left(\frac{\delta F}{\delta M}\cdot\nabla\frac{\delta G}{\delta\sigma}
-\frac{\delta G}{\delta M}\cdot\nabla\frac{\delta F}{\delta\sigma}\right)
\Big]\,d^3r .
\end{aligned}
\]

这个括号的退化性产生 Casimir 不变量。二维 Euler 的典型例子是

\[
\{F,G\}=\int_D\omega\left[\frac{\delta F}{\delta\omega},\frac{\delta G}{\delta\omega}\right]d^2r,\quad
C[\omega]=\int_D \mathcal C(\omega)\,d^2r ,
\]

其中 $[f,g]=f_xg_y-f_yg_x$。三维无熵流中还出现 helicity

\[
C_{\rm hel}[v]=\int_D v\cdot(\nabla\times v)\,d^3r .
\]

稳定性部分的核心是能量-Casimir 泛函

\[
F=H+\lambda_a C^a,\quad \delta F|_{z_e}=0 ,
\]

以及动态可达扰动

\[
\delta z^i_{\rm da}=J^{ji}(z)g_j ,
\]

它们自动保持所有 Casimir：$\delta C=C_{,i}J^{ji}g_j=0$。

### 关键推导

材料坐标变分首先给出压强项。由热力学关系

\[
p=\rho^2\frac{\partial U}{\partial \rho}
\]

和 $\rho=\rho_0/J$，势能

\[
V[q]=\int_D \rho_0 U(s_0,\rho_0/J)\,d^3a
\]

只通过 $J$ 依赖于 $q$。利用行列式变分

\[
\frac{\partial J}{\partial q^i_{,j}}=A_{ij}
\]

以及 Euler-Lagrange 方程

\[
\frac{d}{dt}\frac{\partial L}{\partial\dot q^i}
+\partial_{a^j}\frac{\partial L}{\partial q^i_{,j}}-\frac{\partial L}{\partial q^i}=0 ,
\]

得到

\[
\rho_0\ddot q^i+A_{ij}\partial_{a^j}\left(\frac{\rho_0^2}{J^2}U_\rho\right)=0 .
\]

括号中正是 $p$，再用

\[
\partial_{r^k}=\frac{1}{J}A_{ki}\partial_{a^i}
\]

把材料加速度 $\ddot q$ 改写为空间场的物质导数，得到 Euler 方程

\[
\rho\left(\partial_t v+v\cdot\nabla v\right)=-\nabla p .
\]

非正则括号的推导来自链式法则。对 $F[q,p]=\bar F[\rho,\sigma,M]$ 变分，先写

\[
\delta\rho=-\int\rho_0\nabla\delta(r-q)\cdot\delta q\,d^3a,\quad
\delta M=\int\left(\delta p\,\delta(r-q)-p\nabla\delta(r-q)\cdot\delta q\right)d^3a .
\]

代入

\[
\delta F=\int\left(F_\rho\delta\rho+F_\sigma\delta\sigma+F_M\cdot\delta M\right)d^3r
\]

并对 $r$ 分部积分，得到 $\delta F/\delta q$ 与 $\delta F/\delta p$ 关于 Euler 泛函导数的表达式。再代回正则括号，积分掉 $\delta(r-q)$，便得到上面的 Euler 非正则括号。这个推导说明非正则性不是额外假设，而是由降维映射 $(q,p)\mapsto(M,\rho,\sigma)$ 的不可逆性产生。

二维 Euler 的 Casimir 推导很直接。若

\[
C[\omega]=\int_D\mathcal C(\omega)\,d^2r,\quad C_\omega=\mathcal C'(\omega),
\]

则

\[
\{C,F\}=\int_D\omega[\mathcal C'(\omega),F_\omega]\,d^2r .
\]

因为 $[\mathcal C'(\omega),F_\omega]=\mathcal C''(\omega)[\omega,F_\omega]$，分部积分后等价于 $\int_D F_\omega[\omega,\mathcal C'(\omega)]d^2r=0$。因此任意涡度重排函数都是守恒量。这解释了二维不可压流的相空间不是一个线性空间，而是由等涡度分布的辛叶片组成。

动态可达二阶能量是稳定性推导的关键。一般非正则系统中

\[
\dot z^i=J^{ij}\partial_jH .
\]

若 $J$ 退化，平衡不必满足 $\nabla H=0$，而只需落在 $J\nabla H=0$。能量-Casimir 方法通过 $\delta(H+\lambda C)=0$ 补齐约束；动态可达方法则只沿辛叶片扰动。Morrison 证明，对满足能量-Casimir 极值条件的平衡，

\[
\delta^2H_{\rm da}\equiv \delta^2F[\delta z_{\rm da}]
\]

其中

\[
\delta^2H_{\rm da}
=\frac12 H_{,ij}J^{li}g_lJ^{kj}g_k
+\frac12 H_{,i}\frac{\partial J^{ti}}{\partial z^l}J^{jl}g_tg_j .
\]

三维流体中取生成泛函

\[
G=\int_D(M\cdot\xi+\rho\eta+\sigma\kappa)\,d^3r ,
\]

得一阶动态可达扰动

\[
\delta M_{\rm da}=[M,\xi]^\dagger+\rho\nabla\eta+\sigma\nabla\kappa,\quad
\delta\rho_{\rm da}=\nabla\cdot(\rho\xi),\quad
\delta\sigma_{\rm da}=\nabla\cdot(\sigma\xi).
\]

代入 $H=\int(|M|^2/2\rho+\rho U)d^3r$ 并利用平衡方程化简，得到总二阶能量

\[
\delta^2H_{\rm da}=\frac12\int_D\left[
\frac{|P|^2}{\rho_e}+2P\cdot(v_e\cdot\nabla\xi)
+(\nabla\cdot\xi)^2(\rho_e p_{\rho})
+(\nabla\cdot\xi)(\xi\cdot\nabla p_e)
-(\xi\cdot\nabla\xi)\cdot\nabla p_e
\right]d^3r ,
\]

其中 $P_i=\rho v\cdot\partial_i\xi+\rho\partial_i\eta+\sigma\partial_i\kappa$。若此二次型在允许扰动上正定，就得到 Rayleigh/Fjortoft 型充分稳定条件。

### 对 HPC 框架的启示

这篇文章对 CFD 框架最直接的要求是：离散化不应只盯住守恒通量，还要显式编码 Poisson 结构、Casimir 与边界项。对不可压/可压 Euler 模块，可以把状态变量层分成正则材料变量、Euler 守恒变量、Clebsch/势变量三种视图；不同求解器共享同一个 Hamiltonian 与变分导数接口，而 Poisson operator 作为稀疏/矩阵无关算子提供。

数值格式上，应优先设计离散括号满足反对称性和离散 Jacobi 的近似或精确版本。至少要保证能量不由 Hamiltonian 部分虚假耗散，Casimir 漂移可监控。二维涡度求解器尤其适合加入 Casimir diagnostics：$\int\omega^n dA$、enstrophy、涡度分布直方图。三维则应监控 helicity 与潜涡 Casimir。

稳定性模块可以直接采用能量-Casimir/动态可达二阶变分作为 generalized eigenproblem 的构造器。对于大规模稳态流，可把 $\delta^2H_{\rm da}$ 实现为 matrix-free Hessian action，并用 Krylov/Lanczos 搜索负能量方向；这比只看线性增长率更能解释耗散触发的不稳定。HPC 框架还应暴露“扰动属于同一辛叶片吗”的开关：物理上不同的扰动源对应不同的约束空间。

### 待深入研究的问题

1. 如何在非结构网格、AMR 网格和 GPU kernel 中构造既局部守恒又尽量保持 Jacobi 恒等式的离散 Poisson 括号？
2. 对真实工程边界，$n\cdot v=0$ 与泛函导数边界条件如何兼容？是否需要把边界势能或约束作为 Hamiltonian 的一部分？
3. 动态可达稳定性在含激波、黏性边界层或亚格子模型的计算中应怎样解释？
4. 负能量模能否成为 LES/RANS 模型的结构化诊断量，用来预测耗散闭合项可能触发的非物理失稳？
5. Clebsch 变量的冗余规范自由度怎样离散规范固定，才能避免长期积分中的漂移和病态条件数？

## Review Questions

### 🤔 Questions
1. **Q:** How does the degeneracy of the Lie-Poisson bracket give rise to Casimir invariants, and why does this degeneracy reflect the non-canonical nature of the Eulerian description?
2. **Q:** What is the relationship between dynamically accessible perturbations and the energy-Casimir stability method? Why must physically admissible perturbations lie on the same symplectic leaf as the equilibrium state?
3. **Q:** In the Clebsch representation, what gauge freedom exists, and how does this redundancy relate to the helicity invariant in three-dimensional ideal fluids?
