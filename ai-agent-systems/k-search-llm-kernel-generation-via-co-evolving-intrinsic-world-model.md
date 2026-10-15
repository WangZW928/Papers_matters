# K-Search: LLM Kernel Generation via Co-Evolving Intrinsic World Model

_精读笔记｜arXiv:2602.19128v2，2026-02-26｜全文阅读：主文与主要实验结果_

---

## 📌 书目信息与问题

- **作者：** Shiyi Cao、Ziming Mao、Joseph E. Gonzalez、Ion Stoica，UC Berkeley
- **来源：** [arXiv:2602.19128](https://arxiv.org/abs/2602.19128v2)；[K-Search 代码](https://github.com/caoshiyi/K-Search)
- **研究问题：** 将 LLM 仅作为代码候选生成器加外部进化搜索，是否会错过需要多步、非单调变换的 kernel 优化路径？能否让模型显式规划并随搜索结果更新规划？
- **阅读范围：** 搜索状态与 world model、三阶段循环、FlashInfer 与 GPUMode 实验、作者结论。

## ⚙️ 方法：规划与实现分离

K-Search 将 kernel 优化写成固定 evaluator 预算下的搜索。评估器对候选程序 `x` 返回正确性、延迟和元数据；错误候选得零分，正确候选按参考 SoTA 延迟计算 speedup score。

1. **Action selection：** 搜索树 frontier 保存高层优化假设，如融合 head、split-K 或改变数据驻留；LLM world model 为动作估计优先级。
2. **Local refinement：** 对选中的高层意图生成具体 CUDA kernel，在局部路径上迭代直至停滞；实现暂时失败不立即抹掉策略假设。
3. **World-model update：** 根据编译、正确性和性能证据，在树上插入想法、更新优先级或剪枝。策略规划与程序实例化相互反馈、共同演化。

这一区分有价值：低层代码一次写错不必然说明高层优化方向错误；反过来，一个能编译的候选也不说明该方向值得继续投入。

## 📊 证据与结果

- **主实验：** FlashInfer-Bench 中 4 种 attention/MoE kernel、共 **152 条 workload traces**；NVIDIA H100/B200，CUDA 12.8、FlashInfer 0.5.3、PyTorch 2.8.0。每方法每任务 120 次候选评估，重复 3 次，以同一 FlashInfer reference 和 traces 比较。
- **整体分数：** K-Search 平均 final score **56.13**，高于 OpenEvolve 的 **26.68**（2.10×）和 ShinkaEvolve 的 **25.37**（2.21×）。MoE 得分 **44.1**，相对 OpenEvolve **3.09** 为 14.3×；MLA prefill 为 57.4，GQA decode 为 76.0。
- **并非每实例都赢：** K-Search 的 split-K 在较大 batch 上更易摊薄同步开销，但作者指出其在 GQA decode 的 16 个 batch=1 和 4 个 batch=16 workload 上可能慢于对照搜索方法。
- **GPUMode TriMul：** 作者报告 H100 几何平均延迟 **1030 μs**，超过当时对照方案。此竞赛案例与 FlashInfer 主实验的任务和评分口径不同。

## 🔍 评议、边界与迁移

- **贡献的本质：** 搜索策略不再是静态 heuristic；模型对优化意图的价值判断随评估证据更新，并影响搜索树结构。
- **外推边界：** 主结果集中于 CUDA、四类 FlashInfer kernel、固定真实流量 traces 和 H100/B200；不能直接推出它在任意领域搜索树上都优于进化或 MCTS。论文为 MLA decode 提供初始程序，也说明起始代码质量会影响搜索。
- **正确理解 world model：** 这里的“world model”是维护/更新搜索假设和动作优先级的机制，不是对 GPU 微架构的高保真模拟。
- **对 SCALE_Forge 的启示：** 将高层策略（优化动作 DAG/树）与低层候选代码分层记录；候选效用绑定正确性、实测耗时和 evaluator 元数据；允许策略继承多个已验证变换；停滞时触发局部改写或换分支，而非只重复采样 prompt。

## Review Questions

1. 经验条目应是“代码技巧”还是“带前提的搜索动作”？其状态和证伪条件如何表达？
2. 如何识别变换组合收益，避免因单独尝试分数低而过早剪枝？
3. 固定相同的测量预算后，如何分别消融策略更新、代码生成与初始程序的贡献？

## 价值评估

**阅读价值：很高。** 与“提案—评估—状态转移—再搜索”型 Agent loop 直接相关；应在自身 workload 上验证规划机制，不宜只引用 headline speedup。

**状态：** ✅ 已精读（2026-10-15）

## 核对依据与边界（2026-10-15）

本次取得的 PDF 首页版本与本页声明的 2602.19128v2 一致；检查结果数字与方法边界，统一复读问题及价值评估格式。这里的“已精读”是原有阅读记录，不表示本次重新独立复现了所有实验。
