"""
PW2 Lab B Part 3 -- fit a reaction's rate constant to measured data.

A first-order reaction decays as  C(t) = C0 * exp(-k*t).  You have noisy
concentration-vs-time measurements; find the k that best matches them.
Complete the TODOs. Run:  python kinetics.py
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

# TODO 1: read kinetics.csv (columns time, concentration) into arrays t, C.
#         Set C0 = the first concentration.
data = np.loadtxt("kinetics.csv", delimiter=",", skiprows=1)
t = data[:, 0]
C = data[:, 1]
C0 = C[0]

# TODO 2: write total_error(k) = sum of (measured - C0*exp(-k*t))^2.
#         This is the "how bad" number: small when the model matches the data.
def total_error(k):
    C_model = C0 * np.exp(-k * t)
    error = np.sum((C - C_model) ** 2)
    return error

# TODO 3: minimise total_error with scipy.optimize.minimize (method "SLSQP",
#         bounds [(0, 5)], start x0=0.5). Print the fitted k.
result = minimize(total_error, x0=0.5, method="SLSQP", bounds=[(0, 5)])
fitted_k = result.x[0]
print(f"Fitted k: {fitted_k:.4f}")

# TODO 4: plot the measured data (points) and your fitted curve (line) together.
#         Save as kinetics.png.
t_fit = np.linspace(min(t), max(t), 100)
C_fit = C0 * np.exp(-fitted_k * t_fit)
plt.scatter(t, C, label="measured data", color="blue")
plt.plot(t_fit, C_fit, label="fitted curve", color="red")
plt.xlabel("time")
plt.ylabel("concentration")
plt.title("decay fit")
plt.legend()
plt.savefig("kinetics.png")