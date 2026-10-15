# Quantum Simulation of Partial Differential Equations via Schrödingerization

**作者：** Shi Jin, Nana Liu, Yue Yu

**发表：** Physical Review Letters 133, 230602 (2024)

**DOI:** [10.1103/PhysRevLett.133.230602](https://doi.org/10.1103/PhysRevLett.133.230602)

**Source PDF:** `PhysRevLett.133.230602.pdf`

**阅读状态：** 🔬 精读
**流程状态：** ①元数据 ✓ | ②初稿 ✓ | ③评估 ✓(精读) | ④补充 ✓ | ⑤索引 ✓ | ⑥review ✓ | ⑦提交 ⏳

---

## 摘要

### 中文翻译

Schrödingerization（Jin 等，PRL 2024）：通过 warped phase transformation 与辅助维提升，把一般线性 ODE/PDE 的非幺正演化（如 heat、Fokker-Planck、Black-Scholes）转化为高维 Schrödinger 方程，从而可用量子模拟（Hamiltonian simulation）求解。

## 价值评估

Doctor 指定精读。本文通过 warped phase transformation 把一般线性 ODE/PDE 的非幺正演化提升为高一维 Schrödinger 型幺正演化。它给出的是理论算法框架；完整场重构仍受输入制备、归一化与测量成本限制，故“量子加速”必须按目标 observable 而非仅按演化复杂度判断。

## 公式与代码梳理

### 符号约定与可归一化的提升

统一使用本笔记的 $\dot u=-Au$ 约定，令

\[
A=H+i\bar H,\qquad H=\frac{A+A^\dagger}{2},\qquad
\bar H=\frac{A-A^\dagger}{2i}.
\]

两者均 Hermitian。先假设 $H\succeq0$。在辅助变量 $p>0$ 上定义 $v(t,p)=e^{-p}u(t)$，并把**初值**延拓为整轴上的 $v(0,p)=e^{-|p|}u(0)$。随后在整轴解输运系统，而不是在负半轴也强行定义 $v(t,p)=e^{-|p|}u(t)$。初值可平方积分，能够做 Fourier 变换和量子态归一化。

在正半轴，$\partial_pv=-v$，所以

\[
\partial_t v-H\partial_pv+i\bar H v=0.
\]

输运速度矩阵是 $-H$，其特征速度非正；在上述假设下正半轴不依赖负半轴向右传入的数据。一般增长系统若不满足 $H\succeq0$，需要另行控制恢复区域、谱界或做平移变换，不能无条件使用全部 $p>0$。

采用 $\widetilde v(\eta)=\int_{\mathbb R}e^{-i\eta p}v(p)\,dp$，有 $\partial_p\mapsto i\eta$，得到

\[
i\partial_t\widetilde v=(-\eta H+\bar H)\widetilde v.
\]

因为 $\eta\in\mathbb R$，这个生成元是 Hermitian。按“物理状态空间 $\otimes$ 辅助 Fourier 空间”的排列，离散后为

\[
H_{\rm total}=-H\otimes D+\bar H\otimes I,
\qquad |\widetilde v(t)\rangle=e^{-iH_{\rm total}t}|\widetilde v(0)\rangle.
\]

有限辅助区间的截断、周期化和网格误差需要单独分析。

### 恢复与标量检验

正半轴上可由 $u(t)=e^p v(t,p)$ 恢复，也可在连续、未归一化表示下用

\[
u(t)=\int_0^\infty v(t,p)\,dp.
\]

量子实现涉及归一化、辅助寄存器投影/后选择及其成功概率，不能理解为免费读出全部场分量。态方向、范数和物理观测量的恢复成本应分别计算。

补充自检：取 $A=a>0$、$\bar H=0$，输运解为 $v(t,p)=e^{-|p+at|}u_0$；对 $p>0$，$e^p v(t,p)=e^{-at}u_0$，与原 ODE 一致。若用原笔记的 $e^{+p}$ 正半轴初值，整轴 Fourier/量子态归一化就不成立；修正指数时必须同步修改输运号和 Hamiltonian 的号。

### 对 HPC 框架的启示与限制

空间离散后的耗散矩阵可用这一提升构造 Hermitian 算子。matrix-free 实现只需分别调用 $H$、$\bar H$ 和辅助 Fourier 乘子，无需形成 Kronecker 矩阵。应把额外维数、FFT、输入制备与输出恢复纳入成本。

高维系统幺正并不消除原问题的病态性：逆热方程的高频放大、初值噪声和恢复条件数不会因为提升自动消失。因此，这不是逆热问题无条件稳定求解或端到端量子加速的证明。

### 进一步研究问题

1. 如何从特征速度与谱界判断哪些 $p$ 区域能恢复原解？$H$ 不半正定时怎样调整？
2. 若只需要低阶矩而不是全场，输入、演化、后选择与测量各占多少成本？
3. 对 GPU 上的 $-H\otimes D+\bar H\otimes I$，辅助维数和数据布局如何决定 FFT 与空间算子的瓶颈？

## Review Questions

1. 原解恢复为何必须与辅助变量的延拓、特征速度和后选择概率一起分析？
2. 对非正规或增长的系统，哪些谱界决定有效恢复区域？
3. 若只输出观测量而非全部场数组，Schrödingerization 的端到端资源优势在什么条件下成立？


## 核对依据与边界（2026-10-15）

对照[作者提供的期刊全文](https://ins.sjtu.edu.cn/people/shijin/PS/PhysRevLett-JinLiuYu.pdf)中 warped phase transformation、整轴初值延拓与 Fourier 提升公式（式 2–8）。本页统一到 $\dot u=-Au$ 的符号约定；标量检验为补充推导。
