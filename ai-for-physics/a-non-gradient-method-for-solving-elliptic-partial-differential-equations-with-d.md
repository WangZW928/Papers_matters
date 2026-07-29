# A non-gradient method for solving elliptic partial differential equations with deep neural networks

**Authors:** Yifan Peng

**DOI:** [10.1016/j.jcp.2022.111690](https://doi.org/10.1016/j.jcp.2022.111690)

**Source PDF:** `1-s2.0-S0021999122007537-main.pdf`

---

## 摘要

本文针对椭圆型偏微分方程（PDE）的数值求解问题，提出了一种无需计算梯度的深度神经网络方法。该方法通过将PDE离散化为线性系统，并利用神经网络直接拟合解函数，避免了传统基于梯度反向传播的优化过程。在二维泊松方程和亥姆霍兹方程等典型算例上，该方法在网格节点上的均方误差达到10^{-4}量级，且训练时间较传统PINN方法缩短约50%。

## 结论

本文提出的非梯度深度神经网络方法能够高效求解椭圆型PDE，其精度与有限差分法相当，但无需计算损失函数的梯度，显著降低了训练复杂度。

**状态：** ✅ 已精修
