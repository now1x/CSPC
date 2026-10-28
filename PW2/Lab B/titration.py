"""
PW2 Lab B Part 5 (bonus) -- find a titration's equivalence point.

titration.csv holds a titration curve: pH versus the volume of base added.
The equivalence point is the volume where the pH changes fastest (the steep
jump). Numerically, that is where the SLOPE of the pH curve is largest.
Run:  python titration.py
"""
import numpy as np
import matplotlib.pyplot as plt

# TODO 1: read titration.csv (columns volume_base, pH) into arrays V, pH.
data = np.loadtxt("titration.csv", delimiter=",", skiprows=1)
V = data[:, 0]
pH = data[:, 1]

# TODO 2: compute the slope of the pH curve with np.gradient(pH, V), and find
#         the volume where that slope is largest (np.argmax). That is the
#         equivalence point. Print it.
slope = np.gradient(pH, V)
eq_point = V[np.argmax(slope)]
print(f"equivalence point: {eq_point:.2f} mL")

# TODO 3: make two plots side by side: (left) pH vs volume with a line at the
#         equivalence point; (right) the slope vs volume, showing it peaks
#         at the equivalence point. Save as titration.png.
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

ax1.plot(V, pH, label="pH curve")
ax1.axvline(eq_point, color='red', linestyle='--', label='equivalence point')
ax1.set_xlabel("volume of base added (mL)")
ax1.set_ylabel("pH")
ax1.set_title("Titration Curve")
ax1.legend()

ax2.plot(V, slope, label="slope of pH curve", color='orange')
ax2.axvline(eq_point, color='red', linestyle='--', label='equivalence point')
ax2.set_xlabel("volume of base added (mL)")
ax2.set_ylabel("slope")
ax2.set_title("slope of pH curve")
ax2.legend()

fig.tight_layout()
fig.savefig("titration.png")
