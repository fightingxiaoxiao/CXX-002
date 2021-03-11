# 雪颗粒的堆积床模拟

## 简介

本算例用于模拟稳定状态下的雪颗粒堆积.

## Python shell

采用Python脚本初始化颗粒(constant/kinematicCloudPositions)，只需要指定一个方盒即可填充颗粒.相关的代码位于[pythonModule](../pythonModule).

## 求解器

[case_packing](.)算例采用作者自行扩展的求解器[DPMFoamEx](http://github.com/fightingxiaoxiao/DPMFoamEx/).但是事实上，[case_packing](.)同样能够在原生的DPMFoam/MPPICFoam下运行.
> 为什么要扩展该求解器？
当我们希望在周期性流场中指定某个方向的质量流率(或平均速度)时，需采用自定义源相（fvOptions）中的`meanVelocityForce`，但很遗憾的是OpenFOAM的原生求解器DPMFoam并未引入这一功能.
> 我要如何安装这一求解器以运行这一算例？
[DPMFoamEx](http://github.com/fightingxiaoxiao/DPMFoamEx/)是高度依赖OpenFOAM版本的求解器，您应当在[DPMFoamEx]下方的README中检查求解器的详细信息.
