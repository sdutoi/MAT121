## 1) Intuitive idea of limits

- We say $\lim_{x\to a} f(x) = L$ if we can make $f(x)$ as close as we like to $L$ by taking $x$ sufficiently close to $a$ (but not necessarily equal to $a$).
- The limit is about the behavior near $a$, not at $a$ itself.

Quick pictures in words:
- Removable “hole”: $f(x)=\frac{x^2-1}{x-1}=x+1$ for $x\ne 1$, undefined at $x=1$. The values near $1$ are near $2$, so $\lim_{x\to 1} f(x)=2$ even though $f(1)$ is undefined.
- Jump: $f(x)=\begin{cases}0,&x<0\\1,&x\ge 0\end{cases}$ has different left and right behaviors at $0$, so the two-sided limit doesn’t exist.

Status: intuition laid. Next I’ll formalize with $\varepsilon$–$\delta$.

## 2) Formal $\varepsilon$–$\delta$ definition

We say $\lim_{x\to a} f(x)=L$ if:
- For every $\varepsilon>0$ there exists $\delta>0$ such that for all $x$,
  $$
  0<|x-a|<\delta \implies |f(x)-L|<\varepsilon.
  $$

Notes:
- The condition $0<|x-a|$ excludes $x=a$ itself.
- “For every $\varepsilon$” means we can hit any target accuracy on $f(x)$ by taking $x$ close enough to $a$.

Status: definition stated. Next: the sequences viewpoint.

## 3) Sequence (Heine) definition

$\lim_{x\to a} f(x)=L$ if and only if for every sequence $(x_n)$ with $x_n\ne a$ and $x_n\to a$, we have $f(x_n)\to L$.

This is often easier to use in proofs by contradiction: if two sequences approach $a$ but give different limit values of $f(x_n)$, then the limit at $a$ doesn’t exist.

Status: added the equivalent characterization. Next: types and laws of limits.

## 4) Types of limits and limit laws

- One-sided limits:
  - $\lim_{x\to a^-} f(x)$: $x$ approaches $a$ from the left.
  - $\lim_{x\to a^+} f(x)$: $x$ approaches $a$ from the right.
  - Two-sided $\lim_{x\to a} f(x)$ exists iff both one-sided limits exist and are equal.

- Infinite limits (vertical asymptotes): $\lim_{x\to a} f(x)=\infty$ means values grow beyond any bound near $a$.

- Limits at infinity (end behavior): $\lim_{x\to\infty} f(x)=L$ means $f(x)$ gets arbitrarily close to $L$ as $x$ grows.

- Algebra of limits (when limits exist):
  - $\lim(f\pm g) = \lim f \pm \lim g$
  - $\lim(fg) = (\lim f)(\lim g)$
  - $\lim(f/g) = (\lim f)/(\lim g)$ if $\lim g\ne 0$
  - Composition: if $\lim_{x\to a} f(x)=b$ and $g$ is continuous at $b$, then $\lim_{x\to a} g(f(x)) = g(b)$.

Status: laws noted. Next: diverse worked examples.

## 5) Worked examples

### A. Removable discontinuity and algebraic simplification
Compute $\displaystyle \lim_{x\to 1}\frac{x^2-1}{x-1}$.

Factor:
$$
\frac{x^2-1}{x-1}=\frac{(x-1)(x+1)}{x-1}=x+1 \quad (x\ne 1).
$$
So the limit is $\lim_{x\to 1}(x+1)=2$.

Key idea: simplify to a function continuous at the point, then substitute.

---

### B. Squeeze (Sandwich) Theorem
Compute $\displaystyle \lim_{x\to 0} x\sin\!\left(\tfrac{1}{x}\right)$.

We know $-1\le \sin(\cdot)\le 1$, hence
$$
-|x| \le x\sin\!\left(\tfrac{1}{x}\right)\le |x|.
$$
As $x\to 0$, both bounds go to $0$, so by Squeeze:
$$
\lim_{x\to 0} x\sin\!\left(\tfrac{1}{x}\right)=0.
$$

Contrast: $\lim_{x\to 0} \sin(1/x)$ does not exist (oscillation without damping).

---

### C. No limit due to oscillation
Show $\displaystyle \lim_{x\to 0}\sin\!\left(\tfrac{1}{x}\right)$ does not exist.

Pick sequences approaching $0$:
- $x_n=\frac{1}{\pi/2 + 2\pi n} \to 0$ gives $\sin(1/x_n)=1$.
- $y_n=\frac{1}{3\pi/2 + 2\pi n} \to 0$ gives $\sin(1/y_n)=-1$.

Two different subsequential limits imply the limit does not exist (Heine).

---

### D. Rational functions at infinity
Compute $\displaystyle \lim_{x\to\infty} \frac{3x^2-5x+7}{2x^2+10}$.

Divide numerator and denominator by $x^2$:
$$
\frac{3-5/x+7/x^2}{2+10/x^2}\to \frac{3}{2}.
$$

Rule of thumb:
- Degrees equal: limit is ratio of leading coefficients.
- Degree numerator < denominator: limit is $0$.
- Degree numerator > denominator: limit is $\pm\infty$ (or does not exist if signs vary).

---

### E. One-sided limits and jump discontinuity
Let $f(x)=\begin{cases} x^2,& x<1\\ 2x-1,& x\ge 1.\end{cases}$

- $\lim_{x\to 1^-} f(x) = 1^2 = 1$,
- $\lim_{x\to 1^+} f(x) = 2\cdot 1 - 1 = 1$,
- Hence $\lim_{x\to 1} f(x)=1$ and $f$ is continuous at $1$ (here the pieces meet).

If instead the second piece were $2x$ for $x\ge 1$, then right limit would be $2$, and the two-sided limit would not exist.

---

### F. Composition and continuity
Compute $\displaystyle \lim_{x\to 0} \sqrt{1+3x}$.

Inside limit: $1+3x\to 1$. Since $\sqrt{\cdot}$ is continuous at $1$,
$$
\lim_{x\to 0} \sqrt{1+3x} = \sqrt{1}=1.
$$

---

### G. Using inequalities with $\ln$
Show $\displaystyle \lim_{x\to 0} \frac{\ln(1+x)}{x}=1$.

For $-1<x\ne 0$, standard bounds give
$$
\frac{x}{1+x} \le \ln(1+x) \le x.
$$
Divide by $x$ (consider signs appropriately) and squeeze to $1$.

This is foundational for derivatives of $\ln$ and appearances of $e$.

---

### H. Indeterminate forms and L’Hôpital’s Rule (brief)
Compute $\displaystyle \lim_{x\to 0} \frac{\sin x}{x}$.

Without calculus: squeeze using $\sin x \le x \le \tan x$ for $x>0$ to get $1$.
With L’Hôpital (if derivatives available): derivative top/bottom at $0$ gives $\cos 0 / 1 = 1$.

---

### I. Removable discontinuity via definition of continuity
Let $f(x)=\begin{cases} \frac{\sin x}{x}, & x\ne 0\\ c, & x=0\end{cases}$.
Then $f$ is continuous at $0$ iff $c=\lim_{x\to 0}\frac{\sin x}{x}=1$.

Status: examples provided across techniques. Last: tie to continuity and pitfalls.

## 6) Continuity, pitfalls, and quick checks

- Continuity at $a$ means $\lim_{x\to a} f(x)=f(a)$; it packages limit existence with matching function value.
- Common pitfalls:
  - Evaluating at the point instead of analyzing nearby behavior.
  - Cancelling factors only valid when not zero—okay for limits if you reason about $x\ne a$ before taking the limit.
  - Assuming two-sided limit exists when one-sided limits differ.
  - Ignoring growth rates at infinity; compare degrees or use dominant term analysis.
- Advanced tools:
  - L’Hôpital’s Rule for $0/0$ or $\infty/\infty$ forms.
  - Series expansions for precise asymptotics.
  - Squeeze Theorem for oscillatory or bounded-by-simple-functions cases.

---

Completed (1/7) *Intuitive idea of limits*

Great question. The short answer: divide numerator and denominator by the highest power of $x$ that appears in the denominator (or by the common dominant power if both have the same degree). This normalizes the expression and makes the end behavior transparent.

Here’s the general playbook for rational limits at infinity.

## General idea

Given
$$
\lim_{x\to\infty} \frac{P(x)}{Q(x)},
$$
where $P,Q$ are polynomials with degrees $\deg P = m$ and $\deg Q = n$:

1) Identify the dominant powers:
- The leading terms are $a_m x^m$ in $P$ and $b_n x^n$ in $Q$.

2) Divide numerator and denominator by $x^n$ (the highest power in the denominator). This gives:
$$
\frac{P(x)}{Q(x)} = \frac{\dfrac{P(x)}{x^n}}{\dfrac{Q(x)}{x^n}}.
$$
Now each term in $P(x)/x^n$ looks like $c_k x^{k-n}$, which goes to $0$ if $k<n$, stays constant if $k=n$, and blows up if $k>n$.

3) Read off the limit:
- If $m<n$ (degree numerator < degree denominator), all terms in the numerator go to $0$ while the denominator tends to the constant $b_n$, so the limit is $0$.
- If $m=n$, the lower-degree terms vanish and you get the ratio of leading coefficients:
  $$
  \lim_{x\to\infty} \frac{P(x)}{Q(x)}=\frac{a_m}{b_n}.
  $$
- If $m>n$, the numerator’s leading term dominates and the quotient grows without bound (to $\pm\infty$, depending on signs), so the finite limit does not exist.

This procedure is why in example 5 D) we divided by $x^2$: the denominator’s highest power was $x^2$. Because the numerator had the same degree, the limit becomes the ratio of leading coefficients.

## Worked micro-examples

- Degree numerator < denominator:
  $$
  \lim_{x\to\infty}\frac{5x+1}{2x^2+3} =
  \lim_{x\to\infty}\frac{\frac{5}{x}+ \frac{1}{x^2}}{2+\frac{3}{x^2}} = 0.
  $$

- Equal degrees:
  $$
  \lim_{x\to\infty}\frac{3x^2-5x+7}{2x^2+10} =
  \lim_{x\to\infty}\frac{3-\frac{5}{x}+\frac{7}{x^2}}{2+\frac{10}{x^2}} = \frac{3}{2}.
  $$

- Degree numerator > denominator:
  $$
  \lim_{x\to\infty}\frac{x^3-4}{7x^2+1}
  = \lim_{x\to\infty}\frac{x\left(x^2 - \frac{4}{x}\right)}{7x^2+1}
  \sim \lim_{x\to\infty}\frac{x^3}{7x^2} = \lim_{x\to\infty}\frac{x}{7} = \infty.
  $$

Equivalent move: divide by $x^2$ to see
$$
\frac{x^3-4}{7x^2+1} = \frac{x - \frac{4}{x^2}}{7 + \frac{1}{x^2}} \to \infty.
$$

## Why this works

Dividing by $x^n$ re-expresses everything in terms of powers $x^{k-n}$. As $x\to\infty$:
- negative exponents vanish,
- zero exponent terms stay as constants,
- positive exponents dominate.

This mirrors the intuitive fact that at large $x$, only the highest-degree terms matter.


Yes. When the numerator and denominator are polynomials of the same degree, you can read the limit at $\infty$ (and at $-\infty$) directly as the ratio of the leading coefficients—no need to explicitly divide by $x^2$.

For 5 D),
$$
\lim_{x\to\infty}\frac{3x^2-5x+7}{2x^2+10}=\frac{3}{2},
$$
because both polynomials have degree $2$ and their leading coefficients are $3$ and $2$.

Why this is valid (quick justification):
- Write
  $$
  P(x)=a_d x^d + r(x),\quad Q(x)=b_d x^d + s(x),
  $$
  where $r(x)=o(x^d)$ and $s(x)=o(x^d)$ as $x\to\infty$. Then
  $$
  \frac{P(x)}{Q(x)}
  = \frac{a_d x^d\big(1+\frac{r(x)}{a_d x^d}\big)}{b_d x^d\big(1+\frac{s(x)}{b_d x^d}\big)}
  = \frac{a_d}{b_d}\cdot \frac{1+o(1)}{1+o(1)} \xrightarrow[x\to\infty]{} \frac{a_d}{b_d}.
  $$
- Dividing by $x^d$ is just a standard way to make that “$o(1)$” behavior explicit; once you know the theorem, you can go straight to the ratio.

Summary rule for rational functions $\dfrac{P}{Q}$ with polynomials $P,Q$:
- $\deg P<\deg Q \implies \lim_{x\to\infty}\dfrac{P}{Q}=0$.
- $\deg P=\deg Q \implies \lim_{x\to\infty}\dfrac{P}{Q}=\dfrac{\text{leading coeff of }P}{\text{leading coeff of }Q}$.
- $\deg P>\deg Q \implies \dfrac{P}{Q}$ diverges in magnitude as $x\to\infty$ (sign determined by leading coefficients).

Note: This “leading-coefficient rule” is specific to polynomials in numerator and denominator. If radicals, exponentials, or logs are involved, use dominant growth comparisons or other tools (e.g., divide by the dominant term, asymptotics, or L’Hôpital where appropriate).