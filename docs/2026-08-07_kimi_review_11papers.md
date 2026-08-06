# Kimi Code Review — 11 篇补精读（2026-08-07 批次）

> 审查对象：CODEX_DEEP_READ 审计发现的 11 篇真空壳补精读文档。
> 流程：Codex (gpt-5.5) 精读 → Kimi Code (gpt-5.4, v0.34.0) 审查 → 修正落地 → 归档。
> 审查方式：正文内联进任务文件（两批：批A 6 篇几何/流体，批B 5 篇 AI/量子），Kimi 逐篇输出 公式/代码算法/格式/逻辑问题 + 3 个追加 Review Questions。
> 说明：Kimi 引用的行号对应内联审查文件的偏移，非最终 .md 文件行号。

---

# ============ 批 A（文档 1-6）============

我先读取这份内联总文件并逐篇审查。
我继续读取后半部分，然后按 6 篇完整整理审查意见。
**文档1：`geometric-fluid/covector-fluids.md`**

1. 公式问题
- `59-60` 行说“`u` ... 变换律不是向量推前，而是 covector pullback”，但 `103-110` 行又写 `u(t)=\varphi_{t*}^{-1}u(0)` 与 `u^{*}(x)=DX(x)^T u^n(X(x))`。这里推前/拉回记号混用，建议统一成“`u(t)=(\varphi_t^{-1})^*u(0)`”或明确 `\varphi_{t*}^{-1}` 只是 pullback 的等价写法，否则读者容易误解。
- `74-80` 行把
  \[
  \mathcal L_v u=(v\cdot\nabla)v^\flat+d(\tfrac12|v|^2)
  \]
  代回后得到
  \[
  \partial_t u+\mathcal L_v u=-d\left(p-\frac12|v|^2\right)
  \]
  这一符号是自洽的，但 `191-192` 行再次给出同式时省去了前文“欧氏情形 `u_i=v_i`”的条件，容易让人误以为一般黎曼流形上也直接成立。
- `168-171` 行写
  \[
  \partial_t m+\operatorname{ad}_v^*m=0
  \]
  而前文主要变量是 `u`。这里 `m` 被称为 “one-form density”，但未说明与 `u` 的关系是 `m=u\otimes dV` 还是经 Leray 投影后的对偶变量，记号跳变过快。

2. 代码算法问题
- `133-143` 行把实现写成“先做 covector advection 得到 `u*`，升指标得 `v*`，再解 Poisson，最后 `u^{n+1}=(v^{n+1})^\flat`”。如果实际离散变量本来就是 edge/face one-form，自然的做法应是直接在 one-form 空间做 Hodge/Leray 投影。当前描述更像把几何变量又退回成普通速度场，算法层面少了“离散投影算子与 one-form 存储的匹配”。
- `232-234` 行提出 `advect_covector(field_u, backtrace_X, jacobian_DX)`，但没有说明 `DX` 如何离散计算、插值以及与 `X` 使用同阶精度保持一致。若 `X` 用高阶回溯而 `DX` 只用一阶差分，守恒改进可能明显退化。
- `232-234`、`244-245` 行都强调 AMR/Whitney 1-form，但正文没有交代在非欧氏/AMR 场景下 `\sharp/\flat`、Hodge star、Poisson 投影三者的离散兼容条件，这是该方法能否真正“无缝集成”的关键步骤。

3. 格式问题
- `41-45` 与 `242-246` 出现了两组 `## Review Questions`，重复。
- `39` 行写“`✅ 完整摘要`”，但 `24` 行摘要是“_暂无_”，前后矛盾。
- `49` 行再次出现裸标题 `Covector Fluids`，与文首 `# Covector Fluids` 重复，层级不整齐。
- `53` 行含大量英文/反引号术语，整体风格与前面中文“总结”部分不完全一致，但问题较轻。

4. 逻辑问题
- `34-35` 行称“显著改善...解决了传统流体模拟中的数值耗散问题”。“改善”有依据，但“解决”过满；该方法通常是缓解半拉格朗日速度平流带来的结构耗散，不等于全面解决数值耗散。
- `37` 行把方法直接外推到“HPC 流体求解器，改善高雷诺数流动的涡量守恒”，这个推断方向合理，但原文主要面向图形学不可压模拟，不宜直接上升为工程高 Re 求解器结论。
- `171` 行说“把最关键的 `ad*` 对流变换嵌进了廉价的 semi-Lagrangian step”，这句话抓住了思想，但略弱化了代价前提：需要高质量回溯映射及其 Jacobian，实际在复杂网格/AMR 上未必“廉价”。

5. Review Questions
- 若把 Covector Fluids 嵌入离散外微分/Hodge 框架，`DX^T` pullback 与离散 `d`、Hodge star 需要满足什么交换关系，才能真正保持 circulation 而不只是经验上更稳？
- 在 AMR 或曲线网格上，`u` 作为 one-form 的存储位置应如何选择，才能让 Poisson 投影、涡量诊断和 coarse-fine 同步保持一致？
- 该方法主要改善几何守恒而非能量守恒；若面向长期积分或高 Re 计算，是否需要再叠加 energy-preserving / symplectic 时间推进？

---

**文档2：`geometric-fluid/schrödingers-smoke.md`**

1. 公式问题
- `258` 行 DOI 写成 `[http:](https://doi.org/http:)`，明显错误；`297` 行后文才给出正确 DOI `10.1145/2897824.2925868`，元数据前后不一致。
- `306-307` 行写 `\Psi^\dagger\Psi=1`，`391-392` 行做点态归一化 `\Psi\leftarrow \Psi/|\Psi|`。如果这里的约束是逐点单位范数，应明确写成 `|\Psi(x)|=1`；当前写法既可被读成全局 `L^2` 归一化，也可被读成点态约束。
- `357-370` 行把总能量写为 `E_{\rm kin}+E_{\rm LL}`，但未说明这是精确等式、等价泛函，还是文中某种近似/重写。对熟悉 GP/LL 模型的读者，这里会关心是否缺少约束项或常数因子。

2. 代码算法问题
- `394-405` 行描述算法为“Schrödinger 步 -> 归一化 -> 投影”，但没有说明 projection 与 normalization 的先后次序是否可交换、为何这样分裂保持二阶或一阶精度。对 splitting 方法，这是关键算法细节。
- `407` 行说障碍物“通过 penalty 或 mask 处理”，但没有给出边界条件如何进入相位投影或 Helmholtz/Poisson 求解。对非周期域，这是方法可实现性的核心，不应一笔带过。
- `464-465` 行说周期域核心 kernel 是 FFT 等，`473-474` 行才提到非周期需换 solver；但正文没有交代若离开周期盒，Schrödinger 步本身如何高效离散，这会让“HPC 上实现此类方法需要高效 FFT 和 Poisson”显得过度乐观。

3. 格式问题
- `285-289` 与 `476-480` 两处 `## Review Questions` 重复。
- `282` 行写“`✅ 完整摘要`”，但 `266` 行仍是“_暂无_”。
- `293` 行再次出现裸标题 `Schrödinger's Smoke`，与文首重复。
- 文中英文术语、中文说明、反引号风格混合较多，整体可读性尚可，但风格不完全统一。

4. 逻辑问题
- `276-278` 行称“证明了不可压缩 Euler 流的涡动力学等价于 GP 方程在压力投影极限下的 Schrödinger 演化”“天然保持涡量守恒”“自动捕获涡旋重连”。这几句都偏强。尤其“自动捕获重连”与经典无黏 Euler 的涡线冻结并不相容，后文 `474` 行自己也提出了这个张力。
- `280` 行把方法上升为“量子-经典混合计算方法提供新思路”，这个外推过宽，原文主要是几何/图形学流体表示。
- `460` 行说“该步是酉的，保持 `L^2` 范数；归一化和投影再把状态拉回约束流形。这解释了算法稳定性的来源。”这解释过于简化；整体分裂并不因单步酉性就自动稳定。

5. Review Questions
- 该方法中的 `U(1)` gauge、点态单位范数约束与不可压投影之间，哪个才是真正承载流体几何结构的核心约束？
- 对非周期域和固壁边界，如何构造既保留 Berry connection 解释、又不破坏投影结构的离散 Schrödinger 步？
- 若把 `\Psi` 作为 AI4Physics 的学习变量，怎样处理 gauge 冗余，避免网络学到物理等价但数值不稳定的表示？

---

**文档3：`fluid-mechanics/spectral-analysis-of-nonlinear-flows.md`**

1. 公式问题
- `521` 行写“稀疏促销或优化型 DMD 变体”，应为“稀疏促进”或“sparsity-promoting DMD”，属于术语错误。
- `574-580` 行写
  \[
  \mathbf g(x)=\sum_j\varphi_j(x)\mathbf v_j,\qquad
  \mathbf g(T^t x_0)=\sum_j e^{\lambda_j t}\varphi_j(x_0)\mathbf v_j
  \]
  这是标准形式，但缺少对展开条件的限定，例如周期/准周期、解析可观测量或离散谱情形。当前写法太像无条件成立。
- `601` 行 `A=YX^+` 与 `613-625` 行 exact/projected DMD 公式并列给出，但没有说明 `\Phi_j=YV_r\Sigma_r^{-1}w_j` 对应 exact DMD，而非简单的 projected DMD，记号上略混。

2. 代码算法问题
- `585-640` 行给出标准 DMD 流程，但完全缺少 rank truncation `r` 的选择准则。对实际数据，`r` 的选取比公式本身更决定结果质量。
- `711-717` 行提到大规模 CFD 可改算 `C=X^*X, G=X^*Y` 或 randomized SVD，但没有讨论这些做法在噪声、非均匀内积、加权网格体积下如何修正，算法描述偏理想化。
- `719-722` 行提出 unitary/measure-preserving DMD、symplectic DMD，但正文前面没有说明标准 DMD 对不可压或 Hamiltonian 数据会产生什么具体伪谱污染，导致建议显得悬空。

3. 格式问题
- `517-521` 与 `729-733` 两组 `## Review Questions` 重复。
- `515` 行写“`✅ 完整摘要`”，但 `500` 行是“_暂无_”。
- `525` 行再次出现裸标题 `Spectral Analysis of Nonlinear Flows`，与开头重复。
- `488` 行中文题目，`525` 行英文题目，双标题并存但未分层说明。

4. 逻辑问题
- `510-511` 行说“相比传统 POD/DMD，该方法更好地捕获了非线性模态间的相互作用”。本文本质是在阐明 Koopman 模态观点与 DMD 的关系，把 “该方法” 与 “DMD”对立起来不准确，因为 DMD 正是其数值近似工具之一。
- `529` 行称“是 DMD 与 Koopman mode decomposition 关系的标志性论文”基本成立，但 `504-511` 行摘要部分把它说成“开发了一种新的谱分析框架”，容易让人误解为论文提出了一个全新可直接执行的算法，而非主要做统一解释和示例分析。
- `583-584` 行说“这正是 DMD 输出比 POD 更容易解释的原因”，表述略绝对。很多实际流动中 DMD 也会因噪声、非正态瞬态、采样窗口而难解释。

5. Review Questions
- 对连续谱或强非正态放大的流动，Koopman/DMD 分析应如何区分真实动力学结构与有限窗口、有限秩带来的谱污染？
- 若数据来自 AMR、非均匀网格或加权有限元离散，DMD 的内积和正交化步骤该怎样修改，才能让模态幅值具有物理意义？
- 在 AI4Physics 中，把 Koopman 线性化当作 latent prior 时，怎样避免模型只学到短时频率拟合而丢掉长期守恒和稳定性？

---

**文档4：`fluid-mechanics/粘弹性流体/the-log-conformation-formulation-for-single--and-multi-phase-axisymmetric-viscoe.md`**

1. 公式问题
- `832-835` 行写
  \[
  \nabla u=\Omega+B+NA^{-1},\qquad \Omega^T=-\Omega,\ B A = A B,\ N^T=-N
  \]
  这里分解记号较可疑。Fattal-Kupferman 的分解通常更精细，且 `N A^{-1}` 这一写法若不解释来源和维度，很容易让读者怀疑是否抄写错误或省略了关键定义。
- `838-840` 行给出
  \[
  \partial_t\Psi+u\cdot\nabla\Psi-(\Omega\Psi-\Psi\Omega)-2B
  =-\frac1\lambda e^{-\Psi}f_R(e^\Psi)
  \]
  但 `943-944` 行又写成
  \[
  D_t\Psi=\Omega\Psi-\Psi\Omega+2B-\frac1\lambda e^{-\Psi}f_R(e^\Psi)
  \]
  两处等价，但符号移项后的 presentation 不统一，建议明确一处为最终标准式。
- `818-819` 行 FENE-P 松弛项写成
  \[
  f_R(A)=\frac{A}{1-\operatorname{tr}(A)/L^2}-I
  \]
  若不补充分母正号约束与参数定义，容易让读者忽略 `\operatorname{tr}(A)<L^2` 的物理/数学前提。

2. 代码算法问题
- `958-959` 行说每个网格点需要 `3x3` 矩阵 `log/exp`、特征分解或封闭公式，但对轴对称无旋流结构，`A` 实际有 `2x2+1` 的特征结构可利用。正文没有把这一结构优化转化为明确算法建议。
- `960-963` 行提到 IMEX、BDF2、JFNK、AMR 插值，但没有说明 log-conformation 方程是如何与动量方程耦合离散的：显式对流/隐式松弛/全耦合 Newton 各自适用情形未区分。
- `962` 行说“更稳的做法是在 `\Psi` 空间插值，然后指数映射”，这是合理建议，但没有说明插值后如何保持对称、如何处理界面不连续系数对 `\Psi` 的非线性影响。

3. 格式问题
- `755` 行标题写成 `## Summary`，其余文档大多用中文 `## 总结`，风格不统一。
- `770-774` 与 `972-976` 两组 `## Review Questions` 重复。
- `768` 行写“`✅ 完整摘要`”，但 `753` 行仍是“_暂无_”。
- `778` 行再次出现裸标题 `Log-Conformation Formulation`，重复。

4. 逻辑问题
- `762-764` 行称“高Wi数（Wi>10）下保持数值稳定，远超传统方法上限”“不需要任何人工扩散或稳定化技术，数值稳定性的提升完全来自数学变换”，表述偏满。实际稳定性还依赖离散、时间推进、界面处理和边界条件。
- `821-827` 行把高 Wi 问题的核心归结为 “直接离散 `A` 可能失去正定”。这抓住了一部分，但 HWNP 不仅是正定性问题，也涉及应力边界层解析度、对流主导和离散误差累积。
- `964` 行建议神经网络预测 `\Psi` 优于 `A` 或 `\tau_p`，方向合理，但“可以把正定性作为硬约束，减少...非物理解”说得太顺；实际还要处理 objectivity/frame indifference，不只是 SPD。

5. Review Questions
- 在轴对称多相场景中，`log/exp` 变量变换解决了 SPD 问题，但是否同时保留了正确的离散自由能或应力功关系？
- 若采用 JFNK 全耦合求解，`u-p-\Psi` 三块之间最难预条件的耦合是压力 Schur 补、应力散度，还是局部矩阵函数线性化？
- 对 AI4Physics 而言，仅预测 `\Psi` 是否足够，还是还需要把 frame indifference、界面 jump 条件和 `u_r/r` 轴线结构显式编码进网络？

---

**文档5：`vortex-dynamics/incompressible-flow-simulation-on-vortex-segment-clouds.md`**

1. 公式问题
- `1069-1073` 行把 `\Gamma_i l_i` 直接写进 blob 形式
  \[
  \omega(x)\approx\sum_i \Gamma_i l_i\,\zeta_\epsilon(x-x_i)
  \]
  这里量纲和几何含义需要说明：`l_i` 是长度向量还是方向乘长度，`Γ_i` 是环量还是单位长度强度，否则与 `1078-1080` 的线积分式容易混淆。
- `1093-1099` 行有限直涡段速度公式写法较紧凑，但没有声明 `l_i=b_i-a_i`，而前文 `1066-1069` 只是说 `l_i` 是线段向量；若读者套用不同定义，符号容易误用。
- `1151-1155` 行把
  \[
  D_t\omega=(\nabla u)\omega
  \]
  直接说成 “这就是 Cauchy vorticity formula 的内容”，不够准确。这更像涡量拉伸方程；Cauchy 公式通常是通过流映射 Jacobian 写成显式表示。

2. 代码算法问题
- `1116-1123` 行提到黏性可用 particle strength exchange 思路，但紧接着又说“对涡段，需要同时处理强度、方向和 segment length 的一致性”，没有给出任何离散策略。这是算法空缺，不只是开放问题。
- `1125-1131` 行把 split/merge/reseeding 说成核心，但缺少触发准则、守恒约束和邻域搜索方式；而这些恰恰决定该方法是否比 vortex particle 更稳。
- `1183-1187` 行提出 GPU memory pool、BVH、vortex-in-cell 等实现路线，但没有区分哪种是论文实际采用、哪种是扩展建议，容易让审查对象边界不清。

3. 格式问题
- `1013-1017` 与 `1195-1199` 两组 `## Review Questions` 重复。
- `1011` 行写“`✅ 完整摘要`”，但 `996` 行是“_暂无_”。
- `1021` 行再次出现英文裸标题，和开头中文标题重复。
- `1183` 行出现英文句子 “carefully designed memory pool...”，与全中文叙述风格不统一。

4. 逻辑问题
- `1005-1007` 行称“涡量守恒和拓扑保持方面优于经典涡粒子方法”“计算效率接近粒子方法但精度更高”，这些判断需要非常具体的对比条件。不同 kernel、FMM、重采样策略下结论未必成立。
- `1006` 行说“成功模拟...涡管重联等复杂涡动力学过程”，若模型是无黏或弱物理黏性，重联更多是数值正则化与重采样共同作用的结果，不能直接当作物理真实性背书。
- `1131` 行说“因此能处理非闭合涡管重联和断裂”，这在图形学模拟意义上可以成立，但从流体力学建模角度应更谨慎区分“表示能力”和“物理解的可接受性”。

5. Review Questions
- 在 segment split/merge 过程中，最低限度应守恒哪些矩量或拓扑量，才能避免 reseeding 本身成为主要数值耗散源？
- 多 GPU 上若做 Biot-Savart/FMM，segment cloud 的动态负载均衡会不会比核函数求和本身更快成为瓶颈？
- 若把这种几何表示用于科研级涡动力学而非图形学，如何定量区分物理重联、正则化诱导重联和纯拓扑编辑？

---

**文档6：`wave-mechanics/extended-lagrangian-approach-for-the-numerical-study-of-multidimensional-dispers.md`**

1. 公式问题
- `1270-1277` 行给出的 1D SGN 动量式和 `\gamma` 表达是“常见形式”，但没有说明与论文具体记号是否完全一致。若这是综述性改写，最好明确，否则读者会以为是原文精确方程。
- `1309-1312` 行写扩展拉格朗日
  \[
  \mathcal L_\epsilon=\frac12h|u|^2-\frac12gh^2+\frac16hq^2-\frac1{2\epsilon^2}(q-D_th)^2
  \]
  这看起来是解释性模型，而不一定是论文精确形式。后文 `1314` 行也说“不同论文记号可能...”，说明这里更像概念示意，应更明确标注“示意形式”。
- `1372-1379` 行从
  \[
  \frac1{\epsilon^2}(q-D_th)
  \]
  推出
  \[
  q=D_th+O(\epsilon^2)
  \]
  这个量级结论需要更多条件，当前直接写出偏快。

2. 代码算法问题
- `1337-1349` 行只给出抽象 IMEX RK 模板，没有说明论文里隐式子步是局部求解、线性椭圆求解还是非线性耦合求解。对“可实现性审查”而言，这一步缺得比较关键。
- `1399-1410` 行多次提到 JFNK、multigrid、composite solve，但没有区分哪些是论文实际数值实现，哪些是你对 HPC 框架的外推建议。
- `1409-1410` 行提 AMR reflux 与隐式色散 level/composite solve 的耦合，这是很好的工程问题，但正文没有给出任何一致性策略，停留在口号层面。

3. 格式问题
- `1236-1241` 与 `1419-1423` 两组 `## Review Questions` 重复。
- `1238` 行用了 `### 🤔 问题`，与其他文档的标题风格明显不一致，而且混入 emoji。
- `1234` 行写“`✅ 完整摘要`”，但 `1219` 行是“_暂无_”。
- `1245` 行又出现英文裸标题 `Extended Lagrangian Approach for SGN Equations`，与中文主标题重复。

4. 逻辑问题
- `1228-1230` 行称“推导出了...无条件双曲的近似系统，同时保持了色散精度”“仅需 800×800 网格即可达到...10000×10000 网格下的精度（约 156× 的网格效率提升）”。这里“保持色散精度”与“大幅效率提升”都需要严格限定测试问题、误差范数和参数范围，否则结论过强。
- `1232` 行把该方法外推到 “multiphysics 耦合时的数学模型选择”，方向合理，但距离论文原始贡献较远。
- `1381` 行说“不是任意 artificial compressibility，而是带有变分一致性的 hyperbolic approximation”，判断可能对，但需要更明确区分“变分来源”与“保真程度”，否则容易高估近似系统的结构保持性。

5. Review Questions
- 扩展拉格朗日系统声称“无条件双曲”，这一性质在离散层面是否仍成立，还是只对连续模型和特定参数区间成立？
- 对 SGN 这类色散系统，IMEX 的真正瓶颈是刚性源项、隐式椭圆耦合，还是高频色散模态与 shock-capturing 之间的不兼容？
- 若将 extended variables 作为神经算子的辅助状态，怎样证明它们确实提升了可学习性，而不是只是增加了状态维数和训练负担？

# ============ 批 B（文档 7-11）============

我先读取这份内联总文件并逐篇审查。
我继续读取后半部分，然后按 6 篇完整整理审查意见。
**文档1：`geometric-fluid/covector-fluids.md`**

1. 公式问题
- `59-60` 行说“`u` ... 变换律不是向量推前，而是 covector pullback”，但 `103-110` 行又写 `u(t)=\varphi_{t*}^{-1}u(0)` 与 `u^{*}(x)=DX(x)^T u^n(X(x))`。这里推前/拉回记号混用，建议统一成“`u(t)=(\varphi_t^{-1})^*u(0)`”或明确 `\varphi_{t*}^{-1}` 只是 pullback 的等价写法，否则读者容易误解。
- `74-80` 行把
  \[
  \mathcal L_v u=(v\cdot\nabla)v^\flat+d(\tfrac12|v|^2)
  \]
  代回后得到
  \[
  \partial_t u+\mathcal L_v u=-d\left(p-\frac12|v|^2\right)
  \]
  这一符号是自洽的，但 `191-192` 行再次给出同式时省去了前文“欧氏情形 `u_i=v_i`”的条件，容易让人误以为一般黎曼流形上也直接成立。
- `168-171` 行写
  \[
  \partial_t m+\operatorname{ad}_v^*m=0
  \]
  而前文主要变量是 `u`。这里 `m` 被称为 “one-form density”，但未说明与 `u` 的关系是 `m=u\otimes dV` 还是经 Leray 投影后的对偶变量，记号跳变过快。

2. 代码算法问题
- `133-143` 行把实现写成“先做 covector advection 得到 `u*`，升指标得 `v*`，再解 Poisson，最后 `u^{n+1}=(v^{n+1})^\flat`”。如果实际离散变量本来就是 edge/face one-form，自然的做法应是直接在 one-form 空间做 Hodge/Leray 投影。当前描述更像把几何变量又退回成普通速度场，算法层面少了“离散投影算子与 one-form 存储的匹配”。
- `232-234` 行提出 `advect_covector(field_u, backtrace_X, jacobian_DX)`，但没有说明 `DX` 如何离散计算、插值以及与 `X` 使用同阶精度保持一致。若 `X` 用高阶回溯而 `DX` 只用一阶差分，守恒改进可能明显退化。
- `232-234`、`244-245` 行都强调 AMR/Whitney 1-form，但正文没有交代在非欧氏/AMR 场景下 `\sharp/\flat`、Hodge star、Poisson 投影三者的离散兼容条件，这是该方法能否真正“无缝集成”的关键步骤。

3. 格式问题
- `41-45` 与 `242-246` 出现了两组 `## Review Questions`，重复。
- `39` 行写“`✅ 完整摘要`”，但 `24` 行摘要是“_暂无_”，前后矛盾。
- `49` 行再次出现裸标题 `Covector Fluids`，与文首 `# Covector Fluids` 重复，层级不整齐。
- `53` 行含大量英文/反引号术语，整体风格与前面中文“总结”部分不完全一致，但问题较轻。

4. 逻辑问题
- `34-35` 行称“显著改善...解决了传统流体模拟中的数值耗散问题”。“改善”有依据，但“解决”过满；该方法通常是缓解半拉格朗日速度平流带来的结构耗散，不等于全面解决数值耗散。
- `37` 行把方法直接外推到“HPC 流体求解器，改善高雷诺数流动的涡量守恒”，这个推断方向合理，但原文主要面向图形学不可压模拟，不宜直接上升为工程高 Re 求解器结论。
- `171` 行说“把最关键的 `ad*` 对流变换嵌进了廉价的 semi-Lagrangian step”，这句话抓住了思想，但略弱化了代价前提：需要高质量回溯映射及其 Jacobian，实际在复杂网格/AMR 上未必“廉价”。

5. Review Questions
- 若把 Covector Fluids 嵌入离散外微分/Hodge 框架，`DX^T` pullback 与离散 `d`、Hodge star 需要满足什么交换关系，才能真正保持 circulation 而不只是经验上更稳？
- 在 AMR 或曲线网格上，`u` 作为 one-form 的存储位置应如何选择，才能让 Poisson 投影、涡量诊断和 coarse-fine 同步保持一致？
- 该方法主要改善几何守恒而非能量守恒；若面向长期积分或高 Re 计算，是否需要再叠加 energy-preserving / symplectic 时间推进？

---

**文档2：`geometric-fluid/schrödingers-smoke.md`**

1. 公式问题
- `258` 行 DOI 写成 `[http:](https://doi.org/http:)`，明显错误；`297` 行后文才给出正确 DOI `10.1145/2897824.2925868`，元数据前后不一致。
- `306-307` 行写 `\Psi^\dagger\Psi=1`，`391-392` 行做点态归一化 `\Psi\leftarrow \Psi/|\Psi|`。如果这里的约束是逐点单位范数，应明确写成 `|\Psi(x)|=1`；当前写法既可被读成全局 `L^2` 归一化，也可被读成点态约束。
- `357-370` 行把总能量写为 `E_{\rm kin}+E_{\rm LL}`，但未说明这是精确等式、等价泛函，还是文中某种近似/重写。对熟悉 GP/LL 模型的读者，这里会关心是否缺少约束项或常数因子。

2. 代码算法问题
- `394-405` 行描述算法为“Schrödinger 步 -> 归一化 -> 投影”，但没有说明 projection 与 normalization 的先后次序是否可交换、为何这样分裂保持二阶或一阶精度。对 splitting 方法，这是关键算法细节。
- `407` 行说障碍物“通过 penalty 或 mask 处理”，但没有给出边界条件如何进入相位投影或 Helmholtz/Poisson 求解。对非周期域，这是方法可实现性的核心，不应一笔带过。
- `464-465` 行说周期域核心 kernel 是 FFT 等，`473-474` 行才提到非周期需换 solver；但正文没有交代若离开周期盒，Schrödinger 步本身如何高效离散，这会让“HPC 上实现此类方法需要高效 FFT 和 Poisson”显得过度乐观。

3. 格式问题
- `285-289` 与 `476-480` 两处 `## Review Questions` 重复。
- `282` 行写“`✅ 完整摘要`”，但 `266` 行仍是“_暂无_”。
- `293` 行再次出现裸标题 `Schrödinger's Smoke`，与文首重复。
- 文中英文术语、中文说明、反引号风格混合较多，整体可读性尚可，但风格不完全统一。

4. 逻辑问题
- `276-278` 行称“证明了不可压缩 Euler 流的涡动力学等价于 GP 方程在压力投影极限下的 Schrödinger 演化”“天然保持涡量守恒”“自动捕获涡旋重连”。这几句都偏强。尤其“自动捕获重连”与经典无黏 Euler 的涡线冻结并不相容，后文 `474` 行自己也提出了这个张力。
- `280` 行把方法上升为“量子-经典混合计算方法提供新思路”，这个外推过宽，原文主要是几何/图形学流体表示。
- `460` 行说“该步是酉的，保持 `L^2` 范数；归一化和投影再把状态拉回约束流形。这解释了算法稳定性的来源。”这解释过于简化；整体分裂并不因单步酉性就自动稳定。

5. Review Questions
- 该方法中的 `U(1)` gauge、点态单位范数约束与不可压投影之间，哪个才是真正承载流体几何结构的核心约束？
- 对非周期域和固壁边界，如何构造既保留 Berry connection 解释、又不破坏投影结构的离散 Schrödinger 步？
- 若把 `\Psi` 作为 AI4Physics 的学习变量，怎样处理 gauge 冗余，避免网络学到物理等价但数值不稳定的表示？

---

**文档3：`fluid-mechanics/spectral-analysis-of-nonlinear-flows.md`**

1. 公式问题
- `521` 行写“稀疏促销或优化型 DMD 变体”，应为“稀疏促进”或“sparsity-promoting DMD”，属于术语错误。
- `574-580` 行写
  \[
  \mathbf g(x)=\sum_j\varphi_j(x)\mathbf v_j,\qquad
  \mathbf g(T^t x_0)=\sum_j e^{\lambda_j t}\varphi_j(x_0)\mathbf v_j
  \]
  这是标准形式，但缺少对展开条件的限定，例如周期/准周期、解析可观测量或离散谱情形。当前写法太像无条件成立。
- `601` 行 `A=YX^+` 与 `613-625` 行 exact/projected DMD 公式并列给出，但没有说明 `\Phi_j=YV_r\Sigma_r^{-1}w_j` 对应 exact DMD，而非简单的 projected DMD，记号上略混。

2. 代码算法问题
- `585-640` 行给出标准 DMD 流程，但完全缺少 rank truncation `r` 的选择准则。对实际数据，`r` 的选取比公式本身更决定结果质量。
- `711-717` 行提到大规模 CFD 可改算 `C=X^*X, G=X^*Y` 或 randomized SVD，但没有讨论这些做法在噪声、非均匀内积、加权网格体积下如何修正，算法描述偏理想化。
- `719-722` 行提出 unitary/measure-preserving DMD、symplectic DMD，但正文前面没有说明标准 DMD 对不可压或 Hamiltonian 数据会产生什么具体伪谱污染，导致建议显得悬空。

3. 格式问题
- `517-521` 与 `729-733` 两组 `## Review Questions` 重复。
- `515` 行写“`✅ 完整摘要`”，但 `500` 行是“_暂无_”。
- `525` 行再次出现裸标题 `Spectral Analysis of Nonlinear Flows`，与开头重复。
- `488` 行中文题目，`525` 行英文题目，双标题并存但未分层说明。

4. 逻辑问题
- `510-511` 行说“相比传统 POD/DMD，该方法更好地捕获了非线性模态间的相互作用”。本文本质是在阐明 Koopman 模态观点与 DMD 的关系，把 “该方法” 与 “DMD”对立起来不准确，因为 DMD 正是其数值近似工具之一。
- `529` 行称“是 DMD 与 Koopman mode decomposition 关系的标志性论文”基本成立，但 `504-511` 行摘要部分把它说成“开发了一种新的谱分析框架”，容易让人误解为论文提出了一个全新可直接执行的算法，而非主要做统一解释和示例分析。
- `583-584` 行说“这正是 DMD 输出比 POD 更容易解释的原因”，表述略绝对。很多实际流动中 DMD 也会因噪声、非正态瞬态、采样窗口而难解释。

5. Review Questions
- 对连续谱或强非正态放大的流动，Koopman/DMD 分析应如何区分真实动力学结构与有限窗口、有限秩带来的谱污染？
- 若数据来自 AMR、非均匀网格或加权有限元离散，DMD 的内积和正交化步骤该怎样修改，才能让模态幅值具有物理意义？
- 在 AI4Physics 中，把 Koopman 线性化当作 latent prior 时，怎样避免模型只学到短时频率拟合而丢掉长期守恒和稳定性？

---

**文档4：`fluid-mechanics/粘弹性流体/the-log-conformation-formulation-for-single--and-multi-phase-axisymmetric-viscoe.md`**

1. 公式问题
- `832-835` 行写
  \[
  \nabla u=\Omega+B+NA^{-1},\qquad \Omega^T=-\Omega,\ B A = A B,\ N^T=-N
  \]
  这里分解记号较可疑。Fattal-Kupferman 的分解通常更精细，且 `N A^{-1}` 这一写法若不解释来源和维度，很容易让读者怀疑是否抄写错误或省略了关键定义。
- `838-840` 行给出
  \[
  \partial_t\Psi+u\cdot\nabla\Psi-(\Omega\Psi-\Psi\Omega)-2B
  =-\frac1\lambda e^{-\Psi}f_R(e^\Psi)
  \]
  但 `943-944` 行又写成
  \[
  D_t\Psi=\Omega\Psi-\Psi\Omega+2B-\frac1\lambda e^{-\Psi}f_R(e^\Psi)
  \]
  两处等价，但符号移项后的 presentation 不统一，建议明确一处为最终标准式。
- `818-819` 行 FENE-P 松弛项写成
  \[
  f_R(A)=\frac{A}{1-\operatorname{tr}(A)/L^2}-I
  \]
  若不补充分母正号约束与参数定义，容易让读者忽略 `\operatorname{tr}(A)<L^2` 的物理/数学前提。

2. 代码算法问题
- `958-959` 行说每个网格点需要 `3x3` 矩阵 `log/exp`、特征分解或封闭公式，但对轴对称无旋流结构，`A` 实际有 `2x2+1` 的特征结构可利用。正文没有把这一结构优化转化为明确算法建议。
- `960-963` 行提到 IMEX、BDF2、JFNK、AMR 插值，但没有说明 log-conformation 方程是如何与动量方程耦合离散的：显式对流/隐式松弛/全耦合 Newton 各自适用情形未区分。
- `962` 行说“更稳的做法是在 `\Psi` 空间插值，然后指数映射”，这是合理建议，但没有说明插值后如何保持对称、如何处理界面不连续系数对 `\Psi` 的非线性影响。

3. 格式问题
- `755` 行标题写成 `## Summary`，其余文档大多用中文 `## 总结`，风格不统一。
- `770-774` 与 `972-976` 两组 `## Review Questions` 重复。
- `768` 行写“`✅ 完整摘要`”，但 `753` 行仍是“_暂无_”。
- `778` 行再次出现裸标题 `Log-Conformation Formulation`，重复。

4. 逻辑问题
- `762-764` 行称“高Wi数（Wi>10）下保持数值稳定，远超传统方法上限”“不需要任何人工扩散或稳定化技术，数值稳定性的提升完全来自数学变换”，表述偏满。实际稳定性还依赖离散、时间推进、界面处理和边界条件。
- `821-827` 行把高 Wi 问题的核心归结为 “直接离散 `A` 可能失去正定”。这抓住了一部分，但 HWNP 不仅是正定性问题，也涉及应力边界层解析度、对流主导和离散误差累积。
- `964` 行建议神经网络预测 `\Psi` 优于 `A` 或 `\tau_p`，方向合理，但“可以把正定性作为硬约束，减少...非物理解”说得太顺；实际还要处理 objectivity/frame indifference，不只是 SPD。

5. Review Questions
- 在轴对称多相场景中，`log/exp` 变量变换解决了 SPD 问题，但是否同时保留了正确的离散自由能或应力功关系？
- 若采用 JFNK 全耦合求解，`u-p-\Psi` 三块之间最难预条件的耦合是压力 Schur 补、应力散度，还是局部矩阵函数线性化？
- 对 AI4Physics 而言，仅预测 `\Psi` 是否足够，还是还需要把 frame indifference、界面 jump 条件和 `u_r/r` 轴线结构显式编码进网络？

---

**文档5：`vortex-dynamics/incompressible-flow-simulation-on-vortex-segment-clouds.md`**

1. 公式问题
- `1069-1073` 行把 `\Gamma_i l_i` 直接写进 blob 形式
  \[
  \omega(x)\approx\sum_i \Gamma_i l_i\,\zeta_\epsilon(x-x_i)
  \]
  这里量纲和几何含义需要说明：`l_i` 是长度向量还是方向乘长度，`Γ_i` 是环量还是单位长度强度，否则与 `1078-1080` 的线积分式容易混淆。
- `1093-1099` 行有限直涡段速度公式写法较紧凑，但没有声明 `l_i=b_i-a_i`，而前文 `1066-1069` 只是说 `l_i` 是线段向量；若读者套用不同定义，符号容易误用。
- `1151-1155` 行把
  \[
  D_t\omega=(\nabla u)\omega
  \]
  直接说成 “这就是 Cauchy vorticity formula 的内容”，不够准确。这更像涡量拉伸方程；Cauchy 公式通常是通过流映射 Jacobian 写成显式表示。

2. 代码算法问题
- `1116-1123` 行提到黏性可用 particle strength exchange 思路，但紧接着又说“对涡段，需要同时处理强度、方向和 segment length 的一致性”，没有给出任何离散策略。这是算法空缺，不只是开放问题。
- `1125-1131` 行把 split/merge/reseeding 说成核心，但缺少触发准则、守恒约束和邻域搜索方式；而这些恰恰决定该方法是否比 vortex particle 更稳。
- `1183-1187` 行提出 GPU memory pool、BVH、vortex-in-cell 等实现路线，但没有区分哪种是论文实际采用、哪种是扩展建议，容易让审查对象边界不清。

3. 格式问题
- `1013-1017` 与 `1195-1199` 两组 `## Review Questions` 重复。
- `1011` 行写“`✅ 完整摘要`”，但 `996` 行是“_暂无_”。
- `1021` 行再次出现英文裸标题，和开头中文标题重复。
- `1183` 行出现英文句子 “carefully designed memory pool...”，与全中文叙述风格不统一。

4. 逻辑问题
- `1005-1007` 行称“涡量守恒和拓扑保持方面优于经典涡粒子方法”“计算效率接近粒子方法但精度更高”，这些判断需要非常具体的对比条件。不同 kernel、FMM、重采样策略下结论未必成立。
- `1006` 行说“成功模拟...涡管重联等复杂涡动力学过程”，若模型是无黏或弱物理黏性，重联更多是数值正则化与重采样共同作用的结果，不能直接当作物理真实性背书。
- `1131` 行说“因此能处理非闭合涡管重联和断裂”，这在图形学模拟意义上可以成立，但从流体力学建模角度应更谨慎区分“表示能力”和“物理解的可接受性”。

5. Review Questions
- 在 segment split/merge 过程中，最低限度应守恒哪些矩量或拓扑量，才能避免 reseeding 本身成为主要数值耗散源？
- 多 GPU 上若做 Biot-Savart/FMM，segment cloud 的动态负载均衡会不会比核函数求和本身更快成为瓶颈？
- 若把这种几何表示用于科研级涡动力学而非图形学，如何定量区分物理重联、正则化诱导重联和纯拓扑编辑？

---

**文档6：`wave-mechanics/extended-lagrangian-approach-for-the-numerical-study-of-multidimensional-dispers.md`**

1. 公式问题
- `1270-1277` 行给出的 1D SGN 动量式和 `\gamma` 表达是“常见形式”，但没有说明与论文具体记号是否完全一致。若这是综述性改写，最好明确，否则读者会以为是原文精确方程。
- `1309-1312` 行写扩展拉格朗日
  \[
  \mathcal L_\epsilon=\frac12h|u|^2-\frac12gh^2+\frac16hq^2-\frac1{2\epsilon^2}(q-D_th)^2
  \]
  这看起来是解释性模型，而不一定是论文精确形式。后文 `1314` 行也说“不同论文记号可能...”，说明这里更像概念示意，应更明确标注“示意形式”。
- `1372-1379` 行从
  \[
  \frac1{\epsilon^2}(q-D_th)
  \]
  推出
  \[
  q=D_th+O(\epsilon^2)
  \]
  这个量级结论需要更多条件，当前直接写出偏快。

2. 代码算法问题
- `1337-1349` 行只给出抽象 IMEX RK 模板，没有说明论文里隐式子步是局部求解、线性椭圆求解还是非线性耦合求解。对“可实现性审查”而言，这一步缺得比较关键。
- `1399-1410` 行多次提到 JFNK、multigrid、composite solve，但没有区分哪些是论文实际数值实现，哪些是你对 HPC 框架的外推建议。
- `1409-1410` 行提 AMR reflux 与隐式色散 level/composite solve 的耦合，这是很好的工程问题，但正文没有给出任何一致性策略，停留在口号层面。

3. 格式问题
- `1236-1241` 与 `1419-1423` 两组 `## Review Questions` 重复。
- `1238` 行用了 `### 🤔 问题`，与其他文档的标题风格明显不一致，而且混入 emoji。
- `1234` 行写“`✅ 完整摘要`”，但 `1219` 行是“_暂无_”。
- `1245` 行又出现英文裸标题 `Extended Lagrangian Approach for SGN Equations`，与中文主标题重复。

4. 逻辑问题
- `1228-1230` 行称“推导出了...无条件双曲的近似系统，同时保持了色散精度”“仅需 800×800 网格即可达到...10000×10000 网格下的精度（约 156× 的网格效率提升）”。这里“保持色散精度”与“大幅效率提升”都需要严格限定测试问题、误差范数和参数范围，否则结论过强。
- `1232` 行把该方法外推到 “multiphysics 耦合时的数学模型选择”，方向合理，但距离论文原始贡献较远。
- `1381` 行说“不是任意 artificial compressibility，而是带有变分一致性的 hyperbolic approximation”，判断可能对，但需要更明确区分“变分来源”与“保真程度”，否则容易高估近似系统的结构保持性。

5. Review Questions
- 扩展拉格朗日系统声称“无条件双曲”，这一性质在离散层面是否仍成立，还是只对连续模型和特定参数区间成立？
- 对 SGN 这类色散系统，IMEX 的真正瓶颈是刚性源项、隐式椭圆耦合，还是高频色散模态与 shock-capturing 之间的不兼容？
- 若将 extended variables 作为神经算子的辅助状态，怎样证明它们确实提升了可学习性，而不是只是增加了状态维数和训练负担？
我先读取第二批内联文件，再逐篇给出审查意见。
我先补读文档11后半段，再把 7 到 11 一次性整理完。
**文档7：`ai-for-physics/neural-operator-graph-kernel-network.md`**

1. 公式问题  
- `64-68` 的连续算子层写成带 `b(x)` 的积分表达，但正文没有说明 `b(x)` 是独立的 learnable function，还是已被吸收到 `P/Q` 映射中；当前写法会让参数化对象不清。  
- `82-89` 的离散层使用 `1/|N(i)|` 的邻域平均，而 `123-129` 又强调应考虑 quadrature weight / measure consistency。两处写法在非均匀采样下并不等价，容易让读者误以为简单平均天然保持离散化不变性。  
- `246-255` 把 learned kernel 类比 Green’s operator 是合理直觉，但对非线性 PDE 只能算启发性解释，不能被读成严格算子等价；这里表述略过满。

2. 代码算法问题  
- 文中没有交代图构造规则在跨分辨率泛化中的作用，例如 kNN、radius graph、动态重连各自对稳定性的影响。  
- 对非均匀点云/非结构网格，权重实现方式没有说清。若仍采用均匀邻域平均，算子近似会受采样密度偏置影响。  
- 复杂度讨论偏泛，只强调 message passing 比全局卷积便宜，但没有区分 edge MLP、kernel evaluation 和邻接存储带来的真实内存瓶颈。

3. 格式问题  
- `28-33` 与 `170-174` 出现两组 `Review Questions`，明显重复。  
- `37` 附近标题重复，版式上像是同一节被重新起头。  
- 整体中英文混排尚可，但结构上有“摘要/问题/再摘要”的重复感，影响审稿阅读流畅性。

4. 逻辑问题  
- `20` “比标准 CNN 和 FC 高一个数量级精度、快数百倍”说法偏满，缺少任务范围、分辨率、训练成本和 baseline 设置限定。  
- `24` “误差随数据量指数下降”表述过强。除非明确说明是在特定实验拟合区间，否则容易被理解为一般性统计结论。  
- `53-54` 附近把图表示说成“天然适合离散化不变性”也偏强；实践上是否不变，依赖图构造、权重归一与采样测度处理，并非自动成立。

5. Review Questions  
- 若训练点集是非均匀采样，`82-89` 的邻域平均如何与 `123-129` 的 quadrature-consistent 观点统一？是否需要显式测度权重或 lumped mass 修正？  
- 在 AMR / coarse-fine mesh 场景下，图连接跨层级时如何避免算子只学到插值伪影，而不是真正的跨分辨率 PDE 映射？  
- 如果目标 PDE 具有 Hamiltonian / 守恒结构，GKN 的 kernel parameterization 能否显式编码 skew-symmetry、energy conservation 或 Casimir 约束？

---

**文档8：`ai-for-physics/discovering-governing-equations-from-data-by-sparse-identification-of-nonlinear-.md`**

1. 公式问题  
- `246` 写 `\dot{X}=\Theta(X)\Xi` 是矩阵形式，而 `267` 写成 `\dot{x}_k=\Theta(x)\xi_k`，从批量矩阵到单样本符号切换过快，`X/x` 与 `\Xi/\xi_k` 的层次关系没有交代清楚。  
- `254` 的 `X^{P_2}, X^{P_3}` 记号不够标准，未说明它表示“所有二阶/三阶单项式库”，对首次接触 SINDy 的读者不够自明。  
- `272-288` 把 `\|\xi\|_0` 目标写得像是可直接优化的实际程序，但这通常只是理想稀疏目标；应明确实际求解常靠 sequential thresholded least squares、LASSO 或其变体近似。

2. 代码算法问题  
- 文中没有说明时间导数 `\dot{X}` 的估计方式。对含噪数据，有限差分、Savitzky-Golay、TV regularization 或 weak form 会直接改变识别质量。  
- 没提特征库列标准化/归一化，这在稀疏回归里通常是关键细节，否则阈值选择会被量纲主导。  
- 没说明阈值 `\lambda`、模型选择、交叉验证或 holdout 验证如何做，导致 pipeline 看起来“可复现”，但实际缺少最脆弱的一环。

3. 格式问题  
- `196-200` 与 `397-401` 两组 `Review Questions` 重复。  
- 长标题后正文中又重新引入一次论文标题，版式略冗余。  
- 章节层次基本清楚，但“精读推荐/价值判断”和正式技术总结混在一起，风格不够统一。

4. 逻辑问题  
- `188` “仅依赖少量观测数据即可准确重构控制方程”说法偏强；这依赖可观测性、激励丰富度、候选库完备性以及噪声水平。  
- `192` “高效、可解释地提取控制方程”总体成立，但对隐变量系统、强噪声系统或闭包缺失系统，应加条件。  
- `208` “必须精读”属于价值判断，不是技术错误，但会削弱正文作为中性审查材料的客观性。

5. Review Questions  
- 当数据来自数值离散而非真实连续系统时，SINDy 识别到的是“真方程”还是 modified equation？文中如何区分这两者？  
- 对守恒律主导的 PDE/流体问题，是否应把弱形式、积分量或通量项纳入候选库，而不是只用点值多项式库？  
- 若面向 AMR/GPU 大规模数据，候选库构造和稀疏回归的主要瓶颈在 I/O、导数估计，还是库矩阵 `\Theta(X)` 的形成与存储？

---

**文档9：`ai-for-physics/liepoisson-neural-networks-lpnets-data-based-computing-of-hamiltonian-systems-wi.md`**

1. 公式问题  
- `511-514` 刚体方程写成 `\dot{\Pi}=-I^{-1}\Pi\times\Pi`。它利用叉乘反对称性可与常见写法 `\dot{\Pi}=\Pi\times I^{-1}\Pi` 等价，但当前形式容易让读者误判符号，建议至少说明等价关系。  
- `470-478` 强调“学习保持 Poisson bracket 的离散映射”，但这里关键对象其实是 **Poisson map** 条件；如果不点明，容易把“保持 bracket 的映射”和“连续时间 bracket 结构”混为一谈。  
- `545` 的 `T_{\bar\alpha(\mu_n)}(h)\mu_n` 记号较突兀，`h` 在全文既像 Hamiltonian，又像步长变量，存在符号歧义。

2. 代码算法问题  
- 训练数据形态未说明清楚：是一阶一步映射对 `(z_n,z_{n+1})`，还是长轨迹窗口？这会直接影响 loss 与泛化解释。  
- 没交代不同 Lie algebra / Poisson 结构下网络层如何实例化；若结构依赖具体代数，代码可复用性并不像文字描述那样直接。  
- 文中承认能量只是“保持较好”而非严格守恒，但没有说明长期漂移如何评估、是否做多步 rollout 测试或 shadow Hamiltonian 分析。

3. 格式问题  
- `427-432` 与 `628-632` 两组 `Review Questions` 重复。  
- `436` 附近标题重复。  
- 全文英中术语混排还能接受，但“结构结论”和“经验结论”排版上没有拉开层次。

4. 逻辑问题  
- `419-423` 说网络“自动满足守恒律（如能量与 Casimir）”偏强。对 Lie-Poisson 结构，Casimir 往往可强保证，但能量一般要看离散映射是否同时是恰当积分器，不能一概而论。  
- `440` 附近又说“Casimir 机器精度守恒，能量保持较好”，这与前文“自动满足能量守恒”并不一致。  
- 若训练数据本身来自非结构保持积分器，文中没有讨论网络到底是在学习真实动力系统，还是学习带有数值耗散/色散误差的离散流。

5. Review Questions  
- 对非典范 Poisson bracket，变量选择是否决定了网络能否真正学到结构，而不是仅在某组坐标下拟合守恒量外观？  
- 若训练数据来自非结构保持求解器，LPNets 会把数值伪耗散也编码成“动力学规律”吗？作者如何分离这两者？  
- 与 splitting / variational integrator / discrete gradient 等几何积分器相比，LPNets 的优势究竟在未知模型学习，还是在已知结构下的高效 surrogate？

---

**文档10：`differential-geometry/force-free-fields-are-conformally-geodesic.md`**

1. 公式问题  
- `723-724` 的 `B^\flat=\star\beta` 在三维语境下可以成立，但正文没有说明这是依赖 Hodge star 把 `(n-1)`-form 映到 `1`-form，读者容易忽略维数前提。  
- `729` 把 `\iota_B d\star\beta=0` 与三维 `curl` 直观对应联系起来时，缺少“该对应依赖 metric + Hodge star”的说明；否则看起来像纯拓扑恒等式。  
- `764-765` 的共形变换写成 `\bar g=|\beta|_{\hat g}^2\hat g`，这个因子写法值得质疑。若结论依赖特定维数或归一化，当前文本没有交代，容易把构造误读成无条件通式。

2. 代码算法问题  
- “对 HPC/MHD 的启示”部分更多是扩展联想，不是论文原始算法；若要转成代码路径，缺少离散 field line topology、离散 Hodge star、约束保持推进的基本流程。  
- 提到 DEC / AMR / 几何残差等方向，但没有说明如何把“共形测地性”转成可计算 residual 或 solver objective。  
- 没讨论在离散网格上同时保持 `div-free`、拓扑结构与 force-free 条件时，约束冲突如何处理。

3. 格式问题  
- `648` 标注“_无可用内容_”，但 `663` 又写“✅ 完整摘要”，前后冲突。  
- `665-670` 与 `868-872` 两组 `Review Questions` 重复。  
- `674` 附近标题重复，版面组织不够干净。

4. 逻辑问题  
- `657` “证明了无力场等价于共形测地叶状结构”表述过满；从文脉看，结论应当需要非零场、闭 flux form、同一共形类等前提，不像无条件双向等价。  
- `661` “HPC-MHD 模拟可从中获益”可以成立，但正文没有给出足够具体的数值机制支撑，仍停留在几何启发层。  
- 若论文核心是几何表征，审查文本里把它进一步外推到“稳定求解器设计”时，需要明确这是推测性应用，而非原文已证明结果。

5. Review Questions  
- 若在离散外微分框架中实现本文几何结构，Hodge star 的共形变换如何稳定离散化，尤其在非正交/曲网格上？  
- 文中结构与 Beltrami field、Euler 稳态、磁力线测地性之间到底是哪种关系：等价、特例，还是仅共享几何语言？  
- 在实际 MHD 计算中，若 `div-free`、力平衡和拓扑保持不能同时严格满足，作者更优先保哪个约束，为什么？

---

**文档11：`quantum-computing/quantum-simulation-of-partial-differential-equations-via-schrödingerization.md`**

1. 公式问题  
- `926-995` 的主推导整体自洽，但 `1033-1052` 同一方程先写成 `\partial_t v-H\partial_p v=0`，随后又说“按符号约定写作” `\partial_t v+H\partial_p v=0`。如果只是因为把 `\partial_p v=-v` 代回后的符号重排，需要明确约定来源，否则像是中途换号。  
- `966-973` 将一般非 Hermitian 算子分解为 `A=H+i\bar H`，其中 `H=(A+A^\dagger)/2`、`\bar H=i(A^\dagger-A)/2`。这个分解本身没问题，但正文没有显式点出 `H,\bar H` 都是 Hermitian，读者要自己补一步。  
- `1017-1026` 说明量子输出是归一化态 `|u(t)\rangle`，因此只能直接得到“方向”而非原解范数；这实际上是方法的重要限制，但正文前面对“求解 PDE”表述过于直接，没有同步强调输出语义变化。

2. 代码算法问题  
- `1090-1103` 给了 `A \mapsto (H,\bar H) \mapsto H_{\text{total}}=H\otimes D+\bar H\otimes I` 的 matrix-free 接口思路，但没有讨论辅助 Fourier 维大小、截断误差和 aliasing 控制。  
- 对实际 PDE 离散，`H\otimes D` 往往意味着空间算子与频域批处理耦合；文中没有说明资源瓶颈更接近 FFT、batched sparse matvec，还是 Kronecker-structured apply。  
- `1017-1026` 已承认测量只能给归一化态与观测量，但算法部分没有展开如何恢复范数、如何做 observable estimation、复杂度是否被 readout 吃掉。

3. 格式问题  
- `886-904` 的“摘要/核心问题/方法/关键结果”明显过于空泛，像模板化占位语，没有真正反映这篇论文的技术内容。  
- `907-912` 与 `1110-1114` 前后两组 `Review Questions` 重复设置，结构冗余。  
- `904` 一边给出“完整摘要”语气，实际上摘要信息并不完整，和内容质量不匹配。

4. 逻辑问题  
- `893-900` 对论文贡献的概括太空，几乎没有把“warped phase transformation + auxiliary dimension lifting + Hermitian simulation”这些核心点说出来，导致读者无法从摘要判断论文新意。  
- `916-920` 说方法适用于 heat、transport、Fokker-Planck、Black-Scholes 等线性问题，这个判断方向正确，但没有同步强调其前提是**线性或先线性化后的系统**；否则容易被泛化到一般非线性 PDE。  
- `1080-1089` 把 Schrödingerization 外推到经典 HPC 的稳定时间推进与预条件启发，这种联想有价值，但属于作者性扩展，不应与论文已验证结果混为一体。

5. Review Questions  
- Schrödingerization 最终给出的是归一化量子态 `|u(t)\rangle`，而 CFD/HPC 常需要全场数值和绝对幅值；哪些 PDE 任务真正适合这种“状态方向优先”的输出模型？  
- 对带吸收边界、开放系统或非 Hermitian Schrödinger 方程，本文的 lifting 是否只是把困难转移到更高维 Hamiltonian 模拟，还是确实改善了稳定性与可测量性？  
- 若把 `H_{\text{total}}=H\otimes D+\bar H\otimes I` 当作经典 GPU 上的 matrix-free 算子，其性能瓶颈更接近 FFT、stencil 还是 batched sparse matvec，作者有没有给出可操作的复杂度模型？
