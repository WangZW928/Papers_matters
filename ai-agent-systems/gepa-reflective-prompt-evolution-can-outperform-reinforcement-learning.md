# GEPA: Reflective Prompt Evolution Can Outperform Reinforcement Learning

_精读笔记｜arXiv:2507.19457v2｜ICLR 2026 Oral｜PDF 96 页；精读主文方法与 6-task evaluation（pp. 1–14），并抽查代码优化实验（§5.1，pp. 12–13）；长示例 prompt 附录未逐页复述_

---

## 📌 书目信息与问题

- **作者：** Lakshya A. Agrawal、Shangyin Tan、Dilara Soylu、Noah Ziems、Rishi Khare 等
- **来源：** [arXiv:2507.19457](https://arxiv.org/abs/2507.19457v2)；[GEPA 代码](https://github.com/gepa-ai/gepa)
- **问题：** RL 优化常将长轨迹压缩成 scalar reward；但 agent 的工具调用、错误信息和中间输出本身是可读的密集监督。能否直接通过自然语言反思进化 prompt，并减少 rollout 开销？
- **阅读范围：** compound AI system/prompt 表示、Reflective Prompt Mutation、Pareto candidate selection、6 个任务的 Qwen3 8B 与 GPT-4.1 Mini 结果，以及 code optimization case。

## ⚙️ 方法与机制

GEPA 将系统表示为多个 LLM module、控制流和输入输出 schema。一般优化问题允许 prompt 与权重作为参数，但 GEPA 算法固定模型权重、只更新 prompts（§2–3，pp. 3–4）。每轮从候选 pool 选 parent 与目标 module，抽取 minibatch 执行以收集成绩、trajectory 与可用 textual feedback，reflector 据此诊断失败并提出 prompt 更新。更新先在 minibatch 验证，改善才进入候选池，再对 Pareto/evaluation set 评分（§3，pp. 4–7）。文本反馈/人工解释在可用时有帮助，但不是原文证明的算法必要条件。

选择不是只突变当前总分最高者：Algorithm 2 先取每个 task instance 得分最高候选的并集，再剔除支配候选，按候选领先的实例数加权采样（p. 6）。这有助于保留部分互补策略，但不等同于保留全部数学意义上的非支配折中点；无任何单项最高分的折中候选可能不会入选。可选 System-Aware Merge 将不同 candidate 中有效的模块 prompt 组合（图 3，p. 5）。更可解释的反馈可能有利于反思，但不是算法成立的必要条件；错误 evaluator 会诱导错误优化属于本文之外的风险推论。

## 📊 原文证据与结果

- **6 个任务 / Qwen3 8B：** HotpotQA、IFBench、Hover、PUPA、AIME-2025、LiveBench-Math。Table 1 中 GEPA aggregate score 54.85，相对 baseline 45.23 为 **+9.62 个百分点**；GRPO aggregate 48.91，因此 GEPA 相对 GRPO 是 **+5.94 个百分点**（相对增幅约 12.1%）。GEPA 的 **3,936** 是表中总优化 rollout budget 的汇总值，并非达到最优性能的平均消耗；AIME-2025 上 GEPA 32.00 低于 GRPO 38.00（Table 1，p. 8）。
- **样本效率与代码搜索：** IFBench 上 GEPA 用 678 rollouts 达 38.61，GRPO test score 为 35.88、预算 24,000；摘要“平均 outperform GRPO 约 6%”对应约 6 个百分点而非相对增幅，最多 **35×** 更少 rollout 是任务级，不应写成平均节省 35×（摘要、§4，pp. 1、8）。CUDA 搜索实验使用 KernelBench 的 35 个代表任务、GPT-4o、V100 和 Sequential5；作者报告其中超过 20% 任务生成了比 PyTorch Eager 更快的 kernel（§5.1，pp. 12–13）。训练/Pareto 集包含待解决任务以允许对这些任务优化，因此该实验说明特定推理时搜索可行性，不验证未见 kernel/硬件的泛化。
- **不同模型与优化器：** 论文还报告 GPT-4.1 Mini、MIPROv2 比较；AIME-2025 上 GEPA 相对 MIPROv2 的提升是特定表格设置下的结果。评估中候选 prompt、rollout 预算和拆分策略会影响表现，需按具体表格解释（§4，pp. 8–10）。
- **GPU kernel 优化：** 作者展示把 GEPA 用于 CUDA code prompt/search 的可行性，定位为 promising inference-time search strategy；不是 KernelBench 全套硬件 kernel 排名，也不是与人工优化器的普遍比较（附录示例）。

## 🔍 评议、限制与迁移

- **贡献本质：** 用自然语言轨迹反思提取可操作规则，再以 Pareto pool 做多目标候选保留；文本不仅是提示内容，也是优化器可消费的中间监督。
- **限制：** 可解释反馈可能利于 prompt 反思，但错误 evaluator 诱导偏移是合理风险推论，不是本文直接实验结论。实例冠军筛选不等同于完整 Pareto-front 维护。多任务评测可能存在对参与搜索任务的过拟合；模型、prompt、预算与任务难度不同，数字不可横比。论文摘要中的平均值与个别任务反例必须一并读。
- **对 SCALE_Forge 的启示：** 将编译错误、正确性 counterexample、profile bottleneck 变成结构化上下文与可读反馈；候选优化策略应按多个 workload 的 Pareto frontier 保存。仅对候选 diff 做小预算筛选，进入全量/真实硬件评测后才更新 archive，且明确分开 rollouts、compile runs 与 device measurements。

## Review Questions

1. GPU 反馈中哪些字段对 Reflector 是“密集且可解释”的：错误栈、数值误差、访存效率还是瓶颈标签？
2. 将 optimizer 的 prompt 反思换成可验证的策略 DSL，能否保留 GEPA 的样本效率又提高变换可审计性？
3. 多个 workload 的 Pareto front 应按 correctness、latency、资源/编译成本中的哪些目标构造？

## 价值评估

**六维参考（1–6）：** idea 清晰 5；可验证性 4；迁移价值 4；领域重要性 4；方法创新 5；影响力 5。**阅读价值：高，建议 Tier 2（Agent 优化方法分支）。** 对反思反馈与预算化候选搜索有参考；不应把 prompt 结果直接当成 GPU kernel 的 correctness/performance 证据。

**流程状态：** 元数据、原文、评估、精读、索引、审阅：完成（独立 Codex 只读审阅；未完成 Kimi 复核）；提交：跳过（未请求）。

[^1]: Agrawal et al. (2025). “GEPA: Reflective Prompt Evolution Can Outperform Reinforcement Learning.” ICLR 2026 Oral; arXiv:2507.19457v2. https://arxiv.org/abs/2507.19457v2
