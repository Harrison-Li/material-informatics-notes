# MACE

## Recall MPNN Interatomic Potentials

When applied to parameterize properties of atomistic structures (materials or molecules), the graph is embedded in 3-dimensional (3D) Euclidean space, where each node represents an atom, and edges connect nodes if the corresponding atoms are within a given distance of each other. We represent the state of each node $i$ in layer $t$ of the MPNN by a tuple.
$$
\sigma_i^{(t)}=(r_i,z_i,h_i^{(t)})
$$
Where $r\in \mathbb{R}^3$ is the position of the atom $i$, $z_i$ is the chemical element, and $h^{(t)}$ are its learnable features.

A forward pass of the network consists of multiple message **construction, update**, and **readout** steps.

During message construction, a message $m^{(t)}_i$ is created for each node by pooling over its neighbors:
$$
m_i^{(t)}=\bigoplus_{j\in\mathcal{N}(i)}M_t(\sigma^{(t)},\sigma^{(j)})
$$
where $M_t$ is a learnable message function and $\bigoplus_{j\in\mathcal{N}(i)}$ is a learnable, permutation invariant pooling operation over the neighbors of atom $i$ (e.g., a sum).

In the **update** step, the message $m_i^{(t)}$ is transformed into new features
$$
h^{(t+1)}_i= U_t(\sigma^{(t)}_i,m_i^{(t)})
$$
where $U_t$ is a learnable update function, After $T$ message construction and update steps, the learnable readout functions $R_t$ map the node states $σ^{(t)}_i$ to the target, in this case the site energy of atom $i$.
$$
E_i = \sum^T_{t=1}\mathcal{R}_t(\sigma_i^{(t)})
$$

## The MACE Architecture