# u-Substitution (Change of Variables) Cheat Sheet

A compact reference for performing substitutions in **definite integrals**.

---
## 1. Goal
Transform an integral of the form
\[
\int_a^b f(g(x))\,g'(x)\,dx
\]
into a simpler integral in a new variable \(u = g(x)\).

---
## 2. Standard Algorithm (Definite Integrals)
1. **Choose** \(u = g(x)\) (an "inner" expression whose derivative appears as a factor).
2. **Differentiate:** \(du = g'(x)\,dx\) and solve for \(dx\).
3. **Change bounds:** \(x=a \Rightarrow u = g(a)\); \(x=b \Rightarrow u = g(b)\).
4. **Rewrite** the entire integrand and \(dx\) in terms of \(u\); no \(x\) should remain.
5. **Integrate** with respect to \(u\).
6. **Evaluate** using the new \(u\)-limits (no back-substitution needed if you changed bounds).
7. **(Optional)** If limits were reversed originally, account for the sign: \(\int_a^b = -\int_b^a\).

**NEVER** both change bounds *and* back-substitute—pick one style.

---
## 3. Two Styles (Pick One)
| Style | Steps | When Preferred |
|-------|-------|----------------|
| A. Change Bounds | Steps 1–6 above; never return to \(x\) | Cleaner, less error-prone |
| B. Keep Bounds | Omit Step 3, integrate in \(u\), back-substitute to \(x\), then plug \(a,b\) | If you forgot/can't change bounds |

---
## 4. Recognizing a Good Substitution
- Inside a composite: powers, roots, trig of another function.
- Something whose derivative (up to constant) is present as a factor.
- Linear: \(u = ax + b\) (very common; leads to the shortcut formula).

**Fails** if derivative introduces factors not present (e.g. \(u = x^2 - 3\) in \((x^2 - 3)^3\) without an \(x\) factor). Use symmetry or expansion instead.

---
## 5. Common Patterns
| Integrand | Substitution | Result Skeleton |
|-----------|--------------|-----------------|
| \((ax+b)^n\) | \(u = ax + b\) | \(\frac{(ax+b)^{n+1}}{a(n+1)} + C\) for \(n\neq -1\) |
| \((ax+b)^{-1}\) | \(u = ax + b\) | \(\frac{1}{a}\ln|ax+b| + C\) |
| \(x (x^2 + c)^n\) | \(u = x^2 + c\) | \(\frac{1}{2}\int u^n du\) |
| \(\cos x (\sin x)^n\) | \(u = \sin x\) | \(\int u^n du\) |
| \(\sin x (\cos x)^n\) | \(u = \cos x\) | \(-\int u^n du\) |

---
## 6. Orientation & Reversed Limits
If substitution makes upper bound smaller than lower, you can:
- Keep as-is (the evaluation will reflect the sign), or
- Swap bounds and insert a minus sign.

Example: \(u = 1 - x\) in \(\int_0^1 (1-x)^4 dx\) gives bounds \(1 \to 0\); \(dx = -du\):
\[
\int_{0}^{1} (1-x)^4 dx = \int_{1}^{0} u^4 (-du) = \int_{0}^{1} u^4 du.
\]

---
## 7. Worked Examples
### Example 1 (Linear Shift / Translation Invariance)
\[
\int_{-4}^{-2} (x+4)^{10} dx.
\]
Let \(u = x + 4\), \(du = dx\), bounds: \(-4 \to 0\), \(-2 \to 2\):
\[
\int_{0}^{2} u^{10} du = \left[\frac{u^{11}}{11}\right]_0^2 = \frac{2048}{11}.
\]
If original had reversed limits (\(-2\) to \(-4\)), attach a minus sign.

### Example 2 (Chain Rule Present)
\[
\int_{0}^{1} x (x^2 + 1)^5 dx.
\]
Let \(u = x^2 + 1\), \(du = 2x dx\), so \(x dx = du/2\); bounds: \(0\to 1\), \(1\to 2\):
\[
\frac{1}{2}\int_{1}^{2} u^5 du = \frac{1}{2} \left[\frac{u^6}{6}\right]_1^2 = \frac{63}{12} = \frac{21}{4}.
\]

### Example 3 (When Substitution *Doesn't* Fit Directly)
\[
\int_{-3}^{3} (x^2 - 3)^3 dx.
\]
\(u = x^2 - 3\) gives \(du = 2x dx\) but no \(x\) factor is present. Instead:
- Use even symmetry: integrand is even (only even powers after expansion), so
\[
2 \int_{0}^{3} (x^2 - 3)^3 dx.
\]
Then expand or apply another method.

---
## 8. Quick Error Checklist
- [ ] Wrote down \(u = g(x)\) explicitly.
- [ ] Correct \(du\) and solved for \(dx\).
- [ ] Converted **both** bounds.
- [ ] Rewrote integrand with no stray \(x\).
- [ ] Integrated correctly in \(u\).
- [ ] Evaluated using *only* new bounds (or back-substituted if you kept old bounds).

---
## 9. Mental Shortcut for Linear Inside
If \(u = ax + b\), you can memorize:
\[
\int (ax+b)^n dx = \frac{(ax+b)^{n+1}}{a(n+1)} + C \quad (n \ne -1),
\]
which is just the u-sub rule executed in one step.

---
## 10. Translation Invariance (Special Case)
Horizontal shifts don’t change area shape:
\[
\int_{a}^{b} f(x) dx = \int_{a-h}^{b-h} f(x+h) dx.
\]
Used implicitly when setting \(u = x + h\).

---
**Practice Prompt:** Evaluate \(\int_{0}^{\pi/2} \sin^3 x \cos x dx\) using substitution.
(Answer: \(1/4\) via \(u = \sin x\).)

---
**Tip:** If you *want* a substitution but are missing the matching derivative factor, consider:
- Algebraic manipulation (factor, expand, divide)
- Symmetry (even/odd)
- Integration by parts (to manufacture the derivative)

---
Feel free to extend this file with additional examples you encounter.
