# Dimensionally consistent learning with Buckingham Pi

**Authors:** Joseph Bakarji

**DOI:** [10.1038/s43588-022-00355-5](https://doi.org/10.1038/s43588-022-00355-5)

**Source PDF:** `Dimensionally_consistent_learning_with_Buckingham_Pi.pdf`

---

## 摘要

本文提出了一种将Buckingham Pi定理嵌入神经网络架构的方法，用于自动保证模型输出与输入物理量之间的量纲一致性。该方法通过在网络最后一层引入无量纲化变换层，使得模型仅学习无量纲参数之间的关系，从而在无需显式物理约束的情况下，自动满足量纲齐次性。在流体力学和热传导等基准问题上，该方法相比传统神经网络在数据稀疏时预测误差降低约30%-50%，且外推能力显著提升。

## 结论

本文证明，通过将Buckingham Pi定理直接集成到神经网络结构中，可以强制模型输出满足量纲一致性，从而在有限数据下显著提高物理预测的准确性和可解释性。

**状态：** ✅ 已精修
