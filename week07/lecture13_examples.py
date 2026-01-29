# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: -all
#     default_lexer: ipython3
#     formats: ipynb,py:percent,md
#     notebook_metadata_filter: layout,title
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.18.1
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
#   layout: notebook
#   title: Lecture13 Examples
# ---

# %%
import pandas as pd
import numpy as np

# %%
df = pd.read_csv("building_inventory.csv", na_values = {
    "Year Acquired": 0,
    "Year Constructed": 0,
    "Square Footage": 0
})

# %%
df["Year Acquired"] = pd.to_datetime(df["Year Acquired"], format = "%Y")
df["Year Constructed"] = pd.to_datetime(df["Year Constructed"], format = "%Y")

# %%
y_a = df["Year Acquired"]

# %%
df.groupby("Year Acquired")["Square Footage"].sum().plot()

# %%
# !rm -f us-counties.csv ; wget https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv

# %%
# !rm -f us-states.csv ; wget https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv

# %%
states = pd.read_csv("us-states.csv", parse_dates = ["date"])

# %%
states.dtypes

# %%
states["state"] == "Washington"

# %%
states[states["state"] == "Washington"]

# %%
pd.to_datetime(states["date"])

# %%
illinois_results = states[states["state"] == "Illinois"]

# %%
import bqplot

# %%
x_sc = bqplot.DateScale()
y_sc = bqplot.LinearScale()

x_ax = bqplot.Axis(scale = x_sc, label = "Date")
y_ax = bqplot.Axis(scale = y_sc, orientation = 'vertical', label = "Cases (cumulative)")

lines = bqplot.Lines(x = illinois_results["date"], y = illinois_results["cases"],
                     scales = {'x': x_sc, 'y': y_sc})

fig = bqplot.Figure(marks = [lines], axes = [x_ax, y_ax])
display(fig)

# %%
x_sc = bqplot.DateScale()
y_sc = bqplot.LinearScale()

x_ax = bqplot.Axis(scale = x_sc, label = "Date")
y_ax = bqplot.Axis(scale = y_sc, orientation = 'vertical', label = "Cases (cumulative)")

lines = bqplot.Lines(x = illinois_results["date"], y = illinois_results["cases"],
                     scales = {'x': x_sc, 'y': y_sc})

date_selection = bqplot.interacts.FastIntervalSelector(scale = x_sc)

fig = bqplot.Figure(marks = [lines], axes = [x_ax, y_ax], interaction = date_selection)
display(fig)

# %%
states

# %%
proj = bqplot.AlbersUSA()
mark = bqplot.Map(map_data = bqplot.topo_load("map_data/USStatesMap.json"),
                  scales = {'projection': proj})
fig = bqplot.Figure(marks = [mark])
display(fig)

# %%
case_counts = states.groupby("fips")["cases"].max().to_dict()

proj = bqplot.AlbersUSA()
#color_sc = bqplot.ColorScale(colors = ["white", "black"])
color_sc = bqplot.ColorScale(scheme = "viridis")
color_ax = bqplot.ColorAxis(scale = color_sc, label = 'Case Count')

mark = bqplot.Map(map_data = bqplot.topo_load("map_data/USStatesMap.json"),
                  scales = {'projection': proj, 'color': color_sc},
                  color = case_counts)
fig = bqplot.Figure(marks = [mark], axes = [color_ax])
display(fig)

# %%
counties = pd.read_csv("us-counties.csv", parse_dates = ["date"],
                       dtype = {'fips': pd.Int32Dtype()})

# %%
illinois_by_county = counties[counties["state"] == "Illinois"]

# %%
case_counts = illinois_by_county.groupby("fips")["cases"].max().to_dict()

proj = bqplot.AlbersUSA()
color_sc = bqplot.ColorScale(scheme = "BuPu")
color_ax = bqplot.ColorAxis(scale = color_sc, label = 'Case Count')

mark = bqplot.Map(map_data = bqplot.topo_load("map_data/USCountiesMap.json"),
                  scales = {'projection': proj, 'color': color_sc},
                  color = case_counts)
fig = bqplot.Figure(marks = [mark], axes = [color_ax])
display(fig)

# %%
import ipywidgets
v = ipywidgets.Label()
display(v)


# %%
def hover_over_county(name, value):
    v.value = "%s" % (value)


# %%
mark.on_hover(hover_over_county)

# %%
