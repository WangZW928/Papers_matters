# 单相与多相轴对称粘弹性流的对数构象格式

**作者：** William Doherty

**DOI：** [10.1016/j.jcp.2024.113014](https://doi.org/10.1016/j.jcp.2024.113014)

**来源 PDF：** `The log-conformation formulation for single- and multi-phase.pdf`

**阅读状态：** 🔬 精读
**流程状态：** ①元数据 ✓ | ②初稿 ✓ | ③评估 ✓(精读) | ④补充 ✓ | ⑤索引 ✓ | ⑥review ✓ | ⑦提交 ⏳

---

## 摘要

### 中文翻译

本文在轴对称单相/多相场景下实现 log-conformation formulation：将构象张量 A 改写为矩阵对数 Ψ=log A，从变量层面保证正定性，规避高 Weissenberg 数下直接离散 A 失去正定导致的数值失稳（HWNP）。

## 价值评估

**Doctor 指定精读。** 按 6 级标准，这篇应按 **4/6 到 5/6：方向相关的高价值精读** 处理：idea 清晰，把构象张量 $A$ 改写为矩阵对数 $\Psi=\log A$，从变量层面保证正定性；计算结果面向单相/多相轴对称粘弹性流，工程实用性强；预言能力取决于本构模型，数值格式本身主要提升高 Weissenberg 数稳定性；方法新颖性来自轴对称和多相扩展，而 log-conformation 基础来自 Fattal-Kupferman；来源为 JCP 2024，适合严肃数值实现参考。精读判断：它补上 Doctor 研究画像中“粘弹性流 + 隐式求解 + HPC 框架”的关键分支。

## 公式与代码梳理

#### 数学结构与核心公式

粘弹性流的困难来自 polymer conformation tensor $A$ 的演化。以 Oldroyd-B 类模型为例，不可压条件为

$$
\nabla\cdot u=0 .
$$

动量方程可写为

$$
\rho(\partial_tu+u\cdot\nabla u)
=-\nabla p+\eta_s\Delta u+\nabla\cdot\tau_p+f .
$$

聚合物应力常写作

$$
\tau_p=\frac{\eta_p}{\lambda}(A-I),
$$

其中 $\eta_s$ 是溶剂黏度，$\eta_p$ 是聚合物黏度，$\lambda$ 是松弛时间。构象张量满足上随体导数方程：

$$
\overset{\triangledown}{A}
\equiv \partial_tA+u\cdot\nabla A-(\nabla u)A-A(\nabla u)^T
=-\frac1{\lambda}f_R(A).
$$

Oldroyd-B 中 $f_R(A)=A-I$。FENE-P 中常用

$$
f_R(A)=\frac{A}{1-\operatorname{tr}(A)/L^2}-I ,\qquad \operatorname{tr}(A)<L^2 .
$$

高 Weissenberg 数问题的核心是：直接离散 $A$ 时，即使连续解保持 $A$ 对称正定，数值误差也可能产生非正定特征值，导致应力爆炸或矩阵函数失效。log-conformation 令

$$
\Psi=\log A,\qquad A=e^\Psi .
$$

若 $\Psi$ 对称，则 $e^\Psi$ 自动正定。因此代码中演化 $\Psi$，应力计算时再指数映射回 $A$。

Fattal-Kupferman 的关键是把速度梯度分解成与 $A$ 相容的部分。设

$$
\nabla u=\Omega+B+NA^{-1},
$$

其中 $\Omega^T=-\Omega$ 是反对称旋转部分，$B$ 与 $A$ 对易（$BA=AB$，对应 $A$ 的特征方向上的拉伸），$N^T=-N$ 且 $NA^{-1}$ 是 $A$ 的反对称-对称混合修正项（保证分解在正定矩阵的切空间上唯一，$N$ 满足 $\operatorname{tr}(NA^{-1})=0$）。在这个分解下，log-conformation 方程写为

$$
\partial_t\Psi+u\cdot\nabla\Psi-(\Omega\Psi-\Psi\Omega)-2B
=-\frac1{\lambda}e^{-\Psi}f_R(e^\Psi).
$$

这个公式是实现核心。左侧把旋转、伸长和对流分离；右侧是松弛项。因为 $B$ 与 $A=e^\Psi$ 对易，伸长项能以 $2B$ 的形式进入 $\Psi$ 方程，避免直接对矩阵指数求 Frechet 导数。

轴对称情形采用柱坐标 $(r,z,\theta)$，速度为

$$
u=(u_r,u_z),\qquad u_\theta=0
$$

或在无旋流假设下忽略环向速度。不可压条件变为

$$
\frac1r\partial_r(ru_r)+\partial_z u_z=0 .
$$

构象张量即使无旋流，也包含环向分量：

$$
A=
\begin{pmatrix}
A_{rr} & A_{rz} & 0\\
A_{rz} & A_{zz} & 0\\
0 & 0 & A_{\theta\theta}
\end{pmatrix}.
$$

速度梯度含有几何项

$$
\nabla u=
\begin{pmatrix}
\partial_ru_r & \partial_zu_r & 0\\
\partial_ru_z & \partial_zu_z & 0\\
0 & 0 & u_r/r
\end{pmatrix}.
$$

因此 $A_{\theta\theta}$ 或 $\Psi_{\theta\theta}$ 的方程中会出现 $u_r/r$ 引起的环向伸长。多相扩展通常通过 indicator/level-set/VOF 区分相区，使 $\rho$、$\eta_s$、$\eta_p$、$\lambda$ 成为空间变系数，并在界面处处理表面张力：

$$
f_\sigma=\sigma\kappa\delta_\Gamma n .
$$

应力散度在轴对称坐标下也有额外项，例如径向分量含

$$
(\nabla\cdot\tau)_r
=\frac1r\partial_r(r\tau_{rr})+\partial_z\tau_{rz}-\frac{\tau_{\theta\theta}}{r}.
$$

轴向分量为

$$
(\nabla\cdot\tau)_z
=\frac1r\partial_r(r\tau_{rz})+\partial_z\tau_{zz}.
$$

这些 $1/r$ 项是轴对称实现中最容易出错的地方。

#### 关键推导

第一步是正定性。若 $\Psi=\Psi^T$，谱分解为

$$
\Psi=Q\Lambda Q^T .
$$

则

$$
A=e^\Psi=Qe^\Lambda Q^T .
$$

因为 $e^{\lambda_i}>0$，所以对任意非零 $x$，

$$
x^TAx=(Q^Tx)^Te^\Lambda(Q^Tx)>0 .
$$

因此无论时间推进中 $\Psi$ 的特征值多大，只要保持对称，$A$ 都正定。这是 log-conformation 缓解 HWNP 的数学核心。

第二步是把上随体导数转为 log 方程。直接从 $A=e^\Psi$ 求导会遇到非交换矩阵导数。Fattal-Kupferman 的办法是在 $A$ 的特征基中分解 $\nabla u$，把与 $A$ 对易的伸长部分单独提取。若 $B$ 与 $A$ 对易，则

$$
BA+AB=2BA
$$

对应到 log 变量就是 $2B$。旋转项由 commutator 表示：

$$
\Omega A-A\Omega
$$

在 log 变量中变成

$$
\Omega\Psi-\Psi\Omega .
$$

于是得到

$$
D_t\Psi=\Omega\Psi-\Psi\Omega+2B-\frac1{\lambda}e^{-\Psi}f_R(e^\Psi),
$$

其中 $D_t=\partial_t+u\cdot\nabla$。

第三步是轴对称环向项。即使二维 $(r,z)$ 网格上只存 $u_r,u_z$，材料线在 $\theta$ 方向的伸长率仍为

$$
\partial_\theta u_\theta/r+u_r/r=u_r/r .
$$

所以构象张量不能简化成 $2\times2$，必须保留 $A_{\theta\theta}$ 或 $\Psi_{\theta\theta}$。否则拉伸应力和径向动量中的 $-\tau_{\theta\theta}/r$ 会缺失，液滴颈缩、喷丝和气泡轴向拉伸会失真。

#### 对 HPC 框架的启示

对 Doctor 的 HPC 框架，这篇的工程启示是：复杂本构模型应以“变量变换 + 局部矩阵函数 + 隐式/显式分裂”的方式模块化。每个网格点需要 $3\times3$ 对称矩阵的 `log`、`exp`、特征分解或封闭公式；这是局部 dense algebra，非常适合 GPU，但要避免分支过多和小矩阵库开销过大。

动量方程和 log-conformation 方程形成强耦合。高 Wi 下松弛项和应力散度可能刚性，应考虑 IMEX、BDF2 或 Newton-Krylov。这里可直接关联 `JFNK`：残差包含速度、压力、$\Psi$，Jacobian-free matvec 可通过残差差分实现；预条件器则按 Stokes block、pressure Schur complement、local conformation block 分裂。

与 AMR 的结合点在界面和轴线。多相轴对称有 $1/r$ 奇异项，靠近 $r=0$ 要用奇偶对称或有限体积积分形式，而不是直接点值除以 $r$。AMR coarse-fine 插值必须保持 $\Psi$ 对称；若插值 $A$，需再投影到 SPD cone。更稳的做法是在 $\Psi$ 空间插值，然后指数映射。

与 AI4Physics 的关系是：神经网络若预测粘弹性应力，最好预测 $\Psi$ 或 Cholesky/log-Cholesky 变量，而不是直接预测 $A$ 或 $\tau_p$。这可以把正定性作为硬约束，减少 PINN/Neural Operator 在高 Wi 数据上的非物理解。

#### 待深入研究

1. 对强多相界面，$\lambda$、$\eta_p$ 不连续时，$\Psi$ 的界面 jump condition 应如何离散，才能同时保持 SPD 和应力平衡？
2. 小矩阵 $\log/\exp$ 在 GPU 上用特征分解、Padé 近似还是解析 $2\times2+1$ 轴对称结构更划算？
3. JFNK 处理 log-conformation 全耦合时，怎样构造物理块预条件器，避免高 Wi 下 Krylov 迭代数随 $\lambda$ 爆炸？

## Review Questions

1. log-conformation 保证 $A$ 正定，但是否保证离散应力功与能量耗散关系正确？如果不保证，应额外离散哪些能量项？
2. 轴对称 $u_r/r$ 和 $-\tau_{\theta\theta}/r$ 项在有限体积、有限元和 AMR 中分别应如何处理轴线极限？
3. 若用神经算子加速粘弹性流，预测 $\Psi$、$\tau_p$、还是 closure correction 最合理？如何把 SPD、frame indifference 和 objectivity 作为硬约束？

4. 在轴对称多相场景中，`log/exp` 变量变换解决了 SPD 问题，但是否同时保留了正确的离散自由能或应力功关系？
5. 若采用 JFNK 全耦合求解，`u-p-\Psi` 三块之间最难预条件的耦合是压力 Schur 补、应力散度，还是局部矩阵函数线性化？
6. 对 AI4Physics 而言，仅预测 `\Psi` 是否足够，还是还需要把 frame indifference、界面 jump 条件和 `u_r/r` 轴线结构显式编码进网络？

---

---
