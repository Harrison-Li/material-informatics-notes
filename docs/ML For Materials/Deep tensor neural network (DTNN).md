# Deep tensor neural network (DTNN)

The core idea is to represent atoms in the molecule as vectors depending on their type and to subsequently refine the representation by embedding the atoms in their neighborhood

**1. Assign initial atomic descriptors**

They assign initial coefficient to each atom $i$ of the molecule according to is nuclear charge $Z_i$
$$
c_i^{(0)}=c_{Z_i} \in R^B
$$
Where B is the number of basis functions,  All presented models use atomic descriptors with 30 coefficients.

**2. Gaussian feature expansion of the interatomic distances**

The inter-atomic distances Dij are spread across many dimensions by a uniform grid of Gaussians.
$$
\hat{d_{ij}}=[\exp(-\frac{(D_{ij}-(u_{\text{min}+k\Delta\mu}))^2}{2\sigma^2})]_{0\leq k\leq \mu_\text{max}/\Delta\mu}
$$

- $\Delta \mu$ is the gap between two Gaussians of width $\sigma$



**3. Perform T interaction passes**

$c_i^{(t)}$ is corresponding  to atom $i$ after $t$ steps updates.
$$
c_i^{(t+1)}=c_i^{(t)}+ \sum_{j\ne i}v_{ij}
$$
$v$ is the interaction, reflects the influence of atom j at a distance $D_{ij}$ on atom $i$.

$$
v_{ij}=\tanh{[W^{\text{fc}}(\,(W^\text{cf}c_j+b^{f_1})\circ (W^\text{df}\hat{d_{ij}}+b^{f_2}))]}
$$

- Circle $\circ$ represents the element-wise production

**4. Predict energy contributions**

Finally, we predict the energy contributions $E_i$ from each atom $i$. Employing two fully-connected layers, for each atom a scaled energy contribution $\hat{E_i}$ is predicted
$$
o_i=\tanh{(W^\text{out1}c_i^{(T)}+b^\text{out1})}\\
\hat{E_i}=W^\text{out2}o_i+b^\text{out2}
$$
Due to $\hat{E_i}$ if shifted to mean $E_\mu$ and scaled by the $\text{s.d}\,E_\sigma$ of the energy per atom. So, final energy is:
$$
E_i=E_\sigma\hat{E_i}+E_\mu
$$
**5. Obtain the molecular energy** $\mathbf{E=\sum_i E_i}$