# DLM

## Corrupt Input

```markdown
# For a short response
Target response:
A B C D E

Training canvas:
A B C D E EOS EOS EOS

Canvas mask:
1 1 1 1 1 1 1 1

# For a longer response 
Canvas 1:
A B C D E F G H

Canvas 2:
I J K EOS EOS EOS EOS EOS
```





The full corruption schedule is:
$$
x_t = \begin{cases} x_0, & \text{with probability } \alpha(t),\\ z,\quad z\sim\pi, & \text{with probability } 1-\alpha(t). \end{cases}
$$
Gemma uses a rectified-flow-style schedule with
$$
\alpha(t)=1-t.
$$

- \(x_0\) is the clean target token.
- \(x_t\) is the corrupted token at diffusion time \(t\).
- \(t\) is the diffusion time, increasing from clean data toward noise.
- \(\alpha(t)\) is the probability of preserving the clean token.
- \(\pi\) is the invariant categorical noise distribution.
- \(z\) is a token sampled from \(\pi\).





### Uniform Sampling

$$
P(x_t \mid x_0)
=
\prod_{i=1}^{C}
\left[
(t-\epsilon)\delta(x_t^{(i)},x_0^{(i)})
+
(1-t+\epsilon)\frac{1}{V}
\right]
$$

### Dummy Mask

$$
P(x_t \mid x_0) = Mx_0
$$

**Notation:**
- $x_0$: original, uncorrupted input.
- $x_t$: corrupted input at diffusion time $t$.
- $C$: number of token positions or components.
- $V$: vocabulary size.
- $\epsilon$: small offset.
- $\delta$: indicator/Kronecker delta function.
- $M$: masking operator.

---

## 2. Entropy-Bounded Denoising

###  Probability Normalization

$$
p_{0,i} = \frac{L_i}{\sum_j L_j}
$$

where $L_i$ is a score for component $i$, and $p_{0,i}$ is its normalized value.

###  Average Entropy

$$
\bar e_\theta
=
\frac{1}{C}
\sum_{i=1}^{C}
-p_{0,i}\log P_{0,i}
$$

for all:

$$
i \in \{1,\ldots,C\}
$$

Here $\bar e_\theta$ denotes average entropy, $p_{0,i}$ and $P_{0,i}$ denote probabilities as written, and $\log$ is the logarithm.

###  Early Stopping

Stop the denoising process if:

$$
n>1
\;\land\;
\bar e\le e_{\mathrm{stop}}
\;\land\;
\hat X_{0\mid t}=\hat X_0^{\mathrm{prev}}
$$

$$
\Longrightarrow \boxed{\mathrm{STOP}}
$$

**Conditions:**
1. More than one iteration has occurred.
2. Average entropy falls below the stopping threshold.
3. The current prediction equals the previous prediction.

**Notation:**
- $n$: current iteration.
- $\bar e$: average entropy.
- $e_{\mathrm{stop}}$: entropy stopping threshold.
- $\hat X_{0\mid t}$: current estimate of the clean sequence.
- $\hat X_0^{\mathrm{prev}}$: previous estimate.
- $\land$: logical AND.

###  Entropy-Based Selection

For $n\le N$, sort the token entropies:

$$
e^{\pi_1}<e^{\pi_2}<\cdots<e^{\pi_C}
$$

> The handwritten text says "descending order," but the inequalities show ascending order.

Choose the largest valid $k$:

$$
k \leftarrow
\max\left\{
m\in\{1,\ldots,C\}:
\sum_{j=1}^{m-1}e^{\pi_j}\le b
\right\}
$$

**Notation:**
- $N$: total number of iterations.
- $\pi_j$: index of the token at sorted position $j$.
- $e^{\pi_j}$: entropy of that token.
- $m$: candidate number of selected tokens.
- $k$: selected token count.
- $b$: entropy budget.

###  Confidence-Based Token Selection

$$
\theta_i^e=
\begin{cases}
\tilde\theta_i^t, & i\in S\\
\tilde\theta_i, & i\notin S
\end{cases}
$$

- **$i\in S$:** sufficiently confident → ✓
- **$i\notin S$:** insufficiently confident → ✗ → re-denoise

Here $S$ is the selected set of positions, $i$ is a position index, and the $\theta$ terms denote the corresponding states (exact symbol interpretation is unclear).

###  Equivalent Entropy Constraint

$$
\sum_{j=1}^{k}H_{\pi(j)}
-
\max_{1\le j\le k}H_{\pi(j)}
\le\delta
$$

where:
- $H_{\pi(j)}$: entropy at sorted position $j$.
- $k$: number of selected positions.
- $\delta$: entropy tolerance for this constraint.
- $\max$: largest entropy among the selected positions.

---

## 3. Time-Dependent Entropy-Bounded Selection

###  Pure Entropy-Based Selection

Choose $k$ using:

$$
\sum_{j=1}^{m-1}e^{\pi_j}\le b
$$

**Problems:**
- Over-confidence.
- Time independence.
- Marked as undesirable (✗) in the original notes.

The entropy budget alone does not explicitly account for the current diffusion timestep.

###  Time-Step-Coupled Selection

Introduce a timestep-dependent selection constraint.

The handwritten expression appears to be:

$$
k_n \ge \frac{Cn}{N}
\ge C(1-\tau_{\mathrm{next}})
$$

**Notation:**
- $k_n$: number of selected tokens at iteration $n$.
- $C$: total number of tokens.
- $n$: current iteration.
- $N$: total number of iterations.
- $\tau_{\mathrm{next}}$: next diffusion timestep or noise level.

> The handwritten expression contains a crossed-out term near $k_n$; the exact intended inequality needs verification.

---

## 4. EOS and Canonical Ordering

**Questions:**
- EOS?
- Canonical order?

Proposed sequence representation:

$$
[A_1,A_2,\ldots,A_n,D,V]\in\mathcal C^{\,?}
$$

**Notation:**
- $A_1,\ldots,A_n$: ordered sequence elements.
- $D,V$: additional sequence elements whose meanings are not specified.
- $\mathcal C$: categorical/token space.
- The exponent on $\mathcal C$ is unclear.

**Open issue:** Determine whether a canonical ordering is required.

---

## 5. Sampling Strategy

###  Argmax Selection (Crossed Out)

The notes reject deterministic argmax prediction:

$$
x_0=\arg\max_{x_0}p_\theta(x_0\mid x_t)
$$

**Status:** ✗ Crossed out.

###  Categorical Sampling (Preferred)

Instead, sample each position from the model distribution:

$$
\boxed{
\tilde x_0^{(i)}
\sim
\operatorname{Categorical}
\left(
p_\theta(x_0^{(i)}\mid x_t)
\right)
}
$$

**Notation:**
- $\tilde x_0^{(i)}$: sampled clean token at position $i$.
- $p_\theta$: model-predicted conditional distribution.
- $\theta$: model parameters.
- $x_0^{(i)}$: clean token at position $i$.
- $x_t$: current noisy sequence.
- $\operatorname{Categorical}$: categorical probability distribution.
- $\sim$: "is sampled from."

**Main idea:** Use stochastic categorical sampling rather than always selecting the highest-probability token.

