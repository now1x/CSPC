import time
import decay

N0 = 20000 # number of atoms
lam = 0.4 # lambda, the decay rate
dt = 0.05 # time step
steps = 200 # simulation steps

#Python loop version

start_loop = time.perf_counter()
decay.simulate_loop(N0, lam, dt=dt, steps=steps)
end_loop = time.perf_counter()
time_loop = end_loop - start_loop
print(f"Python loop version took {time_loop:.4f} seconds")

#NumPy version

start_numpy = time.perf_counter()
decay.simulate(N0, lam, dt=dt, steps=steps)
end_numpy = time.perf_counter()
time_numpy = end_numpy - start_numpy
print(f"NumPy version took {time_numpy:.4f} seconds")

time_ratio = time_loop / time_numpy #how many times faster is the NumPy version
print(f"NumPy version is {time_ratio:.2f} times faster than Python loop version")