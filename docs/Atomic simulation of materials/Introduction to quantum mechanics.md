# Introduction to Quantum Mechanics

## 1. Postulates of Quantum Mechanics

**Postulate No. 1.**

The wave functions can be represented by probability depends on the coordinates of the particle(s) $r$ and on time $t$.
$$
\int^{+\infty}_{-\infty}\Psi^\star(r,t)\Psi(r,t)d\tau = \int^{+\infty}_{-\infty}|\Psi(r,t)|^2 =1
$$

- $\tau$ is the volume element and $t$ is the precise instant of time.



**Postulate No. 2.**

To every observable in classical mechanics there corresponds a linear, Hermitian operator in quantum mechanics. If we require that the expectation value of an operator $\hat{A}$  is real, then  $\hat{A}$ must be a real operator. 

**Postulate No.3.**

In any measurement of the observable associated with operator $\hat{A}$, the only values that will ever be observed are the eigenvalues $a$:
$$
\hat{A}\Psi = a\Psi
$$


> [!NOTE]
>
> Although measurements must always yield an eigenvalue, the state does not have to be an eigenstate of $\hat{A}$ initially. An arbitrary state can be expanded in the complete set of eigenvectors of $\hat{A} \quad (\hat{A}\Psi=a\Psi )$

$$
\Psi = \sum_i^{n=\infty}c_i\Psi_i
$$



## 

**Postulate No.4.**

If a system is in a state described by a normalized wave-function $\Psi$, then the average value of the observable corresponding to $\hat{A}$ is:
$$
<A>= \int\Psi^\star\hat{A}\Psi d\tau
$$
**Postulate No.5.**

The wave-function or state function of a system evolves in time according to the time- dependent $\text{Schr\"odinger}$ equation as described
$$
\hat{H}\Psi(r,t) = i\bar{h}\frac{\partial \Psi(r,t)}{dt}
$$
**Postulate No.6.**

The total wave function must be antisymmetric with respect to the interchange of all coordinates of one electron (fermion) with those of another electron (fermion). The electronic spin must be included in this set of coordinates.

> [!NOTE]
>
> A **fermion** is a type of particle that follows the **Pauli exclusion principle** — meaning **no two identical fermions can occupy the same quantum state simultaneously**.



## 2. The $\textbf{Schr\"odinger}$ Equation For The Hydrogen-like Systems

Start form the $\text{Schr\"odinger}$ equation, the $\hat{H}\Psi = \hat{E}+\hat{V} = (-\frac{\bar{h^2}}{2m}\grad^2 + V)\Psi$

The potential $V$ experienced by two charges separated by some distance $r$ is best described by a Coulomb term
$$
V(r) = \frac{Ze^2}{4\pi \epsilon_0 r}
$$

- where $Ze$ is the charge of the nucleus, (Z = 1 being the hydrogen case, Z = 2 helium, etc.)
- $\epsilon_0$ is the permittivity of vacuum

### Separating The Radial From The Angular Part

The $\text{Schr\"odinger}$ equation in Cartesian coordinates is:
$$
\hat{H}\Psi=[-\frac{h^2}{2m}(\frac{\partial^2}{\partial^2 x}+\frac{\partial^2}{\partial^2y}+\frac{\partial^2}{\partial^2z})-\frac{Ze^2}{4\pi\epsilon_0r}]\Psi
$$
The potential part has spherical symmetry. One could write $r = x^2 + y^2 + z^2$ and solve Eq. 2 in Cartesian coordinates. This would work but it would be very tedious, as the mathematics does not display the **symmetry of the physics.** Accordingly, we rather exploit the spherical symmetry of the electrostatic potential and perform a coordinate transformation from Cartesian Coordinates (efficient for rectangle shapes) to Spherical Polar Coordinates (efficient for spherical shapes).

<img src="assets/image-20250929142957857.png" alt="image-20250929142957857" style="zoom:50%;" />
$$
(x,y,z) = (r, \theta, \phi)\\
x = r\sin\theta\cos\phi\\
y = r\sin\theta\sin\phi\\
z = r\cos\theta
$$

$$
\hat{H}\Psi =[-\frac{\bar{h}^2}{2m}(\frac{\partial^2}{\partial^2 r})]
$$

$$
\frac{\partial \Psi(x,y,z)}{\partial x}=\frac{\partial \Psi(r,\theta,\phi)}{\partial r\sin\theta\cos\phi}
$$

$$
\hat{H}\Psi = E\Psi = -\frac{\hbar^2}{2\mu}
\left[
\frac{1}{r^2}\frac{\partial}{\partial r}\left(r^2\frac{\partial}{\partial r}\right)
+\frac{1}{r^2\sin\theta}\frac{\partial}{\partial \theta}\left(\sin\theta\frac{\partial}{\partial \theta}\right)
+\frac{1}{r^2\sin^2\theta}\frac{\partial^2}{\partial \phi^2}
\right]\Psi
-\frac{Ze^2}{4\pi\epsilon_0 r}\Psi = E\Psi
$$

Since the potential part only depends on $r$, which is symmetric, Using the Separation of Variables, we assume a product solution of a radial and an angular function as in:
$$
\Psi(r,\theta, \phi) = R(r)\cdot Y(\theta,\phi)
$$
Since Y (spherical harmonics) is independent of $r$
$$
\frac{\partial \Psi}{\partial r} = Y \frac{\partial R(r)}{\partial r}
$$
and, similarly, since $R$ does not depend on the angular variables. Thus replace $\Psi$ and the differentials:
$$

$$
