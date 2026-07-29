# Uncertainty quantification for DeepONets with ensemble Kalman inversion

**Authors:** Andrew Pensoneault

**DOI:** [10.1016/j.jcp.2024.113670](https://doi.org/10.1016/j.jcp.2024.113670)

**Source PDF:** `1-s2.0-S0021999124009185-main.pdf`

---

## 摘要

本文针对DeepONet（深度算子网络）在物理信息学习中的不确定性量化问题，提出将集合卡尔曼反演（ensemble Kalman inversion, EKI）方法集成到DeepONet的训练与推断过程中。通过在多个基准偏微分方程（如Burgers方程、Darcy流方程）上的数值实验，该方法能够有效估计模型预测的后验不确定性，并在噪声观测下获得比标准DeepONet更可靠的预测区间，同时保持相当的预测精度。

## 结论

集合卡尔曼反演能够为DeepONet提供一种高效且可扩展的不确定性量化框架，使得在数据有限或观测含噪声时，模型不仅能给出点预测，还能输出具有统计意义的不确定性估计，从而提升对物理系统预测的可靠性。

**状态：** ✅ 已精修
