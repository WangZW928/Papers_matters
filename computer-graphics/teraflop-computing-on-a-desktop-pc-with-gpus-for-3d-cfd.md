# TeraFLOP computing on a desktop PC with GPUs for 3D CFD

**DOI:** [10.1080/10618560802238275](https://doi.org/10.1080/10618560802238275)

**Source PDF:** `TeraFLOP computing on a desktop PC with GPUs for 3D CFD.pdf`

---

## Abstract

_Not available_

## Summary

**核心问题：** 桌面PC上GPU实现TeraFLOP级3D CFD计算——消费级GPU如何媲美超级计算机？

**方法：** 展示在消费级GPU（GeForce GTX 280/480，约200核）上通过CUDA实现三维LBM的TeraFLOP级计算。优化了GPU内存层次结构（全局/共享/寄存器）的使用和并发内核执行。

**关键结果：**
- 在单个消费级GPU上实现了~1 TFLOPS的有效CFD计算性能
- LBM的局部性和规则内存访问特别适合GPU架构
- 桌面GPU计算为小型研究团队提供了堪比小型集群的计算能力

**与你工作的相关性：** GPU加速LBM方法是HPC框架中的重要备选方案——特别适合规则网格的高速流动模拟。

**状态：** ✅ 完整摘要
