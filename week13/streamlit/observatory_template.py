# Week 13: An observatory template for your final project
#
# Run this with:
#
#     uv run --extra notebooks streamlit run week13/streamlit/observatory_template.py
#
# This is a skeleton you can copy for Part Three. It runs as-is, using
# weather forecasts from Open-Meteo (free, no API key), but it's meant to be
# gutted and filled with *your* data. Look for the "CHANGE THIS" comments.
#
# The structure is the "martini glass" from week 12:
#
#   * The Story   -- you lead: a summary in words, and one or two annotated charts
#   * Explore     -- then you let go: controls and charts to poke at
#   * Data        -- the table, and a download button
#   * About       -- where the data comes from, how it updates, who made it
#
# And it bakes in what we'll talk about on November 30: words first, charts
# that work with maidr, real labels, and no surprise auto-refreshing.

import datetime

import altair as alt
import pandas as pd
import requests
import streamlit as st
from maidr.widget.streamlit import render_maidr
from streamlit.errors import StreamlitSecretNotFoundError

# --- CHANGE THIS: what is your observatory? -------------------------------

TITLE = "Central Illinois Weather Observatory"
SOURCE = "[Open-Meteo](https://open-meteo.com/) weather forecast API (CC BY 4.0)"
AUTHORS = "Your group's names here"

PLACES = {
    "Champaign": (40.11, -88.24),
    "Chicago": (41.88, -87.63),
    "Springfield": (39.80, -89.64),
    "Carbondale": (37.73, -89.22),
}

VARIABLES = {
    # API name: (readable label, units)
    "temperature_2m": ("Temperature", "°F"),
    "precipitation_probability": ("Chance of precipitation", "%"),
    "wind_speed_10m": ("Wind speed", "mph"),
}

st.set_page_config(page_title=TITLE, layout="wide")


# --- API keys --------------------------------------------------------------
#
# Open-Meteo doesn't need a key, but a lot of APIs do. NEVER put a key in
# your code -- your repo is public! Instead:
#
#   * Locally: put it in .streamlit/secrets.toml (which is in .gitignore):
#         MY_API_KEY = "abc123"
#   * On Streamlit Community Cloud: paste the same thing into your app's
#     Settings -> Secrets.
#
# Then read it like this:
def get_api_key():
    try:
        return st.secrets["MY_API_KEY"]
    except (StreamlitSecretNotFoundError, KeyError):
        return None


# --- CHANGE THIS: loading your data ----------------------------------------
#
# Whatever your data is, try to end up with a tidy dataframe: one row per
# observation, one column per variable. Keep the ttl so you're polite to
# whoever is serving your data.
@st.cache_data(ttl=600)
def load_data(lat, lon):
    response = requests.get(
        "https://api.open-meteo.com/v1/forecast",
        params={
            "latitude": lat,
            "longitude": lon,
            "hourly": ",".join(VARIABLES),
            "temperature_unit": "fahrenheit",
            "wind_speed_unit": "mph",
            "timezone": "America/Chicago",
            "past_days": 2,
            "forecast_days": 3,
        },
        timeout=30,
    )
    response.raise_for_status()  # Fail loudly if the API is down.
    df = pd.DataFrame(response.json()["hourly"])
    df["time"] = pd.to_datetime(df["time"])
    fetched_at = datetime.datetime.now(datetime.timezone.utc)
    return df, fetched_at


def when(t):
    """Format a time like 'Tuesday at 3 PM'. (We do this by hand because the
    strftime code for an hour without a leading zero doesn't work on Windows.)"""
    hour = t.hour % 12 or 12
    return f"{t:%A} at {hour} {'AM' if t.hour < 12 else 'PM'}"


# --- Controls ---------------------------------------------------------------

with st.sidebar:
    place = st.selectbox("Location", list(PLACES))
    if st.button("Check for new data"):
        load_data.clear()

df, fetched_at = load_data(*PLACES[place])

# Where does "now" fall in the data? Everything before it is the past two
# days; everything after is the forecast.
now = pd.Timestamp.now(tz="America/Chicago").tz_localize(None)
df["period"] = df["time"].map(lambda t: "Past two days" if t <= now else "Forecast")

# A readable time label, like "Tue 3 PM". Why? maidr reads a regular
# time axis out loud as a raw number of milliseconds ("time is
# 1,793,952,000,000") -- not very helpful! A text label on an ordinal axis
# gets read as "Time is Tue 3 PM." Check what your charts *sound* like!
df["when"] = df["time"].map(lambda t: f"{t:%a} {t.hour % 12 or 12} {'AM' if t.hour < 12 else 'PM'}")
every_12_hours = list(df["when"][::12])
current = df[df["time"] <= now].iloc[-1]
future = df[df["time"] > now]

st.title(TITLE)
st.caption(f"Data from {SOURCE}, fetched at {fetched_at:%H:%M} UTC.")

story, explore, data, about = st.tabs(["The Story", "Explore", "Data", "About"])

# --- The Story --------------------------------------------------------------

with story:
    # CHANGE THIS: the main point, in words, generated from the data. This is
    # the most important thing on the page. Write it first!
    warmest = future.loc[future["temperature_2m"].idxmax()]
    coldest = future.loc[future["temperature_2m"].idxmin()]
    wettest = future.loc[future["precipitation_probability"].idxmax()]
    st.markdown(
        f"It's **{current['temperature_2m']:.0f}°F** in {place} right now. Over the next "
        f"three days, it'll be warmest on **{when(warmest['time'])}** "
        f"({warmest['temperature_2m']:.0f}°F) and coldest on "
        f"**{when(coldest['time'])}** ({coldest['temperature_2m']:.0f}°F). "
        + (
            f"The best chance of rain or snow is **{wettest['precipitation_probability']:.0f}%**, "
            f"on {when(wettest['time'])}."
            if wettest["precipitation_probability"] >= 20
            else "There's little to no chance of rain or snow."
        )
    )

    # CHANGE THIS: one or two annotated charts that make your point. Title as
    # a sentence! Annotate directly!
    line = (
        alt.Chart(df)
        .mark_line()
        .encode(
            x=alt.X("when:O", sort=None, title="Time",
                    axis=alt.Axis(values=every_12_hours, labelAngle=0)),
            y=alt.Y("temperature_2m:Q", title="Temperature (°F)", scale=alt.Scale(zero=False)),
            strokeDash=alt.StrokeDash("period:N", title=None, sort=["Past two days", "Forecast"]),
        )
    )
    now_rule = (
        alt.Chart(pd.DataFrame({"when": [current["when"]], "label": ["Now"]}))
        .mark_rule(strokeDash=[2, 2], color="gray")
        .encode(x=alt.X("when:O", sort=None))
    )
    now_label = now_rule.mark_text(align="left", dx=4, dy=-8, color="gray").encode(
        text="label:N", y=alt.value(0)
    )
    story_chart = (line + now_rule + now_label).properties(
        title=alt.Title(
            f"It'll get as warm as {warmest['temperature_2m']:.0f}°F by {warmest['time']:%A}",
            subtitle=f"Hourly temperature in {place}: the past two days (solid) and the forecast (dashed)",
            anchor="start",
        ),
        # With 120 hourly labels on the x-axis, Altair will happily make this
        # 2,400 pixels wide unless we say otherwise. (width="container" would
        # be nicer, but it comes out zero pixels wide inside maidr's frame.)
        width=750,
        height=300,
    )
    render_maidr(story_chart)

# --- Explore ----------------------------------------------------------------

with explore:
    st.write(
        "Pick a variable to explore. Every chart here can be explored by keyboard: "
        "Tab to it and use the arrow keys. T for text, S for sound."
    )
    variable = st.radio(
        "Variable to show",
        list(VARIABLES),
        format_func=lambda v: f"{VARIABLES[v][0]} ({VARIABLES[v][1]})",
        horizontal=True,
    )
    label, units = VARIABLES[variable]
    show_past = st.checkbox("Include the past two days", value=True)

    shown = df if show_past else future
    explore_chart = (
        alt.Chart(shown)
        .mark_line()
        .encode(
            x=alt.X("when:O", sort=None, title="Time",
                    axis=alt.Axis(values=every_12_hours, labelAngle=0)),
            # maidr reads the axis *title* aloud, so make it a real one.
            y=alt.Y(f"{variable}:Q", title=f"{label} ({units})"),
        )
        .properties(title=f"{label} in {place}, hourly", width=750, height=300)
    )
    render_maidr(explore_chart)

# --- Data -------------------------------------------------------------------

with data:
    readable = shown.rename(
        columns={"time": "Time", "period": "Period", "when": "Day and hour"}
        | {v: f"{lab} ({u})" for v, (lab, u) in VARIABLES.items()}
    )
    st.dataframe(readable, hide_index=True)
    st.download_button(
        "Download this data as CSV",
        readable.to_csv(index=False),
        file_name=f"{place.lower()}_weather.csv",
        mime="text/csv",
    )

# --- About ------------------------------------------------------------------

with about:
    # CHANGE THIS: tell people what they're looking at.
    st.markdown(
        f"""
**Data source:** {SOURCE}. Forecasts are updated hourly. This page caches the
data for ten minutes; use **Check for new data** in the sidebar to fetch it
again.

**What "past two days" means:** these are the model's values for the
previous two days, not measurements from a weather station.

**Accessibility:** the main point of the page is written out at the top of
The Story. Charts in Explore work with the keyboard, text, sound and braille
through [maidr](https://py.maidr.ai/). All of the data is in the Data tab.

**Made by:** {AUTHORS}
"""
    )
