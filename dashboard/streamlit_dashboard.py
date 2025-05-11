import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="NIDS Dashboard", layout="wide")

st.title("Network Intrusion Detection System Dashboard")

# Placeholder for real-time alerts
alert_placeholder = st.empty()

# Load alerts from log file
if os.path.exists('logs/alerts.log'):
    with open('logs/alerts.log', 'r') as f:
        alerts = f.readlines()
    for alert in alerts[-10:]:  # Show last 10 alerts
        alert_placeholder.text(alert)
else:
    st.info("No alerts logged yet.")
