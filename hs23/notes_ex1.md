Here’s the distilled takeaway for parts (a)–(c).

- Setup. For a function \(f:X\to Y\) and \(A\subseteq X\),
  - Image: \(f(A)=\{f(a):a\in A\}\subseteq Y\).
  - Preimage: \(f^{-1}(B)=\{x\in X:f(x)\in B\}\subseteq X\).

- (a) Always expansive:
  \[
  A \subseteq f^{-1}(f(A)).
  \]
  Reason: every \(x\in A\) maps into \(f(A)\), so it lies in the preimage. Intuition: applying \(f\) “forgets distinctions” (many \(x\) can share one image), and applying \(f^{-1}\) pulls back all points that look the same under \(f\).

- (b) Equality characterizes no-collisions (injectivity):
  - If \(f\) is injective, then
    \[
    f^{-1}(f(A))=A \quad \text{for all } A\subseteq X,
    \]
    because no outside point shares the same image as something in \(A\).
  - So injectivity turns the “expansion” in (a) into exact recovery.

- (c) Conversely, the equality for all subsets forces injectivity:
  \[
  \big(\forall A\subseteq X,\; f^{-1}(f(A))=A\big) \;\Longrightarrow\; f \text{ injective}.
  \]
  Idea: take \(A=\{a\}\). If some \(x\neq a\) had \(f(x)=f(a)\), then \(x\in f^{-1}(f(\{a\}))\), contradicting equality.

- Conceptual picture (equivalence classes):
  - Define \(x\sim y \iff f(x)=f(y)\). Then \(f^{-1}(f(A))\) is the “\(\sim\)-saturation” of \(A\): it contains all points in the same fibers as elements of \(A\).
  - (a) says saturation contains \(A\).
  - (b)(c) say “saturation = \(A\) for all \(A\)” iff each fiber is a singleton, i.e., \(f\) is injective.

- Useful dual fact (for surjectivity, not asked but complementary):
  \[
  f(f^{-1}(B)) \subseteq B \text{ for all } B\subseteq Y,\qquad
  f \text{ surjective } \iff f(f^{-1}(B))=B \text{ for all } B.
  \]
  So preimage–image tests injectivity; image–preimage tests surjectivity.