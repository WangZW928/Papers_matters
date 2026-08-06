# 去噪扩散概率模型

**来源 PDF：** `2006.11239v2.pdf`
**阅读状态：** 🔬 精读
**流程状态：** ①元数据 ✓ | ②初稿 ✓ | ③评估 ✓(精读) | ④补充 ✓ | ⑤索引 ⏳ | ⑥review ✓ | ⑦提交 ⏳

---

## 摘要

_暂无_

## 总结

**核心问题：** 高质量生成模型的训练与采样问题

**方法：** 去噪扩散概率模型（DDPM）方法

**关键结果：**
1. 提出了扩散模型的完整概率框架
2. 实现了与 GAN 可比的高质量图像生成
3. 展示了扩散过程的渐进生成与插值能力

**与你工作的相关性：** 扩散模型可用于流场重建、超分辨和数据同化

## 价值评估

Doctor 指定精读（学习路线规划推荐）。DDPM 是现代扩散生成模型的基础论文之一，对后续流场重建、物理约束生成、数据同化和不确定性采样都有直接影响。对 Doctor 的方向而言，关键不是图像生成结果，而是“正向热化/加噪 + 反向学习去噪”的概率结构如何迁移到 PDE 场数据。

## 公式与代码梳理

### 数学结构与核心公式

DDPM 定义固定的前向扩散过程：

$$
q(x_t|x_{t-1})=
\mathcal{N}\left(x_t;\sqrt{1-\beta_t}x_{t-1},\beta_t I\right),
$$

其中 $\beta_t$ 是预设噪声日程。记

$$
\alpha_t=1-\beta_t,\qquad
\bar{\alpha}_t=\prod_{s=1}^t\alpha_s,
$$

则任意时刻可直接从干净样本 $x_0$ 采样：

$$
q(x_t|x_0)=
\mathcal{N}\left(x_t;\sqrt{\bar{\alpha}_t}x_0,(1-\bar{\alpha}_t)I\right),
$$

等价重参数化为

$$
x_t=\sqrt{\bar{\alpha}_t}x_0+\sqrt{1-\bar{\alpha}_t}\epsilon,\qquad
\epsilon\sim\mathcal{N}(0,I).
$$

反向生成过程由神经网络参数化：

$$
p_\theta(x_{t-1}|x_t)=
\mathcal{N}\left(x_{t-1};\mu_\theta(x_t,t),\Sigma_\theta(x_t,t)\right).
$$

论文将变分下界分解为逐时间步 KL 项：

$$
\mathbb{E}_q[-\log p_\theta(x_0)]
\le
\mathbb{E}_q\left[
-\log\frac{p_\theta(x_{0:T})}{q(x_{1:T}|x_0)}
\right].
$$

关键简化是让网络预测噪声 $\epsilon_\theta(x_t,t)$，训练目标写成

$$
\mathcal{L}_{\mathrm{simple}}
=
\mathbb{E}_{t,x_0,\epsilon}
\left[
\left\|\epsilon-\epsilon_\theta\left(
\sqrt{\bar{\alpha}_t}x_0+\sqrt{1-\bar{\alpha}_t}\epsilon,t
\right)\right\|^2
\right].
$$

这说明模型不是直接生成 $x_0$，而是在每个噪声尺度上学习 score/去噪方向。反向均值可由噪声预测写出：

$$
\mu_\theta(x_t,t)
=\frac{1}{\sqrt{\alpha_t}}
\left(
x_t-\frac{\beta_t}{\sqrt{1-\bar{\alpha}_t}}\epsilon_\theta(x_t,t)
\right).
$$

### 关键推导/算法

训练算法：

```text
repeat:
    sample x0 from data
    sample t uniformly from {1,...,T}
    sample epsilon ~ N(0, I)
    xt = sqrt(alpha_bar[t]) * x0 + sqrt(1-alpha_bar[t]) * epsilon
    loss = ||epsilon - epsilon_theta(xt, t)||^2
    update theta
```

采样算法：

```text
x_T ~ N(0, I)
for t = T,...,1:
    z ~ N(0, I) if t > 1 else 0
    mu = (x_t - beta_t / sqrt(1-alpha_bar[t]) * epsilon_theta(x_t,t)) / sqrt(alpha_t)
    x_{t-1} = mu + sigma_t * z   # sigma_t = sqrt(beta_t)（固定方差设定下）
return x_0
```

推导逻辑是：前向过程固定且可解析，因此真实后验 $q(x_{t-1}|x_t,x_0)$ 是 Gaussian；反向模型只需逼近这个后验。通过重参数化，KL 项可转化为噪声预测误差，形成稳定的监督学习问题。

### 对 HPC 框架的启示

1. 扩散模型天然适合场数据生成和重建，但 $T$ 步反向采样代价高，HPC 应重点支持 batched inference、mixed precision 和 operator fusion。
2. 对 PDE 场，$x_t$ 不应只是图像张量；需要把变量分量、网格、边界条件和守恒约束纳入数据结构。
3. 噪声日程类似人工时间尺度；可探索与物理耗散尺度、谱截断尺度或 LES filter width 对齐。
4. 采样过程可插入 projection、PDE residual guidance 或 data assimilation 约束，形成物理一致的条件生成器。
5. 扩散模型的概率性可用于不确定性量化，尤其适合稀疏观测下的多解流场重建。

### 待深入研究的问题

1. 对不可压流场，应该在速度场上扩散后投影，还是在流函数/涡量等自动满足约束的变量上扩散？
2. DDPM 的 Markov 反向链如何与数值 PDE 的时间推进区分？能否把二者统一为概率积分器？
3. 物理残差作为 guidance 会不会破坏训练得到的概率模型一致性？如何量化这种偏差？

## Review Questions

4. 1. DDPM 的 simplified loss 与完整变分下界在什么条件下近似等价、在什么条件下会偏离？这种偏离对物理场重建中的校准误差意味着什么？
5. 2. 如果把扩散变量换成受守恒约束的场变量，前向加噪是否还应保持各向同性高斯，还是应该改成与物理算子谱结构匹配的噪声过程？
6. 3. 对 HPC 场景，反向采样的主要成本到底来自网络评估、通信，还是物理 guidance；这会如何影响选择 DDPM、DDIM 或 consistency/distillation 路线？

1. 去噪扩散概率模型中的前向固定扩散过程与反向学习生成过程之间，变分下界如何保证训练目标是可处理的？为什么该下界又可以简化为加权的去噪 score matching 目标？
2. 为什么重参数化技巧可以把 DDPM 的损失写成一个简单的噪声预测任务？这一点又如何通过 score function 将 DDPM 与基于 score 的生成建模联系起来？
3. 前向扩散过程在数学上等价于热方程 SDE 的离散化。这种物理类比如何启发流体力学中的应用，例如湍流闭合建模、流场超分辨或 CFD 中的数据同化？
