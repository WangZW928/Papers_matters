# Madelung 变换作为动量映射

# The Madelung Transform as a Momentum Map

**作者：** Daniel Fusca
**期刊：** Journal of Geometric Mechanics 9(2): 157-165, 2017
**DOI：** [https://doi.org/10.3934/jgm.2017006](https://doi.org/10.3934/jgm.2017006)
**arXiv：** [https://arxiv.org/abs/1512.04611](https://arxiv.org/abs/1512.04611)（v2, 2016, math.SG / math-ph；本文库以 arXiv v2 与 JGM 版为准）
**阅读状态：** 🔬 精读（Doctor 指定）
**流程状态：** ①元数据 ✓ | ②初稿 ✓ | ③评估 ✓(精读) | ④补充 ✓ | ⑤索引 ✓ | ⑥review ✓(JARVIS 补) | ⑦提交 ✓

---

## 摘要

### 中文翻译
Madelung 变换把非线性 Schrödinger 方程与称为量子流体动力学系统（quantum hydrodynamical system）的可压 Euler 方程联系起来。本文证明：Madelung 变换是与半直积群 $\mathrm{Diff}(\mathbb{R}^{n})\ltimes C^{\infty}(\mathbb{R}^{n})$（可压流体的位形空间）在波函数空间 $\Psi$ 上的作用相伴的**动量映射**（momentum map）。特别地，文章证明 Madelung 变换是 **Poisson 映射**，把 $\Psi$ 上的自然 Poisson 括号映到可压流体 Poisson 括号，并指出 Madelung 变换为流体动力学系统提供了"Clebsch 变量"的一个实例。

### 原文
> The Madelung transform relates the non-linear Schrödinger equation and a compressible Euler equation known as the quantum hydrodynamical system. We prove that the Madelung transform is a momentum map associated with an action of the semidirect product group $\mathrm{Diff}(\mathbb{R}^{n})\ltimes C^{\infty}(\mathbb{R}^{n})$, which is the configuration space of compressible fluids, on the space $\Psi$ of wave functions. In particular, we show that the Madelung transform is a Poisson map taking the natural Poisson bracket on $\Psi$ to the compressible fluid Poisson bracket, and observe that the Madelung transform provides an example of "Clebsch variables" for the hydrodynamical system.

---

## 文章总结

### 1. 解决什么问题？
波函数表象与流体表象之间的 Madelung 变换（$\psi=\sqrt{\rho}\,e^{i\varphi}$）长期被视为一种"代数替换"：把 NLS 拆成密度方程 + 相位方程。本文要回答的是它背后的**几何机制**——为什么这种代换能保持动力学结构？即：能否把 Madelung 变换理解为某个群作用的动量映射，从而把"波函数变流体"从形式技巧提升为辛几何中的约化（reduction）陈述？

### 2. 用了什么方法论？
- 在波函数空间 $\Psi$（复 Hilbert 空间看作实辛空间）上取自然辛形式（$L^2$ 内积的虚部）。
- 构造半直积群 $G=\mathrm{Diff}(\mathbb{R}^n)\ltimes C^\infty(\mathbb{R}^n)$ 在 $\Psi$ 上的作用（微分同胚搬动波函数 + 相位函数作 $U(1)$ 型相乘）。
- 计算该作用的无穷小生成元与动量映射 $J:\Psi\to\mathfrak{g}^*$，证明 $J(\psi)=(m,\rho)$，其中 $\rho=|\psi|^2$ 是密度、$m=\operatorname{Im}(\bar\psi\nabla\psi)$ 是动量密度——正是可压流体的两个场变量。
- 利用"动量映射是 Poisson 映射"的通用定理：$\Psi$ 上辛结构经 $J$ 落到 $\mathfrak{g}^*$ 上的 Lie-Poisson 括号（半直积约化，Marsden-Weinstein 1984），即流体 Poisson 括号。由此 NLS 的 Hamiltonian 流自动映为量子流体动力学系统的流。
- 观察 $\psi=\sqrt\rho\,e^{i\varphi}$ 给出 $m=\rho\nabla\varphi$，即密度 + 相位构成一组 Clebsch 变量。

### 3. 主要结论是什么？
Madelung 变换是半直积群 $G=\mathrm{Diff}(\mathbb{R}^n)\ltimes C^\infty(\mathbb{R}^n)$ 作用在波函数空间上的动量映射，因而是 Poisson 映射：NLS（含量子势能项的 Schrödinger 流）与可压 Euler 型量子流体动力学方程之间的对应不是巧合，而是辛约化的必然结果；同时 Madelung 变换给出流体动力学的 Clebsch 变量实现。这把"量子-经典流体对应"安放在动量映射/约化这一几何力学主干上，为后续 Khesin-Misiołek-Modin 的 Fisher-Rao/最优传输观点提供了出发点。

---

## 价值评估

Doctor 指定精读（跳过 Codex 价值评估）。

## 公式与代码梳理

（本小节由 Codex 精读补充，2026-08-04）

### 1. 逐公式梳理数学逻辑

本文把波函数空间

\[
\Psi=H^\infty(\mathbb R^n;\mathbb C)
\]

视为一个实 Hilbert 空间，而不是复线性空间。其内积取实 Hermite 内积

\[
\langle f,g\rangle=\operatorname{Re}\int_{\mathbb R^n}\bar f g\,dx .
\]

泛函梯度 $\nabla F$ 也按这个实内积定义。NLS Poisson 括号为

\[
\{F,G\}_{\mathrm{NLS}}(\psi)
=
\left\langle \nabla F,-\frac{i}{2}\nabla G\right\rangle .
\]

这里 $-i/2$ 就是常辛结构对应的 Poisson 张量。若 Hamiltonian 为

\[
H_{\mathrm{NLS}}(\psi)
=
\int_{\mathbb R^n}
\frac12|\nabla\psi|^2+U(|\psi|^2)\,dx,
\qquad U'=f,
\]

则变分给出

\[
\nabla H_{\mathrm{NLS}}
=
-\Delta\psi+2f(|\psi|^2)\psi .
\]

所以 Hamiltonian 向量场为

\[
X_H
=
-\frac{i}{2}\nabla H
=
\frac{i}{2}\left(\Delta\psi-2f(|\psi|^2)\psi\right),
\]

正是文中的 NLS 右端。换言之，NLS 的 Schrödinger 型 $i$ 因子不是额外加上的动力学约定，而是波函数空间实辛结构的 Poisson 张量。

经典 Madelung 形式写作

\[
\psi=\sqrt{\rho}\,e^{i\tau}.
\]

本文强调其“逆变换”更基本：

\[
M(\psi)
=
\left(
\operatorname{Im}\bar\psi\nabla\psi,
\operatorname{Re}\bar\psi\psi
\right)
=
(\mu,\rho).
\]

若代入 $\psi=\sqrt\rho e^{i\tau}$，则

\[
\operatorname{Im}\left(\sqrt\rho e^{-i\tau}\nabla(\sqrt\rho e^{i\tau})\right)
=
\rho\nabla\tau,
\qquad
\rho=|\psi|^2.
\]

因此

\[
\mu=\rho\nabla\tau.
\]

说逆变换更基本，是因为 $M$ 直接从波函数给出流体变量 $(\mu,\rho)\in\mathfrak s^*$，不必先选择全局相位函数 $\tau$；而 $\tau$ 本身只在加常数意义下确定：

\[
\tau\sim \tau+c.
\]

这对应波函数的整体相位等价

\[
\psi\sim e^{ic}\psi,
\]

即 $U(1)$ 规范自由度。流体变量只依赖 $\nabla\tau$ 和 $|\psi|^2$，所以不看整体相位。

可压流体的构型群取半直积

\[
S=\operatorname{Diff}(\mathbb R^n)\ltimes H^\infty(\mathbb R^n).
\]

其在波函数上的作用是

\[
(g,a)\cdot\psi
=
\sqrt{|\operatorname{Det}(Dg^{-1})|}
\,e^{-ia}
(\psi\circ g^{-1}).
\]

第一因子说明 $\psi$ 被当作复值半密度 pushforward；因为 $|\psi|^2dx$ 是密度，所以 $\psi$ 自然带半密度权重。第二因子 $e^{-ia}$ 是逐点相位调整。对 Lie 代数元 $\xi=(v,\alpha)$，无穷小作用为

\[
\xi_\Psi(\psi)
=
-\frac12\psi\nabla\cdot v
-i\alpha\psi
-\nabla\psi\cdot v.
\]

三项分别来自半密度 Jacobian、相位变换、以及复合 $\psi\circ g^{-1}$ 的输运项。

半直积 Lie 代数

\[
\mathfrak s=\operatorname{vect}(\mathbb R^n)\ltimes H^\infty(\mathbb R^n)
\]

的括号为

\[
[(u,\alpha),(v,\beta)]
=
([u,v],\,v\cdot\nabla\alpha-u\cdot\nabla\beta).
\]

其对偶 $\mathfrak s^*$ 以流体动量密度和密度

\[
(\mu,\rho)
\]

为坐标。Lie-Poisson，即可压流体括号，为

\[
\begin{aligned}
\{F,G\}_{\mathrm{CF}}(\mu,\rho)
=&amp;
\int_{\mathbb R^n}
\mu\cdot
\left[
\left(\frac{\delta G}{\delta\mu}\cdot\nabla\right)\frac{\delta F}{\delta\mu}
-
\left(\frac{\delta F}{\delta\mu}\cdot\nabla\right)\frac{\delta G}{\delta\mu}
\right]dx
\\
&+
\int_{\mathbb R^n}
\rho
\left[
\left(\frac{\delta G}{\delta\mu}\cdot\nabla\right)\frac{\delta F}{\delta\rho}
-
\left(\frac{\delta F}{\delta\mu}\cdot\nabla\right)\frac{\delta G}{\delta\rho}
\right]dx .
\end{aligned}
\]

第一项是动量变量上的 Lie-Poisson 部分，第二项是密度作为 advected quantity 被速度场搬运带来的半直积项。这正是 Morrison-Greene 非正则流体括号的几何版本：变量是 Eulerian 物理量而非正则坐标，所以括号退化并带有 Casimir；本文只取无熵、无磁场、可压流体的 $(\mu,\rho)$ 子结构。

动量映射定义为：若 Lie 代数作用 $\xi\mapsto\xi_P$ 在 Poisson 流形 $P$ 上 Hamiltonian 化，则 $J:P\to\mathfrak g^*$ 满足

\[
X_{J(\xi)}=\xi_P,
\qquad
J(\xi)(p)=\langle J(p),\xi\rangle.
\]

Theorem 3.5 证明 $M$ 正是该作用的 momentum map。对 $\xi=(v,\alpha)$，

\[
M(\xi)(\psi)
=
\int_{\mathbb R^n}
(\rho\alpha+\mu\cdot v)\,dx
=
\operatorname{Re}\int_{\mathbb R^n}
\left(\bar\psi\psi\alpha-i\bar\psi\nabla\psi\cdot v\right)dx .
\]

对 $\psi$ 作方向 $\phi$ 的变分并分部积分，得到

\[
\nabla M(\xi)
=
2\psi\alpha-2i\nabla\psi\cdot v-i\psi\nabla\cdot v.
\]

于是

\[
X_{M(\xi)}
=
-\frac{i}{2}\nabla M(\xi)
=
-i\alpha\psi-\nabla\psi\cdot v-\frac12\psi\nabla\cdot v
=
\xi_\Psi(\psi).
\]

这就是“逆 Madelung 变换是动量映射”的核心计算。

Theorem 3.6 进一步证明无穷小等变性：

\[
M([\xi,\eta])
=
\{M(\xi),M(\eta)\}_{\mathrm{NLS}}.
\]

设 $\xi=(u,\alpha)$、$\eta=(v,\beta)$。左边由 Lie 括号直接给出

\[
M([\xi,\eta])(\psi)
=
\operatorname{Re}\int_{\mathbb R^n}
\left(
-i\bar\psi\nabla\psi\cdot [u,v]
+
\bar\psi\psi(v\cdot\nabla\alpha-u\cdot\nabla\beta)
\right)dx .
\]

右边把 Theorem 3.5 的梯度代入 NLS 括号后展开。关键是两个恒等式。第一类为

\[
-2\bar\psi\nabla\psi\cdot v\,\alpha-\bar\psi\psi\nabla\cdot v\,\alpha
=
-\nabla\cdot(\bar\psi\psi v\alpha)
+\bar\psi\psi v\cdot\nabla\alpha
+\psi\nabla\bar\psi\cdot v\,\alpha
-\bar\psi\nabla\psi\cdot v\,\alpha .
\]

其中全散度项在快速衰减假设下积分为零，最后两项互为复共轭差，纯虚，取 $\operatorname{Re}$ 后也不贡献。第二类为

\[
\begin{aligned}
&-i\nabla\bar\psi\cdot u\,\nabla\psi\cdot v
+i\nabla\psi\cdot u\,\nabla\bar\psi\cdot v
-i\psi\nabla\bar\psi\cdot u\,\nabla\cdot v
+i\psi\nabla\bar\psi\cdot v\,\nabla\cdot u
\\
&=
-i\nabla\cdot(\psi\nabla\bar\psi\cdot u\,v)
+i\nabla\cdot(\psi\nabla\bar\psi\cdot v\,u)
-i\psi\nabla\bar\psi\cdot [u,v].
\end{aligned}
\]

同样，全散度项不贡献积分，剩余项正好恢复 $[u,v]$。因此 $M$ 无穷小等变。由标准定理，Corollary 3.7 得到

\[
M:\left(\Psi,\{\cdot,\cdot\}_{\mathrm{NLS}}\right)
\to
\left(\mathfrak s^*,\{\cdot,\cdot\}_{\mathrm{CF}}\right)
\]

是 Poisson 映射。

Hamiltonian 也完全对应。流体侧 Hamiltonian 为

\[
H_{\mathrm{CF}}(\mu,\rho)
=
\int_{\mathbb R^n}
\left(
\frac12\frac{|\mu|^2}{\rho}
+
\frac18\frac{|\nabla\rho|^2}{\rho}
+
U(\rho)
\right)dx .
\]

量子压项来自

\[
\nabla\psi
=
e^{i\tau}\left(\nabla\sqrt\rho+i\sqrt\rho\nabla\tau\right),
\]

所以

\[
|\nabla\psi|^2
=
|\nabla\sqrt\rho|^2+\rho|\nabla\tau|^2
=
\frac14\frac{|\nabla\rho|^2}{\rho}
+\frac{|\mu|^2}{\rho}.
\]

乘上 NLS Hamiltonian 中的 $1/2$，得到

\[
\frac12|\nabla\psi|^2
=
\frac12\frac{|\mu|^2}{\rho}
+
\frac18\frac{|\nabla\rho|^2}{\rho}.
\]

对应的 QHD 系统为

\[
\partial_t\rho=-\nabla\cdot\mu,
\]

\[
\partial_t\mu
=
-\nabla\cdot\left(\frac1\rho\mu\otimes\mu\right)
-\rho\nabla\left(
f(\rho)-\frac{\Delta\sqrt\rho}{2\sqrt\rho}
\right).
\]

它与经典 barotropic Euler 的差异在于量子压

\[
P(\rho)=\frac{\Delta\sqrt\rho}{2\sqrt\rho}
\]

不仅依赖 $\rho$，还依赖 $\rho$ 的空间导数，因此更接近 Korteweg/毛细型修正。

文末 remark 有三层含义。第一，$M$ 是 symplectic/Clebsch variables：从辛空间 $\Psi$ 到 Poisson 空间 $\mathfrak s^*$ 的 Poisson 映射，也称 symplectic realization；它只覆盖 $\mu=\rho\nabla\tau$ 的 gradient subspace。第二，von Renesse 与 Khesin-Misiołek-Modin 的最优传输观点把 Madelung 变换看作

\[
\sigma:C(M)\to T\mathcal P(M)
\]

的满射，并证明它把复函数空间的常辛结构下沉到 Wasserstein 度量诱导的自然辛结构。第三，momentum map 视角可能用于 Hamiltonian reduction 到涡片、涡膜等奇异解空间，这把 Madelung 变换接到 coadjoint orbit、vortex dynamics 与 Clebsch 变量传统上。

### 2. 算法/代码流程推演

本文没有代码，是纯理论几何力学论文。但若把结构转成可计算流程，可从离散波函数 $\psi_j$ 出发。给定网格点 $x_j$ 上的复数采样，先用谱方法或高阶有限差分计算

\[
\nabla\psi_j.
\]

然后逐点计算

\[
\rho_j=|\psi_j|^2,
\qquad
\mu_j=\operatorname{Im}(\bar\psi_j\nabla\psi_j).
\]

若需要速度，则在 $\rho_j>\varepsilon$ 的区域取

\[
v_j=\frac{\mu_j}{\rho_j}.
\]

量子压项可通过

\[
q_j=\sqrt{\max(\rho_j,\varepsilon)}
\]

先正则化，再计算

\[
P_j=\frac{\Delta q_j}{2q_j}.
\]

其中 $\Delta$ 最好与 $\nabla$ 使用同一离散微分体系，避免离散能量和动量映射不一致。数值验证 NLS 到 QHD 的保结构，可以比较两条路线：一条先用结构保持 NLS 积分器推进 $\psi$，再用 $M$ 得到 $(\mu,\rho)$；另一条直接用 QHD 离散方程推进 $(\mu,\rho)$。若离散实现合理，应近似满足

\[
M(\psi^{k+1})\approx \Phi_{\mathrm{QHD}}^{\Delta t}(M(\psi^k)).
\]

还可监控能量

\[
H_{\mathrm{NLS}}(\psi)
\]

与

\[
H_{\mathrm{CF}}(M(\psi))
\]

的一致性、质量

\[
\int\rho\,dx
\]

守恒、以及对称作用下由 momentum map 给出的量

\[
\int(\rho\alpha+\mu\cdot v)\,dx
\]

是否按 Noether 机制守恒或按外力破缺规律变化。

对结构保持神经网络而言，本文的意义很直接：与其让网络在 $(\rho,\mu)$ 上黑箱学习 QHD，不如学习波函数侧的 Hamiltonian

\[
H_\theta(\psi)
\]

或学习 Lie-Poisson 侧的 Hamiltonian

\[
\mathcal H_\theta(\mu,\rho),
\]

并把 Poisson 张量固定。HNN 适合正则/常辛的 $\Psi$ 表示；LPNets 适合非正则 Lie-Poisson 的 $(\mu,\rho)$ 表示。Madelung momentum map 则提供二者之间的结构桥：可以在波函数空间训练，再通过 $M$ 输出流体变量；也可以把损失项设计成同时约束

\[
\rho=|\psi|^2,\qquad
\mu=\operatorname{Im}(\bar\psi\nabla\psi),
\qquad
H_{\mathrm{NLS}}\approx H_{\mathrm{CF}}\circ M.
\]

这对“量子-经典流体对应 + 保结构学习”的主线很关键，因为它说明可学习变量的选择不是中性的：正则变量易训练辛结构，Eulerian 变量易表达物理守恒量，而 momentum map 给出二者一致的几何接口。

### 3. 与库内相关论文的关联

`geometric-fluid/geometric-hydrodynamics-via-madelung-transform.md`：Khesin-Misiołek-Modin 从 Fisher-Rao、Fubini-Study、Wasserstein/Otto 几何解释 Madelung 变换，重点是密度空间与最优传输；本文从 momentum map 和 Lie-Poisson 解释同一结构，重点是半直积对称性与 Poisson 映射。二者互补：前者偏 Riemann/Kähler 几何，后者偏 Hamiltonian reduction。

`geometric-fluid/noncanonical-hamiltonian-density-formulation-of-hydrodynamics-and-ideal-magnetohydrodynamics.md`：Morrison-Greene 是流体非正则 Hamiltonian 括号的源头。本文的 $\{\cdot,\cdot\}_{\mathrm{CF}}$ 可看作其无熵、无磁场、可压缩子情形，并用半直积 Lie-Poisson 语言重写。

`geometric-fluid/hamiltonian-description-of-the-ideal-ﬂuid.md`：Morrison 1998 综述系统整理材料坐标正则括号、Euler 变量非正则括号、Casimir 与 Clebsch 变量。本文可放在“Clebsch 变量作为辛实现”的分支中：波函数 $\psi$ 是正则/辛变量，$(\mu,\rho)$ 是非正则流体变量。

`vortex-dynamics/inside-fluids-clebsch-maps-for-visualization-and-processing.md`：该文把 Clebsch map 用于涡结构可视化和处理。本文给出 Madelung-Clebsch 的几何根基：$\psi$ 到 $(\mu,\rho)$ 的 Poisson 映射说明为什么用波函数处理涡量、相位缺陷和流体变量时能保留 Hamiltonian 结构。

`geometric-fluid/schrödingers-smoke.md`：Schrödinger's Smoke 用 Schrödinger/Gross-Pitaevskii 演化模拟不可压缩涡动力学。本文处理的是可压 QHD，但共同主线都是“波函数表示流体”。本文补上的正是 momentum map 解释：波函数不是数值技巧，而是流体 Poisson 几何的辛实现。

`geometric-fluid/quantum-spin-representation-for-the-navier-stokes-equation.md`：库内存在该文件，但当前摘要内容似乎偏量子自旋/磁子平台，与题名的 Navier-Stokes 表述不完全一致。若后续校正该条目，它可接入“量子变量编码经典流体”的方向；本文则提供 Madelung 型编码的标准几何样板。

`ai-for-physics/hamiltonian-neural-networks.md` 与 `ai-for-physics/liepoisson-neural-networks-lpnets-data-based-computing-of-hamiltonian-systems-wi.md`：HNN 学习正则 Hamiltonian，LPNets 学习非正则 Lie-Poisson 系统。本文正好说明 NLS/QHD 有两种等价学习坐标：$\Psi$ 上用 HNN 型常辛结构，$\mathfrak s^*$ 上用 LPNets 型流体 Lie-Poisson 结构，中间由 Madelung momentum map 保持 Poisson 关系。

因此，本文在库内研究主线中的位置是：它不是单纯介绍 Madelung 代换，而是把“量子波函数表示”和“经典可压流体 Hamiltonian 结构”用 momentum map 精确焊接起来。向前连接 Morrison 的非正则流体括号和 Clebsch 变量，向后连接 Wasserstein/Fisher-Rao 几何、Schrödinger 流体模拟，以及 HNN/LPNets 这类保结构数值与学习框架。

## Review Questions

> ⚠️ **Kimi review 未完成（上游故障）**：2026-08-04 23:57 起 zxcs99.cn 全模型不可用（gpt-5.4-mini 返回 Service temporarily unavailable，gpt-5.4/gpt-5.6 返回 Upstream request failed），重试一次仍失败；以下 3 问由 JARVIS 按 skill 要求自行补充（2026-08-04）。

1. 动量映射的离散版本如何保结构？对 NLS 采用保辛离散化（如 mid-point/变分积分器）推进 $\psi$ 后，再经 $M$ 得到的 $(\mu,\rho)$ 是否仍近似满足 QHD 的离散 Lie-Poisson 结构？离散梯度 $\nabla_h$ 的选择（如 staggered 网格上的 mimetic 算子）如何影响 $\int\rho\,dx$、$H_{\mathrm{NLS}}$ 与动量映射不变量 $\int(\rho\alpha+\mu\cdot v)\,dx$ 的守恒误差？
2. $M$ 的像只覆盖 $\mu=\rho\nabla\tau$ 的 gradient subspace（势流）；涡量非零的流场（如库内 Schrödinger's Smoke 的量子涡、Inside Fluids 的涡线）必须借助相位奇点或扩展的 Clebsch 变量。量子涡的相位缺陷、circulation 量子化与 momentum map 的纤维结构（$U(1)$ 整体相位等价类）之间应如何建立对应，才能在波函数表象里忠实表示有旋流？
3. 对结构保持学习（HNN/LPNets）而言，把 momentum map 作为硬约束（损失项强制 $\rho=|\psi|^2$、$\mu=\operatorname{Im}\bar\psi\nabla\psi$）与作为架构先验（直接在 $\Psi$ 上训练、经 $M$ 输出流体变量）相比，哪种更利于跨初值泛化与长期能量稳定性？量子压 $\Delta\sqrt\rho/(2\sqrt\rho)$ 的高阶导数在 PINN 型损失中会加剧谱偏置与收敛困难，能否借鉴库内 PINN/谱偏置文献（NTK 视角）给出缓解方案？
