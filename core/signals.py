import numpy as np
from scipy.signal import sawtooth


def unit_impulse(t):
    formula = "y(t) = δ(t)"

    return np.where(np.isclose(t, 0), 1.0, 0.0), formula


def unit_step(t):
    formula = "y(t) = u(t)"

    return np.where(t >= 0, 1.0, 0.0), formula


def ramp(t):
    formula = "y(t) = t"

    return np.where(t >= 0, t, 0.0), formula


def exponential(t, a=1.0):
    formula = f"y(t) = {a}^t"

    return np.exp(a * t) * (t >= 0), formula


def sinusoid(t, amplitude=1.0, frequency=1.0, phase=0.0):
    formula = f"y(t) = {amplitude} * sin(2π * {frequency} * t + {phase})"

    return amplitude * np.sin(2 * np.pi * frequency * t + phase), formula


def rectangular_pulse(t, start=-1.0, end=1.0, amplitude=1.0):
    formula = f"y(t) = {amplitude}, for {start} ≤ t ≤ {end}; 0 otherwise"

    x = np.zeros_like(t)
    x[(t >= start) & (t <= end)] = amplitude
    return x, formula


def triangular_wave(t, start=0, end=1, amplitude=1.0):
    x = 1 - np.abs(2 * (t - start) / (end - start) - 1)
    x[x < 0] = 0
    formula = f"y(t) = "

    return x, formula


def time_axis(t_min, t_max, dt=None, num_points=1000):
    """
    Generate time axis from t_min to t_max.
    """
    if dt is not None:
        return np.arange(t_min, t_max + dt, dt)

    return np.linspace(t_min, t_max, num_points)


BASIC_SIGNALS = [
    "Unit Impulse",
    "Unit Step",
    "Ramp",
    "Sinusoidal",
    "Exponential",
    "Rectangular",
    "Triangular",
]
