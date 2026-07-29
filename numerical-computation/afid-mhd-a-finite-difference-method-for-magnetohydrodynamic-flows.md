# AFiD-MHD: A finite difference method for magnetohydrodynamic flows

**Authors:** Shujaut H. Bader

**DOI:** [10.1016/j.jcp.2024.113658](https://doi.org/10.1016/j.jcp.2024.113658)

**Source PDF:** `1-s2.0-S0021999124009069-main.pdf`

---

## Abstract

_Not available_

## Summary

**核心问题：** AFiD-MHD：基于有限差分的磁流体动力学（MHD）Rayleigh-Bénard对流求解器——如何保证磁场无散条件的高精度满足？

**方法：** 在AFiD代码框架上扩展MHD能力：交错网格二阶有限差分 + 三阶Runge-Kutta/Crank-Nicolson时间推进。磁场散度清洁采用面中心标量投影法（物理空间精确清洁）和Lagrange乘子法两种方案。额外实现矢量势法和准静态磁对流模块。

**关键结果：**
- 标量散度清洁可将divB降至机器零，且避免了棋盘格不稳定性
- 求解器成功验证了旋转和非旋转MHD对流、准静态磁对流的多个标准算例
- 在2048³网格上展现出良好的强扩展性（至6000核）

**与你工作的相关性：** AFiD-MHD的高精度MHD格式和扩展性策略可参考用于HPC框架的MHD求解器开发。

**状态：** ✅ 完整摘要
