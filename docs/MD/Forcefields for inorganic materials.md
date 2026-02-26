# Forcefields for inorganic materials



## The Universal Force field (UFF)

$$
E_\text{total} = (E_\text{bond}+E_\text{angle}+E_\text{tor}+E_\text{inv})+(E_\text{vdw}+E_\text{elec})
$$

The parameters of UFF therefore do not directly contain forcefield parameters needed to do simulations with any combination of the 126 atom types covered, but essentially:

- Parameters for the individual atom types: bond radii as a function of hybridization, preferred angles, vdW parameters, torsion- and inversion energy barriers, effective nuclear charges
- Rules: for the calculation of the required forcefield parameters for atom pairs, triples etc. From the stored parameters for individual atoms.

Energy terms in UFF:

<u>bond stretching</u>: $E_\text{bond}=\frac{1}{2}(r_{ij}-r_0)^2$, or L-J, Morse, etc.
$$
r_{ij}=r_i+r_j+r_\text{BO}+r_\text{EN}
$$

- $r_i,r_j$ are the bond radius of the individual atom types $i$ and $j$
- $r_\text{BO}$ is the bond order correction term, $r_\text{BO}=-\lambda(r_i+r_j).\ln(n)$, n =1 for single bond, n=1.5 for aromatic ring, n=2 for double bond etc. $\lambda$ is proportional constant, set to $\lambda =0.1332$ based on optimization for propane, propene, propyne.
- $r_\text{EN}$ is the correction term for electronegativity differences, $r_\text{EN}= r_ir_j\frac{(\sqrt{\chi_i}-\sqrt{\chi_j})^2}{(\chi_ir_i+\chi_jr_j)}$