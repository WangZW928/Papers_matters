# Sparse Matrix Solvers on the GPU: Conjugate Gradients and Multigrid

**Authors:** Jeff Bolz, Ian Farmer, Eitan Grinspun, Peter Schröder

**Journal:** ACM Transactions on Graphics (SIGGRAPH), 2003

**DOI:** [10.1145/882262.882292](https://doi.org/10.1145/882262.882292)

**Source PDF:** `matrix free 1.pdf`

---

## Abstract

_Not available_

## Summary

**核心问题：** GPU上稀疏矩阵求解器：共轭梯度法和多重网格法——早期GPU通用计算在数值代数中的应用

**方法：** 开创性工作：在早期GPU（可编程着色器时代）上实现共轭梯度法（CG）和多重网格法，将稀疏矩阵-向量乘和光滑化操作映射到GPU的纹理和片段处理管线。

**关键结果：**
- 首次展示了GPU在稀疏线性代数中的巨大加速潜力
- CG和多重网格的GPU实现比CPU实现加速数倍
- 为后续GPGPU在科学计算中的应用奠定了基础框架

**与你工作的相关性：** GPU加速线性求解器的先驱性工作，其设计思想对HPC框架有历史参考价值。

**状态：** ✅ 完整摘要
