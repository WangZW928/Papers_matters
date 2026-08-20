# Discovering governing equations from data by sparse identification of nonlinear dynamical systems

**Source PDF:** `brunton-et-al-2016-discovering-governing-equations-from-data-by-sparse-identification-of-nonlinear-dynamical-systems.pdf`

**阅读状态：** 🔬 精读
**流程状态：** ①元数据 ✓ | ②初稿 ✓ | ③评估 ✓(精读) | ④补充 ✓ | ⑤索引 ✓ | ⑥review ✓ | ⑦提交 ⏳

---

## 摘要

### 中文翻译

SINDy（Brunton 等，PNAS 2016）：自然规律在合适函数库中往往是稀疏的，方程发现可化为稀疏回归——构建候选函数库 Θ(X)，用稀疏回归（如 STRidge）从数据中识别控制方程。

## 价值评估

Doctor 指定精读。SINDy 把“合适函数库中的稀疏规律”化为线性系数回归；其可解释外推依赖观测变量充分、导数估计可靠且候选库含有正确项。离散模拟数据还可能使它恢复 modified equation，而非连续方程。

## 公式与代码梳理

### 数学结构与核心公式

SINDy 研究自治动力系统

$$
\frac{d}{dt}\mathbf{x}(t)=\mathbf{f}(\mathbf{x}(t)),
\qquad
\mathbf{x}(t)\in\mathbb{R}^n.
$$

给定 $m$ 个采样时刻 $t_1,\dots,t_m$，构造状态矩阵和导数矩阵：

$$
X=
\begin{bmatrix}
\mathbf{x}(t_1)^T\\
\mathbf{x}(t_2)^T\\
\vdots\\
\mathbf{x}(t_m)^T
\end{bmatrix}
\in\mathbb{R}^{m\times n},
\qquad
\dot{X}=
\begin{bmatrix}
\dot{\mathbf{x}}(t_1)^T\\
\dot{\mathbf{x}}(t_2)^T\\
\vdots\\
\dot{\mathbf{x}}(t_m)^T
\end{bmatrix}.
$$

核心假设是 $\mathbf{f}$ 在候选函数库 $\Theta(X)$ 中稀疏展开：

$$
\dot{X}=\Theta(X)\Xi.
$$

其中 $\Theta(X)\in\mathbb{R}^{m\times p}$ 的列是候选非线性项，例如

$$
\Theta(X)=
\begin{bmatrix}
\mathbf{1} & X & X^{P_2} & X^{P_3} & \sin(X) & \cos(X) & \cdots
\end{bmatrix}.
$$

若 $\mathbf{x}=(x,y,z)$，二阶多项式库可包含

$$
1,\ x,\ y,\ z,\ x^2,\ xy,\ xz,\ y^2,\ yz,\ z^2.
$$

系数矩阵 $\Xi\in\mathbb{R}^{p\times n}$ 的第 $k$ 列 $\xi_k$ 给出第 $k$ 个状态方程：

$$
\dot{x}_k=\Theta(\mathbf{x})\xi_k.
$$

稀疏回归目标可写作

$$
\xi_k
=
\arg\min_{\xi}
\left\|\dot{X}_k-\Theta(X)\xi\right\|_2^2
+\lambda\|\xi\|_0,
$$

实际求解常用近似算法，例如 LASSO：

$$
\xi_k
=
\arg\min_{\xi}
\left\|\dot{X}_k-\Theta(X)\xi\right\|_2^2
+\lambda\|\xi\|_1,
$$

或 sequential thresholded least squares / ridge。STRidge 的基本迭代是先解岭回归

$$
\xi^{(r)}
=
\arg\min_{\xi}
\left\|\dot{X}_k-\Theta(X)\xi\right\|_2^2
+\alpha\|\xi\|_2^2,
$$

再按阈值 $\lambda$ 剪枝：

$$
\xi_j^{(r)}=0
\quad\text{if}\quad
|\xi_j^{(r)}|<\lambda,
$$

然后在保留支撑集 $S=\{j:|\xi_j|\geq\lambda\}$ 上重新回归。最终得到稀疏模型

$$
\dot{\mathbf{x}}=
\begin{bmatrix}
\Theta(\mathbf{x})\xi_1 &
\Theta(\mathbf{x})\xi_2 &
\cdots &
\Theta(\mathbf{x})\xi_n
\end{bmatrix}.
$$

代码实现上，SINDy 的 pipeline 很直接：`differentiate(X)` 得到 $\dot{X}$，`build_library(X)` 得到 $\Theta$，`sparse_regression(Theta, dXdt)` 得到 $\Xi$，`print_equations(Theta_names, Xi)` 输出显式方程。最脆弱的是第一步导数估计。若数据噪声为 $\epsilon$，有限差分会放大为 $O(\epsilon/\Delta t)$；因此实际代码常加入 Savitzky-Golay、total variation regularized derivative、弱形式积分或神经平滑器。

### 关键推导

第一步是把非线性动力学转写为线性参数问题。虽然 $\mathbf{f}(\mathbf{x})$ 对状态是非线性的，但一旦候选库固定，未知只剩线性系数：

$$
\dot{x}_k(t_i)=
\sum_{j=1}^{p}\Theta_j(\mathbf{x}(t_i))\xi_{jk}.
$$

因此每个状态分量都变成一个高维线性回归问题。SINDy 的力量来自“非线性在特征中，稀疏在线性系数中”。

第二步是稀疏性选择。若真实动力学只含少数项，支撑集 $S^\star$ 远小于候选库大小 $p$。顺序阈值回归近似求解

$$
S^\star=\operatorname{supp}(\xi),
\qquad
\xi_{S^\star}
=
\arg\min_{\eta}
\left\|\dot{X}_k-\Theta_{S^\star}(X)\eta\right\|_2^2.
$$

它交替执行“估计系数”和“删除小系数”，类似物理建模中的项筛选。

第三步是模型验证。得到 $\Xi$ 后，需要积分

$$
\frac{d}{dt}\hat{\mathbf{x}}=\Theta(\hat{\mathbf{x}})\Xi
$$

并与原始轨迹比较。只看 one-step derivative error 不够，因为错误项可能在长期积分中被非线性放大。

### 对 HPC 框架的启示

SINDy 对 Doctor 的 HPC 框架最直接的价值是 closure discovery。对于 LES、AMR coarse-grid correction、量子涡 coarse-graining，可把未闭合项写作

$$
\mathcal{R}(U)=\partial_t U-\mathcal{N}_{\text{resolved}}(U),
$$

再用候选库 $\Theta(U,\nabla U,\nabla^2 U,\dots)$ 稀疏识别 $\mathcal{R}$。这比黑箱网络更容易进入生产级 solver，因为输出是显式项，可做稳定性、量纲和守恒分析。

第二个结合点是 PDE-FIND。对 PDE

$$
u_t=\mathcal{F}(u,u_x,u_{xx},\dots),
$$

候选库可扩展为

$$
\Theta(u)=
\begin{bmatrix}
1 & u & u^2 & u_x & uu_x & u_{xx} & u^2u_x & \cdots
\end{bmatrix}.
$$

这与仓库里的 PINN、Neural Operator、JFNK 文档可互补：PINN 偏连续约束，Neural Operator 偏快速替代求解器，SINDy 偏显式方程发现，JFNK 则可用已发现项构造隐式残差。

第三个结合点是结构保持发现。对 Hamiltonian / Lie-Poisson 系统，不应直接对 $\dot{x}=f(x)$ 做任意库回归，而应识别 Hamiltonian、Poisson tensor 或耗散 bracket：

$$
\dot{z}=J(z)\nabla H(z),
\qquad
\dot{\mu}=\operatorname{ad}_{\delta h/\delta\mu}^{*}\mu.
$$

这样可避免 SINDy 找到短期准确但破坏 Casimir 的模型。

### 待深入研究

1. 如何为理想流体、MHD、GPE 构造满足量纲、对称性、守恒律的候选库，而不是盲目枚举多项式？
2. 弱形式 SINDy 与有限体积残差能否合并，在 AMR patch 上直接识别 conservative flux closure？
3. 如何把 SINDy 的稀疏显式项作为 Neural Operator 的可解释残差分支，形成 hybrid model？

## Review Questions

1. 对 Hamiltonian ideal fluid，SINDy 应识别速度方程、涡量方程、Hamiltonian density，还是 Poisson bracket？哪一种最能保证长期结构？
2. 如果训练数据来自数值求解器而非真实物理，SINDy 发现的是连续方程、离散 modified equation，还是求解器误差模型？
3. 在 GPU/AMR 框架中，候选库 $\Theta$ 的构造是否会成为比稀疏回归本身更大的性能瓶颈？
