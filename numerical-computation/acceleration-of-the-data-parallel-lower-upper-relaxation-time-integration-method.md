# Acceleration of the data-parallel lower-upper relaxation time-integration method on GPU for an unstructured CFD solver

**Authors:** Paul Zehner

**DOI:** [10.1016/j.compfluid.2023.105842](https://doi.org/10.1016/j.compfluid.2023.105842)

**Source PDF:** `DPLUR.pdf`

---

## Abstract

_Not available_

## Summary

**核心问题：** 数据并行LU松弛（DPLUR）方法的时间积分加速——如何在不损害并行效率的前提下加速隐式时间推进？

**方法：** 提出数据并行LU松弛方法：对隐式时间推进的LU分解进行松弛迭代，将串行的LU扫描转化为数据并行的多次迭代，适合在GPU和分布式系统上实现。

**关键结果：**
- DPLUR在GPU和分布式系统上实现了近线性的并行加速
- 松弛迭代的收敛速度可接受——通常在几十次迭代内达到等效精度
- 方法成功应用于可压缩和非压缩流动的定常和非定常模拟

**与你工作的相关性：** DPLUR的并行化策略可直接参考用于HPC框架中隐式求解器的GPU/分布式加速。

**状态：** ✅ 完整摘要
