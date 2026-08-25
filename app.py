"""Starter Streamlit app for Mitchell Site."""

import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Mitchell Site – Demo App", layout="wide")

st.title("Mitchell Site – Demo App")
st.write(
    "Welcome! This is a starter Streamlit application. "
    "Replace this content with your own research tools and visualizations."
)

st.sidebar.header("Settings")
num_points = st.sidebar.slider("Number of data points", min_value=50, max_value=500, value=200)

# Generate sample data
rng = np.random.default_rng(42)
df = pd.DataFrame(
    {
        "x": rng.standard_normal(num_points),
        "y": rng.standard_normal(num_points),
        "category": rng.choice(["A", "B", "C"], size=num_points),
    }
)

st.subheader("Sample Scatter Plot")
st.scatter_chart(df, x="x", y="y", color="category")

st.subheader("Data Preview")
st.dataframe(df.head(10), use_container_width=True)
