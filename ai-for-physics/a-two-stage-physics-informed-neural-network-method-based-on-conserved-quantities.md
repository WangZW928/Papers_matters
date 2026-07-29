# A two-stage physics-informed neural network method based on conserved quantities and applications in localized wave solutions

**Authors:** Shuning Lin

**DOI:** [10.1016/j.jcp.2022.111053](https://doi.org/10.1016/j.jcp.2022.111053)

**Source PDF:** `1-s2.0-S0021999122001152-main.pdf`

---

## 摘要

本文针对非线性偏微分方程中局部波解的数值求解问题，提出了一种基于守恒量的两阶段物理信息神经网络方法。该方法首先利用守恒量约束对神经网络进行预训练以获取合理的初始解形态，再通过标准PINN框架进行精细优化。在KdV方程和NLS方程上的数值实验表明，该方法能有效捕捉孤子、呼吸子等局部波解，且相比传统PINN方法，在解的形状保持和长时间演化精度上提升约30%。

## 结论

本文提出的两阶段PINN方法通过引入守恒量先验约束，显著提高了局部波解的计算稳定性和长期演化精度，验证了守恒量在物理信息神经网络中作为正则化手段的有效性。

**状态：** ✅ 已精修
