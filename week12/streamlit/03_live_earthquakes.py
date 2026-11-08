# Week 12, Streamlit Example 3: Live earthquakes
#
# Run this with:
#
#     uv run --extra notebooks streamlit run week12/streamlit/03_live_earthquakes.py
#
# What do you do when your data keeps changing? We pull the USGS earthquake
# feed, which updates every minute or so, and show it a couple of different
# ways.
#
# Your final project does *not* need live data. But if your dataset comes
# from an API that updates, this is how you'd handle it: a refresh button,
# or a fragment that re-runs itself on a timer. I'll show you both.
#
# Feed docs: https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php

import datetime

import altair as alt
import pandas as pd
import requests
import streamlit as st

st.set_page_config(page_title="Live Earthquakes", layout="wide")

FEEDS = {
    "Past hour": "all_hour",
    "Past day": "all_day",
    "Past week": "all_week",
}


# ttl = "time to live." After 5 minutes, the cache expires and the next run
# of the script will go fetch fresh data. This is a nice, polite way to not
# hammer somebody else's server every time a user moves a slider.
@st.cache_data(ttl=300)
def load_quakes(feed):
    url = f"https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/{feed}.geojson"
    data = requests.get(url, timeout=30).json()
    # GeoJSON! We've seen this before -- each "feature" has properties and a
    # geometry. Let's flatten it into a dataframe.
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
                "url": p["url"],
            }
        )
    fetched_at = datetime.datetime.now(datetime.timezone.utc)
    return pd.DataFrame(rows).dropna(subset=["mag"]), fetched_at


st.title("Live Earthquakes")

with st.sidebar:
    feed_name = st.radio("Time window", list(FEEDS), index=1)
    min_mag = st.slider("Minimum magnitude", -1.0, 7.0, 2.5, step=0.5)

    # Option 1: the refresh button. Clearing the cache means the next run
    # has to go fetch the data again.
    if st.button("Check for new data"):
        load_quakes.clear()

    # Option 2: actually live. See the fragment below.
    live = st.toggle("Auto-refresh every minute", value=False)


# A "fragment" is a piece of the app that can re-run *by itself*, without
# re-running the whole script. With run_every, it re-runs on a timer. This is
# the Streamlit version of what we were doing last week with vega-lite
# changesets -- new data comes in, the view updates.
@st.fragment(run_every="60s" if live else None)
def live_quakes():
    if live:
        load_quakes.clear()

    quakes, fetched_at = load_quakes(FEEDS[feed_name])
    quakes = quakes[quakes["mag"] >= min_mag]

    st.caption(f"Data fetched at {fetched_at:%Y-%m-%d %H:%M:%S} UTC")

    if quakes.empty:
        st.info("No earthquakes that big in this window. (Which is good news, really.)")
        return

    c1, c2, c3 = st.columns(3)
    c1.metric("Earthquakes", len(quakes))
    c2.metric("Largest", f"M {quakes['mag'].max():.1f}")
    c3.metric("Most recent", quakes["time"].max().strftime("%H:%M UTC"))

    # st.map is the fastest possible map. It is not the *best* map -- we
    # spent a whole week on projections! -- but for a first pass it's great.
    # st.map wants the *name* of a column for the dot size (in meters), so we
    # make one. Magnitude is logarithmic, so let's exaggerate it a bit.
    quakes = quakes.assign(dot_size=10_000 * 2 ** quakes["mag"].clip(lower=0))
    st.map(quakes, latitude="lat", longitude="lon", size="dot_size")

    left, right = st.columns(2)

    with left:
        st.write("**Magnitude distribution**")
        hist = (
            alt.Chart(quakes)
            .mark_bar()
            .encode(
                x=alt.X("mag:Q", bin=alt.Bin(step=0.5), title="Magnitude"),
                y=alt.Y("count():Q", title="Number of earthquakes"),
            )
        )
        st.altair_chart(hist, width="stretch")

    with right:
        st.write("**Magnitude vs. depth**")
        scatter = (
            alt.Chart(quakes)
            .mark_circle()
            .encode(
                x=alt.X("mag:Q", title="Magnitude"),
                y=alt.Y("depth:Q", title="Depth (km)", scale=alt.Scale(reverse=True)),
                tooltip=["place", "mag", "depth", "time"],
            )
        )
        st.altair_chart(scatter, width="stretch")

    st.write("**The ten biggest**")
    st.dataframe(
        quakes.nlargest(10, "mag")[["time", "place", "mag", "depth", "url"]],
        column_config={"url": st.column_config.LinkColumn("USGS page", display_text="details")},
        hide_index=True,
    )


live_quakes()
