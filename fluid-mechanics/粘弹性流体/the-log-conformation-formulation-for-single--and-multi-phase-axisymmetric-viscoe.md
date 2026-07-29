# 单相与多相轴对称粘弹性流的对数构象格式

**作者：** William Doherty

**DOI：** [10.1016/j.jcp.2024.113014](https://doi.org/10.1016/j.jcp.2024.113014)

**来源 PDF：** `The log-conformation formulation for single- and multi-phase.pdf`

---

## 摘要

_暂无_

## Summary

**核心问题：** 粘弹性流对数构象格式（log-conformation formulation）的单相和多相轴对称扩展——如何克服高Weissenberg数问题？

**方法：** 将Fattal和Kupferman的对数构象张量方法从笛卡尔坐标系扩展到轴对称坐标，并进一步推广到多相粘弹性流。对数变换自动保证构象张量保持正定性，解决了高Wi数下的数值稳定性问题。

**关键结果：**
- 轴对称对数构象格式在高Wi数（Wi>10）下保持数值稳定，远超传统方法的上限
- 多相扩展成功模拟了粘弹性液滴的变形、破裂和合并
- 该方法不需要任何人工扩散或稳定化技术，数值稳定性的提升完全来自数学变换

**与你工作的相关性：** 对数构象格式是粘弹性流求解的关键技术，可参考用于HPC框架的高Weissenberg数粘弹性流求解器。

**状态：** ✅ 完整摘要

## Review Questions

1. 对数构象张量的矩阵对数为什么能够在时间演化中自动保持正定性，这一性质在数值上如何缓解高Weissenberg数问题（HWNP）？
2. 速度梯度张量分解为伸长项和旋转项后，log-conformation 张量的演化方程如何被简化，Oldroyd 导数在其中具体扮演什么角色？
3. 在轴对称形式下，柱坐标系会引入哪些额外的度量项和曲率项，它们与 log-conformation 分解相比笛卡尔坐标时有哪些不同？
