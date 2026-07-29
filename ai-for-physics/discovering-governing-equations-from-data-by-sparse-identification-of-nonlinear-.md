# Discovering governing equations from data by sparse identification of nonlinear dynamical systems

**Source PDF:** `brunton-et-al-2016-discovering-governing-equations-from-data-by-sparse-identification-of-nonlinear-dynamical-systems.pdf`

---

## 摘要

本文提出了一种从数据中稀疏识别非线性动力系统控制方程的方法（SINDy）。该方法利用稀疏回归技术，从大量候选函数库中自动筛选出控制方程中少数关键的非线性项，从而在仅依赖少量观测数据的情况下，准确重构出系统的动力学模型。在多个经典非线性系统（如洛伦兹系统、杜芬振子）的数值实验中，该方法成功恢复了已知的控制方程，且对噪声具有较好的鲁棒性。

## 结论

SINDy方法能够从时间序列数据中高效、可解释地提取出非线性动力系统的稀疏控制方程，为数据驱动的科学发现提供了一种实用工具。

**状态：** ✅ 已精修

## Review Questions

### 🤔 Questions
1. **Q:** How does the sequential thresholded least-squares algorithm in SINDy balance sparsity promotion with numerical stability, and why is hard thresholding preferred over L1 regularization for identifying the correct sparsity pattern?
2. **Q:** What are the key limitations of SINDy when the true governing equations contain rational functions, non-polynomial nonlinearities, or implicit algebraic constraints that cannot be expressed in a linear combination of candidate library functions?
3. **Q:** How does the choice of numerical derivative approximation (e.g., finite differences vs. total variation regularized derivatives) fundamentally affect SINDy's robustness to measurement noise, and when would you choose one over the other?
