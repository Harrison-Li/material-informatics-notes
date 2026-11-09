# Long Range MLIP

## Latent Ewald summation

Ref: 10.1038/s41524-025-01577-7

For a periodic atomic system, the total energy can be divided into a short-range and a long range part. i.e. $E=E^{sr}+E^{lr}$, the short range is summed over the atomic contribution of each atom $i$ by the GNN:
$$
E^{sr}=\sum_iE_\theta{B_i}
$$
Where $E_\theta$ is the neural network with parameters $\theta$ that maps the invariant features $B$

For the long range part, another MLP with parameter $\phi$ maps the invariant features into a hidden variable, or called latent charge in paper:
$$
q_i^\text{raw}=Q_\phi(B_i)
$$




The Coulomb interaction is also separated into short and long range contributions using Gaussian screening:
$$
\frac{1}{r}=\frac{\text{erfc}(\alpha r)}{r} + \frac{\text{erf}(\alpha r)}{r}
$$
Where $\alpha$ denotes the Gaussian screening parameter, while $\text{erfc}(\cdot)$ and $\text{erf}(\cdot)$ denotes the error function and its complementary function. The rapidly decaying short range contribution is contributing to the short range energy term $E^\text{SR}$, and the smooth long range contribution is evaluated explicitly from the latent charges.

And the predicted latent charge can be used to compute the long range contribution $E^\text{lr}$:
$$
E^\text{lr} = \frac{1}{2\epsilon_0 V}\sum_{0<k<k_c}\frac{1}{k^2}e^{-\sigma^2k^2/2}|S(\mathbf{k})|^2
$$
The structure factor $S(\mathbf{k})$ of the hidden variable is defined as:
$$
S(\mathbf{k}) = \sum_{i=1}^B q_i^\text{les} e^{ikr}
$$


## Born Effective Charge tensor

The polarization $P$ of a system underlies many electrical response properties including capacitance, dielectric constant, ferroelectricity, piezoelectricity, ionic conductivity, and infrared (IR) spectra. The Born effective charge (BEC) tensor $Z^\star$ quantifies the variation in $\mathbf{P}$ due to an atomic displacement at position $r_i$ of atom $i$. And those two properties can be extracted from Long range MLIP.
$$
Z^\star_{i\alpha\beta} = \frac{\partial P_\alpha}{\partial r_{i\beta}}=\frac{\partial \mathcal{F}_{i\alpha}}{\partial E_\beta^0}
$$
Where $\alpha, \beta$ are Cartesian directions. And second part links the electrostatic force $\mathcal{F_i}$ on atom $i$ resulting from the external electric field $E_0$.



They interpret the Latent charges as scaled charges. $q^\text{les}=q_i/\sqrt{\epsilon_\infty}$.  and $\epsilon_\infty$ denotes the high-frequency relative permittivity.

While the real polarization (dipole moment) of a finite system is:
$$
P = \sum_{i=1}^N q_i r_i
$$
And the BEC $Z^\star$ can be obtained by taking its derivative:
$$
Z^\star_{i\alpha\beta} = \frac{\partial P_\alpha}{\partial r_{i\beta}} = q_i\delta_{\alpha,\beta}+ \sum_{j=1}^Nr_{j\alpha}\frac{\partial q_j}{\partial r_{i\beta}}
$$

> [!NOTE]
> $$
> \frac{\partial P_\alpha}{\partial r_{i\beta}}
> =
> \frac{\partial}{\partial r_{i\beta}}
> \left(
> \sum_jq_jr_{j\alpha}
> \right)
> $$
> Applying the product rule:
> $$
> \begin{aligned}
> \frac{\partial P_\alpha}{\partial r_{i\beta}}= \sum_j [r_{j,\alpha}\frac{\partial q_j}{\partial r_{i,\beta}} + \frac{\partial r_{i,\alpha}}{\partial r_{i,\beta}}  q_j]\\
> \Downarrow \frac{\partial r_{i,\alpha}}{\partial r_{i,\beta}} = \delta_{\alpha,\beta}\\
> = q_i\delta_{\alpha,\beta}+ \sum_{j=1}^Nr_{j\alpha}\frac{\partial q_j}{\partial r_{i\beta}}
> \end{aligned}
> $$
> This two terms denotes for static charge contribution and charge-redistribution contribution for the BEC



**Extending the BEC to PBC condition**

Equation 7 did not work for PBC. Since $\Delta P = q_i(nL+x) - q_i(x) = nq_iL\neq0$

So, 
$$
P_\alpha (k) = \sum_{j=1}^N\frac{q_j}{ik}e^{ikr_{i,\alpha}}
$$
