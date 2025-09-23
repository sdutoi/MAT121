Here is the step-by-step solution for the area between \(f(x) = x^{1/2}\) and \(g(x) = x^2\) from \(a=0\) to \(b=2\).

### Step-by-Step Solution

The area is given by the formula:
\[
A = \int_a^b |f(x) - g(x)| \, dx
\]

#### Step 1: Find intersection points
Set \(f(x) = g(x)\) to find where the graphs cross.
\[
x^{1/2} = x^2
\]
Square both sides:
\[
x = x^4
\]
\[
x^4 - x = 0
\]
\[
x(x^3 - 1) = 0
\]
The intersection points are \(x=0\) and \(x=1\). Since \(x=1\) is within our integration interval \([0, 2]\), we must split the integral into two parts: one from 0 to 1, and another from 1 to 2.

#### Step 2: Determine the greater function on each sub-interval

*   **Interval \([0, 1]\):** Let's test \(x=1/4\).
    *   \(f(1/4) = (1/4)^{1/2} = 1/2\)
    *   \(g(1/4) = (1/4)^2 = 1/16\)
    *   On \([0, 1]\), \(f(x) \geq g(x)\). The integrand is \(x^{1/2} - x^2\).

*   **Interval \([1, 2]\):** Let's test \(x=1.5\).
    *   \(f(1.5) = (1.5)^{1/2} \approx 1.22\)
    *   \(g(1.5) = (1.5)^2 = 2.25\)
    *   On \([1, 2]\), \(g(x) > f(x)\). The integrand is \(x^2 - x^{1/2}\).

#### Step 3: Set up and evaluate the integrals

The total area is the sum of the areas from the two sub-intervals.
\[
A = \int_{0}^{1} (x^{1/2} - x^2) \, dx + \int_{1}^{2} (x^2 - x^{1/2}) \, dx
\]

**Part 1: Integral from 0 to 1**
\[
\int_{0}^{1} (x^{1/2} - x^2) \, dx = \left[ \frac{x^{3/2}}{3/2} - \frac{x^3}{3} \right]_{0}^{1} = \left[ \frac{2}{3}x^{3/2} - \frac{1}{3}x^3 \right]_{0}^{1}
\]
\[
= \left( \frac{2}{3}(1) - \frac{1}{3}(1) \right) - (0) = \frac{1}{3}
\]

**Part 2: Integral from 1 to 2**
\[
\int_{1}^{2} (x^2 - x^{1/2}) \, dx = \left[ \frac{x^3}{3} - \frac{2}{3}x^{3/2} \right]_{1}^{2}
\]
\[
= \left( \frac{(2)^3}{3} - \frac{2}{3}(2)^{3/2} \right) - \left( \frac{(1)^3}{3} - \frac{2}{3}(1)^{3/2} \right)
\]
\[
= \left( \frac{8}{3} - \frac{2}{3}(2\sqrt{2}) \right) - \left( \frac{1}{3} - \frac{2}{3} \right) = \left( \frac{8 - 4\sqrt{2}}{3} \right) - \left( -\frac{1}{3} \right)
\]
\[
= \frac{8 - 4\sqrt{2} + 1}{3} = \frac{9 - 4\sqrt{2}}{3}
\]

#### Step 4: Add the results
\[
A_{total} = \frac{1}{3} + \frac{9 - 4\sqrt{2}}{3} = \frac{1 + 9 - 4\sqrt{2}}{3} = \frac{10 - 4\sqrt{2}}{3}
\]

#### Final Answer
The total area is **\(\frac{10 - 4\sqrt{2}}{3}\)** square units.

(This is approximately 1.448 square units).