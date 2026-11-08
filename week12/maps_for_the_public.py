# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: -all
#     formats: ipynb,py:percent,md
#     notebook_metadata_filter: layout,title
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.5
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
#   layout: notebook
#   title: Maps for the Public
# ---

# %% [markdown]
# # Maps for the Public
#
# Back in weeks 7 through 9 we learned how to _make_ maps -- cartopy,
# geopandas, bqplot. Today is about making maps that don't mislead people.
#
# Maps are one of the most popular things you can show the public. Everybody
# wants to find where they live! But they're also one of the easiest
# things to get wrong, in ways that look totally fine.
#
# We'll use a few small datasets from
# [vega-datasets](https://github.com/vega/vega-datasets): state populations,
# the share of each state's population that works as an engineer, and county
# unemployment rates.

# %%
import altair as alt
import pandas as pd

VEGA_DATA = "https://cdn.jsdelivr.net/npm/vega-datasets@2.11.0/data/"
us_map = VEGA_DATA + "us-10m.json"
states = alt.topo_feature(us_map, "states")
counties = alt.topo_feature(us_map, "counties")

df = pd.read_csv(VEGA_DATA + "population_engineers_hurricanes.csv")
# "engineers" is a fraction of the population. Let's make it something a
# person can actually picture, and also get the raw count back out.
df["engineers_per_1000"] = df["engineers"] * 1000
df["engineer_count"] = (df["engineers"] * df["population"]).round()
# We'll stick to the 50 states for this one.
df = df[~df["state"].isin(["District of Columbia", "Puerto Rico"])]
df.sort_values("engineer_count", ascending=False).head()


# %% [markdown]
# A little helper, so we don't have to write out the lookup every time. A
# `transform_lookup` joins our dataframe onto the shapes, matching on the
# state's FIPS `id`.

# %%
def state_map(field, title, scheme="yellowgreenblue"):
    return (
        alt.Chart(states)
        .mark_geoshape(stroke="white", strokeWidth=0.5)
        .transform_lookup(
            lookup="id", from_=alt.LookupData(df, "id", ["state", field])
        )
        .encode(
            color=alt.Color(f"{field}:Q", title=title, scale=alt.Scale(scheme=scheme)),
            tooltip=["state:N", alt.Tooltip(f"{field}:Q", title=title, format=",.1f")],
        )
        .project("albersUsa")
        .properties(width=380, height=240)
    )


# %% [markdown]
# ## 1. Every raw-count map is a population map
#
# Here's where the engineers are.

# %%
state_map("engineer_count", "Number of engineers").properties(
    title="Where are the engineers?"
)

# %% [markdown]
# California, Texas, New York. Interesting! ...Or is it? Let's put
# it next to a map of how many _people_ live in each state.

# %%
alt.hconcat(
    state_map("engineer_count", "Number of engineers").properties(title="Engineers"),
    state_map("population", "Population", scheme="greys").properties(title="People"),
).resolve_scale(color="independent")

# %% [markdown]
# They're the same map. Most of what a raw count tells you is "more people
# live here." (This is [xkcd #1138](https://xkcd.com/1138/), and it is
# _everywhere_.)
#
# What we almost always want is a **rate**: engineers per 1,000 people.

# %%
state_map("engineers_per_1000", "Engineers per 1,000 people").properties(
    title="Washington, Massachusetts and Virginia have the most engineers per person"
)

# %% [markdown]
# A different story. California is still up there (sixth), but Texas drops
# to the middle of the pack, and Florida is in the bottom half.
#
# **Rule of thumb:** if your number goes up just because more people live
# somewhere, divide by population (or area, or number of households --
# whatever the right denominator is). And say what you divided by, in the
# legend!

# %% [markdown]
# ## 2. How you bin the colors changes the story
#
# With a continuous color scale, every value gets its own color. But a lot of
# maps (most newspaper maps!) put values into a handful of _classes_. How you
# draw the lines between classes is a choice, and it changes what people
# see.
#
# Let's look at county unemployment rates, three ways:
#
# - **Continuous** -- no classes
# - **Equal interval** (`quantize`) -- split the _range_ of values into five
#   equal-width chunks
# - **Quantile** -- put the same _number of counties_ in each of five classes

# %%
def county_map(scale, title):
    return (
        alt.Chart(counties)
        .mark_geoshape()
        .transform_lookup(
            lookup="id",
            from_=alt.LookupData(VEGA_DATA + "unemployment.tsv", "id", ["rate"]),
        )
        .encode(
            color=alt.Color(
                "rate:Q", title="Unemployment", scale=scale, legend=alt.Legend(format=".0%")
            )
        )
        .project("albersUsa")
        .properties(width=300, height=190, title=title)
    )


alt.vconcat(
    county_map(alt.Scale(scheme="blues"), "Continuous"),
    county_map(alt.Scale(type="quantize", nice=True, scheme="blues"), "Equal interval"),
    county_map(alt.Scale(type="quantile", scheme="blues"), "Quantile"),
).resolve_scale(color="independent")

# %% [markdown]
# Same data. Which one makes unemployment look like a crisis? Which one
# makes it look like a few hot spots?
#
# - **Equal interval** is easy to explain, but if a few counties are extreme,
#   almost everybody else lands in one or two classes.
# - **Quantile** always uses every color equally, which makes the map look
#   busy and dramatic -- even if the actual differences are tiny. Look at
#   the legend: the classes are only a couple of percentage points wide.
# - **Continuous** is the most honest about the values, but it's harder to
#   read "which group is this county in."
#
# None of these is wrong. Make the choice on purpose, and make sure the legend
# shows people where the lines are.

# %% [markdown]
# ## 3. Big, empty states
#
# On a map, the size of a thing is its _land area_. That's almost never what
# your data is about. Wyoming gets about 11 times as much ink as New Jersey,
# with about a fifteenth of the people.
#
# When the question is "which states are highest?", a map usually isn't the
# best chart. A sorted bar chart is.

# %%
bars = (
    alt.Chart(df)
    .mark_bar()
    .encode(
        x=alt.X("engineers_per_1000:Q", title="Engineers per 1,000 people"),
        y=alt.Y("state:N", sort="-x", title=None),
    )
    .properties(
        title="Washington, Massachusetts and Virginia have the most engineers per person",
        width=400,
    )
)
bars

# %% [markdown]
# Every state gets the same amount of space, Rhode Island is just as visible
# as Texas, and you can read off the ranking. You lose "where," which is why
# you might show both: the map for the geographic pattern, the bars for the
# details.

# %% [markdown]
# ## 4. Color: sequential or diverging?
#
# - **Sequential** (light to dark, one hue) when the values go from "low" to
#   "high" and there's nothing special in the middle. That's what we've
#   used so far.
# - **Diverging** (two hues, light in the middle) _only_ when there's a
#   meaningful midpoint -- zero, an average, a target.
#
# Here's unemployment as a difference from the median county, where the
# midpoint really does mean something.

# %%
median_rate = pd.read_csv(VEGA_DATA + "unemployment.tsv", sep="\t")["rate"].median()

(
    alt.Chart(counties)
    .mark_geoshape()
    .transform_lookup(
        lookup="id", from_=alt.LookupData(VEGA_DATA + "unemployment.tsv", "id", ["rate"])
    )
    .transform_calculate(difference=f"(datum.rate - {median_rate}) * 100")
    .encode(
        color=alt.Color(
            "difference:Q",
            title="Points above/below median",
            scale=alt.Scale(scheme="blueorange", domainMid=0),
        )
    )
    .project("albersUsa")
    .properties(
        width=500,
        height=300,
        title=f"County unemployment, compared to the median county ({median_rate:.1%})",
    )
)

# %% [markdown]
# A diverging scheme on data with no meaningful middle invents a
# "good side" and a "bad side" that aren't there.
#
# And remember the contrast check from week 14 (coming up!): the lightest
# end of a sequential scheme is often nearly invisible against a white
# background. The white borders between shapes help.

# %% [markdown]
# ## 5. What does a map sound like?
#
# Let's give our map to maidr and listen.

# %%
import maidr

maidr.show(state_map("engineers_per_1000", "Engineers per 1,000 people"))

# %% [markdown]
# Tab to it and press the right arrow. You'll hear something like:
#
# > id is 2, Engineers per 1,000 people is 1.59
#
# "id is 2." That's Alaska's FIPS code! The shapes are in FIPS order (not
# alphabetical, not geographic), and the state's name never gets read, even
# though it's in our tooltip. Somebody using a screen reader gets a list of
# mystery numbers.
#
# So for a map, the accessible version is _everything around it_:
#
# 1. **A sentence that says the point**, generated from the data.
# 2. **A sorted bar chart** -- which maidr reads perfectly, state names and
#    all.
# 3. **A table**, so people can look up their own state.

# %%
top = df.nlargest(3, "engineers_per_1000")
bottom = df.nsmallest(1, "engineers_per_1000").iloc[0]
summary = (
    f"{top['state'].iloc[0]} has the most engineers per person "
    f"({top['engineers_per_1000'].iloc[0]:.1f} per 1,000 people), followed by "
    f"{top['state'].iloc[1]} and {top['state'].iloc[2]}. "
    f"{bottom['state']} has the fewest ({bottom['engineers_per_1000']:.1f} per 1,000)."
)
print(summary)

# %%
maidr.show(bars)

# %% [markdown]
# Now it reads "state is Washington, Engineers per 1,000 people is 10.71."
# Much better.

# %% [markdown]
# ## A checklist for maps for the public
#
# - [ ] **Does it need to be a map?** If the question is "where," yes. If
#   it's "which is highest," maybe a sorted bar chart.
# - [ ] **Rate, not count**, unless you really mean the count -- and the
#   legend says what you divided by.
# - [ ] **Classes chosen on purpose**, and the legend shows the breaks.
# - [ ] **Sequential unless there's a real midpoint.**
# - [ ] **Missing data looks different from zero.** (Gray, or a hatch -- not
#   the lightest color in your scheme!)
# - [ ] **The title says what the map shows.**
# - [ ] **A sentence, a chart, or a table carries the point too**, for
#   anybody who can't use the map.
