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
#   title: Accessible Visualization
# ---

# %% [markdown]
# # Accessible Visualization
#
# All semester we've been making charts that you have to _see_ to use. Today
# we're going to fix that, at least a little.
#
# We'll go through it in layers:
#
# 1. **Color and contrast** -- can people with low vision or color vision
#    deficiencies read it?
# 2. **Text alternatives** -- what does somebody who can't see it get?
# 3. **Exploring without seeing** -- keyboard, sound and braille, with
#    [maidr](https://py.maidr.ai/)
# 4. **Putting it in your app** -- Streamlit
#
# Building inventory, one last time. (I promise.)

# %%
import altair as alt
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# %%
df = pd.read_csv("../data/building_inventory.csv")
df = df[(df["Year Constructed"] > 0) & (df["Square Footage"] > 0)]
top_agencies = df["Agency Name"].value_counts().index[:6]
df = df[df["Agency Name"].isin(top_agencies)].copy()
df["Agency"] = df["Agency Name"].str.replace("Department of ", "Dept. of ")
df["Decade"] = df["Year Constructed"] // 10 * 10

by_decade = df.groupby(["Agency", "Decade"]).size().reset_index(name="Buildings")
by_agency = df.groupby("Agency").size().reset_index(name="Buildings")

# %% [markdown]
# ## 1. Color and Contrast
#
# ### How much contrast is enough?
#
# The Web Content Accessibility Guidelines (WCAG) give us numbers to aim
# for. Contrast is measured as a ratio between the lighter and darker color,
# from 1:1 (identical) to 21:1 (black on white):
#
# - **Text:** at least **4.5:1** (3:1 for large text)
# - **Graphical objects** you need to understand the chart -- bars, lines,
#   points: at least **3:1** against what's next to them
#
# Here's how that ratio is computed. It's not magic!

# %%
def relative_luminance(hex_color):
    """How bright a color looks, per the WCAG definition."""
    hex_color = hex_color.lstrip("#")
    channels = [int(hex_color[i : i + 2], 16) / 255 for i in (0, 2, 4)]
    linear = [c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4 for c in channels]
    r, g, b = linear
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast_ratio(color1, color2="#ffffff"):
    l1, l2 = sorted([relative_luminance(color1), relative_luminance(color2)], reverse=True)
    return (l1 + 0.05) / (l2 + 0.05)


contrast_ratio("#000000"), contrast_ratio("#777777")

# %% [markdown]
# ### Checking Altair's default colors
#
# These are the default categorical colors in Altair/vega-lite ("tableau10").
# How do they do against a white background?

# %%
tableau10 = ["#4c78a8", "#f58518", "#e45756", "#72b7b2", "#54a24b",
             "#eeca3b", "#b279a2", "#ff9da6", "#9d755d", "#bab0ac"]

palette = pd.DataFrame({"color": tableau10})
palette["contrast vs. white"] = palette["color"].map(contrast_ratio).round(2)
palette["passes 3:1?"] = palette["contrast vs. white"] >= 3
palette

# %% [markdown]
# Half of the default palette doesn't pass! That yellow is about 1.6:1. If
# your line is yellow on a white background, a lot of people simply won't
# see it.
#
# This doesn't mean "never use light colors." It means: don't make anything
# _important_ depend on them, and check.

# %% [markdown]
# ### Don't rely on color alone
#
# About 1 in 12 men (and about 1 in 200 women) have some form of color
# vision deficiency. If the _only_ way to tell two lines apart is their
# color, some of your readers can't tell them apart.
#
# Here's our spaghetti chart from week 13, limited to three agencies. Then
# the same thing with **redundant encoding** -- color _and_ shape _and_ dash
# pattern _and_ a direct label on each line, so you don't need the legend at all.

# %%
three = by_decade[by_decade["Agency"].isin(
    ["Dept. of Corrections", "Dept. of Natural Resources", "University of Illinois"]
) & (by_decade["Decade"] >= 1900)]

alt.Chart(three).mark_line().encode(
    x="Decade:O", y="Buildings:Q", color="Agency:N"
).properties(width=450, title="Color only")

# %%
# Colors picked to pass 3:1 against white, *and* to differ in lightness.
colors = alt.Scale(
    domain=["Dept. of Corrections", "Dept. of Natural Resources", "University of Illinois"],
    range=["#1b4f72", "#b9770e", "#7d3c98"],
)

lines = alt.Chart(three).mark_line(point=True).encode(
    x="Decade:O",
    y="Buildings:Q",
    color=alt.Color("Agency:N", scale=colors, legend=None),
    shape=alt.Shape("Agency:N", legend=None),
    strokeDash=alt.StrokeDash("Agency:N", legend=None),
)

# Label each line at its peak. (The obvious place -- the end of each line --
# doesn't work here, because all three end up near zero and the labels pile
# on top of each other. Always look at where your labels land!)
labels = alt.Chart(three).mark_text(align="left", dx=8, dy=-8, fontWeight="bold").encode(
    x="Decade:O",
    y="Buildings:Q",
    text="Agency:N",
    color=alt.Color("Agency:N", scale=colors, legend=None),
).transform_joinaggregate(
    peak="max(Buildings)", groupby=["Agency"]
).transform_filter(alt.datum.Buildings == alt.datum.peak)

(lines + labels).properties(width=450, title="Color, shape, dash pattern, and direct labels")

# %% [markdown]
# Try squinting, or taking a screenshot and making it grayscale. You can
# still tell them apart.

# %% [markdown]
# ## 2. Text Alternatives
#
# ### Alt text
#
# Somebody using a screen reader gets whatever text you give them. If you
# give them nothing, they get "image" -- or worse, a file name.
#
# A good, simple pattern for alt text on a chart (from Amy Cesal's
# ["Writing Alt Text for Data Visualization"](https://medium.com/nightingale/writing-alt-text-for-data-visualization-2a218ef43f81)):
#
# > _[Chart type] of [type of data] where [reason for including the chart]._
#
# For example:
#
# > _Line chart of buildings constructed per decade for three Illinois
# > agencies, where Natural Resources builds far more than the other two,
# > peaking in the 1970s and again in the 2000s._
#
# Keep it short. Say the point. Then, if it matters, give them a way to get
# the details (a table, a longer description, or -- see below -- maidr).
#
# ### `description` in vega-lite
#
# Vega-lite takes a `description`, and puts it on the chart as an
# `aria-label` -- which is what a screen reader announces.

# %%
(lines + labels).properties(
    width=450,
    title="When three agencies built their buildings",
    description=(
        "Line chart of buildings constructed per decade for three Illinois agencies, "
        "1900s to 2010s. Natural Resources' construction peaks in the 1970s and again "
        "in the 2000s, at over 600 buildings per decade. Corrections peaks in the "
        "1980s, and the University of Illinois in the 1960s, both well under 400."
    ),
)

# %% [markdown]
# ### Give them the data
#
# Sometimes the best text alternative is just... the table. It's not
# glamorous, but a screen reader handles tables really well. In Streamlit
# that's `st.dataframe(...)`, maybe tucked inside `st.expander("Data table")`.

# %%
three.pivot(index="Decade", columns="Agency", values="Buildings").fillna(0).astype(int)

# %% [markdown]
# ## 3. Exploring Without Seeing: maidr
#
# Alt text gets you the takeaway. But what if somebody wants to _explore_
# the chart -- find the peak themselves, compare two bars, follow a trend?
#
# [maidr](https://py.maidr.ai/) (Multimodal Access and Interactive Data
# Representation) comes from the [xability](https://xability.github.io/)
# lab, right here in the iSchool. It takes a regular matplotlib, seaborn or
# Altair chart and makes it explorable four ways:
#
# - **Keyboard:** arrow keys move between data points
# - **Text:** each point is read out (**T** toggles)
# - **Sound:** pitch goes up and down with the value (**S** toggles)
# - **Braille:** for refreshable braille displays (**B** toggles)
#
# Click on a chart (or Tab to it) to start. **Ctrl + /** (Command + / on a
# Mac) shows every shortcut. **R** turns on "review mode," which lets you
# read the current text with your screen reader's own navigation.
#
# **Try this with your eyes closed.** Seriously. Find the biggest bar.

# %%
import maidr

# Note: importing maidr switches matplotlib's backend, so plt.show() makes
# accessible charts from now on. maidr.set_backend(use_maidr=False) undoes it.

# %%
fig, ax = plt.subplots(figsize=(7, 4))
sns.barplot(data=by_agency.sort_values("Buildings"), x="Agency", y="Buildings", ax=ax)
ax.set_title("Buildings owned by each agency")
ax.tick_params(axis="x", rotation=30)
maidr.show(fig)

# %% [markdown]
# Did you find it? Now try a line chart. Turn on sound (**S**) and just hold
# down the right arrow. You can _hear_ the shape of the trend.

# %%
nr = by_decade[by_decade["Agency"] == "Dept. of Natural Resources"]

fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(nr["Decade"], nr["Buildings"], marker="o")
ax.set_title("Natural Resources buildings constructed per decade")
ax.set_xlabel("Decade")
ax.set_ylabel("Buildings")
maidr.show(fig)

# %% [markdown]
# It handles a lot of chart types -- bar, line, scatter, histogram, box plot,
# heatmap, and more. Here's a box plot:

# %%
fig, ax = plt.subplots(figsize=(7, 4))
sns.boxplot(data=df, x="Square Footage", y="Agency", log_scale=True, ax=ax)
ax.set_title("Building sizes by agency")
maidr.show(fig)

# %% [markdown]
# ### Altair works too
#
# Single and layered Altair charts work. (Faceted and concatenated ones
# don't, yet -- remember week 13!)

# %%
maidr.show(
    alt.Chart(by_agency).mark_bar().encode(
        x=alt.X("Agency:N", sort="-y"), y="Buildings:Q"
    ).properties(title="Buildings owned by each agency", width=400)
)

# %% [markdown]
# ### Sharing an accessible chart
#
# `maidr.save_html` writes a standalone web page you can put anywhere --
# GitHub Pages, an email attachment, a Canvas page.
#
# ```python
# maidr.save_html(fig, "buildings.html")
# ```

# %% [markdown]
# ## 4. In Your Streamlit App
#
# `week14/streamlit/accessible_observatory.py` is the earthquake observatory
# from week 12, redone with accessibility in mind:
#
# - charts drawn with `render_maidr` instead of `st.altair_chart`
# - a written summary, generated from the data, above the charts
# - the data available as a table
# - color never the only encoding
# - auto-refresh _off_ by default (things that change on their own are
#   really disorienting with a screen reader -- or for anybody, honestly)
#
# ```python
# from maidr.widget.streamlit import render_maidr
#
# render_maidr(chart)  # instead of st.altair_chart(chart)
# ```

# %% [markdown]
# ## Your turn: audit your final project
#
# Go through your group's observatory:
#
# 1. **Contrast:** run your colors through `contrast_ratio`. Anything
#    important under 3:1?
# 2. **Color alone:** turn it grayscale. Can you still read it?
# 3. **Alt text:** write one sentence for each chart, using the pattern above.
# 4. **Keyboard:** unplug your mouse. Can you use every control?
# 5. **Screen reader:** turn on VoiceOver (Cmd + F5 on a Mac) or NVDA
#    (free, on Windows) and try to get the main point of your app.
# 6. **maidr:** swap in `render_maidr` for at least one chart, and try to
#    explore it with your eyes closed.
