# BEACONS: Bounded-Error, Algebraically-Composable Neural Solvers for Partial Differential Equations

**Authors:** Jonathan Gorard; Ammar Hakim; James Juno

**Source PDF:** `2602.14853v1.pdf`

---

## 摘要

本文针对物理信息神经网络（PINNs）在求解偏微分方程（PDEs）时存在的误差不可控和组合性差的问题，提出了一种名为BEACONS的新型神经求解器框架。该方法通过引入有界误差约束和代数组合机制，确保每个局部解的误差在可证明的范围内，并允许将多个局部解通过代数运算（如加、乘、复合）组合成全局解，同时保持误差边界。在多个标准PDE基准测试（如泊松方程、对流-扩散方程）上，BEACONS相比传统PINNs将最大点态误差降低了一个数量级以上，并首次实现了神经求解器在复杂几何区域上的可组合、可验证的求解。

## 结论

本文证明，通过将神经求解器设计为具有有界误差的代数可组合模块，可以克服传统PINNs在误差控制和多区域耦合上的根本局限，从而为复杂工程问题提供一种可靠且可扩展的PDE求解新范式。

**状态：** ✅ 已精修
