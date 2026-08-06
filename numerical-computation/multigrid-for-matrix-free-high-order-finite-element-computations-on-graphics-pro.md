# 面向图形处理器的矩阵无关高阶有限元多重网格计算

**期刊：** ACM Transactions on Parallel Computing，2019

**DOI：** [10.1145/3322813](https://doi.org/10.1145/3322813)

**来源 PDF：** `matrix free 3.pdf`
**阅读状态：** 🔬 精读
**流程状态：** ①元数据 ✓ | ②初稿 ✓ | ③评估 ✓(精读) | ④补充 ✓ | ⑤索引 ⏳ | ⑥review ✓ | ⑦提交 ⏳

---

## 摘要

_无可用摘要_

## 总结

**核心问题：** 如何在图形处理器上为矩阵无关高阶有限元构建高效的多重网格加速方案，并兼顾高阶方法的计算效率与多重网格的收敛性。

**方法：** 论文提出了一种面向 GPU 的矩阵无关多重网格方法用于高阶有限元计算：通过 sum-factorization 技术高效完成单元级矩阵-向量乘，并结合 p-多重网格与 h-多重网格实现多层求解。

**关键结果：**
- sum-factorization 将高阶单元的矩阵-向量乘复杂度从 O(p^6) 降至 O(p^4)（三维情形；一般维度为 O(p^{2d}) → O(dp^{d+1})）
- GPU 加速的多重网格在三维高阶有限元中实现了近线性复杂度
- p-多重网格与 h-多重网格的组合策略平衡了收敛性与并行效率

**与你工作的相关性：** 这种矩阵无关多重网格方法可为 HPC 框架中的高阶离散最优复杂度求解提供参考。

## 价值评估

Doctor 指定精读（学习路线规划推荐）。本文是高阶 FEM、matrix-free operator、GPU kernel 和 multigrid 预条件结合的关键工程论文。对 Doctor 的 HPC 数值框架，它直接对应“高阶离散如何在 GPU 上达到可用性能，并且求解器复杂度不被线性系统拖垮”的核心问题。

## 公式与代码梳理

### 数学结构与核心公式

高阶有限元离散后要求解

$$
Au=b,
$$

但 matrix-free 方法不显式组装 $A$，而是在每次 Krylov 或 multigrid 平滑中计算

$$
y=Ax
$$

的作用。

对单元 $K$，有限元算子应用通常来自弱形式积分：

$$
(A_K u)_i
=
\sum_q w_q
\left[
\nabla\varphi_i(x_q)\cdot C(x_q)\nabla u(x_q)
+\varphi_i(x_q)c(x_q)u(x_q)
\right]J_K(x_q).
$$

直接张量收缩在 $d$ 维、阶数 $p$ 下代价接近

$$
O(p^{2d}),
$$

而 tensor-product 基函数的 sum-factorization 将其降为

$$
O(dp^{d+1}).
$$

核心思想是把多维插值/微分矩阵拆成一维矩阵连乘，避免形成完整单元矩阵。

多重网格使用层级空间 $V_\ell$ 和算子 $A_\ell$。一次误差校正为

$$
r_\ell=b_\ell-A_\ell u_\ell,\qquad
b_{\ell-1}=R_\ell r_\ell,
$$

粗层求解后

$$
u_\ell\leftarrow u_\ell+P_\ell e_{\ell-1}.
$$

高阶方法中常结合 $p$-multigrid 与 $h$-multigrid：先降低多项式阶数，再在低阶层做几何或代数粗化，从而兼顾高阶局部效率和粗网格全局传播。

### 关键推导/算法

matrix-free operator apply：

```text
for each cell K in parallel:
    gather local DoFs
    apply 1D basis interpolation in each tensor direction
    evaluate values/gradients at quadrature points
    multiply by coefficients, weights, Jacobians
    apply transposed 1D basis operations
    scatter-add local result
```

multigrid/preconditioned Krylov：

```text
build p/h hierarchy
for each Krylov iteration:
    apply matrix-free A on fine level
    apply multigrid preconditioner:
        smooth with Jacobi/Chebyshev-type matrix-free smoother
        restrict residual
        solve/coarsen recursively
        prolongate correction
        postsmooth
```

GPU 实现重点：

1. 每个单元或单元批次映射到 thread block；
2. 局部自由度和一维插值矩阵尽量放入寄存器/shared memory；
3. 避免存储高阶稠密单元矩阵；
4. 平滑器选择偏向 Jacobi/Chebyshev，因为它们并行度高、同步少；
5. 粗层和边界上的 gather/scatter 需要避免原子冲突或降低其占比。

### 对 HPC 框架的启示

1. 高阶 GPU FEM 的性能来自 sum-factorization 和 matrix-free，不应默认组装全局稀疏矩阵。
2. 求解器层级必须和离散层级一起设计：单独优化 operator kernel 不能保证端到端 time-to-solution。
3. $p$-coarsening 是高阶框架应内建的能力，而不是外部 solver 的附属选项。
4. Chebyshev/Jacobi 这类简单平滑器在 GPU 上常比复杂但串行的平滑器更有整体优势。
5. 框架需要统一表达 operator apply、diagonal extraction、restriction/prolongation 和 coarse solve，才能复用 multigrid 逻辑。

### 待深入研究的问题

1. 对非张量网格、曲边几何或自适应网格，sum-factorization 的数据布局如何保持高占用率？
2. matrix-free 高阶算子如何与 AmgX 这类 assembled AMG 结合，形成低阶粗层或辅助空间预条件？
3. 对 Hamiltonian 波动问题，高阶 matrix-free multigrid 在隐式时间步中如何避免过度耗散？

## Review Questions

4. 1. sum-factorization 提高的是算子求值效率，但多重网格收敛性取决于层间误差传播；在 GPU 上这两者何时会相互冲突？
5. 2. 对连续高阶 FEM，matrix-free kernel 的瓶颈究竟在单元内张量操作、面通量、还是全局 scatter/gather？不同离散类型下最优线程映射是否应不同？
6. 3. 若 Doctor 的框架同时支持高阶 Hamiltonian 波动问题和黏性流动问题，是否应共享同一套 matrix-free multigrid 基础设施，还是按算子谱性质拆成两类预条件路线？

1. **Q:** sum-factorization 如何将高阶 FEM 算子求值的复杂度从 O(p^{2d}) 降到 O(d p^{d+1})，这种变化对 GPU 上的内存带宽和算术强度意味着什么？
2. **Q:** 为什么在高阶 FEM 中需要将 p-multigrid 与 h-multigrid 结合以获得稳健收敛，而 p-coarsening（降低多项式阶数）与 h-coarsening（粗化网格）在谱半径性质上有何差异？
3. **Q:** 在高多项式阶数下实现无矩阵平滑器（例如 Chebyshev-accelerated Jacobi）时，关键挑战是什么，sum-factorization 的单元局部特性又如何与 multigrid cycles 中的全局通信需求相互作用？
