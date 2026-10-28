"""
PW2 Lab B Part 4 -- chemical equilibrium via the equilibrium constant K.

Reaction  H2 + I2 <=> 2 HI, starting from 1 mol H2 and 1 mol I2.
As the reaction proceeds by an extent x:  H2 = 1-x,  I2 = 1-x,  HI = 2x.
At equilibrium the composition satisfies the equilibrium constant
        K = [HI]^2 / ([H2][I2]) = (2x)^2 / ((1-x)(1-x)).
Given K, find the extent x. Solve it TWO ways and compare.
Run:  python equilibrium.py
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import newton, minimize

K = 15.6
a = b = 1.0

# TODO 1: write k_imbalance(x) = (2x)^2/((a-x)(b-x)) - K.
#         It equals zero exactly at equilibrium.
def k_imbalance(x):
        return (2*x)**2 / ((a-x)*(b-x)) - K

# TODO 2 (method 1): use scipy.optimize.newton to find the root of k_imbalance
#         (start x0=0.5). This is root-finding.
x_newton = newton(k_imbalance, x0=0.5)

# TODO 3 (method 2): use scipy.optimize.minimize to minimise k_imbalance(x)**2
#         (method "SLSQP", bounds [(0, 0.999)], x0=[0.5]). Print both answers
#         and confirm they agree.
def k_sqr(x):
    return k_imbalance(x)**2

x_minimize = minimize(k_sqr, x0=0.5, method="SLSQP", bounds=[(0, 0.999)]).x[0]


print(f"equilibrium extent (newton): {x_newton}")
print(f"equilibrium extent (minimize): {x_minimize}")



# TODO 4: report the equilibrium amounts (H2, I2, HI), and plot how the three
#         amounts change with the extent x, marking the equilibrium. Save
#         equilibrium.png.
h2 = a - x_minimize
i2 = b - x_minimize
hi = 2 * x_minimize
print(f"equilibrium amounts: H2={h2}, I2={i2}, HI={hi}")

x_values = np.linspace(0, 0.99, 200)
h2_values = a - x_values
i2_values = b - x_values
hi_values = 2 * x_values

fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(x_values, h2_values, label="H2")
ax.plot(x_values, i2_values, label="I2")
ax.plot(x_values, hi_values, label="HI")
ax.axvline(x_minimize, color='red', linestyle='--', label='equilibrium extent')
ax.set_xlabel("extent of reaction x")
ax.set_ylabel("amount (mol)")
ax.set_title("Chemical Equilibrium")
ax.legend()
fig.tight_layout()
fig.savefig("equilibrium.png")