# GemNet: Universal Directional Graph Neural Networks for Molecules

### Context: Spherical Harmonics

Spherical harmonics $Y_l^m(\theta, \phi)$ appear as solutions to the **angular part** of Laplace’s equation in spherical coordinates.

- l = **degree** (non-negative integer, like angular momentum quantum number)
- m = **order** (integer related to projection/orientation)





## Motivation

1. Regular GNNs are only as powerful as the 1-Weisfeiler Lehman test of isomorphism and thus cannot distinguish between certain molecules. Moreover, they require a large number of training samples to achieve good accuracy.
2. Resolve the questionable expressiveness of GNNs by proving sufficient conditions for universality in the case of **invariance to translations and rotations and equivariance to permutations**; and then extending this result to rotationally equivariant predictions.

## Preliminaries

GNNs for molecules typically incorporate directional information in one of two ways: Via <u>SO(3) representations</u> or by <u>using directions in real space</u>

**Mathematical terminology**

Assume a point cloud with n points (atoms), each is associated with a position in coordinates $\mathbf{X}\in \mathbb{R}^{3\times n}$ and a set of rotationally invariant features (e.g. atom types) defined as $\mathbf{H}_{\text{in}}\in\mathbb{R}^{h\times n}$

We define model classes by sets of functions $\mathcal{F}$, we need to prove that the set $\mathcal{F}$ is equal to the full set of functions $\mathcal{G}'$ which are invariant to the group of translations $\mathbb{T}^3$ , rotations $\text{SO(3)}$ and equivariant to the group of permutations. $\rightarrow \mathbb{T}^3 \or \text{SO(3)}\or S_n$, We denote a vector’s norm by $x = ||x||_2$, with direction towards $\hat{x}=\mathbf{x}/x$, and the relative position between point $a$ and $b$ is $x_{ba}=x_b-x_a$

**Tensor field network**
$$
\mathcal{F}^\text{TFN}_{K(D),D} = \{f|f(\mathbf{X,H_\text{in}})=\sum^K_{k=1}f^{(k)}_{\text{pool}}*(f^{(k)}_{\text{feat}}(\mathbf{X,H_\text{in}})),f^{(k)}_{\text{pool}}\in \mathcal{F}^\text{TFN}_\text{pool}(D),\mathcal{f}_\text{feat}^{(k)}\in \mathcal{F}^\text{TFN}_\text{feat}(D)\}
$$
Where: $D\in \mathbb{N}$ denotes the function's maximum polynomial degree.

We define set $\mathcal{F}^\text{TFN}_\text{pool}$ as all rotationally equivariant linear functions on the $\text{SO}(3)$ group.

The embedding functions $\mathcal{F}^\text{TFN}_\text{feat}(D)=\{\pi_2 \circ f^{(2D)} \circ \cdots \circ f^{(1)}|f^{(i)}\in\mathcal{F}_\text{prod}^\text{TFN}\}$, each $f^{(i)}$ is one of the **tensor product layers** in the TFN and there is spherical harmonics and Clebsch–Gordan coefficients come in to mix spatial and feature information.$\pi_2(\mathbf{X},\mathbf{H})=\mathbf{H}$ , implies this function does nothing to geometry, just pass along features.

So, $\mathcal{F}_\text{prod}^\text{TFN}=\{f|f(\mathbf{X},\mathbf{H})=(\mathbf{X},\mathbf{\tilde{H}}^\text{TFN}(\mathbf{X},\mathbf{H})) \}$, It’s the set of feature update functions. The intermediate representations are $\mathbf{H}\in W^n_\text{feat}$， $W_\text{feat}$ is a representation of $\text{SO}(3)$ indexed by the degree l and the order m.
$$
\tilde{H}^{\text{TFN}(l_o)}_{a m_o} (X,H) = \theta H^{(l_o)}_{a m_o}+\sum_{l_f, m_f} \sum_{l_i, m_i} C^{(l_o, m_o)}_{(l_f, m_f), (l_i, m_i)} \sum_{b \in \mathcal{N}_a} F^{(l_f)}_{\text{TFN}, m_f}(x_b - x_a) \; H^{(l_i)}_{b m_i}
$$

- $C^{(l_o, m_o)}_{(l_f, m_f), (l_i, m_i)}$ is Clebsch-Gordan coefficients represents the tensor product of two input $\text{SO}(3)$ representations (the filter and input representations) into a sum of output representations.
- $\sum_{b\in\mathcal{N}_a}$ is looping over all neighbor atoms b of atom a.
- $F^{(l_f)}_{\text{TFN}, m_f}(x_b - x_a)$ a is rotationally equivariant **filter** applied to the vector from atom a to b.
- $H^{(l_i)}_{b m_i}$ Neighbor $b$’s feature of type $(l_i, m_i)$.

> [!NOTE]
>
> $F^{(l)}_{\text{TFN}, m}(x) = R^{(l)}(\|x\|) \; Y_{l m}(\hat{x})$ is a rotationally equivariant filter, with a (learned) radial part R, which is any polynomial of degree ≤D, and the real spherical
>
> harmonics $Y_{lm}$ with degree land order m.
>
> - $R^{(l)}$ = learned **radial function** of the bond length $\|x\|$
> - $Y_{l m}$ = **spherical harmonic** capturing the angular dependence

**Spherical networks**

 Instead of intermediate $\text{SO}(3)$ representations we now switch to spherical representations, which are functions on the sphere $H : S^2 →R$. We define the set of functions $\mathcal{F}^\text{sphere}_{ K(D),D}$  analogously to $\mathcal{F}^\text{TFN}_{ K(D),D}$. However, for $\mathcal{F}^\text{sphere}_\text{feat}(D)$ we use
$$
\tilde{\mathbf{H}}(\mathbf{X,H})(\hat{r})=\theta\mathbf{H}_a(\hat{r})+\sum_{b\in\mathcal{N}_a}F_\text{sphere}(x_b-x_a,\hat{r})\mathbf{H}_a(\hat{r})
$$

> [!NOTE]
>
> $F^{\text{sphere}}(x,\hat r) = \sum_{l,m} R^{(l)}(x)\;\Re\!\big[\,Y^{(l)}_m(\widehat{x})^{*}\;Y^{(l)}_m(\hat r)\,\big]$
>
> - $R^{(l)}(x)$: learned **radial** function of the distance $\|x\|$ (one per degree $l$).
> - $Y^{(l)}_m$: (complex) **spherical harmonics** (the angular basis on the sphere).
> - $\widehat{x}=x/\|x\|:$ the **direction** from $a$ to $b$.
> - $\Re[\cdot]$: take the real part → yields a real-valued filter.

The set of pooling functions for invariant predictions is:
$$
F^{\text{sphere}}_{\text{pool}}
=\Big\{\, f \ \big|\
f(\mathbf{H}) \;=\; \theta_{\text{pool}} \int_{\mathbb{S}^2} H(\hat r)\, d\hat r \;\Big\}.
$$

- $\theta_\text{pool}$ is a learnable parameter
