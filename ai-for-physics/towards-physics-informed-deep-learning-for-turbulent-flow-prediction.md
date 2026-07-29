# Towards physics-informed deep learning for turbulent flow prediction

**Authors:** Rui Wang, Karthik Kashinath, Mustafa Mustafa, Adrian Albert, and Rose Yu

**DOI:** [10.1145/3394486.3403198](https://doi.org/10.1145/3394486.3403198)

**Source PDF:** `3394486.3403198.pdf`

---

## 摘要

本文针对湍流预测中纯数据驱动深度学习模型物理一致性差的问题，提出了一种物理信息深度学习（PINN）方法。该方法将纳维-斯托克斯方程等物理约束嵌入神经网络损失函数，在二维圆柱绕流和三维湍流通道流数据集上训练。结果表明，相比纯数据驱动模型，该方法在预测湍流场时均速度与雷诺应力分布上误差降低约30%，并能更准确地捕捉涡旋结构等关键物理特征。

## 结论

通过将物理定律显式嵌入深度学习模型，可显著提升湍流预测的物理一致性与泛化能力，尤其在小样本或外推工况下优势明显。

**状态：** ✅ 已精修
