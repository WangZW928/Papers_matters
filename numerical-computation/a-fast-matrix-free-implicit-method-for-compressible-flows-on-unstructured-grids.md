# A Fast, Matrix-free Implicit Method for Compressible Flows on Unstructured Grids

**Authors:** Hong Luo, Joseph D. Baum, Rainald Löhner

**Journal:** Journal of Computational Physics, 1998

**DOI:** [10.1006/jcph.1998.6076](https://doi.org/10.1006/jcph.1998.6076)

**Source PDF:** `Luo 等 - 1998 - A fast, matrix-free implicit method for compressible flows on unstructured grids.pdf`

---

## Abstract

_Not available_

## Summary

**核心问题：** 可压缩流在非结构网格上的矩阵无关隐式方法——经典LUO方法（1998）

**方法：** 提出矩阵无关的隐式方法（经典的LUO方法）：使用近似Newton法 + GMRES求解隐式Euler/Navier-Stokes方程，利用颜色分组（coloring）实现非结构网格上的有限差分Jacobian-向量积。

**关键结果：**
- 矩阵无关方法避免了显式Jacobian存储，内存需求大幅降低
- 颜色分组技术使非结构网格上的有限差分逼近高效且正确
- 方法成功应用于从低速到超音速的广泛可压缩流模拟

**与你工作的相关性：** Luo的矩阵无关方法是现代HPC CFD的基础，其设计思想直接适用于HPC框架。

**状态：** ✅ 完整摘要
