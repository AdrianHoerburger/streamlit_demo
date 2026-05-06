import streamlit as st

st.title("Streamlit Demo App")
st.markdown("This is a simple Streamlit app to demonstrate its capabilities.")

st.header("Interactive Widgets")

name = st.text_input("Your name", placeholder="Enter your name")
if name:
    st.success(f"Hello, {name}!")

age = st.slider("Your age", min_value=1, max_value=100, value=25)
st.write(f"You are {age} years old.")

if st.button("Click me"):
    st.balloons()
    st.info("Button clicked!")

st.header("Data Example")

import pandas as pd
import numpy as np

data = pd.DataFrame(
    np.random.randn(10, 3),
    columns=["Column A", "Column B", "Column C"]
)
st.dataframe(data)
st.line_chart(data)
