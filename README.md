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