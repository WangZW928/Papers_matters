# KernelCraft: Benchmarking for Agentic Close-to-Metal Kernel Generation on Emerging Hardware

_精读笔记｜arXiv:2603.08721v2，2026-05-29｜ICML 2026｜全文阅读：主文与结果/消融部分_

---

## 书目信息与问题

- **作者：** Jiayi Nie、Haoran Wu、Yao Lai、Zeyu Cao、Cheng Zhang、Binglei Lou、Erwei Wang、Jianyi Cheng、Timothy M. Jones、Robert Mullins、Rika Antonova、Yiren Zhao
- **来源：** [arXiv:2603.08721v2](https://arxiv.org/abs/2603.08721v2)；[项目主页](https://kernelcraft-cam.github.io/)
- **研究问题：** 面向新兴加速器及新 ISA，工具使用 Agent 能否生成并迭代优化接近硬件的 assembly kernel？任务复杂度、文档、工具和推理预算怎样影响成功率？
- **阅读范围：** benchmark 设计、三类硬件与工具闭环、模型/平台结果、消融、CPU 与专家内核扩展案例。

## 方法与基准设计

- **层级：** Level 1 primitive operations、Level 2 composite/algorithmic operations、Level 3 end-to-end systems；分别组织 ML 与 CPU 任务。
- **平台：** PLENA 自定义 ISA、AMD NPU、Coral NPU，以及扩展评估中的 RISC-V BOOM CPU。Agent 使用 ISA/硬件说明、平台工具和执行反馈。
- **Agent 工具：** 写代码、语法检查/编译、运行正确性与延迟评估、查看输出差异、查询指令数量、搜索硬件文档等，形成诊断—修复循环。
- **评估：** 按平台语义做容差正确性检查；PLENA 用事务级模拟器，AMD NPU 在实机运行，Coral 与 BOOM 用 Verilator；不能将四种后端统称为周期精确模拟。性能以相同配置的周期数或延迟对比平台编译器 baseline（Table 3、附录 C.1，pp.4、15）。

论文包含 **33 个任务（23 个 ML、10 个 CPU）**；三类加速器主实验每个可支持任务有 5 个配置，4 个模型共超过 1,100 次运行。加速器 L1/L2/L3 的上限分别为 15/20/25 轮（Table 5，pp.5–6）。

## 证据与结果

- **成功率与分母：** GPT-5.2 在 PLENA/AMD/Coral 为 **56/100、19/110、35/75**，约 **56%/17%/47%**。分母不同，是因为部分任务不受 ISA 或编译器支持，不应补成模型失败或直接据此排序硬件难度。PLENA L2 正文写 45%，但 Table 5 小计为 **19/40=47.5%**；这里保留原文冲突并以表内计数说明（p.5）。
- **系统级任务仍难：** Level 3 只有 Coral 上 Gemini-3-Flash 的 ConvBlock 一个配置成功。性能图则选各任务表现最好的 Agent：Coral 的 ConvBlock 达 **7.93×**，不能解释为模型平均收益；AMD 所示结果多在 **0.89–1.18×**（Fig. 3、§4.2，pp.6–7）。
- **推理和示例：** Table 7 中四类任务关闭 thinking 均 0/5，中等 thinking 为 3/5 或 4/5，同时增加 token 和实际迭代数。Table 8 中 PLENA MQA 的 GPT-5.2 从 **1/5→4/5**，Gemini 仍 **0/5→0/5**。AMD 主实验本就含 GEMM 示例，不能把全部平台称为 zero-shot（p.6）。
- **正确性补充：** 附录 C.2 在 PLENA 的 SiLU/Linear/FFN 上补测 13 种输入条件，三者均通过；它只覆盖三个选定 kernel。Table 12 不同容差下的逐元素匹配率最低 **97.3%**，与正文“全通过”的笼统说法有张力，需明确最终判定阈值（p.16）。
- **专家与 CPU：** Coral depthwise-conv C1，Agent/专家相对 compiler 为 **2.5×/20×**，C2/C3 的 Agent 仅 **0.6×/0.5×**（Table 11，p.9）。BOOM 的 10/10 任务正确，但相对 `-O2` 基线，Quicksort 为 **1.63×**、Radix sort 为 **0.12×**（Table 10，p.8）。

## 评议、边界与迁移

- **贡献定位：** 将评测对象从成熟 CUDA 扩展到 ISA、文档和工具仍不完善的平台；其价值在于揭示“模型 × 支持材料 × 执行工具”的系统能力，而非孤立的模型编码分数。
- **归因限制：** 跨平台任务覆盖、算术格式、文档长度和后端都不同。推理消融也改变实际迭代量和 token 消耗，证明的是配置整体有用，不能单独证明多出的 reasoning token 更高效。工具调用频率与成功相关，同样不构成因果证据。
- **验证边界：** Coral 整数输出要求精确一致，PLENA/AMD 采用不同容差；不能用统一“正确率”掩盖语义差异。附录已有边界输入测试，不应声称完全未测鲁棒性，但其覆盖不足以保证全任务泛化。
- **对 SCALE_Forge 的启示：** 将支持范围、精度语义、文档版本、工具接口和预算一起版本化；报告可评估覆盖率、功能正确率和性能分布。新增后端应从 primitive、组合算子到系统块逐层验收，并保留专家基线。

## Review Questions

1. 对齐共同任务、算术格式和 token 预算后，平台间的成功率差距还剩多少？
2. 多元素输出的容差是逐元素全通过，还是允许一定比例不匹配；这会怎样影响成功率？
3. 相同模型增加 ISA 文档、可执行示例或诊断工具，哪一项带来的单位成本收益最大？

## 价值评估

**阅读价值：高。** 对 Agent tools、低层代码生成、硬件文档与难度分层基准很有参考；CUDA 专属闭环的结论不能无条件外推。

**状态：** 已精读；原文复核于 2026-10-19。

## 核对依据与边界（2026-10-15）

保留 2026-10-15 的阅读记录；2026-10-19 按本页所链版本重新核对方法、结果及相关附录。以下页码均为该版 PDF 页码；评价与迁移建议是本笔记的审阅判断。本次未复现实验。
