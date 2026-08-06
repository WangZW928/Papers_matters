### geometric-fluid/hamiltonian-structure-symmetries-and-conservation-laws-for-water-waves.md
- 公式问题:
  - `geometric-fluid/hamiltonian-structure-symmetries-and-conservation-laws-for-water-waves.md:77` 将“水平动量”写成“自由面变量中常写成 $\int \xi\nabla\eta\,dx$ 的等价形式”不够严谨。对 Zakharov 变量，常见水平动量写法应是标量/向量形式的
    $$
    P=\int \xi\,\eta_x\,dx \quad (1D), \qquad \mathbf P=\int \xi\,\nabla\eta\,dx \quad (多维),
    $$
    现文把 1D/多维混写，量纲和对象类型没交代清楚。
  - `:77` “由空间旋转、时间平移、Galilean 变换等产生的量”这一句偏大。对含重力的完整自由面水波，Galilean 不变性并不是这里最稳妥的表述，至少需要说明适用设定；否则容易把近似模型的对称性误投到完整问题上。
- 代码/算法问题:
  - `:85-86` “筛选保持方程、边界条件和 Hamiltonian 结构的对称群”表述过强。该文核心是结构与守恒律分析，不宜让读者误以为作者给出了可执行的“完整算法筛选流程”；建议审查时注意这段更像复述式算法，不是论文显式算法。
- 格式问题:
  - 无。
- 逻辑问题:
  - `:15-19` 摘要与结论都强调“无穷多个守恒律”“完整对称性分类”“可积性基础”，这对“完整自由边界水波问题”说得过满。若原论文并非严格证明 integrability 或“无穷多个独立守恒律”，这里有夸大风险。
  - 全文把“经典结构论文”讲成了“完整 Noether 分类 + 可积性路线图”，逻辑主轴略偏向后世总结，和题目本身可能不完全同幅。
- Review Questions 补充/修正:
  1. Zakharov 变量中的正则辛结构与 Eulerian 变量中的非正则 Lie-Poisson 结构如何对应？这种对应在含涡量或自由边界拓扑变化时会在哪里失效？
  2. 对 Dirichlet-Neumann 算子做离散近似时，保持自伴性、正定性与几何一致性三者之间是否存在不可兼得的张力？这会如何影响长期能量与动量诊断？
  3. 若把 Benjamin-Olver 的对称性分析推广到量子自由面或带相位缺陷的超流界面，守恒量生成机制会更接近 Noether、Casimir，还是约束流形上的约化动力学？

### fluid-mechanics/universal-anomalous-diffusion-of-quantized-vortices-in-ultraquantum-turbulence.md
- 公式问题:
  - `fluid-mechanics/universal-anomalous-diffusion-of-quantized-vortices-in-ultraquantum-turbulence.md:39-42` GPE 写成
    $$
    i\partial_t\psi=-\frac12\nabla^2\psi+\frac12(|\psi|^2-1)\psi
    $$
    这里非线性项前的 `1/2` 很可疑。更常见无量纲形式是
    $$
    i\partial_t\psi=-\frac12\nabla^2\psi+(|\psi|^2-1)\psi
    $$
    或等价缩放版本；若保留 `1/2`，需要说明时间/长度/化学势的具体归一化，否则容易误写。
  - `:47` 写 $\mathbf v_s=\nabla\theta$ 只在特定无量纲下成立。若前面又保留“有量纲环量为 $nh/m$”，这里最好说明已取 $\hbar/m=1$，否则符号体系不统一。
  - `:71` “论文报告的普适反常扩散区间，说明涡线输运不是简单 Brownian 随机游走”成立，但“普适”仅凭单个指数值仍偏强，应注明适用时间窗与统计区间。
- 代码/算法问题:
  - `:91` “相邻时间步做涡线点匹配，得到轨迹 $\mathbf s(t)$”在有重联时并不充分。这里缺少对“标记点在重联前后如何继续定义”的说明，否则 MSD 的对象到底是物质点、几何点还是重新参数化点会含糊。
  - `:93` 把“ballistic、反常扩散和长时普通扩散/有限尺寸效应”并列为流程步骤，但没有说明如何区分 crossover 与 finite-size artifact，算法描述略跳步。
- 格式问题:
  - `:53-55` 该行公式块末尾未以句号或解释句完整收束，紧接着下一段括注；可读性略差，但不算严重错误。
  - 文档主体用英文标题 `Abstract/Summary/Review Questions`，其余多为中文标题，风格不统一。
- 逻辑问题:
  - `:19` “超流体氦中量子化涡旋线的运动”与 `:36` “弱相互作用 Bose 凝聚体/GPE 模型”之间需要补一句“以 GPE 作为超流湍流的有效模型”。否则对象从原子 BEC 到 He II 容易被读成直接等同。
  - `:23` 把异常扩散直接归因于“重联事件和 Kelvin 波激发的共同作用”，如果论文只是证据支持而非严格因果分解，这里表述过实。
- Review Questions 补充/修正:
  1. 在重联频繁发生时，MSD 统计的“粒子”到底应定义为涡线上的物质标签、几何弧长参数点，还是事件间重新识别的拓扑特征点？不同定义会不会改变扩散指数？
  2. 若从 Hamiltonian/波湍流视角看，Kelvin 波级联、声辐射和重联各自对应哪些时间尺度，它们如何共同决定 $\alpha$ 的有效区间而非单一普适常数？
  3. 对大规模 HPC 量子湍流模拟，在线提取涡线拓扑图并做长时输运统计时，I/O、拓扑一致性和跨步匹配哪个才是主瓶颈？

### ai-for-physics/hamiltonian-neural-networks.md
- 公式问题:
  - `ai-for-physics/hamiltonian-neural-networks.md:71-72` 
    $$
    \frac{dH_\theta}{dt}=\nabla H_\theta^\top J\nabla H_\theta=0
    $$
    只对连续时间向量场成立；若数值积分器不是辛的，离散轨道上并不严格守恒。文中 `:75` 把这一点直接解释成“长期能量漂移被抑制”，需要加上“在连续模型层面”或“相较普通向量场学习更有利”。
  - `:61-66` 损失写成对整个状态导数做二范数平方没问题，但如果 $x=(q,p)$ 量纲不同，严格说通常需要归一化或加权；这里不是错，但过于理想化。
- 代码/算法问题:
  - `:81` “用数值差分或模拟器得到监督信号 $\dot x(t)$”遗漏了 HNN 实践中的关键限制：噪声数据下数值差分会非常脆弱。作为算法梳理，这里少了一句对导数监督依赖的风险说明。
  - `:86` “交给 ODE integrator”过于宽泛。若读者照此实现并用显式欧拉，前面强调的结构优势会被严重削弱。
- 格式问题:
  - 无。
- 逻辑问题:
  - `:14` 把“三体问题”列为 HNN 代表实验对象需谨慎；若原文实验集并不包含标准三体，这里属于事实风险。
  - `:52-77` 文档把 HNN 的理论收益写得较强，但对其假设边界交代不够：标准 HNN 依赖正则坐标、保守系统、可得导数监督。摘要和结论应更明确这一点。
- Review Questions 补充/修正:
  1. HNN 学到的是“连续 Hamiltonian 结构”还是“训练数据采样与积分器共同诱导的等效离散 Hamiltonian”？这两者在长时外推时如何区分？
  2. 对非正则流体/等离子体系统，直接学习 Poisson 张量 $J(x)$ 与先找 Darboux 坐标再学标量 Hamiltonian，哪条路线在数值稳定性和物理可解释性上更可行？
  3. 若把 HNN 接到 PDE 半离散系统中，能量守恒、Casimir 保持和网格加密一致性三者应优先保哪个？

### ai-for-physics/machine-learning-hidden-symmetries.md
- 公式问题:
  - `ai-for-physics/machine-learning-hidden-symmetries.md:44-46` asymmetry loss 写成
    $$
    \mathcal A(\theta)=\|\mathcal L_\xi T_\theta\|^2
    $$
    但 $\xi$ 本身若也是未知生成元，则这里不应只依赖 $\theta$。若论文同时优化变换和生成元，记号应写成 $\mathcal A(\theta,\xi)$ 或等价形式。
  - `:48` “$T_\theta$ 是把原对象通过 $y=f_\theta(x)$ 推前或拉回后的表达”是对的，但张量对象到底是 pushforward 还是 pullback 依其协变/逆变型而定；当前表述把两者并列，数学上略糊。
  - `:67-68` 写
    $$
    \dot y = J\nabla H(y)
    $$
    时默认正则常矩阵 $J$，但上一段刚讨论一般隐藏对称性；这里应强调只是 Hamiltonian 模板的一种特殊情形。
- 代码/算法问题:
  - `:75` “保证变换不会通过降维或折叠伪造对称性”说得太满。可逆性只能避免明显信息丢失，不保证不会制造数值上近似退化的“假对称”。
  - `:79` “回译到原变量中”在实践上并不自动成立，尤其当学到的是复杂神经坐标时，可解释性可能很弱。
- 格式问题:
  - 无。
- 逻辑问题:
  - `:13-17` 摘要声称“发现了先前未被注意的守恒量”，这是高风险表述；若原文主张是恢复隐藏对称或重参数化结构，而非真正发现新的物理守恒量，这里有夸张。
  - `:17` “不依赖先验物理知识”与正文 `:74` “先选结构模板”不一致。模板本身就是强先验。
- Review Questions 补充/修正:
  1. 当“隐藏对称性”是通过可逆神经变换显现出来时，怎样区分它是物理上有意义的约化坐标，还是只对训练分布局部成立的统计坐标？
  2. 对非正则 Hamiltonian 场论，应该把 asymmetry loss 作用在 Poisson 张量、Casimir 叶、约束分布，还是作用在轨道数据本身？
  3. 若把该方法用于 Clebsch 变量、涡量-流函数变量或量子相位变量的自动发现，边界条件与规范自由度应如何并入可逆学习框架？

### ai-model/denoising-diffusion-probabilistic-models.md
- 公式问题:
  - `ai-model/denoising-diffusion-probabilistic-models.md:95-99` 反向均值写成
    $$
    \mu_\theta(x_t,t)=\frac{1}{\sqrt{\alpha_t}}\left(
    x_t-\frac{\beta_t}{\sqrt{1-\bar{\alpha}_t}}\epsilon_\theta(x_t,t)
    \right)
    $$
    少了后验方差/均值公式中的一个系数背景说明。若按 Ho et al. 的常见参数化，这个式子本身可成立，但应明确是在“固定方差、由噪声参数化均值”的设定下，否则容易被当作完整后验均值。
  - `:145-147` “前向扩散过程在数学上等价于热方程 SDE 的离散化”表述过强。更准确地说，它在极限下对应 variance-preserving SDE / Ornstein-Uhlenbeck 型连续扩散，而不是字面上的空间热方程离散化。
- 代码/算法问题:
  - `:122-123` 采样伪代码里 `sigma_t` 未定义。对审查任务而言，这是明确的算法说明缺口。
  - `:127` “KL 项可转化为噪声预测误差”少了“在特定参数化与权重简化下”的限定，容易把 simplified objective 与完整 VLB 混为一谈。
- 格式问题:
  - 文档采用中文主标题与中文主体，但 `Review Questions` 用英文；风格不统一。
  - `:11` 写 `_暂无_`，与其他文档的 `_Not available_` 混用，整套文档风格不一致。
- 逻辑问题:
  - `:20-22` “实现了与 GAN 可比的高质量图像生成”可以，但若配合 `:21` “完整概率框架”一起看，摘要更像泛化总结，缺少该文真正贡献点：VLB + simplified objective + progressive lossy decompression/采样解释。
  - `:92` “学习 score/去噪方向”是对的，但全文没有提醒 DDPM 原文网络直接预测的是噪声，score 只是等价重写，容易让读者把 DDPM 与 score SDE 混成同一训练形式。
- Review Questions 补充/修正:
  1. DDPM 的 simplified loss 与完整变分下界在什么条件下近似等价、在什么条件下会偏离？这种偏离对物理场重建中的校准误差意味着什么？
  2. 如果把扩散变量换成受守恒约束的场变量，前向加噪是否还应保持各向同性高斯，还是应该改成与物理算子谱结构匹配的噪声过程？
  3. 对 HPC 场景，反向采样的主要成本到底来自网络评估、通信，还是物理 guidance；这会如何影响选择 DDPM、DDIM 或 consistency/distillation 路线？

### ai-for-physics/a-physics-informed-diffusion-model-for-high-fidelity-flow-field-reconstruction.md
- 公式问题:
  - `ai-for-physics/a-physics-informed-diffusion-model-for-high-fidelity-flow-field-reconstruction.md:85-90` 
    $$
    x_{t-1}\leftarrow x_{t-1}-\lambda_t\nabla_{x_t}\mathcal L_{\mathrm{phys}}(x_t)
    $$
    变量不一致：左边更新的是 $x_{t-1}$，右边梯度却对 $x_t$ 求导。这可能是“在 $x_t$ 上做 guidance 再进入下一步”，也可能是记号疏漏；需要统一成同一时层的更新变量。
  - `:76-80` 动量方程写成
    $$
    \partial_t\mathbf u+(\mathbf u\cdot\nabla)\mathbf u+\nabla p-\nu\nabla^2\mathbf u=0
    $$
    只适用于无外力、适当无量纲化、密度常数已吸收的不可压 NS。若作为“常见约束包括”，最好注明是示意式，不一定是论文具体残差。
  - `:64` $\mathcal L_{\mathrm{phys}}=\|\mathcal N(u_\theta)\|_2^2$ 过于抽象，没有指出残差是在空间点、批量样本还是整场积分上取范数；不是错误，但对“physics-informed”来说略空。
- 代码/算法问题:
  - `:113` “enforce observation consistency on known/low-fidelity components”没有说明是硬替换、投影、再加权损失还是 posterior sampling correction；算法关键步骤定义不够清楚。
  - `:118` “多轮注噪-去噪 refinement”若原论文并非核心机制，这里属于额外发挥，应谨慎。
- 格式问题:
  - 无明显 Markdown 配对错误。
- 逻辑问题:
  - `:15` “相比传统插值方法和纯数据驱动扩散模型提升约15%-20%”这种定量结论需要非常确信原文数值；若未逐表核实，风险高。
  - `:23` “训练时只使用高保真数据，推理时再用低保真或稀疏观测条件化，并可加入 PDE residual guidance”是一个很具体的方法框架；若原文训练中已经使用 paired/conditional 信息，这里会误导。
- Review Questions 补充/修正:
  1. PDE residual guidance 应被理解为后验修正还是生成先验的一部分？若 guidance 很强，它是否仍在采样同一个 learned distribution？
  2. 在不可压流体重建中，散度自由约束、边界条件一致性与观测匹配三者若冲突，推理阶段应该按什么优先级处理？
  3. 若扩展到三维湍流或量子涡场，条件变量应继续放在欧拉网格场上，还是改成谱系数、涡结构或拓扑特征，为什么？

### numerical-computation/amgx-a-library-for-gpu-accelerated-algebraic-multigrid-and-preconditioned-iterat.md
- 公式问题:
  - `numerical-computation/amgx-a-library-for-gpu-accelerated-algebraic-multigrid-and-preconditioned-iterat.md:85` 
    $$
    M^{-1}Ax=M^{-1}b
    $$
    只对应左预条件形式。既然正文讨论通用 Krylov/库设计，最好注明这是“例如左预条件”；否则容易让读者以为论文只讨论这一种。
  - `:74` “常见选择是 $R=P^\top$”对 classical/aggregation AMG 是常见，但严格说还取决于内积、尺度和问题类型；这里没错，但应避免暗示总是如此。
- 代码/算法问题:
  - `:112-113` V-cycle 伪代码里粗层求解后直接 `x_l = x_l + P_l e_{l+1}`，但前一步没有显式定义粗层误差变量 `e_{l+1}` 如何初始化/返回，伪代码略跳步。
  - `:120-123` GPU 设计点列得合理，但没有区分 setup 与 solve 的不同瓶颈，例如 coarse-grid setup、triple-matrix product、partitioning。作为工程论文审查，这一块略概括。
- 格式问题:
  - 主标题过长，直接把期刊信息塞进 `#` 标题，影响可读性。
  - 主体中 `Abstract/Summary` 与中文内容混用，风格不统一。
- 逻辑问题:
  - `:25` “单GPU上比CPU实现加速8-10倍，多GPU扩展良好”是具体性能结论，需谨慎；不同矩阵族与基线差异很大，这种摘要式数字若未核表容易过度概括。
  - `:88` 把 `K-cycle` 与整个库组件并列没有问题，但如果原文重点并不在全部 cycle 类型，这里会让读者误判覆盖范围。
- Review Questions 补充/修正:
  1. 在 GPU 上，AMG 的 setup 阶段与 solve 阶段哪个更容易成为端到端瓶颈？这一判断会如何改变非线性/瞬态求解器里的层级复用策略？
  2. 对高阶 PDE 离散，何时应把 AmgX 当作黑盒线性代数后端，何时必须暴露物理块结构、Schur 补或辅助空间信息给它？
  3. 多 GPU AMG 的最粗层往往并行度最低、通信最重。对 exascale 风格硬件，继续做更深层级是否总是有利，还是应提前切换到聚合粗求解或混合直接法？

### wave-mechanics/diffusion-equation-is-compatible-with-special-relativity.md
- 公式问题:
  - `wave-mechanics/diffusion-equation-is-compatible-with-special-relativity.md:48` 将 Fourier 模写成
    $$
    \omega=-iD|\mathbf k|^2
    $$
    依赖约定 $e^{i(\mathbf k\cdot x-\omega t)}$；本身没错，但若不说明符号约定，后文讨论 boost 下稳定性时容易混淆增长/衰减号。
  - `:56` 
    $$
    N^\mu(x)=\int p^\mu f(x,p)\,dP
    $$
    是标准粒子流形式，但若没有说明壳面约束与测度定义（如 $dP=d^3p/p^0$ 型），这里略显过于简写。
- 代码/算法问题:
  - `:77-79` “构造一个相对论相空间分布 $f$…验证其满足某个 Vlasov-Fokker-Planck 型方程”是论文证明主线的高层概括，但缺少关键约束：正性、归一化、局域性、平滑性。算法式表述过粗，容易低估证明难度。
- 格式问题:
  - `Journal: Physical Review Letters, 2026` 与 DOI `10.1103/rkz9-xps2` 看起来像占位或异常 DOI；至少元数据一致性可疑。
  - 文档使用 `Abstract/Summary` 英文标题，而主体多为中文，风格不统一。
- 逻辑问题:
  - `:23` “任意光滑局域解恰好是相对论 Vlasov-Fokker-Planck 方程的粒子密度解”是极强断言，建议核实“任意”“恰好”“精确解”这些词是否过满。
  - `:68-70` 从“存在因果稳定的动理论 lift”到“扩散方程与狭义相对论兼容”的结论需要限定“对可实现解类而言”。正文虽有暗示，但摘要与总结仍显绝对。
- Review Questions 补充/修正:
  1. 这篇工作的关键到底是在“修改扩散方程”，还是在“收缩可接受的解类与信号定义”？这两种立场对数值建模和物理解释有本质不同。
  2. 若一个宏观扩散解存在 relativistic kinetic lift，这个 lift 的非唯一性是否会影响熵产生、涨落统计或边界层行为？
  3. 对 Hamiltonian-耗散混合系统，是否可以把这种“微观因果、宏观抛物”的思路嵌入 GENERIC 或 kinetic-fluid 混合框架，而不是诉诸 Maxwell-Cattaneo 型双曲修正？

### numerical-computation/multigrid-for-matrix-free-high-order-finite-element-computations-on-graphics-pro.md
- 公式问题:
  - `numerical-computation/multigrid-for-matrix-free-high-order-finite-element-computations-on-graphics-pro.md:24` 写“复杂度从 `O(p^6)` 降至 `O(p^4)`”默认是三维情形；而 `:67-74` 又给出一般维数 `O(p^{2d})` 到 `O(dp^{d+1})`。建议统一说明“在 3D 时即为 `O(p^6)\to O(p^4)`”，否则上下文略跳。
  - `:55-62` 单元公式中的记号 $(A_K u)_i$、$J_K(x_q)$、$C(x_q)$、$c(x_q)$ 都是合理的，但没有说明是在标量椭圆型双线性型背景下，容易被误读成通用高阶 FEM 公式。
- 代码/算法问题:
  - `:98-105` matrix-free apply 伪代码里 `scatter-add local result` 在 GPU 上往往是关键难点之一，特别是连续 Galerkin 下写回冲突；这里只一句带过，低估了实现复杂度。
  - `:114` 平滑器只写 “Jacobi/Chebyshev-type” 合理，但若论文对 smoother 选择有更具体结论，这里应更明确，否则算法层重点偏淡。
- 格式问题:
  - `:145-147` `Review Questions` 中每条都带 `**Q:**`，而其他文档没有，整套输出风格不统一。
  - 标题和元数据为中文，但 `Review Questions` 用英文标题，风格不统一。
- 逻辑问题:
  - `:25` “实现了近线性复杂度”是较强结论。对高阶 GPU FEM，更稳妥的说法通常是“接近最优复杂度/良好可扩展性”；如果原文没有严格 complexity claim，这里略夸张。
  - `:91` 把 `p`-multigrid 与 `h`-multigrid 组合讲成通用途径是合理的，但若原文更偏某一类 hierarchy，当前总结略泛化。
- Review Questions 补充/修正:
  1. sum-factorization 提高的是算子求值效率，但多重网格收敛性取决于层间误差传播；在 GPU 上这两者何时会相互冲突？
  2. 对连续高阶 FEM，matrix-free kernel 的瓶颈究竟在单元内张量操作、面通量、还是全局 scatter/gather？不同离散类型下最优线程映射是否应不同？
  3. 若 Doctor 的框架同时支持高阶 Hamiltonian 波动问题和黏性流动问题，是否应共享同一套 matrix-free multigrid 基础设施，还是按算子谱性质拆成两类预条件路线？