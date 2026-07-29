# Extended Lagrangian approach for the numerical study of multidimensional dispersive waves: Applications to the Serre-Green-Naghdi equations

**Authors:** Sergey Tkachenko

**DOI:** [10.1016/j.jcp.2022.111901](https://doi.org/10.1016/j.jcp.2022.111901)

**Source PDF:** `1-s2.0-S0021999122009640-main.pdf`

---

## Abstract

_Not available_

## Summary

**核心问题：** 如何处理多维非线性色散浅水波方程的数值求解——既要保双曲性（允许间断初值），又要准确捕获色散效应。

**方法：** 采用 Favrie & Gavrilyuk (2017) 的扩展 Lagrangian 方法：将原始的 Euler-Lagrange 方程通过增加松弛变量转化为无条件双曲的近似系统。针对 SGN 方程实现了二阶 IMEX ARS(2,2,2) 格式，隐式处理色散项，显式处理双曲部分。

**关键结果：**
- 推导出了 Galilean 不变且无条件双曲的近似系统，同时保持色散精度
- 1D 和 2D dam-break 问题数值解与精确解和其他数值方法高度一致
- 二阶 IMEX 仅需 800×800 网格即可达到一阶 splitting 方法 10000×10000 网格的精度（~156× 网格效率提升）

**与你工作的相关性：** 扩展 Lagrangian 方法将非双曲色散系统转化为双曲系统的思路，对你在 HPC 框架中处理 multiphysics 耦合时的数学模型选择有参考价值；IMEX 格式的设计模式可作为你框架中时间积分模块的参考。

**状态：** ✅ 完整摘要


## Review Questions

### 🤔 Questions
1. **Q:** How does the extended Lagrangian method convert a non-hyperbolic dispersive PDE system into an unconditionally hyperbolic one through the introduction of relaxation variables, and what determines the choice of relaxation time scales?
2. **Q:** Why is the IMEX splitting strategy (implicit dispersive terms, explicit hyperbolic terms) well-suited for the extended Serre-Green-Naghdi system, and how does the CFL condition for the explicit hyperbolic part relate to the gravity wave speed rather than the dispersive stiffness?
3. **Q:** How does the Galilean invariance of the extended system affect the accuracy of solutions involving moving reference frames or rotating coordinates, and why is this property essential for simulating ship wakes or coastal wave transformation?
