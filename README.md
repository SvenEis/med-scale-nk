# The dynamic consequences of a risk premium shock in a medium scale model with wage rigidity and different monetary policy regimes

This repository contains the final project for the course "Research Module in Macroeconomics and Public Economics" by Sven Eis (University of Bonn, winter term 22/23).

The paper deals with a non-linear medium-scale representative-agent New Keynesian model (RANK) and analyses the dynamic consequences of a risk premium shock, where a central bank deals either with inflation-level targeting (ILT) or price-level targeting (PLT).

---

The src folder contains all relevant files to run the model:

## `/yamls`
This folder contains to yaml files which contain the model. `model_ILT.yaml` for the model, where the central bank follows inflation-level targeting and `model_PLT.yaml`, where price-level targeting is implemented in the Taylor rule.

## `analysis.py`
This file solves the model using [`econpizza`](https://github.com/gboehl/econpizza) by Gregor Böhl, PhD.

## `plot.py`
This file plots the Impulse Response Functions.
