# A Clebsch Method for Free-Surface Vortical Flow Simulation

**Authors:** Shiying Xiong, Zhecheng Wang, Mengdi Wang, and Bo Zhu

**DOI:** [10.1145/3528223.3530150](https://doi.org/10.1145/3528223.3530150)

**Source PDF:** `clebsch_fluid.pdf`

---

## 摘要

本文针对自由表面涡流模拟中涡量生成与界面拓扑变化耦合的难题，提出了一种基于Clebsch变量的数值方法。该方法通过将速度场分解为Clebsch势函数与涡量场的组合，利用哈密顿变分原理推导出自由表面边界上的涡量生成方程，并采用谱方法进行空间离散。在三维溃坝和波浪破碎算例中，该方法成功捕捉了自由表面卷曲、破碎及涡环形成等复杂流动现象，且涡量守恒误差低于1%。

## 结论

本文提出的Clebsch方法能够精确模拟自由表面涡流的生成与演化，其核心优势在于通过势函数-涡量分解避免了传统方法中对自由表面涡量边界条件的显式构造，从而在保持涡量守恒的同时实现了对拓扑变化的高效追踪。

**状态：** ✅ 已精修
