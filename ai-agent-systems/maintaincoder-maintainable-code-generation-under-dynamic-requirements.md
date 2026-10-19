# MaintainCoder: Maintainable Code Generation Under Dynamic Requirements

_精读笔记｜arXiv:2503.24260v3，2025-09-29｜NeurIPS 2025｜阅读范围：主文 pp. 1–10；核读实现细节与稳健性附录（pp. 30–34），其余代码案例作抽查_

---

## 📌 书目信息与问题

- **作者：** Zhengren Wang、Rui Ling、Chufan Wang、Yongan Yu、Sizhe Wang、Zhiyu Li、Feiyu Xiong、Wentao Zhang
- **来源：** [arXiv:2503.24260v3](https://arxiv.org/abs/2503.24260v3)；[项目代码](https://github.com/IAAR-Shanghai/MaintainCoder)
- **问题：** 现有代码生成基准主要衡量静态需求下的功能正确性，难以衡量需求变化后代码是否容易修改。作者提出 MaintainBench 与 MaintainCoder 来评估和改善这种动态维护能力。

## ⚙️ 方法与评估

MaintainCoder 将生成过程分成两个相连模块：代码框架模块先分析需求、拆分职责、选择设计模式、生成框架并迭代评估；代码生成模块再在框架内实现、运行测试并修正。论文强调瀑布式阶段划分、设计模式与多 agent 分工（§3，pp. 5–7）。

MaintainBench 从 HumanEval、MBPP、APPS、CodeContests、xCodeEval 构造动态需求变体，覆盖功能扩展、接口变化、数据结构转换和错误处理四类修改。论文用变体上的 Pass@k、ASTsim、CodeDiff 等衡量修改后的通过率和代码变化（§4，pp. 7–9）。

## 📊 原文结果

- 在 APPS-Dyn，GPT-4o-mini 基线 Pass@5 为 35.5%，MaintainCoder 为 50.5%；DeepSeek-V3 基线为 59.5%，MaintainCoder 为 62.5%。对应 ASTsim 从 0.589/0.598 提升至 0.797/0.828，Code percentage difference 明显降低（Table 1，p. 8）。
- CodeContests-Dyn 上，GPT-4o-mini 的 Pass@5 从 24.2% 到 32.6%，DeepSeek-V3 从 26.5% 到 37.9%；xCodeEval-Dyn 上 GPT-4o-mini 从 23.4% 到 27.3%，DeepSeek-V3 从 21.9% 到 36.7%（Table 2，pp. 8–9）。这显示效果依赖模型与数据集，并非每个指标均一致改善。
- 原始任务的初始 Pass@5 也有改善，例如 GPT-4o-mini 在 xCodeEval 从 46% 到 57%，DeepSeek-V3 从 75% 到 77%（Table 3，p. 9）。
- 附录实现细节指出 Phase II 的需求变体生成器固定为 GPT-4o-mini（主实验），每种动态指标平均五轮；ASTsim 与 CodeDiff 均直接用 Python `difflib` 计算（Appendix D，p. 30）。作者另用 Gemini-2.5-Flash-Preview 作 Phase II 生成器，报告总体结论相近（Appendix E，p. 32）。

## 🔍 评议与边界

论文的价值在于把“改动后是否仍能通过任务”纳入代码生成评估，并提醒静态复杂度指标不等于可维护性。框架生成与代码实现分阶段，确实为需求理解和结构组织留出了显式步骤。

但动态指标是代理量：Pass@5 受生成随机性影响；AST 相似度与文本差异未必等价于真实维护工时或架构质量。特别是 `difflib` 被用于 ASTsim/CodeDiff，定义与复现细节需结合代码进一步确认。数据集以竞赛题/Python 代码为主，单步需求变体不能代表长期演化的大型软件仓库；自动生成的需求变体和测试也可能带来构造偏差。论文中的“提升超过 60%”是特定指标、模型和数据集上的作者总结，不应推广为普遍维护成本降低。

**对工程实践的启示：** 生成代码时明确模块边界和接口，再做变更场景评估；实际项目应在仓库级变更、真实测试和人工架构审阅中验证，而不只依赖 MI/CC 或文本相似度。

## Review Questions

1. 用哪些实证数据能校准 Pass@k、ASTsim 与真实维护工时之间的关系？
2. 若变更生成器与被测模型同源或能力接近，如何避免 benchmark 的生成器偏置？
3. 多 agent 框架的增益来自阶段划分、设计模式、额外采样，还是测试反馈？怎样做成本匹配的消融？

## 价值评估

**阅读价值：中高，建议 Tier 2。** 研究问题重要，基准思路适合补充“可修改性”维度；但其动态代理指标和竞赛题数据域仍需谨慎外推到生产仓库。

**流程状态：** 已精读并归档（2026-10-19）；未独立复现，也未进行独立同行复核。

[^1]: Wang, Z. et al. (2025). “MaintainCoder: Maintainable Code Generation Under Dynamic Requirements.” NeurIPS 2025. https://arxiv.org/abs/2503.24260v3
