# Inside Fluids: Clebsch Maps for Visualization and Processing

**Authors:** Albert Chern, Felix Knöppel, Ulrich Pinkall, and Peter Schröder

**DOI:** [http://dx.doi.org/10.1145/3072959.3073591](https://doi.org/http://dx.doi.org/10.1145/3072959.3073591)

**Source PDF:** `Clebsch1.pdf`

---

## Abstract

_Not available_

## Summary

**核心问题：** Clebsch映射在流体可视化和涡旋处理中的应用——如何利用Schrödinger方程处理涡旋数据？

**方法：** 引入Clebsch映射（Clebsch maps）概念：将流体速度场通过Clebsch势表示映射到波函数空间，利用Schrödinger流（量子力学中波函数的演化）处理流体数据，用于可视化涡丝追踪和流场处理。

**关键结果：**
- Clebsch映射提供了涡丝自动检测和追踪的新方法——涡线对应波函数的相位缺陷
- Schrödinger演化天然保持拓扑守恒（如螺旋度、环量），适合处理涡旋数据的平滑和插值
- 方法在计算流体和实验流体数据上都展示了优异的涡结构可视化能力

**与你工作的相关性：** Clebsch表示的数值框架可参考用于HPC框架中涡动力学的可视化和数据分析工具。

**状态：** ✅ 完整摘要


## 精读笔记

### 数学结构与核心公式

本文把 Clebsch 表示从经典势函数推广为流形值映射。经典形式写速度一形式

$$
\eta=u\cdot dr=\lambda\,d\mu-d\phi ,
$$

于是涡量二形式

$$
\omega=d\eta=d\lambda\wedge d\mu
$$

对应向量形式

$$
w=\nabla\times u=\nabla\lambda\times\nabla\mu .
$$

这说明涡线是 $(\lambda,\mu)$ 的等值线。用 pullback 语言，若固定一形式 $\alpha=x\,dy-dz$，$\psi=(\lambda,\mu,\phi):M\to\mathbb R^3$，则

$$
\eta=\psi^*\alpha,\quad \omega=d\eta=\psi^*(dx\wedge dy).
$$

更一般地，Clebsch map 是

$$
\psi:M\to C,\quad \psi^*\alpha=\eta ,
$$

或涡量映射

$$
s:M\to\Sigma,\quad s^*\sigma=\omega ,
$$

并要求投影 $\pi:C\to\Sigma$ 满足 $\pi^*\sigma=d\alpha$。本文重点采用球面 Clebsch map：

$$
C=S^3,\quad \Sigma=S^2,\quad s=\pi\circ\psi ,
$$

其中 $S^3$ 用单位四元数 $q$ 表示，固定

$$
\alpha=\hbar\langle dq,iq\rangle,\quad \sigma=\frac{\hbar}{2}dA_{S^2},\quad \pi(q)=qiq .
$$

速度与涡量由

$$
\eta=\psi^*\alpha=\hbar\langle d\psi,i\psi\rangle,\quad
\omega=s^*\sigma
$$

给出。因为 $s^{-1}(p)$ 是 $S^2$ 上点 $p$ 的原像，所以它天然给出闭合涡线；$s^{-1}(\Omega)$ 给出涡管。

给定目标速度一形式 $\eta_0$，算法求解

$$
E_\epsilon(\psi)=\int_M\frac{\epsilon}{4}|ds|^2+\frac1{\hbar^2}|\eta-\eta_0|^2 ,
$$

并逐步减小 $\epsilon$。等价地，引入联络

$$
\nabla_{\eta_0}\psi=d\psi-\frac{i\eta_0}{\hbar}\psi ,
$$

以及 Berger 球度量

$$
|X|_\epsilon^2=|P_{\mathbb C_\psi}X|^2+\epsilon|P_{\mathbb C_\psi^\perp}X|^2 ,
$$

可写成联络 Dirichlet 能量

$$
E_\epsilon(\psi)=\int_M|\nabla_{\eta_0}\psi|_\epsilon^2 .
$$

helicity 是拓扑核心：

$$
H(w)=\int_M u\cdot w\,dV=\int_M\eta\wedge\omega .
$$

经典 $\mathbb R^2$ Clebsch map 只能表示 $H=0$ 的场；$S^2$ Clebsch map 可表示非零 helicity，但量子化为

$$
H(w)=n h^2,\quad h=2\pi\hbar,\quad n\in\mathbb Z .
$$

### 关键推导

经典 Clebsch 的涡量公式来自外微分的自然性：

$$
\eta=\lambda d\mu-d\phi .
$$

取外微分得

$$
d\eta=d\lambda\wedge d\mu-d^2\phi=d\lambda\wedge d\mu .
$$

在三维 Euclidean 空间中，二形式 $d\lambda\wedge d\mu$ 与向量 $\nabla\lambda\times\nabla\mu$ Hodge 对偶，因此

$$
\nabla\times u=\nabla\lambda\times\nabla\mu .
$$

对任意曲面 $\Omega$，涡通量为

$$
\int_\Omega\omega=\int_\Omega s^*dA_{\mathbb R^2}=\operatorname{Area}(s(\Omega))
$$

带符号和重数。这给出可视化解释：涡通量由 Clebsch 图像在目标面上覆盖的面积表示。

球面 map 从涡量到速度的 lift 也有明确构造。给定 $s:M\to S^2$，若 $M$ 星形且 $\omega=s^*\sigma$ 精确，沿从原点到 $r$ 的径向线定义 $s_r(t)=s(tr)$，解

$$
\frac{d}{dt}\psi_r=-\frac{i}{2}\psi_r\frac{d}{dt}s_r,\quad \psi_r(0)=\psi_0 .
$$

可得

$$
\frac{d}{dt}(\psi_ri\bar\psi_r)=\frac{d}{dt}s_r,
$$

故 $\psi_ri\bar\psi_r=s_r$。令 $\varphi(r)=\psi_r(1)$，则 $\pi\circ\varphi=s$。由

$$
\tilde\eta=\hbar\langle d\varphi,i\varphi\rangle
$$

有 $d\tilde\eta=d\eta$；若 $M$ 单连通，则存在 $\theta$ 使 $d\theta=\eta-\tilde\eta$，最终

$$
\psi=e^{i\theta}\varphi
$$

满足 $\psi^*\alpha=\eta$。

能量等价式的推导依赖四元数正交分解。论文给出

$$
-\bar\psi i\nabla_{\eta_0}\psi
=\frac1\hbar(\eta-\eta_0)-\frac12 ds .
$$

右侧第一项沿 $\mathbb C_\psi=\operatorname{span}\{\psi,i\psi\}$，第二项沿正交补 $\mathbb C_\psi^\perp=\operatorname{span}\{j\psi,k\psi\}$，所以

$$
P_{\mathbb C_\psi}(\nabla_{\eta_0}\psi)=\frac1\hbar(\eta-\eta_0)i\psi,\quad
P_{\mathbb C_\psi^\perp}(\nabla_{\eta_0}\psi)=-\frac12 i\psi ds .
$$

代入 Berger 度量：

$$
|\nabla_{\eta_0}\psi|_\epsilon^2
=\frac1{\hbar^2}|\eta-\eta_0|^2+\frac{\epsilon}{4}|ds|^2 ,
$$

正好恢复 $E_\epsilon$。

经典 Clebsch helicity 为零也可一行证明：

$$
H=\int_M(\lambda d\mu-d\phi)\wedge d\lambda\wedge d\mu
=-\int_M d\phi\wedge d\lambda\wedge d\mu
=-\int_M d(\phi\,d\lambda\wedge d\mu).
$$

若涡量在边界消失，边界积分为零，所以 $H=0$。球面情形中，$s:M\to S^2$ 可延拓到紧化 $S^3\to S^2$，其 Hopf 不变量为整数 $n$，helicity 因而按 $h^2$ 量子化。这也是 spherical Clebsch map 能表达链接涡线的拓扑原因。

离散算法把 $\psi=(\psi_1,\psi_2)^T\in\mathbb C^2$ 放在网格顶点，一形式放在有向边。边上的协变差分为

$$
(\nabla_{\eta_0}\psi)_{ij}
=e^{-i(\eta_0)_{ij}/2\hbar}\psi_j-e^{i(\eta_0)_{ij}/2\hbar}\psi_i .
$$

投影矩阵由 Pauli 矩阵构造，形成稀疏二次型

$$
E_\epsilon(\psi)=\sum_{ij\in E}w_{ij}\left|P^\epsilon_{ij}(\nabla_{\eta_0}\psi)_{ij}\right|^2
=\psi^\ast L\psi .
$$

半隐式梯度步为

$$
(M_V+\Delta t\,L^{(k)})\psi^{(k+1)}=M_V\psi^{(k)},
$$

随后逐点归一化到 $S^3$。

### 对 HPC 框架的启示

本文给 CFD 后处理和涡动力学模块一个很明确的工程路线：把涡量场转成低维目标流形上的 map，然后用原像操作做可视化、追踪和多尺度处理。相比直接积分涡线，$s^{-1}(p)$ 和 $s^{-1}(\Omega)$ 更适合批量并行提取，也更容易保持涡管方向与涡量方向一致。

在 HPC 实现中，瓶颈是 connection Laplacian 的重复求解。论文原型使用共轭梯度；生产级应实现 multigrid/preconditioned CG，且支持复数 $2\times2$ block sparse matrix。由于 $\epsilon$ 逐步降低会加剧条件数问题，continuation schedule、预条件器重用和 mixed precision refinement 都值得做成框架能力。

这套表示也适合作为亚格子涡量增强接口。后处理 $\tilde\psi=\Xi\circ\psi$、$\tilde s=\xi\circ s$ 可以把粗涡管分裂为细涡管，并用映射次数 $m_\xi$ 重标定

$$
\tilde\eta=\frac{\hbar}{m_\xi}\langle d\tilde\psi,i\tilde\psi\rangle
$$

以保持局部涡通量。最后再做压力投影，得到不可压速度场。这比各向同性噪声更结构化，尤其适合 LES 可视化或艺术/工程混合仿真。

### 待深入研究的问题

1. 如何为 $E_\epsilon$ 设计可扩展预条件器，使 $256^3$ 以上网格可实际使用？
2. spherical Clebsch map 对非闭合涡线只能近似闭合；这种拓扑误差如何随网格分辨率和 $\hbar$ 收敛？
3. helicity 量子化对任意 helicity 数据的近似误差是否可给出可计算上界？
4. 边界切割涡管时，怎样设置边界条件才不引入虚假链接数？
5. Clebsch-map flow processing 能否和能量守恒/辛时间推进结合，成为长期稳定的涡量亚格子模型？
