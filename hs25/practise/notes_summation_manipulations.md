You’re asking exactly the right question: when can we change the summation index (like \(k\)) freely, and when must we keep \(n\) fixed because it plays a different role? The short answer: 

- \(k\) (or \(j,i,\ell\)) inside \(\sum\) is a **dummy (bound) variable**: you can rename or shift it as long as you change every occurrence consistently and adjust limits.  
- \(n\) is a **free (external) parameter** in the statement you’re proving—don’t rename or treat it like a dummy variable in the same expression.  
- Confusion often comes from writing an equality and silently replacing a dummy variable but forgetting what is bound and what is free.

Below is a structured guide.

---

## 1. Bound (dummy) vs free variables

Example:
\[
S_n = \sum_{k=1}^{n} (-1)^{k-1} k^2.
\]
Here:
- \(n\) is a free parameter: it specifies which partial sum you mean.
- \(k\) is a dummy index: it “runs” through the integers \(1,2,\dots,n\). The symbol \(k\) itself has no life outside the sum.

You may replace \(k\) by \(j\):
\[
\sum_{k=1}^n (-1)^{k-1}k^2 = \sum_{j=1}^n (-1)^{j-1}j^2.
\]
Same object—just a rename.

But you may **not** replace \(k\) by \(n\) inside:
\[
\sum_{k=1}^n (-1)^{k-1} k^2 \;\not=\; \sum_{n=1}^n (-1)^{n-1} n^2.
\]
The right-hand side is nonsense (or collapses) because now \(n\) is both the index and the upper limit; the outer \(n\) loses its meaning.

---

## 2. Reindexing (shifting the dummy variable)

Shifts are legal if you adjust bounds:

Example:
\[
\sum_{k=1}^{n} (-1)^{k-1} T_k
\quad\text{let } j=k-1 \Longrightarrow k=j+1,\; k=1\to j=0,\; k=n\to j=n-1
\]
\[
= \sum_{j=0}^{n-1} (-1)^{(j+1)-1} T_{j+1} = \sum_{j=0}^{n-1} (-1)^j T_{j+1}.
\]

Both sums are equal; only the “dummy label” and bounds changed.

---

## 3. Why you cannot “turn \(k\) into \(n\)” mid-stream

Suppose you are in the induction step and you write:
\[
S_{n+1} = \sum_{k=1}^{n+1} (-1)^{k-1} k^2.
\]
You might be tempted to say “let’s just call \(k = n\)” for the last term—fine—but that **specific** term is:
\[
(-1)^{(n+1)-1} (n+1)^2.
\]
You isolate it by splitting the sum:
\[
\sum_{k=1}^{n+1} \cdots = \left(\sum_{k=1}^{n} \cdots\right) + \text{(the term with }k=n+1).
\]
You are *not* replacing all \(k\) by \(n\); you are separating one endpoint term. This is legitimate because:
\[
\sum_{k=1}^{n+1} a_k = \left(\sum_{k=1}^{n} a_k\right) + a_{n+1}.
\]
But if you wrote
\[
\sum_{k=1}^{n+1} a_k = \sum_{n=1}^{n+1} a_n
\]
you’d destroy the meaning: the symbol \(n\) is already used as the bound.

---

## 4. Common safe operations

1. Renaming the dummy:
   \[
   \sum_{k=1}^{n} f(k) = \sum_{j=1}^{n} f(j).
   \]

2. Shifting:
   \[
   \sum_{k=r}^{s} f(k) = \sum_{j=0}^{s-r} f(j+r).
   \]

3. Splitting off last term:
   \[
   \sum_{k=1}^{n} f(k) = \left(\sum_{k=1}^{n-1} f(k)\right) + f(n).
   \]

4. Pairing:
   \[
   \sum_{k=1}^{n} \bigl(g(k)-g(k-1)\bigr) = g(n)-g(0).
   \]

All preserve meaning because they respect which variables are bound.

---

## 5. Where mistakes happen

| Mistake | Example | Why wrong |
|---------|---------|-----------|
| Using the parameter name as the dummy | \(\sum_{n=1}^{n} (-1)^n n^2\) | Ambiguous: the first \(n\) (limit) depends on itself.|
| Changing the dummy in only part of an expression | \(\sum_{k=1}^n k^2 = \sum_{j=1}^n k^2\) | Mixed symbols inside; must change all occurrences of \(k\). |
| Forgetting to adjust limits when shifting | \(\sum_{k=1}^n f(k) = \sum_{j=0}^n f(j+1)\) | Upper limit should be \(n-1\) if \(j=k-1\). |
| Treating a free variable as if it were dummy | Replacing \(n\) by \(m\) halfway in the same formula | Changes the meaning (different parameter). |

---

## 6. Induction context: variable roles

In the induction step:
- You assume a statement \(P(n)\) (with \(n\) free).
- You must prove \(P(n+1)\).
- Inside sums defining \(S_{n+1}\), the dummy \(k\) lives only inside the summation—never replace the free \(n+1\) with \(k\), or vice versa.

A clean template:
\[
S_{n+1} = \sum_{k=1}^{n+1} a_k
= \Bigl(\sum_{k=1}^{n} a_k\Bigr) + a_{n+1}
\xrightarrow{\text{use hypothesis on the first sum}} \cdots
\]

---

## 7. Practical checklist before altering a sum

Before you rename/reindex, ask:

1. Is the symbol I’m changing currently a dummy (bound) variable?  
   If yes → safe to rename.
2. Will I change every occurrence of it inside the summation expression?  
   If yes → proceed.
3. Did I correctly transform the limits when shifting (add/subtract)?  
4. Am I accidentally reusing the parameter’s symbol as a dummy? If yes → pick a different dummy name.

---

## 8. Extra examples

### Example A: Alternating linear sum
\[
\sum_{k=1}^{n} (-1)^{k-1} k
\]
Write \(k = T_k - T_{k-1}\) where \(T_k = k(k+1)/2\):
\[
= \sum_{k=1}^{n} (-1)^{k-1}(T_k - T_{k-1})
= \sum_{k=1}^{n} (-1)^{k-1} T_k - \sum_{k=1}^{n} (-1)^{k-1}T_{k-1}.
\]
Reindex second:
\[
= \sum_{k=1}^{n} (-1)^{k-1} T_k - \sum_{j=0}^{n-1} (-1)^j T_j.
\]
Cancellation leaves \((-1)^{n-1} T_n\). Dummy variable renaming was legitimate each time.

### Example B: Shift to start at zero
\[
\sum_{k=1}^n f(k) = \sum_{j=0}^{n-1} f(j+1),
\]
valid because \(j = k-1\). Note changed upper bound.

---

## 9. Mental model

Think of a summation like an integral:
\[
\sum_{k=1}^n f(k) \quad\text{is analogous to}\quad \int_0^1 f(x)\,dx.
\]
Just as
\[
\int_{0}^{1} f(x)\,dx = \int_{0}^{1} f(t)\,dt
\]
(the variable is dummy), but you would not write
\[
\int_{0}^{x} f(x)\,dx
\]
with the same symbol for limit and integrand variable (ambiguous). Same principle.

---

## 10. Quick “OK / NOT OK” table

| Expression | OK? | Reason |
|------------|-----|--------|
| \(\sum_{k=1}^n k^2\) | Yes | Standard |
| \(\sum_{j=1}^n j^2\) | Yes | Renamed dummy |
| \(\sum_{k=1}^{n+1} k^2 = \sum_{k=1}^n k^2 + (n+1)^2\) | Yes | Split last term |
| \(\sum_{k=1}^{n} k^2 = \sum_{n=1}^{n} n^2\) | No | Parameter reused as dummy |
| \(\sum_{k=1}^n k^2 = \sum_{j=0}^n (j+1)^2\) | No | Upper limit should be \(n-1\) |
| \(\sum_{k=1}^n f(k) = \sum_{j=1}^n f(k)\) | No | Inconsistent replacement |

---

## 11. Summary mantra

Bound variables (inside \(\sum\)) are “disposable labels.”  
Free variables (parameters of the statement) carry meaning across the equation.  
Never promote a bound variable to a free one by accident, and never let a free one masquerade as bound.

---
