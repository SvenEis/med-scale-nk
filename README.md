# The dynamic consequences of a risk premium shock in a medium scale model with wage rigidity and different monetary policy regimes

This repository contains the final project for the course "Research Module in Macroeconomics and Public Economics" by Sven Eis (University of Bonn, winter term 22/23).

The paper deals with a non-linear medium-scale representative-agent New Keynesian model (RANK) and analyses the dynamic consequences of a risk premium shock, where a central bank deals either with inflation-level targeting (ILT) or price-level targeting (PLT).

## Usage

To get started, create and activate the environment with

.. code-block:: console

    $ conda/mamba env create
    $ conda activate med-scale-nk

---

The src folder contains all relevant files to run the model:

## `model_ILT.yaml`
RANK model, where inflation-level targeting is implemented in the Taylor rule.

## `model_PLT.yaml`
RANK model, where price-level targeting is implemented in the Taylor rule.

## `analysis.py`
This file contains a function which solves the model using [`econpizza`](https://github.com/gboehl/econpizza) by Gregor Böhl, PhD.

## `plot.py`
This file contains a function for creating the plots.

## `run_all.py`
This file runs all the necessary python files and creates a bld folder to save the data and plots.
