# Hartree-Fock

## Multi-electron $\textbf{Schr\"odinger}$ Equation

$$
\hat{H}=\sum_ih_i + \sum_i\sum_j\frac{1}{r_{ij}}
$$

For a single electron integral $\epsilon_i=\int\mathcal{X_i}^*(x_i)h_i\mathcal{X_i}(x_i)dx_i$

For two electron integral:  $\epsilon_i=\int\mathcal{X_1}^*(x_1)\mathcal{X_2}^*(x_2)h_i\mathcal{X_1}(x_1)\mathcal{X_2}(x_2)dx_1dx_2$

**Energy contribution**

- Coulomb: $J =\int\mathcal{X_1}^*(x_1)\mathcal{X_2}^*(x_2)\frac{1}{|r_{12}|}\mathcal{X_1}(x_1)\mathcal{X_2}(x_2)dx_1dx_2 = \int|\mathcal{X_1}(x_1)^2|\frac{1}{r_{12}}|\mathcal{X_2}(x_2)^2|dx_1dx_2$
- Exchange: $K =$



So, for exchange behavior for electron orbitals with inverse spin, the exchange term will be zero.

## Hartree-Fock equation



## Linear combination of atomic orbitals (LCAO)

$$
\mathcal{X_i}=\sum C_{ui}\psi_u\\
\hat{F}(x_1)\mathcal{X_i} =\epsilon_i\mathcal{X_i}(x_1)\\
\Rightarrow \hat{F}(x_1)\sum C_{ui}\psi_u = \epsilon_i\sum C_{ui}\psi_u
$$

- $\psi_u$ is a basis function set, $\psi\in \{\psi_{100},\psi_{200},\psi_{300}\}$