# AmgX: A Library for GPU Accelerated Algebraic Multigrid and Preconditioned Iterative Methods | SIAM Journal on Scientific Computing | Vol. 37, No. 5 | Society for Industrial and Applied Mathematics

**Authors:** M. Naumov, M. Arsaev, P. Castonguay, J. Cohen, J. Demouth, J. Eaton, S. Layton, N. Markovskiy, I. Reguly, N. Sakharnykh, V. Sellappan, and R. Strzodka

**DOI:** [10.1137/140980260](https://doi.org/10.1137/140980260)

**Source PDF:** `140980260.pdf`

---

## Abstract

_Not available_

## Summary

**核心问题：** AMGX：GPU加速代数多重网格（AMG）和预条件迭代求解器库——如何在GPU上高效实现AMG？

**方法：** 开发了AMGX库：在CUDA GPU上实现全套AMG算法（经典AMG、聚合AMG等），提供灵活的求解器配置和与现有CFD代码的接口。支持多GPU分布并行。

**关键结果：**
- 实现了GPU上AMG全套组件的高效CUDA内核，包括setup和solve阶段
- 在单GPU上比CPU实现加速8-10倍，多GPU扩展良好
- 提供了灵活的嵌套求解器和复合预条件框架，可作为CFD代码的即插即用线性求解器

**与你工作的相关性：** GPU加速线性求解器（AMG）是HPC框架中最关键的组件之一，AMGX库可直接评估集成。

**状态：** ✅ 完整摘要
