# Majorant and Geometric Series for Convergence Tests

## What is a "Majorant"?

A **majorant** (German: "Majorante") is a series that provides an **upper bound** for another series.

**Definition:** If we have two series $\sum a_n$ and $\sum b_n$ with $|a_n| \leq b_n$ for all $n$, then $\sum b_n$ is called a **majorant** of $\sum a_n$.

## Geometric Series as Majorant

### The Geometric Series: $\sum_{l=0}^{\infty} q^l$ where $|q| < 1$

**Key facts:**
- **Converges** when $|q| < 1$
- **Sum** = $\frac{1}{1-q}$
- **Terms** decrease exponentially: $q^0, q^1, q^2, q^3, \ldots$

### How to Use as Majorant for Comparison

**Step 1: Find the right geometric series**
Look for a constant $q$ with $|q| < 1$ such that your series terms can be bounded by $Cq^n$ for some constant $C$.

**Step 2: Establish the inequality**
Show that $|a_n| \leq C \cdot q^n$ for large $n$.

**Step 3: Apply comparison test**
Since $\sum C \cdot q^n = C \sum q^n$ converges, your series $\sum a_n$ converges.

## Practical Examples

### Example 1: $\sum_{n=1}^{\infty} \frac{1}{2^n + n}$

**Strategy:** Compare with geometric series $\sum \left(\frac{1}{2}\right)^n$

**Majorant inequality:** For $n \geq 1$:
$$\frac{1}{2^n + n} < \frac{1}{2^n} = \left(\frac{1}{2}\right)^n$$

Since $\sum \left(\frac{1}{2}\right)^n$ converges (geometric, $|q| = \frac{1}{2} < 1$), our series converges.

### Example 2: $\sum_{n=0}^{\infty} \frac{n^2}{3^n}$

**Strategy:** For large $n$, polynomial growth is dominated by exponential decay.

**Majorant:** We can show that for large $n$:
$$\frac{n^2}{3^n} \leq \left(\frac{2}{3}\right)^n$$

Since $\sum \left(\frac{2}{3}\right)^n$ converges, our series converges.

### Example 3: $\sum_{n=1}^{\infty} \frac{\sin(n)}{2^n}$

**Majorant inequality:** Since $|\sin(n)| \leq 1$:
$$\left|\frac{\sin(n)}{2^n}\right| \leq \frac{1}{2^n} = \left(\frac{1}{2}\right)^n$$

The geometric majorant $\sum \left(\frac{1}{2}\right)^n$ converges, so our series converges absolutely.

## Why Geometric Series Are Perfect Majorants

1. **Simple form**: Easy to work with algebraically
2. **Known convergence**: We know exactly when they converge
3. **Exponential decay**: They decrease faster than polynomial growth
4. **Flexible**: Can adjust the ratio $q$ and multiplier $C$ as needed

## The Comparison Test Process

1. **Identify** if your series has exponentially decreasing behavior
2. **Choose** appropriate $q < 1$ and constant $C$
3. **Prove** the inequality $|a_n| \leq C \cdot q^n$
4. **Conclude** convergence since geometric majorant converges

The geometric series $\sum q^n$ with $|q| < 1$ is like a "convergence measuring stick" - if you can bound your series by a convergent geometric series, then your series must also converge!

## Practice Exercises

**Exercise 1:** Use geometric majorants to test convergence of the following series:

(a) $\sum_{n=1}^{\infty} \frac{1}{3^n + n^2}$

(b) $\sum_{n=0}^{\infty} \frac{n}{4^n}$

(c) $\sum_{n=1}^{\infty} \frac{\cos(n^2)}{5^n}$

(d) $\sum_{n=1}^{\infty} \frac{1}{2^n - 1}$

**Exercise 2:** For each series, find an appropriate geometric majorant and prove the inequality:

(a) $\sum_{n=2}^{\infty} \frac{1}{3^n + 2^n}$

(b) $\sum_{n=0}^{\infty} \frac{n^3}{7^n}$

(c) $\sum_{n=1}^{\infty} \frac{(-1)^n}{4^n + n}$

(d) $\sum_{n=1}^{\infty} \frac{n!}{n^n \cdot 2^n}$

**Exercise 3:** Advanced problems:

(a) $\sum_{n=1}^{\infty} \frac{1}{n \cdot 3^n}$

(b) $\sum_{n=0}^{\infty} \frac{\sin(n) + \cos(n)}{2^n}$

(c) $\sum_{n=1}^{\infty} \frac{1}{2^n + 3^n}$

(d) $\sum_{n=1}^{\infty} \frac{n^2 + \sin(n)}{5^n}$

**Exercise 4:** Challenge problems:

(a) Show that $\sum_{n=1}^{\infty} \frac{1}{n^2 \cdot 2^n}$ converges and find a geometric majorant.

(b) For what values of $a > 0$ does $\sum_{n=1}^{\infty} \frac{1}{a^n + n}$ converge?

(c) Compare $\sum_{n=1}^{\infty} \frac{1}{2^n + 3^n}$ with $\sum_{n=1}^{\infty} \frac{1}{3^n}$ and explain the result.

(d) Prove that if $|a_n| \leq C \cdot r^n$ for some $C > 0$ and $0 < r < 1$, then $\sum a_n$ converges absolutely.