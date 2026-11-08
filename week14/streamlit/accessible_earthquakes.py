# Week 14: *Accessible* live earthquakes
#
# Run this with:
#
#     uv run --extra notebooks streamlit run week14/streamlit/accessible_earthquakes.py
#
# This is the earthquake app from week 12 (week12/streamlit/03_live_earthquakes.py),
# redone with accessibility in mind. Open them side by side and compare!
# What changed:
#
#   1. Every chart goes through maidr's `render_maidr`, so it can be explored
#      by keyboard, as text, as sound, and in braille.
#   2. There's a written summary, generated from the data, *before* the
#      charts. Somebody who can't see the charts gets the main point first.
#   3. The data is available as a table.
#   4. Color is never the only way to read anything.
#   5. Auto-refresh is off by default, and when it's on, we say so. Content
#      that changes by itself is really disorienting with a screen reader.
#   6. The map (which a screen reader can't do anything with) is described
#      in words, and the "where" is in the table.

import datetime

import altair as alt
import pandas as pd
import requests
import streamlit as st
from maidr.widget.streamlit import render_maidr

st.set_page_config(page_title="Accessible Live Earthquakes", layout="wide")

FEEDS = {"Past hour": "all_hour", "Past day": "all_day", "Past week": "all_week"}


@st.cache_data(ttl=300)
def load_quakes(feed):
    url = f"https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/{feed}.geojson"
    data = requests.get(url, timeout=30).json()
    rows = []
    for f in data["features"]:
        lon, lat, depth = f["geometry"]["coordinates"]
        p = f["properties"]
        rows.append(
            {
                "time": pd.to_datetime(p["time"], unit="ms", utc=True),
                "place": p["place"],
                "mag": p["mag"],
                "depth": depth,
                "lat": lat,
                "lon": lon,
            }
        )
    fetched_at = datetime.datetime.now(datetime.timezone.utc)
    return pd.DataFrame(rows).dropna(subset=["mag"]), fetched_at


def describe(quakes, window):
    """Write the main point in words. This is the most important accessibility
    feature on the page -- everybody reads this, and it works everywhere."""
    biggest = quakes.loc[quakes["mag"].idxmax()]
    strong = (quakes["mag"] >= 4.5).sum()
    text = (
        f"In the {window.lower()}, there were **{len(quakes)} earthquakes** at or above "
        f"the magnitude you selected. The largest was **magnitude {biggest['mag']:.1f}**, "
        f"{biggest['place']}, at a depth of {biggest['depth']:.0f} km. "
    )
    if strong:
        text += f"{strong} of them were magnitude 4.5 or larger. "
    text += f"The median magnitude was {quakes['mag'].median():.1f}."
    return text


st.title("Accessible Live Earthquakes")
st.write(
    "Live earthquake data from the U.S. Geological Survey. Every chart on this page "
    "can be explored with the keyboard: Tab to a chart, then use the arrow keys. "
    "Press T for text, S for sound, B for braille, and Control + slash "
    "(Command + slash on a Mac) for all the keyboard shortcuts."
)

with st.sidebar:
    # Every widget gets a real, descriptive label. A screen reader reads the
    # label, so "Window" alone wouldn't tell anybody much.
    window = st.radio("Time window to show", list(FEEDS), index=1)
    min_mag = st.slider("Minimum magnitude to include", -1.0, 7.0, 2.5, step=0.5)

    if st.button("Check for new data"):
        load_quakes.clear()

    live = st.toggle(
        "Automatically check for new data every minute",
        value=False,
        help="Off by default: content that changes on its own can be disorienting, "
        "especially with a screen reader.",
    )


@st.fragment(run_every="60s" if live else None)
def live_quakes():
    if live:
        load_quakes.clear()

    quakes, fetched_at = load_quakes(FEEDS[window])
    quakes = quakes[quakes["mag"] >= min_mag]

    status = f"Data fetched at {fetched_at:%H:%M} UTC."
    if live:
        status += " This page checks for new data every minute."
    st.caption(status)

    if quakes.empty:
        st.info(f"No earthquakes of magnitude {min_mag} or larger in the {window.lower()}.")
        return

    # 1. Words first.
    st.subheader("Summary")
    st.markdown(describe(quakes, window))

    # 2. Charts, via maidr.
    left, right = st.columns(2)

    with left:
        st.subheader("How big were they?")
        hist = (
            alt.Chart(quakes)
            .mark_bar()
            .encode(
                x=alt.X("mag:Q", bin=alt.Bin(step=0.5), title="Magnitude"),
                y=alt.Y("count():Q", title="Number of earthquakes"),
            )
            .properties(title="Earthquakes by magnitude")
        )
        render_maidr(hist)

    with right:
        st.subheader("Bigger earthquakes, deeper?")
        scatter = (
            alt.Chart(quakes)
            .mark_point(filled=True)
            .encode(
                x=alt.X("mag:Q", title="Magnitude"),
                y=alt.Y("depth:Q", title="Depth (km)"),
            )
            .properties(title="Magnitude and depth of each earthquake")
        )
        render_maidr(scatter)

    # 3. The map, described -- and the "where" lives in the table.
    st.subheader("Where were they?")
    regions = quakes["place"].str.split(", ").str[-1].value_counts().head(3)
    st.markdown(
        "The places with the most earthquakes in this window were "
        + ", ".join(f"{region} ({count})" for region, count in regions.items())
        + f", out of {len(quakes)} total. The full list, with locations, is in the "
        "table below."
    )
    st.map(quakes, latitude="lat", longitude="lon")

    # 4. The data itself.
    with st.expander("Data table: every earthquake shown on this page"):
        st.dataframe(
            quakes.sort_values("mag", ascending=False)[["time", "place", "mag", "depth"]],
            column_config={
                "time": st.column_config.DatetimeColumn("Time (UTC)"),
                "place": "Location",
                "mag": st.column_config.NumberColumn("Magnitude", format="%.1f"),
                "depth": st.column_config.NumberColumn("Depth (km)", format="%.0f"),
            },
            hide_index=True,
        )


live_quakes()
