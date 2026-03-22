# Useful Algebraic Identities

## Difference of powers (telescoping factorization)

For any numbers (or elements in a commutative ring) \(a,b\) and integer \(n\ge 1\):

- Identity:
  \[
  a^n - b^n = (a-b)\sum_{k=0}^{n-1} a^{\,n-1-k} b^{\,k}.
  \]

- Quick proof: Divide both sides by \((a-b)\) (or expand and collect terms) and note the internal sum telescopes:
  \[
  (a-b)\sum_{k=0}^{n-1} a^{\,n-1-k} b^{\,k}
  = \sum_{k=0}^{n-1} a^{\,n-k} b^{\,k} - \sum_{k=0}^{n-1} a^{\,n-1-k} b^{\,k+1}
  = a^n - b^n.
  \]

- Consequence (uniform bound when \(|a|,|b|\le B<1\)):
  \[
  |a^n - b^n| \le |a-b| \sum_{k=0}^{n-1} |a|^{\,n-1-k} |b|^{\,k}
  \le |a-b|\, n \, B^{\,n-1}.
  \]
  This is the estimate used to control the “finite part” in Exercise 2(c).

- Example (\(n=4\)):
  \[
  a^4 - b^4 = (a-b)(a^3 + a^2 b + a b^2 + b^3),
  \]
  which has \(n=4\) terms inside the parentheses, each of degree \(n-1=3\).
