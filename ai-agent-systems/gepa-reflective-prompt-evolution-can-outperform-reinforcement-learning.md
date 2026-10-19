# GEPA: Reflective Prompt Evolution Can Outperform Reinforcement Learning

_精读笔记｜arXiv:2507.19457v2｜ICLR 2026 Oral｜PDF 96 页；精读主文方法与 6-task evaluation（pp. 1–14），并抽查代码优化实验（§5.1，pp. 12–13）；长示例 prompt 附录未逐页复述_

---

## 书目信息与问题

- **作者：** Lakshya A. Agrawal、Shangyin Tan、Dilara Soylu、Noah Ziems、Rishi Khare 等
- **来源：** [arXiv:2507.19457v2](https://arxiv.org/abs/2507.19457v2)[^1]；[GEPA 代码](https://github.com/gepa-ai/gepa)
- **问题：** RL 优化常将长轨迹压缩成 scalar reward；但 agent 的工具调用、错误信息和中间输出本身是可读的密集监督。能否直接通过自然语言反思进化 prompt，并减少 rollout 开销？
- **阅读范围：** compound AI system/prompt 表示、Reflective Prompt Mutation、Pareto candidate selection、6 个任务的 Qwen3 8B 与 GPT-4.1 Mini 结果，以及 code optimization case。

## 方法与机制

GEPA 固定底层模型权重，优化复合 LLM 系统各模块的 prompts。每轮选 parent 和目标模块，运行小批量样本，收集模块输入输出、轨迹、分数及可用文本反馈；反思模型提出 prompt 变体，在同一小批量上改善后加入候选池，再在独立的选择集 Dpareto 上评分。最终返回选择集平均分最高者；该选择集不是最终测试集（§§2–3，Algorithms 1–2，PDF pp. 4–6）。

Algorithm 2 先取“至少在一个实例上并列最高分”的候选并集，去除被支配者，再按领先实例数加权抽样。这里的维度是**实例得分**，不是延迟、显存等工程目标；该规则也不保留所有一般意义的 Pareto 非支配点。可选 Merge 将不同谱系的模块 prompt 组合，收益取决于预算分配与谱系互补性（§3.1、§4，pp. 7–11）。

## 原文证据与结果

- **六任务主结果：** Qwen3-8B 的 aggregate score：baseline 45.23、GRPO 48.91、GEPA 54.85；相对 GRPO 增加 **5.94 个百分点**。AIME-2025 上 GEPA 32.00 低于 GRPO 38.00。Table 1 的 **3,936** 是各任务优化 rollout 预算的平均量级，不是六任务合计；表内六项预算合计 23,619（PDF p. 8）。
- **样本效率：** IFBench 用 678 rollouts 达到 38.61，对照 GRPO 为 35.88、预算 24,000；约 35× 是此任务比较，不是所有任务的平均。Rollout 次数也不等于 token、反思调用或美元成本（Table 1、Appendix E.3）。
- **选择策略与 Merge：** 固定进化流程的四任务消融中，GEPA 平均 61.28，greedy 为 54.89、beam 为 53.95，支持实例覆盖式选择的价值。Merge 在 Qwen3-8B 的六任务平均从 54.85 降至 52.40，在 GPT-4.1 Mini 则从 65.22 升至 66.36，不能写作稳定附加收益（Tables 1–3，pp. 8–10）。
- **代码搜索：** GPT-4o/Sequential5 在 V100 上优化 KernelBench 的 35 个代表任务，fast1 超过 20%。这里把待解决任务本身放入 Dtrain 与 Dpareto，属于有意针对目标实例的推理时搜索，不是未见 kernel 的泛化实验；NPU 实验的 vector utilization 也不能与 CUDA speedup 混为一个指标（§5.1、Figs. 7–8，pp. 12–13）。

## 评议、限制与迁移

- **贡献本质：** 将执行/评估轨迹作为 prompt 修改的诊断信号，并通过实例级强项保留互补候选。固定进化流程的选择策略消融是较直接的机制证据；仅凭结果优于某个 GRPO 配置，不能推出 prompt 搜索普遍替代权重训练。
- **审阅判断：** 不同优化空间的可达解、反思模型成本和验证集调用方式不同，需要同时比较预算、最终性能与服务开销。反复使用 Dpareto 会产生选择过拟合风险；论文六任务的标准 train/validation/test 结果与目标实例代码搜索应分开解读。Merge 的模型依赖性说明并非增加组件就必然获益。
- **对 SCALE_Forge 的启示（待验证）：** 将编译和数值失败转为可定位的反思反馈，并用独立输入复验候选。若引入 latency/memory 多目标 archive，那是对 GEPA 实例得分选择的扩展，应明确额外的接受准则；不要把原算法直接称为完整工程 Pareto 优化器。

## Review Questions

1. 统一计入反思、验证、训练和最终服务 token 后，GEPA 与 GRPO 的成本—效果结论如何变化？
2. 实例冠军抽样相对完整非支配集合，在任务得分噪声较大时会丢失哪些候选？
3. 在未参与搜索的 kernel、输入形状和硬件上，反思所得指令还能保留多少收益？

## 价值评估

**阅读价值：高，建议 Tier 2（Agent 优化方法分支）。** 对反思反馈与预算化候选搜索有参考；不应把 prompt 结果直接当成 GPU kernel 的 correctness/performance 证据。

**流程状态：** 2026-10-19 核查 v2 Algorithms 1–2、Tables 1–3 与 §5.1；修正预算聚合及实例级 Pareto 语义。未复现实验。

[^1]: Agrawal et al. (2025). “GEPA: Reflective Prompt Evolution Can Outperform Reinforcement Learning.” ICLR 2026 Oral; arXiv:2507.19457v2. https://arxiv.org/abs/2507.19457v2
