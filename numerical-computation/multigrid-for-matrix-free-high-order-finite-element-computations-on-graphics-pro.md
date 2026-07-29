# Multigrid for Matrix-Free High-Order Finite Element Computations on Graphics Processors

**Journal:** ACM Transactions on Parallel Computing, 2019

**DOI:** [10.1145/3322813](https://doi.org/10.1145/3322813)

**Source PDF:** `matrix free 3.pdf`

---

## Abstract

_Not available_

## Summary

**核心问题：** 矩阵无关高阶有限元的GPU多重网格加速——如何结合高阶方法和多重网格的最优复杂度？

**方法：** 提出GPU加速的矩阵无关多重网格方法用于高阶有限元：利用sum-factorization技术高效计算单元矩阵-向量乘，多级网格通过p-多重网格和h-多重网格组合实现。

**关键结果：**
- sum-factorization使高阶单元的矩阵-向量乘复杂度从O(p^6)降至O(p^4)
- GPU加速的多重网格在三维高阶有限元中实现了近线性复杂度
- p-多重网格 + h-多重网格的组合策略平衡了收敛性和并行效率

**与你工作的相关性：** 矩阵无关多重网格方法可参考用于HPC框架中高阶离散的最优复杂度求解。

**状态：** ✅ 完整摘要
