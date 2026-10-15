# Tensor Program Optimization with Probabilistic Programs

_精读笔记｜arXiv:2205.13603v2｜全文 18 页；阅读主文 §§1–6 与搜索空间构造/硬件模块附录 A.1–A.4_

---

## 📌 书目信息与问题

- **作者：** Junru Shao、Xiyou Zhou、Siyuan Feng、Bohan Hou、Ruihang Lai、Hongyi Jin、Wuwei Lin、Masahiro Masuda、Cody Hao Yu、Tianqi Chen
- **来源：** [arXiv:2205.13603](https://arxiv.org/abs/2205.13603v2)；论文提出的抽象后来用于 TVM MetaSchedule
- **问题：** 自动调优器能否不把优化空间硬编码为固定模板，而以模块化、可组合方式让领域专家扩展 tensor program 的候选空间？
- **阅读范围：** 概率程序式搜索空间与模块组合（§§3.1–3.2）、trace 驱动学习搜索（§4）、TVM 实验（§6）与硬件特定模块附录。

## ⚙️ 方法与机制

MetaSchedule 把优化空间写成从初始程序 (e_0) 出发的一串参数化随机变换：每个 transformation module 检查当前程序状态、选择可作用的循环/块，并对 tiling、loop order、vectorization、thread binding、tensor-core 使用等做随机决定。固定 trace 中的指令和采样选择可确定一个候选；单独固定变换指令仍可能对应多个候选，变异产生的 trace 也需 validator 检查有效性。组合多个模块即可构造更丰富的 search space，而不用改动 search engine（§3.2，pp. 4–5；§4，pp. 6–7）。

搜索与空间定义解耦：system engineer 定义/扩充 transformations，learning-driven search 对 trace 候选做代价评估与迭代优化（§4，pp. 6–7）。因此贡献不只是 cost model，而是将“如何产生候选”也抽象为可编程组件。硬件特定优化（如 Tensor Core module）可以和通用空间组合；随机/模块化构造可能增加探索难度或预算需求，但实际影响需在固定预算与停止条件下测量，不能假定随机化必然增成本。

## 📊 原文证据与结果

- **表达力：** 在一组来自深度学习模型的算子与子图上，对照 PyTorch 1.11 及 TVM/AutoTVM/Ansor（各配置取对应较优基线）；CPU 和 GPU 结果显示 MetaSchedule 通常与 TVM 相当或更好（§6.1，p. 8）。这是对测试 workload 的经验结果，不构成搜索空间包含关系的形式证明。
- **空间增量价值：** BERT 的 fused-dense 子图逐步加入 multi-level tiling、auto-inline、random-unroll 等模块后，搜索结果持续改善。研究生用约 **2 天**写出 **82 行**的 `Use-Tensor-Core` 模块；对 BERT-Large，定制空间相对 TVM AutoTVM 带来 **48%** speedup（§6.3，p. 9；附录 A.3–A.4）。此数字是特定模型和 baseline 的结果，不是对端到端所有模型的 48%。
- **端到端模型：** BERT-Base、ResNet50、MobileNetV2 在 CPU/GPU 上的结果与 TVM Ansor 接近或更好（§6.2，p. 8）。硬件、库和 workload 设置见附录 A.1–A.2。

## 🔍 评议、限制与迁移

- **贡献本质：** 将“搜索算法”与“搜索空间语言”拆开，使编译器开发者可以显式注入专业知识；这解决的是空间表达/可维护性瓶颈，不是免除 expert effort。
- **边界：** 候选质量仍受 transformation 集合限制；不同 search-space 需在明确预算下测量探索成本。结果依赖 TVM 编译/测量栈、特定模型和硬件，论文未给出理论最优性保证；不同空间下 benchmark 搜索预算应保持可比。论文 MAP 目标还含 trace 先验：若延迟为 f(g(e_0, τ))，公式相当于最小化 f − log P(τ)，一般并非纯最小延迟。原文未说明该先验是否均匀或延迟如何归一化；这是对论文公式的数学审阅，不能据此断言代码实现错误。
- **对高性能框架的启示：** 将硬件优化知识封装为可组合模块，统一候选 trace、合法性结果、编译耗时、性能样本和缓存键。可把 AMR 的 tile/block 尺寸、数据布局、融合、CPU/GPU 映射分成模块，再由同一 search driver 探索。对选择算子时应保留每个模块的贡献消融，避免“更大搜索空间”被误认为无成本改进。

## Review Questions

1. AMR 任务的搜索空间是否可由参数化 transformation 表达，如何处理 coarse-fine 边界和 ghost-cell 依赖？
2. trace 级缓存要包含哪些编译器版本、硬件状态与输入形状，才能防止错误复用？
3. 公式（1）的 trace 先验是否均匀、延迟如何归一化？实际优化目标是纯延迟还是带先验项的 MAP 目标？

## 价值评估

**六维参考（1–6）：** idea 清晰 5；可验证性 5；迁移价值 6；领域重要性 4；方法创新 5；影响力 5。**阅读价值：高，建议 Tier 2。** 与 Exo 2 互补：前者提供概率化空间抽象与学习搜索，后者突出用户可增长、语义受约束的调度语言。

**流程状态：** 元数据、原文、评估、精读、索引、审阅：完成（独立 Codex 只读审阅；MetaSchedule reviewer/Kimi 未完成复核）；提交：跳过（未请求）。

[^1]: Shao et al. (2022). “Tensor Program Optimization with Probabilistic Programs.” arXiv:2205.13603v2. https://arxiv.org/abs/2205.13603v2
