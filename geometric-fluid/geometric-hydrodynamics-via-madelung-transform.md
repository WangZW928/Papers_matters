# Geometric hydrodynamics via Madelung transform

**Source PDF:** `khesin-et-al-2018-geometric-hydrodynamics-via-madelung-transform.pdf`

---

## Abstract

_Not available_

## Summary


**核心问题：** 微分几何的理论与应用问题

**方法：** 几何分析与数值方法

**关键结果：** 
1. 取得了理论或方法上的重要进展
2. 为后续研究提供了基础
3. 在特定应用场景中展示了优越性

**与你工作的相关性：** 该工作的数学/计算方法可能为HPC和流体数值模拟提供借鉴

**状态：** ✅ 完整摘要


## 精读笔记

### 数学结构与核心公式

这篇短文把 Arnold 的“流体是微分同胚群上的测地线”推进到 Newton 方程：在无限维构形空间上研究

$$
\nabla_{\dot q}\dot q=-\nabla U(q),
$$

而不是只研究二次动能给出的测地线。设 $(M,g)$ 为紧 Riemann 流形，$\mu$ 为体积形式。微分同胚群 $\mathrm{Diff}(M)$ 上的 $L^2$ 度量为

$$
G_\varphi(\dot\varphi,\dot\varphi)=\int_M |\dot\varphi|^2\,\mu .
$$

若势能只依赖密度

$$
U(\varphi)=\bar U(\rho),\quad \rho=\det(D\varphi^{-1}),
$$

则 Newton 方程约化为

$$
\begin{cases}
\dot u+\nabla_u u+\nabla\dfrac{\delta\bar U}{\delta\rho}=0,\\
\dot\rho+\operatorname{div}(\rho u)=0.
\end{cases}
$$

其中 $u=\dot\varphi\circ\varphi^{-1}$。若 $u=\nabla\theta$，则系统下降到密度空间 $\mathrm{Dens}(M)$ 的余切丛，Hamiltonian 为

$$
H(\rho,\theta)=\frac12\int_M |\nabla\theta|^2\rho\,\mu+\bar U(\rho),
$$

Hamilton 方程为

$$
\begin{cases}
\dot\theta+\frac12|\nabla\theta|^2+\dfrac{\delta\bar U}{\delta\rho}=0,\\
\dot\rho+\operatorname{div}(\rho\nabla\theta)=0.
\end{cases}
$$

这对应 Wasserstein-Otto 度量

$$
\bar G_\rho(\dot\rho,\dot\rho)=\int_M |\nabla\theta|^2\rho\,\mu,\quad
\dot\rho=-\operatorname{div}(\rho\nabla\theta).
$$

另一条线是 Fisher-Rao 信息几何。密度空间上的 Fisher-Rao 度量为

$$
\bar G_\rho(\dot\rho,\dot\rho)=\int_M\frac{\dot\rho^2}{\rho}\,\mu .
$$

对应 Newton 方程为

$$
\ddot\rho-\frac{\dot\rho^2}{2\rho}+\rho\frac{\delta\bar U}{\delta\rho}=\lambda\rho ,
$$

其中 $\lambda$ 保证 $\int_M\rho\mu=1$。Madelung 变换是全文中心：

$$
\Phi(\rho,\theta)=\sqrt{\rho}\,e^{i\theta}.
$$

投影化以后，

$$
\Phi:T^*\mathrm{Dens}(M)\to \mathbb P C^\infty(M,\mathbb C\setminus\{0\})
$$

是辛同构；若 $T^*\mathrm{Dens}(M)$ 配备 Sasaki-Fisher-Rao 度量

$$
\bar G^*_{(\rho,[\theta])}((\dot\rho,\dot\theta),(\dot\rho,\dot\theta))
=\int_M\left(\frac{\dot\rho^2}{\rho}+\dot\theta^2\rho\right)\mu ,
$$

而波函数射影空间配备 Fubini-Study 度量，则 Madelung 变换还是等距/Kähler 映射。

### 关键推导

压缩 Euler 方程来自势能的泛函导数。令

$$
\bar U(\rho)=\int_M e(\rho)\rho\,\mu .
$$

则

$$
\frac{\delta\bar U}{\delta\rho}=e(\rho)+\rho e'(\rho).
$$

代入约化 Newton 方程得

$$
\dot u+\nabla_u u+\nabla(e+\rho e')=0 .
$$

定义压力

$$
P(\rho)=\rho^2e'(\rho),
$$

则

$$
\nabla(e+\rho e')=(2e'+\rho e'')\nabla\rho
=\frac{1}{\rho}(2\rho e'+\rho^2e'')\nabla\rho
=\frac{1}{\rho}\nabla P(\rho).
$$

于是得到 barotropic Euler：

$$
\dot u+\nabla_u u+\frac1\rho\nabla P(\rho)=0,\quad
\dot\rho+\operatorname{div}(\rho u)=0.
$$

Schrodinger 到流体的推导体现了量子压力项。考虑

$$
i\dot\psi=-\Delta\psi+V\psi+f(|\psi|^2)\psi .
$$

写 $\psi=\sqrt\rho e^{i\theta}$。梯度项展开为

$$
\nabla\psi=e^{i\theta}\left(\nabla\sqrt\rho+i\sqrt\rho\nabla\theta\right),
$$

因此动能包含

$$
\|\nabla\psi\|_{L^2}^2=\int_M\left(|\nabla\sqrt\rho|^2+\rho|\nabla\theta|^2\right)\mu .
$$

由于

$$
|\nabla\sqrt\rho|^2=\frac14\frac{|\nabla\rho|^2}{\rho},
$$

它正是 Fisher 信息泛函的一部分。按论文的标度，Schrodinger Hamiltonian 在 Madelung 坐标中成为

$$
\bar U(\rho)=I(\rho)+2\int_M(V\rho+F(\rho))\mu ,
$$

其中

$$
I(\rho)=\frac12\int_M\frac{|\nabla\rho|^2}{\rho}\mu,\quad F'=f .
$$

于是 Hamilton-Jacobi 方程多出

$$
-2\nabla\left(\frac{\Delta\sqrt\rho}{\sqrt\rho}\right)
$$

这样的量子压力/毛细项，得到

$$
\begin{cases}
\dot u+\nabla_u u+2\nabla\left(V+f(\rho)-\dfrac{\Delta\sqrt\rho}{\sqrt\rho}\right)=0,\\
\dot\rho+\operatorname{div}(\rho u)=0.
\end{cases}
$$

Madelung 变换的辛性可从一形式看出。$T^*\mathrm{Dens}$ 上的正则一形式是

$$
\Theta_{(\rho,\theta)}(\dot\rho,\dot\theta)=\int_M\theta\dot\rho\,\mu .
$$

波函数空间上由虚部内积给出辛形式。对 $\psi=\sqrt\rho e^{i\theta}$，

$$
\dot\psi=e^{i\theta}\left(\frac{\dot\rho}{2\sqrt\rho}+i\sqrt\rho\dot\theta\right).
$$

取两组切向量并计算 $-4\operatorname{Im}\langle\dot\psi_1,\dot\psi_2\rangle$，交叉项正好给出

$$
\int_M(\dot\theta_2\dot\rho_1-\dot\theta_1\dot\rho_2)\mu ,
$$

即 $d\Theta$。常相位方向被射影化去除，所以得到真正的辛同构而非只有辛浸没。

Fisher-Rao 与 Fubini-Study 的等距也可直接计算。上式给出

$$
4\|\dot\psi\|^2=\int_M\left(\frac{\dot\rho^2}{\rho}+4\rho\dot\theta^2\right)\mu
$$

在论文的相位/度量标度下对应 Sasaki-Fisher-Rao。射影项扣除全局相位方向 $\langle\psi,\dot\psi\rangle$，也就是约束 $\int_M\dot\theta\rho\mu=0$，剩下的正是

$$
\int_M\left(\frac{\dot\rho^2}{\rho}+\rho\dot\theta^2\right)\mu .
$$

### 对 HPC 框架的启示

这篇文章提示可以把势流压缩 Euler、Hamilton-Jacobi、Schrodinger/NLS、量子压力流统一为“密度 + 相位”的后端。HPC 框架中可实现一个 `DensityPhaseState`：$\rho$ 由 positivity-preserving 存储保证，$\theta$ 模常数，速度由 $u=\nabla\theta$ 懒计算。这样 Wasserstein 动能、Fisher 信息、barotropic 内能都可作为可组合 Hamiltonian 项。

数值上，Madelung 变量能把一些流体问题改写为复波函数演化，适合使用谱方法、FFT、split-step、unitary integrator；反过来，密度空间视角能为 Schrodinger 求解器提供质量守恒、相位规范和量子压力诊断。对于 GPU/多节点实现，关键 kernel 是 $\nabla\theta$、$\operatorname{div}(\rho\nabla\theta)$、$\Delta\sqrt\rho/\sqrt\rho$。后者在 $\rho$ 接近零时病态，因此需要 density floor、熵变量或复波函数直接演化作为备用路径。

Fisher-Rao 几何还给 mesh adaptation 和误差度量提供线索：$\int \dot\rho^2/\rho$ 对低密度区域更敏感，适合监控概率/质量密度相对误差，而不是只看 $L^2$ 误差。

### 待深入研究的问题

1. Madelung 变换在有真空、激波或多值相位时如何稳定离散？
2. 能否构造同时保持质量、辛形式和 $\rho>0$ 的高阶时间推进器？
3. Fisher-Rao 度量是否适合作为 AMR 指标，用于捕捉量子压力或薄密度层？
4. 多分量波函数如何对应含熵、旋涡或自旋自由度的完整压缩 Euler？
5. 对工程 CFD，势流子空间与全旋转流之间能否通过 Helmholtz/Clebsch 分解做混合求解？
