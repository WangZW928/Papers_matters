# Taylor series error correction network for super-resolution of discretized partial differential equation solutions

**Authors:** Wenzhuo Xu

**DOI:** [10.1016/j.jcp.2024.113569](https://doi.org/10.1016/j.jcp.2024.113569)

**Source PDF:** `1-s2.0-S0021999124008179-main.pdf`

---

## 摘要

本文针对离散化偏微分方程数值解的超分辨率重建问题，提出了一种基于泰勒级数误差校正的神经网络方法。该方法通过将泰勒展开的局部截断误差显式嵌入网络结构，在粗网格解上重建高分辨率场，并在多个经典PDE基准（如Burgers方程、对流扩散方程）上实现了比传统插值和纯数据驱动方法更低的L2相对误差（平均降低30%-50%），同时保持了物理一致性。

## 结论

实验表明，所提出的泰勒级数误差校正网络能够有效利用PDE离散化的局部误差结构，在粗网格到细网格的超分辨率任务中显著提升重建精度，且泛化能力优于纯数据驱动模型。

**状态：** ✅ 已精修
