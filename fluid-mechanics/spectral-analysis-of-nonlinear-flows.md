# 非线性流动的谱分析

**作者：** CLARENCE W. ROWLEY, IGOR MEZIĆ, SHERVIN BAGHERI, PHILIPP SCHLATTER, DAN S. HENNINGSON

**DOI：** [10.1017/S0022112009992059](https://doi.org/10.1017/S0022112009992059)

**源 PDF：** `spectral-analysis-of-nonlinear-flows.pdf`

**阅读状态：** 🔬 精读
**流程状态：** ①元数据 ✓ | ②初稿 ✓ | ③评估 ✓(精读) | ④补充 ✓ | ⑤索引 ✓ | ⑥review ✓ | ⑦提交 ⏳

---

## 摘要

### 中文翻译

Rowley 等（2009）将 Koopman 算子谱理论引入流体分析，把非线性流动的相干结构问题转化为线性谱问题，并统一了 DMD 与 Koopman mode decomposition 的关系。喷流、腔流等经典例子奠定了 DMD/Koopman 流体分析范式，是降阶建模与流场诊断的基础文献。

## 价值评估

**Doctor 指定精读。** 按 6 级标准，这篇应按 **5/6：高优先级精读** 处理：idea 清晰，把非线性流场的相干结构问题转化为 Koopman 算子的线性谱问题；计算结果经典，喷流、腔流等例子奠定了 DMD/Koopman 流体分析范式；预言能力中等，谱分解本身适合诊断和短中期建模，但对强湍流连续谱和噪声敏感；方法新颖性高，是 DMD 与 Koopman mode decomposition 关系的标志性论文；来源为 JFM 2009，引用影响大。精读判断：它是 Doctor 的 AI4Physics、降阶模型、神经算子、流场诊断和稳定性分析的共同基础。

## 公式与代码梳理

#### 数学结构与核心公式

论文的核心对象不是直接作用在状态空间上的非线性流映射，而是作用在 observable 上的 Koopman 算子。设非线性动力系统为

$$
\dot x=F(x),\qquad x\in M,
$$

流映射为

$$
x(t)=T^t(x_0).
$$

对任意标量 observable $g:M\to\mathbb C$，Koopman 算子定义为

$$
U^t g=g\circ T^t .
$$

虽然 $T^t$ 对 $x$ 是非线性的，但 $U^t$ 对函数 $g$ 是线性的：

$$
U^t(\alpha g_1+\beta g_2)=\alpha U^t g_1+\beta U^t g_2 .
$$

Koopman eigenfunction $\varphi_j$ 满足

$$
U^t\varphi_j=e^{\lambda_j t}\varphi_j .
$$

若向量值 observable 是流场本身或测量量

$$
\mathbf g(x)=\mathbf u(\cdot;x),
$$

并且可在 Koopman eigenfunction 上展开，则有

$$
\mathbf g(x)=\sum_j\varphi_j(x)\mathbf v_j .
$$

沿轨道演化得到 Koopman mode decomposition：

$$
\mathbf g(T^t x_0)=\sum_j e^{\lambda_j t}\varphi_j(x_0)\mathbf v_j .
$$

这里 $\lambda_j=\sigma_j+i\omega_j$，$\sigma_j$ 是增长/衰减率，$\omega_j$ 是频率，$\mathbf v_j$ 是空间 Koopman mode。对流体而言，$\mathbf v_j$ 是具有单一时间频率的空间结构，这正是 DMD 输出在谱结构上比 POD 更易解释的原因（噪声、非正态瞬态与有限采样窗口仍会使其难解释）。

DMD 是 Koopman 谱的有限维数据近似。给定快照

$$
X=[x_1,x_2,\ldots,x_{m-1}],\qquad
Y=[x_2,x_3,\ldots,x_m],
$$

假设存在低秩线性映射

$$
Y\approx AX .
$$

最小二乘意义下

$$
A=YX^{+}.
$$

实际代码不显式构造大矩阵 $A$，而是对 $X$ 做截断 SVD：

$$
X=U_r\Sigma_r V_r^* .
$$

低维投影算子为

$$
\tilde A=U_r^*YV_r\Sigma_r^{-1}.
$$

求解

$$
\tilde A w_j=\mu_j w_j,
$$

DMD mode 为

$$
\Phi_j=YV_r\Sigma_r^{-1}w_j,
$$

连续时间特征值为

$$
\lambda_j=\frac{\log\mu_j}{\Delta t}.
$$

最终重构为

$$
x_k\approx\sum_j b_j\Phi_j\mu_j^{k-1},
$$

其中 $b_j$ 由初始快照投影得到。

与 POD 的区别可由优化目标说明。POD 寻找能量最优正交基：

$$
\min_{\{\phi_j\}_{j=1}^r}\sum_k\left\|x_k-\sum_{j=1}^r\langle x_k,\phi_j\rangle\phi_j\right\|^2 .
$$

DMD/Koopman 寻找具有单一指数时间因子的非正交模态。POD mode 能量最优但时间动力学混合；Koopman mode 不一定正交，却把频率、增长率和空间结构绑定起来。

#### 关键推导

第一步是从 Koopman eigenfunction 推出模态分解。若

$$
\mathbf g(x)=\sum_j\varphi_j(x)\mathbf v_j,
$$

则

$$
\mathbf g(T^t x)
=\sum_j\varphi_j(T^t x)\mathbf v_j
=\sum_j (U^t\varphi_j)(x)\mathbf v_j
=\sum_j e^{\lambda_jt}\varphi_j(x)\mathbf v_j .
$$

所以非线性系统的观测量演化被表示为线性指数谱叠加。非线性隐藏在 eigenfunction $\varphi_j(x)$ 中，时间依赖变成线性的 $e^{\lambda_jt}$。

第二步是 DMD 作为有限维 Koopman 近似。快照序列满足

$$
x_{k+1}\approx Ax_k .
$$

若 $X=U_r\Sigma_rV_r^*$，则在 POD 子空间中

$$
\tilde A=U_r^*AU_r\approx U_r^*YV_r\Sigma_r^{-1}.
$$

对 $\tilde A$ 做特征分解后，$A$ 的近似特征向量可 lifted 为

$$
\Phi_j=YV_r\Sigma_r^{-1}w_j .
$$

这一步避免构造维度等于网格自由度的大矩阵，计算成本主要由 SVD 和小矩阵特征分解决定。

第三步是周期流的谱解释。若极限环用相位 $\theta$ 参数化，且

$$
\dot\theta=\omega,
$$

则 eigenfunction 可取

$$
\varphi_n(\theta)=e^{in\theta},
$$

对应

$$
U^t\varphi_n=e^{in\omega t}\varphi_n .
$$

因此 Koopman spectrum 是基频及其谐波。DMD 在周期涡脱落中得到的模态，本质上就是这些 Fourier-Koopman 模态。

#### 对 HPC 框架的启示

对 Doctor 的 HPC 框架，Koopman/DMD 最适合作为“诊断层”和“降阶建模层”，而不是替代核心 PDE solver。框架应支持高吞吐快照输出、在线统计、随机化 SVD、分布式 Gram 矩阵和流式 DMD。对大规模 CFD，快照矩阵 $X$ 不应集中到单节点；应计算

$$
C=X^*X,\qquad G=X^*Y
$$

或使用 randomized range finder，把通信量控制在 snapshot 数量维度。

与 `JFNK` 的关系是：DMD 可作为 Krylov 子空间和线性化动力学的外部诊断，用于估计主导增长率、选择预条件器目标频段，或构造 Newton 初值。与 `Fourier Neural Operator`、`PDE Transformer` 的关系是：Koopman 提供了“可解释 latent dynamics”的线性谱目标，神经算子可学习 observable/dictionary，使非线性系统在 latent space 中更接近线性演化。

与几何力学主线的结合点在 measure-preserving Koopman。不可压 Euler 的理想演化具有体积保持和 Hamiltonian 结构；若数据来自结构保持求解器，Koopman 近似也应避免产生虚假的耗散谱。可以考虑 unitary/measure-preserving DMD、symplectic DMD 或 physics-informed DMD，把能量、Casimir、divergence-free 约束作为矩阵流形约束。

#### 待深入研究

1. 对强湍流，Koopman 谱含连续谱；有限 rank DMD 给出的离散特征值哪些是物理模态，哪些是 spectral pollution？
2. 如何在 AMR 和非均匀网格上定义快照内积，使 DMD mode 的能量和正交性不被网格体积权重扭曲？
3. 能否把 DMD/Koopman 模态作为神经算子的 spectral regularizer，让 learned latent evolution 同时具备预测能力和可解释频率结构？

## Review Questions

1. 对不可压 Euler 或 Navier-Stokes，Koopman observable 应选速度、涡量、压力、Clebsch 变量还是能量/Casimir 诊断量，才能最稳定地捕捉几何结构？
2. 在大规模 GPU/AMR 数据上，如何设计 streaming DMD，使 I/O、通信和 SVD 成本不压倒流体求解本身？
3. 若把 Koopman 模态用于 AI4Physics 预测，如何避免模型只学习短期频率拟合，却破坏长期守恒律和稳定性？

4. 对连续谱或强非正态放大的流动，Koopman/DMD 分析应如何区分真实动力学结构与有限窗口、有限秩带来的谱污染？
5. 若数据来自 AMR、非均匀网格或加权有限元离散，DMD 的内积和正交化步骤该怎样修改，才能让模态幅值具有物理意义？
6. 在 AI4Physics 中，把 Koopman 线性化当作 latent prior 时，怎样避免模型只学到短时频率拟合而丢掉长期守恒和稳定性？

---

---
