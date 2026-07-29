# Lie–Poisson Neural Networks (LPNets): Data-based computing of Hamiltonian systems with symmetries

**Authors:** Christopher Eldred

**DOI:** [10.1016/j.neunet.2024.106162](https://doi.org/10.1016/j.neunet.2024.106162)

**Source PDF:** `1-s2.0-S0893608024000868-main.pdf`

---

## 摘要

本文针对具有对称性的哈密顿系统，提出了一种基于李-泊松结构的神经网络（LPNets），用于从数据中学习系统的动力学演化。该方法通过将网络结构约束为李-泊松括号形式，自动满足系统的辛几何结构与守恒律（如能量与卡西米尔函数），并在刚体旋转和KdV方程等数值实验中验证了其长期预测稳定性优于标准神经网络。

## 结论

LPNets能够从数据中准确恢复哈密顿系统的对称性与守恒量，并在长时间积分中保持物理一致性，显著优于未嵌入几何结构的黑箱神经网络方法。

**状态：** ✅ 已精修

## Review Questions

### 🤔 Questions
1. **Q:** LPNets 如何把 Jacobi identity 和 antisymmetry 嵌入网络结构中，这种结构性约束为什么能在 rollout 过程中保证长期的能量守恒与 Casimir 守恒？
2. **Q:** LPNets 中可学习的结构矩阵 `J_{ij}(z)` 与底层哈密顿系统的 Poisson bracket 之间是什么关系？`J_{ij}` 如何编码系统的对称性？
3. **Q:** LPNets 在什么意义上将 Hamiltonian Neural Networks (HNNs) 推广到了具有非典范 Poisson structure 的系统？为什么标准 HNNs 若不做结构修改，难以学习 rigid body 或 ideal fluid 这类系统？
