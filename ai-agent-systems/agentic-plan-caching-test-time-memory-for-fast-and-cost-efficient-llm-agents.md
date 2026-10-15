# Agentic Plan Caching: Test-Time Memory for Fast and Cost-Efficient LLM Agents

_精读笔记｜arXiv:2506.14852v2｜全文 27 页；重点阅读方法 §§3–4、五类 workload 结果与 Appendix B–D 的实验/案例说明_

---

## 📌 书目信息与问题

- **作者：** Qizheng Zhang、Michael Wornow、Gerry Wan、Kunle Olukotun
- **来源：** [arXiv:2506.14852](https://arxiv.org/abs/2506.14852v2)
- **问题：** Plan-Act agent 的多轮 planning 会反复支付昂贵 LLM 推理成本；传统 KV/context cache 缓存 token 前缀，semantic cache 常缓存最终回答，但对依赖外部数据和环境变化的 agent 容易复用错误答案。能否复用“做事计划”而让其适配新任务上下文？
- **阅读范围：** 系统流程与 cache 生成/命中、与 semantic/full-history caching 对比、五个 agent workload、成本/延迟/匹配阈值分析及扩展实验。

## ⚙️ 方法与机制

正文要求仅从正确完成的 cache-miss 执行中生成可复用 **plan template**，存成 `(keyword, template)`。新任务先由轻量模型提取概括意图的 keyword，再查询 cache：命中时小 planner 将模板适配到当次任务的公司、年份等动态 context；未命中则由大 planner 正常生成计划。Actor 在当前环境执行，Planner 根据 response 判断是否继续（§3.1，pp. 4–5）。正文未充分说明在线如何判定“正确完成”；所给 Algorithm 3 也未显式展示正确性验证，因此这是系统描述中的要求，不应视为已证明的 cache correctness guarantee。

因此复用对象不是上一条 query 的答案或完整历史，而是抽象化的步骤骨架。作者观察到 Llama-3.1-8B 等小 planner 难以从冗长、未筛选的全部 agent history 中稳定抽取可复用计划，故先做模板化再适配（§3.2，p. 6）。

## 📊 原文证据与结果

- **评估任务：** FinanceBench、QASPER、Tabular Math Word Problems、AIME 2024/2025、GAIA，并测试 Minion 与 Open Deep Research 等 agent 设置（§4，pp. 6–8）。
- **作者报告的总体结果：** 摘要/结论报告 APC 平均成本降低 **50.31%**、application-level performance 保留 **96.61%**（摘要、§4.2，pp. 1、7；Table 9，p. 25）。但正文表格未交代这些平均数的完整聚合权重；按展示列等权重重算并不能精确得到这两个数。因此将其视为作者报告值而非独立核清的汇总。96.61% 是相对性能保留，不是绝对准确率。
- **延迟证据范围：** **27.28%** 延迟下降来自 FinanceBench 随机抽取 100 题、命中率 46% 的实验（§4.3，p. 8；Table 3，p. 9），不是五类 workload 的跨任务平均。该表总延迟 1959.24 秒降至 1424.82 秒，按此相对降幅约 27.28%。
- **命中质量与开销：** semantic caching 在较低相似阈值下会 false-positive hit；APC hit/miss accuracy 在报告实验中较接近，但这不构成 correctness guarantee。Table 1 显示 APC 位于 accuracy-optimal 与 cost-optimal 两端之间（§4.2，pp. 7–8）。**1.04%** cache 开销是 FinanceBench 与 TabMWP 的表列开销率 1.15%、0.93% 的算术平均（Table 2，p. 9），不能代表全部 workload。
- **阈值与扩展代价：** keyword 模糊匹配阈值从 100% 降至 >60% 时，表中 hit rate 由 46% 升至 64%，成本由 $1.86 降至 $0.93，但 accuracy 从 85.50% 降到 77.00%；1M 条 cache 下 fuzzy lookup 延迟约 148 ms，而 exact lookup 约 56 μs（§4.4，p. 10）。这是特定实现和阈值配置，提示大 cache fuzzy search 的吞吐瓶颈。

## 🔍 评议、限制与迁移

- **贡献本质：** 把 agent experience 从“原始轨迹/最终答案”提炼成带可变槽位的 plan template，并把计划复用放入 serving path；它主要优化推理效率，不声称让 planner 获得新能力。
- **限制：** 模板质量依赖源任务成功与抽取质量；命中率、keyword 语义漂移、任务状态变化决定收益。论文也指出低 hit-rate 可能让 cache overhead 不划算，并提出持续低命中时关闭 caching；模糊匹配带来 accuracy–latency tradeoff。实验使用特定 Minion 架构和 LM 组合，迁移到其他 agent 需要重新验证。
- **对 SCALE_Forge 的启示（待验证推演）：** 若要复用优化轨迹，可研究缓存“策略骨架”与旧代码/完整 history 的差别：以 operator family、瓶颈类型、硬件代际做检索键，shape、编译器和设备状态作为适配字段；命中后仍重新走 correctness 与 benchmark evaluator，不复用旧的性能结论。需监控 hit rate、false hit、adaptation overhead，并比较启用/关闭缓存的配对结果。论文未验证这些 kernel-search 设计。

## Review Questions

1. 哪些优化操作可被模板化为可适配步骤，哪些必须因输入形状或硬件状态重新测量？
2. cache key 是否应包含 operator signature、dtype/layout、硬件型号与编译器版本，避免高语义相似但技术条件不同的误命中？
3. 性能 cache 的 hit/miss evaluator 能否保持 correctness 先行，并对 stale result 设置失效策略？

## 价值评估

**六维参考（1–6）：** idea 清晰 5；可验证性 4；迁移价值 4；领域重要性 3；方法创新 4；影响力 3。**阅读价值：中高，建议 Tier 3。** 对 agent 运行成本与历史经验复用有参考；对数值算法及 kernel correctness 的直接贡献有限。

**流程状态：** 元数据、原文、评估、精读、索引、审阅：完成（独立 Codex 只读审阅；未完成 Kimi 复核）；提交：跳过（未请求）。

[^1]: Zhang et al. (2025). “Agentic Plan Caching: Test-Time Memory for Fast and Cost-Efficient LLM Agents.” arXiv:2506.14852v2. https://arxiv.org/abs/2506.14852v2
