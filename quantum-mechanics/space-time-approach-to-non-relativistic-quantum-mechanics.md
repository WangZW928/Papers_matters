# 非相对论量子力学的时空方法

# Space-Time Approach to Non-Relativistic Quantum Mechanics

**作者：** R. P. Feynman（费曼）
**期刊：** Reviews of Modern Physics 20, 367–387 (1948)
**DOI：** [https://doi.org/10.1103/RevModPhys.20.367](https://doi.org/10.1103/RevModPhys.20.367)
**arXiv：** 无（1948 年 APS 论文，全文取自 harvest.aps.org PDF）
**阅读状态：** 🔬 精读（Doctor 指定）
**流程状态：** ①元数据 ✓ | ②初稿 ✓ | ③评估 ✓(精读) | ④补充 ✓ | ⑤索引 ⏳ | ⑥review ✓ | ⑦提交 ⏳

---

## 摘要

### 中文翻译
本文以不同的方式表述非相对论量子力学；它在数学上等价于熟悉的表述。在量子力学中，可以以多种不同方式发生的事件，其概率等于若干复贡献之和的模平方，每种方式对应一个贡献。粒子被发现沿路径 $x(t)$ 落在时空某区域内的概率，是该区域内每条路径贡献之和的模平方。单条路径的贡献被设定为指数函数，其（虚）相位是该路径的经典作用量（以 ℏ 为单位）。所有从过去到达 $(x,t)$ 的路径的总贡献即波函数 $\psi(x,t)$。文中证明它满足 Schrödinger 方程，并讨论与矩阵和算符代数的关系。应用方面指出，特别是可以从量子电动力学方程中消去场振子的坐标。

### 原文
> Non-relativistic quantum mechanics is formulated here in a different way. It is, however, mathematically equivalent to the familiar formulation. In quantum mechanics the probability of an event which can happen in several different ways is the absolute square of a sum of complex contributions, one from each alternative way. The probability that a particle will be found to have a path $x(t)$ lying somewhere within a region of space time is the square of a sum of contributions, one from each path in the region. The contribution from a single path is postulated to be an exponential whose (imaginary) phase is the classical action (in units of ℏ) for the path in question. The total contribution from all paths reaching $x$, $t$ from the past is the wave function $\psi(x, t)$. This is shown to satisfy Schroedinger's equation. The relation to matrix and operator algebra is discussed. Applications are indicated, in particular to eliminate the coordinates of the field oscillators from the equations of quantum electrodynamics.

---

## 文章总结

### 1. 解决什么问题？
标准的 Schrödinger 表述（波函数演化）与 Heisenberg 表述（矩阵力学）虽然成功，但依赖于"态在时刻 t 的演化"这一逐时（step-by-step）图像，物理直观与经典力学（尤其是最小作用量原理）的联系被算符代数掩盖。费曼的目标：**给出一种全新的量子力学表述**——不借助算符与 Hilbert 空间，直接用时空中的路径（worldline）与经典作用量来构造量子力学振幅，使"几率幅叠加"成为唯一基本假设，并让经典极限（最小作用量原理）在形式上显而易见。

### 2. 用了什么方法论？
1. **叠加原理的极致化**：把"事件可以多种方式发生"的叠加原理推广到连续无穷——粒子从 A 到 B 有无穷多条路径，每条路径贡献一个振幅 $e^{iS[x(t)]/\hbar}$（S 为该路径的经典作用量），总振幅 = 所有路径贡献之和。
2. **路径积分的构造**：把时间细分为 $N$ 个小区间，用完备性关系在中间时刻插入坐标本征态，将传播子 $K(b,a)=\langle b|e^{-iH(t_b-t_a)/\hbar}|a\rangle$ 改写为对中间坐标的多重积分；取 $N\to\infty$ 极限得到对路径 $x(t)$ 的泛函积分（文中用"对路径空间求和"的直观语言，并给出短时传播子的显式表达式）。
3. **短时间传播子**：对自由粒子与势场情形推导 $\epsilon$ 时间步的传播子（含经典作用量的指数 + 归一化因子），证明其满足 Schrödinger 方程（直接代入验证或通过组合律）。
4. **等价性证明**：证明路径积分表述与 Schrödinger 方程、矩阵力学（对易关系 $pq-qp=\hbar/i$）在数学上完全等价；经典极限 $\hbar\to0$ 时驻相近似恢复最小作用量原理。
5. **应用**：指出可把场论中的场振子坐标"积分掉"（消去），为后续 QED 时空方法（1949 论文）铺路——路径积分是那篇 QED 工作的数学基础。

### 3. 主要结论是什么？
- **量子力学 = 路径振幅求和**：$\psi(x,t)=\int \mathcal D[x(t)]\, e^{iS[x]/\hbar}$（对所有从过去到达 $(x,t)$ 的路径积分），满足 Schrödinger 方程。
- **与既有表述等价**：与 Schrödinger 波动力学、Heisenberg 矩阵力学数学等价；对易关系、观测期望值等全部可由此重新导出。
- **经典极限自然出现**：$\hbar\to0$ 时驻相近似 → 经典路径（最小作用量）主导，量子力学平滑过渡到经典力学。
- **泛函积分技术**：引入短时传播子组合（Chapman-Kolmogorov 型半群性质）、泛函积分测度、驻相近似等工具。
- **历史意义**：路径积分量子化的奠基文献，深刻影响：量子场论（Feynman 1949 QED 方法、Dyson 形式化）、统计力学（配分函数 = 虚时路径积分）、凝聚态多体（Green 函数泛函积分表述）、以及现代量子模拟/量子蒙特卡洛（Path Integral MC、PIMD——库内已有 path-integral-molecular-dynamics 一脉）。

---

## 价值评估

Doctor 指定精读（跳过 Codex 价值评估）。

## 公式与代码梳理

### 1. 基本公设：从概率幅叠加到路径振幅

费曼把量子力学的核心压缩成一个规则：若一个事件可以通过若干不可区分的 alternative ways 发生，则事件概率不是各路径概率相加，而是先把每条路径的 probability amplitude 相加，再取模平方。若中间量 $b$ 没有被测量：

\[
\phi_{ac}=\sum_b \phi_{ab}\phi_{bc},\qquad P_{ac}=|\phi_{ac}|^2.
\]

若中间量 $b$ 被实际测量，即使测量结果随后不被使用，干涉也被破坏，概率按经典互斥事件相加：

\[
P_{ac}=\sum_b P_{ab}P_{bc}.
\]

路径积分就是把这个规则从有限个 alternative ways 推到连续无穷条时空路径。给定路径 $x(t)$，第二公设指定其贡献大小相等、相位由 classical action 决定：

\[
\mathcal C[x(t)]\propto \exp\left(\frac{i}{\hbar}S[x]\right),
\qquad
S[x]=\int_{t_a}^{t_b} L(x,\dot x,t)\,dt.
\]

因此，到达 $(x,t)$ 的 wave function 是所有从过去制备条件出发并抵达该点的路径贡献和：

\[
\psi(x,t)=\sum_{\text{paths ending at }(x,t)} \mathcal C[x(t)].
\]

更严格地说，费曼先用时间格点定义路径：$t_j=t_a+j\epsilon$，路径由中间坐标 $x_1,\ldots,x_{N-1}$ 指定；最后才取 $\epsilon\to0$。他特别强调这个限制过程不是数学装饰，而是当时避免“对函数空间定义复测度”困难的实际定义。

### 2. Propagator $K(b,a)$ 的构造

设 $a=(x_a,t_a)$、$b=(x_b,t_b)$，传播子 $K(b,a)$ 是从 $a$ 到 $b$ 的总 probability amplitude。把时间区间分为 $N$ 段，$\epsilon=(t_b-t_a)/N$，固定 $x_0=x_a$、$x_N=x_b$，则

\[
K(b,a)=\lim_{\epsilon\to0}\frac{1}{A^N}
\int dx_1\cdots dx_{N-1}
\exp\left[\frac{i}{\hbar}\sum_{j=0}^{N-1}S(x_{j+1},x_j)\right].
\]

其中 $S(x_{j+1},x_j)$ 是在短时间 $[t_j,t_{j+1}]$ 内、连接两端点的 classical path 上的作用量：

\[
S(x_{j+1},x_j)=\int_{t_j}^{t_{j+1}}L(x,\dot x,t)\,dt.
\]

连续极限写成现代符号就是泛函积分：

\[
K(b,a)=\int_{x(t_a)=x_a}^{x(t_b)=x_b}\mathcal D x(t)\,
\exp\left(\frac{i}{\hbar}S[x]\right).
\]

对自由粒子 $L=m\dot x^2/2$，短时传播子为

\[
K(x',t+\epsilon;x,t)
=\left(\frac{m}{2\pi i\hbar\epsilon}\right)^{1/2}
\exp\left[\frac{i}{\hbar}\frac{m(x'-x)^2}{2\epsilon}\right].
\]

费曼用 $1/A$ 表示每个时间片的归一化，故一维自由粒子中

\[
A=\left(\frac{2\pi i\hbar\epsilon}{m}\right)^{1/2}.
\]

若有标量势 $V(x)$，短时作用量可取

\[
S(x_{j+1},x_j)\simeq
\frac{m(x_{j+1}-x_j)^2}{2\epsilon}
-\epsilon V(x_{j+1}),
\]

或等价地取中点形式：

\[
S(x_{j+1},x_j)\simeq
\epsilon L\left(\frac{x_{j+1}-x_j}{\epsilon},
\frac{x_{j+1}+x_j}{2}\right).
\]

有 vector potential 或速度线性项时，中点处方不能随意改成端点处方，否则会改变 $O(\epsilon)$ 项并导致算符排序错误。费曼指出，正确的短时 action 定义会自动解析 $p$ 与 $q$ 非对易带来的 ordering ambiguity。

### 3. 组合律与 Schrödinger 方程等价性

由于 action 对相邻时间片可加，

\[
S[x]=\sum_j S(x_{j+1},x_j),
\]

传播子满足 Chapman-Kolmogorov 型组合律：

\[
K(c,a)=\int db\,K(c,b)K(b,a),
\]

坐标表象中更明确地写为

\[
K(x_c,t_c;x_a,t_a)
=\int dx_b\,
K(x_c,t_c;x_b,t_b)K(x_b,t_b;x_a,t_a).
\]

wave function 的一步演化为

\[
\psi(x',t+\epsilon)
=\int \frac{dx}{A}\,
\exp\left[\frac{i}{\hbar}S(x',x)\right]\psi(x,t).
\]

对 $L=m\dot x^2/2-V(x)$，令 $x'=x$、$x_{\text{old}}=x-\xi$，得到

\[
\psi(x,t+\epsilon)
=\frac{1}{A}\exp\left[-\frac{i\epsilon}{\hbar}V(x)\right]
\int d\xi\,
\exp\left(\frac{im\xi^2}{2\hbar\epsilon}\right)
\psi(x-\xi,t).
\]

由于 $\epsilon\to0$ 时快速振荡使主要贡献来自 $\xi\sim(\hbar\epsilon/m)^{1/2}$，展开

\[
\psi(x-\xi,t)=\psi(x,t)-\xi\partial_x\psi(x,t)
+\frac{\xi^2}{2}\partial_x^2\psi(x,t)+\cdots.
\]

用 Gaussian 型振荡积分

\[
\int d\xi\,e^{im\xi^2/(2\hbar\epsilon)}
=\left(\frac{2\pi i\hbar\epsilon}{m}\right)^{1/2},
\]

\[
\int d\xi\,\xi^2 e^{im\xi^2/(2\hbar\epsilon)}
=\frac{i\hbar\epsilon}{m}
\left(\frac{2\pi i\hbar\epsilon}{m}\right)^{1/2},
\]

并取 $A=(2\pi i\hbar\epsilon/m)^{1/2}$，保留 $O(\epsilon)$ 项，得到

\[
i\hbar\frac{\partial\psi}{\partial t}
=-\frac{\hbar^2}{2m}\frac{\partial^2\psi}{\partial x^2}
+V(x)\psi.
\]

这就是 Schrödinger equation。反过来，若从 Schrödinger 演化算符出发，

\[
\psi(t+\epsilon)=\exp\left(-\frac{i\epsilon H}{\hbar}\right)\psi(t),
\]

则短时传播子正是坐标表象的 transformation function：

\[
(x'|x)_\epsilon\simeq \frac{1}{A}
\exp\left[\frac{i}{\hbar}S(x',x)\right].
\]

所以路径积分不是近似图像，而是在上述短时极限和归一化下与 Schrödinger 表述等价。

### 研究者复核：时间切片、归一化和方程极限

The free-kernel normalization follows from the identity limit,
\[
\lim_{\epsilon\downarrow0}\int dx\,K_0(x',t+\epsilon;x,t)f(x)=f(x').
\]
With the branch obtained by \(\epsilon\to\epsilon-i0\), the Gaussian moments already displayed give
\[
\psi(t+\epsilon)=\psi+\epsilon\left(\frac{i\hbar}{2m}\partial_x^2-\frac{i}{\hbar}V\right)\psi+o(\epsilon),
\]
which establishes the Schrödinger limit for smooth \(V\) and \(\psi\). Singular potentials require a separately defined short-time kernel.

For velocity-dependent actions, midpoint slicing fixes an operator-ordering prescription; it is not merely an interchangeable quadrature rule. Thus \(\mathcal D x\) denotes the stated time-sliced oscillatory limit, not a real probability measure. Likewise, classical paths dominate only as a stationary-phase asymptotic under the usual nondegeneracy assumptions, rather than through a literal least-action selection.

### 4. 与矩阵力学和算符代数的关系

费曼把通常的 matrix element 改写为跨越一段时间的 transition element。若初态在 $t'$ 为 $\psi$、末态实验在 $t''$ 由 $\chi$ 表示，则

\[
(\chi|1|\psi)_S
=\int dx''dx'\,\chi^*(x'',t'')K(x'',t'';x',t')\psi(x',t').
\]

对路径 functional $F[x]$，定义

\[
(\chi|F|\psi)_S
=\lim_{\epsilon\to0}
\int \chi^*(x_N,t'')F(x_0,\ldots,x_N)
\exp\left(\frac{iS}{\hbar}\right)\psi(x_0,t')
\prod_j\frac{dx_j}{A}.
\]

若 $F$ 对某个中间坐标 $x_k$ 可微，对 $x_k$ 分部积分可得核心恒等式：

\[
\left(\chi\left|\frac{\partial F}{\partial x_k}\right|\psi\right)_S
=-\frac{i}{\hbar}
\left(\chi\left|F\frac{\partial S}{\partial x_k}\right|\psi\right)_S.
\]

等价地，

\[
\frac{\hbar}{i}\frac{\partial F}{\partial x_k}
\sim_S
F\frac{\partial S}{\partial x_k}.
\]

对简单势场，

\[
\frac{\partial S}{\partial x_k}
=-\frac{m(x_{k+1}-x_k)}{\epsilon}
+\frac{m(x_k-x_{k-1})}{\epsilon}
-\epsilon V'(x_k).
\]

取 $F=1$，除以 $\epsilon$ 后得到矩阵形式的 Newton equation：

\[
m\frac{(x_{k+1}-x_k)/\epsilon-(x_k-x_{k-1})/\epsilon}{\epsilon}
\sim_S -V'(x_k).
\]

取 $F=x_k$，并按时间顺序把较晚时刻的因子放在算符乘积左侧，可得

\[
px-xp=\frac{\hbar}{i},
\]

即

\[
[p,q]=\frac{\hbar}{i}.
\]

这里的要点是：path functional 中普通乘法本身可交换，但翻译回 operator product 时，时间顺序决定算符顺序；非对易性正是从“相邻时间点的坐标因子如何映射成同一时刻算符”中出现。

### 5. 经典极限：stationary phase 与最小作用量

有限时间传播可写为

\[
\psi(x'',t'')=
\lim_{\epsilon\to0}\int
\exp\left[\frac{i}{\hbar}\sum_{j=0}^{N-1}S(x_{j+1},x_j)\right]
\psi(x',t')\prod_{j=0}^{N-1}\frac{dx_j}{A}.
\]

当 $\hbar\to0$ 时，指数相位快速振荡。除非相位对每个中间坐标的一阶变分为零，邻近路径贡献会相互抵消。因此主导贡献满足

\[
\frac{\partial}{\partial x_k}\sum_j S(x_{j+1},x_j)=0
\qquad \forall k.
\]

连续极限就是

\[
\delta S[x]=\delta\int_{t_a}^{t_b}L(x,\dot x,t)\,dt=0.
\]

这恢复 Hamilton principle / principle of least action，并给出 Euler-Lagrange equation：

\[
\frac{d}{dt}\frac{\partial L}{\partial \dot x}
-\frac{\partial L}{\partial x}=0.
\]

因此 classical path 不是额外假设，而是 $\hbar$ 很小时 stationary phase 后留下的相干贡献。费曼把它类比为几何光学从波动光学的短波长极限中出现：matter wave 的 Huygens principle 中，相位延迟由 action 而不是光程时间给出。

### 6. 测量、几率与干涉

路径积分的概率规则始终是

\[
P(R)=|\phi(R)|^2,
\qquad
\phi(R)=\sum_{\text{paths in }R}\mathcal C[x].
\]

若测量只问“路径是否在区域 $R$ 中”，而不区分 $R$ 内具体路径，则 $R$ 内路径幅相加后再取模平方：

\[
P(R)=\left|\int_R\mathcal D x\,e^{iS[x]/\hbar}\right|^2.
\]

若中间位置或路径细节被真实测量，路径按测量结果分成互斥类别，概率而非概率幅相加：

\[
P=\sum_\alpha |\phi_\alpha|^2.
\]

若没有中间观测，则

\[
P=\left|\sum_\alpha \phi_\alpha\right|^2.
\]

这一区别是论文实验哲学的核心：不是粒子“实际上是否经过某条路径”的经典问题，而是实验设置是否允许那些 alternatives 发生干涉。费曼把测量扰动解释为中间装置引入不可控相位或记录，使不同分量不能再作为同一个 amplitude coherent 地相加。

### 7. 应用：消去场振子坐标

论文最后的关键应用是“先积分掉 harmonic oscillator / field oscillator 坐标，再处理粒子路径”。这正是后来 QED spacetime approach 的技术前身。

设粒子坐标为 $x(t)$，自身 action 为 $S_x$；一个 oscillator 坐标 $q(t)$，频率 $\omega$，与粒子通过

\[
L_{\text{int}}=y(x,t)q(t)
\]

耦合。总 action 分成

\[
S=S_x+S_q+S_{\text{int}},
\]

\[
S_q=\int_{t'}^{t''}\frac{1}{2}(\dot q^2-\omega^2q^2)\,dt,
\qquad
S_{\text{int}}=\int_{t'}^{t''}y(x(t),t)q(t)\,dt.
\]

在离散表达中，$q_1,\ldots,q_{N-1}$ 只以二次型出现，因此对所有中间 $q_j$ 的积分是 Gaussian path integral。结果是粒子路径振幅中多出一个只依赖 $x(t)$ 历史的 influence functional：

\[
\int \mathcal Dq\,
\exp\left[\frac{i}{\hbar}(S_q+S_{\text{int}})\right]
=G[y]\,
\exp\left(\frac{i}{\hbar}S_{\text{osc,cl}}[y]\right).
\]

这里 $S_{\text{osc,cl}}[y]$ 是受外源 $y(x(t),t)$ 驱动的 classical forced oscillator action。若 oscillator 初末态也指定为能级 $n,m$，则还要对端点 $q_0,q_N$ 与对应 oscillator wave functions 做积分：

\[
G_{mn}[x]=\int dq_Ndq_0\,
\varphi_m^*(q_N)
\exp\left[\frac{i}{\hbar}Q(q_N,q_0;y)\right]
\varphi_n(q_0).
\]

消去后，粒子 transition amplitude 变为

\[
(\chi,m|1|\psi,n)
=\int \mathcal D x\,
\chi^*(x'',t'')G_{mn}[x]
\exp\left(\frac{i}{\hbar}S_x[x]\right)
\psi(x',t').
\]

物理意义：场的 oscillator 坐标充当“记忆”粒子过去运动的自由度。传统 wave function $\psi(x_a,x_b,t)$ 只能描述同一时刻的坐标，难以直接表达一个粒子现在受另一个粒子过去运动影响；路径积分保留整条历史，允许把场自由度积分掉，得到非局域于时间的有效作用量。这为费曼 1949 年 QED 论文中的 photon propagator、retarded/interparticle spacetime interaction 和 Feynman diagram 展开铺路。

### 8. 可计算离散化骨架

对一维势场问题，最小实现可以按如下结构理解：

```text
given x_a, t_a, x_b, t_b, N
epsilon = (t_b - t_a) / N
A = sqrt(2*pi*i*hbar*epsilon/m)
integrand(x_1,...,x_{N-1}):
    S = sum_j [m*(x_{j+1}-x_j)^2/(2*epsilon) - epsilon*V(x_{j+1})]
    return exp(i*S/hbar) / A^N
K = integral over x_1,...,x_{N-1} of integrand
```

Schrödinger 方程推导对应的是只保留单步 kernel 的 $O(\epsilon)$ 展开；数值路径积分、imaginary-time Monte Carlo、PIMD 则通常做 Wick rotation $t=-i\tau$，把振荡权重变成阻尼权重：

\[
e^{iS/\hbar}\longrightarrow e^{-S_E/\hbar}.
\]

### 9. 历史影响

量子场论：路径积分把“对历史求和”推广为“对场构型求和”，

\[
Z[J]=\int\mathcal D\phi\,
\exp\left[\frac{i}{\hbar}\left(S[\phi]+\int J\phi\right)\right],
\]

微扰展开中的 Wick contraction 与传播子组合直接导向 Feynman diagrams。1948 这篇文中消去 oscillator 的思路，已经包含后来“积分掉场自由度得到有效相互作用”的雏形。

统计力学：虚时路径积分给出配分函数

\[
Z=\operatorname{Tr}e^{-\beta H}
=\int_{\text{periodic}}\mathcal D x(\tau)\,
e^{-S_E[x]/\hbar},
\]

把量子热力学问题映射为多一维的 Euclidean classical statistical problem。

凝聚态多体：coherent-state path integral、Grassmann path integral、Hubbard-Stratonovich transformation、effective action 和 Green function 形式，都继承了这篇论文的“积分掉自由度、保留有效作用量/核”的视角。

量子蒙特卡洛与 PIMD：Wick rotation 后的单粒子路径等价于 imaginary time ring polymer；$N$ 个 time slices 对应 $N$ 个 beads，短时 action 给出相邻 beads 的 harmonic spring，加上物理势能项。这就是 path-integral Monte Carlo 与 path-integral molecular dynamics 的基本计算结构，也与库内 `path-integral-molecular-dynamics` 一脉直接相连。

## Review Questions

Review Questions
1. 如果把这篇 1948 论文中的离散短时传播子形式，推广到量子多体中的高维相空间路径积分，哪些步骤会最先遇到测度与排序问题？这种问题与 PDE 机器学习里用离散时间推进逼近连续半群时的误差结构有何对应关系？
2. 费曼把“积分掉场自由度”作为处理 QED 的基本思路。若把同样思想用于流体力学中的不可压缩约束或随机湍流建模，哪些自由度应被视为“可积去”的辅助变量，哪些量必须保留为有效作用量或约束？
3. 从 HPC 与数值计算角度看，路径积分离散化本质上是高维振荡积分。若要把这一框架用于量子多体或机器学习中的核近似，怎样设计并行分解、重要性采样或低秩近似，才能在保持相位信息的同时控制计算成本？
