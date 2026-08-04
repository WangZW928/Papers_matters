# 带对称性的偏微分方程量子力学闭包

# Quantum Mechanical Closure of Partial Differential Equations with Symmetries

**作者：** Chris Vales, David C. Freeman, Joanna Slawinska, Dimitrios Giannakis
**期刊：** Journal of Computational Physics (2026) 114992; arXiv:2505.07519v3（JCP/DOI 信息来自外部出版页，本地全文仅标注 arXiv:2505.07519v3 [math.DS] 16 Mar 2026）
**DOI：** [https://doi.org/10.1016/j.jcp.2026.114992](https://doi.org/10.1016/j.jcp.2026.114992)（待外部核实）
**arXiv：** [https://arxiv.org/abs/2505.07519](https://arxiv.org/abs/2505.07519)
**阅读状态：** 🔬 精读（Doctor 指定）
**流程状态：** ①元数据 ✓ | ②初稿 ✓ | ③评估 ✓(精读) | ④补充 ✓ | ⑤索引 ✓ | ⑥review ✓ | ⑦提交 ✓

---

## 摘要

### 中文翻译
发展了一个统计框架，用于受 PDE 支配的时空动力学的动力学闭包（dynamical closure）。借用量子力学数学框架把经典动力学嵌入量子力学表示：用量子密度算子空间以统计意义建模原始动力学的未解析自由度，用量子测量框架预测它们对已解析动力学的贡献。嵌入动力学通过保正（positivity preserving）过程离散化，得到在已解析动力学对称性下不变的压缩表示。给出闭包方案的数据驱动表述，并应用于浅水方程闭包问题。数值结果证明闭包模型能准确预测真实动力学的主要特征（含样本外初始条件）。

### 原文
> We develop a statistical framework for the dynamical closure of spatiotemporal dynamics governed by partial differential equations. Employing the mathematical framework of quantum mechanics to embed the original classical dynamics into a quantum mechanical representation, we use the space of quantum density operators to model the unresolved degrees of freedom of the original dynamics in a statistical sense, and the framework of quantum measurement to predict their contributions to the resolved dynamics. The embedded dynamics is discretized by a positivity preserving process, leading to a compressed representation that is invariant under the dynamical symmetries of the resolved dynamics.

---

## 文章总结

### 1. 解决什么问题？
如何对受 PDE 支配的时空动力学做系统性的动力学闭包（参数化未解析尺度）？

### 2. 用了什么方法论？
量子力学嵌入：经典场 → 量子密度算子表示；未解析自由度用密度算子统计建模，量子测量预测其对已解析自由度的反馈；保正离散化 + 核方法/延迟嵌入/迁移算子，得到对称性不变的压缩表示；数据驱动公式 + 浅水方程验证。

### 3. 主要结论是什么？
量子力学框架为动力系统闭包提供新途径：密度算子表示未解析自由度、量子测量作为反馈预测，压缩表示保持动力学对称性；浅水方程上准确预测包括样本外初始条件的主要特征。

---

## 价值评估

Doctor 指定精读（跳过 Codex 价值评估）。

## 公式与代码梳理

### 1. 闭包问题的数学骨架

论文从一般动力系统出发。设原始 PDE 生成离散时间动力学 $\Phi^n:X\to X$（$\Phi$ 是连续时间动力学的时间离散版本），并把状态空间分解为

$$
X=X_r\oplus X_u,
$$

其中 $X_r$ 是已解析/粗粒化自由度，$X_u=X_r^\perp$ 是未解析自由度。若 $u\in X$，则粗变量可写为 $\hat u=\operatorname{proj}_r(u)$。闭包困难来自：粗变量的演化并不只依赖 $\hat u$，还依赖被投影掉的细尺度信息。

论文用一个空间平均的标量输运方程说明这一点：

$$
\partial_t u+c\partial_xu=F(u),
$$

局部平均后得到

$$
\partial_t\hat u+c\partial_x\hat u=F(\hat u)+G(\hat u,u),
$$

其中残差/通量项为

$$
G(\hat u,u)(x)
=
\frac{1}{\ell}\int_{x-\ell/2}^{x+\ell/2}F(u)(y)\,dy
-
F(\hat u)(x).
$$

这里 $G$ 就是闭包目标：它显式依赖完整细尺度状态 $u$，但在线预测时只希望用粗变量 $\hat u$ 来近似。

### 2. 经典动力学到量子力学表示的嵌入

论文的关键不是使用量子硬件，而是借用量子力学的算子语言，把经典统计闭包写成 Hilbert 空间上的密度算子演化。

对 PDE 闭包，作者使用乘积空间

$$
\Omega=X\times S,
$$

其中 $S$ 是空间区域，并定义 spatiotemporal observable 的 Hilbert 空间

$$
\mathcal H=L^2(\Omega,\sigma;\mathbb C),
\qquad
\sigma=\mu\times\nu.
$$

$\mu$ 是原动力学的不变概率测度，$\nu$ 是空间 Lebesgue 测度。一个经典概率密度 $p\in L^1(X,\mu)$（ODE 版本）被嵌入为纯量子态，即秩一密度算子

$$
\rho=\langle \sqrt p,\cdot\rangle \sqrt p.
$$

PDE 闭包版本把这一构造逐点推广：$\Omega=X\times S$ 上每个空间点 $x\in S$ 对应一个局部密度 $p_x\in L^1(\Omega)$，由它得到局部 density field $\rho(x)$——即每个粗网格 cell 一个密度算子，而不是全局单一密度算子。

量子密度算子满足

$$
\rho\succeq 0,\qquad \rho^\ast=\rho,\qquad \operatorname{tr}\rho=1.
$$

经典可观测量 $f\in L^\infty(X,\mu)$ 被嵌入为乘法算子 $A$：

$$
Ag=fg,\qquad g\in\mathcal H.
$$

于是通量估计变成量子测量期望：

$$
\mathbb E_\rho A=\operatorname{tr}(\rho A).
$$

这对应经典统计闭包里的

$$
\int_X f(u)p(u)\,d\mu(u),
$$

但在有限维离散化后保留为矩阵-向量/矩阵-矩阵形式。

### 3. Koopman / Perron-Frobenius 视角

在经典统计动力学中，密度随动力学由 Perron-Frobenius/transfer operator 推进。若 $P:\mathcal H\to\mathcal H$ 表示迁移算子，则

$$
P\sqrt p=\sqrt p\circ\Phi^{-1}.
$$

密度算子的推进由共轭作用给出：

$$
\rho_{n+1}=P\rho_nP^{-1}.
$$

（理论上 $P\rho=P\rho P^{-1}$ 是严格共轭推进；数据实现中的 $P_N^L$ 是 shift operator 投影后再归一化得到的有限维矩阵，一般非正交，不是完整可逆算子的共轭。）

这也是 Koopman-von Neumann 表示的核心：经典动力学不再只作用在点态 $u_n$ 上，而作用在 Hilbert 空间中的波函数/密度表示上。与常见 Koopman 方法的联系是：Koopman 侧重可观测量演化，Perron-Frobenius 侧重密度演化；本文闭包模型主要使用 density/operator side，但核特征空间和迁移算子的离散化仍然属于 Koopman 谱方法家族。

### 4. 未解析自由度的空间场表示

原始 QMCl 只给整个系统一个密度算子。本文扩展到 PDE 时，把未解析自由度表示为空间上的密度算子场：

$$
\rho:S\to B(\mathcal H),
\qquad
x\mapsto \rho(x).
$$

每个空间网格点 $x_m$ 有一个密度算子 $\rho(x_m)$，用于统计描述该位置附近未解析尺度的状态。若 PDE 有 $d$ 个物理变量，则需要 $d$ 个通量可观测量 $A_j$，$j=0,\dots,d-1$。预测的闭包通量为

$$
\tilde f_j(x_m)=\operatorname{tr}(\rho(x_m)A_j).
$$

在有限维基底中，若 $\rho(x_m)$ 是秩一态，由向量 $\rho_m\in\mathbb R^L$ 表示，则

$$
\tilde f_j(x_m)=\rho_m^\top A_j\rho_m.
$$

这点很重要：闭包不是学习一个确定函数 $G(\hat u)$，而是维护一个随时间演化和被观测修正的局部统计态 $\rho(x_m)$。

### 5. 量子测量与 Bayes 修正

每步在线预测包含两个信息流：

1. 密度算子给粗模型提供闭包通量；
2. 更新后的粗状态反过来修正密度算子。

修正使用量子 Bayes 公式。给定量子 effect operator $e\succeq0$，

$$
\rho\mid e
=
\frac{\sqrt e\,\rho\,\sqrt e}{\mathbb E_\rho e}
=
\frac{\sqrt e\,\rho\,\sqrt e}{\operatorname{tr}(\rho e)}.
$$

在实现中，effect operator 来自当前粗状态与训练集中局部模式的相似度。论文定义局部 stencil embedding $W_J$，例如一维网格上

$$
W_J((u,x_m))
=
\big(
\operatorname{proj}_r(u)(x_{m-(J-1)/2}),
\dots,
\operatorname{proj}_r(u)(x_m),
\dots,
\operatorname{proj}_r(u)(x_{m+(J-1)/2})
\big),
$$

再用高斯核构造相似度：

$$
k_c(W_J(\omega),W_J(\omega'))
=
\exp\left(
-\frac{1}{\epsilon'J}
\|W_J(\omega)-W_J(\omega')\|^2
\right).
$$

对当前局部状态（在线阶段由当前粗状态/ resolved state $\tilde u$ 的局部 stencil 与训练 resolved samples 比较得到，不依赖真实 fine state），核函数生成 feature vector

$$
f_m(\cdot)=\kappa_c(\omega_m,\cdot),
$$

再由 $f_m^{1/2}$ 构造 effect operator $e_m$。有限维秩一态更新写作

$$
\rho_m\mid e_m
=
\frac{e_m\rho_m}{\|e_m\rho_m\|_2}.
$$

因此，QMCl 的在线阶段类似“预测-校正”滤波器：transfer operator 给先验，quantum Bayes 给后验。

### 6. 保正离散化

论文强调的一个技术优势是 positivity preserving。若经典通量函数 $f_j$ 是非负的，则对应乘法算子 $\tilde A_j$ 是正算子；投影到有限维子空间后

$$
A_j=\operatorname{proj}_L \tilde A_j\operatorname{proj}_L
$$

仍保持正性：

$$
f_j\ge 0
\quad\Longrightarrow\quad
A_j\succeq0.
$$

更一般地，若 $f_j$ 是 sign definite 函数（正定或负定），投影后的可观测量也保持符号，从而 surrogate flux 与真实 flux 符号一致。

因此对任意密度算子 $\rho\succeq0$，

$$
\operatorname{tr}(\rho A_j)\ge0.
$$

这比直接把函数 $f_j$ 投影成有限维系数向量更稳健，因为普通谱截断可能破坏符号。代价是维度更高：直接函数离散是 $L$ 维，而自伴算子空间规模约为

$$
\frac{1}{2}L(L+1).
$$

所以 QMCl 用更多内存和矩阵计算换取保正性与更强统计表达能力。

### 7. 对称性不变的压缩表示：核方法与延迟嵌入

有限维空间 $\mathcal H_N^L$ 由核积分算子的前 $L$ 个特征函数张成。核算子为

$$
Kf
=
\int_\Omega \kappa(\cdot,\omega)f(\omega)\,d\sigma(\omega).
$$

核函数不是直接比较全状态，而是比较粗变量的时间延迟嵌入：

$$
W_Q((u,x))
=
\big(
\operatorname{proj}_r(u)(x),
\operatorname{proj}_r(\Phi^{-1}(u))(x),
\dots,
\operatorname{proj}_r(\Phi^{-(Q-1)}(u))(x)
\big),
$$

$$
\kappa(\omega,\omega')
=
\exp\left(
-\frac{1}{\epsilon Q}
\|W_Q(\omega)-W_Q(\omega')\|^2
\right).
$$

若 resolved dynamics 对群 $G$ 等变（前提：群作用保持测度 $\nu$、$X_r$ 对群作用不变、resolved dynamics 等变、flux functions 满足相应等变性）：

$$
\Phi_r^n\circ\Gamma_{X,g}
=
\Gamma_{r,g}\circ\Phi_r^n,
$$

则由 $W_Q$ 诱导的等价类中，对称轨道包含在 delay map 的等价类内（对称变换后的样本归为同类，但等价类不一定只由对称轨道组成）。核函数在这些等价类上常数，因此 $K$ 的值域函数满足

$$
f\circ\Gamma_{\Omega,g}=f.
$$

这意味着特征函数天然对 resolved dynamics 的对称性不变。对于周期边界 PDE，特别是一维浅水方程，平移对称性会被自动因子化，不需要把训练集人为扩增为所有平移副本。相比 POD 那种“时间模态 $\otimes$ 空间模态”的张量积基，本文的核特征函数可以直接表示非可分的时空结构，因此压缩效率更高。

### 8. 浅水方程闭包设置

应用问题是一维周期浅水方程：

$$
\partial_t h+\partial_x q=0,
$$

$$
\partial_t q+
\partial_x\left(
\frac{q^2}{h}
+\frac{1}{2}Fr^{-2}h^2
\right)=0.
$$

写成守恒律形式：

$$
\partial_tu+\partial_x f(u)=0,
\qquad
u=(h,q),
$$

$$
f(u)=
\left(
q,
\frac{q^2}{h}+\frac{1}{2}Fr^{-2}h^2
\right).
$$

真值模型使用细网格有限体积离散。细网格 cell average 满足

$$
\dot u_m
=
\frac{1}{\Delta x}
(F_m-F_{m+1}),
$$

局部 Lax-Friedrichs 数值通量为

$$
F_m
=
\frac12[f(u_{m-1})+f(u_m)]
-
\frac{\lambda_m}{2}(u_m-u_{m-1}),
$$

$$
\lambda_m
=
\max\left(
\left|\frac{q_{m-1}}{h_{m-1}}\right|+Fr^{-1}\sqrt{h_{m-1}},
\left|\frac{q_m}{h_m}\right|+Fr^{-1}\sqrt{h_m}
\right).
$$

粗网格由每 $M_s$ 个细网格合并得到。粗变量演化为

$$
\dot{\hat u}_m
=
\frac{1}{\Delta\hat x}
\left[
(\hat F_m+G_m)-(\hat F_{m+1}+G_{m+1})
\right],
$$

其中粗通量只依赖粗变量：

$$
\hat F_m=F_{\mathrm{LLF}}(\hat u_{m-1},\hat u_m),
$$

子网格通量为闭包目标：

$$
G_m=F_{M_sm}-\hat F_m.
$$

这里 $G_m$ 是细网格界面通量与粗网格通量的差。物理上，它主要起反扩散修正作用，用来抵消粗网格离散带来的过度数值扩散。

### 9. 数值参数与结果要点

论文实验使用空间区间 $S=[-25,25]$，细网格数

$$
M_f=1920,
$$

每 $M_s=20$ 个细网格合并为一个粗网格，因此

$$
M=M_c=96.
$$

每个粗状态包含 $2M=192$ 个值，即 $h$ 和 $q$ 各 96 个。训练初值族为

$$
h_0(x)
=
1+0.3(1-\delta/2)
\sin\left(
\frac{2\pi}{L_S}3.5(1-\delta/2)x+\frac{\pi}{6}
\right),
$$

$$
v_0(x)
=
1+0.2(1-\delta)
\sin\left(
\frac{2\pi}{L_S}3(1-\delta)x
\right),
$$

$$
q_0=h_0v_0,
\qquad
\delta\in[0,1].
$$

训练轨线取

$$
\delta\in\{0,0.5,1\},
$$

测试轨线取未见过的

$$
\delta\in\{0.25,0.75\}.
$$

训练中每条轨线最终保留 163 个粗采样点；使用 $Q=64$ 个延迟后，每条轨线得到 100 个 delay-embedded 样本，总计

$$
N=300,
\qquad
NM=28800.
$$

谱空间取

$$
L=6144.
$$

Bayes 修正的局部 stencil 取

$$
J=5.
$$

在线预测 120 个粗时间步，Bayes conditioning 每 10 步执行一次（附录伪代码是每步 conditioning，实验为每 10 步）。$G_m=F_{M_s m}-\hat F_m$ 作为反扩散子网格通量，依赖 coarse cell interface 附近的 fine cells。结果显示：QMCl 能捕捉主要行波结构、波前交互和 $h,q$ 的主要幅值；相比真值仍更扩散，尤其在子网格通量尖峰处不够锐利；但明显优于直接把 $G_m=0$ 的纯粗网格模拟。需要说明：论文主要以 heatmap/profile 做定性比较，未给出与经典 ML 参数化 baseline 的 L2/RMSE 量化误差表。

### 10. 算法流程

离线阶段：

1. 从细网格真值模拟生成训练轨线，粗粒化得到 resolved samples $\{\hat u_n\}$。
2. 用细网格界面通量和粗网格通量计算子网格通量样本 $\{G_n\}$，即训练标签。
3. 用 resolved samples 构造 delay embedding $W_Q$。
4. 构造高斯核矩阵 $K_N$，并做 bistochastic normalization。
5. 求 $K_N$ 的前 $L$ 个特征函数，形成基矩阵 $\Phi\in\mathbb R^{NM\times L}$。
6. 为降低成本，对 $NM\times NM$ 核矩阵使用 partial Cholesky 低秩近似。
7. 构造投影后的 transfer operator $P_N^L$。
8. 由通量样本构造两个量子可观测量矩阵 $A_0,A_1$，分别预测 $h$ 与 $q$ 的子网格通量。
9. 为每个粗网格点 $x_m$ 初始化一个密度算子向量 $\rho_m$。
10. 校准 conditioning kernel 的带宽 $\epsilon'$，并使用 variable bandwidth 增强稳定性。

在线阶段：

1. 输入初始粗状态 $\tilde u_0$。
2. 用非信息化初态初始化所有 $\rho_m$（单位函数方向上的投影）。
3. 先用初始 $\tilde u$ 做 Bayes conditioning，再计算每个网格点的闭包通量；循环中先更新 resolved state，再 transfer，再 conditioning，再计算更新后的通量（对应附录顺序）。
4. 计算每个网格点的闭包通量：

$$
\tilde f_j(x_m)=\rho_m^\top A_j\rho_m.
$$

5. 将 $\tilde f_j$ 代入粗网格有限体积方程推进 $\tilde u_n\to\tilde u_{n+1}$。
6. 用 transfer operator 推进密度态：

$$
\rho_m\leftarrow
\frac{P_N^L\rho_m}{\|P_N^L\rho_m\|_2}.
$$

7. 每隔若干步重新做 Bayes conditioning；论文实验中是每 10 步一次。
8. 重复直到预测结束。

### 11. 与本库其他方向的关联

与 Schrödingerization / 量子 PDE 模拟的关系：Schrödingerization 通常把非幺正 PDE 或线性系统嵌入 Schrödinger 型幺正演化，以便量子算法处理；本文则把经典非线性 PDE 的闭包问题嵌入量子测量和密度算子框架。前者偏“量子算法求解 PDE”，后者偏“量子力学算子语言组织统计闭包”。共同点是都通过扩大 Hilbert 空间来获得更好的结构保持性。

与 Koopman 方法的关系：本文是 Koopman-von Neumann / transfer-operator 思路在闭包中的应用。延迟嵌入核特征函数、迁移算子 $P_N^L$、不变测度采样都与 Koopman 谱方法一致；不同点是本文不直接学习有限维 Koopman 线性模型来预测状态，而是学习密度算子与量子可观测量，用期望值输出闭包通量。

与 SINDy 的关系：SINDy 通常在候选函数库中稀疏识别显式方程，例如

$$
\dot x=\Theta(x)\xi.
$$

若用于闭包，SINDy 会倾向学习显式的 $G(\hat u)$ 或 $G(\hat u,\partial_x\hat u,\dots)$。本文不追求稀疏显式公式，而是用训练数据、核相似度和密度算子进行非参数统计估计。因此 QMCl 更像“带物理结构的非参数闭包”，可解释性不如 SINDy 公式直接，但能容纳多值性、不确定性和局部统计记忆。

与 PINN / physics-informed ML 的关系：PINN 把 PDE 残差、边界条件、守恒律等写进神经网络损失；本文没有训练神经网络，也没有通过残差优化求解 PDE。它保持粗网格有限体积求解器，只替换子网格通量 $G_m$ 的估计方式。与 PINN 相比，QMCl 的物理结构主要体现在守恒型粗网格方程、保正算子离散、迁移算子演化和对称性不变核基上，而不是损失函数约束。与姊妹论文相比：QMCl 不是神经算子（GKN 学 PDE solution operator 与离散化不变性），也不是 Hamiltonian/Lie-Poisson 神经网络（LPNets 保持几何结构），而是非神经的 density-operator/statistical closure，结构保持来自保正算子、transfer operator 与 symmetry-invariant kernel basis。
## Review Questions

1. 在实现 QMCl 时，如何把每个 coarse cell 的 $\rho_m\in\mathbb R^L$、$A_j$、$P_N^L$ 与 $e_m$ 组织成可扩展的批处理矩阵计算，同时保证归一化、保正性，并控制 $NM=28800, L=6144$ 下的在线 conditioning 成本？
2. 在粗网格有限体积 SWE 中，$G_m=F_{M_s m}-\hat F_m$ 作为反扩散子网格通量会如何影响 CFL、守恒性和稳定性；当 QMCl 预测的 flux peaks 被抹平时，应设计哪些诊断来区分闭包误差与数值扩散？
3. 对具有平移对称性的 PDE，delay kernel 的 symmetry factorization 如何减少训练数据扩增需求；若扩展到二维、多物理场或 AMR 网格，需要怎样修改 stencil、measure 和 kernel normalization？
