TBR Data
========

This repository contains data produced by the tritium breeding ratio Monte Carlo simulation.


Usage
-----

The repository is divided into multiple runs, each corresponding to a separate directory. For the reasons of scalability, runs are divided into a multitude of batches that correspond to individual jobs scheduled at a computing cluster. These are labeled by file prefix (e.g. `batch42...`).

Each batch consists of two files:

    1. `_in.csv` file that contains data points in the TBR parameter domain to be sampled,
    2. `_out.csv` file that repeats the contents of the `_in.csv` file but also includes the results of the TBR simulation for each data point.

Sometimes, data handling scripts are included for convenience.


License
-------

This work was realised in 2020 as a group project at University College London with the support from UKAEA. The authors of the implementation are Petr Mánek and Graham Van Goffrier.

Permission to use, distribute and modify is hereby granted in accordance with the MIT License. See the LICENSE file for details.
