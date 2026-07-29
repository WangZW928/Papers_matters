# An immersed boundary method using online sequential data assimilation

**Authors:** Miguel M. Valero

**DOI:** [10.1016/j.jcp.2024.113697](https://doi.org/10.1016/j.jcp.2024.113697)

**Source PDF:** `1-s2.0-S0021999124009458-main.pdf`

---

## Abstract

_Not available_

## Summary

**核心问题：** 基于在线顺序数据同化（EnKF）改进浸入边界法精度——能否用传感器数据实时修正IBM的壁面模型误差？

**方法：** 提出物理信息注入（physics-infused）策略：用集合卡尔曼滤波（EnKF）在线同化壁面应力和无滑移条件的观测数据，同时更新流场状态和IBM惩罚参数，提高低分辨率IBM的精度。

**关键结果：**
- EnKF同化显著减小了低分辨率IBM与高分辨率DNS之间的壁面摩擦系数和湍流统计量偏差
- Q准则显示同化后的湍流结构与DNS具有相似的相干组织
- 方法对网格分辨率和传感器位置变化表现出良好的鲁棒性

**与你工作的相关性：** 基于数据同化的数值方法增强策略可参考用于HPC框架中的实时仿真和数字孪生应用。

**状态：** ✅ 完整摘要
