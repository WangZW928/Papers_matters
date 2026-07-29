# Physics-informed machine learning of the Lagrangian dynamics of velocity gradient tensor

**Authors:** Yifeng Tian

**DOI:** [10.1103/PhysRevFluids.6.094607](https://doi.org/10.1103/PhysRevFluids.6.094607)

**Source PDF:** `PhysRevFluids.6.094607.pdf`

---

## 摘要

本文针对湍流中速度梯度张量的拉格朗日动力学建模问题，提出了一种物理信息机器学习方法。该方法将不可压缩Navier-Stokes方程所蕴含的精确约束（如迹为零、旋转-拉伸耦合关系）作为软约束嵌入神经网络损失函数，在直接数值模拟数据上训练模型。结果表明，与纯数据驱动方法相比，该物理信息模型能够更准确地预测速度梯度张量的时间演化轨迹，并显著改善对涡量拉伸和应变自放大等关键物理过程的复现能力。

## 结论

本文证明，将速度梯度张量演化的精确物理约束（如不可压缩条件及涡量-应变耦合方程）显式嵌入机器学习模型，能够有效提升拉格朗日动力学预测的物理一致性与长期稳定性，为湍流小尺度建模提供了可解释的替代方案。

**状态：** ✅ 已精修
