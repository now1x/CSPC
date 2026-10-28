"""
PW2 Lab A -- Motion from tracking data.

Read noisy free-fall position measurements, then:
  - differentiate once  -> velocity
  - differentiate twice -> acceleration (should be ~ constant -g, but noisy!)
  - integrate the acceleration back up -> recover velocity and position

Complete the TODOs. Run:  python analysis.py
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import cumulative_trapezoid

G = -9.81  # m/s^2

# TODO 1: read freefall.csv into arrays t and y
#         (hint: np.loadtxt with a comma delimiter, skipping the header)
data = np.loadtxt("freefall.csv", delimiter=",", skiprows=1)
t = data[:, 0]
y = data[:, 1]

# TODO 2: compute velocity v = derivative of y w.r.t. t   (np.gradient)
#         and acceleration a = derivative of v w.r.t. t    (np.gradient again)
#         Print the mean acceleration. Is it close to -9.81? Is it noisy?
v = np.gradient(y, t)
a = np.gradient(v, t)

print(f"mean acceleration: {np.mean(a):.2f} m/s^2")
print(f"std of acceleration: {np.std(a):.2f} m/s^2")
# TODO 3: integrate a back up to recover velocity and position
#         (hint: cumulative_trapezoid(a, t, initial=0) + v[0], then again)
v_rec = cumulative_trapezoid(a, t, initial=0) + v[0]
y_rec = cumulative_trapezoid(v_rec, t, initial=0) + y[0]

max_error = np.max(np.abs(y_rec - y))
print(f"max error between recovered and original: {max_error:.2f} m")
# TODO 4: make a figure with 3 stacked panels: position, velocity, acceleration
#         vs time. Mark the true -9.81 line on the acceleration panel.
#         Save it as motion.png
fig, (ax_y, ax_v, ax_a) = plt.subplots(3, 1, sharex=True, figsize=(8, 10))

ax_y.plot(t, y, color="blue")
ax_y.set_ylabel("position (m)")
ax_y.set_title("free fall motion")

ax_v.plot(t, v, label="velocity", color="red")
ax_v.set_ylabel("velocity (m/s)")

ax_a.plot(t, a, label="acceleration", color="green")
ax_a.set_ylabel("acceleration (m/s^2)")
ax_a.axhline(G, color="black", linestyle="--", label="-9.81 m/s^2")
ax_a.set_xlabel("time (s)")
ax_a.legend()

fig.tight_layout()
fig.savefig("motion.png")