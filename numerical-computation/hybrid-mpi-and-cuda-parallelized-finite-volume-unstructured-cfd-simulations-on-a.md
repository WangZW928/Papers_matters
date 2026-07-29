# Hybrid MPI and CUDA Parallelized Finite Volume Unstructured CFD Simulations on a Multi-GPU System

**Authors:** Xi Zhang, Xiaohu Guo, Yue Weng, Xianwei Zhang, Yutong Lu, Zhong Zhao

**Journal:** Future Generation Computer Systems, 139 (2023) 1–16

**DOI:** [10.1016/j.future.2022.09.005](https://doi.org/10.1016/j.future.2022.09.005)

**Source PDF:** `MPI-CUDA-FVM.pdf`

---

## Abstract

_Not available_

## Summary

**核心问题：** MPI+CUDA混合并行有限体积非结构CFD仿真——如何在多GPU节点上高效求解？

**方法：** 开发MPI+CUDA混合并行框架用于非结构有限体积CFD：MPI处理节点间通信（域分解），CUDA处理节点内GPU计算。优化了GPU核函数的内存合并访问和共享内存使用。

**关键结果：**
- 多GPU节点上实现了良好的强/弱扩展性
- GPU加速的关键在于最大化核函数的占用率和内存带宽利用
- MPI+CUDA混合框架比纯MPI（CPU）方案加速可达10倍以上

**与你工作的相关性：** MPI+CUDA混合并行框架是HPC框架中多GPU节点计算的标准范式。

**状态：** ✅ 完整摘要
