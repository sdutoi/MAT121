
## 1. Spotting the “gap” from the suspected limit

For the sequence \(x_n = \dfrac{n}{n+1}\), the numerator and denominator have the same degree (both linear in \(n\)). A standard heuristic:

- If \(\displaystyle x_n = \frac{a n + b}{c n + d}\) with \(c\neq 0\), then \(\lim x_n = a/c\) (ratio of leading coefficients).
- After guessing \(L = a/c\), explicitly compute the gap \(x_n - L\). If that gap \(\to 0\), limit confirmed.

For \(x_n = n/(n+1)\) we guess \(L=1\) (since coefficients \(a=c=1\)). Then:
\[
x_n - 1 = \frac{n}{n+1} - 1 = \frac{n - (n+1)}{n+1} = -\frac{1}{n+1}.
\]
So
\[
|x_n - 1| = \frac{1}{n+1} \longrightarrow 0.
\]
That’s the “intuitive idea” turned rigorous: we rewrote the fraction to isolate a tiny term.

---

## 2. General template for rational sequences of degree 1

Let
\[
x_n = \frac{a n + b}{c n + d}, \quad c\neq 0.
\]
Guess \(L = a/c\). Then
\[
x_n - \frac{a}{c} = \frac{a n + b}{c n + d} - \frac{a}{c}
= \frac{c(a n + b) - a(c n + d)}{c(c n + d)}
= \frac{acn + bc - acn - ad}{c(c n + d)}
= \frac{bc - ad}{c(c n + d)}.
\]
Magnitude:
\[
|x_n - L| = \frac{|bc - ad|}{|c|\,|c n + d|} \le \frac{|bc - ad|}{|c|^2 n - |c d|} \sim \frac{C}{n} \to 0.
\]
Thus \(x_n \to a/c\).

Exactly the same pattern—compute the algebraic difference.

---

## 3. Higher-degree rational sequences

If
\[
x_n = \frac{P(n)}{Q(n)},\quad P,Q\text{ polynomials},
\]
let \(m=\deg P\), \(k=\deg Q\).

- If \(m<k\): \(\lim x_n = 0\).
- If \(m=k\): \(\lim x_n = \) ratio of leading coefficients.
- If \(m>k\): \(|x_n|\to \infty\) (diverges in magnitude).

Proof mechanism: divide numerator & denominator by \(n^k\) (highest degree in the denominator) and let lower-order terms vanish. For example,
\[
\frac{3n^2+5}{2n^2 - n + 7} = \frac{3 + 5/n^2}{2 - 1/n + 7/n^2} \longrightarrow \frac{3}{2}.
\]

If you want an explicit “gap,” after finding \(L\) compute \(x_n - L\) and simplify; it’ll collapse to something like \(C/n\) or \(C/n^p\).

---

## 4. Rewrite tricks to expose a small term

Common goal: express the sequence as “limit candidate \(\pm\) something that \(\to 0\).”

Patterns:

1. “Almost 1”:
   \[
   \frac{n}{n+1} = 1 - \frac{1}{n+1},\qquad
   \frac{n+a}{n+b} = 1 + \frac{a-b}{n+b}.
   \]

2. “Almost constant \(L\)”:
   \[
   \frac{an+b}{cn+d} = \frac{a}{c} + \frac{bc-ad}{c(cn+d)}.
   \]

3. Powers near 1:
   \[
   \left(\frac{n}{n+1}\right)^p = \left(1 - \frac{1}{n+1}\right)^p
   \quad\text{and}\quad
   \Big| \left(1 - \frac{1}{n+1}\right)^p - 1\Big| \le p\frac{1}{n+1}
   \]
   (using Bernoulli inequality or binomial expansion) so still \(\to 0\).

4. Exponential type:
   \[
   \left(1 + \frac{1}{n}\right)^n \to e,
   \quad
   \left(1 + \frac{k}{n}\right)^n \to e^{k}.
   \]

5. Sequences with sine:
   \[
   \frac{\sin n}{\sqrt{n}} \to 0
   \quad \text{since } |\sin n| \le 1 \text{ and } \frac{1}{\sqrt{n}} \to 0.
   \]

---

## 5. Epsilon–proof pattern (after you have the gap)

Steps always look the same:

1. Guess \(L\).
2. Compute \( |x_n - L| \) exactly.
3. Simplify to a known “small” prototype (e.g. \(1/n\), \(1/n^2\), \(C/(n+1)\)).
4. Invoke Archimedean property: for \(\varepsilon>0\) choose \(N\) with that prototype \(<\varepsilon\) for \(n\ge N\).
5. Conclude by the definition.

Example for \((n+a)/(n+b)\):

\[
\left|\frac{n+a}{n+b} - 1\right| = \left|\frac{a-b}{n+b}\right| \le \frac{|a-b|}{n - |b|}\quad(\text{eventually}).
\]

Given \(\varepsilon\), pick \(N > \max\{|b|, |a-b|/\varepsilon\}\), then for \(n\ge N\),
\[
|x_n - 1| \le \frac{|a-b|}{n - |b|} < \varepsilon.
\]

---

## 6. Big‑O language (helpful shorthand)

Once you’re comfortable, you can compress the reasoning:

\[
\frac{n}{n+1} = 1 - \frac{1}{n+1} = 1 + O\!\left(\frac{1}{n}\right),
\]
meaning \(x_n - 1\) is on the order of \(1/n\), hence tends to \(0\). For rigorous write‑ups you expand that “\(O\)” into the epsilon argument.

---

## 7. Decision tree for typical sequence limits

1. Is it obviously bounded and monotone? Then maybe use Monotone Convergence.
2. Is it rational in \(n\)? Use degrees & leading coefficients; compute gap if needed.
3. Is it algebraic + root? Factor highest power; e.g. \(\sqrt{n^2+3n} - n = n(\sqrt{1+3/n}-1)\).
4. Is it oscillatory with shrinking weight? Bound oscillation term and show weight \(\to 0\).
5. Is it exponential/power mix? Compare growth rates: \(a^n\) vs \(n^k\) vs \(\log n\).
6. Can you squeeze it? Create upper/lower simpler sequences.

---

## 8. Practice variants

Try to apply the “gap” method to these:

- \(\displaystyle x_n = \frac{3n+2}{3n-5}\) (expect \(1 + \frac{7}{3n-5}\)).
- \(\displaystyle x_n = \frac{2n^2+1}{5n^2 - n} = \frac{2}{5} + \frac{(5)(1)-2(-1)}{5(5n^2 - n)}\) (or just divide by \(n^2\)).
- \(\displaystyle x_n = \sqrt{n^2 + 4n} - n\) (trick: multiply by conjugate ⇒ limit \(2\)).
- \(\displaystyle x_n = \left(1 - \frac{2}{n}\right)^n \to e^{-2}\).

Work out \(x_n - L\) each time until it reduces to something like \(C/n\) or \(C/n^2\).

---

## 9. Summary “recipe”

Identify pattern → guess limit \(L\) → algebraically isolate \(x_n - L\) → bound it by a simple decreasing positive sequence → use Archimedean property → done.

The “gap” is not a lucky guess; it’s a systematic exploitation of algebra to expose a term known to go to zero.

---
