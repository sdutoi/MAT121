# Cauchy product of absolutely convergent series — a clear index guide

This note unpacks the “star” regrouping identity and the proof that the product of two absolutely convergent series equals the sum of their Cauchy product.

## Setup and goal

Let \((x_n)_{n\ge 0}\) and \((y_n)_{n\ge 0}\) be real (or complex) sequences such that the series
$$
\sum_{n=0}^{\infty} |x_n| < \infty, \qquad \sum_{n=0}^{\infty} |y_n| < \infty
$$
are absolutely convergent. Define the partial sums
$$
X_n := \sum_{k=0}^{n} x_k, \qquad Y_n := \sum_{\ell=0}^{n} y_\ell.
$$
The Cauchy product sequence \((z_n)\) is
$$
\boxed{\; z_n := \sum_{k=0}^{n} x_k\, y_{n-k} \;}
$$
The claim is that \(\sum_{n=0}^{\infty} z_n\) converges absolutely and
$$
\boxed{\;\Bigl(\sum_{n=0}^{\infty} x_n\Bigr)\Bigl(\sum_{n=0}^{\infty} y_n\Bigr)
= \sum_{n=0}^{\infty} z_n\; }.
$$

## The diagonal regrouping identity (\(*\))
Start from the product of partial sums and expand:
$$
X_n\, Y_n
= \Bigl(\sum_{k=0}^{n} x_k\Bigr)\Bigl(\sum_{\ell=0}^{n} y_\ell\Bigr)
= \sum_{k=0}^{n} \sum_{\ell=0}^{n} x_k y_\ell.
$$
Regroup by diagonals \(m = k+\ell\):
$$
X_n Y_n
= \sum_{m=0}^{2n} \sum_{\substack{0\le k,\,\ell\le n\\ k+\ell=m}} x_k y_\ell\tag{*}
$$
Split the \(m\)-range:
- If \(0\le m\le n\): then \(0\le k\le m\) and \(\ell = m-k\), so
  $$\sum_{\substack{0\le k,\,\ell\le n\\ k+\ell=m}} x_k y_\ell = \sum_{k=0}^{m} x_k y_{m-k}.$$
- If \(n+1\le m\le 2n\): then \(m-n\le k\le n\) and \(\ell = m-k\), so
  $$\sum_{\substack{0\le k,\,\ell\le n\\ k+\ell=m}} x_k y_\ell = \sum_{k=m-n}^{n} x_k y_{m-k}.$$
Therefore
$$
X_n Y_n = \sum_{m=0}^{n} \sum_{k=0}^{m} x_k y_{m-k}
+ \sum_{m=n+1}^{2n} \sum_{k=m-n}^{n} x_k y_{m-k}.
$$
Recognize the Cauchy product and define the “remainder triangle”
$$
T_n := \sum_{m=n+1}^{2n} \sum_{\substack{0\le k,\,\ell\le n\\ k+\ell=m}} x_k y_\ell,
$$
so that
$$
\boxed{\; X_n Y_n = \sum_{m=0}^{n} z_m + T_n \; }.
$$

## Absolute convergence of \(\sum z_n\)
Using \((*)\) with absolute values gives
$$
\sum_{m=0}^{n} |z_m|
\le \sum_{m=0}^{n} \sum_{k=0}^{m} |x_k|\,|y_{m-k}|
\le \sum_{m=0}^{2n} \sum_{\substack{0\le k,\,\ell\le n\\ k+\ell=m}} |x_k|\,|y_\ell|
= \Bigl(\sum_{k=0}^{n} |x_k|\Bigr) \Bigl(\sum_{\ell=0}^{n} |y_\ell|\Bigr)
\le \Bigl(\sum_{k=0}^{\infty} |x_k|\Bigr) \Bigl(\sum_{\ell=0}^{\infty} |y_\ell|\Bigr) < \infty.
$$
Hence \(\sum_{n=0}^{\infty} z_n\) is absolutely convergent.

## Controlling the remainder triangle \(T_n\)
From the definition and absolute values,
$$
|T_n| \le \sum_{m=n+1}^{2n} \sum_{\substack{0\le k,\,\ell\le n\\ k+\ell=m}} |x_k|\,|y_\ell|
= \sum_{k=0}^{n} |x_k| \sum_{\ell=n+1-k}^{n} |y_\ell|.
$$
Split at \(k = \lfloor n/2\rfloor\):
$$
|T_n| \le \sum_{k=0}^{\lfloor n/2\rfloor} |x_k| \sum_{\ell=\lceil n/2\rceil}^{n} |y_\ell|
\; + \; \sum_{k=\lfloor n/2\rfloor+1}^{n} |x_k| \sum_{\ell=0}^{n} |y_\ell|.
$$
Let
$$
 a := \sum_{k=0}^{\infty} |x_k|, \qquad b := \sum_{\ell=0}^{\infty} |y_\ell|.
$$
Then
$$
|T_n| \le a\, \sum_{\ell=\lceil n/2\rceil}^{n} |y_\ell| \; + \; b\, \sum_{k=\lfloor n/2\rfloor+1}^{n} |x_k|.
$$
Given \(\varepsilon>0\), by absolute convergence there are indices \(n_1,n_2\) such that for all \(n>m\ge n_1\)
$$
\sum_{k=m+1}^{n} |x_k| < \frac{\varepsilon}{2b},
$$
and for all \(n>m\ge n_2\)
$$
\sum_{\ell=m+1}^{n} |y_\ell| < \frac{\varepsilon}{2a}.
$$
Set
$$
 n_{\varepsilon} := 2\max\{n_1,n_2\}+2.
$$
Then for all \(n\ge n_{\varepsilon}\)
$$
 |T_n| \le a\cdot \frac{\varepsilon}{2a} + b\cdot \frac{\varepsilon}{2b} = \varepsilon,
$$
so \(T_n\to 0\).

## Conclusion
From \(X_n Y_n = \sum_{m=0}^{n} z_m + T_n\) and \(T_n\to 0\), while \(\sum z_n\) converges absolutely, we obtain
$$
\lim_{n\to\infty} X_n Y_n = \sum_{m=0}^{\infty} z_m,
$$
hence
$$
\boxed{\;\Bigl(\sum_{n=0}^{\infty} x_n\Bigr)\Bigl(\sum_{n=0}^{\infty} y_n\Bigr) = \sum_{n=0}^{\infty} \Bigl(\sum_{k=0}^{n} x_k y_{n-k}\Bigr).\;}
$$

## Intuition: diagonals in an \(n\times n\) grid
- Consider all pairs \((k,\ell)\) with \(0\le k,\ell\le n\). The diagonal \(m=k+\ell\) collects pairs with the same sum.
- The first \(n+1\) diagonals \(m=0,\dots,n\) exactly produce \(z_0+\cdots+z_n\).
- The last \(n\) diagonals \(m=n+1,\dots,2n\) form the top-right triangle \(T_n\), which vanishes as \(n\to\infty\) under absolute convergence.

## Tiny sanity check (\(n=2\))
With \(n=2\):
$$
X_2 Y_2 = (x_0+x_1+x_2)(y_0+y_1+y_2)
= \underbrace{x_0y_0}_{m=0} + \underbrace{(x_0y_1+x_1y_0)}_{m=1}
+ \underbrace{(x_0y_2+x_1y_1+x_2y_0)}_{m=2}
+ \underbrace{(x_1y_2+x_2y_1)}_{m=3} + \underbrace{x_2y_2}_{m=4}.
$$
Here \(z_0+z_1+z_2\) are the first three diagonals (\(m\le 2\)), and the last two diagonals form \(T_2\).