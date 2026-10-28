# CSPC - Computer Science for Physics and Chemistry

My coursework repository. Each practical is under PW<n>/Lab <X>/.

## Setup
Create the environment for a given lab:
conda env create -f PW<n>/Lab\ <X>/environment.yml
conda activate cspc

---

## PW1 - Lab A: Reproducible Foundations
**What I built:**
- Managed a reproducible conda environment and organized a clean repo structure.
- Added automated `pytest` checks to keep everything stable.
- Built a radioactive decay simulation, benchmarking a standard Python loop against a vectorized NumPy version with some guidance from Gemini AI, which helped me review some errors when using pytest.

**Speed comparison (loop vs NumPy):**
- loop : 0.2673 s
- numpy : 0.0002 s
- speed-up: 1278.76x faster

**Tests:** all passed (yes)

**Conclusion:**
- Switching to NumPy makes a massive difference by completely destroying Python in a speed competition. Dealing with variance in the unit tests took a bit of time to correct, but everything passes cleanly and proves the mathematical model holds up.

---

## PW1 - Lab B: Data, Plotting, and Automation
**What I built:**
- Wrote a data-analysis script (`plot.py`) to break down the observed decay data and put together a clean 1x2 subplot comparing the practical scatter points straight up against the theoretical curve.
- Set up a `Snakefile` to automate the whole figure-generation pipeline so it only reruns when something actually changes.

**Results & Observations:**
- **Data check:** The messy real-world measurements match the expected $N_0 e^{-\lambda t}$ exponential decay pattern ($\lambda = 0.3$) really well.
- **Visual match:** Having both panels share the same axes makes it super obvious that the physical data lines up right with the math model.

**Pipeline Automation:**
- Snakemake handles the file tracking smoothly - if nothing's edited, it skips unnecessary work, but the second you modify the script or data, it instantly rebuilds the figure.

---

## PW2 - Lab A: Motion from Tracking Data
**What I built:**
- Wrote an analysis script (`analysis.py`) that reads noisy free-fall position data and uses `np.gradient` twice to get velocity and then acceleration.
- Integrated the noisy acceleration back up with `cumulative_trapezoid` to recover velocity and position.
- Made a 3-panel figure (`motion.png`) with position, velocity and acceleration sharing the time axis, with a dashed line at -9.81 m/s² on the acceleration panel.

**Results & Observations:**
- **Mean acceleration:** -8.58 m/s², pretty close to the expected -9.81, so the object really is in free fall.
- **Noise:** the standard deviation of the acceleration was 28.72 m/s², huge compared to the mean.
- **Why so noisy:** a derivative compares neighbouring points, so the small errors in the position get magnified every time you differentiate. I differentiated twice, while the position itself never was, so it stays smooth.
- **Integrating back:** the recovered position was within 0.78 m of the original (largest difference), even though the acceleration was so noisy.

**Conclusion:**
- Differentiation amplifies noise and integration suppresses it, because random errors partly cancel out when you add things up. The three panels show it well: smooth position, slightly rough velocity, very noisy acceleration.

---

## PW2 - Lab B: Optimization in Chemistry
**What I built:**
- `warmup.py`: compared gradient descent, Newton and SLSQP on an easy and a harder function.
- `kinetics.py`: fitted the rate constant of a first-order reaction by minimising the squared error between the model and the data.
- `equilibrium.py`: solved for the equilibrium extent of H2 + I2 ⇌ 2 HI with Newton (root-finding) and SLSQP (minimisation).
- `titration.py` (bonus): found the equivalence point as the volume where the slope of the pH curve is largest.

**Comparing the three methods:**
- **Easy function** f(x) = (x-3)² + 1: all three methods gave x = 3, so no difference.
- **Harder function** g(x) = x⁴ - 3x² + x + 5, from x0 = 0: Newton gave x = 0.17, but g'' there is -5.65 (negative), so it is a maximum and not a minimum. Gradient descent and SLSQP found the real minimum at x = -1.30.
- **Harder function, from x0 = 2:** gradient descent and Newton got stuck in a local minimum at x = 1.13, while SLSQP still found the lowest one at x = -1.30.
- So the methods don't always agree, and the starting point changes the result.

**Chemistry results:**
- **Rate constant:** k = 0.262, close to the expected 0.25, and the fitted curve goes through the data points (`kinetics.png`).
- **Equilibrium:** Newton and SLSQP both gave x = 0.664, so H2 = 0.336 mol, I2 = 0.336 mol and HI = 1.328 mol (`equilibrium.png`).
- **Titration:** the equivalence point is at 50.0 mL (pH 7.00), where the slope of the pH curve peaks (`titration.png`).

**Conclusion:**
- On a simple convex problem every method works, but on a complicated landscape the starting point and the algorithm matter. Optimisation also turned out to be useful for real chemistry problems like fitting a rate constant and finding an equilibrium.