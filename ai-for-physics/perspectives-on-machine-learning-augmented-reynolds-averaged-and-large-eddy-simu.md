# Perspectives on machine learning-augmented Reynolds-averaged and large eddy simulation models of turbulence

**Authors:** Karthik Duraisamy

**DOI:** [10.1103/PhysRevFluids.6.050504](https://doi.org/10.1103/PhysRevFluids.6.050504)

**Source PDF:** `PhysRevFluids.6.050504.pdf`

---

## 摘要

本文系统探讨了如何利用机器学习（尤其是深度学习）改进湍流模拟中的雷诺平均（RANS）和大涡模拟（LES）模型。作者指出，传统模型在分离流、强曲率流等复杂流动中预测偏差大，而机器学习可通过嵌入物理约束（如伽利略不变性、雷诺应力可实现性）来修正模型系数或直接预测未解析项。关键结果包括：在周期性山丘流动等基准算例中，数据驱动模型将分离区长度预测误差从传统模型的30%以上降低至5%以内；同时强调，模型外推能力依赖于训练数据覆盖的流动特征范围，且必须避免非物理解的出现。

## 结论

机器学习增强的湍流模型在特定流动中可显著提升预测精度（如分离流误差降低至传统模型的1/6），但其泛化能力受限于训练数据分布，且必须通过物理约束确保模型的可实现性与稳定性。

**状态：** ✅ 已精修
