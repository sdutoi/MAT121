
- Goal: From A ~₂ B and B ~₂ C (i.e., N \ (A ∩ B) and N \ (B ∩ C) are finite), show A ~₂ C (i.e., N \ (A ∩ C) is finite).

- Key identity (De Morgan):
  $$\mathbb N \setminus (A \cap C) = (\mathbb N \setminus A) \cup (\mathbb N \setminus C).$$
  In the red notes this was written with “⊂”, but it should be “=” here.

- Two simple inclusions:
  - Since A ∩ B ⊆ A, taking complements gives
    $$\mathbb N \setminus A \subseteq \mathbb N \setminus (A \cap B).$$
  - Since B ∩ C ⊆ C, taking complements gives
    $$\mathbb N \setminus C \subseteq \mathbb N \setminus (B \cap C).$$

- Union preserves inclusion, so combining the two:
  $$(\mathbb N \setminus A) \cup (\mathbb N \setminus C) \subseteq \big(\mathbb N \setminus (A \cap B)\big) \cup \big(\mathbb N \setminus (B \cap C)\big).$$

- Substitute De Morgan’s identity on the left:
  $$\mathbb N \setminus (A \cap C) \subseteq \big(\mathbb N \setminus (A \cap B)\big) \cup \big(\mathbb N \setminus (B \cap C)\big).$$

- Conclusion: The right-hand side is a union of two finite sets (by the assumptions A ~₂ B and B ~₂ C), hence finite. Any subset of a finite set is finite, so N \ (A ∩ C) is finite. Therefore A ~₂ C.

Quick intuition check (element-wise): If x ∉ A ∩ C, then x ∉ A or x ∉ C. If x ∉ A, then x ∉ A ∩ B; if x ∉ C, then x ∉ B ∩ C. So x lies in N \ (A ∩ B) or N \ (B ∩ C), which is exactly the inclusion above.

Summary of the red line:
- Corrected form:
  $$\mathbb N \setminus (A \cap C) = (\mathbb N \setminus A) \cup (\mathbb N \setminus C) \subseteq \big(\mathbb N \setminus (A \cap B)\big) \cup \big(\mathbb N \setminus (B \cap C)\big).$$
- This yields transitivity because a subset of a finite union of finite sets is finite.

---


What the step needs: Given a positive lower bound ℓ > 0, we want an N ∈ N with 1/N < ℓ. That’s exactly the Archimedean property:

- Archimedean property: For every ε > 0 there exists N ∈ N such that 1/N < ε. Equivalently, for every x ∈ R there exists n ∈ N with n > x.

Applied here with ε = ℓ > 0, it gives an N with 1/N < ℓ. But 1/N ∈ M and ℓ is a lower bound of M, so we must also have ℓ ≤ 1/N, a contradiction. Hence no positive ℓ can be a lower bound, so the greatest lower bound is 0.

Notes:
- Some texts phrase the step as “since 1/n → 0, there exists N with 1/N < ℓ.” That convergence itself is typically proven using the Archimedean property. Either way, the logical engine behind picking such an N is the Archimedean property.

---

