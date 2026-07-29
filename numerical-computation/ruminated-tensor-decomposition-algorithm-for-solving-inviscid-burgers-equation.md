# Ruminated Tensor Decomposition algorithm for solving inviscid Burgers' equation

**Authors:** Shaoqiang Tang

**DOI:** [10.1016/j.jcp.2024.113663](https://doi.org/10.1016/j.jcp.2024.113663)

**Source PDF:** `1-s2.0-S0021999124009112-main.pdf`

---

## Abstract

_Not available_

## Summary

**核心问题：** 利用反刍张量分解（RTD）算法求解无粘Burgers方程——如何结合PGD鲁棒性和TD精度进行降阶建模？

**方法：** 提出RTD策略：交替执行PGD（Proper Generalized Decomposition，鲁棒的随机初始化ADAM优化）和TD（Tensor Decomposition，高精度的确定性优化）。先PGD预训练三个新模式→TD精化所有模式。

**关键结果：**
- RTD在精度和鲁棒性上均优于单独使用PGD或TD
- 成功复现Godunov格式的标准解，且避免时间积分的累积误差
- 方法可扩展到多维Euler方程和等温流动，展示了非线性守恒律降阶建模的潜力

**与你工作的相关性：** 张量分解降阶建模方法可参考用于HPC框架中的高效代理模型构建。

**状态：** ✅ 完整摘要
