# Boltzmann generators

## Context

For conventional statistical mechanics, it's try to compute the average behaviors of physical systems (ensembles). e.g. the probability of a protein to be folded under a certain temperature. To get this, we need to compute the statistics of the equilibrium stages of many body systems while enumerating all the equilibrium configurations is not possible, and also we can not directly sample them from the distribution, since the distribution is not feasible. 

The main approach is to start with one configuration, and apply tiny changes to it over time. e.g. using Markov-chain Mote Carlo or the molecular. Dynamics. How ever these simulations get trapped in metastable or long-lived stages. And high energy barrier takes a lot of times to jump.

**RATIONALE**

The Boltzmann generators try to directly provide unbiased, one shot samples from its equilibrium state.

<img src="/Users/harrison-li/Desktop/material-informatics-notes/docs/Computational Chemistry/assets/boltzmann generators.png" alt="image-20260826135550285" style="zoom:67%;" />



## Method

They used invertible networks with trainable parameters $\theta$ to learn the transformation between Gaussian random variables $\mathbf{z}$ and the Boltzmann-distributed random variables $\mathbf{x}$
$$
\mathbf{z} = F_{xz}(\mathbf{x};\theta)\\
\mathbf{x} = F_{zx}(\mathbf{z};\theta)
$$
Since the network is invertible, hence the $F_{xz}=F_{zx}^{-1}$, each transformation matrix has a Jacobian matrix with the pairwise first derivatives with respect to the input variables:
$$
\mathbf{J}_{zx}(\mathbf{z};\theta)=\left[\begin{array}{ccc}\dfrac{\partial F_{zx}(\mathbf{z};\theta)}{\partial z_1},&\ldots,&\dfrac{\partial F_{zx}(\mathbf{z};\theta)}{\partial z_n}\end{array}\right]\\
\mathbf{J}_{xz}(\mathbf{x};\theta)=\left[\begin{array}{ccc}\dfrac{\partial F_{xz}(\mathbf{x};\theta)}{\partial x_1},&\ldots,&\dfrac{\partial F_{xz}(\mathbf{x};\theta)}{\partial x_n}\end{array}\right]
$$
And the absolute value of the Jacobian's determinant, $|\text{det}\mathbf{J}_{zx}(\mathbf{z})|$, measures how much a volume element at $z$ is scaled by the transformation (the scaler between $z$ and $x$), represented by $R$
$$
R_{xz}(\mathbf{x})=|\text{det}\mathbf{J}_{xz}(\mathbf{x})|\\
R_{zx}(\mathbf{z})=|\text{det}\mathbf{J}_{zx}(\mathbf{z})|
$$
For the **conservation of probability**:
$$
p_X(\mathbf{x})dx =p_Z(\mathbf{z})d_z\\
p_X(\mathbf{x})=p_Z(\mathbf{z})\frac{d_z}{dx} = p_Z(\mathbf{z})R_{xz}(x)
$$
Hence the invertible transformations could be:

****

$$
p_X(\mathbf{x})=p_Z(\mathbf{z})R_{zx}(\mathbf{z})^{-1}=p_Z(F_{xz}(\mathbf{x}))R_{xz}(\mathbf{z})\\
p_Z(\mathbf{z})=p_X(\mathbf{x})R_{xz}(\mathbf{x})^{-1}=p_X(F_{zx}(\mathbf{z}))R_{zx}(\mathbf{x})
$$

$$
[ \mathbb E_{a\sim p}[k_3(\log q-\log p)] = KL(p\Vert q) ]
$$





### How to sample from Boltzmann distribution

Denote $\mu$ as the exact distributions and $q$ the generated distribution, $\mu(\mathbf{z})$ is the Gaussian prior distribution  form which we directly sample latent space variables, and $q_x(\mathbf{x)}$ is the distribution from network transformation $F_{zx}$.

$\mu_X(\mathbf{x})\propto\exp{(-\mu(\mathbf{x}))}$ is the Boltzmann distribution in configurational space. And $q_Z(\mathbf{z})$ is the distribution form network transformation:
$$
\begin{aligned}
\mu_Z(\mathbf{z})\overset{F_{zx}}\longrightarrow q_X(\mathbf{x})\\
\mu_X(\mathbf{x})\overset{F_{xz}}\longrightarrow q_Z(\mathbf{z})
\end{aligned}
$$
The standard Boltzmann distribution in Canonical ensemble:
$$
\mu_X(\mathbf{x})=Z_X^{-1}e^{-\beta U(\mathbf{x})}\Rightarrow \mu(\mathbf{x})=\frac{U(x)}{k_B T}
$$
To work with multi-temperature conditions: $(T_1,T_2,...,T_K)$, we define a reference temperature $T_0$, and reduced energy $\mu^0(\mathbf{x})=U(\mathbf{x})/k_BT_0$
$$
\mu^k(\mathbf{x})=\frac{T_0}{T_k}\mu^0(\mathbf{x})=\frac{\mu_0(\mathbf{x})}{\tau_k}, \quad \tau_k = \frac{T_k}{T_0}
$$
