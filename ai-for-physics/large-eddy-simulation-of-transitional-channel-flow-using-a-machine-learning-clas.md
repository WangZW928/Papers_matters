# Large eddy simulation of transitional channel flow using a machine learning classifier to distinguish laminar and turbulent regions

**Authors:** Ghanesh Narasimhan

**DOI:** [10.1103/PhysRevFluids.6.074608](https://doi.org/10.1103/PhysRevFluids.6.074608)

**Source PDF:** `PhysRevFluids.6.074608.pdf`

---

## 摘要

本文针对过渡态槽道流中层流与湍流区域共存的问题，提出了一种基于机器学习分类器的大涡模拟（LES）方法。通过训练一个支持向量机（SVM）分类器，利用局部流动特征（如涡量、应变率等）实时区分层流与湍流区域，并在湍流区域启用亚格子模型、层流区域关闭模型。在雷诺数Re=2800的过渡态槽道流算例中，该方法成功捕捉了湍流斑的生成与演化，与直接数值模拟（DNS）结果相比，平均速度剖面误差小于3%，同时计算成本降低了约40%。

## 结论

基于机器学习分类器的自适应LES方法能够准确识别过渡态流动中的层流与湍流区域，在保证计算精度的前提下显著降低计算开销，为工程中复杂过渡态流动的高效模拟提供了可行方案。

**状态：** ✅ 已精修
