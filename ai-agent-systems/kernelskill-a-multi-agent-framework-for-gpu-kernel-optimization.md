# KernelSkill: A Multi-Agent Framework for GPU Kernel Optimization

_精读笔记｜arXiv:2603.10085v1｜全文 15 页；阅读系统架构、memory policy、KernelBench 实验、消融和 conclusion_

---

## 📌 书目信息与问题

- **作者：** Qitong Sun、Jun Han、Tianlin Li、Zhe Tang、Sheng Chen、Fei Yang、Aishan Liu、Xianglong Liu、Yang Liu
- **来源：** [arXiv:2603.10085](https://arxiv.org/abs/2603.10085v1)；[代码仓库](https://github.com/0satan0/KernelMem/)
- **问题：** LLM 优化 GPU kernel 往往依赖隐式优化直觉，导致试错不透明、反复走回头路。能否将 expert optimization knowledge 和每个任务的历史轨迹显式纳入多 agent 闭环？
- **阅读范围：** Generator/Diagnoser/Planner/Repairer/Optimizer 与 Reviewer 角色、双层 memory、KernelBench 评估与 ablation。

## ⚙️ 方法与机制

KernelSkill 将流程拆为候选生成、编译、校验、profile、方法规划、修复/优化多个角色。Reviewer 由 compiler、verifier 与 profiler 构成：输出构建状态/错误、与 PyTorch reference 的数值比较，以及 nsys/ncu 的 latency、register/shared-memory 等数据（§4.1，pp. 4–5）。

记忆分两层：**长期 memory** 将 GPU 优化知识整理为可检索的 skill，并把条件—方法映射物化成 deterministic decision policy（predicate、priority、global veto、decision table）；规则负责筛选候选方法，LLM 再生成解释与具体计划。**短期 memory** 记录当前任务每轮候选、修改、错误、profile 和结果，旨在减少重复失败策略并稳定逐轮 refinement；实验支持记忆设计有用，但没有量化“消除”回退（§4.2，pp. 6–7）。

## 📊 原文证据与结果

- **基准与定义：** KernelBench Levels 1–3；success 表示候选可编译且通过 correctness verification；speedup 是相对 Torch Eager 的平均 runtime speedup，不代表胜过 `torch.compile`、cuDNN 或生产实现（Table 1，p. 8）。
- **结果：** KernelSkill 三层 success 均为 100%，speedup 分别 **5.44× / 2.82× / 1.92×**。但表 3 的 Fast1（达到 Torch Eager 速度以上的任务比例）在 Level 1/3 为 0.62/0.82，低于 STARK 的 0.71/0.87；Level 2 都为 1.00。因此平均加速最高，不代表逐项全面领先。部分 baseline 结果取自其论文，另一些由作者重实现，非统一复现实验（§5，pp. 8–9）。所有模型调用采用 ChatGPT-5.1；每任务生成 3 个 seed，挑选通过验证且 latency 最低者，最多 15 轮 refinement；profile 使用 NVIDIA Nsight Compute/Systems；候选 base 更新门槛为相对 30% 或绝对 0.3 speedup。
- **消融与边界：** 去除长期 memory 后平均 speedup 下降（Table 2，p. 8），但论文未报告重复实验方差或统计显著性；缺少匹配案例时可能退回 LLM-only 方法选择（§5、§6，pp. 9–10）。

## 🔍 评议、限制与迁移

- **贡献本质：** 把优化经验显式化为“规则筛选 + 文本知识”的两阶段选择，并通过任务内短记忆尝试减少重复 backtracking；这是搜索流程治理，而不只是增加 agent 数量。
- **限制：** 结果不能直接推出相对 `torch.compile`、cuDNN 或生产实现的优势。论文依赖特定 LLM、KernelBench、NVIDIA profile 工具与 memory 知识库；专家 skill 的覆盖和正确性是系统先验，覆盖不足可能影响性能；success 仅表示按论文定义通过编译与 correctness，不等同于跨平台 correctness 或任务加速。
- **对高性能框架的启示：** 将策略选择变为可审核规则：bottleneck、dtype、shape、occupancy、memory traffic 决定候选优化集合；对每轮记录源码 hash、环境、correctness、profile 和被否决的策略。针对 AMR，应把 layout/halo/patch 约束纳入 veto rules，避免只凭 LLM 建议引入违反数据依赖或边界条件的变换。

## Review Questions

1. 该决策表能否用公开 profile 特征稳定映射到 AMR stencil 的优化类别？
2. 长期 skill 是由专家文献蒸馏还是由本地成功轨迹归纳，二者如何标注证据强度？
3. 若 baseline 替换为 `torch.compile`/vendor library，100% success 和平均 speedup 会如何变化？

## 价值评估

**六维参考（1–6）：** idea 清晰 5；可验证性 4；迁移价值 5；领域重要性 4；方法创新 4；影响力 3。**阅读价值：中高，建议 Tier 2。** 对 memory、可解释策略选择与反馈闭环有直接工程启发；数值结论需要按 baseline 与目标 GPU 重测。

**流程状态：** 元数据、原文、评估、精读、索引、审阅：完成（独立 Codex 只读审阅；未完成 Kimi 复核）；提交：跳过（未请求）。

[^1]: Sun et al. (2026). “KernelSkill: A Multi-Agent Framework for GPU Kernel Optimization.” arXiv:2603.10085v1. https://arxiv.org/abs/2603.10085v1
