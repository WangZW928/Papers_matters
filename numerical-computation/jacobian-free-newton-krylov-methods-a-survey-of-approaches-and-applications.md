# Jacobian-free Newton-Krylov Methods: A Survey of Approaches and Applications

**Authors:** D. A. Knoll, D. E. Keyes

**Journal:** Journal of Computational Physics, 193 (2004) 357–397

**DOI:** [10.1016/j.jcp.2003.08.010](https://doi.org/10.1016/j.jcp.2003.08.010)

**Source PDF:** `JFK.pdf`

---

## Abstract

_Not available_

## Summary

**核心问题：** Jacobian-free Newton-Krylov（JFNK）方法的全面综述——方法、应用和前沿

**方法：** 全面综述JFNK方法：从基本概念（Newton非线性迭代+Krylov线性迭代的嵌套）到关键技术（预条件、强制项选择、全局化策略），涵盖在流体力学、反应流、MHD、辐射输运等领域的应用。

**关键结果：**
- JFNK是解决大规模非线性PDE系统的最有效方法之一
- 预条件子的质量是JFNK性能的决定性因素
- 矩阵无关实现（通过有限差分近似Jacobian-向量积）避免存储Jacobian，适合超大规模问题

**与你工作的相关性：** JFNK方法是HPC框架中大规模非线性求解的核心技术，该综述提供了完整的方法论指导。

**状态：** ✅ 完整摘要
