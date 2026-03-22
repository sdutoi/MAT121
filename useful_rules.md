## Linear-power integration rule

For any constants \(a\neq 0\), \(b\), and exponent \(n\):

- If \(n\neq -1\),
\[
\int (ax+b)^{n}\,dx \;=\; \frac{(ax+b)^{\,n+1}}{a(n+1)} \;+\; C.
\]
- If \(n=-1\),
\[
\int (ax+b)^{-1}\,dx \;=\; \frac{1}{a}\,\ln|ax+b| \;+\; C.
\]

### Why (quick derivation)
Let \(u=ax+b\). Then \(du=a\,dx\) and \(dx=\frac{1}{a}\,du\). Hence, for \(n\neq -1\),
\[
\int (ax+b)^n\,dx
= \int u^n \,\frac{1}{a}\,du
= \frac{1}{a}\cdot \frac{u^{n+1}}{n+1}+C
= \frac{(ax+b)^{n+1}}{a(n+1)}+C,
\]
and for \(n=-1\),
\[
\int (ax+b)^{-1}\,dx
= \frac{1}{a}\int \frac{1}{u}\,du
= \frac{1}{a}\ln|u|+C
= \frac{1}{a}\ln|ax+b|+C.
\]

### Definite integrals
Either apply the antiderivative directly:
\[
\int_{\alpha}^{\beta} (ax+b)^{n}\,dx
= \left[\frac{(ax+b)^{n+1}}{a(n+1)}\right]_{\alpha}^{\beta}
\quad (n\neq -1),
\]
or change variables and limits:
\[
\int_{\alpha}^{\beta} (ax+b)^{n}\,dx
= \frac{1}{a}\int_{a\alpha+b}^{a\beta+b} u^{n}\,du.
\]

### Example (#17)
\[
\int_{0}^{3} (2x-5)^{3}\,dx
= \left[\frac{(2x-5)^{4}}{2\cdot 4}\right]_{0}^{3}
= \frac{1^{4}}{8}-\frac{(-5)^{4}}{8}
= -\frac{624}{8}
= -78.
\]


---

Here’s the quick guide you want.

## Even vs. odd (how to tell)

Definition test:
- Even: \(f(-x)=f(x)\) for all \(x\).
- Odd: \(f(-x)=-f(x)\) for all \(x\).

Practical checks (especially for polynomials):
- If the polynomial has only even powers of \(x\) (and possibly a constant term), it’s even.
- If it has only odd powers of \(x\) and no constant term, it’s odd.
- Mixed even and odd powers → neither.

Useful rules:
- Product: even·even = even; odd·odd = even; even·odd = odd.
- Composition: if \(g\) is even, then \(h(g(x))\) is even (because \(g(-x)=g(x)\) so the input to \(h\) is unchanged).

Applied to #18:
\[
f(x)=(x^2-3)^3.
\]
Since \(x^2-3\) is even, \((x^2-3)^3\) is also even:
\[
f(-x)=((-x)^2-3)^3=(x^2-3)^3=f(x).
\]
Equivalently, expanding gives only even powers: \(x^6-9x^4+27x^2-27\).

Therefore on symmetric limits \([-a,a]\):
\[
\int_{-a}^{a} f(x)\,dx=
\begin{cases}
0, & f \text{ odd},\\[4pt]
2\displaystyle\int_{0}^{a} f(x)\,dx, & f \text{ even}.
\end{cases}
\]

## Why we didn’t use the “linear-power” rule here

The shortcut
\[
\int (ax+b)^n\,dx=\frac{(ax+b)^{n+1}}{a(n+1)}+C
\]
comes from the substitution \(u=ax+b\) (linear inside), where \(du=a\,dx\) is a constant multiple of \(dx\).

In #18 the inside is quadratic, \(x^2-3\), not linear. If we set \(u=x^2-3\), then \(du=2x\,dx\), which introduces an \(x\) factor that we don’t have in the integrand. So the direct chain-rule shortcut doesn’t apply.

Two natural options instead:
- Use even symmetry: \(\int_{-3}^{3}(x^2-3)^3\,dx=2\int_{0}^{3}(x^2-3)^3\,dx\).
- Expand and integrate term-by-term (which is what we did).

Note: If the integrand had an \(x\) factor, e.g.
\[
\int (x^2-3)^3\,(2x)\,dx,
\]
then the substitution \(u=x^2-3\) would work perfectly:
\[
\int u^3\,du=\frac{u^4}{4}+C=\frac{(x^2-3)^4}{4}+C.
\]


---

Yes — they are the same. Here’s why:

---

### Step 1: Factor the negative

$$
(5 - x) = -(x - 5).
$$

---

### Step 2: Raise to the 4th power

$$
(5 - x)^4 = [-(x - 5)]^4.
$$

---

### Step 3: Simplify

When you raise a negative to an **even power**, the negative sign disappears:

$$
[-(x - 5)]^4 = (-1)^4 (x - 5)^4 = 1 \cdot (x - 5)^4.
$$

---

### Final result

$$
(5 - x)^4 = (x - 5)^4.
$$

---

✅ In short: They are equal because raising to the 4th power (an even power) makes the minus sign vanish.
If instead the exponent were **odd** (say $(x-5)^3$ vs $(5-x)^3$), they would be negatives of each other.

Do you want me to also show you how this relates to the **general rule** $(a-b)^n = (-1)^n (b-a)^n$?

