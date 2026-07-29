# A Matrix-free GMRES Algorithm on GPU Clusters for Implicit Large Eddy Simulation

**Authors:** Eduardo Jourdan, Z. J. Wang

**Journal:** AIAA Scitech 2021

**DOI:** [10.2514/6.2021-1837](https://doi.org/10.2514/6.2021-1837)

**Source PDF:** `GPU_GMRES_2021_online.pdf`

---

## Abstract

_Not available_

## Summary

**核心问题：** GPU集群上用于隐式大涡模拟（LES）的矩阵无关GMRES算法

**方法：** 提出在GPU集群上实现的矩阵无关GMRES算法用于隐式LES：结合MPI多节点通信和CUDA GPU计算，优化稀疏矩阵-向量乘和全局约简操作的GPU内核。

**关键结果：**
- 在GPU集群上实现了高效的矩阵无关GMRES，性能提升显著
- GPU加速了每次GMRES迭代中的稀疏矩阵-向量乘（关键瓶颈）
- MPI+CUDA混合并行策略有效解决了LES中的大规模隐式系统求解

**与你工作的相关性：** GPU集群上的矩阵无关GMRES算法可参考用于HPC框架的大规模隐式求解器。

**状态：** ✅ 完整摘要
