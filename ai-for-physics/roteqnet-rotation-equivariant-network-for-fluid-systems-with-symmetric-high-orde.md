# RotEqNet: Rotation-equivariant network for fluid systems with symmetric high-order tensors

**Authors:** Liyao Gao

**DOI:** [10.1016/j.jcp.2022.111205](https://doi.org/10.1016/j.jcp.2022.111205)

**Source PDF:** `1-s2.0-S0021999122002674-main.pdf`

---

## 摘要

本文针对流体系统中对称高阶张量场的旋转等变建模问题，提出了一种名为RotEqNet的旋转等变神经网络架构。该方法通过设计基于张量代数运算的等变卷积层，使网络能够自动保持对任意旋转操作的等变性，从而在无需数据增强的情况下有效学习流体应力张量等对称高阶张量场。在合成湍流数据和真实流体模拟数据上的实验表明，RotEqNet相比传统CNN在张量场预测精度上提升约30%，且所需训练数据量减少50%以上。

## 结论

本文证明，通过显式编码旋转等变性，RotEqNet能够以更少的数据和更高的精度学习流体系统中的对称高阶张量场，为基于深度学习的流体力学建模提供了新的有效范式。

**状态：** ✅ 已精修
