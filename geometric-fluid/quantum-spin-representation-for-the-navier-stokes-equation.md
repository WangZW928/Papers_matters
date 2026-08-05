# Quantum spin representation for the Navier-Stokes equation

**Authors:** Zhaoyuan Meng, Yue Yang

**DOI:** [10.1103/PhysRevResearch.6.043130](https://doi.org/10.1103/PhysRevResearch.6.043130)

**Source PDF:** `PhysRevResearch.6.043130.pdf`

---

## Abstract

### 中文翻译
本文为牛顿粘性流建立量子表示：在 Navier-Stokes 方程（NSE）与 Schrödinger-Pauli 方程（SPE）之间建立映射。所提出的非线性 SPE 包含双分量波函数与虚扩散项，从而经典流体流动可以被解释为非厄米量子自旋系统。基于 SPE 的粘性流数值模拟展示了流动动力学中的量子/类波行为；此外，与 NSE 等价的 SPE 可用于流体力学的量子模拟。

### 原文
> We develop a quantum representation for Newtonian viscous fluid flows by establishing a mapping between the Navier-Stokes equation (NSE) and the Schrödinger-Pauli equation (SPE). The proposed nonlinear SPE incorporates the two-component wave function and the imaginary diffusion. Consequently, classical fluid flow can be interpreted as a non-Hermitian quantum spin system. Using the SPE-based numerical simulation of viscous flows, we demonstrate the quantum/wavelike behavior in flow dynamics. Furthermore, the SPE equivalent to the NSE can facilitate the quantum simulation of fluid dynamics.

## Summary

**核心问题：** 如何把经典粘性流（Navier-Stokes 方程）编码为量子系统，使流体动力学可被量子模拟与量子/类波视角理解？

**方法：** 建立 NSE 与 Schrödinger-Pauli 方程（SPE）之间的映射：SPE 采用双分量波函数并引入虚扩散项，使经典流场对应非厄米量子自旋系统；并基于 SPE 对粘性流进行数值模拟。

**关键结果：**
1. 建立了 NSE ↔ SPE 的映射（量子自旋表示）：经典粘性流可解释为非厄米量子自旋系统
2. 基于 SPE 的粘性流数值模拟展示了流动动力学中的量子/类波行为
3. 与 NSE 等价的 SPE 为流体力学的量子模拟提供了平台

**与你工作的相关性：** 与 HPC 直接关联中等：SPE 形式的演化方程为流场模拟提供了波函数/自旋表象的替代数值格式；且与库内 Madelung 变换（波函数编码经典流体）路线一脉相承——Madelung 用标量波函数编码可压 QHD，本文用双分量自旋波函数编码粘性流，可对照阅读。

**状态：** ✅ 完整摘要（2026-08-05 校正：原摘要误贴另一篇磁子/量子信息论文内容，已按 Crossref 官方摘要重写）
