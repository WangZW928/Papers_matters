# 涡段云上的不可压缩流动模拟

**作者：** Shiying Xiong, Rui Tao, Yaorui Zhang, Fan Feng, and Bo Zhu

**DOI：** [10.1145/3450626.3459865](https://doi.org/10.1145/3450626.3459865)

**源 PDF：** `vortex_segment.pdf`

**阅读状态：** 🔬 精读
**流程状态：** ①元数据 ✓ | ②初稿 ✓ | ③评估 ✓(精读) | ④补充 ✓ | ⑤索引 ✓ | ⑥review ✓ | ⑦提交 ⏳

---

## 摘要

### 中文翻译

本文用离散涡段云（vortex segment clouds）表示强各向异性涡量结构：每个线段携带环量与方向，Biot-Savart 求速度场，split/merge/reseeding 处理拓扑变化。计算效率接近经典涡粒子方法，同时更好地保持涡量守恒与涡管拓扑。

## 价值评估

**Doctor 指定精读。** 按 6 级标准，这篇应按 **4/6：强相关精读** 处理：idea 清晰，用离散涡段云表示强各向异性涡量结构；计算结果对图形学烟雾、涡管重联、旋转固体尾涡较强；预言能力中等，主要是视觉和几何动力学模拟，物理黏性与湍流精度需谨慎；方法新颖性较高，在 vortex particle 与 vortex filament 之间提供折中表示；来源为 ACM TOG/SIGGRAPH 2021，图形学流体可信。精读判断：它是 Doctor 涡动力学、Biot-Savart 快速算法、Lagrangian-HPC 和量子涡/涡丝表示的重要补充。

## 公式与代码梳理

#### 数学结构与核心公式

不可压流体的涡量形式为

$$
\omega=\nabla\times u,\qquad \nabla\cdot u=0 .
$$

Navier-Stokes 涡量方程为

$$
\partial_t\omega+u\cdot\nabla\omega
=(\omega\cdot\nabla)u+\nu\Delta\omega .
$$

无黏 Euler 情形去掉扩散项：

$$
D_t\omega=(\omega\cdot\nabla)u .
$$

速度由 Biot-Savart 定律恢复：

$$
u(x)=\frac1{4\pi}\int_{\mathbb R^3}
\omega(y)\times\frac{x-y}{|x-y|^3}\,dy .
$$

传统 vortex particle 方法把涡量表示成 blob：

$$
\omega(x)\approx\sum_i \gamma_i \zeta_\epsilon(x-x_i),
$$

但强细长涡管的方向性会被各向同性 blob 弱化。vortex filament 方法能表示涡线，却在拓扑更新、开放涡段、边界交互上麻烦。本文用 vortex segment cloud 折中：每个 primitive 是带方向的短线段

$$
s_i=(x_i,l_i,\Gamma_i),
$$

其中 $x_i$ 是中心，$l_i$ 是线段向量，$\Gamma_i$ 是环量或强度。涡量可形式化为

$$
\omega(x)\approx\sum_i \Gamma_i l_i\,\zeta_\epsilon(x-x_i),
$$

或更接近线积分地写为

$$
\omega(x)\approx\sum_i\Gamma_i\int_{-1/2}^{1/2}
l_i\,\zeta_\epsilon(x-x_i-\alpha l_i)\,d\alpha .
$$

单个有限涡段对速度的贡献可由正则化 Biot-Savart 写成

$$
u_i(x)=\frac{\Gamma_i}{4\pi}
\int_{s_i}\frac{d y\times(x-y)}
{\left(|x-y|^2+\epsilon^2\right)^{3/2}} .
$$

无正则化有限直涡段常见闭式形式为

$$
u_i(x)=\frac{\Gamma_i}{4\pi}
\frac{r_1\times r_2}{|r_1\times r_2|^2}
\left(
\frac{r_1\cdot l_i}{|r_1|}
-\frac{r_2\cdot l_i}{|r_2|}
\right),
$$

其中 $r_1=x-a_i$，$r_2=x-b_i$，$a_i,b_i$ 是线段端点。实际实现会用 smoothing radius $\epsilon$ 避免近场奇异。

涡段几何演化来自涡线随流映射变形。端点随速度运动：

$$
\frac{d a_i}{dt}=u(a_i),\qquad
\frac{d b_i}{dt}=u(b_i).
$$

于是中心和方向更新为

$$
x_i=\frac{a_i+b_i}{2},\qquad l_i=b_i-a_i .
$$

这自动包含拉伸项 $(\omega\cdot\nabla)u$：若两端点速度不同，$l_i$ 被拉长、旋转或压缩。对黏性项，常用 particle strength exchange 思路：

$$
\frac{d\omega_i}{dt}\bigg|_{\nu}
\approx \nu\sum_j V_j(\omega_j-\omega_i)\eta_\epsilon(x_i-x_j),
$$

其中 $\eta_\epsilon$ 是扩散核。对涡段，需要同时处理强度、方向和 segment length 的一致性。

局部 reseeding 是本文算法核心之一。若线段过长，则 split：

$$
s_i\rightarrow s_{i,1}+s_{i,2}.
$$

若线段过短、过密或方向相近，则 merge。若邻域方向变化大或涡管拓扑发生变化，则重新采样以保持 segment cloud 的覆盖质量。目标不是保持固定连接拓扑，而是用局部云表示涡量几何，因此能处理非闭合涡管重联和断裂。

固体边界通过边界涡量或边界条件耦合。不可穿透条件为

$$
u\cdot n=u_b\cdot n\quad\text{on }\partial\Omega .
$$

动态固体可通过边界诱导涡段、镜像/面元修正或 projection-like correction 处理，使 Biot-Savart 得到的速度满足边界法向约束。

#### 关键推导

第一步是涡段为何自然编码拉伸。连续涡线材料元 $\delta x$ 满足

$$
D_t\delta x=(\nabla u)\delta x .
$$

涡量满足

$$
D_t\omega=(\nabla u)\omega .
$$

因此在无黏 barotropic 不可压流中，涡量方向和材料线元同向演化，这就是涡量拉伸方程（严格说 Cauchy vorticity formula 是通过流映射 Jacobian 的显式表示，这里给出的是其微分形式）。把涡段端点随流 advect，相当于直接离散材料线元，所以拉伸项无需显式差分 $\nabla u$。

第二步是 Biot-Savart 从涡量恢复速度。不可压条件和 $\omega=\nabla\times u$ 给出

$$
\nabla\times\nabla\times u=\nabla(\nabla\cdot u)-\Delta u=-\Delta u=\nabla\times\omega .
$$

在无界域中用 Laplace Green 函数可得

$$
u(x)=\frac1{4\pi}\int\omega(y)\times\frac{x-y}{|x-y|^3}\,dy .
$$

离散后就是所有涡段对所有采样点的 N-body 求和。直接计算为 $O(N^2)$，大规模时需要树码、FMM 或局部网格加速。

第三步是 reseeding 与守恒量平衡。split/merge 不能只保持线段数量稳定，还要保持局部环量和涡量矩。理想条件是对局部测试函数 $\phi$，

$$
\sum_{i\in old}\Gamma_i\int_{s_i}\phi(x)\,dx
\approx
\sum_{j\in new}\Gamma_j\int_{s_j}\phi(x)\,dx .
$$

至少应保持零阶环量、一阶位置矩和主方向。否则 reseeding 会成为隐式数值黏性或虚假涡量源。

#### 对 HPC 框架的启示

这篇对 Doctor 的框架启示主要在 Lagrangian vortex data structure。相对于 Eulerian 网格，涡段云的数据结构是动态数组：split、merge、邻域搜索、近远场分离、固体边界耦合。这非常适合 GPU，但需要 carefully designed memory pool、prefix-sum compaction、cell list 或 BVH。Biot-Savart 是核心瓶颈：近场可用 cell list，远场可用 FMM/treecode，或者 vortex-in-cell 把涡量散布到网格后用 FFT/Poisson 求速度。

与 `Schrödinger's Smoke` 的关系是：两者都重视涡丝和重联，但变量完全不同。Schrödinger 方法用 spinor 和 FFT 让重联自然发生；vortex segment cloud 用几何 primitive 和 reseeding 显式表达涡管拓扑更新。与 `Clebsch Maps` 的关系是：Clebsch 更适合诊断和拓扑可视化，涡段云更适合 Lagrangian 运动和局部编辑。

对 HPC 框架，可设计统一的 vortex backend：Eulerian grid 存 $u,p$，segment cloud 存 $\omega$，两者通过 scatter/gather 和 Biot-Savart/Poisson 转换。若与 AMR 结合，可让涡段驱动 refinement tagging：高 $|\omega|$、高曲率、高拉伸率区域自动细化。对 AI4Physics，可把涡段云看成几何图，使用 SE(3)-equivariant GNN 学习 subgrid stretching、reconnection trigger 或 reseeding policy。

#### 待深入研究

1. 涡段云的 split/merge 如何严格保持 helicity 或至少控制 helicity drift？
2. 对高雷诺数真实 DNS，涡段正则化半径 $\epsilon$ 与物理黏性尺度、网格尺度之间应如何匹配？
3. 能否把 Biot-Savart 远场求和、AMR Poisson 和 GPU FMM 统一成一个可替换 velocity reconstruction backend？

## Review Questions

1. vortex segment cloud 与 vortex particle、vortex filament 相比，分别牺牲和保留了哪些几何不变量？
2. 若要在多 GPU 上实现涡段 Biot-Savart，近场直接求和、远场 FMM、vortex-in-cell 三种方案的通信瓶颈分别在哪里？
3. 涡重联在涡段云中由 reseeding/topology update 触发；如何判定这是物理重联、数值正则化结果，还是视觉模拟中的人为拓扑编辑？

4. 在 segment split/merge 过程中，最低限度应守恒哪些矩量或拓扑量，才能避免 reseeding 本身成为主要数值耗散源？
5. 多 GPU 上若做 Biot-Savart/FMM，segment cloud 的动态负载均衡会不会比核函数求和本身更快成为瓶颈？
6. 若把这种几何表示用于科研级涡动力学而非图形学，如何定量区分物理重联、正则化诱导重联和纯拓扑编辑？

---

---
