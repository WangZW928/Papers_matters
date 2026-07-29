# Incompressible Navier–Stokes solve on noisy quantum hardware via a hybrid quantum–classical scheme

**Authors:** Zhixin Song

**DOI:** [10.1016/j.compfluid.2024.106507](https://doi.org/10.1016/j.compfluid.2024.106507)

**Source PDF:** `main.pdf`

---

## 摘要

本文针对含噪声量子硬件上求解不可压缩Navier–Stokes方程的计算困难，提出了一种混合量子-经典方案。该方法将非线性对流项与压力泊松方程的求解分别分配给经典计算机与变分量子求解器，并在IBM Q噪声模拟器上对二维方腔驱动流进行了数值实验。结果表明，在量子比特数较少且噪声水平适中的条件下，该方案能够以可接受的精度复现经典有限差分法的流场结果，验证了混合架构在近时期量子设备上求解流体力学问题的可行性。

## 结论

本文提出的混合量子-经典方案能够在含噪声量子硬件上有效求解不可压缩Navier–Stokes方程，通过将非线性部分保留在经典端、线性压力求解器迁移至量子端，实现了对经典计算瓶颈的缓解，并在噪声模拟中获得了与经典方法一致的流场分布。

**状态：** ✅ 已精修
