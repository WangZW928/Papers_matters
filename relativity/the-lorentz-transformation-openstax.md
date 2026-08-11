# 洛伦兹变换（OpenStax 大学物理 III §5.6 教材精读）

# The Lorentz Transformation (OpenStax University Physics Vol. 3, §5.6)

**来源：** OpenStax *University Physics Volume 3 — Optics and Modern Physics*，第 5 章 *Relativity*，§5.6 The Lorentz Transformation
**作者：** Samuel J. Ling, Jeff Sanny, William Moebs 等（OpenStax / Rice University）
**链接：** [phys.libretexts.org §5.6](https://phys.libretexts.org/Bookshelves/University_Physics/University_Physics_(OpenStax)/University_Physics_III_-_Optics_and_Modern_Physics_(OpenStax)/05:__Relativity/5.06:_The_Lorentz_Transformation)
**性质：** 教材章节精读（非论文，不进入 CODEX_DEEP_READ.md 论文 Tier 索引）
**阅读状态：** 🔬 精读（Doctor 指定）
**流程状态：** ①元数据 ✓ | ②初稿 ✓ | ③评估 ✓(精读) | ④补充 ✓ | ⑤索引 ⏭️(非论文) | ⑥review ✓ | ⑦提交 ✓

---

## 摘要

### 中文翻译
本节从经典力学的伽利略变换出发，指出其与爱因斯坦两条公设的矛盾（同一光脉冲在不同惯性系中速度不同），进而推导出满足光速不变的洛伦兹变换。随后用三个例题展示洛伦兹变换如何统一复现时间膨胀、长度收缩与同时性的相对性；最后引入四维时空与时空间隔 $\Delta s^2=\Delta x^2+\Delta y^2+\Delta z^2-(c\Delta t)^2$，证明其在洛伦兹变换下不变，把洛伦兹变换解释为时空中的"旋转"，并给出世界线、固有时与光锥的几何图像——相对论效应是时空本身的性质，而非电磁学的特殊效应。附带一个推论练习：$d\tau = dt/\gamma$（固有时与坐标时的关系）。

### 原文要点
> Learning objectives: (1) Describe the Galilean transformation of classical mechanics; (2) Derive the corresponding Lorentz transformation equations, which are consistent with special relativity; (3) Explain the Lorentz transformation and many of the features of relativity in terms of four-dimensional space-time.
>
> "…to support the view that the consequences of special relativity result from the properties of time and space itself, rather than electromagnetism."

---

## 文章总结

### 1. 解决什么问题？
牛顿力学中联系两个惯性系的伽利略变换隐含绝对时间假设 $t=t'$，导致光速随参考系线性叠加（$u_x=u_x'+v$），与爱因斯坦公设（光速不变）直接冲突。需要找到一组新的坐标变换，使光球方程 $x^2+y^2+z^2-c^2t^2=0$ 在一切惯性系中形式不变。

### 2. 用了什么方法论？
纯公设 + 代数推导：
1. 由长度收缩效应（此前章节已从公设推出）直接给出 $x'=(x-vt)/\sqrt{1-v^2/c^2}$；
2. 联立光球不变条件 $x^2-c^2t^2=x'^2-c^2t'^2$，解出时间变换 $t'=(t-vx/c^2)/\sqrt{1-v^2/c^2}$；
3. 用三个"识别已知量 → 列方程 → 计算"的标准例题验证推论；
4. 用四维时空几何（世界线、间隔、光锥）重新诠释，把洛伦兹变换类比为三维旋转。

### 3. 主要结论是什么？
- 洛伦兹变换是唯一满足光速不变的惯性系间坐标变换，其逆变换形式对称；
- 时间膨胀、长度收缩、同时性相对性全部可由洛伦兹变换**一个公式组**统一导出（三个例题分别复现）；
- 时空间隔 $\Delta s^2$ 是洛伦兹不变量，等价于三维空间中距离 $\Delta r^2$ 在旋转下的不变性；
- 固有时 $c^2\Delta\tau^2=-\Delta s^2$ 也是洛伦兹不变量，所有惯性系一致；
- 光锥（$\Delta s^2=0$ 曲面）把时空划分为类时/类光/类空区域，因果结构由此确定。

---

## 价值评估

Doctor 指定精读（跳过 Codex 价值评估）。作为教材章节，其价值在于把"两条公设 → 变换方程 → 全部运动学推论"的推导链条一次性打通，是仓库中 Einstein 1905 精读笔记（`relativity/on-the-electrodynamics-of-moving-bodies.md`）的现代化教学复述，并首次给出**四维时空几何化**视角——这与 Doctor 主线中"寻找结构不变量并把结构变成可计算表达"的思路在几何层面直接共鸣（参见学习路线规划"扩散、Wick rotation 与 Lorentz invariance"侧线）。

---

## 公式与代码梳理

### 1. 伽利略变换及其推论

事件在惯性系 $S$ 中记为 $(x,y,z,t)$；$S'$ 以速度 $v$ 沿 $x$ 轴相对 $S$ 运动。伽利略变换：

\[x = x' + vt,\qquad y = y',\qquad z = z',\qquad t = t'\]

隐含假设：两系时间测量相同（绝对时间）。对时间求导得速度合成与加速度变换：

\[u_x = u_x' + v,\quad u_y = u_y',\quad u_z = u_z';\qquad a_x = a_x',\quad a_y = a_y',\quad a_z = a_z'\]

关键点：**加速度在两系中相同**、质量不变、距离不变 ⇒ 牛顿第二定律 $F=ma$ 在一切惯性系形式相同 ⇒ 力学满足相对性原理（公设一）。但速度合成律使光速变为 $c-v$，违反公设二。

### 2. 洛伦兹变换的推导（两条思路）

**光球条件**：闪光脉冲的波前在 $S$ 中满足 $r=ct$，即

\[x^2+y^2+z^2-c^2t^2 = 0,\qquad x'^2+y'^2+z'^2-c^2t'^2 = 0\]

两式左边同为 0 故相等；又 $y=y'$、$z=z'$，得核心约束：

\[x^2-c^2t^2 = x'^2-c^2t'^2\]

伽利略变换（$t=t'$，$x=x'+vt'$）无法满足此式（代回可得 $2vxt'+v^2t'^2=0$，非零 $v$ 下不成立）。

**推导（教材路径）**：设事件在 $S'$ 中为 $(x',0,0,t')$、在 $S$ 中为 $(x,0,0,t)$。原点重合瞬间闪光，$S$ 中 $S'$ 原点位于 $x=vt$；$S'$ 观测者（借助 $S$ 中的朋友）测得事件到 $S'$ 原点的距离为 $x'\sqrt{1-v^2/c^2}$（这正是长度收缩的结论），故

\[x = vt + x'\sqrt{1-v^2/c^2}\quad\Longrightarrow\quad x' = \frac{x-vt}{\sqrt{1-v^2/c^2}} \tag{*}\]

将 (*) 代入光球不变约束 $x^2-c^2t^2=x'^2-c^2t'^2$，解出

\[t' = \frac{t-vx/c^2}{\sqrt{1-v^2/c^2}}\]

**洛伦兹变换（正变换，$S'\to S$ 视角整理）：**

\[t = \frac{t' + vx'/c^2}{\sqrt{1-v^2/c^2}},\qquad
x = \frac{x' + vt'}{\sqrt{1-v^2/c^2}},\qquad
y = y',\qquad z = z'\]

**逆变换**（互换带撇量并替换 $v\to-v$）：

\[t' = \frac{t - vx/c^2}{\sqrt{1-v^2/c^2}},\qquad
x' = \frac{x - vt}{\sqrt{1-v^2/c^2}},\qquad
y' = y,\qquad z' = z\]

历史注记：H. A. Lorentz (1853–1928) 最先提出该变换，但其原始论证基于（后来被证明错误的）以太收缩假说；正确的理论基础是爱因斯坦的狭义相对论。

### 3. 三个例题：一个公式组统一三大效应

**例 1（时间膨胀）**：飞船 $S'$ 以 $c/2$ 相对 $S$ 运动，船长发出持续 $\Delta t'=1.2\,\mathrm s$ 的信号（钟在 $S'$ 静止 ⇒ $\Delta x'=0$）。用正变换的时间式：

\[\Delta t = \frac{\Delta t' + v\Delta x'/c^2}{\sqrt{1-v^2/c^2}} = \frac{\Delta t'}{\sqrt{1-v^2/c^2}} = \frac{1.2}{\sqrt{1-(1/2)^2}} = 1.4\,\mathrm s\]

> 洛伦兹变换自动复现时间膨胀公式；$\Delta x'=0$ 是"同地两事件"的条件。

**例 2（长度收缩）**：$S$ 中街道长 $L=100\,\mathrm m$（两端同时测量，$\Delta t=0$）。飞船 $S'$ 以 $0.20c$ 掠过，测得的长度：

\[L' = x_2'-x_1' = (x_2-x_1)\sqrt{1-v^2/c^2} = (100\,\mathrm m)\sqrt{1-0.2^2} = 98.0\,\mathrm m\]

> 关键：收缩来自"同时性标准不同"——$S$ 中同时测两端（$\Delta t=0$），代入 $x_2-x_1=(x_2'-x_1')/\sqrt{1-v^2/c^2}$。

**例 3（同时性的相对性）**：轨道旁观测者看到 26 m 车厢两端灯泡同时闪亮（$\Delta t=0$），车速 $c/2$。车厢中点的乘客测得两闪时间差：

\[0 = \frac{\Delta t' + v\Delta x'/c^2}{\sqrt{1-v^2/c^2}}
\quad\Longrightarrow\quad
\Delta t' = -\frac{v\Delta x'}{c^2} = -\frac{(c/2)(26\,\mathrm m)}{c^2} = -4.33\times10^{-8}\,\mathrm s\]

> 负号：$x'$ 较大的一端（右端灯）先闪。**同一变换，同时性成了相对量。**

### 4. 四维时空与间隔不变性

把事件放在 $(x,y,z,ct)$ 四维坐标中，定义两事件的**时空间隔**：

\[\Delta s^2 = (\Delta x)^2 + (\Delta y)^2 + (\Delta z)^2 - (c\Delta t)^2\]

三维距离 $\Delta r^2$ 在坐标轴旋转下不变；类比地，$\Delta s^2$ 在洛伦兹变换下不变。直接代入正变换可验证（交叉项 $v\Delta t'\Delta x'$ 恰好抵消）：

\[\Delta s^2 = (\Delta x')^2 + (\Delta y')^2 + (\Delta z')^2 - (c\Delta t')^2 = \Delta s'^2\]

粒子的轨迹（每个时刻一个事件）称为**世界线**：静止粒子世界线平行于时间轴，匀速运动为斜直线 $x=vt$，加速运动为曲线。微分形式：

\[ds^2 = dx^2 + dy^2 + dz^2 - c^2 dt^2\]

### 5. 洛伦兹变换 = 时空中的旋转

引入 $\beta = v/c$、$\gamma = 1/\sqrt{1-\beta^2}$，洛伦兹变换（$x,ct$ 部分）写成矩阵：

\[
\begin{pmatrix} x' \\ ct' \end{pmatrix}
=
\begin{pmatrix} \gamma & -\beta\gamma \\ -\beta\gamma & \gamma \end{pmatrix}
\begin{pmatrix} x \\ ct \end{pmatrix}
\]

与绕 $z$ 轴的二维旋转 $\begin{pmatrix} x' \\ y' \end{pmatrix} = \begin{pmatrix} \cos\theta & \sin\theta \\ -\sin\theta & \cos\theta \end{pmatrix}\begin{pmatrix} x \\ y \end{pmatrix}$ 结构相同（$\gamma \leftrightarrow \cos\theta$，$\beta\gamma \leftrightarrow \sin\theta$）。

**但有一个关键差异**：普通旋转保持轴垂直与各轴尺度；涉及时间轴的洛伦兹变换不保持这些欧氏特征——因为度规不同（时间项带负号）。数学上，若用**快度** $\eta$（rapidity）定义 $\tanh\eta=\beta$，则 $\gamma=\cosh\eta$、$\beta\gamma=\sinh\eta$，洛伦兹变换正是 Minkowski 度规下的"双曲旋转"。而 Wick rotation（$t\to i\tau$）把 $\cosh/\sinh$ 变成 $\cos/\sin$，正是把 Minkowski 几何变成欧氏几何的桥梁。

### 6. 固有时与光锥

$\Delta s^2$ 可正可负。当两事件满足 $(\Delta x)^2+(\Delta y)^2+(\Delta z)^2 < (c\Delta t)^2$（$\Delta s^2<0$）时，定义**固有时**

\[c^2\Delta\tau^2 = -\Delta s^2\]

其意义：在"两事件同地发生"的参考系中 $\Delta x=\Delta y=\Delta z=0$，故 $c^2\Delta\tau^2=(c\Delta t)^2$——固有时就是同地事件的坐标时间间隔（此前讨论的 proper time）。由于 $\Delta s$ 是洛伦兹不变量，**固有时也是洛伦兹不变量**，所有惯性系对其一致。微分形式 $d\tau = \sqrt{-ds^2}/c = dt/\gamma$（练习：把 $ds^2$ 展开、提出 $dt^2$ 即得）。

**光锥**（本节末尾，原文抓取被截断，以下为标准内容）：以某事件为原点，把三个空间坐标合为一条水平轴、$ct$ 为纵轴。满足 $\Delta s^2=0$（即 $\Delta r^2=(c\Delta t)^2$）的事件构成**光锥面**（类光/零间隔）；锥内 $\Delta s^2<0$（类时间隔，可通过低于光速的信号联系，具有因果序）；锥外 $\Delta s^2>0$（类空间隔，无法因果联系）。由于洛伦兹变换保持 $\Delta s^2$ 不变，它**不改变间隔的符号**，因此因果结构（谁在谁的过去/将来）是洛伦兹不变的——这是"超光速信号会导致因果悖论"的几何表述。

### 7. 原文勘误（LibreTexts 版）

- 伽利略变换第三式原文印作 $x=z'$，应为 $z=z'$（排版错误）。
- 例 1 题干 "The time signal starts as $(x', t'_1)$ and stops at $(x', t'_1)$" 应为 $t'_2$。
- 例 2 的已知量写 $\Delta\tau=0$，语义应为 $\Delta t=0$（$S$ 中同时测量）。
- 练习 1 解答中 $dx^2+dx^2+dx^2$ 应为 $dx^2+dy^2+dz^2$（原文错误，等式末行结果正确）。

---

## 与库内论文的关联

- **Einstein 1905**（`relativity/on-the-electrodynamics-of-moving-bodies.md`，Tier 3 #32）：本节的推导链条正是该论文 §2–§3（同时性定义与坐标变换）的现代复述；1905 原文从"同时性的操作定义"出发，本节则直接由长度收缩+光球条件代数导出，两条路线殊途同归。
- **Einstein 1907**（`relativity/on-the-relativity-principle-and-the-conclusions-drawn-from-it.md`，Tier 3 #38）：把相对性原理向非惯性系与热力学推广的过渡，本节是其运动学基础。
- **扩散方程与狭义相对论相容性**（`wave-mechanics/diffusion-equation-is-compatible-with-special-relativity.md`，Tier 3 #44）：抛物型扩散方程不是洛伦兹协变的——本节的光锥因果结构正是理解"相对论性扩散必须改造"的几何背景，直接服务于学习路线规划中"扩散、Wick rotation 与 Lorentz invariance 是否冲突"侧线。
- **几何流体/量子涡主线**：$\Delta s^2$ 不变性与 Hamiltonian/Poisson 结构中的守恒不变量在"寻找变换下不变的结构量"这一方法论上同构；Madelung 变换（`geometric-fluid/geometric-hydrodynamics-via-madelung-transform.md`）中 Schrödinger 方程对 Galilean boost 的协变性与本节相对论运动学也有关联。

---

## Review Questions

1. 伽利略变换下加速度不变（$a_x=a'_x$），牛顿第二定律因此在所有惯性系形式相同。对洛伦兹变换求导得到的速度合成律 $u_x=(u'_x+v)/(1+u'_xv/c^2)$ 在 $u'_x\to c$ 时给出 $u_x=c$；但加速度**不再**不变。试推导洛伦兹变换下的加速度变换，说明为什么相对论动力学必须放弃 $F=ma$（常质量）而采用 $F=d(\gamma m v)/dt$。这与 1905 论文中"纵向/横向质量"的引入有何对应？

2. 把洛伦兹变换写成快度形式（$\tanh\eta=\beta$，$\gamma=\cosh\eta$，$\beta\gamma=\sinh\eta$），它成为 Minkowski 度规下的双曲旋转。Wick rotation $t\to i\tau$ 将 $\cosh\to\cos$、$\sinh\to i\sin$，把双曲旋转变成欧氏旋转。试写出 Wick 旋转后的变换矩阵，并讨论：若把这一"度规符号翻转"机械地用到扩散方程上会得到什么（与 Tier 3 #44 的结论对照）？

3. 光锥把时空分为类时（$\Delta s^2<0$）、类光（$=0$）、类空（$>0$）三类间隔。洛伦兹变换保持 $\Delta s^2$ 不变，因而保持因果序。但若允许 $v>c$ 的"参考系"（如 tachyonic 理论），变换矩阵将含虚数 $\gamma$，间隔符号不再保持。试论证：类空事件对的时序不可能靠洛伦兹变换颠倒，除非存在超光速信号——并说明这是否意味着"类空关联"（如 EPR 纠缠）必然违反相对论因果性，还是仅仅不传递信息即可。
