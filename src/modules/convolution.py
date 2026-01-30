import numpy as np
import streamlit as st

from src.core.signals import (
    BASIC_SIGNALS,
    exponential,
    ramp,
    rectangular_pulse,
    sinusoid,
    time_axis,
    triangular_wave,
    unit_impulse,
    unit_step,
)
from src.ui.plots import plot_signal


def generate_signal_ui(
    t, parent_col, signal_label, signal_types, default_values=None, key_prefix="sig"
):
    """
    Render signal selection, parameters, and return signal & formula.
    parent_col : column where the widgets appear
    signal_label : str, e.g., "Input Signal 1"
    signal_types : list of signal options
    default_values : dict for default params
    key_prefix : unique key prefix to avoid duplicate ID
    """
    with parent_col:
        st.markdown(
            f"<h4 style='margin:0 0 5px 0;'>{signal_label}</h4>", unsafe_allow_html=True
        )

        signal_type = st.selectbox(
            f"Select {signal_label}",
            signal_types,
            key=f"{key_prefix}_type",
            label_visibility="collapsed",
        )

        # Default values
        defaults = default_values or {}

        # Generate signal & formula
        if signal_type == "Sinusoidal":
            amp_col, freq_col, phase_col = parent_col.columns(3)
            with amp_col:
                amplitude = st.number_input(
                    "Amplitude",
                    value=defaults.get("amplitude", 1.0),
                    step=0.1,
                    key=f"{key_prefix}_amp",
                )
            with freq_col:
                frequency = st.number_input(
                    "Frequency (Hz)",
                    value=defaults.get("frequency", 1.0),
                    step=0.1,
                    key=f"{key_prefix}_freq",
                )
            with phase_col:
                phase = st.number_input(
                    "Phase (rad)",
                    value=defaults.get("phase", 0.0),
                    step=0.1,
                    key=f"{key_prefix}_phase",
                )

            x, formula = sinusoid(t, amplitude, frequency, phase)

        elif signal_type == "Unit Impulse":
            x, formula = unit_impulse(t)

        elif signal_type == "Unit Step":
            x, formula = unit_step(t)

        elif signal_type == "Ramp":
            x, formula = ramp(t)

        elif signal_type == "Rectangular":
            start_col, end_col, amp_col = parent_col.columns(3)
            with start_col:
                start = st.number_input(
                    "Start time",
                    value=defaults.get("start", -1.0),
                    step=0.1,
                    key=f"{key_prefix}_start",
                )
            with end_col:
                end = st.number_input(
                    "End time",
                    value=defaults.get("end", 1.0),
                    step=0.1,
                    key=f"{key_prefix}_end",
                )
            with amp_col:
                amplitude = st.number_input(
                    "Amplitude",
                    value=defaults.get("amplitude", 1.0),
                    step=0.1,
                    key=f"{key_prefix}_amp",
                )

            x, formula = rectangular_pulse(t, start, end, amplitude)

        elif signal_type == "Exponential":
            alpha = st.number_input(
                "Exponential alpha",
                value=defaults.get("alpha", np.e),
                step=0.05,
                key=f"{key_prefix}_alpha",
            )
            x, formula = exponential(t, alpha)

        elif signal_type == "Triangular":
            start_col, end_col, amp_col = parent_col.columns(3)

            with start_col:
                start = st.number_input(
                    "Start time", value=0.0, step=0.1, key=f"{key_prefix}_tri_start"
                )

            with end_col:
                end = st.number_input(
                    "End time", value=1.0, step=0.1, key=f"{key_prefix}_tri_end"
                )

            with amp_col:
                amplitude = st.number_input(
                    "Amplitude", value=1.0, step=0.1, key=f"{key_prefix}_tri_amplitude"
                )

            x, formula = triangular_wave(t, start=start, end=end, amplitude=amplitude)

        st.markdown("<div style='margin-top:20px'></div>", unsafe_allow_html=True)
        # Plot
        st.plotly_chart(
            plot_signal(
                t, x, title=formula, color="green" if "1" in signal_label else "blue"
            ),
            use_container_width=True,
        )

        return x, formula


def run_convolution_module():
    st.header("Convolution Operation")
    st.markdown(
        """
        **Definition:** Convolution is a mathematical operation that expresses the output of a system
        in terms of its input signal and impulse response.

        **Continuous-time formula:** $y(t) = \\int_{-\\infty}^{\\infty} x(\\tau) h(t-\\tau) d\\tau$

        **Discrete-time formula:** $y[n] = \\sum_{k=-\\infty}^{\\infty} x[k] h[n-k]$
        """
    )
    st.markdown("----")

    # Time axis
    t = time_axis(0, 1, dt=0.1)
    dt = t[1] - t[0]

    col1, col2 = st.columns(2)

    # Input Signal 1
    x1, _ = generate_signal_ui(
        t, col1, "Input Signal 1", BASIC_SIGNALS, key_prefix="sig1"
    )

    # Input Signal 2
    x2, _ = generate_signal_ui(
        t, col2, "Input Signal 2", BASIC_SIGNALS, key_prefix="sig2"
    )

    st.markdown("----")

    # Compute convolution
    y = np.convolve(x1, x2, mode="full") * dt

    st.markdown("### Output Signal (Convoluted)")
    st.markdown("<div style='margin-top:20px'></div>", unsafe_allow_html=True)
    st.plotly_chart(
        plot_signal(t, y, title="y(t) = signal1 * singal2"),
        use_container_width=True,
    )
