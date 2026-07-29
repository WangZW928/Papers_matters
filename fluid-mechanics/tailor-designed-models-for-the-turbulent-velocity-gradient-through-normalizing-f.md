# Tailor-Designed Models for the Turbulent Velocity Gradient through Normalizing Flow

**DOI:** [10.1103/PhysRevLett.133.184001](https://doi.org/10.1103/PhysRevLett.133.184001)

**Source PDF:** `PhysRevLett.133.184001.pdf`

---

## Abstract

_Not available_

## Summary

**核心问题：** 湍流速度梯度张量的归一化流定制模型——如何用可逆神经网络精确建模湍流小尺度的统计行为？

**方法：** 机器学习方法：利用归一化流（normalizing flow）可逆神经网络直接学习湍流速度梯度张量的概率分布，通过物理约束（如不可压缩条件、Galilean不变性等）确保模型一致性。

**关键结果：**
- 归一化流模型精确再现了湍流速度梯度张量的完整统计分布，包括各向异性和间歇性
- 物理约束的嵌入显著提高了模型在小样本条件下的泛化能力
- 模型生成的速度梯度统计量（偏斜度、平坦度、Lundberg度量等）与DNS数据一致

**与你工作的相关性：** 数据驱动的湍流建模方法可参考用于HPC框架中的湍流闭合模型开发。

**状态：** ✅ 完整摘要
