# Week 13: A template for Part 3 of your final project (Viz for the Public)
#
# Run this with:
#
#     uv run --extra notebooks streamlit run week13/streamlit/part3_template.py
#
# This is a skeleton you can copy. It runs as-is, using our old friend the
# Illinois building inventory, but it's meant to be gutted and filled with
# *your* group's data. Look for the "CHANGE THIS" comments.
#
# The structure is the "martini glass" from week 12:
#
#   * The Story   -- you lead: the main point in words, and one or two
#                    annotated charts
#   * Explore     -- then you let go: controls and charts to poke at
#   * Data        -- the table, and a download button
#   * About       -- where the data comes from, what you did to it, who made it
#
# And it bakes in what we'll talk about on November 30: words first, charts
# that work with maidr, and real labels everywhere.

import pathlib

import altair as alt
import pandas as pd
import streamlit as st
from maidr.widget.streamlit import render_maidr

# --- CHANGE THIS: what is your project? ------------------------------------

TITLE = "Who Owns Illinois's Buildings?"
SOURCE = "[Illinois Building Inventory](https://data.illinois.gov/), via the IS445 course site"
AUTHORS = "Your group's names here"

# Put your data file in your repo, next to this script. Paths are relative to
# *this file*, so it works the same on your laptop and on Streamlit Community
# Cloud. (If you don't have the file, we grab the course copy from the web.)
DATA_FILE = pathlib.Path(__file__).parent / "building_inventory.csv"
DATA_URL = "https://uiuc-ischool-dataviz.github.io/fall2026-acg-acu/data/building_inventory.csv"

st.set_page_config(page_title=TITLE, layout="wide")


# --- CHANGE THIS: loading and cleaning your data ---------------------------
#
# Do your cleaning here, once, and write down what you did in the About tab.
# Remember: the whole script re-runs every time somebody touches a widget,
# so @st.cache_data matters.
@st.cache_data
def load_data():
    raw = pd.read_csv(DATA_FILE if DATA_FILE.exists() else DATA_URL)
    # A year of 0 means "we don't know."
    df = raw[raw["Year Constructed"] > 0].copy()
    df["Decade"] = (df["Year Constructed"] // 10 * 10).astype(str) + "s"
    # Keep track of what we threw away, so we can say so in the About tab.
    dropped = len(raw) - len(df)
    return df, dropped


df, dropped = load_data()

st.title(TITLE)
st.caption(f"Data from {SOURCE}.")

story, explore, data, about = st.tabs(["The Story", "Explore", "Data", "About"])

# --- The Story ---------------------------------------------------------------

with story:
    # CHANGE THIS: the main point, in words, computed from the data. This is
    # the most important thing on the page. Write it first! Computing it
    # (instead of typing the numbers) means it can't go out of date.
    by_agency = (
        df.groupby("Agency Name", as_index=False)["Square Footage"]
        .sum()
        .sort_values("Square Footage", ascending=False)
    )
    by_agency["Million square feet"] = by_agency["Square Footage"] / 1e6
    total = by_agency["Square Footage"].sum()
    first, second = by_agency.iloc[0], by_agency.iloc[1]

    st.markdown(
        f"The state of Illinois owns **{total / 1e6:.0f} million square feet** of "
        f"buildings, spread across {len(by_agency)} agencies. The "
        f"**{first['Agency Name']}** alone has **{first['Square Footage'] / total:.0%}** "
        f"of it -- {first['Million square feet']:.0f} million square feet. Second "
        f"place, with {second['Million square feet']:.0f} million, is the "
        f"{second['Agency Name']}."
    )

    # CHANGE THIS: one or two charts that make your point. Title as a
    # sentence! Highlight what matters, gray out the rest, annotate directly.
    top10 = by_agency.head(10)
    # Sort the bars biggest-first. (sort="-x" gets quietly ignored once you
    # layer a text label on top, so we hand it the order explicitly. Always
    # look at your chart!)
    order = top10["Agency Name"].tolist()
    bars = (
        alt.Chart(top10)
        .mark_bar()
        .encode(
            x=alt.X("Million square feet:Q", title="Building space (million square feet)"),
            y=alt.Y("Agency Name:N", sort=order, title=None, axis=alt.Axis(labelLimit=300)),
            color=alt.condition(
                alt.datum["Agency Name"] == first["Agency Name"],
                alt.value("#1f5fa8"),  # passes 3:1 contrast against white
                alt.value("#9aa0a6"),
            ),
        )
    )
    label = (
        alt.Chart(top10.head(1))
        .mark_text(align="left", dx=6, color="#1f5fa8", fontWeight="bold")
        .encode(
            x="Million square feet:Q",
            y=alt.Y("Agency Name:N", sort=order),
            text=alt.value(f"{first['Square Footage'] / total:.0%} of all state building space"),
        )
    )
    story_chart = (bars + label).properties(
        title=alt.Title(
            f"The {first['Agency Name']} has more building space than any other agency",
            subtitle="The ten Illinois state agencies with the most building space",
            anchor="start",
        ),
        # Set a width. (width="container" comes out zero pixels wide inside
        # maidr's frame.)
        width=600,
        height=300,
    )
    render_maidr(story_chart)

# --- Explore ------------------------------------------------------------------

with explore:
    st.write(
        "Pick an agency to see when its buildings were built. Every chart here can "
        "be explored by keyboard: Tab to it and use the arrow keys. T for text, S for sound."
    )
    # CHANGE THIS: the controls that make sense for your data. Every widget
    # gets a real, descriptive label -- a screen reader reads it out loud.
    agencies = by_agency["Agency Name"].tolist()
    agency = st.selectbox("Agency to show", agencies)
    measure = st.radio(
        "What to count",
        ["Number of buildings", "Square footage"],
        horizontal=True,
    )

    shown = df[df["Agency Name"] == agency]
    by_decade = (
        shown.groupby("Decade", as_index=False)
        .agg(**{"Number of buildings": ("Square Footage", "size"),
                "Square footage": ("Square Footage", "sum")})
    )
    explore_chart = (
        alt.Chart(by_decade)
        .mark_bar()
        .encode(
            # A text label like "1960s" on an ordinal axis reads well in
            # maidr. A temporal axis gets read as raw milliseconds!
            x=alt.X("Decade:O", title="Decade built", axis=alt.Axis(labelAngle=0)),
            # maidr reads the axis *title* aloud, so make it a real one.
            y=alt.Y(f"{measure}:Q", title=measure),
        )
        .properties(title=f"{agency}: {measure.lower()} by decade built", width=600, height=300)
    )
    render_maidr(explore_chart)

# --- Data ---------------------------------------------------------------------

with data:
    columns = ["Agency Name", "Location Name", "City", "County", "Year Constructed",
               "Square Footage", "Bldg Status"]
    st.write(f"All {len(shown):,} buildings for the {agency} (pick a different one in Explore).")
    st.dataframe(shown[columns], hide_index=True)
    st.download_button(
        "Download this data as CSV",
        shown[columns].to_csv(index=False),
        file_name="buildings.csv",
        mime="text/csv",
    )

# --- About --------------------------------------------------------------------

with about:
    # CHANGE THIS: tell people what they're looking at, and what you did to it.
    st.markdown(
        f"""
**Data source:** {SOURCE}.

**What we did to it:** we dropped the {dropped:,} buildings with
no construction year (they're listed with a year of 0), and grouped years
into decades.

**Accessibility:** the main point of the page is written out at the top of
The Story. The charts work with the keyboard, text, sound and braille
through [maidr](https://py.maidr.ai/). All of the data is in the Data tab.

**Use of AI tools:** if you used an LLM, say which one and when, the prompt,
and how you checked its work. (See the syllabus policy.)

**Made by:** {AUTHORS}
"""
    )
