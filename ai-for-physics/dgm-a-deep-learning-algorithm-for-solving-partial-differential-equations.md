# DGM: A deep learning algorithm for solving partial differential equations

**Authors:** Justin Sirignano

**DOI:** [10.1016/j.jcp.2018.08.029](https://doi.org/10.1016/j.jcp.2018.08.029)

**Source PDF:** `1-s2.0-S0021999118305527-main.pdf`

---

## 摘要

本文提出了一种名为深度伽辽金方法（DGM）的深度学习算法，用于求解高维偏微分方程（PDE）。该方法利用深度神经网络近似PDE的解，并通过随机梯度下降优化损失函数，从而避免了传统网格方法的维度灾难。实验表明，DGM在求解包括Black-Scholes方程和Hamilton-Jacobi-Bellman方程在内的多个高维PDE时，能够达到与解析解或数值参考解一致的精度，且计算效率随维度增长保持稳定。

## 结论

DGM算法能够有效求解高维非线性PDE，其精度与经典数值方法相当，且计算成本不随维度指数增长，为金融工程、物理模拟等领域的高维问题提供了可行的数值求解方案。

**状态：** ✅ 已精修
