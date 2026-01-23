import streamlit as st
from modules.signals import run_signals_module
from modules.basic_operations import run_basic_operations_module

st.set_page_config(layout="wide", page_title="CS Viz", menu_items={})
st.sidebar.markdown("## Communication Systems Viz")
st.sidebar.markdown("---")

signal_topic = st.sidebar.selectbox(
    "Signal Analysis", ["Signal Foundations", "Signal Operations"], key="signal_analysis"
)

if signal_topic == "Signal Foundations":
    run_signals_module()
elif signal_topic == "Signal Operations":
    run_basic_operations_module()
