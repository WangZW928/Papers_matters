# Covector Fluids

**作者：** Mohammad Sina Nabizadeh, Stephanie Wang, Ravi Ramamoorthi, Albert Chern

**DOI：** [10.1145/3528223.3530120](https://doi.org/10.1145/3528223.3530120)

**Source PDF：** `CovectorFluids.pdf`

**阅读状态：** 🔬 精读（重读）

**流程状态：** ①元数据 ✓ | ②初稿 ✓ | ③评估 ✓(精读) | ④补充 ✓ | ⑤索引 ✓ | ⑥review ✓ | ⑦提交 ✓

---

## 摘要

本文针对低黏性、涡结构主导的不可压流体动画，提出 Covector Fluids（CF）。方法把速度视为一形式/余向量，并以 inverse flow map 的协变 pullback 替代逐分量半拉格朗日平流：

\[
\mathbf u^{*}(\mathbf x)=\bigl(d\Psi(\mathbf x)\bigr)^T\mathbf u^n(\Psi(\mathbf x)).
\]

这样在连续层面遵循 Kelvin 环量定理，隐式得到正确的涡量输运；数值实现仍采用 MAC 网格、压力投影、RK4 回溯、插值和 BFECC/MCM。论文在涡环、涡结、烟雾和障碍物尾迹等实验中显示出比传统方法更低的涡量衰减和更好的动能保持。

## 文章总结

### 1. 解决什么问题？

传统 advection-projection 将速度分量当作标量搬运，会把旋转分量的一部分转化为散度分量，随后被 pressure projection 删除，造成涡量损失。CF 在速度层面加入 inverse flow map 的 transpose Jacobian，避免显式执行“涡量 → 速度”的全局重建。

### 2. 用了什么方法论？

连续理论使用速度一形式、pullback、Lie derivative 和外微分；工程实现则是在规则 MAC staggered grid 上，对现有 semi-Lagrangian advection 做局部 Jacobian 转置乘法，并与二阶 midpoint、BFECC 以及 BiMocq/MCM 结合。

### 3. 主要结论是什么？

在论文测试的规则 MAC 网格、时间步和 BFECC/MCM 配置下，CF/CF+MCM 比 SF、MC、SCPF、MC+R 和 BiMocq 更能保持涡结构，并通常改善动能曲线。论文并未证明任意网格上的严格离散 Kelvin、能量或涡量守恒。

## 价值评估

Doctor 指定精读。该文是把 Euler–Poincare/Lie advection 的几何语言落到常规图形学 advection-projection solver 的代表性工作，连接 Hamiltonian ideal fluid、Clebsch Maps、vortex methods 与工程实现。它对结构保持流体变量设计很有价值，但不是完整的 Navier–Stokes、AMR、曲线网格或严格离散微分几何方案。

## 重读精读（2026-08-24）

### 1. 核心问题与方法边界

不可压 Euler 方程为

\[
\frac{\partial\mathbf u}{\partial t}+\mathbf u\cdot\nabla\mathbf u=-\nabla p,\qquad \nabla\cdot\mathbf u=0.
\]

传统方法先逐分量平流，再投影。CF 将欧氏速度看作速度余向量 \(\eta=\mathbf u^\flat\)，用 covector pullback 代替逐分量平流；其核心是连续层面的 Lie advection，而非一个新的压力求解器。

必须区分三个概念：

1. Kelvin circulation 是随流闭合曲线上的环量守恒；
2. 二维涡量标量随粒子输运，三维还包含 vortex stretching，不能说每一点涡量幅值恒定；
3. 连续无粘 Euler 在合适边界下守恒动能，但论文数值实验中的 “preservation” 只是相对于其他方法的衰减更小，不是机器精度意义下的严格离散守恒。

论文实际使用规则笛卡尔 MAC 网格、RK4 回溯、插值、有限差分 Jacobian、pressure projection、BFECC limiter 和经验 CFL。它没有证明任意网格、严格离散 Kelvin 定理、严格离散能量守恒，也没有解决黏性边界层、完整固液耦合或高雷诺数工程预测。

### 2. 数学结构：Euler 到 covector Lie advection

利用

\[
(\nabla\mathbf u)^T\mathbf u=\nabla\left(\frac12|\mathbf u|^2\right),
\]

令 \(\eta=\mathbf u^\flat\)、\(\lambda=p-\frac12|\mathbf u|^2\)，Euler 方程可写成

\[
\frac{\partial\eta}{\partial t}+\mathcal L_{\mathbf u}\eta=-d\lambda,
\qquad \mathbf u=\eta^\sharp.
\]

设 forward flow map \(\Phi_t\) 满足 \(\partial_t\Phi_t=\mathbf v\circ\Phi_t\)，inverse map 为 \(\Psi_t=\Phi_t^{-1}\)。标量只需复合 \(q_t=q_0\circ\Psi_t\)，而一形式必须按 pullback 变换：

\[
\eta_t=\Psi_t^*\eta_0,
\qquad
\eta_t(\mathbf x)=\bigl(d\Psi_t(\mathbf x)\bigr)^T\eta_0(\Psi_t(\mathbf x)).
\]

对任意切向量 \(\mathbf a\)，pullback 满足

\[
(\Psi^*\eta)_\mathbf x[\mathbf a]=\eta_{\Psi(\mathbf x)}[d\Psi(\mathbf x)\mathbf a].
\]

因此对任意物质曲线 \(C_t=\Phi_t(C_0)\)，有

\[
\int_{C_t}\eta_t=\int_{C_t}\Psi_t^*\eta_0=\int_{C_0}\eta_0.
\]

闭合曲线即得到 Kelvin 环量性质。压力项是 exact one-form，\(\oint d\lambda=0\)，所以完整 Euler 的压力不会改变闭合环量。pressure projection 的作用是从相差 exact differential 的等价类中选出无散代表；连续层面 pullback 与外微分满足 \(\Psi^*d=d\Psi^*\)，但离散插值、边界和有限容差并不自动保留该交换关系。

### 3. 涡量方程等价性

定义涡量二形式 \(\omega=d\eta\)。对 covector transport 取外微分并使用 \(d\mathcal L_\mathbf v=\mathcal L_\mathbf v d\)：

\[
\frac{\partial\omega}{\partial t}+\mathcal L_\mathbf v\omega=0.
\]

等价地，\(\eta_t=\Psi_t^*\eta_0\) 给出 \(\omega_t=d\eta_t=\Psi_t^*\omega_0\)。三维中 \(\omega=\iota_\boldsymbol\zeta\mu\)，不可压时 \(\mathcal L_\mathbf v\mu=0\)，于是

\[
\frac{\partial\boldsymbol\zeta}{\partial t}+\mathbf v\cdot\nabla\boldsymbol\zeta-\boldsymbol\zeta\cdot\nabla\mathbf v=0.
\]

最后一项就是 vortex stretching/tilting；三维中保持的是涡量二形式的输运/涡管通量结构，不是点值涡量幅值。二维中 \(\omega=\zeta\,dx\wedge dy\)，不可压条件消去 stretching，涡量标量满足 \(\partial_t\zeta+\mathbf v\cdot\nabla\zeta=0\)。

相比之下，传统逐分量平流会产生论文推导的非物理附加项

\[
\frac{\partial\boldsymbol\zeta}{\partial t}+\mathbf v\cdot\nabla\boldsymbol\zeta-\boldsymbol\zeta\cdot\nabla\mathbf v=\langle\nabla\mathbf u\times\nabla\mathbf v\rangle.
\]

这解释了 CF 的连续理论优势，但不证明其 MAC 离散满足 \(d_hP_{\Psi,h}=P_{\Psi,h}d_h\)。

### 4. 算法流程

标准 advection-projection 是：冻结输运速度 \(\mathbf v\)，回溯得到 \(\Psi\)，做 \(\mathbf u^*=\mathbf u^n\circ\Psi\)，再解 Poisson 并投影。

一阶 CF 将第三步替换为

\[
\mathbf u^*=(d\Psi)^T(\mathbf u^n\circ\Psi),
\]

然后仍做 pressure projection。二阶 CF 用 midpoint 先估计半步速度，再用该速度完成全步 covector advection 和 projection。

Algorithm 3 的 covector semi-Lagrangian advection 对每个位置：用 RK4 回溯、在 departure point 插值旧速度、由邻近 map 样本差分得到 \(d\Psi\)，最后执行 transpose-Jacobian 乘法。它比普通 semi-Lagrangian 多出的核心数据是 inverse map 的空间 Jacobian。

BFECC 对 covector advection 做正向、反向、误差估计和半误差修正；正向、反向和修正都必须使用 covector pullback，且论文用 extrema limiter 抑制振荡。limiter 也意味着该算法不是严格线性的精确 pullback。

CF+MCM/BiMocq 保存较长时间的 forward/inverse map，减少每步速度插值。传统 MCM 需要记录沿轨迹累积的压力贡献；CF+MCM 利用 exact differential 在最终 projection 中吸收压力历史，因此不需显式维护该历史压力梯度。论文实验中 mapping 每 5 步重置；3D BiMocq 使用 DMC，2D BiMocq 和 CF+MCM 使用 RK4。

### 5. 离散化与实现边界

实际实现是规则 MAC staggered grid：速度分量位于对应法向 face center，映射和相关量主要在 cell center。以一个 face 分量为例，更新需要该 face 上 Jacobian 的一行与回溯位置处的三分量速度做矩阵—向量乘法；Jacobian 由相邻 cell-center map 值有限差分得到。

误差来源包括 RK4 回溯、off-grid 插值、有限差分 Jacobian、BFECC 误差估计、limiter、离散 projection、Poisson 容差、长时间 map 变形以及边界外回溯。论文的“局部调整”是相对于显式涡量法的全局 vorticity-to-velocity 重建而言；完整时间步仍约增加 15% 成本，且需要额外 map、Jacobian 和误差修正存储。

边界处理主要是 no-through 法向条件、自由表面压力 Dirichlet 和 projection 中的移动障碍物条件，不是完整解析 no-slip 边界层模型。论文指出 CF 条件稳定，需要经验 CFL；临界 CFL 约 6.18，高于 SCPF 的 4.85 和 IVOCK 的 1.45，但没有解析稳定性判据。Jacobian 对流动变形敏感，是主要不稳定来源。

### 6. 实验与结论

论文比较 SF、SF+R、SCPF、MC、MC+R、BiMocq、CF 和 CF+MCM。实验包括 covector 刚体旋转、涡环 leapfrogging、Taylor vortices、trefoil vortex knot、墨水/烟雾/浮力 plume、von Kármán vortex street、移动 bunny、delta wing 和 bunny meteor。

结果支持的结论是：在论文的规则 MAC 网格、时间步、BFECC/MCM 配置和测试问题上，CF/CF+MCM 的涡结构衰减更慢、涡环寿命更长，动能曲线通常优于低阶耗散方法。Taylor vortices 中，较好的动能表现依赖 BFECC，不能归因于 covector 表示自动产生严格能量守恒。von Kármán 实验中的 MC+R 是数值 ground truth，不是解析解或实验测量。

论文不支持“任意网格精确模拟”“严格离散能量守恒”“所有时间步精确 Kelvin 环量守恒”或“高雷诺数真实空气动力学定量预测”。delta-wing 章节明确省略了精确空气动力学所需的边界层和固液耦合处理；实验也不是标准 homogeneous isotropic turbulence decay benchmark。

### 7. 与 AMReX/VWiS 的关联

以下是实现启发，不是论文在 AMReX、AMR 或 VWiS 上验证的结果。

1. 应区分速度向量、速度一形式和法向体积通量。欧氏笛卡尔网格上它们可借助固定 metric 共享分量，但曲线/非正交网格、EB 和 AMR 上必须显式定义 metric/Hodge 映射。
2. MAC face-centered 数据天然适合面法向速度/通量；严格 DEC 中一形式更接近沿 edge 的积分，而不可压通量更接近 \((n-1)\)-form。因此不能只把已有 face `MultiFab` 改名为 one-form；应明确 primal/dual complex，并区分 circulation one-form、face-normal flux 和 vorticity two-form。
3. 若要获得强于“经验上少耗散”的结构保证，应测试离散交换关系

\[
d_hP_{\Psi,h}\approx P_{\Psi,h}d_h.
\]

应分别记录 material-loop circulation error、离散 curl transport error、projection residual 和 coarse-fine synchronization error。
4. AMR 还需处理 map 在 refinement interface 的 ghost/prolongation、regridding 后 \(\Phi,\Psi\) 转移、one-form/flux/vorticity 的 restriction/prolongation 与 \(d_h\) 的兼容，以及 reflux 的通量守恒和 Kelvin 环量约束之间的关系。EB 或移动边界的 closest-point traceback 可能注入非物理环量。
5. `dPsi` 计算、回溯采样和矩阵—向量乘法适合 AMReX/GPU patch-local kernel，但 CF+MCM 的长期 map、参考场、重置判据和通信/内存成本必须单独评估，不能直接套用论文约 15% 的均匀网格开销。

### 8. 需要修正的旧笔记表述

- “离散化过程中自然保持涡量守恒和能量守恒”应改为：连续 covector advection 正确诱导涡量输运并满足 Kelvin 环量结构；具体离散实现只在实验中改善涡量和动能保持。
- “引入离散微分几何工具”应改为：理论使用微分形式/pullback/Lie derivative，实际算法使用规则 MAC 网格、插值、RK4 和有限差分 Jacobian，并非完整 DEC 离散复形。
- “在任意网格上实现无散度流动的精确模拟”应改为：论文只在规则笛卡尔 MAC 网格上测试，无散条件由数值 pressure projection 近似实现。
- “湍流衰减”应改为论文实际列出的 Taylor vortices、涡结、涡环、浮力烟雾和障碍物尾迹等实验；没有标准 homogeneous isotropic turbulence decay benchmark。
- “离散层面严格保持涡量和能量守恒”应删除。采样误差、BFECC limiter、经验 CFL、Jacobian 敏感性和额外成本都说明该实现不是严格守恒离散积分器。

### 9. Review Questions

1. MAC 插值、有限差分 Jacobian 和 BFECC limiter 组成的离散 pullback 能否构造为满足 \(d_hP_{\Psi,h}=P_{\Psi,h}d_h\) 的交换图，并定量拆分 splitting、sampling 与 commutation error？
2. 在 block-structured AMR 上，若 circulation one-form、face-normal flux 和 vorticity two-form 位于不同 primal/dual 网格对象，如何设计 prolongation、restriction、reflux、projection 与 map reinitialization，使 coarse-fine 通量守恒和物质闭合路径的低环量漂移兼容？
3. 能否构造一种同时控制 Jacobian 条件不稳定、降低插值耗散，并具有可证明离散能量界或 Kelvin 环量误差界的高阶时间—空间离散？

## Review 记录

Kimi Code review 已完成；公式、边界、实现成本和“严格守恒/任意网格”表述按 review 结论修订。未发现阻塞性公式或算法描述问题；Review Questions 已保留在文末。
