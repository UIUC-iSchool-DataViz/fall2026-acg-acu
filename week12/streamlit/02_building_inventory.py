# Week 12, Streamlit Example 2: Our old friend, the building inventory
#
# Run this with:
#
#     uv run --extra notebooks streamlit run week12/streamlit/02_building_inventory.py
#
# This is the same kind of dashboard we built with bqplot -- a couple of
# controls, a couple of linked views -- but in Streamlit. A few things to
# watch for:
#
#   * @st.cache_data, so we don't re-read the CSV every time a slider moves
#   * the sidebar for our controls
#   * an Altair chart with a *selection*, and using that selection to drive
#     another view (linking and brushing!)

import pathlib

import altair as alt
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Illinois Building Inventory", layout="wide")

# If you're running this from inside the course repo, we use the local copy.
# If you've copied this file somewhere else (like a HuggingFace Space!) we'll
# grab it from the course website instead.
LOCAL_DATA = pathlib.Path(__file__).parents[2] / "data" / "building_inventory.csv"
REMOTE_DATA = "https://uiuc-ischool-dataviz.github.io/fall2026-acg-acu/data/building_inventory.csv"


# Remember: the whole script re-runs every time somebody touches a widget.
# Without this decorator, we'd be reading ~9,000 rows off disk every single
# time. With it, we read it once and Streamlit hands us back the same thing.
@st.cache_data
def load_data():
    source = LOCAL_DATA if LOCAL_DATA.exists() else REMOTE_DATA
    df = pd.read_csv(source)
    # Same cleaning as always: a year of 0 means "we don't know."
    df = df[(df["Year Acquired"] > 0) & (df["Year Constructed"] > 0)]
    return df


df = load_data()

st.title("Illinois State Building Inventory")
st.write(
    "Every building the state of Illinois owns, when it was built, and how big it is. "
    "Use the sidebar to filter, and drag across the scatter plot to select some buildings."
)

# --- Controls -------------------------------------------------------------

st.sidebar.header("Filters")

# Defaulting to the top few agencies so the plot isn't an unreadable rainbow.
agencies = df["Agency Name"].value_counts().index.tolist()
chosen_agencies = st.sidebar.multiselect(
    "Agencies", agencies, default=agencies[:4]
)

min_year, max_year = int(df["Year Constructed"].min()), int(df["Year Constructed"].max())
year_range = st.sidebar.slider(
    "Year constructed", min_year, max_year, (1900, max_year)
)

statuses = st.sidebar.multiselect(
    "Building status", df["Bldg Status"].unique().tolist(), default=["In Use"]
)

filtered = df[
    df["Agency Name"].isin(chosen_agencies)
    & df["Year Constructed"].between(*year_range)
    & df["Bldg Status"].isin(statuses)
]

if filtered.empty:
    st.warning("Nothing matches those filters! Try loosening them up a bit.")
    st.stop()  # st.stop() ends this run of the script right here.

# --- Summary numbers ------------------------------------------------------

c1, c2, c3 = st.columns(3)
c1.metric("Buildings", f"{len(filtered):,}")
c2.metric("Total square footage", f"{filtered['Square Footage'].sum():,.0f}")
c3.metric("Median year built", int(filtered["Year Constructed"].median()))

# --- Linked views ---------------------------------------------------------

# This is vega-lite under the hood -- the same interval selection we made
# by hand a few weeks ago, just written in Python.
brush = alt.selection_interval(name="brush", encodings=["x"])

scatter = (
    alt.Chart(filtered)
    .mark_circle(opacity=0.5)
    .encode(
        x=alt.X("Year Constructed:Q", scale=alt.Scale(zero=False)),
        y=alt.Y("Square Footage:Q", scale=alt.Scale(type="log")),
        color="Agency Name:N",
        tooltip=["Location Name", "Agency Name", "Year Constructed", "Square Footage"],
    )
    .add_params(brush)
    .properties(height=400)
)

# on_select="rerun" means: when the selection changes, re-run the script and
# hand us the selection. This is how we get *Python* to react to something
# the user did *inside* the vega-lite chart.
event = st.altair_chart(scatter, on_select="rerun", width="stretch")

selection = event.selection.get("brush", {})
if "Year Constructed" in selection:
    lo, hi = selection["Year Constructed"]
    selected = filtered[filtered["Year Constructed"].between(lo, hi)]
    st.subheader(f"Built between {lo:.0f} and {hi:.0f}")
else:
    selected = filtered
    st.subheader("All filtered buildings (drag on the plot above to narrow it down)")

left, right = st.columns(2)

with left:
    st.write("**Square footage by agency**")
    by_agency = (
        selected.groupby("Agency Name")["Square Footage"].sum().sort_values(ascending=False)
    )
    st.bar_chart(by_agency, horizontal=True)

with right:
    st.write("**The biggest ones**")
    st.dataframe(
        selected.nlargest(15, "Square Footage")[
            ["Location Name", "City", "Year Constructed", "Square Footage"]
        ],
        hide_index=True,
    )
