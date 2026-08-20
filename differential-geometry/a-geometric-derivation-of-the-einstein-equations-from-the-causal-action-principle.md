# 从因果作用原理几何推导爱因斯坦方程

# A Geometric Derivation of the Einstein Equations from the Causal Action Principle

**作者：** Felix Finster, Christoph Krpoun
**期刊：** arXiv:2607.13871, 2026（预印本）
**arXiv：** [https://arxiv.org/abs/2607.13871](https://arxiv.org/abs/2607.13871)
**阅读状态：** 🔬 精读（Doctor 指定）
**流程状态：** ①元数据 ✓ | ②初稿 ✓ | ③评估 ✓(精读) | ④补充 ✓ | ⑤索引 ✓ | ⑥review ✓ | ⑦提交 ✓

---

## 摘要

### 中文翻译
分析因果费米子系统的因果作用原理：设极小化测度的支撑为光滑流形 M̃。引入 osculating vacua（密切真空）概念，证明 Lagrangian 在 M̃ 上诱导出 Lorentz 度量；因果作用的 Euler-Lagrange 方程蕴含 Ricci 张量必须满足广义相对论的爱因斯坦方程，其中能量-动量张量以正则化长度的幂级数给出。引力耦合常数等于正则化长度的平方。方法提供系统推导爱因斯坦方程修正项的程序。论文含因果变分原理与因果作用原理的自足导引；连接、Riemann 度量、曲率等几何结构在一般维数 M̃ 的因果变分原理框架下引入与分析；Lorentz 设定仅适用于四维时空的因果费米子系统。

### 原文
> The causal action principle for causal fermion systems is analyzed for a minimizing measure whose support is assumed to have the structure of a smooth manifold M̃. The concept of osculating vacua is introduced. It is shown that the Lagrangian induces on M̃ a Lorentzian metric. Moreover, the Euler-Lagrange equations of the causal action imply that the Ricci tensor must satisfy the Einstein equations of general relativity for an energy momentum tensor given in terms of a power expansion in the regularization length. The gravitational coupling constant is found to be the square of the regularization length.

---

## 文章总结

### 1. 解决什么问题？
如何从因果作用原理（量子物理底层的变分原理）推导出宏观爱因斯坦方程？

### 2. 用了什么方法论？
因果变分原理一般框架：极小测度支撑为光滑流形 M̃；osculating vacua（密切真空）概念给出局部真空结构；Lagrangian 诱导 Lorentz 度量；Euler-Lagrange 方程在正则化长度幂级数展开下化为 Einstein 方程，引力常数 = 正则化长度²。

### 3. 主要结论是什么？
因果作用原理在流形支撑假设下几何地导出 Einstein 方程：引力耦合常数被确定为正则化长度的平方，并提供系统性推导广义相对论修正项（如高阶曲率项）的程序。

---

## 价值评估

Doctor 指定精读（跳过 Codex 价值评估）。

## 公式与代码梳理

**1. 因果变分原理的一般形式**

设 $\mathcal F$ 是光滑流形，Lagrangian 为非负光滑函数

$$
\mathcal L\in C^\infty(\mathcal F\times \mathcal F,\mathbb R_0^+),
$$

满足对称性与对角正性：

$$
\mathcal L(x,y)=\mathcal L(y,x),\qquad \mathcal L(x,x)>0.
$$

因果变分原理以正 Borel 测度 $\rho$ 为变量，最小化作用量

$$
\mathcal S(\rho)=\int_{\mathcal F}d\rho(x)\int_{\mathcal F}d\rho(y)\,\mathcal L(x,y),
$$

并保持总体积约束。时空不是预设流形，而是极小化测度的支撑：

$$
M:=\operatorname{supp}\rho.
$$

极小化测度满足 Euler-Lagrange 方程。定义

$$
\ell(x)=\int_{\mathcal F}\mathcal L(x,y)\,d\rho(y)-s,
$$

其中 $s>0$ 是体积约束的 Lagrange 乘子，则

$$
\ell|_M\equiv \inf_{\mathcal F}\ell=0.
$$

本文额外假设 Lagrangian 是短程的：存在正则化长度 $\delta$，使得

$$
d(x,y)>\delta\quad\Longrightarrow\quad \mathcal L(x,y)=0.
$$

因此所有局部几何量都可按 $\delta$ 做幂级数展开。物理上 $\delta$ 对应 Planck 尺度，最终引力耦合常数由 $\delta^2$ 给出。

**2. 因果作用原理与因果费米子系统**

因果费米子系统由三元组

$$
(\mathcal H,\mathcal F,\rho)
$$

给出，其中 $\mathcal H$ 是可分复 Hilbert 空间，$\mathcal F$ 是 $\mathcal H$ 上有限秩对称算子的集合，并且每个算子最多有 $n$ 个正特征值和 $n$ 个负特征值。

对 $x,y\in\mathcal F$，令 $\lambda_1^{xy},\dots,\lambda_{2n}^{xy}$ 为 $xy$ 的非平凡特征值（不足补零）。$\kappa$-Lagrangian 为

$$
\mathcal L(x,y)
=
\frac{1}{4n}\sum_{i,j=1}^{2n}
\left(|\lambda_i^{xy}|-|\lambda_j^{xy}|\right)^2
+
\kappa\left(\sum_{j=1}^{2n}|\lambda_j^{xy}|\right)^2.
$$

对应因果作用为

$$
\mathcal S(\rho)=\iint_{\mathcal F\times\mathcal F}\mathcal L(x,y)\,d\rho(x)d\rho(y).
$$

约束包括

$$
\rho(\mathcal F)=1,\qquad \int_{\mathcal F}\operatorname{tr}(x)\,d\rho(x)=1.
$$

在有限维、固定迹、满秩等正则条件下，因果作用原理可化入一般因果变分原理；区别在于 CFS 的 $\mathcal F$ 有算子谱结构，因而能进一步给出 Lorentz 度量，而一般 CVP 只能自然得到 Riemannian 版本。

**3. Osculating vacua：用局部真空替代切空间**

论文引入两个测度：真空 $\rho$ 与相互作用时空 $\tilde\rho$，

$$
M=\operatorname{supp}\rho,\qquad \tilde M=\operatorname{supp}\tilde\rho.
$$

真空 $M$ 被视为向量空间，并假设 Lagrangian 在 $M$ 上平移不变：

$$
\mathcal L(x,y)=\mathcal L[y-x],\qquad \mathcal L[\xi]=\mathcal L[-\xi].
$$

对每个 $p\in\tilde M$，选择 Lagrangian 的对称变换 $\Phi_p$，把真空搬到 $p$ 附近：

$$
\rho_p=(\Phi_p)_*\rho,\qquad M_p=\operatorname{supp}\rho_p.
$$

$M_p$ 称为 $p$ 处的 osculating vacuum（密切真空）。它的作用类似微分几何中的切空间，但更强：它不仅近似几何，还试图通过对称变换“吸收”物质场扰动。

选择基 $e_i$ 后，密切真空由局部变分问题确定：

$$
S_p(\Phi_p)=\sum_{i=1}^k D^2\tilde\ell|_p\big(e_i(p),e_i(p)\big).
$$

若 $S_p=0$，称为 optimal osculation，此时有

$$
D^2\tilde\ell|_{M_p}(p)=0.
$$

若进一步满足

$$
T_p\tilde M=T_{0_p}M_p,
$$

则 $M_p$ 与 $\tilde M$ 在 $p$ 处一阶相切。全文主推导主要在这个 optimal osculation 假设下进行；非最优情形会引入扭率，作为高阶修正处理。

**4. Lagrangian 诱导图、连接与 Riemannian 度量**

在 $p$ 处定义 L-induced chart：

$$
\varphi_p(\tilde x)=\frac{1}{s}\int_{M_p}\mathcal L(\tilde x,y)\,y\,d\rho_p(y).
$$

optimal osculation 给出标准化性质：

$$
\varphi_p(p)=0_p,\qquad D\varphi_p|_p=\operatorname{id}_{M_p}.
$$

因此 $\varphi_p$ 可作为 $\tilde M$ 上以 $p$ 为中心的局部坐标。由这些坐标定义 L-induced connection：

$$
\nabla^L_v u|_p
=
v\big(u\varphi_p\big)|_{\tilde x=p}.
$$

在 L-induced chart 中，

$$
\nabla_i^L u^j=\partial_i u^j+\Gamma^j_{ik}u^k,
\qquad
\Gamma^j_{ik}(p)=
\left.
\frac{\partial^2\varphi_p^j(x)}{\partial x^i\partial x^k}
\right|_{x=p}.
$$

该连接在 optimal osculation 情形无扭率。Lagrangian 还在 $M_p^*$ 上诱导余度量：

$$
g_p^*(\alpha,\beta)
=
\frac{1}{\delta^2}\frac{1}{s}
\int_{M_p}\mathcal L(p,y)\,\alpha(y)\beta(y)\,d\rho_p(y),
$$

再由逆矩阵得到 $M_p\simeq T_p\tilde M$ 上的 Riemannian 度量 $g_p$。因子 $1/\delta^2$ 保证 $\delta\to0$ 时度量量级有限。

$\nabla^L$ 一般不是严格 metric connection，但满足

$$
\nabla^L g=O(\delta^2).
$$

令 $\nabla^g$ 为 $g$ 的 Levi-Civita 连接，定义 deviation tensor

$$
K^j_{ik}=(\Gamma^g)^j_{ik}-\Gamma^j_{ik},
$$

则

$$
K^j_{ik}=O(\delta^2).
$$

因此 $\nabla^L$ 与 $\nabla^g$ 的差异被归入能量-动量张量，而不是主几何项。

**5. 从 EL 方程到 Einstein 方程的推导链**

L-induced connection 的曲率为

$$
R^k{}_{ijl}
=
\partial_i\Gamma^k_{jl}-\partial_j\Gamma^k_{il}
+\Gamma^k_{ia}\Gamma^a_{jl}
-\Gamma^k_{ja}\Gamma^a_{il}.
$$

在以 $q$ 为中心的 L-induced chart 中，$\Gamma(q)=0$，L-connection 的 Ricci 张量可写成（注意：这是 $\nabla^L$ 导出的 Ricci，一般并不对称；与后文 Levi-Civita 意义下的 $R^g$、$R^\eta$ 不同）

$$
R_{il}(q)
=
\left.
\left(\bar\partial_i\partial_k\partial_l\varphi_p^k
-
\bar\partial_k\partial_i\partial_l\varphi_p^k
\right)
\right|_{x=p=q},
$$

其中 $\bar\partial_i=\partial_{x^i}+\partial_{p^i}$。

关键技巧是引入 alignment vector field：

$$
A_p^k(x)
=
\frac{1}{s}
\int_M
\mathcal L(F(x),F_p(y))\,(y-x)^k\,f_p\,d\rho(y).
$$

利用 EL 方程与 osculation 方程，可在曲率公式中把 $\varphi_p$ 替换为 $A_p$：

$$
R^k{}_{ijl}(q)
=
\left.
(\bar\partial_i\partial_j\partial_l-\bar\partial_j\partial_i\partial_l)
A_p^k(x)
\right|_{x=p=q}.
$$

因为 $A_p$ 含有差向量 $\xi=y-x$，对其散度展开会天然产生 $\delta$ 的幂。EL 方程消掉零阶和一阶贡献，Ricci 张量只剩从 $r=2$ 开始的项：

$$
T_{jk}=O(\delta^2).
$$

这就是“弱引力”的来源：Einstein 张量不是任意阶，而是被短程 Lagrangian 与 EL 方程强迫为正则化长度平方阶。

Riemannian 版本定理为

$$
R^g_{il}-\frac12 R^g g_{il}=T_{il},
$$

其中

$$
T_{il}-\frac{1}{k-2}Tg_{il}
=
-\nabla_i^gK^a{}_{al}
+\nabla_a^gK^a{}_{il}
-K^b{}_{ia}K^a{}_{bl}
+K^b{}_{ba}K^a{}_{il}
+\text{alignment divergence expansion}.
$$

后面的 alignment divergence expansion 由两类项组成：$x$-散度展开与 $p$-散度展开，均从 $r=2$ 起：

$$
\sum_{r=2}^{\infty}
\frac{(-1)^r}{r!}
\partial_{p^i}\partial_{x^l}
\frac{1}{s}\int_M
\left(\xi^k\partial_{x^k}\right)^r
f(x)\mathcal L(F(x),F_p(y))f_p\,d\rho(y),
$$

以及

$$
\sum_{r=2}^{\infty}
\frac{1}{r!}
\frac{1}{s}\int_M
\left(\xi^k\partial_{p^k}\right)^r
\partial_{1,il}\mathcal L(F(x),F_p(y))f_p\,d\rho(y).
$$

因此 $T_{il}$ 不是外加的物质张量，而是从 causal action 的 EL 方程、测度权函数 $f$、osculation 偏差和短程 Lagrangian 展开中读出的有效张量，并自动满足

$$
T_{il}=T_{li},\qquad \nabla_i^gT^{il}=0.
$$

**6. Lorentz 度量与引力耦合常数**

Lorentz 结构需要 CFS 的额外数据。四维正则化 Dirac sea 真空中存在 time direction functional：

$$
\mathcal C(x,y)
=
i\,\operatorname{tr}\left(yx\,\pi_y\pi_x-xy\,\pi_x\pi_y\right),
$$

其中 $\pi_x:\mathcal H\to x(\mathcal H)$ 是到 spin space 的正交投影。由此定义 regularizing vector field：

$$
u(p)=\frac{1}{s}\int_{M_p}
\mathcal L(p,y)\mathcal C(p,y)y\,d\rho_p(y).
$$

在 L-induced chart 的局部坐标展开中，与 alignment field $A_p^k$ 一致地采用 $1/s$ 归一化写法（见原文 Definition 6.2 及后续局部表达），即

$$
u^k(p)=\frac{1}{s}\int_M \mathcal L(F(p),F_p(y))\,\mathcal C(F(p),F_p(y))\,(y-p)^k f_p\,d\rho(y).
$$

它几乎平行：

$$
\nabla^L u=O(\delta^2).
$$

归一化

$$
\hat u=\frac{u}{\sqrt{g(u,u)}},\qquad \omega(v)=g(\hat u,v),
$$

Lorentz flip metric 定义为

$$
\eta=4\,\omega\otimes\omega-g.
$$

系数 $4$ 由正则化 Dirac sea 真空的光锥匹配确定：若 Lagrangian 主支撑在 Minkowski 光锥上，则 $\eta$ 的因果锥与 CFS 因果结构一致当且仅当 flip 参数 $\tau=4$。

Lorentz 版本 Einstein 方程为

$$
R^\eta_{il}-\frac12 R^\eta\eta_{il}=T^\eta_{il},
$$

其中 $T^\eta$ 等于 Riemannian $T$ 加上从 $\nabla^\eta-\nabla^g$ 来的修正。若

$$
\nabla_i^\eta v^k-\nabla_i^g v^k=C^k{}_{ij}v^j,
$$

则 Ricci 差为

$$
\operatorname{Ric}^\eta_{il}-\operatorname{Ric}^g_{il}
=
\nabla_k^g C^k{}_{li}
-
C^k{}_{lj}C^j{}_{ki}.
$$

⚠️ 符号注记：原文（Theorem 6.8 附近）先给出 Riemann 曲率差

$$
R(\eta)^k{}_{ijl}-R(g)^k{}_{ijl}
=
\nabla^g_j C^k{}_{li}-\nabla^g_l C^k{}_{ji}
+C^k{}_{jm}C^m{}_{li}-C^k{}_{lm}C^m{}_{ji},
$$

经收缩后进入 Einstein 方程右端的附加项为

$$
+\nabla^g_a C^a{}_{li}-C^a{}_{lj}C^j{}_{ai},
$$

这里省略了收缩过程中的交叉项（含 $C^a{}_{lj}C^j{}_{ai}$ 的非对称贡献），只保留对 $T^\eta$ 有效的对称部分。

由于 $\hat u$ 几乎平行，这些 Lorentz 修正同样是 $O(\delta^2)$，可归入能量-动量张量。于是引力耦合常数的尺度为

$$
G_{\mathrm{eff}}\sim \delta^2.
$$

更准确地说，论文的结论不是从实验输入 $G$，而是从 EL 方程推出 Einstein 张量的右端自然带有 $\delta^2$ 小因子；因此正则化长度平方扮演 gravitational coupling constant。

**7. 修正项的系统推导程序**

本文给出的“代码化”推导流程可以概括为：

```text
输入：Lagrangian L、真空测度 rho、相互作用测度 rho_tilde、正则化长度 delta

1. 求极小化测度支撑：
   M = supp rho,  M_tilde = supp rho_tilde

2. 对每个 p in M_tilde 构造 osculating vacuum：
   rho_p = (Phi_p)_* rho
   M_p = supp rho_p

3. 用局部变分最小化 S_p(Phi_p)，检查 optimal osculation：
   D^2 ell_tilde|_{M_p}(p) = 0
   T_p M_tilde = T_{0_p} M_p

4. 构造 L-induced chart：
   phi_p(x) = (1/s) int_{M_p} L(x,y)y d rho_p(y)

5. 从 phi_p 计算连接：
   Gamma^j_{ik} = partial_i partial_k phi_p^j

6. 从 L 计算余度量并取逆：
   g_p^*(alpha,beta) = delta^{-2}(1/s) int L(p,y) alpha(y) beta(y) d rho_p(y)

7. 计算 L-curvature 与 Ricci：
   R^k_{ijl}, R_{il}

8. 引入 alignment A_p，把 Ricci 改写为 divergence form

9. 用 EL 方程消去低阶项，对 divergence 做 delta 幂级数展开

10. 把 K = Gamma^g - Gamma^L、alignment 展开、Lorentz flip 修正统一收进 T_{ij}

输出：
   R^g_{ij} - 1/2 R^g g_{ij} = T_{ij}
   或四维 CFS 中
   R^eta_{ij} - 1/2 R^eta eta_{ij} = T^eta_{ij}
```

修正项主要有四类：

- Planck 尺度高阶项：alignment 展开中 $r\ge3$ 的 $\delta$ 高阶贡献。
- osculation 修正：若 $T_p\tilde M$ 与 $M_p$ 不完全相切，映射 $D\varphi_p$ 不再是恒等，且 $0_p\ne p$。
- 扭率修正：非最优 osculation 下 $\nabla^L$ 可有 torsion，
  $$
  T^L(u,v)=\nabla_u^Lv-\nabla_v^Lu-[u,v].
  $$
  可用 contorsion tensor 构造无扭连接，并把差异归入有效 $T_{ij}$。
- modified measure 修正：CFS 的时空测度 $d\rho$ 不必等于 Lorentz 体积测度
  $$
  \sqrt{|\det\eta|}\,d^4x,
  $$
  权函数 $f$ 的展开可能带来类似 modified measure theory 的有效项。

**8. 与本库其他论文的关联**

与 Geometric Deep Learning 的关联在于“几何不是背景，而是由结构诱导”。GDL 通过群作用、等变性、规范选择把网络架构限制在尊重对称性的函数类中；本文则通过 Lagrangian 的对称群与 osculating vacua 选择局部 chart、连接和度量。两者都把“规范/坐标选择”视为中间表示，真正重要的是由对称性控制的不变量或协变量。

与 Force-Free Fields are Conformally Geodesic 的关联在于“物理方程可重写为几何轨道条件”。Force-free 磁场把 MHD 平衡写成共形测地叶状结构；本文把因果作用的 EL 方程写成 Ricci/Einstein 几何方程。二者都不是在既定几何上求解场，而是把场方程改写为几何结构的兼容条件。

与 Hamilton 原理/离散变分积分器相关论文的关联在于“变分原理决定结构保持”。Hamilton 流体和 double-bracket 离散变分强调由作用量和约束推出 Euler-Lagrange 方程，并保持伴随轨道、Casimir 或涡量结构；本文同样从作用量极小化出发，但变量不是轨迹或场，而是测度 $\rho$。它的守恒律来自 EL 方程与 Bianchi identities，而不是外加能量-动量守恒假设。

整体上，这篇论文可放在本库“几何/变分/物理结构保持”主线中：  
从 **对称性 → 局部规范/密切模型 → 连接与曲率 → EL 方程 → 守恒律/Einstein 方程**，形成一条由底层变分原理生成宏观几何的路线。
## 研究者复核：逻辑地位、边界项与有效应力

The displayed Einstein equation is an effective result conditional on the paper's regularity, short-range expansion, and (for the Lorentzian part) causal-fermion-system vacuum hypotheses; it is not a derivation of classical GR from the bare action without additional input. The EL relation \(\ell|_M=0\) only permits the integrations by parts used in the alignment expansion when the variations are compactly supported or the relevant nonlocal boundary terms vanish. Since the effective tensor includes \(K\), alignment, and measure corrections, its conservation is tied to the Bianchi identity and the approximation order, rather than an independently postulated standard matter stress tensor.

For comparison with the conventional normalization one would write \(G_{ij}+\Lambda g_{ij}=8\pi G_{\!N}T^{\rm matter}_{ij}\). Here the note's \(T_{ij}\) absorbs normalization and geometric correction terms, so \(G_{\rm eff}\sim\delta^2\) is a scaling statement, not an equality that fixes Newton's constant. The Lorentz flip \(\eta=4\omega\otimes\omega-g\) has signature \((+---)\) when \(g\) is positive definite and \(\omega\) is unit; swapping signature conventions reverses which direction is called timelike.

## Review Questions

1. 如果把这里的 alignment vector field 与 x/p-divergence 展开落到实际数值框架里，哪些离散可观测量最适合作为 $O(\delta^2)$ 有效应力项的诊断量，以区分“真实几何响应”和“核截断/网格误差”？
2. 若在有限元、有限体积或粒子法里实现 osculating vacua 与 L-induced chart，你会如何组织局部坐标、短程核支撑 $d(x,y)>\delta \Rightarrow \mathcal L(x,y)=0$、以及各阶导数近似，才能既保留几何结构又控制计算复杂度？
3. Lorentzian 部分把 $\eta=\tau\,\omega\otimes\omega-g$（并在真空匹配下取 $\tau=4$）和 regularizing vector field 绑定在一起；在离散实现时，怎样验证由 $\hat u$ 引入的修正没有把 gauge choice、采样偏置或 regularization artifact 误识别成能量-动量张量 $T^\eta$？
