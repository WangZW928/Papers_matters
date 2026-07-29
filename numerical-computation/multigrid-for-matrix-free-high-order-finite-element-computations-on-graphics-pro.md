# 面向图形处理器的矩阵无关高阶有限元多重网格计算

**期刊：** ACM Transactions on Parallel Computing，2019

**DOI：** [10.1145/3322813](https://doi.org/10.1145/3322813)

**来源 PDF：** `matrix free 3.pdf`

---

## 摘要

_无可用摘要_

## 总结

**核心问题：** 如何在图形处理器上为矩阵无关高阶有限元构建高效的多重网格加速方案，并兼顾高阶方法的计算效率与多重网格的收敛性。

**方法：** 论文提出了一种面向 GPU 的矩阵无关多重网格方法用于高阶有限元计算：通过 sum-factorization 技术高效完成单元级矩阵-向量乘，并结合 p-多重网格与 h-多重网格实现多层求解。

**关键结果：**
- sum-factorization 将高阶单元的矩阵-向量乘复杂度从 O(p^6) 降至 O(p^4)
- GPU 加速的多重网格在三维高阶有限元中实现了近线性复杂度
- p-多重网格与 h-多重网格的组合策略平衡了收敛性与并行效率

**与你工作的相关性：** 这种矩阵无关多重网格方法可为 HPC 框架中的高阶离散最优复杂度求解提供参考。

**状态：** ✅ 完整摘要

## Review Questions

1. **Q:** sum-factorization 如何将高阶 FEM 算子求值的复杂度从 O(p^{2d}) 降到 O(d p^{d+1})，这种变化对 GPU 上的内存带宽和算术强度意味着什么？
2. **Q:** 为什么在高阶 FEM 中需要将 p-multigrid 与 h-multigrid 结合以获得稳健收敛，而 p-coarsening（降低多项式阶数）与 h-coarsening（粗化网格）在谱半径性质上有何差异？
3. **Q:** 在高多项式阶数下实现无矩阵平滑器（例如 Chebyshev-accelerated Jacobi）时，关键挑战是什么，sum-factorization 的单元局部特性又如何与 multigrid cycles 中的全局通信需求相互作用？
