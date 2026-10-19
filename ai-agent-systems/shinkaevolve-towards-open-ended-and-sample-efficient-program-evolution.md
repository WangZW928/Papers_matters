# ShinkaEvolve: Towards Open-Ended and Sample-Efficient Program Evolution

_精读笔记｜arXiv:2509.19349v1｜PDF 52 页；重点阅读主文 §§3–4.4（pp. 1–11）及 circle-packing、AIME、ALE-Bench、MoE loss 结果；另核对附录 C.4 损失实现_

---

## 书目信息与问题

- **作者：** Robert Tjarko Lange、Yuki Imajuku、Edoardo Cetin，Sakana AI
- **来源：** [arXiv:2509.19349v1](https://arxiv.org/abs/2509.19349v1)[^1]；[ShinkaEvolve 开源实现](https://github.com/SakanaAI/ShinkaEvolve)
- **问题：** LLM 驱动的程序进化会耗费大量候选评估，且单一模型、父代或解空间可能造成低效/同质化。如何让 open-ended program evolution 更省 sample，并保留跨任务可用性？
- **阅读范围：** 父代采样、程序 novelty rejection、LLM ensemble bandit、运行反馈/多目标 archive，以及四类实验。

## 方法与机制

ShinkaEvolve 保存固定容量的程序档案，并在 island 子群间迁移部分程序。一次 mutation 的上下文包括 parent、高分和随机 inspiration；候选可由 diff、整段重写或 crossover 产生，受不可修改代码块约束（§§3.1–3.2，pp.3–4）。三个主要机制是：

1. **Parent sampling：** weighted 规则将中位 fitness 附近的 sigmoid 权重与 `1/(1+offspring数)` 相乘；这里的 novelty 实际是较少被扩展，区别于代码语义新颖性。power-law 是另一可选策略。
2. **Novelty rejection：** 对可修改代码做 embedding；与子群程序的最大余弦相似度超过阈值（示例 0.95）后，再让 LLM 判断是否有实质变化。该判断是启发式筛选，不是语义等价验证。
3. **LLM ensemble bandit：** 基于 UCB1，奖励相对 parent 与初始程序中较好者的 fitness 增量，并以截断指数变换偏向较大改进；未直接按 API 或执行成本归一化（§3.3，p.5）。

执行器返回 scalar fitness、public metrics 与文本反馈；周期性 meta-scratchpad 汇总近期经验并进入后续提示。多指标进入上下文不意味着所有选择都按 Pareto 支配关系执行。

## 原文证据与结果

- **圆填充：** 26 圆单位正方形问题，在约 **150 次已评估程序提案**内超越所比 AlphaEvolve 构造（Fig. 5，p.6）。这不包括所有补丁重采样、embedding 和 novelty-judge 调用，也未对齐 AlphaEvolve 的模型和总算力，不能写成同预算下的普遍优势。
- **AIME：** 用 GPT-4.1-nano 在 AIME 2024 的 30 题上搜索 75 generations，每候选评估 3 次、每题最多 10 次调用；发现 3 个专家、3 次复核和 1 次汇总的 7-call scaffold。Fig. 6 中其 2024/2023 成绩高于 Majority@5，但 **2025 为 20.0%，低于 Majority@5 的 25.6%**（§4.2，p.7）。因此存在跨年迁移证据，不能声称全面优于投票；题目是否进入训练集也未独立验证。
- **ALE-Bench：** 从 ALE-Agent 最佳初解继续搜索 50 generations，public fitness 选择后测 private；Fig. 7 的 public Top-1 对应均分 **1879.3→1923.5**，约 **2.35%**。图中另列 Top-5 和 Max Private，后者不能与仅按 public 选解的部署口径混用（§4.3，p.8）。
- **MoE：** 在 556M 参数、64 专家/top-8、约 2B tokens 的模型上搜索 30 次，将 CE 与负载不均衡合为 fitness；再在 2.7B、近 30B tokens、三种正则系数上验证（§4.4，p.9）。已做规模迁移，但模型架构相近，不能说尚无规模实验，也不能外推到任意 MoE。
- **公式与代码冲突：** Eq. 1 用熵权重乘专家最低使用率缺口，阈值写 **`0.064/N_E`**（p.10）；附录 C.4 却写 **`0.01*(64/N_E)=0.64/N_E`**，相差 10 倍（p.52）。代码用 hard indices 的 `one_hot` 计算频率；按所列实现，缺口项本身不对选中频率求导，新增项的可微路径来自熵权重。应澄清实验实际版本，不能仅凭示意梯度宣称直接提升每个冷门专家的路由概率。

## 评议、限制与迁移

- **贡献定位：** 组合父代扩展、多样性筛选与模型调度，减少昂贵评估中的重复候选；它搜索人定义目标下的程序，并未实现自主生成目标的 open-endedness，后者被列为未来工作（§6，p.11）。
- **消融范围：** Fig. 9 是圆填充实验，不能据此推出 weighted sampling 在四个领域都优越。图注称 bandit 相对均匀 ensemble “略有改善”，正文称显著优于；未见对应统计检验，不把修辞上的显著当统计结论（pp.10–11）。
- **评估与发现分开：** 更少程序评估不等于更少总成本；AIME 搜索集反复使用、ALE 初解限制探索和 MoE 代理目标都影响结果。应分别核验提出的构造、留出迁移和搜索流程贡献，而非以最佳案例支撑通用科学发现能力。
- **对 SCALE_Forge 的启示：** 同时记录有效评估数、拒绝候选数、模型/API 成本与执行时间；让 novelty 筛选具有可恢复机制，并独立测试其误拒率。bandit 可加入成本与延迟，但这是迁移建议，不是论文已有实现。

## Review Questions

1. 将拒绝提案、辅助模型调用与程序运行都计费后，novelty filter 是否仍提高单位成本的发现率？
2. 在其他任务和多随机种子下，bandit 相对均匀模型混合的优势能否重复？
3. MoE 实验实际使用哪一个阈值，hard routing 下新增项的梯度路径与论文解释是否一致？

## 价值评估

**阅读价值：高，建议 Tier 2（开放式程序搜索方法）。** 对预算化进化搜索、采样多样性和模型路由有启发；每个案例的 scientific merit 仍由任务级 oracle 决定。

**流程状态：** 已按原文复核（2026-10-19），包括损失公式与附录实现；未复现实验。

[^1]: Lange, Imajuku, and Cetin (2025). “ShinkaEvolve: Towards Open-Ended and Sample-Efficient Program Evolution.” arXiv:2509.19349v1. https://arxiv.org/abs/2509.19349v1
