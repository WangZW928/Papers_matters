# Covector Fluids

_速度一形式如何改变平流—投影分裂，以及这种连续结构在 MAC 网格上保留到什么程度。2026-11-19 重读整理。_

- 作者：Mohammad Sina Nabizadeh、Stephanie Wang、Ravi Ramamoorthi、Albert Chern。
- 发表：ACM Transactions on Graphics 41(4)，Article 113，2022 年 7 月；DOI：[10.1145/3528223.3530120](https://doi.org/10.1145/3528223.3530120)。
- 原文：[作者托管 PDF](https://cseweb.ucsd.edu/~viscomp/projects/SIG22CovectorFluids/paper/CovectorFluids.pdf)；[项目页](https://cseweb.ucsd.edu/~viscomp/projects/SIG22CovectorFluids/)。本次取得 16 页，PDF 第 1–16 页对应印刷页 113:1–113:16，下文页码均指 PDF 页码。项目页 BibTeX 写作 113:1–113:15，与实得 PDF 及其首页引用中的 16 页不一致；本笔记以实际字节版本为准。
- 原件 SHA256：`e5d82df5b81da7f5edac5fa751dabd35edb67cad0ca10a55ef04ec6a9a2fcfd8`。本地保留[原文快照](<../.paper-runs/20261119-covector-fluids/source.pdf>)；作者托管链接可能更新，DOI 本身不锁定该 PDF 的字节版本。
- 阅读范围：主文 §1–7、Appendix A.1–A.3，参考文献用于定位关联工作，未逐篇核读其原件。未审计补充代码、未观看配套视频，未复现流体实验或性能测试。
- 阅读优先级沿用 **Tier 2**。本次由用户明确要求精读，独立六级价值筛选记为 `skipped`，不另造 1–6 级分数。
- 本次运行：`20261119-covector-fluids`。各阶段状态、审阅覆盖哈希及意见处理以[运行记录](<../reading/records/20261119-covector-fluids/run.json>)和[意见处理记录](<../reading/records/20261119-covector-fluids/resolution.json>)为准；历史 2026-08-24 重读与 Kimi review 不替代本次核证。

---

## 从速度分量的平流，转向沿曲线的环量

这篇论文最值得保留的不是“多乘一个矩阵”这句实现概括，而是它改变了平流子步所服从的运动规律。传统方法把速度的每个分量当作标量搬运；Covector Fluids（CF）则把速度看成能沿曲线积分的一形式，让平流随曲线的形变一起变换。这样，涡量输运的结构已经包含在速度更新中，不必先演化涡量，再做一次全局的涡量—速度重建。[原文 §1、§4.2–4.4，pp.1–2、7；式 (3)、(26)–(31)。][^1]

传统 advection–projection 先冻结输运速度，再逐分量平流，最后用压力投影恢复无散度。问题并非“投影凭空删掉了 curl”：连续梯度的 curl 为零。问题在于，冻结速度下的逐分量平流没有按正确的涡量方程推进流场；之后的投影也补不回这一步损失的旋转结构。原文 Fig.3 给出直观说明，§4.4 与 Appendix A.3 则写出对应的非物理附加项。[pp.2、7、16。][^1]

CF 的选择是改平流，不另加涡量恢复力，也不重新安排 reflection 步来补偿这种分裂。它仍然需要压力投影，仍然存在回溯与插值误差。连续模型对环量的处理更合适，不等于整个离散求解器已经严格守恒。[§4.3–4.5、§5，pp.7–10。][^1]

## 把 Euler 方程改写成一形式方程

### 符号与适用范围

论文考虑欧氏域 \(M\subset\mathbb R^n\)，\(n=2,3\)，基本模型是不可压、无黏 Euler 方程。\(\mathbf u\) 是待求的物理速度，\(\mathbf v\) 是平流子步使用的输运速度；一阶方法取步初 \(\mathbf u\)，二阶方法估计半步速度。进入子步后，两者应分开看待。下述连续 pullback 论证假定流足够光滑、流映射可逆；离散触边截断未必满足这些条件。[§3、§4.1–4.3、Algorithm 1–2，pp.4–9。][^1]

| 符号 | 在本笔记中的含义 |
| --- | --- |
| \(\eta=\mathbf u^\flat\) | 速度一形式；\(\flat\) 用欧氏度量把向量转成协向量，\(\sharp\) 为逆变换 |
| \(p\)、\(\lambda\) | 运动学压力与 Lagrangian pressure，\(\lambda=p-\lvert\mathbf u\rvert^2/2\) |
| \(\Phi_t\)、\(\Psi_t=\Phi_t^{-1}\) | 正向流映射与逆映射，分别从参考位置到当前位置、从当前位置到参考位置 |
| \(d\)、\(\mathcal L_{\mathbf v}\) | 外微分与沿 \(\mathbf v\) 的 Lie derivative |
| \(\Omega=d\eta\)、\(\boldsymbol\zeta=\nabla\times\mathbf u\) | 涡量二形式与三维涡量向量；区别于原文有时用于标量涡量的 \(\omega\) |
| \(P\)、\(T_\Psi=\Psi^*\) | 压力投影与连续一形式 pullback |

若位置用 m、时间用 s，则速度分量为 m/s，\(p\) 与 \(\lambda\) 为 m²/s²，环量为 m²/s，涡量分量为 s⁻¹。\(d\Psi\) 是无量纲的空间 Jacobian。下文约定 \((J_{\mathbf v})_{ij}=\partial_jv_i\)，避免把原文的梯度记号直接套成另一种矩阵约定。

### 多出的项为什么是动能梯度

从

\[
\partial_t\mathbf u+(\mathbf u\cdot\nabla)\mathbf u=-\nabla p,
\qquad \nabla\cdot\mathbf u=0
\]

出发，利用 \((J_{\mathbf u})^T\mathbf u=\nabla(\lvert\mathbf u\rvert^2/2)\)，得到

\[
\partial_t\mathbf u+(\mathbf u\cdot\nabla)\mathbf u
+(J_{\mathbf u})^T\mathbf u
=-\nabla\lambda.
\]

一形式 Lie derivative 的分量为

\[
(\mathcal L_{\mathbf v}\eta)_i
=v_j\partial_j\eta_i+\eta_j\partial_i v_j,
\]

这里重复指标求和。于是完整 Euler 方程写成

\[
\boxed{\partial_t\eta+\mathcal L_{\mathbf u}\eta=-d\lambda,
\qquad\mathbf u=\eta^\sharp,
\qquad\nabla\cdot\mathbf u=0.}
\]

这对应原文式 (14)、(25)–(26) 与 Appendix A.1。上面的分量写法是为统一矩阵约定所作的展开，不是另一套物理模型。[pp.5、7、16。][^1]

冻结 \(\mathbf v\) 后，CF 平流子步解的是

\[
\partial_t\eta+\mathcal L_{\mathbf v}\eta=0,
\]

其向量表示包含 \((J_{\mathbf v})^T\mathbf u\)。此时 \(\mathbf v\) 与正在变化的 \(\mathbf u\) 一般不同，这一项也一般不再等于 \(\nabla(\lvert\mathbf u\rvert^2/2)\)。因此，“原方程等价改写”和“冻结速度后的两个不同平流子步”是两个层次；CF 改进的正是后者。[§4.1–4.3，式 (23)、(28)–(29)。][^1]

### Jacobian 转置来自哪里

对任意切向量 \(\mathbf a\)，一形式 pullback 定义为

\[
(\Psi^*\eta)_{\mathbf x}[\mathbf a]
=\eta_{\Psi(\mathbf x)}[d\Psi(\mathbf x)\mathbf a].
\]

因而，在笛卡尔分量下

\[
\boxed{\eta_t(\mathbf x)
=(d\Psi_t(\mathbf x))^T\eta_0(\Psi_t(\mathbf x)).}
\]

标量只需取旧位置的值，一形式还要变换它所作用的线元；转置 Jacobian 就来自这个配对关系。只写 \(\eta_0\circ\Psi\)，相当于搬走数值却没有处理曲线的方向和伸缩。Fig.5 的刚体旋转对照展示了这一区别，也展示了正确的 covector transport 仍会受低阶插值耗散影响。[§3.4、§4.1，式 (6)、(9)–(10)、(19)–(24)，pp.5–6。][^1]

## 环量、涡量与压力投影之间的关系

### 纯平流与完整 Euler 的环量说法不同

若 \(C_t=\Phi_t(C_0)\)，纯 Lie transport 给出

\[
\int_{C_t}\eta_t=\int_{C_0}\eta_0.
\]

这个关系对开曲线也成立。完整 Euler 则有

\[
\frac{d}{dt}\int_{C_t}\eta_t=-\int_{C_t}d\lambda.
\]

开曲线会有端点势差；闭曲线的右端为零，才得到 Kelvin 环量定理。压力不改变闭合环量，是因为它对应 exact one-form，而不是因为完整方程里没有压力。[式 (4)、(8)、(22)、(26)，pp.2、5–7。][^1]

对平流方程取外微分，并用 \(d\mathcal L_{\mathbf v}=\mathcal L_{\mathbf v}d\)，有

\[
\partial_t\Omega+\mathcal L_{\mathbf v}\Omega=0,
\qquad \Omega=d\eta.
\]

三维中，令 \(\Omega=\iota_{\boldsymbol\zeta}\mu\)，其中 \(\mu\) 是体积形式、\(\iota\) 是内乘；若输运速度满足 \(\nabla\cdot\mathbf v=0\)，便得到

\[
\partial_t\boldsymbol\zeta
+(\mathbf v\cdot\nabla)\boldsymbol\zeta
-(\boldsymbol\zeta\cdot\nabla)\mathbf v=0.
\]

最后一项保留 vortex stretching/tilting，故三维涡量幅值不必逐点恒定。二维不可压情况下，二形式写成 \(\Omega=\zeta\,dx\wedge dy\)，涡量标量 \(\zeta\) 才满足随流输运。[§4.4、Appendix A.2，式 (31)，pp.7、16。][^1]

作为对照，逐分量平流会得到

\[
\partial_t\boldsymbol\zeta
+(\mathbf v\cdot\nabla)\boldsymbol\zeta
-(\boldsymbol\zeta\cdot\nabla)\mathbf v
=\sum_\ell\nabla u_\ell\times\nabla v_\ell.
\]

这就是原文式 (30) 的附加项。若某一瞬间 \(\mathbf u=\mathbf v\)，右端恰为零；但冻结 \(\mathbf v\) 后，\(\mathbf u\) 在子步内变化，二者一般不再相同。不能以步初相等否定这项分裂误差。[§4.4、Appendix A.3，pp.7、16。][^1]

### “平流与投影交换”应读成什么

原文 §4.5 以相差 exact differential 的一形式定义等价类。固定同一个输运场、同一个映射，并使用相容的投影边界条件时，

\[
T_\Psi(d\varphi)=d(\varphi\circ\Psi).
\]

因此，初始场是否先去掉 exact 部分，不影响平流后再投影得到的无散代表。准确关系是

\[
\boxed{P\,T_\Psi\,P=P\,T_\Psi,}
\]

而非通常意义上的 \(P\,T_\Psi=T_\Psi\,P\)：pullback 后的场一般仍有散度，需要最后一次投影。这是对式 (32)–(33) 及其后文字的数学展开；不表示重算输运速度后的非线性更新可以任意交换，也不表示离散插值与 limiter 自动满足同样的关系。[pp.7–8。][^1]

从这个角度看，CF 不是去掉不可压约束，而是让“相差一个压力梯度”的关系在输运中保持下去。投影在每一步仍有实际作用，尤其要为下一步流映射提供无散速度。

作为阅读者的几何补充，投影选取哪一个代表依赖边界条件；自由表面上的压力 Dirichlet 条件会限制可被吸收的梯度。多连通域中，相同 curl 也未必意味着只差一个全局 exact form，还可能有不同的 harmonic circulation，不能在改写时一并丢弃。这种一形式模 exact form 的表示可与 Lie–Poisson 主线衔接，但论文并未构造离散 Poisson bracket，也未证明其 MAC/BFECC 更新满足 Jacobi 恒等式或离散余伴随轨道保持。

还要区分环量与动能。作为阅读者补充推导，在周期域或无输运边界通量、\(\nabla\cdot\mathbf v=0\) 时，冻结速度的纯 covector 子步对 \(E=\frac12\int_M\lvert\mathbf u\rvert^2\,dV\) 满足

\[
\frac{dE}{dt}=-\int_M u_i u_j\,\partial_i v_j\,dV,
\]

一般不为零。这里 \(E\) 省略常密度因子，\(dV\) 是体积元；推导只用了分量 Lie 方程和分部积分。pullback 保持相应曲线积分，不等于对速度的 \(L^2\) 范数等距，这也是为什么论文的能量结果仍须由具体误差修正与实验来说明。

## 从连续 pullback 到可执行的网格更新

### 基础 CF：时间精度与输运精度分开看

令 \(A_{\mathbf v,\delta t}\) 表示时间跨度为 \(\delta t\) 的 covector advection，\(\delta t\) 可以为负。Algorithm 1 先取 \(\mathbf v=\mathbf u^n\)，再做平流、投影；Algorithm 2 先估计半步速度：

\[
\mathbf v^{n+1/2}
=P\,A_{\mathbf u^n,\Delta t/2}\mathbf u^n,
\qquad
\mathbf u^{n+1}
=P\,A_{\mathbf v^{n+1/2},\Delta t}\mathbf u^n.
\]

这处理的是冻结输运速度的时间截断误差。Algorithm 3 中的 RK4 回溯处理的是给定 \(\mathbf v\) 后的轨迹积分；采用 RK4 并不会让整个分裂求解器自动变成四阶。[§5.1–5.2，pp.8–9。][^1]

```mermaid
flowchart LR
    accTitle: Covector Fluids Time Step
    accDescr: 先估计半步输运速度，再通过回溯、插值和转置Jacobian执行一形式输运，最后投影恢复不可压约束。
    estimate_velocity["估计半步速度"] --> trace_map["RK4 回溯映射"]
    trace_map --> interpolate_velocity["插值旧速度"]
    interpolate_velocity --> pullback_covector["乘转置 Jacobian"]
    pullback_covector --> correct_error["BFECC 误差修正"]
    correct_error --> project_velocity["压力投影"]
```

图中是单步计算关系，不表示每个模块只调用一次。BFECC 内部有三次输运。按 Algorithm 4，若 \(A_+\) 与 \(A_-\) 分别是固定 \(\mathbf v\) 下的正、反时间半拉格朗日 covector transport，则

\[
\mathbf u_1=A_+\mathbf u^n,
\qquad
\widetilde{\mathbf u}_0=A_-\mathbf u_1,
\qquad
\mathbf e=\widetilde{\mathbf u}_0-\mathbf u^n,
\qquad
\mathbf u_{\rm corr}=\mathbf u_1-A_+(\mathbf e/2).
\]

最后还要做 §5.4.2 的 extrema limiter：按分量将修正值限制到 \(\mathbf u_1\) 的邻域极值范围。这个非线性限制器用于抑制振荡，也使实际更新不再是精确线性 pullback。BFECC 与对照方法 MacCormack（MC）有亲缘关系，但不能混称；这里误差经过再次输运后才在目标网格修正。[p.9，Algorithm 4、§5.4.2。][^1]

### MAC 网格上到底多算了什么

速度分量位于相应法向的 face center，压力及映射等量位于 cell center。以法向为 \(x\) 的面 \(F_{ij}\) 为例，CF 更新该面上的第一分量：

\[
u_{1,F_{ij}}^*
=\sum_{\alpha\in\{x,y,z\}}
\left.\frac{\partial\Psi_\alpha}{\partial x}\right|_{F_{ij}}
 u_\alpha(\Psi(F_{ij})),
\qquad
\left.\frac{\partial\Psi_\alpha}{\partial x}\right|_{F_{ij}}
\approx\frac{\Psi_\alpha(C_j)-\Psi_\alpha(C_i)}{\Delta x}.
\]

\(C_i,C_j\) 是该面两侧的相邻单元中心，\(\Delta x\) 是中心间距。若 \((d\Psi)_{\alpha i}=\partial_i\Psi_\alpha\)，这里使用的是 **\(d\Psi\) 的第 \(i\) 列**，即其转置的第 \(i\) 行。旧笔记直接说“Jacobian 的一行”不够准确，容易把转置写反。[§5.4.1，式 (39)–(40)，p.9。][^1]

所以，局部修改指的是：在速度插值之后加入映射导数的收缩，不再额外求解涡量到速度的全局重建。它没有取消原有的全局压力求解，也没有消除构造映射、回溯与通信的成本。

边界也沿用常规网格求解器处理：固体处约束 \((\mathbf u-\mathbf u_{\rm solid})\cdot\mathbf n=0\)，\(\mathbf n\) 是边界法向，\(\mathbf u_{\rm solid}\) 是固体速度；自由表面/流出设置使用零压力 Dirichlet 条件，回溯越界时取域内最近点的场值。这是 no-through 处理，不是解析黏性 no-slip 边界层；最近点取值也不自动保持物质曲线的 pullback 关系。[§5.4.5，p.10。][^1]

### CF+MCM：少插值速度，不是长时间不投影

普通逐步输运不断对速度插值；长期 characteristic mapping 保存参考速度与正、逆映射，通过较长时间的映射直接拉回参考场，减少反复采样。CF+MCM 又利用 exact differential 在 pullback 下仍 exact 的性质，使累积压力历史可以在最终投影中吸收，而不必像传统 MCM 那样逐项维护。[§4.6、§5.3，式 (34)–(38)、Algorithm 5，pp.8–9。][^1]

这里的“最终投影”要放回算法理解：Algorithm 5 第 10 行仍在**每个时间步**投影。长期映射保存的是一个参考态，不是让生成下一步流映射的物理速度持续带着散度。它同时维护 \(\Phi\) 与 \(\Psi\)，用于往返误差修正，并在映射失真或达到预设间隔时重置。本论文实验采用 one-level mapping，每 5 个时间步重置；3D BiMocq 用 DMC，而 2D BiMocq 与所有 CF+MCM 用 RK4，因此比较也不完全是只替换一个变量的消融。[§5.3、§6，pp.9–10。][^1]

长期映射还有两个实现边界。§5.3 用 \(\Phi\circ\Psi\ne\Psi\circ\Phi\) 举例说明映射失准，但判断互逆性应分别检查 \(\Phi\circ\Psi\) 和 \(\Psi\circ\Phi\) 偏离恒等映射的程度；仅比较两种复合是否相等，不能保证互逆。[p.9。][^1]

另一个边界来自外力。可被投影吸收的是 exact 压力历史，空间变化密度产生的浮力 \(\mathbf f=c\rho\mathbf g\) 一般并非 exact。这里 \(c\) 是比例常数，\(\rho\) 是输运的密度/温度标量，\(\mathbf g\) 为重力加速度；\(c\rho\) 的尺度由所用示踪量定义。非保守源项需要另行累计或等效更新到长期参考表示中。Algorithm 5 未列出这部分完整处理，§5.4.4 只说明投影前加力；本次未核对补充代码，不据此认定实际实现遗漏。[pp.9–10。][^1]

### 原文两处需要带着推导阅读的细节

以下为本次核证发现，不是作者发布的勘误，也不是已经验证的代码修复。

第一，p.8 式 (36)–(38) 把累积压力项写成加号，但式 (1)、(26) 的右端分别为 \(-\nabla p\)、\(-d\lambda\)。由完整方程直接推导，

\[
\frac{d}{dt}\Phi_t^*\eta_t=-d(\Phi_t^*\lambda_t),
\]

所以在同一符号约定下应得到

\[
\eta_t=\Psi_t^*\eta_0
-d\!\left[\int_0^t(\Phi_\tau\circ\Psi_t)^*\lambda_\tau\,d\tau\right].
\]

\(\tau\) 是积分时间，\(\Phi_\tau\circ\Psi_t\) 把当前点映射到中间时刻。原 PDF 页面也印为加号，已排除纯文本提取漏号的可能。上述负号是阅读者依据式 (26) 的推导；exact 项最后被投影吸收的结论并不因这处符号差异改变。[p.8，Remark 2。][^1]

第二，Algorithm 5 第 8 行印为 \(\mathbf e=\widetilde{\mathbf u}_0-\mathbf u\)，而第 1 行保存的参考速度是 \(\mathbf u_0\)，第 7 行的 \(\widetilde{\mathbf u}_0^\flat=\Phi^*(\mathbf u_1^\flat)\) 也已回到参考域。按往返误差的域和时间层，应核查参照量是否应为 \(\mathbf u_0\)。本文不据此宣称作者实现有错；补充代码尚未审计，实现前需要对照确认。[p.9，Algorithm 5，第 1、5、7–9 行。][^1]

## 实验证据支持了多强的结论

### 先看比较口径

除 Fig.7 比较一阶与二阶外，正文实验使用二阶 CF 加 BFECC；MC+R 也使用二阶版本。表 1 中，SF 为 Stable Fluids，SCPF 为 Stable and Circulation Preserving Fluids，MC 为 MacCormack，R 为 Reflection，MCM 为 Method of Characteristic Mapping，BiMocq 为 Bi-directional Mapping of Convective Quantities，IVOCK 为 Integrated Vorticity of Convective Kinematics。它们处理的误差来源不同，不能把所有差异都归因于是否使用协向量。[Table 1、§6，pp.3、10。][^1]

| 实验与定位 | 条件与比较对象 | 证据及其边界 |
| --- | --- | --- |
| 一形式刚体旋转，Fig.5，p.6 | \(200\times200\)，见 Table 2；逐分量输运、covector sL、covector BFECC | 分离方向变换错误与采样耗散；不是完整不可压求解器的守恒测试 |
| Taylor vortices，§6.1.1、Fig.8，pp.10–11 | 两个相距 0.81 m 的 shielded Gaussian vortices；核半径 0.3 m，最大切向速度 1 m/s；\(256^2\)，\(\Delta t=1/40\) s | CF/CF+MCM 能量曲线接近 MC+R、BiMocq；BFECC/MC 误差修正对结果关键。这不是常见的 Taylor–Green vortex 基准，也不是严格离散能量守恒证明 |
| Trefoil knot，§6.1.2、Fig.9，p.11 | 初始环量 1 m²/s；\(256\times128\times128\)，\(\Delta t=1/48\) s | 展示重连、涡量强度与能量曲线；结果是该配置下的比较，不提供普适误差界；重连的定性相似也不是光滑无黏 Euler 涡线拓扑保持的验证 |
| 双涡环 leapfrogging，§6.1.3、Fig.10，p.11 | 半径 1.2 m 与 2.0 m，环量各 0.56 m²/s；\(256\times128\times128\)，\(\Delta t=1/48\) s | 作者方法第三次 leap 后仍分离，其他展示方法较早合并；不是无限期保持的数值验证 |
| von Kármán vortex street，§6.3.1、Fig.15，p.13 | 背景流 0.5 m/s；控制黏性比较 Re=300 与 4000；Fig.15 使用 \(1024\times512\)、\(\Delta t=1/40\) s | 与高分辨、小步长 MC+R 数值 reference 对照，支持形态一致性；“ground truth”不是解析解或实验测量 |
| Delta wing，§6.3.3、Fig.17，pp.13–14 | 攻角 20°、后掠角 70°、厚度 0.125 m，背景流 1 m/s | 与物理实验图作定性对照；作者明确省略精细固液相互作用与边界层建模，未给出升阻力定量验证 |

表中网格与步长来自 Table 2（p.10），现象与解释来自对应章节、图注；没有从曲线像素估算作者未报告的百分比。[Table 2、Fig.5、8–10、15、17。][^1]

Ink drop、ink jet、烟羽、pyroclastic cloud、移动 bunny 与 bunny meteor 则补充了浮力、重力和障碍物下的动画场景，主要支撑涡结构与视觉细节的比较。浮力按 Boussinesq 模型在投影前加入；这类有外力场景不适合直接套用无外力的动能或 Kelvin 守恒说法。原文也没有给出标准均匀各向同性湍流衰减的统计基准。[§5.4.4、§6.2–6.3，pp.10–14。][^1]

### 成本与稳定性要保留实验条件

§6 的 Performance Summary 报告：相对 existing methods，完整时间步总体观察到约 15% 的计算时间增加。额外成本主要来自逆映射回溯；与 BiMocq 比较时可复用已有映射回溯，作者将额外成本主要归于二阶速度估计。表 2 只列 CF 与 CF+MCM 的逐例时间，没有列出所有基线的对应时间，因此这不是可据表逐项重算的统一 15% 比值。[p.10。][^1]

例如，Table 2 的 trefoil knot 在 \(10\times5\times5\) m³、\(256\times128\times128\)、\(\Delta t=1/48\) s 下，CF 与 CF+MCM 单步分别为 8.0 s 与 4.8 s。这是两种 CF 配置的计时，不是“相对 MC 慢 15%”的分母。2D 使用 CPU 并行；3D 只有 advection 部分在 RTX 2080 上使用 CUDA，其余仍在 CPU。因此该计时也不代表全 GPU 或 AMR 实现的性能。[§6、Table 2，p.10。][^1]

§5.4.3 针对 trefoil knot 与 smoke plume 尝试不同步长，以保持稳定的最大步长构造

\[
C=\frac{U\Delta t_{\rm critical}}{\Delta x},
\qquad U=\max_{\mathbf x,t}\lvert\mathbf u(\mathbf x,t)\rvert.
\]

表列 CF 为 6.18、SCPF 为 4.85、IVOCK 为 1.45。这是指定实验与实现中的经验临界值，不是保证所有流动稳定的 CFL 上限。作者在 §7 明确没有解析稳定性判据，并将主要不稳定来源指向对流动形变敏感的 flow-map Jacobian。[pp.9–10、14。][^1]

## 放到 AMReX/VWiS 主线里，哪些东西值得带走

以下是阅读者的迁移分析与待验证设想，论文没有在 AMReX、EB、AMR 或 VWiS 上验证这些结论。

首先应带走的是变量的几何含义，而不是变量名。在欧氏笛卡尔网格上，速度向量与速度一形式可以通过固定度量共用分量；但一形式的环量、面法向体积通量，以及涡量二形式承担的是不同的积分关系。MAC face-centered 速度并不因为改名为 covector 就成为严格 DEC 一形式。不过，face 存储位置本身也不排斥一形式解释：正交 MAC 的 face center 同时可以是 dual edge 的中点，沿 dual edge 的环量与穿过 primal face 的通量需要不同的长度、面积权重。论文使用的是点样本，而非已建立完整积分 cochain 复形的方案。进入曲线网格、EB 或 AMR 前，需要明确 primal/dual complex、metric/Hodge 映射和各量的存储位置。

其次是把结构问题转成可检查的离散关系。令 \(T_{\Psi,h}\) 为网格间距 \(h\) 下的离散 pullback，\(d_h\) 为相应离散外微分，\(P_h\) 为离散投影；前两个作用于不同次数形式时需要各自匹配的算子。可以分别检查

\[
d_hT_{\Psi,h}\eta_h-T_{\Psi,h}d_h\eta_h,
\qquad
P_hT_{\Psi,h}P_h\eta_h-P_hT_{\Psi,h}\eta_h,
\]

再结合物质闭合路径的环量漂移、散度残差与能量变化，区分插值、Jacobian 差分、limiter 和投影容差的影响。这里提出的是误差诊断，不是已有离散交换定理。

对于 AMR，还要把检查推进到 coarse–fine 同步：映射的 ghost fill、prolongation、restriction、regridding 与重置会怎样影响环量？通量 reflux 保证的守恒量，是否与当前的 circulation 表示兼容？EB 附近的回溯截断和最近点取值是否额外注入环量？这些都是单层规则网格结果没有回答的问题。

GPU 方面，局部回溯采样、映射导数与矩阵—向量乘法适合 patch-local kernel，但长期 \(\Phi/\Psi\)、参考速度和误差场增加了存储及跨 patch 取样需求。应先在单层 MAC 基线上分离精度与计时，再加入 AMR，不直接把原文约 15% 的观察当作工程预算。

## 保留的问题与核证边界

1. 在相同插值、回溯和投影容差下，怎样分别测量 \(d_hT_{\Psi,h}-T_{\Psi,h}d_h\) 与 \(P_hT_{\Psi,h}P_h-P_hT_{\Psi,h}\) 的缺陷？BFECC limiter 激活后，哪一部分误差主导闭合环量漂移？
2. 若 circulation、face-normal flux 与 vorticity 位于不同 primal/dual 对象，怎样设计 AMR restriction/prolongation、reflux 和 map reinitialization，使通量守恒与低环量误差相容？
3. 能否用 flow-map Jacobian 的变形程度或条件数构造比固定每 5 步更有依据的重置/步长准则，并在不增加过多插值耗散的情况下建立能量或环量误差界？

本次重整保留了旧笔记的数学—算法—AMReX 关联，但重新区分了三类陈述：连续方程的几何性质、论文给定离散配置下的实验现象，以及尚未验证的工程迁移。尤其不将“更好保持能量”写成严格能量守恒，不将“速度层面的 vortex method”写成无需压力求解，也不把原文疑点写成已完成代码修复。

方法补充、实验核查、独立终审及主 Agent 的逐项处理意见均保存在[本次归档目录](<../reading/records/20261119-covector-fluids/>)。独立上下文审阅与主 Agent 核证是不同环节；实际路由及输入/输出哈希见该目录记录，不以模型名称或调用成功替代内容验收。未复现实验的范围保持不变。

[^1]: Nabizadeh, M. S., Wang, S., Ramamoorthi, R., & Chern, A. (2022). Covector Fluids. ACM Transactions on Graphics 41(4), Article 113. https://doi.org/10.1145/3528223.3530120 。本次核读的作者托管 16 页 PDF：https://cseweb.ucsd.edu/~viscomp/projects/SIG22CovectorFluids/paper/CovectorFluids.pdf 。文中给出的页码、式号、图表及算法号均对应这一哈希版本。
