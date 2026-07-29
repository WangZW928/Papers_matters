# GPGPU-based heterogeneous parallel implementation of direct discontinuous Galerkin methods

**Authors:** Jiaxin Wang

**DOI:** [10.1016/j.matcom.2024.09.034](https://doi.org/10.1016/j.matcom.2024.09.034)

**Source PDF:** `GPGPU-DG.pdf`

---

## Abstract

_Not available_

## Summary

**核心问题：** 间断Galerkin（DG）方法的GPU异构并行实现——如何在GPU上充分挖掘DG方法的并行潜力？

**方法：** 提出GPGPU加速的DG方法：利用DG方法的局部性（单元内独立计算），将体积分、面积分和限制器映射到CUDA线程块。优化内存访问模式和共享内存使用以提高GPU占用率。

**关键结果：**
- GPU DG相比CPU实现加速20-50倍（取决于问题规模和多项式阶数）
- DG方法的高计算密度（每个单元大量FLOP）特别适合GPU架构
- 多GPU扩展实现了近乎线性的加速——DG的弱耦合特性适合域分解

**与你工作的相关性：** DG方法的GPU加速策略可直接参考用于HPC框架中的高阶CFD求解器。

**状态：** ✅ 完整摘要
