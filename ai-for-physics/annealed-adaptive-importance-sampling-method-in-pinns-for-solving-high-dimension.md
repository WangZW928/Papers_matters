# Annealed adaptive importance sampling method in PINNs for solving high dimensional partial differential equations

**Authors:** Zhengqi Zhang

**DOI:** [10.1016/j.jcp.2024.113561](https://doi.org/10.1016/j.jcp.2024.113561)

**Source PDF:** `1-s2.0-S002199912400809X-main.pdf`

---

## 摘要

本文针对物理信息神经网络（PINNs）求解高维偏微分方程（PDEs）时训练点采样效率低的问题，提出了一种退火自适应重要性采样方法。该方法通过迭代更新采样分布，使训练点更集中于PDE残差较大的区域，并引入退火策略避免采样分布过早收敛。在100维的Allen-Cahn方程和Black-Scholes方程等数值实验中，该方法相比均匀采样和传统自适应采样，将PDE残差降低了约一个数量级，同时减少了所需训练点数。

## 结论

本文提出的退火自适应重要性采样方法能有效提升PINNs求解高维PDEs的精度和效率，通过动态聚焦于高残差区域，显著降低了数值误差。

**状态：** ✅ 已精修
