# exercise sheet 2


# 1.b)

## Problem

Given
- initial value: $a_0=1$,
- recurrence (for all $n\ge 0$):
  $$
  a_{n+1}=a_n+a_{n-1}+\cdots+a_1+a_0+1=\sum_{k=0}^{n} a_k + 1,
  $$
find a closed formula for $a_n$.

This is a “cumulative” recurrence: the next term equals the sum of all previous terms plus a constant.

## How to see the trick

Define partial sums
$$
S_n:=\sum_{k=0}^n a_k.
$$
Then the recurrence is simply
$$
a_{n+1}=S_n+1.
$$
But also
$$
a_n=S_{n-1}+1.
$$
If you subtract these two equations, the constants cancel and you expose the last added term:
$$
a_{n+1}-a_n=(S_n+1)-(S_{n-1}+1)=S_n-S_{n-1}=a_n.
$$
This is the key “difference of consecutive cumulative sums = last term” idea.

So you get a first‑order linear recurrence with constant coefficient:
$$
a_{n+1}=2a_n \quad (n\ge 0).
$$

With $a_0=1$, the solution is immediate:
$$
a_n=2^n.
$$

## Why this works (intuition)

- $a_{n+1}$ is “all the previous stuff” plus $1$.
- $a_n$ is “all the stuff before that” plus $1$.
- Their difference is exactly the most recent piece, which is $a_n$ itself.
- So each step doubles the sequence value.

## Verification (first terms)

- $a_0=1$,
- $a_1=a_0+1=2$,
- $a_2=a_1+a_0+1=2+1+1=4$,
- $a_3=4+2+1+1=8$,
matching $2^n$.

## Alternative route via partial sums

From $a_{n+1}=S_n+1$,
$$
S_{n+1}=S_n+a_{n+1}=2S_n+1,\qquad S_0=a_0=1.
$$
Solve $S_{n+1}=2S_n+1$:
- homogeneous part $C\cdot 2^n$, particular solution $-1$,
- $S_n=2^{n+1}-1$ (from $S_0=1$),
so $a_{n+1}=S_n+1=2^{n+1}$ and hence $a_n=2^n$.

## Generalization and consistency check

If the problem were $a_{n+1}=\sum_{k=0}^n a_k + c$ with $a_0=\alpha$, the same subtraction gives $a_{n+1}=2a_n$ (the constant cancels), so $a_n=2^n\alpha$. For this to be consistent with $a_1=a_0+c$, you must have $c=\alpha$ (as in our problem: $c=1$, $\alpha=1$).

## Takeaway pattern

- For recurrences of the form “next = sum of previous + constant,” try subtracting consecutive equations; you’ll often reduce to a simple first‑order linear recurrence.
- Once you have $a_{n+1}=r a_n$ and an initial value, the solution is $a_n=a_0\, r^n$. Here, $r=2$ and $a_0=1$, so $a_n=2^n$.