# Simulation for drifting snow

## Language(多语言)

[English(This page)](README_en.md)  |  [简体中文](README.md)

## Introduction

This case is designed to reproduce the snow drifting in a turbulent wind field.

## Map Fields

* Map fields from [case_packing](../case_packing) to initialize the lagrangian field(snow packing bed).
* Map fields from [case_steady](../case_steady) to initialize the velocity, pressure, turbulence information...

## Solver

[case_drifting](.) uses a custom solver [DPMFoamEx](http://github.com/fightingxiaoxiao/DPMFoamEx/).

> Why extend the origin DPM solver?

When you want to specify the mass flow rate (or average velocity) in a certain direction in a periodic flow field, you need to use the `meanVelocityForce` in the custom source term module(fvOptions). Unfortunately, this feature is not provided by DPMFoam, which is the origin DPM solver in OpenFOAM.

> How do I install the extended solver to run this case?

[DPMFoamEx](http://github.com/fightingxiaoxiao/DPMFoamEx/) is a solver that highly depends on the OpenFOAM version. You should check the details of this solver in the [README](http://github.com/fightingxiaoxiao/DPMFoamEx/README.md) under [DPMFoamEx](http://github.com/fightingxiaoxiao/DPMFoamEx/).
