# Fluid Simulation on Neural Flow Maps

**Authors:** Yitong Deng, Hong-Xing Yu, Diyang Zhang, Jiajun Wu, and Bo Zhu

**DOI:** [10.1145/3618392reconnections](https://doi.org/10.1145/3618392reconnections)

**Source PDF:** `NFM_v1.pdf`

---

## 摘要

本文提出了一种基于神经流图（Neural Flow Maps）的流体模拟新方法，将物理模拟的数值计算与神经网络的可微分表示相结合。该方法通过将流体运动建模为连续时间流映射，并利用神经网络隐式学习速度场与密度场的演化，在保持物理守恒性的同时显著提升了模拟的长期稳定性和细节保真度。实验表明，该方法在2D和3D湍流模拟中，相比传统欧拉法和SPH方法，能更准确地捕捉涡旋结构且数值耗散降低约一个数量级。

## 结论

本文证明，神经流图框架能够有效克服传统流体模拟中数值耗散与网格分辨率限制的矛盾，通过可微分流映射实现高保真、长时稳定的流体动力学仿真。

**状态：** ✅ 已精修
