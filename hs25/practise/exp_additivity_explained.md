# Additivity of the exponential via power series

We prove for all \(z_1,z_2\in\mathbb{C}\):
$$
\exp(z_1+z_2)=\exp(z_1)\,\exp(z_2).
$$
Every step below states the relied-on facts explicitly.

## Pre-knowledge used

1. Definition (power series for \(\exp\)). For any \(z\in\mathbb{C}\)
   $$
   \exp(z)=\sum_{n=0}^{\infty}\frac{z^n}{n!}.
   $$
   This series has infinite radius of convergence and is absolutely convergent for every \(z\):
   $$
   \sum_{n=0}^{\infty}\left|\frac{z^n}{n!}\right|=\sum_{n=0}^{\infty}\frac{|z|^n}{n!}<\infty.
   $$
2. Cauchy product theorem (for absolutely convergent series). If \(\sum x_n\) and \(\sum y_n\) are absolutely convergent, then the series with terms
   $$
   z_n:=\sum_{k=0}^{n}x_k\,y_{n-k}
   $$
   also converges absolutely and
   $$
   \sum_{n=0}^{\infty}z_n=\Bigl(\sum_{n=0}^{\infty}x_n\Bigr)\Bigl(\sum_{n=0}^{\infty}y_n\Bigr).
   $$
   We will apply this with \(x_n=z_1^n/n!\) and \(y_n=z_2^n/n!\).
3. Binomial theorem (for complex numbers). For each integer \(n\ge 0\) and \(z_1,z_2\in\mathbb{C}\),
   $$
   (z_1+z_2)^n=\sum_{k=0}^{n}\binom{n}{k}z_1^{\,k}z_2^{\,n-k},\qquad\binom{n}{k}=\frac{n!}{k!(n-k)!}.
   $$

## Step 1: Expand the product of series

Using the definition of \(\exp\):
$$
\exp(z_1)\,\exp(z_2)=\Bigl(\sum_{n=0}^{\infty}\frac{z_1^{n}}{n!}\Bigr)\Bigl(\sum_{m=0}^{\infty}\frac{z_2^{m}}{m!}\Bigr).
$$
Both series are absolutely convergent, hence their product equals the sum of their Cauchy product (justified by the Cauchy product theorem).

## Step 2: Apply the Cauchy product

Therefore
$$
\exp(z_1)\,\exp(z_2)=\sum_{n=0}^{\infty}\,\sum_{k=0}^{n}\frac{z_1^{\,k}}{k!}\,\frac{z_2^{\,n-k}}{(n-k)!}.
$$
Rewriting the inner sum by factoring \(1/n!\):
$$
\sum_{k=0}^{n}\frac{z_1^{\,k}}{k!}\,\frac{z_2^{\,n-k}}{(n-k)!}
=\frac{1}{n!}\sum_{k=0}^{n}\binom{n}{k}z_1^{\,k}z_2^{\,n-k}.
$$

## Step 3: Invoke the binomial theorem

By the binomial theorem,
$$
\sum_{k=0}^{n}\binom{n}{k}z_1^{\,k}z_2^{\,n-k}=(z_1+z_2)^n.
$$
Hence the Cauchy product becomes
$$
\exp(z_1)\,\exp(z_2)=\sum_{n=0}^{\infty}\frac{(z_1+z_2)^n}{n!}.
$$

## Step 4: Recognize the exponential of the sum

By the power-series definition of \(\exp\), the right-hand side is exactly \(\exp(z_1+z_2)\). Therefore
$$
\boxed{\;\exp(z_1+z_2)=\exp(z_1)\,\exp(z_2).\;}
$$

## Corollaries

1. Setting \(z_1=0\): since \(\exp(0)=\sum_{n\ge 0}0^n/n!=1\), we get
   $$
   1=\exp(0)=\exp(z)\,\exp(-z) \quad\Rightarrow\quad \exp(-z)=\frac{1}{\exp(z)}.
   $$
2. In particular, \(\exp(z)\ne 0\) for all \(z\in\mathbb{C}\).

## Optional: Index picture of the Cauchy product

The inner sum for fixed \(n\)
$$
\sum_{k=0}^{n}\frac{z_1^{\,k}}{k!}\,\frac{z_2^{\,n-k}}{(n-k)!}
$$
collects all pairs \((k,\ell)\) with \(k+\ell=n\); this is the “diagonal” in the grid of indices of the two series. Absolute convergence is what licenses this regrouping.
