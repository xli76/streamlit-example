import streamlit as st
from data.dataset import get_data
from common.chart import get_chart

st.title("⬇ Time series annotations")
st.sidebar.markdown("# Page 1 ❄️")

def space(num_lines=1):
    """Adds empty lines to the Streamlit app."""
    for _ in range(num_lines):
        st.write("")

space(1)

source = get_data()
chart = get_chart(source)

st.altair_chart(chart, use_container_width=True)