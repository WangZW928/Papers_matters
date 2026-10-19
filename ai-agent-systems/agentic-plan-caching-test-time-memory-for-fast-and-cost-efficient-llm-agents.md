# Agentic Plan Caching: Test-Time Memory for Fast and Cost-Efficient LLM Agents

_精读笔记｜arXiv:2506.14852v2｜全文 27 页；重点阅读方法 §§3–4、五类 workload 结果与 Appendix B–D 的实验/案例说明_

---

## 书目信息与问题

- **作者：** Qizheng Zhang、Michael Wornow、Gerry Wan、Kunle Olukotun
- **来源：** [arXiv:2506.14852v2](https://arxiv.org/abs/2506.14852v2)[^1]
- **问题：** Plan-Act agent 的多轮 planning 会反复支付昂贵 LLM 推理成本；传统 KV/context cache 缓存 token 前缀，semantic cache 常缓存最终回答，但对依赖外部数据和环境变化的 agent 容易复用错误答案。能否复用“做事计划”而让其适配新任务上下文？
- **阅读范围：** 系统流程与 cache 生成/命中、与 semantic/full-history caching 对比、五个 agent workload、成本/延迟/匹配阈值分析及扩展实验。

## 方法与机制

正文要求仅从正确完成的 cache-miss 执行中生成可复用 **plan template**，存成 `(keyword, template)`。新任务先由轻量模型提取概括意图的 keyword，再查询 cache：命中时小 planner 将模板适配到当次任务的公司、年份等动态 context；未命中则由大 planner 正常生成计划。Actor 在当前环境执行，Planner 根据 response 判断是否继续（§3.1，PDF pp. 4–5）。正文未充分说明在线如何判定“正确完成”；所给 Algorithm 3 也未显式展示正确性验证，因此这是系统描述中的要求，不应视为已证明的 cache correctness guarantee。

复用对象是去除实体与具体数值的计划模板；Actor 仍在当前数据/环境执行。默认关键词精确匹配，模糊匹配是单独实验。Full-History 对照改变了上下文长度、过滤方式和表示，因此结果支持模板化整体方案，尚不能单独归因于小模型“理解长历史能力不足”（§3.2、§4.2，pp. 5–7）。

## 原文证据与结果

- **评估任务与指标：** FinanceBench、QASPER、TabMWP、AIME 2024/2025、GAIA；主配置为 GPT-4o planner、Llama-3.1-8B small planner/actor、GPT-4o-mini 模板过滤。应用质量由 GPT-4o judge 评定，成本按当时 API token 价格计算；“accuracy-optimal”只是始终调用大 planner 的对照名，不是理论上界（§4.1，pp. 6–8）。
- **作者报告的总体结果：** 摘要/结论报告 APC 平均成本降低 **50.31%**、application-level performance 保留 **96.61%**（摘要、§4.2，pp. 1、7；Table 9，p. 25）。原文没有清楚给出跨数据集、模型和配置的聚合权重；这里保留为作者报告值，不作为本次独立重算结果。96.61% 是相对性能保留，不是绝对准确率。
- **延迟证据范围：** **27.28%** 延迟下降来自 FinanceBench 随机抽取 100 题、命中率 46% 的实验（§4.3，p. 8；Table 3，p. 9），不是五类 workload 的跨任务平均。该表总延迟 1959.24 秒降至 1424.82 秒，按此相对降幅约 27.28%。
- **命中质量与开销：** semantic caching 在较低相似阈值下会 false-positive hit；APC hit/miss accuracy 在报告实验中较接近，但这不构成 correctness guarantee。Table 1 显示 APC 位于 accuracy-optimal 与 cost-optimal 两端之间（§4.2，pp. 7–8）。**1.04%** cache 开销是 FinanceBench 与 TabMWP 的表列开销率 1.15%、0.93% 的算术平均（Table 2，p. 9），不能代表全部 workload。
- **阈值与扩展代价：** keyword 模糊匹配阈值从 100% 降至 >60% 时，表中 hit rate 由 46% 升至 64%，成本由 $1.86 降至 $0.93，但 accuracy 从 85.50% 降到 77.00%；1M 条 cache 下 fuzzy lookup 延迟约 148 ms，而 exact lookup 约 56 μs（§4.4，p. 10）。这是特定实现和阈值配置，提示大 cache fuzzy search 的吞吐瓶颈。

## 评议、限制与迁移

- **贡献本质：** 把案例式计划复用实现为 LLM serving 中的大/小 planner 路由，命中后重新适配与执行，避免直接复用过期答案。创新主要在自动抽象和部署机制，计划复用思想本身与 case-based planning 有明确联系（§2.3，p. 4）。
- **审阅判断：** 准确率与费用的折中受到任务重复度、到达顺序、冷启动和模型组合共同影响；降低阈值会同时提高命中率并降低准确率，不能只优化 hit rate。GPT-4o 同时作为大 planner 和质量 judge，需用独立判定器复查偏差。缓存写入依赖“正确完成”的前提，却没有足够明确的线上成功判定；部署前应检验错误模板传播与失效策略（§§3–4，pp. 5–10）。
- **对 SCALE_Forge 的启示（待验证）：** 可比较缓存优化策略骨架、完整轨迹和直接重规划；命中后仍重新做数值与性能验证。以新 workload、形状、编译器和设备变化检验复用，而不是把原任务成本降低解释为跨任务能力提高。

## Review Questions

1. 在不使用测试答案的条件下，哪些可观测信号足以允许成功轨迹写入缓存？
2. 固定模型和评测器，打乱任务顺序、控制重复度后，冷启动及稳态的成本—准确率曲线如何变化？
3. 缓存命中但适配失败时，回退大 planner 的成本是否抵消原先报告的节省？

## 价值评估

**阅读价值：中高，建议 Tier 3。** 对 agent 运行成本与历史经验复用有参考；对数值算法及 kernel correctness 的直接贡献有限。

**流程状态：** 2026-10-19 核查 v2 §§3–4、Tables 1–7、9 与缓存算法描述；保留作者汇总值并明确统计范围。未复现实验。

[^1]: Zhang et al. (2025). “Agentic Plan Caching: Test-Time Memory for Fast and Cost-Efficient LLM Agents.” arXiv:2506.14852v2. https://arxiv.org/abs/2506.14852v2
