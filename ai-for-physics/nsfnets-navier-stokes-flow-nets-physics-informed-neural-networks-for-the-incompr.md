# NSFnets (Navier-Stokes flow nets): Physics-informed neural networks for the incompressible Navier-Stokes equations

**Authors:** Xiaowei Jin

**DOI:** [10.1016/j.jcp.2020.109951](https://doi.org/10.1016/j.jcp.2020.109951)

**Source PDF:** `1-s2.0-S0021999120307257-main.pdf`

---

## 摘要

本文针对不可压缩Navier-Stokes方程的数值求解问题，提出了一种基于物理信息神经网络（PINNs）的NSFnets方法。该方法将控制方程、边界条件和初始条件直接嵌入神经网络的损失函数中，无需网格生成即可求解流场。在多个经典流动问题（如方腔驱动流、圆柱绕流）上的测试表明，NSFnets能够以高精度预测速度场和压力场，且与数值解或解析解吻合良好。

## 结论

本文证明了NSFnets能够在不依赖传统数值离散方法的情况下，有效求解不可压缩Navier-Stokes方程，为复杂流动问题的无网格求解提供了一种可行的深度学习方案。

**状态：** ✅ 已精修
