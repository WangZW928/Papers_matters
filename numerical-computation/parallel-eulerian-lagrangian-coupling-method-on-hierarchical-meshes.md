# Parallel Eulerian-Lagrangian coupling method on hierarchical meshes

**Authors:** Tim Wegmann

**DOI:** [10.1016/j.jcp.2024.113509](https://doi.org/10.1016/j.jcp.2024.113509)

**Source PDF:** `1-s2.0-S0021999124007575-main.pdf`

---

## Abstract

_Not available_

## Summary

**核心问题：** 层级网格上欧拉-拉格朗日两相耦合的高效并行方法——喷雾模拟中如何消除并行通信瓶颈？

**方法：** 提出交错时间步执行模式（interleaved time step execution）+ 非阻塞通信，将欧拉和拉格朗日求解子步交错执行以避免通信障碍。结合动态负载平衡（基于运行时测量的DCW）和分层分区策略（PLS）。

**关键结果：**
- 交错执行模式相比传统顺序方案提升12%-50%性能，取决于并行度和喷雾-网格比
- 动态单元权重（DCW）比精心调优的静态权重减少额外15%的运行时间
- 分层分区（PLS）带来最高89%的性能提升；在262144 MPI进程上达到78%的并行效率

**与你工作的相关性：** 交错执行+动态负载平衡的并行策略可直接参考用于HPC框架中的欧拉-拉格朗日耦合求解器。

**状态：** ✅ 完整摘要
