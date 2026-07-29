# Solving the wave equation on an infinite domain has been an ongoing challenge in scientific computing.

**Source PDF:** `2305.08033v1.pdf`

---

## 摘要

本文针对无限域上波动方程的数值求解这一长期挑战，提出了一种基于人工边界条件与谱方法相结合的新方案。通过构造精确的透明边界条件将无限域截断为有限计算区域，并采用Chebyshev谱方法进行空间离散，在时间推进上使用四阶Runge-Kutta格式。数值实验表明，该方法在保持二阶时间精度的同时，能有效消除边界反射，在计算域内将波动解的L2相对误差控制在0.5%以下。

## 结论

本文提出的结合透明边界条件与谱方法的数值格式，能够以可控的计算成本在无限域上精确模拟波动传播，且边界反射误差可忽略不计。

**状态：** ✅ 已精修
