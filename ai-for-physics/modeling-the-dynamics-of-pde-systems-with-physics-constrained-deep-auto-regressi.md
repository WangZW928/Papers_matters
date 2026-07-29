# Modeling the dynamics of PDE systems with physics-constrained deep auto-regressive networks

**Authors:** Nicholas Geneva

**DOI:** [10.1016/j.jcp.2019.109056](https://doi.org/10.1016/j.jcp.2019.109056)

**Source PDF:** `1-s2.0-S0021999119307612-main.pdf`

---

## 摘要

本文提出了一种基于物理约束的深度自回归网络（Physics-Constrained Deep Auto-Regressive Networks, PCDAN），用于模拟偏微分方程（PDE）系统的动力学演化。该方法将PDE的残差作为显式损失项嵌入网络训练过程，无需依赖大量仿真数据即可学习系统的时间推进规律。在Burgers方程和反应扩散方程上的实验表明，PCDAN在长期预测中相比纯数据驱动方法将均方误差降低了一个数量级，并能准确捕捉激波和模式形成等非线性现象。

## 结论

本文证明了将PDE残差作为硬约束嵌入深度自回归网络，能够在不使用完整数值解数据的情况下，实现高精度、长期稳定的动力学预测，且对初始条件和参数变化具有良好的泛化能力。

**状态：** ✅ 已精修
