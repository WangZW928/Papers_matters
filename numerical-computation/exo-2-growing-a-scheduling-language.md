# Exo 2: Growing a Scheduling Language

_精读笔记｜arXiv:2411.07211v4｜全文 35 页；重点阅读主文 pp. 1–15 与性能评测 pp. 18–23_

---

## 📌 书目信息与问题

- **作者：** Yuka Ikarashi、Kevin Qian、Samir Droubi、Alex Reinking、Gilbert Louis Bernstein、Jonathan Ragan-Kelley
- **发表信息：** ASPLOS ’25；[arXiv:2411.07211](https://arxiv.org/abs/2411.07211v4)
- **问题：** 性能敏感程序的使用者想要控制什么，会随应用/硬件而变化。若调度语言把所有操作预先固定进编译器，扩展新自动化就要改编译器或退回 C/汇编。论文提出 user-schedulable language 应当“可生长”。
- **阅读范围：** Exo 2 设计、Actions/Inspection/References、Cursor 实现、用户调度库案例及与 Exo/Halide/BLAS 实现的性能比较。

## ⚙️ 方法与机制

Exo 2 将调度程序放在宿主语言中，由一组受信任、细粒度的**动作（修改程序）、检查（查询程序）与引用（定位程序部分）**原语组成用户自定义 scheduling library。关键机制是 **Cursor**：它指向某一程序版本中的循环、语句或 gap；程序变换后，Cursor 支持跨版本 forwarding。歧义情况下实现会以确定性启发式尽量给出有效引用，部分删除/移动操作会令引用失效；这与无效导航时报错是不同情况（§5.2，pp. 5–8）。

安全主张主要来自受信任原语的等价保持与合法性检查，而不是 `Op` 类型接口本身，也不是对任意 Python 调度代码的正确性证明。用户可以把重复低层步骤封装为高层 schedule（如 tiling、向量化、内存 staging），逐步形成适配应用和目标架构的语言抽象。部分精度/内存/并行约束检查推迟至代码生成前（Appendix A.7，p. 23）。论文将其与仅提供固定调度操作的 USL 区分：Exo 2 让抽象本身成为用户可编程对象。

## 📊 原文证据与结果

- 作者构造调度库并应用到 **80 多个高性能 kernel**，使调度代码总量减少约一个数量级，同时在 **三种平台**上取得与专家实现有竞争力的性能（摘要；§6，pp. 9–14）。代码量的比较是对用户显式调度工作量的代理指标，作者承认可能高估相对精心编写的 Exo schedule 的差距；它不直接量化开发时间、验证或维护成本（§6.2.3，p. 12）。摘要的“competitive”不是逐任务全面胜过专家库。
- 一个针对 3×3 box blur 与 unsharp masking 的 Halide-like library 案例得到与专家编写 Halide schedule 相近的性能（§6.3.2，p. 14）。这验证了可在 Exo 2 外部重建高层自动化，而不是证明 Exo 2 对所有 DSL 性能更优。
- 性能图主要见 pp. 9、11、13，BLAS 补充图在 pp. 30–35；Exo/Exo 2 及 BLAS、OpenBLAS、MKL、BLIS 的比较覆盖特定 kernel/平台。解读时应按每个比较的 baseline、向量指令集和具体 kernel 读，不能将 heatmap 概括成统一加速倍数。作者还指出某些原语组合无法表达的变换仍需修改编译器，细粒度检查会增加调度时间（§8，p. 15）。

## 🔍 评议、限制与迁移

- **贡献本质：** 把“优化抽象如何演进”从编译器团队的内置设计问题，转成用户可组合、可复用且受安全原语约束的库设计问题。
- **限制：** 可扩展性不等于自动找到好 schedule；领域专家仍需提供调度策略和检查逻辑。Cursor 转发语义与代码变换必须维护复杂的引用不变量；论文的 case studies 证明可行性，不代表任意领域皆能经济地构造库。跨平台结果也依赖编译器、目标 ISA 和手工优化能力。
- **对高性能框架的启示：** 为可插拔调优接口定义小而可信的 primitive（loop transform、layout、memory-space、vector/thread mapping），允许框架用户以 Python/DSL 组合成新策略。将**候选策略层**与**合法性/IR变换层**分开，失败时输出精确的 schedule 约束与引用诊断。对 AMR 可探索将 patch/block tiling、halo exchange 排程和 GPU launch policy 做成库，而非散落成后端特例。

## Review Questions

1. 现有 AMR/PDE IR 是否能为 loop、patch、数据区间提供稳定且可诊断的引用？
2. 哪些 schedule primitives 能保证数值等价，哪些需要边界/别名/浮点重排条件？
3. 将调度代码缩短一个数量级后，是否也降低了跨硬件验证/维护成本，还是把复杂度转移给库作者？

## 价值评估

**六维参考（1–6）：** idea 清晰 5；可验证性 4；迁移价值 6；领域重要性 4；方法创新 5；影响力 4。**阅读价值：很高，建议 Tier 2。** 对可扩展性能工程接口直接相关，应与 MetaSchedule、egg 和现有 AMReX/BoxLib 架构文献联合阅读。

**流程状态：** 元数据、原文、评估、精读、索引、审阅：完成（独立 Codex 只读审阅；未完成 Kimi 复核）；提交：跳过（未请求）。

[^1]: Ikarashi et al. (2025). “Exo 2: Growing a Scheduling Language.” ASPLOS ’25; arXiv:2411.07211v4. https://arxiv.org/abs/2411.07211v4
