# Different types of distance



## Wasserstein distance

For two probability distributions $u$ and $v$ on a metric space $M$, the $p$-th Wasserstein distance is defined as:
$$
W_p(u,v) = (\underset{\gamma(x,y)\in \Gamma(u,v)}{\text{inf}}\int_{M\times M}d(x,y)^pd\gamma(x,y))^{1/p}
$$

- $\Gamma(u,v)$: The set of all possible "transport plans" (joint distributions) whose marginals are $u$ and $v$.
- $d(x,y)$: The distance between point $x$ in $u$ and point $y$ in $v$.
- $\gamma(x,y)$: The amount of "mass" moved from $x$ to $y$.

e.g. **1st Wasserstein distance** the integral of the difference between the cumulative distribution functions (CDFs) in the 1D case:
$$
W_1(P,Q) = \int_{-\infty}^\infty |F_P(x))-F_Q(x)|dx
$$
