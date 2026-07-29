# A Fast, Matrix-free Implicit Method for Computing Low Mach Number Flows on Unstructured Grids

**Authors:** Hong Luo, Joseph D. Baum, Rainald Löhner

**Journal:** International Journal of Computational Fluid Dynamics, 2000

**DOI:** [10.1080/10618560008940720](https://doi.org/10.1080/10618560008940720)

**Source PDF:** `A Fast, Matrix-free Implicit Method for Computing Low Mach Number Flows on Unstructured Grids (LUO, HONG BAUM, JOSEPH D. LÖHNER, RAINALD) (Z-Library).pdf`

---

## Abstract

_Not available_

## Summary

**核心问题：** 低马赫数流动在非结构网格上的矩阵无关隐式方法——如何高效求解低速可压缩/不可压缩流动？

**方法：** 开发矩阵无关（matrix-free）的隐式Newton-Krylov方法用于低马赫数流动：基于近似Newton法+GMRES，利用有限差分近似Jacobian-向量积，避免显式构造和存储Jacobian矩阵。结合低马赫数预处理克服刚性问题。

**关键结果：**
- 矩阵无关方法内存开销远低于传统稀疏矩阵方法，适合大规模问题
- 低马赫数预处理有效解决了低速可压缩流的刚性问题
- 方法在多种非结构网格上验证了收敛性和效率

**与你工作的相关性：** 矩阵无关Newton-Krylov方法可参考用于HPC框架中的大规模隐式求解器。

**状态：** ✅ 完整摘要
