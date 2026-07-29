# Schrödinger's Smoke

**Authors:** Albert Chern, Felix Knöppel, Ulrich Pinkall, Peter Schröder, Steffen Weißmann

**DOI:** [http:](https://doi.org/http:)

**Source PDF:** `SchrodingersSmoke.pdf`

---

## Abstract

_Not available_

## Summary


**核心问题：** 如何用薛定谔方程描述不可压缩流体的涡动力学，实现无耗散的流体模拟

**方法：** 薛定谔烟雾（Schrödinger's Smoke）方法——将不可压缩Euler方程映射为Gross-Pitaevskii方程的极限形式，用波函数的涡丝演化替代传统的速度-压力求解

**关键结果：** 
1. 证明了不可压缩Euler流的涡动力学等价于GP方程在压力投影极限下的Schrödinger演化
2. 该方法天然保持涡量守恒，无需显式处理涡量输运方程
3. 实现了无人工数值耗散的涡丝动力学模拟，自动捕获涡旋重连等复杂拓扑变化

**与你工作的相关性：** 该方法提供了将量子力学方法映射到经典流体力学的范式，其波函数表示可能为湍流模拟和量子-经典混合计算方法提供新思路；在HPC上实现此类方法需要高效的FFT和Poisson求解器

**状态：** ✅ 完整摘要


## Review Questions

### 🤔 Questions
1. **Q:** How does the Gross-Pitaevskii equation in the Thomas-Fermi limit recover the incompressible Euler equations, and what role does the pressure projection (enforcing constant density) play in establishing this correspondence?
2. **Q:** Why does the Schrödinger formulation naturally conserve vortex topology (helicity, linking number, knot type) during evolution, whereas traditional grid-based CFD methods may introduce spurious numerical reconnection events?
3. **Q:** What is the physical interpretation of the Madelung quantum potential term in the GP equation when applied to classical incompressible fluid dynamics, and under what conditions can it be safely neglected?
