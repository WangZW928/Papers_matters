# 论相对性原理及其推论（通往广义相对论的过渡论文）

# On the Relativity Principle and the Conclusions Drawn from It (Über das Relativitätsprinzip und die aus demselben gezogenen Folgerungen)

**作者：** Albert Einstein
**期刊：** Jahrbuch der Radioaktivität und Elektronik 4: 411-462, 1907（1907-12-04 收稿）
**DOI：** 无（1907 年期刊文章，无 DOI/arXiv）
**原文依据：** 德文原文扫描件（Internet Archive: jahrbuch-der-radioaktivitat-und-elektronik-4.1907, pp. 411-462；本库 `_full.txt` 为该扫描件的 OCR 文本）；英文参考 *The Collected Papers of Albert Einstein* Vol. 2（Beck 英译, Doc. 47）
**阅读状态：** 🔬 精读（Doctor 指定）
**流程状态：** ①元数据 ✓ | ②初稿 ✓ | ③评估 ✓(精读) | ④补充 ✓ | ⑤索引 ✓ | ⑥review ✓ | ⑦提交 ⏳

---

## 摘要

### 中文翻译
（原文无摘要。）这是一篇应编者之邀为《放射性与电子学年鉴》撰写的狭义相对论综述，但远不止综述：Einstein 借此把 1905 年狭义相对论系统化（运动学、动力学、电子论、光学），并在 §17-§18（加速系与引力场）迈出通往广义相对论的关键一步。核心新结果有三：其一，**等效原理**——均匀加速参考系与均匀引力场在局部不可区分，物理定律在加速系中的形式揭示了引力场的作用；其二，**引力红移与引力时间膨胀**——引力势高处钟走得更快，从低势处发出的光到高势处观测会发生红移，Einstein 由此估计太阳表面谱线红移量级 ~10⁻⁶；其三，**能量的引力质量**——能量 E 不仅具有惯性质量 E/c²，也具有同样大小的引力质量（能量有重量），这是质能关系的引力推广。论文还包含相对论动力学（运动质点的质量-速度关系、电子纵/横质量）、速度叠加、多普勒效应推广等完整推导。

### 原文
> （1907 年德文原文无摘要。论文首段）Die Newtonschen Bewegungsgleichungen behalten ihre Form, wenn man auf ein neues, relativ zu dem ursprünglich benutzten in gleichförmiger Translationsbewegung begriffenes Koordinatensystem transformiert ... Jene Unabhängigkeit vom Bewegungszustande des benutzten Koordinatensystems, im folgenden "Relativitätsprinzip" genannt, schien aber mit einem Male in Frage gestellt durch die glänzenden Bestätigungen, welche die H. A. Lorentzsche Elektrodynamik bewegter Körper erfahren hat.

---

## 文章总结

### 1. 解决什么问题？
把 1905 年狭义相对论写成系统综述（面向放射性与电子学读者），并解决其未覆盖的问题：相对性原理是否适用于**加速系统**？引力现象能否纳入相对论框架？若加速与引力等价，光在引力场中会有什么行为（红移）？能量是否也有"重量"（引力质量）？

### 2. 用了什么方法论？
- 从相对性原理与光速不变两条公设出发，系统推导洛伦兹变换及其全部推论（长度收缩、时间膨胀、速度叠加、多普勒、电子动力学）。
- 引入均匀加速参考系 K'（相对惯性系 K 以恒定加速度 γ 运动），对 K' 中静止的钟与杆作坐标变换分析：K' 中不同位置的钟速率不同，位置 x 处的钟相对 K 中同时钟的关系给出时间膨胀因子 (1 + γx/c²)。
- **等效原理**：加速系中出现的"惯性力场"在局部与均匀引力场不可区分；把 K' 中导出的结论直接翻译为引力场中的物理（引力势 Φ = γx 对应钟速率因子）。
- 由光在加速系中的传播分析推出引力红移：低势处发出的光在高势处观测频率降低 Δν/ν = -Φ/c²（对太阳估计 ~2×10⁻⁶）。
- 用能量守恒 + 等效原理推广质能关系：能量 E 的引力质量 = E/c²（能量有重量）。

### 3. 主要结论是什么？
相对性原理可推广到加速系：加速系等价于引力场（等效原理），引力场中钟慢、光红移、能量具有引力质量 E/c²。这些结论是广义相对论的直接先声——1911 年《论引力对光传播的影响》与 1915 年场方程都由此出发。同时该文把狭义相对论的全部标准结果整理成统一体系，是 1905 年论文（库内已精读）与 1916 年广义相对论之间的关键桥梁。

---

## 价值评估

Doctor 指定精读（跳过 Codex 价值评估）。

## 公式与代码梳理

（本小节由 Codex 精读补充，2026-08-04；德文 OCR 公式乱码处按标准文本重建）

### 1. 逐公式梳理数学逻辑

本文前四部分主要是对 1905 狭义相对论及 1907 Planck/Einstein 动力学结果的系统化重述，第五部分才是从 SR 通往 GR 的关键跃迁。其总逻辑是：先把惯性系中的时空、光学、动力学写成 Lorentz-covariant 形式，再问这些结论在加速系中如何改变，最后用等效原理把加速系解释为引力场。

**洛伦兹变换与运动学回顾**

设 $K'$ 以速度 $v$ 沿 $K$ 的 $x$ 轴运动，标准洛伦兹变换为

\[
x'=\gamma(x-vt),\qquad y'=y,\qquad z'=z,\qquad
t'=\gamma\left(t-\frac{vx}{c^2}\right),
\]

其中

\[
\gamma=\frac{1}{\sqrt{1-v^2/c^2}}.
\]

它不是坐标技巧，而是由两条要求共同固定的：真空光速在两个惯性系中均为 $c$，物理定律在两个惯性系中同形。由此，运动杆在运动方向发生长度收缩：

\[
L=L_0\sqrt{1-\frac{v^2}{c^2}}=\frac{L_0}{\gamma},
\]

运动钟相对静止钟变慢：

\[
\tau=\frac{\tau_0}{\sqrt{1-v^2/c^2}}=\gamma\tau_0.
\]

这里若 $\tau_0$ 是钟自身的固有周期，则外部惯性系看到该钟完成一周期需要更长时间；等价地，其频率变为 $\nu=\nu_0/\gamma$。速度叠加也随之替代伽利略公式。若 $K'$ 中质点沿同一方向速度为 $u$，则 $K$ 中速度为

\[
w=\frac{v+u}{1+vu/c^2}.
\]

这保证两个小于 $c$ 的速度合成后仍小于 $c$，并排除超光速信号导致的因果倒置。

**相对论动力学**

本文把电子/质点动力学写成

\[
\mathbf p=m\mathbf v,\qquad
m=\frac{m_0}{\sqrt{1-v^2/c^2}},
\]

即

\[
\mathbf p=\gamma m_0\mathbf v.
\]

力仍定义为动量变化率：

\[
\mathbf F=\frac{d\mathbf p}{dt}.
\]

但加速度方向与速度方向不同时，惯性响应不再由一个标量质量完全描述。沿速度方向的纵质量与垂直速度方向的横质量分别为

\[
m_{\parallel}=\frac{m_0}{(1-v^2/c^2)^{3/2}}=\gamma^3m_0,
\]

\[
m_{\perp}=\frac{m_0}{\sqrt{1-v^2/c^2}}=\gamma m_0.
\]

> 注：纵/横质量是按原文力定义 $\mathbf F=d\mathbf p/dt$ 得到的历史记号；现代表述中静质量 $m_0$ 不变，速度依赖写入动量 $\mathbf p=\gamma m_0\mathbf v$，不再引入方向依赖的“质量”。

更重要的是能量推导。由功-动能关系

\[
dK=\mathbf F\cdot d\mathbf x
\]

结合相对论动量积分，得到

\[
K=m_0c^2\left(\frac{1}{\sqrt{1-v^2/c^2}}-1\right)
=(\gamma-1)m_0c^2.
\]

因此总能量可写为

\[
E=K+m_0c^2=\gamma m_0c^2=mc^2.
\]

这比简单口号 $E=mc^2$ 更强：静止物体已有静止能

\[
E_0=m_0c^2,
\]

而运动能量只是总能量相对静止能的增量。本文 §11 还把结论推广到任意物理系统：系统能量增加 $\Delta E$，惯性质量增加

\[
\Delta M=\frac{\Delta E}{c^2}.
\]

这为后文“能量是否也有引力质量”埋下问题。

**光学推论：多普勒效应与光行差**

对平面光波相位作洛伦兹变换，可得频率与传播方向的变换。沿视线方向远离时，标准纵向多普勒公式为

\[
\nu=\nu_0\sqrt{\frac{1-v/c}{1+v/c}}.
\]

接近时符号相反。若发射源横向运动，即一阶经典多普勒项为零，仍有二阶效应：

\[
\nu=\nu_0\sqrt{1-\frac{v^2}{c^2}}=\frac{\nu_0}{\gamma}.
\]

这就是横向多普勒效应，本质上来自运动钟变慢。光行差来自波矢方向变换。若光线与相对速度方向夹角为 $\theta$，变换到另一惯性系后的角度 $\theta'$ 满足

\[
\cos\theta'=\frac{\cos\theta-v/c}{1-(v/c)\cos\theta}.
\]

（以上光学公式按现代常用记号重写，与原文记号体系等价。）

因此“光源位置”的观测方向不是几何绝对量，而依赖观察者运动状态。

**加速系中的时间：§17-§18 的关键公式**

Einstein 接着考虑均匀加速参考系 $K'$。为避免与洛伦兹因子混淆，这里把原文加速度记作 $a$；若沿用原文/题目记号，则 $a=\gamma_{\text{acc}}$。在某一瞬间，$K'$ 与惯性系 $K$ 共动。对 $K'$ 中坐标为 $x'$ 的静止钟，Einstein 得到局部时间 $\sigma$ 与参考时间 $\tau$ 的一阶关系：

\[
\sigma=\tau\left(1+\frac{a x'}{c^2}\right).
\]

等价地，位置 $x'$ 处静止钟相对原点钟的速率为

\[
\frac{d\sigma}{d\tau}=1+\frac{a x'}{c^2}.
\]

符号约定很重要：若 $x'$ 沿加速度方向增加，则更大的 $x'$ 处钟走得更快。精确形式在 Rindler 图像中对应指数或线性弱场近似；Einstein 在本文只保留一阶项。结论是：均匀加速系中不存在一个全局处处等速的时间，不同位置的钟速率不同，杆长与同时性定义也随位置而变。

**等效原理**

§18 的核心思想是：均匀加速系中的惯性力场，与均匀引力场在局部物理上等价。若令引力势为

\[
\Phi=a x',
\]

则加速系钟速率公式转化为引力场中的时间膨胀：

\[
\frac{d\tau_{\text{local}}}{dt}=1+\frac{\Phi}{c^2}.
\]

> 注：这是 1907 年的启发式弱场表述，仅在一阶近似下成立；现代 GR 中静态时空的精确红移公式为 $d\tau=\sqrt{1+2\Phi/c^2}\,dt$（弱场极限回到上式），两者不应混写。

势越高，钟越快；势越低，钟越慢。这是广义相对论时间观的胚胎。

**引力红移**

若光从势 $\Phi_1$ 处发出，在势 $\Phi_2$ 处被接收，静态观察者测得的频率满足弱场关系

\[
\frac{\nu_2}{\nu_1}
=1+\frac{\Phi_1-\Phi_2}{c^2}.
\]

从低势到高势，$\Phi_1<\Phi_2$，故

\[
\nu_2<\nu_1,
\]

即红移。若把无穷远势取为 $0$，太阳表面势为

\[
\Phi_\odot=-\frac{GM_\odot}{R_\odot},
\]

则从太阳表面到无穷远

\[
\frac{\Delta\nu}{\nu}\approx -\frac{GM_\odot}{c^2R_\odot}
\approx -2.1\times 10^{-6}.
\]

原文给出约 $2\times10^{-6}$ 的量级估计。按波长表示则

\[
\frac{\Delta\lambda}{\lambda}\approx +2\times10^{-6}.
\]

**能量的引力质量**

§20 的结论是质能关系的引力推广。若局部测得能量为 $E$，它在引力场中不仅贡献惯性质量

\[
m_{\text{inertial}}=\frac{E}{c^2},
\]

也具有引力质量

\[
m_{\text{gravitational}}=\frac{E}{c^2}.
\]

因此能量在引力场中有势能

\[
U=\frac{E}{c^2}\Phi.
\]

> 注：$U=(E/c^2)\Phi$ 是对“能量有重量”的一阶弱场表达，不是一般相对论中完整的物质-引力耦合势能。

这一步非常关键：1905 的 $E=mc^2$ 首先说明能量有惯性；1907 本文进一步说明能量有重量。它把能量、惯性、引力三者连到同一条线上。

**与 1905、1911、1915 的位置**

本文前半部分是对 1905 《Zur Elektrodynamik bewegter Körper》的系统化重述：洛伦兹变换、同时性、长度收缩、时间膨胀、速度叠加、多普勒、光行差、电子纵/横质量都属于 SR 框架内的整理与推广。真正的新结果集中在第五部分：等效原理、引力时间膨胀、引力红移、能量的引力质量。1911 年《论引力对光传播的影响》会更明确地发展光线弯曲和红移；1915 年场方程则把这里的启发式“均匀引力场/加速系等价”升级为一般协变的时空几何动力学。

### 2. 算法/代码流程梳理

> 注：以下为现代对应计算流程（含弱场/GR/GPS 工程化表述），不属于原文显式算法。

本文无代码，但可以把它的推理转成三个可计算流程。

第一，模拟均匀加速系中的钟同步与光传播。设惯性系中采用事件坐标 $(ct,x)$，构造一组 Rindler 观察者，其近似坐标满足

\[
d\tau(x')=\left(1+\frac{a x'}{c^2}\right)dt.
\]

算法上逐事件推进：先在惯性系中生成光线世界线 $x(t)=x_0\pm ct$，再用瞬时共动洛伦兹变换把事件投影到加速系，最后比较不同 $x'$ 处钟的固有时间累积。这样可直接看到同一束光在加速坐标中表现为弯曲轨迹，且不同高度钟的相位累积不同。

第二，用现代 GR 弱场极限验证红移。Schwarzschild 度规静态弱场近似给出

\[
d\tau=dt\sqrt{1+\frac{2\phi(r)}{c^2}}
\approx dt\left(1+\frac{\phi(r)}{c^2}\right),
\]

其中

\[
\phi(r)=-\frac{GM}{r}.
\]

两个半径 $r_1,r_2$ 处静态钟的频率比为

\[
\frac{\nu_2}{\nu_1}
\approx 1+\frac{\phi(r_1)-\phi(r_2)}{c^2}.
\]

数值上，太阳表面到无穷远为 $-2.1\times10^{-6}$；地球表面到无穷远约为

\[
-\frac{GM_\oplus}{c^2R_\oplus}\approx -7.0\times10^{-10}.
\]

第三，把引力时间膨胀纳入卫星导航/时频传递。对地面钟与轨道钟，先算引力势差

\[
\Delta_{\text{grav}}
=\frac{\phi_{\text{ground}}-\phi_{\text{sat}}}{c^2},
\]

再加上卫星运动导致的 SR 运动钟慢

\[
\Delta_{\text{SR}}\approx -\frac{v^2}{2c^2}.
\]

GPS 量级上，引力项约使卫星钟每天快 $45\ \mu s$，运动学项约使其每天慢 $7\ \mu s$，净效应约每天快 $38\ \mu s$。这正是本文引力红移与 SR 时间膨胀合并后的工程化后代。

### 3. 与库内相关论文的关联

- `relativity/on-the-electrodynamics-of-moving-bodies.md`：1905 SR 奠基论文。本文是其系统化与推广，衔接点是洛伦兹变换、速度叠加、光学效应、电子动力学，以及由 $E=mc^2$ 走向“能量有重量”。
- `geometric-fluid/hamilton-principle-for-the-vortex-flow-of-an-ideal-fluid-in-special-relativity.md`：展示 SR 框架如何进入连续介质与流体涡旋动力学。它承接的是本文前四部分确立的 Lorentz-covariant 物理建模语言。
- `geometric-fluid/hamiltonian-description-of-the-ideal-ﬂuid.md`：对应 Hamiltonian 结构主线。本文 §9 已把相对论质点力学写入 Lagrange/Hamilton 原理，是从粒子到场/流体 Hamiltonian 化的早期接口。
- `differential-geometry/a-geometric-derivation-of-the-einstein-equations-from-the-causal-action-principle.md`：现代从变分原理和几何结构推出 Einstein 方程；与本文形成方法论对照：1907 是从物理公设和启发式等效原理推出可观测结论，现代几何论文则从作用量、Lorentz 度量和 Euler-Lagrange 方程导出场方程。
- `ai-theory/neural-tangent-kernel-convergence-and-generalization-in-neural-networks.md`、`ai-model/deep-equilibrium-models.md`：关联较远，但可作为“物理归纳偏置”的现代参照。Lorentz invariance/协变性在物理建模中扮演硬约束角色，类似现代 ML 中用核结构、不动点结构或等变结构限制假设空间。

对 Doctor 的知识链而言，本文位于“相对论协变性 + 物理建模”的枢纽：它一端连接 1905 SR 的惯性系协变性，另一端开启引力、非惯性系、局部等效、时间膨胀与几何化建模的主线。

## Review Questions

1. 1907 文中“均匀加速系 ≡ 均匀引力场”的推理，和库内 [Einstein 1905](../relativity/on-the-electrodynamics-of-moving-bodies.md) 的惯性系协变性、以及 [因果作用原理推导 Einstein 方程](../differential-geometry/a-geometric-derivation-of-the-einstein-equations-from-the-causal-action-principle.md) 的局部几何化之间，分别在哪一步从“物理直觉”变成了“可计算结构”？
2. 这篇笔记把引力红移、钟慢、能量有重量放在一起讲；如果把它们统一成一个弱场近似框架，哪些公式应明确标注为 1907 的启发式结果，哪些应标注为后来的 GR/弱场极限？
3. 与 [Hamiltonian description of the ideal ﬂuid](../geometric-fluid/hamiltonian-description-of-the-ideal-ﬂuid.md) 和 [Hamilton principle for the vortex flow of an ideal fluid in special relativity](../geometric-fluid/hamilton-principle-for-the-vortex-flow-of-an-ideal-fluid-in-special-relativity.md) 对照时，1907 这篇“先建等效、再推广”的方法，对构造协变的守恒量或结构保持约束最有启发的一点是什么？
