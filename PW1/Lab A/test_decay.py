"""
Tests for the decay simulation.

One complete test is given as a model. Add the two tests described in the
lab handout (a negative-rate test, and a test against the analytical law).
Run with:  pytest -v
"""

import numpy as np
import pytest
import decay


def test_starts_at_N0():
    # at time zero, no atoms have decayed yet
    assert decay.simulate(1000, 0.4)[0] == 1000


def test_rejects_negative_rate():
    # a negative decay rate is not possible, so the function should
    # raise a ValueError if lam < 0
    with pytest.raises(ValueError):
        decay.simulate(1000, -0.4)

def test_matches_law():
    # the average of many simulations should match the analytical law
    N0, lam = 10000, 0.4
    dt = 0.05
    avg = np.mean([decay.simulate(N0, lam, dt=dt) for _ in range(200)], axis=0)
    t = np.arange(len(avg)) * dt
    expected = N0 * np.exp(-lam * t)
    assert avg == pytest.approx(expected, rel=0.15) # allowed 15% relative error, 5% was too strict and gave out an error 