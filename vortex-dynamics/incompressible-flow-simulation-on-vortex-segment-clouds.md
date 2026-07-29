# Incompressible Flow Simulation on Vortex Segment Clouds

**Authors:** Shiying Xiong, Rui Tao, Yaorui Zhang, Fan Feng, and Bo Zhu

**DOI:** [10.1145/3450626.3459865](https://doi.org/10.1145/3450626.3459865)

**Source PDF:** `vortex_segment.pdf`

---

## Abstract

_Not available_

## Summary

**核心问题：** 涡段云方法的高效不可压缩流动模拟——如何用涡段（而非粒子或网格）离散化涡量场？

**方法：** 提出基于涡段云（vortex segment cloud）的拉格朗日涡方法：将涡量场离散为一组涡段，利用Biot-Savart定律计算速度场，涡段随流场对流和拉伸演化。引入快速多极方法加速N-body计算。

**关键结果：**
- 涡段云方法在涡量守恒和拓扑保持方面优于经典涡粒子方法
- 成功模拟了涡环碰撞、涡管重联等复杂涡动力学过程
- 计算效率接近粒子方法但精度更高——涡段天然表示涡线的方向性

**与你工作的相关性：** 涡方法的离散格式和快速算法可参考用于HPC框架中的涡动力学模拟。

**状态：** ✅ 完整摘要
