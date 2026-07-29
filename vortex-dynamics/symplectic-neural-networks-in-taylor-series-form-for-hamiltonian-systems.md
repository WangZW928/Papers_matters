# Symplectic neural networks in Taylor series form for Hamiltonian systems

**Authors:** Yunjin Tong

**DOI:** [10.1016/j.jcp.2021.110325](https://doi.org/10.1016/j.jcp.2021.110325)

**Source PDF:** `1-s2.0-S0021999121002205-main.pdf`

---

## Abstract

_Not available_

## Summary

**核心问题：** 如何设计保持辛结构（symplectic structure）的神经网络以长期精确预测Hamilton动力学系统？

**方法：** 提出Taylor-net架构：两个子网络以四阶辛积分器组合，每个子网络嵌入Taylor级数展开形式，每项设计为对称结构以保证辛性。从稀疏短时观测中学习连续时间演化。

**关键结果：**
- Taylor-net的预测精度是HNN的2倍、ODE-net的7倍，长期预测误差远小于对比方法
- 在噪声条件下表现出优异的鲁棒性——大噪声下Taylor-net预测误差仅为HNN的1/2、ODE-net的1/20
- 仅需对比方法1/5的训练样本和1/10-1/70的训练轮数即可收敛；1轮训练即可获得有效预测

**与你工作的相关性：** 辛神经网络（SNN）的结构保持特性可参考用于HPC框架中保物理结构的代理模型构建。

**状态：** ✅ 完整摘要
