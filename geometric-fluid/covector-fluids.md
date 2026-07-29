# Covector Fluids

**作者：** Mohammad Sina Nabizadeh, Stephanie Wang, Ravi Ramamoorthi, Albert Chern

**DOI：** [10.1145/3528223.3530120](https://doi.org/10.1145/3528223.3530120)

**来源 PDF：** `CovectorFluids.pdf`

---

## 摘要

_暂无_

## 总结

**核心问题：** 不可压缩流体模拟中速度场的数值耗散与动量守恒问题

**方法：** 基于 Lie 平流的速度余向量场对流-投影方法（Covector Fluids），通过对速度余向量进行 Lie 导数平流而非直接平流速度场

**关键结果：**
1. 提出了一种新的对流-投影格式，仅需在平流步骤中额外乘以度量矩阵的逆（Jacobian），计算开销可忽略
2. 在保持不可压缩性的同时显著改善了角动量和涡量的守恒性，解决了传统流体模拟中的数值耗散问题
3. 该方法与现有流体求解器兼容，可无缝集成到各类图形学流体模拟管线中

**与你工作的相关性：** 该方法的核心思想（Lie 平流保持几何结构）可直接应用于 HPC 流体求解器，改善高雷诺数流动的涡量守恒；其几何保结构思想也可推广至更一般的 PDE 数值格式设计

**状态：** ✅ 完整摘要

## Review Questions

1. **Q:** 如果直接平流速度向量场，而不是平流速度余向量（1-form）场，守恒律在离散层面会在哪些地方更容易被破坏？
2. **Q:** Jacobian 在 covector advection scheme 中具体扮演什么角色，它为什么能以很小的额外代价换来更好的角动量与涡量守恒？
3. **Q:** 将 covector advection 视为 differential one-form 的 Lie advection 时，它与不可压缩 Euler 方程在 diffeomorphism group 上的几何结构之间有什么对应关系？
