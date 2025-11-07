# SchNet

## Introduction

All of the computation is applied to stable systems which means equilibrium conditions. i.e., local minima of the potential energy

surface $E(r_1,...,r_n)$ where $r_i$ is the position of atom $i$

But it's not clear how obtain an equilibrium state without optimize the position of atoms. Therefore, we need to compute both the total energy $E(r_1,...,r_n)$ and the forces acting on the atoms.
$$
F_i(r_1,...,r_n)=-\frac{\partial E_i}{\partial r_i}
$$
**Requirement for a MLFF**

1. In order to learn the equilibrium state, the model should  learn a representation for molecules using equilibrium and non-equilibrium conformations.
2. Invariance of the molecular energy with respect to rotation, translation and atom indexing.

## Continuous-filter convolutions

Given the feature representations of $n$ objects $X^l = (x^l_1,...,x^l_n)$ with $x^l_i\in\mathbb{R}^F$ at locations $R=(r_1,...,r_n)$ with $r_i \in \mathbb{R}^D$ , the continuous-filter convolutional layer $l$ requires a filter-generating function