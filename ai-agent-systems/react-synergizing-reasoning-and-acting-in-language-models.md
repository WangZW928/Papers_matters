# ReAct: Synergizing Reasoning and Acting in Language Models

_精读笔记｜arXiv:2210.03629v3，2023-03-10｜ICLR 2023｜主文 pp. 1–10；核读附录中的提示、示例与代表性失败轨迹_

---

## 书目信息与问题

- **作者：** Shunyu Yao、Jeffrey Zhao、Dian Yu、Nan Du、Izhak Shafran、Karthik Narasimhan、Yuan Cao
- **来源：** [arXiv:2210.03629v3](https://arxiv.org/abs/2210.03629v3)[^1]
- **问题：** 纯语言推理容易产生无依据的事实，纯行动策略又缺少可检查的规划；能否让语言模型在交互任务中交替生成推理文本与环境动作？
- **阅读范围：** 方法定义、HotpotQA/FEVER、ALFWorld/WebShop 结果、错误分析和提示示例。附录提示逐字内容未全部转录。

## 方法

ReAct 把语言思考加入 agent 的动作空间：`Thought` 更新上下文而不改变环境；`Action` 操作检索接口或任务环境；`Observation` 来自外部执行。知识问答采用较密集的 thought–action–observation 交替；ALFWorld/WebShop 的长行动序列只在关键位置插入稀疏思考，由模型决定时机（§2–§3.2，PDF pp. 3–4）。

主要实验用冻结的 PaLM-540B 和少量人工轨迹提示，Act 消融删除相同示例中的 thoughts，因而能够检验语言思考在给定动作接口上的增量作用。论文也用 3,000 条正确轨迹微调 PaLM-8B/62B，故不能概括成“只有 prompting、没有训练”。HotpotQA/FEVER 的检索动作限于 `search`、`lookup`、`finish`，不等同于现代检索增强系统的完整能力（§3.1–§3.3，pp. 4–7）。

## 结果与证据

- **知识问答：** PaLM-540B 的 ReAct 在 HotpotQA EM/FEVER accuracy 为 27.4/60.9，CoT 为 29.4/56.3：检索并未使两项任务都变好。HotpotQA 最佳混合结果 35.1 来自 ReAct → CoT-SC，FEVER 的 64.6 来自 CoT-SC → ReAct，是两种不同的回退策略（Table 1，PDF p. 5）。
- **错误分析：** 作者对两种方法各抽取 50 条成功、50 条失败轨迹，共 200 条人工分类。ReAct 失败样本中 47% 为推理错误、23% 为搜索结果错误；CoT 失败样本中 56% 为幻觉。这些是按成功/失败分层抽样后的条件比例，不能解释为总体幻觉率或安全保证（Table 2，p. 6）。
- **交互任务：** ALFWorld 的 ReAct 六组提示平均成功率为 **57%**，最佳提示组为 **71%**；Act 的 45% 同样是 best-of-6。WebShop 的 ReAct 得分/成功率为 66.6/40.0，Act 为 62.3/30.1，人类专家为 82.1/59.6。两个环境的评价样本分别为 134 个游戏、500 条购物指令（Tables 3–4，pp. 7–8）。
- **规模与学习方式：** 小模型的 few-shot ReAct 较弱，而用正确轨迹微调后明显改善（Fig. 3，p. 7）。证据支持“交互格式需要模型能力或轨迹训练配合”，不支持仅靠固定模板就能普遍提高能力。

## 评议与边界

本文的主要贡献是把推理置于可获得外部反馈的控制循环，并用同轨迹删去 thought 的消融检验其价值。它展示了检索对事实依据的帮助，也揭示强制交替可能限制推理灵活性；两种混合回退策略优于单独 ReAct，正说明内部知识与环境观察具有互补性（§3.3，pp. 5–6）。

**审阅判断：** 可读轨迹提供诊断接口，但不能由此推断 thought 是模型决策的忠实因果解释。Act 消融能支持给定提示设计下的效果差异；最佳提示组、提示平均与跨模型结果必须分开。论文的人工 thought-editing 示例展示可纠错性，尚不足以估计大规模部署中的人工成本或恢复成功率（§4，pp. 8–9）。

**迁移启示（待验证）：** 科学代码 agent 可沿用执行—观察循环，但应以编译结果、数值误差和实测耗时作为反馈，并单独评估循环检测及回退策略；这些属于应用设计建议，不是本文已验证的 kernel 优化结论。

## Review Questions

1. 若固定总 token、工具调用次数与示例轨迹，ReAct 相对 Act/CoT 的收益还剩多少？
2. 何时应从检索切换到内部推理，怎样在验证集上选择阈值而不利用测试答案？
3. 人工编辑 thought 的收益能否超越直接修正动作，且在独立任务上保持？

## 价值评估

**阅读价值：高，建议 Tier 2。** ReAct 是工具使用型 LLM agent 的基础接口论文。实际应用时应吸收其轨迹结构与环境反馈原则，同时补上权限、成本、循环和错误恢复机制。

**流程状态：** 2026-10-19 按 arXiv v3 核查方法、Tables 1–4 与相关附录；修正作者名单、思考密度及 ALFWorld 聚合口径。未复现实验。

[^1]: Yao, S. et al. (2023). “ReAct: Synergizing Reasoning and Acting in Language Models.” ICLR 2023. https://arxiv.org/abs/2210.03629v3
