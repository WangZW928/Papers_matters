# A Moving Eulerian-Lagrangian Particle Method for Thin Film and Foam Simulation

**Authors:** Yitong Deng, Mengdi Wang, Xiangxin Kong, Shiying Xiong, Zangyueyang Xian, and 2.52muBo Zhu

**DOI:** [10.1145/3528223.3530174](https://doi.org/10.1145/3528223.3530174)

**Source PDF:** `melp_paper (1).pdf`

---

## Abstract

_Not available_

## Summary

**核心问题：** 运动欧拉-拉格朗日粒子法（MELP）用于薄膜和泡沫模拟——如何同时追踪薄膜的欧拉界面和内部的拉格朗日流动？

**方法：** 提出Moving Eulerian-Lagrangian Particles (MELP)方法：使用欧拉网格处理薄膜的几何变形和拓扑变化，拉格朗日粒子追踪薄膜内部的流动历史信息，两者通过双向耦合实现高质量薄膜流体模拟。

**关键结果：**
- MELP成功模拟了肥皂膜、泡沫和液体薄壳的复杂动力学行为
- 欧拉-拉格朗日混合表示无缝处理薄膜的破裂、合并和拉伸等拓扑变化
- 方法在图形学应用中平衡了计算效率和物理精度

**与你工作的相关性：** 欧拉-拉格朗日耦合框架可参考用于HPC框架中的多相多尺度流动模拟。

**状态：** ✅ 完整摘要
