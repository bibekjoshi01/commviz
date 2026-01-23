import streamlit as st
import numpy as np
from core.signals import (
    time_axis,
    unit_impulse,
    unit_step,
    ramp,
    exponential,
    sinusoid,
)
from core.basic_operations import (
    time_shift,
    time_scale,
    time_reverse,
    amplitude_scale,
)
from ui.plots import plot_signal


def run_basic_operations_module():
    st.subheader("Operations on Signals")

    signal_mode = st.radio("Signal Mode", ("Continuous", "Discrete"), horizontal=True)

    col1, col2 = st.columns(2)
    with col1:
        t_min = st.number_input("Start Time", value=-1.0, step=0.1, format="%.5f")
    with col2:
        t_max = st.number_input("End Time", value=1.0, step=0.1, format="%.5f")
    if t_min >= t_max:
        st.warning("Start time must be less than end time.")
        return

    signal_type = st.selectbox(
        "Select Signal",
        ["Unit Impulse", "Unit Step", "Ramp", "Exponential", "Sinusoidal"],
    )

    # Generate base signal
    if signal_mode == "Discrete":
        t = np.arange(t_min, t_max, (t_max - t_min) / 50)
    else:
        t = time_axis(t_min, t_max)

    if signal_type == "Unit Impulse":
        x = unit_impulse(t)
    elif signal_type == "Unit Step":
        x = unit_step(t)
    elif signal_type == "Ramp":
        x = ramp(t)
    elif signal_type == "Exponential":
        a = st.slider("Exponential Constant (a)", -5.0, 5.0, 1.0, 0.1)
        x = exponential(t, a)
    elif signal_type == "Sinusoidal":
        amplitude = st.slider("Amplitude", 0.1, 5.0, 1.0, 0.1)
        frequency = st.slider("Frequency (Hz)", 0.1, 10.0, 1.0, 0.1)
        phase = st.slider("Phase (rad)", -np.pi, np.pi, 0.0, 0.1)
        x = sinusoid(t, amplitude, frequency, phase)

    st.markdown("### Signal Transformations")
    col1, col2 = st.columns(2)
    with col1:
        shift = st.number_input("Time Shift", value=0.0, step=0.1)
        scale = st.number_input("Time Scale", value=1.0, step=0.1, min_value=0.01)
    with col2:
        reverse = st.checkbox("Time Reverse")
        amp_scale = st.number_input("Amplitude Scale", value=1.0, step=0.1)

    # Apply operations
    t_new, x_new = t.copy(), x.copy()
    t_new, x_new = time_shift(x_new, t_new, shift)
    t_new, x_new = time_scale(x_new, t_new, scale)
    if reverse:
        t_new, x_new = time_reverse(x_new, t_new)
    x_new = amplitude_scale(x_new, amp_scale)

    # Plot original and transformed signals
    st.plotly_chart(
        plot_signal(
            t, x, title="Original Signal", discrete=(signal_mode == "Discrete")
        ),
        width='stretch',
    )
    st.plotly_chart(
        plot_signal(
            t_new,
            x_new,
            title="Transformed Signal",
            discrete=(signal_mode == "Discrete"),
        ),
        width='stretch',
    )
