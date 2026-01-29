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
#   title: Lecture16 Examples
# ---

# %%
import pandas as pd
import traitlets
import ipywidgets
import bqplot
import numpy as np

# %%
states = pd.read_csv("us-states.csv", parse_dates = ["date"])

# %%
states.loc

# %%
states.iloc

# %%
states.head()

# %%
states.loc[0:3]

# %%
states.iloc[0:3]

# %%
states_by_date = states.set_index("date")

# %%
states_by_date

# %%
states_by_date.loc['2020-01-21':'2020-01-23']

# %%
states_by_date.iloc[0:4]

# %%
states_by_date.loc['2020-01-21':'2020-01-25']

# %%
states_by_date.groupby("state").max()["cases"]

# %%
total_cases = states_by_date.groupby("date").sum()["cases"]

# %%
states_by_date.groupby("state").get_group("Illinois")

# %%
states_timeseries = dict(tuple(_) for _ in states_by_date.groupby("state"))

# %%
states_timeseries['Illinois']

# %%
case_counts = states.groupby("fips")["cases"].max().to_dict()

proj = bqplot.AlbersUSA()
color_sc = bqplot.ColorScale(scheme = 'Reds')
color_ax = bqplot.ColorAxis(scale = color_sc, label = "Case Count", reverse = True)

mark = bqplot.Map(map_data = bqplot.topo_load("map_data/USStatesMap.json"),
                  scales = {'projection': proj, 'color': color_sc},
                  color = case_counts,
                  colors = {17: '#ff0000'},
                  hovered_styles = {'hovered_fill': 'none',
                                    'hovered_stroke': 'black',
                                    'hovered_stroke_width': 5.0}
                 )
fig = bqplot.Figure(marks = [mark], axes = [color_ax])
display(fig)

# %%
date_sc = bqplot.DateScale()
case_sc = bqplot.LogScale()

date_ax = bqplot.Axis(scale = date_sc)
case_ax = bqplot.Axis(scale = case_sc, orientation = 'vertical')

lines = bqplot.Lines(x = total_cases.index, y = total_cases,
                     scales = {'x': date_sc, 'y': case_sc})

interval_selector = bqplot.interacts.FastIntervalSelector(scale = date_sc)

fig = bqplot.Figure(marks = [lines], axes = [date_ax, case_ax], interaction = interval_selector)
display(fig)

# %%
case_counts = states_by_date.groupby("fips")["cases"].max().to_dict()

proj = bqplot.AlbersUSA()
color_sc = bqplot.ColorScale(scheme = 'Reds', min = states_by_date["cases"].min(), max = states_by_date["cases"].max())
color_ax = bqplot.ColorAxis(scale = color_sc, label = "Case Count", reverse = True)

mark = bqplot.Map(map_data = bqplot.topo_load("map_data/USStatesMap.json"),
                  scales = {'projection': proj, 'color': color_sc},
                  color = case_counts,
                  colors = {'default_color': 'white'},
                  hovered_styles = {'hovered_fill': 'none',
                                    'hovered_stroke': 'black',
                                    'hovered_stroke_width': 5.0}
                 )
fig_map = bqplot.Figure(marks = [mark], axes = [color_ax])

date_sc = bqplot.DateScale()
case_sc = bqplot.LogScale()

date_ax = bqplot.Axis(scale = date_sc)
case_ax = bqplot.Axis(scale = case_sc, orientation = 'vertical')

lines = bqplot.Lines(x = total_cases.index, y = total_cases,
                     scales = {'x': date_sc, 'y': case_sc})

interval_selector = bqplot.interacts.FastIntervalSelector(scale = date_sc)

fig_line = bqplot.Figure(marks = [lines], axes = [date_ax, case_ax], interaction = interval_selector)

def on_selection_change(change):
    if change['new'] is None: return
    start_date, stop_date = change['new']
    new_color = states_by_date.loc[start_date:stop_date].groupby("fips").max()["cases"].to_dict()
    mark.color = new_color

interval_selector.observe(on_selection_change, "selected")

display(ipywidgets.VBox([fig_map, fig_line]))

# %%
mark.interactions = {'click': 'select'}

# %%
mark.selected

# %%
case_counts = states_by_date.groupby("fips")["cases"].max().to_dict()

proj = bqplot.AlbersUSA()
color_sc = bqplot.ColorScale(scheme = 'Reds', min = states_by_date["cases"].min(), max = states_by_date["cases"].max())
color_ax = bqplot.ColorAxis(scale = color_sc, label = "Case Count", reverse = True)

mark = bqplot.Map(map_data = bqplot.topo_load("map_data/USStatesMap.json"),
                  scales = {'projection': proj, 'color': color_sc},
                  color = case_counts,
                  colors = {'default_color': 'white'},
                  hovered_styles = {'hovered_fill': 'none',
                                    'hovered_stroke': 'black',
                                    'hovered_stroke_width': 5.0}
                 )
mark.interactions = {'click': 'select'}
fig_map = bqplot.Figure(marks = [mark], axes = [color_ax])

date_sc = bqplot.DateScale()
case_sc = bqplot.LogScale()

date_ax = bqplot.Axis(scale = date_sc)
case_ax = bqplot.Axis(scale = case_sc, orientation = 'vertical')

lines = bqplot.Lines(x = total_cases.index, y = total_cases,
                     scales = {'x': date_sc, 'y': case_sc})

interval_selector = bqplot.interacts.FastIntervalSelector(scale = date_sc)

fig_line = bqplot.Figure(marks = [lines], axes = [date_ax, case_ax], interaction = interval_selector)

def on_state_selection_change(change):
    if change['new'] is None: return
    new_data = [total_cases]
    fips_groupby = states_by_date.groupby("fips")
    for fips_value in change['new']:
        new_data.append(fips_groupby.get_group(fips_value)["cases"])
    lines.y = pd.DataFrame(new_data)

mark.observe(on_state_selection_change, "selected")

def on_selection_change(change):
    if change['new'] is None: return
    start_date, stop_date = change['new']
    new_color = states_by_date.loc[start_date:stop_date].groupby("fips").max()["cases"].to_dict()
    mark.color = new_color

interval_selector.observe(on_selection_change, "selected")

display(ipywidgets.VBox([fig_map, fig_line]))
