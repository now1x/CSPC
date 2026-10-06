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