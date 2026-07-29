# Dynamically regularized Lagrange multiplier schemes with energy dissipation for the incompressible Navier-Stokes equations

**Authors:** Cao-Kha Doan

**DOI:** [10.1016/j.jcp.2024.113550](https://doi.org/10.1016/j.jcp.2024.113550)

**Source PDF:** `1-s2.0-S0021999124007988-main.pdf`

---

## Abstract

_Not available_

## Summary

**核心问题：** 不可压缩 Navier-Stokes 方程的 Lagrange 乘子方法存在唯一性问题和时间步长限制。如何构造无条件能量稳定且允许大步长的新型格式？

**方法：** 引入包含原始能量、Lagrange 乘子和正则化参数的动态方程，将 NS 方程重构为等价系统。基于 BDF 方法显式处理非线性对流项，推导了一阶和二阶 DRLM 格式，配合 MAC 空间离散实现全离散能量稳定性。

**关键结果：**
- DRLM 格式无条件满足能量耗散律，正则化参数确保 Lagrange 乘子唯一性
- 每时间步仅需解两个广义 Stokes 系统 + 一个二次方程，线性易实现
- 2D/3D 数值实验验证了收敛性和能量稳定性

**与你工作的相关性：** 能量稳定的时间推进格式设计模式可参考用于 HPC 框架中的不可压缩流求解器。

**状态：** ✅ 完整摘要

