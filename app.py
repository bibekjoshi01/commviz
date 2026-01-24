import streamlit as st
from modules.basic_operations import run_basic_operations_module
from modules.energy_power_signals import run_energy_power_module
from modules.signals import run_signals_module

st.set_page_config(layout="wide", page_title="CS Viz", menu_items={})
st.sidebar.markdown("## Comm. Systems Visualizer")
st.sidebar.markdown("---")

signal_topic = st.sidebar.radio(
    "Signal Analysis",
    [
        "Signal Fundamentals",
        "Basic Signal Operations",
        "Energy and Power Signals",
        "Convolution",
    ],
    key="signal_analysis",
)

if signal_topic == "Signal Fundamentals":
    run_signals_module()
if signal_topic == "Basic Signal Operations":
    run_basic_operations_module()
if signal_topic == "Energy and Power Signals":
    run_energy_power_module()
