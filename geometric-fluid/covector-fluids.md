# Covector Fluids

**Authors:** Mohammad Sina Nabizadeh, Stephanie Wang, Ravi Ramamoorthi, and Albert Chern

**DOI:** [10.1145/3528223.3530120](https://doi.org/10.1145/3528223.3530120)

**Source PDF:** `CovectorFluids.pdf`

---

## Abstract

_Not available_

## Summary


**核心问题：** 不可压缩流体模拟中速度场的数值耗散与动量守恒问题

**方法：** 基于Lie平流的速度余向量场对流-投影方法（Covector Fluids），通过对速度余向量进行Lie导数平流而非直接平流速度场

**关键结果：** 
1. 提出了一种新的对流-投影格式，仅需在平流步骤中额外乘以度量矩阵的逆（Jacobian），计算开销可忽略
2. 在保持不可压缩性的同时显著改善了角动量和涡量的守恒性，解决了传统流体模拟中的数值耗散问题
3. 该方法与现有流体求解器兼容，可无缝集成到各类图形学流体模拟管线中

**与你工作的相关性：** 该方法的核心思想（Lie平流保持几何结构）可直接应用于HPC流体求解器，改善高雷诺数流动的涡量守恒；其几何保结构思想也可推广至更一般的PDE数值格式设计

**状态：** ✅ 完整摘要

