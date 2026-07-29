# Schrödinger's Smoke

**作者：** Albert Chern, Felix Knöppel, Ulrich Pinkall, Peter Schröder, Steffen Weißmann

**DOI：** [http:](https://doi.org/http:)

**源 PDF：** `SchrodingersSmoke.pdf`

---

## 摘要

_暂无_

## 总结


**核心问题：** 如何用薛定谔方程描述不可压缩流体的涡动力学，实现无耗散的流体模拟

**方法：** 薛定谔烟雾（Schrödinger's Smoke）方法——将不可压缩 Euler 方程映射为 Gross-Pitaevskii 方程的极限形式，用波函数的涡丝演化替代传统的速度-压力求解

**关键结果：** 
1. 证明了不可压缩 Euler 流的涡动力学等价于 GP 方程在压力投影极限下的 Schrödinger 演化
2. 该方法天然保持涡量守恒，无需显式处理涡量输运方程
3. 实现了无人工数值耗散的涡丝动力学模拟，自动捕获涡旋重连等复杂拓扑变化

**与你工作的相关性：** 该方法提供了将量子力学方法映射到经典流体力学的范式，其波函数表示可能为湍流模拟和量子-经典混合计算方法提供新思路；在 HPC 上实现此类方法需要高效的 FFT 和 Poisson 求解器

**状态：** ✅ 完整摘要


## Review Questions

1. Schrödinger's Smoke 中的压力投影与密度约束在数学上如何共同确保不可压缩极限成立？
2. 该方法在涡旋重连、拓扑不变量保持和数值稳定性之间的关系是什么？
3. Madelung 量子势项在该流体类比中的物理意义是什么，何种近似下可以忽略？
