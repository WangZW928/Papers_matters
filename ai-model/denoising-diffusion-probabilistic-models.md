# Denoising Diffusion Probabilistic Models

**Source PDF:** `2006.11239v2.pdf`

---

## Abstract

_Not available_

## Summary


**核心问题：** 高质量生成模型的训练与采样问题

**方法：** 去噪扩散概率模型（DDPM）方法

**关键结果：** 
1. 提出了扩散模型的完整概率框架
2. 实现了与GAN可比的高质量图像生成
3. 展示了扩散过程的渐进生成与插值能力

**与你工作的相关性：** 扩散模型可用于流场重建、超分辨和数据同化

**状态：** ✅ 完整摘要


## Review Questions

### 🤔 Questions
1. test

## Review Questions

### 🤔 Questions
1. **Q:** How does the variational lower bound connecting the forward (fixed) diffusion process to the reverse (learned) generative process guarantee a tractable training objective, and why does this bound simplify to a weighted denoising score-matching objective?
2. **Q:** Why does the reparameterization trick allow the DDPM loss to be expressed as a simple noise-prediction task, and how does this connect DDPMs to score-based generative modeling via the score function?
3. **Q:** The forward diffusion process is mathematically equivalent to a discretization of the heat equation SDE. How might this physical analogy inspire fluid dynamics applications such as turbulence closure modeling, super-resolution of flow fields, or data assimilation in CFD?
