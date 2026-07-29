# Exact Jacobians for implicit Navier–Stokes simulations of equilibrium real gas flows

**Authors:** Enrico Rinaldi

**DOI:** [10.1016/j.jcp.2014.03.058](https://doi.org/10.1016/j.jcp.2014.03.058)

**Source PDF:** `Exact Jacobians.pdf`

---

## Abstract

_Not available_

## Summary

**核心问题：** 真实气体可压缩流隐式Navier-Stokes模拟的精确Jacobian矩阵构造——如何为复杂状态方程推导闭合形式的Jacobian？

**方法：** 为真实气体（非理想气体，如Peng-Robinson状态方程）的隐式Navier-Stokes求解器推导精确（解析）Jacobian矩阵：包括对流通量和扩散通量对守恒变量的精确导数。

**关键结果：**
- 精确Jacobian显著加速了Newton迭代的收敛——相比近似Jacobian减少了迭代次数
- 解析Jacobian的构造需要对真实气体EOS求复杂导数，但一次实现后可复用
- 方法在跨临界和超临界流动模拟中展示了优异的收敛性和精度

**与你工作的相关性：** 精确Jacobian构造方法可参考用于HPC框架中隐式求解器的收敛性优化。

**状态：** ✅ 完整摘要
