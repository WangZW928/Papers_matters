# An Energy Stable Immersed Boundary Method for Deformable Membrane Problem with Non-uniform Density and Viscosity

**Authors:** Qinghe Wang

**DOI:** [10.1007/s10915-022-02092-3](https://doi.org/10.1007/s10915-022-02092-3)

**Source PDF:** `s10915-022-02092-3 (2).pdf`

---

## Abstract

_Not available_

## Summary

**核心问题：** 粘弹性流中可变形膜问题的能量稳定浸入边界法

**方法：** 提出了一种能量稳定的浸入边界格式，在空间上采用有限差分/傅里叶谱方法离散，时间上采用二阶精度的能量稳定时间推进格式，保证半离散和全离散能量不增长。

**关键结果：**
- 格式被证明无条件能量稳定，适用于大变形膜问题
- 在二维和三维可变形膜基准测试中验证了收敛性和稳定性
- 能量稳定性的理论保证比传统的显式IBM具有更大的时间步长自由度

**与你工作的相关性：** 能量稳定的数值格式设计模式可参考用于HPC框架中的流固耦合求解器。

**状态：** ✅ 完整摘要
