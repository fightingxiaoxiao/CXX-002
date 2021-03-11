# 风致雪漂模拟

## 简介

本算例用于湍流风场下的雪颗粒运动。

## 场映射

* 使用[case_packing算例](../case_packing)得到的拉格朗日场初始化雪堆。
* 使用[case_steady算例](../case_steady)得到的流场信息初始化风场。

## 求解器

[case_drifting](.)算例采用作者自行扩展的求解器[DPMFoamEx](http://github.com/fightingxiaoxiao/DPMFoamEx/)。

> 为什么要扩展该求解器？

当我们希望在周期性流场中指定某个方向的质量流率(或平均速度)时，需采用自定义源相（fvOptions）中的`meanVelocityForce`，但很遗憾的是OpenFOAM的原生求解器DPMFoam并未引入这一功能。

> 我要如何安装这一求解器以运行这一算例？

[DPMFoamEx](http://github.com/fightingxiaoxiao/DPMFoamEx/)是高度依赖OpenFOAM版本的求解器，您应当在[DPMFoamEx](http://github.com/fightingxiaoxiao/DPMFoamEx/)下方的README中检查求解器的详细信息。
