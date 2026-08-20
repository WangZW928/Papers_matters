# Quantum Simulation of Partial Differential Equations via Schrödingerization

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

### 数学结构与核心公式

Schrödingerization 的目标是把非 Hermitian、非幺正的线性动力学

$$
\frac{d}{dt}u(t)=-Au(t)
$$

转化为 Schrödinger 型方程

$$
i\frac{d}{dt}\psi(t)=H\psi(t),
\qquad
H=H^\dagger.
$$

对 PDE，空间离散后通常也得到上述 ODE 系统，其中 $A$ 可来自扩散、输运、边界条件或耗散算子。一般 $A$ 不是 Hermitian，不能直接作为量子 Hamiltonian。论文将 $A$ 分解为两个 Hermitian 矩阵：

$$
A=H+i\bar{H},
\qquad
H=\frac{A+A^\dagger}{2},
\qquad
\bar{H}=\frac{i(A^\dagger-A)}{2}.
$$

若 $H$ 半正定，则可用 warped phase transformation 引入辅助变量 $p$。采用下列符号约定，在 $p>0$ 区域定义

$$
v(t,p)=e^{p}u(t).
$$

因为 $\partial_p v=e^{p}u=v$，原方程

$$
\partial_t u=-(H+i\bar{H})u
$$

可转写为

$$
\partial_t v+H\partial_p v+i\bar{H}v=0.
$$

对 $p$ 做 Fourier 变换，设共轭变量为 $\eta$：

$$
\tilde{v}(t,\eta)=\int_{\mathbb{R}}e^{-i\eta p}v(t,p)\,dp.
$$

利用 $\partial_p\mapsto i\eta$，得到

$$
\partial_t\tilde{v}+i\eta H\tilde{v}+i\bar{H}\tilde{v}=0,
$$

即

$$
i\partial_t\tilde{v}
=
(\eta H+\bar{H})\tilde{v}.
$$

由于 $\eta\in\mathbb{R}$ 且 $H,\bar{H}$ 都 Hermitian，所以

$$
H_{\text{tot}}(\eta)=\eta H+\bar{H}
$$

是 Hermitian。这就是 Schrödingerization 的核心：每个 Fourier mode $\eta$ 都对应一个实时间 Schrödinger 方程。

离散辅助变量后，可写成张量积 Hamiltonian：

$$
i\frac{d}{dt}\tilde{v}
=
\left(
H\otimes D+\bar{H}\otimes I
\right)\tilde{v}
=
H_{\text{total}}\tilde{v},
$$

其中 $D$ 是 $\eta$ 或离散 Fourier multiplier 对角矩阵。量子态演化为

$$
|\tilde{v}(t)\rangle
=
e^{-iH_{\text{total}}t}
|\tilde{v}(0)\rangle.
$$

原解 $u(t)$ 的恢复不是直接读出所有分量，而是通过投影到辅助维中的正 $p$ 区域或相应权重态。量子态通常表示归一化解：

$$
|u(t)\rangle
=
\frac{1}{\|u(t)\|}
\sum_i u(t,x_i)|i\rangle.
$$

因此算法天然给出状态方向，范数 $\|u(t)\|$ 或物理观测量需额外估计。

### 关键推导

第一步是从耗散到输运。设

$$
\frac{d}{dt}u=-Hu
$$

且 $H=H^\dagger\geq 0$。按上面的约定定义 $v=e^{p}u$，则

$$
\partial_t v=e^{p}\partial_t u=-He^{p}u=-Hv.
$$

又有 $\partial_p v=v$，所以

$$
\partial_t v+H\partial_p v=0.
$$

这说明原来的耗散衰减被编码为辅助维 $p$ 上的平移。若采用 $e^{-p}$ 或相反的 Fourier 相位，运输号和 Fourier 标签必须同时反号；不能只改其中一个。

第二步是 Fourier 化后获得 Hermitian generator。对 $p$ 变换后，$\partial_p$ 变成 $i\eta$，于是

$$
\partial_t\tilde{v}+i\eta H\tilde{v}=0
$$

等价于

$$
i\partial_t\tilde{v}=\eta H\tilde{v}.
$$

若 $H$ Hermitian，则 $\eta H$ Hermitian，演化幺正。

第三步是推广到一般非 Hermitian $A$。分解 $A=H+i\bar{H}$ 后，耗散部分 $H$ 通过 warped phase 进入 $\eta H$，反 Hermitian 部分本来就是 Schrödinger 型，进入 $\bar{H}$。合并得到

$$
i\partial_t\tilde{v}=(\eta H+\bar{H})\tilde{v}.
$$

这避免了 imaginary time evolution 只适合热方程的限制。

### 对 HPC 框架的启示

对 Doctor 的 HPC 框架，这篇论文最有价值的不是“马上量子加速 PDE”，而是提供了一种 operator lifting 思想。许多经典 PDE 半离散后是非正规、非 Hermitian、带耗散的矩阵系统：

$$
\dot{u}=Lu.
$$

Schrödingerization 说明可以通过增加一维，把耗散写成更高维 conservative / Hamiltonian-like 演化。这与仓库里的 Quantum closure、Hamiltonian ideal fluid、JFNK 和 matrix-free solver 都有连接。

在经典 HPC 上，这种提升也可能有算法启发。例如对 ill-posed backward heat、非 Hermitian 边界吸收层、open quantum system，可把不稳定的非幺正传播改写成更高维 skew-Hermitian 系统，再用能量稳定时间推进。虽然维度增加，但结构更好，可能适合 Krylov exponential、split-step Fourier 或 GPU batched Hamiltonian simulation。

代码实现上，核心接口类似：

$$
A \mapsto (H,\bar{H}) \mapsto H_{\text{total}}=H\otimes D+\bar{H}\otimes I.
$$

这正是 matrix-free operator construction。无需显式形成 Kronecker 矩阵，只需实现

$$
y=(H\otimes D)x+(\bar{H}\otimes I)x.
$$

对 GPU，$D$ 是辅助 Fourier 维上的逐模态乘法，$H,\bar{H}$ 是空间算子；可以按 $\eta$ mode batch 调用已有 PDE stencil 或 sparse/matrix-free kernel。

### 待深入研究

1. Schrödingerization 的测量瓶颈如何影响 PDE 场量重构？如果只需要 observables、低阶矩或局部统计量，优势是否更现实？
2. 对非线性 PDE，Carleman linearization 加 Schrödingerization 的维度爆炸如何控制？是否可结合稀疏截断或 Neural Operator closure？
3. 在经典 HPC 中，高一维 Hamiltonian lifting 能否用于构造稳定预条件器或 time-reversible solver？

## Review Questions

1. Schrödingerization 给出的是归一化量子态 $|u(t)\rangle$，而 CFD/HPC 通常需要全场数组；哪些 PDE 任务真正适合这种输出模型？
2. 对 GPE、open quantum system 或含吸收边界的 Schrödinger 方程，本文的非 Hermitian 到 Hermitian lifting 能否提供比 PML 更结构化的边界处理？
3. 若把 $H_{\text{total}}=H\otimes D+\bar{H}\otimes I$ 作为 matrix-free 算子，在 GPU 上它的 Roofline 瓶颈更像 stencil、FFT，还是 batched sparse matvec？

---
