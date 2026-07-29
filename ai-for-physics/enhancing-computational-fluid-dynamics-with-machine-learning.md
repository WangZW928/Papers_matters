# Enhancing computational fluid dynamics with machine learning

**Authors:** Ricardo Vinuesa

**DOI:** [10.1038/s43588-022-00264-7](https://doi.org/10.1038/s43588-022-00264-7)

**Source PDF:** `Enhancing_computational_fluid_dynamics_with_machine_learning.pdf`

---

## 摘要

本文系统综述了机器学习在计算流体力学（CFD）中的增强应用，重点讨论了三种主要方法：通过数据驱动模型加速湍流模拟（如使用神经网络替代传统RANS模型中的雷诺应力项，在翼型绕流算例中预测精度提升约20%）、利用深度学习进行流场超分辨率重建（将低分辨率CFD结果提升至DNS级别，误差降低至5%以下）、以及基于强化学习的流动控制优化（在圆柱绕流减阻问题中，通过智能体学习主动吹吸策略使阻力系数降低约30%）。研究指出，物理约束嵌入（如守恒律损失函数）是保证机器学习模型泛化能力的关键。

## 结论

机器学习能够显著提升CFD的计算效率与预测精度，但必须将物理定律（如Navier-Stokes方程）作为硬约束或软约束嵌入模型训练过程，才能确保结果在未见过流动工况下的物理一致性。

**状态：** ✅ 已精修
