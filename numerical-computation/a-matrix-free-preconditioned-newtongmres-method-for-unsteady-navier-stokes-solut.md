# A Matrix-free Preconditioned Newton/GMRES Method for Unsteady Navier-Stokes Solutions

**Authors:** Ning Qin, D. K. Ludlow, S. T. Shaw

**Journal:** International Journal for Numerical Methods in Fluids, 2000

**DOI:** [10.1002/(SICI)1097-0363(20000530)33:2<223::AID-FLD10>3.0.CO;2-V](https://doi.org/10.1002/(SICI)1097-0363(20000530)33:2<223::AID-FLD10>3.0.CO;2-V)

**Source PDF:** `Numerical Methods in Fluids - 2000 - Qin - A matrix‐free preconditioned Newton GMRES method for unsteady Navier Stokes.pdf`

---

## Abstract

_Not available_

## Summary

**核心问题：** 非定常Navier-Stokes的矩阵无关预条件Newton-GMRES方法

**方法：** 提出矩阵无关的预条件Newton-GMRES方法用于非定常不可压缩NS方程：使用二阶BDF时间离散 + Newton线性化 + 预条件GMRES求解每步线性系统。预条件子基于近似块LU分解。

**关键结果：**
- 矩阵无关方法在非定常NS中展示了良好的收敛性
- 预条件子对收敛速度至关重要——近似块LU比简单对角预条件快数倍
- 方法的内存开销远低于需要存储Jacobian的传统Newton方法

**与你工作的相关性：** 矩阵无关Newton-GMRES方法可直接应用于HPC框架中非定常NS求解器的开发。

**状态：** ✅ 完整摘要
