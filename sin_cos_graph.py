import numpy as np
import matplotlib.pyplot as plt

# Define the x range from -2π to 2π
x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)

# Define the functions
y_sin = np.sin(x)
y_cos = np.cos(x)

# Create subplots for sin and cos
fig, axs = plt.subplots(2, 1, figsize=(8, 6))

# Plot sin(x)
axs[0].plot(x, y_sin, label="sin(x)", color="blue")
axs[0].axhline(0, color="black", linewidth=0.5)
axs[0].axvline(0, color="black", linewidth=0.5)
from matplotlib.ticker import FixedLocator, FixedFormatter

xticks = np.arange(-2 * np.pi, 2.5 * np.pi, np.pi / 2)
xticklabels = [
    r"$-2\pi$",
    r"$-\frac{3\pi}{2}$",
    r"$-\pi$",
    r"$-\frac{\pi}{2}$",
    r"$0$",
    r"$\frac{\pi}{2}$",
    r"$\pi$",
    r"$\frac{3\pi}{2}$",
    r"$2\pi$",
]
axs[0].xaxis.set_major_locator(FixedLocator(xticks))
axs[0].xaxis.set_major_formatter(FixedFormatter(xticklabels))
axs[0].set_title("Graph of sin(x)")
axs[0].legend()
axs[0].grid(True, linestyle="--", alpha=0.6)

# Plot cos(x)
axs[1].plot(x, y_cos, label="cos(x)", color="red")
axs[1].axhline(0, color="black", linewidth=0.5)
axs[1].axvline(0, color="black", linewidth=0.5)
axs[1].xaxis.set_major_locator(FixedLocator(xticks))
axs[1].xaxis.set_major_formatter(FixedFormatter(xticklabels))
axs[1].set_title("Graph of cos(x)")
axs[1].legend()
axs[1].grid(True, linestyle="--", alpha=0.6)

plt.tight_layout()
plt.show()
