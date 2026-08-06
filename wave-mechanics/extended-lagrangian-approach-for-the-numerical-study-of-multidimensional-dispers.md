# 扩展拉格朗日方法用于多维色散波数值研究：以 Serre-Green-Naghdi 方程为例

**作者：** Sergey Tkachenko

**DOI：** [10.1016/j.jcp.2022.111901](https://doi.org/10.1016/j.jcp.2022.111901)

**源 PDF：** `1-s2.0-S0021999122009640-main.pdf`

**阅读状态：** 🔬 精读
**流程状态：** ①元数据 ✓ | ②初稿 ✓ | ③评估 ✓(精读) | ④补充 ✓ | ⑤索引 ✓ | ⑥review ✓ | ⑦提交 ⏳

---

## 摘要

### 中文翻译

本文用 extended Lagrangian / hyperbolic relaxation 技巧处理多维色散水波方程（SGN 类）：把色散项引入辅助变量并加惩罚约束，构造无条件双曲的近似系统，从而可用显式双曲求解器达到粗网格上的色散精度，显著降低网格需求。

## 价值评估

**Doctor 指定精读。** 按 6 级标准，这篇应按 **4/6：方法相关精读** 处理：idea 清晰，用 extended Lagrangian/hyperbolic relaxation 把多维非线性色散系统改写成无条件双曲近似；计算结果覆盖 1D/2D SGN 浅水波和色散冲击，数值实用性强；预言能力依赖松弛尺度和色散参数，适合工程波浪和多物理框架；方法新颖性中高，核心思想来自 Favrie-Gavrilyuk，本文推广到 SGN/IKW 等系统；来源为 JCP 2022，可信度高。精读判断：它与 Doctor 的 Hamiltonian/变分结构、IMEX、AMR 和 HPC PDE 框架直接相关。

## 公式与代码梳理

#### 数学结构与核心公式

Serre-Green-Naghdi 方程描述非静水、弱色散、全非线性浅水波。基本变量是水深 $h(x,t)$ 和水平速度 $u(x,t)$。一维质量守恒为

$$
\partial_t h+\partial_x(hu)=0 .
$$

经典浅水动量通量是

$$
\partial_t(hu)+\partial_x\left(hu^2+\frac12gh^2\right)=0 .
$$

SGN 在此基础上加入色散/非静水修正。常见一维形式可写为

$$
\partial_t(hu)+\partial_x\left(hu^2+\frac12gh^2+\frac13h^2\gamma\right)=0 ,
$$

其中 $\gamma$ 表示垂向加速度型量，典型表达为

$$
\gamma=h\left((\partial_xu)^2-\partial_x\partial_tu-u\partial_{xx}u\right).
$$

多维形式中，质量方程是

$$
\partial_t h+\nabla\cdot(hu)=0 ,
$$

动量方程包含非静水压力或材料导数相关项。SGN 的困难在于：色散项含高阶空间导数和时间-空间混合导数，使系统不再是标准双曲守恒律，也不适合直接处理间断初值和 Riemann solver。

论文从变分结构出发。SGN 可由 Lagrangian 得到，简化地写成

$$
\mathcal L(h,u,D_th)
=\frac12h|u|^2-\frac12gh^2+\frac16h(D_th)^2 ,
$$

其中

$$
D_t h=\partial_t h+u\cdot\nabla h .
$$

更一般地，作者考虑压力依赖材料导数的 Euler-Lagrange 系统。extended Lagrangian 的核心是引入松弛变量，把 $D_t h$ 这类高阶诱因替换为新变量，例如

$$
q\approx D_t h .
$$

同时加入惩罚/松弛能量，使扩展 Lagrangian 形如

$$
\mathcal L_\epsilon(h,u,q)
=\frac12h|u|^2-\frac12gh^2+\frac16hq^2
-\frac1{2\epsilon^2}(q-D_th)^2 .
$$

不同论文记号可能把松弛参数写作 $\alpha$、$\varepsilon$ 或 $c$；其作用相同：当 $\epsilon\to0$ 时强制 $q\to D_th$，恢复原 SGN 色散结构；有限 $\epsilon$ 时得到一阶扩展系统。

扩展系统的目标是无条件双曲。抽象地，变量可写为

$$
U=(h,hu,q,\ldots),
$$

满足

$$
\partial_t U+\nabla\cdot F(U)=S_\epsilon(U).
$$

其中 $F(U)$ 是双曲通量，$S_\epsilon$ 是刚性松弛源项。双曲部分允许使用有限体积、Riemann solver、TVD/WENO、AMR；刚性源项和色散恢复项用隐式处理。

时间离散采用 IMEX 思路：

$$
\frac{U^{n+1}-U^n}{\Delta t}
= -\mathcal H(U) + \mathcal S(U),
$$

其中 $\mathcal H$ 是显式双曲算子，$\mathcal S$ 是隐式松弛/色散算子。二阶 ARS(2,2,2) 类格式可抽象写为

$$
U^{(i)}=U^n-\Delta t\sum_{j<i}\tilde a_{ij}\mathcal H(U^{(j)})
+\Delta t\sum_{j\le i}a_{ij}\mathcal S(U^{(j)}),
$$

最后

$$
U^{n+1}=U^n-\Delta t\sum_i\tilde b_i\mathcal H(U^{(i)})
+\Delta t\sum_i b_i\mathcal S(U^{(i)}).
$$

显式 CFL 主要受重力波速控制：

$$
\Delta t\le C_{\rm CFL}\frac{\Delta x}{|u|+\sqrt{gh}},
$$

而不是被色散高阶导数强制到 $\Delta x^3$ 量级。这是该方法对 HPC 的关键意义。

#### 关键推导

第一步是识别 SGN 的“非双曲来源”。浅水方程本身是双曲守恒律，因为通量 Jacobian 特征值为

$$
\lambda_\pm=u\pm\sqrt{gh}.
$$

SGN 的色散项引入 $\partial_{xxt}u$、$\partial_{xxx}u$ 等高阶项，使系统不能直接写成局部一阶守恒律。extended Lagrangian 通过引入 $q$ 把高阶材料导数局部化，使主部重新成为一阶系统。

第二步是松弛极限。若源项中包含

$$
\frac1{\epsilon^2}(q-D_th),
$$

则当 $\epsilon\to0$，有约束

$$
q=D_th+O(\epsilon^2).
$$

把这个关系代回扩展系统，得到原始 SGN 的色散压力项。因此扩展模型不是任意 artificial compressibility，而是带有变分一致性的 hyperbolic approximation。

第三步是 IMEX 稳定性。若把系统线性化为

$$
\partial_t U+A\partial_xU=\frac1{\epsilon}RU,
$$

显式处理 $R/\epsilon$ 会要求

$$
\Delta t=O(\epsilon).
$$

IMEX 把 $A\partial_xU$ 显式、$RU/\epsilon$ 隐式，于是 CFL 由双曲波速决定，而刚性松弛由局部或椭圆型隐式求解吸收。对色散波，这等价于避免高阶导数带来的小步长限制。

#### 对 HPC 框架的启示

这篇对 Doctor 的框架启示在于：对非标准 PDE，不一定直接离散原方程；可以先做结构化变量扩展，把问题转成框架擅长的双曲守恒律 + 刚性源项。这样 AMR、Riemann solver、GPU stencil、限幅器、ghost exchange 都能复用。SGN 色散部分则进入 IMEX implicit backend，可由 matrix-free Krylov、multigrid 或 JFNK 处理。

与 `Hamiltonian structure for water waves` 的关系是：SGN 来自变分/拉格朗日结构，extended Lagrangian 保留了这条来源，而不是纯经验松弛。与 `JFNK` 的关系是：每个隐式 stage 可能需要解非线性残差

$$
R(U^{(i)})=0 .
$$

Jacobian-free Newton-Krylov 可以避免显式装配复杂色散 Jacobian；预条件器可用浅水双曲 block 加局部松弛 block 近似。

对 AMR，双曲部分可自然使用 refinement、reflux 和 shock capturing；但色散项跨 stencil 更宽，coarse-fine 边界需要额外一致性。一个实用设计是：显式守恒通量走 AMR reflux，隐式色散/松弛走 level solve 或 composite solve，并监控质量、动量和 Hamiltonian-like energy 漂移。

对 AI4Physics，extended variables $q$ 等可作为神经算子的辅助通道。直接学习 $h,u$ 的 SGN 演化会把高阶色散隐藏在黑箱中；学习扩展双曲系统则可把波速、松弛尺度、守恒通量显式暴露，便于做结构保持网络或 physics-informed loss。

#### 待深入研究

1. extended Lagrangian 的松弛参数如何与网格尺度、波数范围和物理色散关系匹配，才能避免过度耗散或虚假高频波？
2. 在 AMR 上，色散项的隐式 composite solve 如何与双曲 reflux 保持质量、动量和能量一致？
3. 能否构造真正的离散变分/辛 IMEX 格式，使扩展系统不仅稳定，而且长期保持 SGN 的 Hamiltonian 结构？

## Review Questions

1. extended Lagrangian 方法把非双曲色散系统转成双曲松弛系统时，哪些守恒律是严格保留的，哪些只在 $\epsilon\to0$ 极限中恢复？
2. 对多维 SGN，IMEX 隐式部分更适合用 JFNK、multigrid 还是局部松弛求解？瓶颈主要来自椭圆耦合还是刚性源项？
3. 若用神经网络学习浅水色散波，扩展变量 $q$ 是否能作为更好的 latent state，使模型同时捕捉 shock、solitary wave 和 dispersive tail？

4. 扩展拉格朗日系统声称“无条件双曲”，这一性质在离散层面是否仍成立，还是只对连续模型和特定参数区间成立？
5. 对 SGN 这类色散系统，IMEX 的真正瓶颈是刚性源项、隐式椭圆耦合，还是高频色散模态与 shock-capturing 之间的不兼容？
6. 若将 extended variables 作为神经算子的辅助状态，怎样证明它们确实提升了可学习性，而不是只是增加了状态维数和训练负担？ 我先读取第二批内联文件，再逐篇给出审查意见。 我先补读文档11后半段，再把 7 到 11 一次性整理完。 **
tokens used
133,169

---
