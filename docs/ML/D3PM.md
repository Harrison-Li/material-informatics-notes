# Discrete Denoising Diffusion Probabilistic Models

## Background

### Diffusion models

In order to optimize the generative model $p_\theta(x_0)$ to fit the data distribution $q(x_0)$, we typically optimize a variational upper bound on the negative log-likelihood:
$$
L_{vb} =\mathbb{E}_q \left[
\underbrace{D_{\mathrm{KL}}\left(q(\mathbf{x}_T|\mathbf{x}_0) \,\|\, p(\mathbf{x}_T)\right)}_{L_T}
+ \sum_{t > 1}
\underbrace{D_{\mathrm{KL}}\left(q(\mathbf{x}_{t-1}|\mathbf{x}_t, \mathbf{x}_0) \,\|\, p_\theta(\mathbf{x}_{t-1}|\mathbf{x}_t)\right)}_{L_{t-1}}
- \underbrace{\log p_\theta(\mathbf{x}_0|\mathbf{x}_1)}_{L_0}
\right]
$$


We would like minimize the negative log-likelihood $-\log{p_\theta(x_0)}$,  which is equivalent the average over the dataset $E_{q(x_0)}[-\log p_\theta(x_0)]$, But $p_\theta(x_0)$ is difficult to evaluate because the diffusion model contains latent variables: $x_1,x_2,\ldots,x_T.$
$$
p_\theta(x_0)=\int p_\theta(x_{0:T})\,dx_{1:T}.
$$
We can rewrite the $p_\theta(x_0)$ to:
$$
p_\theta(x_0)=\int q(x_{1:T}\mid x_0) \frac{ p_\theta(x_{0:T}) }{ q(x_{1:T}\mid x_0) } \,dx_{1:T}.\\
p_\theta(x_0)=\mathbb E_{q(x_{1:T}\mid x_0)}\left[\frac{p_\theta(x_{0:T})}{q(x_{1:T}\mid x_0)}\right].
$$
Then we can take <u>Jensen’s inequality</u>, since logarithm function is concave. $\log{Z}\leq Z$
$$
-\log p_\theta(x_0)\leq\mathbb E_q\left[\log\frac{q(x_{1:T}\mid x_0)}{p_\theta(x_{0:T})}\right].
$$
This right-hand side is the **variational upper bound** on the negative log-likelihood.

Then we can define the loss function, trying to minimize the variational upper bound:
$$
\boxed{
L_{\mathrm{vb}}
=
\mathbb E_{q(x_0)}
\mathbb E_{q(x_{1:T}\mid x_0)}
\left[
\log
\frac{
q(x_{1:T}\mid x_0)
}{
p_\theta(x_{0:T})
}
\right]
}
$$

## Diffusion models for discrete state spaces

For scalar discrete random variables with $K$ categories $x_t, x_{t-1}\in 1,\ldots, K$, then the forward transition probabilities should be $[Q_t]_{ij}=q(x_t=i|x_{t-1}=j)$, Denoting the one-hot version of $x$ with the row vector $x$, we can write
$$
q(\mathbf{x}_t|\mathbf{x}_{t-1}) = \text{Cat}(\mathbf{x}_t;\mathbf{p}=\mathbf{x}_{t-1}Q_t)
$$

- $\text{Cat}(\mathbf{x}; \mathbf{p})$ is a categorical distribution over the one-hot row vector $x$ with probabilities given by the row vector $p$
- $x_{t-1}Q_t$ is to be understood as a row vector-matrix product, $Q_t$ is applied to each pixel of an image or each token in a sequence independently.



So, we thus write $q(x_t|x_{t−1})$ in terms of a single element. Starting from $x_0$, we obtain the following $t$-step marginal and posterior at time $t−1$:
$$
q(x_t|x_0) = \text{Cat}(x_t; p=x_0\bar{Q_t}), \quad \text{with } \bar{Q_t} = Q_1Q_2\ldots Q_t
$$

$$
q(x_{t-1}|x_t,x_0) =  \frac{q(x_t|x_{t-1},x_0)q(x_{t-1}|x_0)}{q(x_t|x_0)} = \text{Cat}(x_{t-1};p = \frac{x_tQ_t^T\odot x_0\bar{Q}_{t-1}}{x_0\bar{Q}_{t}x_t^T})
$$

### Choice of Markov transition matrices for the forward process

The only constraints for the transition matrices $Q_t$ is that the product of $\bar{Q}_t$ should reach stationary (limiting distribution) when t becomes large.



**Uniform **
$$
Q_t=(1-\beta_t)\mathbf{I} + \beta_t/K, \quad \beta_t\in [0,1]
$$