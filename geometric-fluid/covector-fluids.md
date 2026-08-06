# Covector Fluids

**作者：** Mohammad Sina Nabizadeh, Stephanie Wang, Ravi Ramamoorthi, Albert Chern

**DOI：** [10.1145/3528223.3530120](https://doi.org/10.1145/3528223.3530120)

**来源 PDF：** `CovectorFluids.pdf`

**阅读状态：** 🔬 精读
**流程状态：** ①元数据 ✓ | ②初稿 ✓ | ③评估 ✓(精读) | ④补充 ✓ | ⑤索引 ✓ | ⑥review ✓ | ⑦提交 ⏳

---

## 摘要

### 中文翻译

本文提出 Covector Fluids：将不可压流体的速度场改写为余向量（one-form），用 Lie 导数平流代替传统向量平流，使 Euler 方程自然保持 Kelvin 环量定理。数值上仅需在 semi-Lagrangian 回溯采样外多乘一个 Jacobian 转置，开销可忽略，即可显著改善角动量与涡量守恒，且与现有流体求解器兼容。

## 价值评估

**Doctor 指定精读。** 按 6 级标准，这篇应按 **5/6：高优先级精读** 处理：idea 非常清晰，把速度变量从 vector field 换成 covector/one-form 后，Euler 对流自然写成 Lie advection；计算结果扎实，主要面向图形学流体中的涡结构保持；预言能力中等偏强，适合长时间保持涡量/环量而非用于高精度工程湍流闭合；方法新颖性高，是把 Kelvin circulation theorem 直接落到 advection-projection solver 的代表；来源为 SIGGRAPH/ACM TOG 2022，可信度高。精读判断：它是 `Hamiltonian ideal fluid`、Morrison 非正则 Hamiltonian、`Clebsch Maps` 与工程流体求解器之间的桥梁，值得作为结构保持不可压流体离散的重点样板。

## 公式与代码梳理

#### 数学结构与核心公式

本文的核心记号约定是：$v$ 表示速度向量场，$u=v^\flat$ 表示由度量 $g$ 降指标得到的速度余向量，也就是一形式；在欧氏网格上可以把 $u$ 看成速度分量数组，但它的变换律不是向量推前，而是 covector pullback。不可压 Euler 方程通常写为

$$
\partial_t v+\nabla_v v=-\nabla p,\qquad \nabla\cdot v=0 .
$$

把速度改写为一形式 $u=v^\flat$ 后，利用一形式 Lie 导数

$$
(\mathcal L_v u)_i=v^j\partial_j u_i+u_j\partial_i v^j ,
$$

以及欧氏情形 $u_i=v_i$，有恒等式

$$
\mathcal L_v u=(v\cdot\nabla)v^\flat+d\left(\frac12 |v|^2\right).
$$

因此 Euler 方程等价于

$$
\partial_t u+\mathcal L_v u=-d\left(p-\frac12 |v|^2\right),\qquad \delta u=0 ,
$$

其中 $\delta$ 是余微分；在向量分析中 $\delta u=0$ 对应 $\nabla\cdot v=0$。这个形式很关键：右端是精确一形式，因此闭合回路上的积分不受影响：

$$
\frac{d}{dt}\oint_{\gamma_t}u=0 .
$$

这就是 Kelvin 环量定理的 covector 版本。若 $\varphi_t$ 是流映射，满足

$$
\frac{d}{dt}\varphi_t(a)=v(\varphi_t(a),t),
$$

则无压力部分的 covector 对流满足

$$
\frac{d}{dt}\varphi_t^*u(t)=0,
$$

即

$$
u(t)=(\varphi_t^{-1})^{*}u(0)
$$

或在半拉格朗日回溯映射 $X(x)=\varphi_{t_n,t_{n+1}}^{-1}(x)$ 下写成

$$
u^{*}(x)=DX(x)^T u^n(X(x)).
$$

这就是代码层面的核心差异：传统 velocity advection 多写为

$$
v^{*}(x)=v^n(X(x)),
$$

而 Covector Fluids 写为

$$
u^{*}(x)=DX(x)^T u^n(X(x)).
$$

也就是说，在普通半拉格朗日采样之外，多乘一个回溯映射的 Jacobian 转置。若离散变量存的是速度向量，最后仍需用度量升指标：

$$
v^{*}=(u^{*})^\sharp .
$$

在均匀欧氏网格上 $\sharp$ 可近似为逐分量识别；在曲线网格、AMR 或嵌入边界上，这一步应显式使用局部质量矩阵或 Hodge star。

压力投影仍保持 Chorin 型结构。先做 covector advection 得到 $u^{*}$，升指标得 $v^{*}$，再解 Poisson 方程

$$
\Delta q=\nabla\cdot v^{*},
$$

并更新

$$
v^{n+1}=v^{*}-\nabla q,\qquad u^{n+1}=(v^{n+1})^\flat .
$$

从一形式角度，投影减去的是精确一形式 $dq$。由于 $d^2q=0$，涡量二形式

$$
\omega=du
$$

不被投影步骤改变：

$$
d(u^{*}-dq)=du^{*}.
$$

这解释了为什么该方法能在 advection-projection 框架中减少涡量损失。传统速度平流错误地把 $v$ 当作标量分量逐点搬运，忽略了局部坐标基随流映射变形的协变变换；covector advection 则把 $DX^T$ 作为离散 pullback，直接保留一形式积分。

从非正则 Hamiltonian 角度看，不可压 Euler 是体积保持微分同胚群 $\mathrm{Diff}_{\rm vol}(M)$ 上的测地线，Eulerian 动量属于李代数对偶 $\mathfrak X_{\rm div}(M)^*$。Hamiltonian 是动能

$$
H[u]=\frac12\int_M u(v)\,dV=\frac12\int_M |v|^2\,dV ,
$$

演化可理解为余伴随运动

$$
\partial_t m+\operatorname{ad}_v^*m=0,
$$

其中 $m=u\otimes dV$ 是动量 one-form density（速度 one-form 与体积元的张量积，与 $u$ 通过度规升降指标对应）。不可压和压力约束把演化限制在 coadjoint orbit 上；Kelvin 环量、涡量通量、helicity 等都是这个几何结构的投影。Covector Fluids 的工程意义就在于：它没有显式实现完整 Lie-Poisson 积分器，却把最关键的 $\operatorname{ad}^*$ 对流变换嵌进了廉价的 semi-Lagrangian step。

#### 关键推导

第一步是把 Euler 方程从 vector advection 改写为 covector Lie advection。对一形式 $u=v_i dx^i$，

$$
\mathcal L_v u=i_vdu+d(i_vu).
$$

在欧氏空间中 $i_vu=|v|^2$，而 $i_vdu$ 对应涡量项。用分量展开得到

$$
(\mathcal L_vu)_i=v^j\partial_ju_i+u_j\partial_iv^j
=(v\cdot\nabla)v_i+\partial_i\left(\frac12|v|^2\right).
$$

代回 Euler 方程可得

$$
\partial_tu+\mathcal L_vu=-d\left(p-\frac12|v|^2\right).
$$

所以 pressure 只负责 gauge/exact form，不负责改变 $du$ 的拓扑内容。

第二步是从 Lie advection 得到 pullback 离散。若忽略右端 exact form，

$$
\partial_tu+\mathcal L_vu=0 .
$$

对随体曲线 $\gamma_t=\varphi_t(\gamma_0)$，

$$
\frac{d}{dt}\int_{\gamma_t}u
=\frac{d}{dt}\int_{\gamma_0}\varphi_t^*u
=\int_{\gamma_0}\varphi_t^*(\partial_tu+\mathcal L_vu)=0 .
$$

因此离散时应更新的是 $\varphi_t^*u$，不是逐分量搬运 $v$。半拉格朗日回溯 $X$ 给出局部公式 $u^{*}(x)=DX(x)^Tu^n(X(x))$。

第三步是投影与涡量的交换。压力投影为

$$
u^{n+1}=u^{*}-dq .
$$

取外微分：

$$
du^{n+1}=du^{*}-d^2q=du^{*}.
$$

因此投影只改变速度的一形式代表元，不改变涡量二形式。这与 `Hamiltonian ideal fluid` 中的非正则退化结构一致：物理状态在 gauge 商空间上演化，压力是约束乘子。

#### 对 HPC 框架的启示

对 Doctor 的框架，这篇最直接的价值是把“变量类型”提升为数值抽象：cell-centered vector、face flux、edge one-form、cell two-form 不应混用。可以在 AMR/HPC 框架中建立离散外微分接口：$d_0$ 对应 gradient，$d_1$ 对应 curl，$\delta$ 对应 divergence，Hodge star 负责 vector/covector 转换。这样 pressure projection、vorticity diagnostic、Kelvin circulation test 可以共享同一套离散微分算子。

与 `Hamiltonian ideal fluid` 的关联是：Covector Fluids 是非正则 Hamiltonian/coadjoint 结构的低成本工程投影。它不像完整变分积分器那样从离散作用量出发，但保住了最容易被传统 advection-projection 破坏的 circulation。与 `Clebsch Maps` 和 `Schrödinger's Smoke` 的关系是：三者都在寻找“比速度更合适”的流体变量；Covector 用 one-form，Clebsch 用相位/映射，Schrödinger 用 spinor wavefunction。

代码上，最值得封装的是 `advect_covector(field_u, backtrace_X, jacobian_DX)`。该 kernel 的访问模式与普通 semi-Lagrangian advection 几乎相同，但额外需要 $DX$。在 GPU 上，$DX$ 可由回溯映射的有限差分局部计算，也可与 flow-map 方法共享缓存。对 AMR，需要特别处理 coarse-fine 边界处的 $DX$ 连续性；否则环量误差会集中在 refinement interface 上。

与 JFNK/投影求解器的结合点在 Poisson 阶段。Covector advection 只替换显式对流，不改变压力 Poisson 的矩阵结构，因此很适合作为现有不可压求解器的低风险改造。对高阶有限元或 matrix-free 框架，则应把 $u$ 存为 Whitney 1-form 或 edge-based DOF，把投影写成 Hodge-Laplace 问题。

#### 待深入研究

1. 在 AMR coarse-fine 同步、reflux 和 interpolation 之后，如何定义离散回路积分 $\oint u_h$，使 Kelvin 误差可测且不被网格层级切换污染？
2. 对粘性 Navier-Stokes，covector Lie advection 与 diffusion step 的分裂误差如何控制？是否能设计保持 circulation 衰减律而非简单保环量的格式？
3. 能否把 covector advection 作为 LPNets 或等变神经算子的硬结构层，让网络只学习 subgrid stress 或 unresolved flow map？

## Review Questions

1. 若在 AMR 网格上实现 Covector Fluids，$DX^T u(X)$ 的离散 pullback 应定义在 cell center、face 还是 edge 上，才能与离散 curl/divergence 交换？
2. Covector advection 保持 Kelvin circulation，但不必严格保持能量；如何把它和辛/Poisson 时间积分或 energy correction 结合，避免长期能量漂移？
3. 若用神经网络学习回溯 flow map $X$，需要给网络施加哪些结构约束，才能保证 $DX$、体积保持和 covector pullback 不互相矛盾？

4. 若把 Covector Fluids 嵌入离散外微分/Hodge 框架，`DX^T` pullback 与离散 `d`、Hodge star 需要满足什么交换关系，才能真正保持 circulation 而不只是经验上更稳？
5. 在 AMR 或曲线网格上，`u` 作为 one-form 的存储位置应如何选择，才能让 Poisson 投影、涡量诊断和 coarse-fine 同步保持一致？
6. 该方法主要改善几何守恒而非能量守恒；若面向长期积分或高 Re 计算，是否需要再叠加 energy-preserving / symplectic 时间推进？

---

---
