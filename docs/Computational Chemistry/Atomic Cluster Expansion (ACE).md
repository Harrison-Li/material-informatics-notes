# Atomic Cluster Expansion (ACE)

**Background**

The energy of a system can be assumed  that  the total energy E of the system as a sum of atomic contributions $E_i$
$$
E =	\sum_iE_i
$$
So, it's straightforward to write down the energy of a collection of atoms $i= 1, . . . , N$ in a many-atom expansion:
$$
\begin{aligned}
E =\;& V_0
+ \sum_i V^{(1)}(r_i)
+ \frac{1}{2}\sum_{ij} V^{(2)}(r_i, r_j) \\
&+ \frac{1}{3!}\sum_{ijk} V^{(3)}(r_i, r_j, r_k) \\
&+ \frac{1}{4!}\sum_{ijkl} V^{(4)}(r_i, r_j, r_k, r_l)
+ \cdots
\end{aligned}
$$
$r_i$ is the position of atom $i$ and the potential $V^{(2)}, V^{(3)},...$ are symmetric, uniquely defined, and zero if two or more indices take identical values.

Commonly, $V_0$ is a constant offset that can be set to zero and $V^{(1)}$ is the chemical potential