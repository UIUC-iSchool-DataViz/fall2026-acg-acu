# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: -all
#     notebook_metadata_filter: layout,title
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.5
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %%
import pandas as pd

# %%
counties = pd.read_csv("https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv",
                       parse_dates = ["date"])

# %%
del counties["deaths"]

# %%
counties

# %%
states = pd.read_csv("https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv",
                       parse_dates = ["date"])
del states["deaths"]

# %%
states.describe()

# %%
states

# %%
states.dtypes

# %%
counties.dtypes

# %%
counties = counties.dropna()
counties["fips"] = counties["fips"].astype("int64")

# %%
counties

# %%
illinois_results = states[states["state"] == "Illinois"]

# %%
il_by_date = illinois_results.set_index("date")

# %%
il_by_date.loc["2020-01-01":"2020-09-30"]

# %%
import matplotlib.pyplot as plt

# %%
fig, ax = plt.subplots()
ax.plot("cases", data=il_by_date)
plt.xticks(rotation=90);

# %%

# %%
import bqplot

# %%
x_sc = bqplot.DateScale()
y_sc = bqplot.LinearScale()

x_ax = bqplot.Axis(scale = x_sc, label = "Date")
y_ax = bqplot.Axis(scale = y_sc, label = "Cases (cumulative)", orientation = "vertical")

lines = bqplot.Lines(x = il_by_date.index, y = il_by_date["cases"], scales = {'x': x_sc, 'y': y_sc})
fig = bqplot.Figure(marks = [lines], axes = [x_ax, y_ax])
display(fig)

# %%
x_sc = bqplot.DateScale()
y_sc = bqplot.LinearScale()

x_ax = bqplot.Axis(scale = x_sc, label = "Date")
y_ax = bqplot.Axis(scale = y_sc, label = "Cases (cumulative)", orientation = "vertical")

lines = bqplot.Lines(x = il_by_date.index, y = il_by_date["cases"], scales = {'x': x_sc, 'y': y_sc})

date_selection = bqplot.interacts.FastIntervalSelector(scale = x_sc)

fig = bqplot.Figure(marks = [lines], axes = [x_ax, y_ax], interaction = date_selection)
display(fig)

# %%
import numpy as np

# %%
date_selection.selected = np.array(['2022-01-16', '2023-01-10'], dtype='datetime64')

# %%
date_selection

# %%
import ipywidgets

# %%
start = ipywidgets.DatePicker()
end = ipywidgets.DatePicker()

# %%
import traitlets


# %%
def selection_changed(change):
    start.value = pd.Timestamp(change['new'][0]).to_pydatetime()
    end.value = pd.Timestamp(change['new'][1]).to_pydatetime()

def picker_changed(change):
    date_selection.selected = np.array([start.value, end.value], dtype='datetime64')


# %%
start.observe(picker_changed, ['value'])
end.observe(picker_changed, ['value'])
date_selection.observe(selection_changed, ['selected'])

# %%
ipywidgets.VBox([ipywidgets.HBox([start, end]), fig])

# %% [markdown]
# ## Link the selection to the date pickers `start` and `end`

# %%
state_map = bqplot.topo_load("map_data/USStatesMap.json")

# %%
cases_by_fips = states[states["date"] == "2022-04-01"].groupby("fips")["cases"].max().to_dict()

# %%
proj = bqplot.AlbersUSA()
color_sc = bqplot.ColorScale(scheme = "BuPu")
color_ax = bqplot.ColorAxis(scale = color_sc)
map_mark = bqplot.Map(
    map_data = state_map,
    scales = {'projection': proj, 'color': color_sc},
    color = cases_by_fips
)
fig = bqplot.Figure(marks = [map_mark], axes = [color_ax])
display(fig)

# %%
label = ipywidgets.Label()


# %%
def hover_over_state(mark, hover_info):
    label.value = "State %s had %s cases" % (hover_info["data"]["name"], hover_info["data"]["color"])
map_mark.on_hover(hover_over_state)

# %%
label

# %%
usa_cases_by_date = states.groupby("date")["cases"].sum()

# %%
x_sc = bqplot.DateScale()
y_sc = bqplot.LinearScale()

x_ax = bqplot.Axis(scale = x_sc, label = "Date")
y_ax = bqplot.Axis(scale = y_sc, label = "Cases (cumulative)", orientation = "vertical")

lines = bqplot.Lines(x = usa_cases_by_date.index, y = usa_cases_by_date.values, scales = {'x': x_sc, 'y': y_sc})

date_selection = bqplot.interacts.IndexSelector(scale = x_sc)

fig1 = bqplot.Figure(marks = [lines], axes = [x_ax, y_ax], interaction = date_selection)
display(fig1)

# %%
date_selection.selected

# %%
import datetime

# %%
states[states["date"] == pd.to_datetime(date_selection.selected).round("1d")[0]]

# %%
proj = bqplot.AlbersUSA()
color_sc = bqplot.ColorScale(scheme = "BuPu")
color_ax = bqplot.ColorAxis(scale = color_sc)

use_cases_by_date = states[states["date"] == pd.to_datetime(date_selection.selected).round("1d")[0]].groupby("fips")["cases"].sum().to_dict()
map_mark = bqplot.Map(
    map_data = state_map,
    scales = {'projection': proj, 'color': color_sc},
    color = use_cases_by_date
)
fig2 = bqplot.Figure(marks = [map_mark], axes = [color_ax])
display(fig2)


# %%
def update_cases(change):
    use_cases_by_date = states[states["date"] == pd.to_datetime(date_selection.selected).round("1d")[0]].groupby("fips")["cases"].sum().to_dict()
    map_mark.color = use_cases_by_date

date_selection.unobserve_all()
date_selection.observe(update_cases, ['selected'])    

# %%
ipywidgets.VBox([fig1, fig2])

# %%
color_sc.min = 0
color_sc.max = states.groupby("state")["cases"].max().max()

# %%
