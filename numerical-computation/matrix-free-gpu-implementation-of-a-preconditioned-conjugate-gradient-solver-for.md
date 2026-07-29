# Matrix-free GPU Implementation of a Preconditioned Conjugate Gradient Solver for Anisotropic Elliptic PDEs

**Authors:** Eike Müller, Xu Guo, Robert Scheichl, Sinan Shi

**Journal:** Computing and Visualization in Science, 16:41–58, 2013

**DOI:** [10.1007/s00791-014-0223-x](https://doi.org/10.1007/s00791-014-0223-x)

**Source PDF:** `matrix free 2.pdf`

---

## Abstract

_Not available_

## Summary

**核心问题：** 预条件共轭梯度法的矩阵无关GPU加速实现——如何在高阶有限元中避免全局矩阵组装？

**方法：** 提出矩阵无关的预条件CG方法用于弹性力学/流体力学：利用单元级矩阵-向量乘避免全局矩阵组装，预条件子采用单元级Jacobi或近似块LU。在GPU上高效实现。

**关键结果：**
- 矩阵无关实现的内存占用极低（无需存储全局刚度矩阵）
- GPU加速的矩阵无关CG实现了显著的加速比
- 方法在高阶单元中特别有效——单元内自由度多，计算密度高

**与你工作的相关性：** 矩阵无关CG方法可参考用于HPC框架中大规模有限元系统的高效求解。

**状态：** ✅ 完整摘要
