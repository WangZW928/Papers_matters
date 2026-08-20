# Discrete variational calculus for double-bracket dissipation（双括号耗散的离散变分计算）

**作者：** Anthony M. Bloch, Sebastián J. Ferraro, David Martín de Diego, Shreyas Bharadwaj
**期刊：** arXiv preprint (math.NA / math.DG), 2026-04-28
**arXiv：** [https://arxiv.org/abs/2604.26049](https://arxiv.org/abs/2604.26049)
**DOI：** [https://doi.org/10.48550/arXiv.2604.26049](https://doi.org/10.48550/arXiv.2604.26049)
**阅读状态：** 🔬 精读
**流程状态：** ①元数据 ✓ | ②初稿 ✓ | ③评估 ✓(Doctor指定精读) | ④补充 ✓ | ⑤索引 ✓ | ⑥review ✓ | ⑦提交 ✓

---

## 摘要

### 中文翻译
离散变分方法在力学系统的数值模拟中表现出色。本文将离散变分积分器适配到具有双括号耗散的力学系统中。具体而言，我们处理受迫 Euler-Poincaré 系统和受迫 Lie-Poisson 系统，我们感兴趣的情形是：伴随轨道保持不变，但能量沿轨道递减。这类特殊的耗散系统出现在多种物理系统中，例如带阻尼器的卫星、地球物理流体、等离子体物理和恒星动力学。我们提出的几何积分器精确保持伴随轨道。通过与多种通用方法（包括高阶方法）在不同数值模拟中的对比，我们展示了这一特性的优势。

### 原文
> Discrete variational methods show excellent performance in numerical simulations of mechanical systems. In this paper, we adapt discrete variational integrators for the case of mechanical systems with double-bracket dissipation. In particular, we will work with forced Euler-Poincaré and forced Lie-Poisson systems, and the case of interest for us will be when the coadjoint orbits remain invariant, but the energy is decreasing along the orbit. This particular kind of dissipative system appears in various physical systems such as satellites with dampers, geophysical fluids, plasma physics and stellar dynamics. The proposed geometric integrator preserves the coadjoint orbits exactly. We highlight the advantages of this feature by comparing it with other general-purpose methods (including higher-order ones) across different numerical simulations.

---

## 文章总结

### 1. 解决什么问题？
如何为具有双括号耗散（double-bracket dissipation）的力学系统构造保结构（structure-preserving）的离散变分积分器，使得数值解精确保持在伴随轨道（coadjoint orbit）上，同时能量递减。

### 2. 用了什么方法论？
- 将连续的双括号耗散系统（forced Euler-Poincaré / Lie-Poisson）通过离散变分原理（discrete variational principle）离散化
- 构造保持伴随轨道不变性的几何积分器（geometric integrator）
- 核心数学框架：Lie 群/代数上的变分原理、伴随轨道、双括号结构

### 3. 主要结论是什么？
提出的几何积分器能够**精确保持伴随轨道**，而通用方法（包括高阶 Runge-Kutta）存在轨道漂移。在卫星阻尼器、地球物理流体、等离子体等典型耗散系统中展示了数值优势。

---

## 价值评估
Doctor 指定精读

## 公式与代码梳理

本文研究的核心问题是：如何为具有双括号耗散的 Lie-Poisson / Euler-Poincaré 系统构造离散变分积分器，使数值解在耗散能量的同时，精确保持伴随轨道。论文的关键贡献不是单纯加入阻尼项，而是把阻尼项设计成仍然切于伴随轨道的余伴随向量场，并在离散层面把一步更新写成精确的 \(Ad^*\) 作用。

### 1. 连续数学框架

设 \(G\) 为 Lie 群，\(\mathfrak g=T_eG\)，\(\mathfrak g^*\) 为其对偶。使用左平凡化：

\[TG\to G\times \mathfrak g,\qquad (g,\dot g)\mapsto (g,g^{-1}\dot g)=(g,\xi).\]

若 \(L:TG\to \mathbb R\) 左不变，则可约化为

\[l:\mathfrak g\to \mathbb R,\qquad l(\xi)=L(g,g\xi).\]

**无外力时的 Euler-Poincaré 方程：**

\[\frac{d}{dt}\frac{\delta l}{\delta \xi}=ad_\xi^*\frac{\delta l}{\delta \xi}.\]

**加入外力后的 forced Euler-Poincaré 方程：**

\[\frac{d}{dt}\frac{\delta l}{\delta \xi}=ad_\xi^*\frac{\delta l}{\delta \xi}+f(\xi).\]

**Lie-Poisson 方程**（Legendre 变换 \(\mu = \delta l/\delta \xi\) 后）：

\[\dot \mu = ad^*_{\delta H/\delta \mu}\mu.\]

Lie-Poisson 括号：

\[\{f,g\}(\mu) = -\left\langle \mu, \left[\frac{\delta f}{\delta \mu}, \frac{\delta g}{\delta \mu}\right]\right\rangle.\]

**伴随轨道：**

\[\mathcal O_{\mu_0} = \left\{Ad^*_{g^{-1}}\mu_0\mid g\in G\right\}.\]

无外力时，解满足 \(\mu(t)\in \mathcal O_{\mu(0)}\)。其数学来源是 Lie-Poisson 向量场具有形式 \(\dot \mu=ad^*_{\chi(\mu)}\mu\)，速度向量永远属于伴随轨道的切空间。

#### 双括号耗散的引入

一般外力会破坏能量、Poisson 结构和伴随轨道。但本文考虑特殊外力：

\[f(\xi) = ad^*_{\phi(\xi)} \frac{\delta l}{\delta \xi},\quad \phi:\mathfrak g\to \mathfrak g.\]

于是 forced Euler-Poincaré 方程变成：

\[\frac{d}{dt}\frac{\delta l}{\delta \xi} = ad^*_{\xi+\phi(\xi)} \frac{\delta l}{\delta \xi}.\]

这仍然是余伴随形式，因此仍切于伴随轨道。

**Hamiltonian 版本：**

\[\dot \mu = ad^*_{\frac{\delta H}{\delta \mu}+\phi\left(\frac{\delta H}{\delta \mu}\right)}\mu.\]

物理意义：耗散项不施加"外部净力矩"式的轨道漂移，而是在固定 Casimir/固定伴随轨道内部重新分配状态，使能量沿轨道下降。

**关键性质：**
- 对任意 Casimir：\(dC/dt = 0\)
- 对 Hamiltonian：\(dH/dt = \langle \mu, [\phi(\delta H/\delta \mu), \delta H/\delta \mu]\rangle\)

**构造耗散映射：** 取半正定内积 \(k:\mathfrak g^*\times \mathfrak g^*\to \mathbb R\)，令

\[\phi(\xi) = k^\sharp(ad^*_\xi\, \delta l/\delta \xi).\]

则能量耗散满足：

\[dE_l/dt = -k(ad^*_\xi\, \delta l/\delta \xi,\, ad^*_\xi\, \delta l/\delta \xi) \le 0.\]

**双括号形式：**

\[\{\{f,g\}\}(\mu) = -\langle \mu, [k^\sharp(ad^*_{\delta f/\delta \mu}\mu), \delta g/\delta \mu]\rangle.\]

动力学：\(\dot f = \{f,H\} - \{\{f,H\}\}\)。

矩阵形式：\(\dot z = \Pi(z)\nabla H(z) - S(z)\nabla H(z)\)，其中 \(S = \Pi^T K \Pi\)。由于 \(S\nabla C = 0\)，Casimir 不被耗散项改变。

### 2. 离散变分结构与关键推导

**无外力离散 Euler-Poincaré：**

离散曲线取 Lie 群元素序列 \(\{w_k\}\subset G\)，离散 Lagrangian \(l_d:G\to \mathbb R\)，离散作用量 \(S_d = \sum l_d(w_k)\)。

对固定乘积 \(w_1w_2=w_f\)，取变分曲线 \(c(t)=(w_1\gamma(t), \gamma(t)^{-1}w_2)\)，得：

\[0 = \overleftarrow{\xi}(w_1)(l_d) - \overrightarrow{\xi}(w_2)(l_d),\quad \forall \xi\in \mathfrak g.\]

这就是**离散 Euler-Poincaré 方程**。

定义离散 Legendre 变换 \(\mathbb F l_d^-(w) = L_w^* dl_d(w)\)，\(\mathbb F l_d^+(w) = R_w^* dl_d(w)\)，令 \(M_k = \mathbb F l_d^+(w_k) = R_{w_k}^* dl_d(w_k)\)，则无外力离散 Lie-Poisson 更新为：

\[M_{k+1} = Ad^*_{w_k} M_k.\]

**核心推广——引入耗散映射：**

引入离散耗散映射 \(\phi_d:G\to G\)，强迫离散变分为：

\[\delta w_k = -\eta_k w_k + w_k(Ad_{\phi_d(w_k)}\eta_{k+1}),\quad \eta_0=\eta_N=0.\]

对应连续变分 \(\delta \xi = \dot \eta + [\xi+\phi(\xi), \eta]\)。

代入离散作用量推导得 **forced discrete Euler-Poincaré 方程**：

\[R^*_{w_{k+1}} dl_d(w_{k+1}) = Ad^*_{\phi_d(w_k)} L^*_{w_k} dl_d(w_k).\]

利用 \(L^*_{w_k} dl_d(w_k) = Ad^*_{w_k} M_k\)，得 **forced discrete Lie-Poisson 方程**：

\[M_{k+1} = Ad^*_{w_k\phi_d(w_k)} M_k.\]

> **这是全文最重要的保结构机制：每一步更新都是 Lie 群元素对 \(M_k\) 的余伴随作用。无论步长多大，数值动量都严格满足 \(M_{k+1}\in \mathcal O_{M_k}\)，递推得 \(M_k\in \mathcal O_{M_0},\; \forall k\)。伴随轨道保持是代数精确性质，不是近似性质。**

### 3. 基于 retraction 的具体离散化

引入 retraction \(\tau:\mathfrak g\to G\)（至少 \(\tau(0)=e\)、\(d\tau_0=\operatorname{id}\)；\(\tau(\xi)\tau(-\xi)=e\) 是指数/Cayley 等对称 retraction 的额外性质）：

\[w_k = \tau(h\xi_k),\quad \xi_k = \frac{1}{h}\tau^{-1}(w_k).\]

离散 Lagrangian：\(l_d(w_k) = h\,l(\xi_k).\)

耗散映射：\(\phi_d(w_k) = \tau(h\phi(\xi_k)).\)

定义右平凡化导数 \(d\tau_\xi\) 及其逆，记 \(p_k = \partial l/\partial \xi(\xi_k)\)，离散动量：

\[M_k = (d\tau^{-1}_{h\xi_k})^* p_k.\]

得到核心更新：

\[M_{k+1} = Ad^*_{\tau(h\xi_k)\tau(h\phi(\xi_k))} M_k.\]

**注意：** 真正精确保持伴随轨道的是 \(M_k\)，不是 \(p_k\)。

**常用 retraction：**

- **指数映射：** \(d\exp_x y = \sum_{j=0}^{\infty} \frac{1}{(j+1)!}ad_x^j y\)，\(d\exp_x^{-1}y = \sum_{j=0}^{\infty} \frac{B_j}{j!}ad_x^j y\)
- **Cayley 映射：** \(\text{cay}(\xi) = (I-\xi/2)^{-1}(I+\xi/2)\)
  - \(SO(3)\) 上：\(dcay_{\hat x}^{-1} = I - \hat x/2 + x\otimes x/4\)，对偶 \((dcay_{\hat x}^{-1})^* = I + \hat x/2 + x\otimes x/4\)

**二阶对称耗散：** \(\phi_d(w_k) = \tau(h\phi((\xi_k+\xi_{k+1})/2))\) 或 \(\phi_d(w_k) = \tau(h\phi(\xi_k)/2 + h\phi(\xi_{k+1})/2)\) 给出二阶对称方法。

### 4. 刚体例子与 DDB 算法

**刚体 Lagrangian：**\(l(\Omega) = \frac12 I\Omega\cdot \Omega\)，动量 \(M = I\Omega\)。

**双括号耗散刚体方程：** \(\dot M = M\times \Omega + \alpha M\times(M\times \Omega)\)，其中 \(\phi(\Omega) = \alpha I\Omega\times \Omega\)。

能量耗散：\(dE/dt = -\alpha \|M\times \Omega\|^2 \le 0\)，Casimir：\(C(M) = \|M\|^2\)。

**矩阵形式离散 Lagrangian：** \(l_d(w_k) = (\text{trace}(J) - \text{trace}(w_k J))/h\)，Moser-Veselov 离散动量：\(M_k = (w_k J - J w_k^T)/h\)。

**DDB 算法流程（伪代码）：**

```
M = M0
for k = 0,...,N-1:
    solve xi from M = (d tau^{-1}_{h xi})^* dl/dxi(xi)   # 隐式求解 ξ_k
    w = tau(h xi)                                         # 群增量
    q = tau(h phi(xi))                                    # 耗散群元
    M = Ad^*_{w q} M                                      # 更新（精确保轨道）
    store M
```

每一步都是 \(M_{k+1} = Ad^*_{g_k} M_k\)，\(g_k = w_k \phi_d(w_k) \in G\)，因此轨道保持为代数精确性质。

### 5. 数值实验结果

通过 3 个 Scenario（刚体，不同 \(I\) 和时间跨度）对比：

| 方法 | Casimir 保持 | 长时间优势 | 运行时间 (Scenario A, h=0.1) |
|------|-------------|-----------|----------------------------|
| DDB (cay) | ✓ 精确 | ✓ 接近极限点 | 0.108s |
| DDB (exp) | ✓ 精确 | ✓ 接近极限点 | 0.107s |
| RK4 | ✗ 漂移 | ✗ 系统偏差 | 0.162s |
| Lobatto IIIC | ✗ 漂移 | ✗ 系统偏差 | 1.616s |
| DOP853 (参考) | — | — | 0.207s |

**关键发现：**
1. DDB 精确保持 Casimir，RK4/Lobatto IIIC 出现漂移
2. 短时间：高阶通用方法有局部截断误差优势
3. **长时间：DDB 反超**——因为渐近行为发生在固定伴随轨道上，漂离 Casimir 球面的方法会产生系统偏差
4. Scenario C（大圆极限集）：DDB 因严格保持 \(\|M_k\| = \|M_0\|\) 而更准确地停留在正确几何约束上
5. DDB 不仅几何性质更好，计算代价也低于 RK4 和 DOP853

### 6. 与 Doctor 研究方向的关联

这篇论文在 **Lie 群/伴随轨道/动量映射**、**几何流体动力学** 和 **几何数值方法** 三个方向上都有直接价值：

- **微分几何：** 把"保持伴随轨道"从连续几何性质落实为离散代数构造 \(M_{k+1}=Ad^*_{g_k}M_k\)，展示了一类在辛叶内部耗散 Hamiltonian 的系统
- **流体力学：** 论文未来工作明确指向理想流体——用有限维 Lie 群逼近体积保持微分同胚群，构造保持 Casimir 的选择性衰减机制
- **几何数值方法：** 提供清晰范式：先找连续系统的几何变分结构 → 离散变分 → 用群作用保证不变量。适合长期模拟、耗散渐近行为、Casimir 约束敏感系统

**局限：** 数值实验集中在刚体，推广到流体需解决有限维近似、非交换群计算、隐式方程求解和高阶精度构造等问题。DDB 方法精确保持的是离散动量 \(M_k\) 的伴随轨道，不是所有自然变量都自动保持相同结构。

**核心启发：**
- 连续层面：耗散不必破坏几何约束；只要耗散项仍写成余伴随方向，轨道可保持而能量可下降
- 离散层面：要保持伴随轨道，就把每一步更新设计成精确的 \(Ad^*\) 作用

## 研究者复核：约定、耗散号与离散顺序

All coadjoint formulas in this note use the stated left-trivialization convention. With \(\langle ad^*_\xi\mu,\eta\rangle=\langle\mu,[\eta,\xi]\rangle\), changing the orbit parameterization from \(Ad^*_{g^{-1}}\mu_0\) to \(Ad^*_g\mu_0\) reverses the continuous sign; the bracket and equation must then change together. The discrete product order \(w_k\phi_d(w_k)\) must not be reversed.

If \(a=ad^*_\xi\mu\) and \(\phi(\xi)=k^\sharp a\), the sign check is
\[
\frac{dE_l}{dt}=\langle \xi,ad^*_{\phi(\xi)}\mu\rangle
=-\langle ad^*_\xi\mu,\phi(\xi)\rangle=-k(a,a)\leq0.
\]
This uses positive-semidefiniteness of \(k\). It proves continuous energy decrease, not unconditional stepwise decrease for every discrete \(\phi_d\); the exact discrete claim is orbit preservation of \(M_k\) when the implicit Legendre equation is solved accurately.

## Review Questions

### 公式推导检查
- 这份笔记的主线推导总体是通顺的，但 `ad^*` 与 `Ad^*` 的上下文必须区分：连续方程里的 `ad^*` 出现在 Euler-Poincaré / Lie-Poisson 形式；离散更新则使用 `Ad^*`。原文定理 4.3 的式 (4.7) 明确给出 $M_{k+1}=Ad^*_{w_k\varphi_d(w_k)}M_k$，其中离散耗散映射为 $\varphi_d(w_k)$，群乘法次序为 $w_k\varphi_d(w_k)$；这依赖该文采用的左/右平凡化约定，换约定时不能直接照搬。
- `\tau` 的 retraction 约定也建议再核对一次。笔记里写了 `\tau(0)=e` 和 `\tau(\xi)\tau(-\xi)=e`，这更像是对称 retraction 的附加性质，但不是所有 retraction 都满足；如果原文只使用一般 retraction，则这里应改成更弱的假设，避免把特殊假设误写成定义。相应地，`d\tau^{-1}` 的公式最好区分“右平凡化”还是“左平凡化”版本，否则 `M_k=(d\tau^{-1}_{h\xi_k})^*p_k` 这一句很容易在实现时被用错。
- 双括号耗散项的能量耗散符号也值得重新检查。笔记中写 `dE_l/dt=-k(ad^*_\xi\delta l/\delta\xi, ad^*_\xi\delta l/\delta\xi)\le 0`，这在选择半正定内积时是合理的，但前面把 `\phi(\xi)` 直接写成 `k^\sharp(ad^*_\xi\delta l/\delta\xi)` 时，需要确认论文里是否还有一个负号或投影算子；否则从连续耗散到离散耗散的符号链条可能前后不一致。
- `\dot\mu = ad^*_{\delta H/\delta\mu + \phi(\delta H/\delta\mu)}\mu` 这一条也建议和原文逐字核对。对于 forced Lie-Poisson / forced Euler-Poincaré 系统，常见写法会把外力写成 `ad^*` 形式的附加项，但是否能并入同一个 `ad^*` 里，要看作者对 `f(\xi)`、`\phi` 和 Legendre 变换的定义；目前笔记写法逻辑上可读，但不排除把两个不同层次的结构混写在一起。

### 算法流程与伪代码检查
- 伪代码整体流程是对的：先隐式解 `\xi_k`，再算群增量 `w_k`、耗散群元 `q_k`，最后用 `Ad^*` 更新动量。真正需要补的是“隐式方程的输入输出对象”。现在写成 `solve xi from M = (d tau^{-1}_{h xi})^* dl/dxi(xi)`，读者会不清楚求解变量是 `\xi_k` 还是 `w_k`，以及该方程是否还同时依赖 `M_k` 之外的已知量。更稳妥的写法应明确为“已知 `M_k`，求 `\xi_k` 使 `M_k=(d\tau^{-1}_{h\xi_k})^*\partial l/\partial\xi(\xi_k)`”。
- `q = tau(h phi(xi))` 这一步也建议核对。若论文中的耗散映射本身是通过 `\phi_d(w_k)` 定义，而不是直接由 `\phi(\xi_k)` 生成，那么这里应写成与论文一致的离散对象，避免把连续映射和离散映射混为一步。否则后面的 `Ad^*_{wq}` 可能掩盖了离散化误差来源。
- 算法流程里缺少停止条件、初值接口和每步后变量存储对象的说明。对数值算法笔记来说不致命，但如果将来要复现，建议明确“存储的是 `M_k`、`\xi_k` 还是 `w_k`”，以及 `store M` 是否意味着保存全轨迹还是仅保存当前值。

### Markdown 语法与格式检查
- 结构总体正确，标题层级清晰，数学公式也基本能正常渲染。$\varphi_d$、`\tau`、`Ad^*` 等符号均已置于合适的数学环境中，没有明显 Markdown 语法错误。
- 但文中 `Scenario` 和 `DDB` 等英文术语的大小写比较混杂，建议统一一种写法，避免笔记风格显得不够整洁。
- 末尾原来的占位符 `✓ Kimi Code 完成 (2026-07-30)` 已被替换为正式审查内容，这样不会残留未完成标记。

### 文档逻辑连贯性
- 文章从“连续系统”到“离散变分结构”再到“retraction 具体实现”，整体叙事是连贯的，符合论文的数学主线。
- 唯一比较跳跃的是从“离散 Lie-Poisson 更新”直接进入“刚体例子与 DDB 算法”，中间缺少一句过渡，说明为什么刚体是最自然的验证对象，以及这个例子如何对应前面的抽象构造。补一句“刚体是 `SO(3)` 上最标准的有限维测试床，因此可以直接验证轨道保持与能量衰减”会更顺。
- “关键性质”和“核心启发”两处有些重复，可以保留，但最好让前者偏公式结论、后者偏研究启发，避免语义重叠。

### 给 Doctor 的 3 个深入问题
1. 如果把这里的双括号耗散推广到 `Diff_vol` 或其他无限维 Lie 群，`Ad^*` 精确保轨道在连续极限和离散实现之间还会保持同样强的意义吗？在数值上，有限维截断会首先破坏 Casimir 还是先破坏轨道切向性？
2. 文中构造的耗散项本质上仍是一个 `ad^*` 型向量场。对于几何流体动力学里的选择性衰减问题，是否可以把这种构造和 Kelvin 定理或动量映射框架统一起来，形成“只在叶内部耗散、但不离开叶”的一般理论？
3. 如果把 `\tau` 从 `\exp` / Cayley 换成更一般的 retraction，离散双括号结构的阶数、稳定性和轨道保持会如何权衡？是否存在一个“最优 retraction”准则，使得在保持几何结构的同时最大化长时间能量耗散的真实性？
