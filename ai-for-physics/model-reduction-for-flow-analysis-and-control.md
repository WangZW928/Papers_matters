# Model Reduction for Flow Analysis and Control

**Authors:** Clarence W. Rowley and Scott T.M. Dawson

**DOI:** [10.1146/annurev-ﬂuid-010816-060042](https://doi.org/10.1146/annurev-ﬂuid-010816-060042)

**Source PDF:** `rowley-dawson-2017-model-reduction-for-flow-analysis-and-control.pdf`

---

## 摘要

本文针对流体动力学中的流动分析与控制问题，系统综述了基于模态分解的模型降阶方法。重点介绍了本征正交分解（POD）与动态模态分解（DMD）两种核心技术的数学原理及其在不可压缩流动中的适用条件，并对比了它们在捕捉相干结构、构建低维模型以及设计反馈控制器时的性能差异。通过圆柱绕流和槽道湍流等典型算例，展示了降阶模型在将原始高维Navier-Stokes方程缩减至数十个模态时，仍能准确复现流动的瞬态演化与关键失稳特征。

## 结论

POD适用于能量最优的低维表示，但难以直接提取动力学特征；DMD能直接识别流动的固有频率与增长率，更适合用于线性反馈控制器的设计。两种方法结合可有效平衡模型精度与控制性能。

**状态：** ✅ 已精修
