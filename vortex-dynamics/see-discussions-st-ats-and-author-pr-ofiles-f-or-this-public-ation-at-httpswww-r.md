# See discussions, st ats, and author pr ofiles f or this public ation at : https://www .researchgate.ne t/public ation/342027470

**DOI:** [nverses](https://doi.org/nverses)

**Source PDF:** `RoeNet.pdf`

---

## Abstract

_Not available_

## Summary

**核心问题：** RoeNet：基于神经网络的PDE残差预测方法——如何用数据驱动方法替代经典PDE数值格式中的数值通量计算？

**方法：** 提出RoeNet架构：用神经网络学习PDE控制方程中的残差（数值通量），替代经典数值格式中的物理模型。网络从数据中自动学习通量函数，无需预设解析形式。

**关键结果：**
- RoeNet在多种PDE系统（包括Burgers方程、浅水方程等）中生成了准确的长期预测
- 神经网络通量天然保证守恒性，因为它在通量差分形式上训练
- 数据驱动的通量比解析通量在非理想条件下更具鲁棒性

**与你工作的相关性：** 数据驱动的数值通量方法可参考用于HPC框架中替代传统物理模型的代理求解器。

**状态：** ✅ 完整摘要
