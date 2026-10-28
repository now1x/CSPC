"""
PW2 Lab B Part 2 -- three routes to a minimum.

Compare gradient descent, Newton, and SLSQP on two functions:
  2A: f(x) = (x-3)**2 + 1          (easy, one minimum at x=3)
  2B: g(x) = x**4 - 3*x**2 + x + 5 (harder, several stationary points)
Run:  python warmup.py
"""
import numpy as np
from scipy.optimize import newton, minimize

def grad_descent(df, x0, lr=0.01):
    x = x0
    for _ in range(1000):
        step = lr * df(x)
        x -= step
        if abs(step) < 1e-6:
            break
    return x

# ---------- 2A: easy convex function ----------
def f(x):   return (x-3)**2 + 1
def df(x):  return 2*(x-3)
def d2f(x): return 2.0

# TODO 2A: minimise f three ways from x0=0 and print each result:
#   (1) gradient descent by hand (loop x = x - lr*df(x) until the step is tiny)
#   (2) scipy.optimize.newton(df, x0, fprime=d2f)
#   (3) scipy.optimize.minimize(f, x0, method="SLSQP")

x0=0

# gradient descent
x_gd = grad_descent(df, x0, lr=0.01)

# newton
x_nw = newton(df, x0, fprime=d2f)

#slsqp
x_sl = minimize(f, x0, method="SLSQP").x[0]

print("2A: f(x) = x**4 - 3*x**2 + x + 5")
print(f"gradient descent: x = {x_gd:.6f}")
print(f"newton: x = {x_nw:.6f}")
print(f"SLSQP: x = {x_sl:.6f}")

# ---------- 2B: harder landscape ----------
def g(x):   return x**4 - 3*x**2 + x + 5
def dg(x):  return 4*x**3 - 6*x + 1
def d2g(x): return 12*x**2 - 6

# TODO 2B: run the same three methods on g, from x0=0 AND from x0=2.
#   For Newton (which solves dg(x)=0), also check the sign of d2g at the answer:
#   d2g > 0 means a minimum, d2g < 0 means a maximum.
#   In your README note: do the methods agree? did Newton find a minimum or
#   another stationary point? how did the starting point change the result?

for x0 in (0.0,2.0):
    # gradient descent
    x_gd = grad_descent(dg, x0, lr=0.01)

    # newton
    x_nw = newton(dg, x0, fprime=d2g)

    #slsqp
    x_sl = minimize(g, x0, method="SLSQP").x[0]

    curvature = d2g(x_nw)
    if curvature > 0:
        point_type = "minimum"
    elif curvature < 0:
        point_type = "maximum"
    else:
        point_type = "inflection point"

    print(f"\n2B: g(x) = x**4 - 3*x**2 + x + 5, x0={x0}")
    print(f"gradient descent: x = {x_gd:.6f}")
    print(f"newton: x = {x_nw:.6f}, d2g={d2g(x_nw):.6f}"
          f" (g'' = {curvature:.6f} -> {point_type})")
    print(f"SLSQP: x = {x_sl:.6f}")