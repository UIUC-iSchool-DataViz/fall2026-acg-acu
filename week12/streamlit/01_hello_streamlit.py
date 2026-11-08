# Week 12, Streamlit Example 1: Hello, Streamlit
#
# Run this with:
#
#     uv run --extra notebooks streamlit run week12/streamlit/01_hello_streamlit.py
#
# (or just `streamlit run 01_hello_streamlit.py` if you have streamlit installed)
#
# The big idea: a Streamlit app is just a Python script. Every time somebody
# touches a widget, Streamlit re-runs the *whole script*, top to bottom, and
# whatever the widget returns is just a regular Python value. No callbacks,
# no `observe`, no linking widgets to traitlets like we did with bqplot and
# ipywidgets.

import numpy as np
import pandas as pd
import streamlit as st

st.title("Hello, Streamlit!")

# st.write is kind of the "do what I mean" function -- strings become
# markdown, dataframes become tables, charts become charts.
st.write("This is a Streamlit app. It is *also* just a Python script.")

# Widgets return values. That's it. That's the trick.
n_points = st.slider("How many points?", min_value=10, max_value=1000, value=100)
noise = st.slider("How noisy?", min_value=0.0, max_value=2.0, value=0.5)

st.write(f"You asked for **{n_points}** points with a noise level of **{noise}**.")

# Every time you move a slider, this gets re-generated. Watch the numbers
# change even if you don't move the slider -- try hitting "R" to rerun.
x = np.linspace(0, 4 * np.pi, n_points)
df = pd.DataFrame({"x": x, "y": np.sin(x) + np.random.normal(0, noise, n_points)})

# The built-in charts are quick and dirty -- great for "viz for self."
st.line_chart(df, x="x", y="y")

# Want to see the raw data? Checkboxes return True/False.
if st.checkbox("Show me the data"):
    st.dataframe(df)

# A little bit of layout: columns and the sidebar.
st.sidebar.header("About")
st.sidebar.write("Anything you put in `st.sidebar` ends up over here.")

left, right = st.columns(2)
left.metric("Mean of y", f"{df['y'].mean():.3f}")
right.metric("Std. dev. of y", f"{df['y'].std():.3f}")

# Because the script re-runs every time, regular variables get reset. If you
# want something to stick around between reruns, it goes in st.session_state.
if "clicks" not in st.session_state:
    st.session_state.clicks = 0

if st.button("Click me"):
    st.session_state.clicks += 1

st.write(f"You've clicked the button {st.session_state.clicks} times.")
