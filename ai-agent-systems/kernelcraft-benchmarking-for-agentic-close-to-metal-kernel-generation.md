# KernelCraft: Benchmarking for Agentic Close-to-Metal Kernel Generation on Emerging Hardware

_精读笔记｜arXiv:2603.08721v2，2026-05-29｜ICML 2026｜全文阅读：主文与结果/消融部分_

---

## 📌 书目信息与问题

- **作者：** Jiayi Nie、Haoran Wu、Yao Lai、Zeyu Cao、Cheng Zhang、Binglei Lou、Erwei Wang、Jianyi Cheng、Timothy M. Jones、Robert Mullins、Rika Antonova、Yiren Zhao
- **来源：** [arXiv:2603.08721](https://arxiv.org/abs/2603.08721v2)；[项目主页](https://kernelcraft-cam.github.io/)
- **研究问题：** 面向新兴加速器及新 ISA，工具使用 Agent 能否生成并迭代优化接近硬件的 assembly kernel？任务复杂度、文档、工具和推理预算怎样影响成功率？
- **阅读范围：** benchmark 设计、三类硬件与工具闭环、模型/平台结果、消融、CPU 与专家内核扩展案例。

## ⚙️ 方法与基准设计

- **层级：** Level 1 primitive operations、Level 2 composite/algorithmic operations、Level 3 end-to-end systems；分别组织 ML 与 CPU 任务。
- **平台：** PLENA 自定义 ISA、AMD NPU、Coral NPU，以及扩展评估中的 RISC-V BOOM CPU。Agent 使用 ISA/硬件说明、平台工具和执行反馈。
- **Agent 工具：** 写代码、语法检查/编译、运行正确性与延迟评估、查看输出差异、查询指令数量、搜索硬件文档等，形成诊断—修复循环。
- **评估：** 按平台语义做容差正确性检查；性能以硬件或周期精确模拟的周期数/延迟相对平台编译器 baseline 计算。每项任务有多个配置与迭代预算。

论文包含 **33 个任务（23 个 ML、10 个 CPU）**；加上配置和多模型运行形成超过 1,100 次实验。摘要中的“>20 tasks”与详细贡献处的 33 个 benchmark tasks 是不同粒度的描述。

## 📊 证据与结果

- **任务成功率：** accelerator 主实验中 GPT-5.2 对 PLENA/AMD/Coral 分别为 **56% / 17% / 47%**，Gemini-3-Flash 为 **35% / 11% / 39%**；这是论文定义的各层与有效配置上的 aggregate，不代表端到端任务胜率。
- **难度效应：** GPT-5.2 在 PLENA Level 1 primitives 可达 **74%**，Level 2 降至 **45%**；Level 3 的端到端 block 几乎全部失败，只有 Coral 上 Gemini-3-Flash 成功一个 ConvBlock。AMD NPU 最难，最佳总体成功率低于 20%。
- **速度：** Coral 上部分 GEMV/GEMM/ConvBlock 任务达到编译器 baseline 的 2–8×；AMD 结果多数接近 baseline（0.89–1.18×）。必须同时看成功率：少数快速候选不能掩盖大量任务未通过 correctness。
- **文档与推理消融：** extended reasoning 提高部分复杂任务成功率，但需要更多 token 和迭代；提供相关示例可提高若干任务成功率，例如 PLENA MQA（GPT-5.2）从 1/5 至 4/5，说明 ISA 文档和参考 kernel 是能力的重要组成。
- **CPU 扩展：** GPT-5.2 对 BOOM 10/10 任务生成了正确实现；Quicksort 达编译器 baseline 的 **1.63×**，Radix sort 只有 **0.12×**，说明 correctness 成功与性能成功必须分开计量。

## 🔍 评议、边界与迁移

- **贡献：** 将 Agentic close-to-metal generation 的 benchmark 扩展到成熟 GPU CUDA 之外，显式覆盖异构 ISA、工具调用、诊断反馈和系统集成层级。
- **主要限制：** 结果受硬件文档、prompt token、tool API、模拟器/设备可用性、容差定义和各平台 baseline 影响；correctness 主要是数值验证，不是形式证明。不同 ISA 的任务也非严格等难度交叉对照。
- **人类专家对比：** Coral depthwise-convolution 案例中，Agent 相对 compiler baseline 在 C1 为 2.5×，人工优化为 20×；C2/C3 Agent 反而低于 baseline。胜过 compiler 不代表接近专家上限。
- **对 SCALE_Forge 的启示：** 硬件 specification 与 tools 作为实验条件版本化；分开记录任务可评估、编译成功、语义正确、性能比和预算；backend 适配评估要覆盖 Level 1→2→3 难度曲线，而非单 kernel 演示。

## Review Questions

1. 后端规范能否以 Agent 可检索、但带版本和来源的结构化资源暴露？
2. 对精度容差、编译器 baseline 与测量后端，如何使跨芯片结果仍可解释？
3. 硬件、任务子集和编译配置改变时，哪些结论仍可比较，哪些必须重新测量？

## 价值评估

**阅读价值：高。** 对 Agent tools、低层代码生成、硬件文档与难度分层基准很有参考；CUDA 专属闭环的结论不能无条件外推。

**状态：** ✅ 已精读（2026-10-15）

## 核对依据与边界（2026-10-15）

本次取得的 PDF 首页版本与本页声明的 2603.08721v2 一致；检查结果数字与方法边界，统一复读问题及价值评估格式。这里的“已精读”是原有阅读记录，不表示本次重新独立复现了所有实验。
