# The Hermite-Taylor Correction Function Method for Maxwell's Equations

**Authors:** Yann-Meing Law, Daniel Appelö

**Journal:** arXiv:2210.07134

**Source PDF:** `2210.07134v2.pdf`

---

## Abstract

_Not available_

## Summary

**核心问题：** Maxwell方程的Hermite-Taylor校正函数方法——如何构造高阶精度且满足散度约束的电磁求解器？

**方法：** 提出Hermite-Taylor校正函数法：利用Hermite插值和Taylor级数构造高阶通量重构格式，结合校正函数确保电场和磁场的散度条件在离散层面精确满足。

**关键结果：**
- 格式在高阶精度下保持电/磁场的散度为零（机器精度）
- 在电磁波传播、散射等基准测试中验证了高阶收敛率和精度
- 方法避免了传统散度清洁或约束输运方案的额外计算开销

**与你工作的相关性：** 电磁场的高阶数值格式可参考用于HPC框架中的多物理（MHD/EM）求解器。

**状态：** ✅ 完整摘要
