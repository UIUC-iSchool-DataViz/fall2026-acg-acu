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
#     display_name: py311
#     language: python
#     name: py311
#   layout: notebook
#   title: Lecture07 Examples
# ---

# %%
import pandas as pd

# %%
counties = pd.read_csv("https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv",
                       parse_dates = ["date"])

# %%
states = pd.read_csv("https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv",
                    parse_dates = ["date"])

# %%
states

# %%
states.dtypes

# %%
counties

# %%
counties.dtypes

illinois_results = states[
    states["state"] == "Illinois"
]

# %%
illinois_results

# %%
illinois_results["date"] == "January 28, 2020"

# %%
import bqplot

# %%
x_sc = bqplot.DateScale()
y_sc = bqplot.LinearScale()

x_ax = bqplot.Axis(scale = x_sc, label = "Date")
y_ax = bqplot.Axis(scale = y_sc, label = "Cases (cumulative)", orientation = "vertical")

lines = bqplot.Lines(x = illinois_results["date"], y = illinois_results["cases"],
                    scales = {'x': x_sc, 'y': y_sc})

fig = bqplot.Figure(marks = [lines], axes = [x_ax, y_ax])
display(fig)

# %%
x_sc = bqplot.DateScale()
y_sc = bqplot.LinearScale()

x_ax = bqplot.Axis(scale = x_sc, label = "Date")
y_ax = bqplot.Axis(scale = y_sc, label = "Cases (cumulative)", orientation = "vertical")

lines = bqplot.Lines(x = illinois_results["date"], y = illinois_results["cases"],
                    scales = {'x': x_sc, 'y': y_sc})

date_selection = bqplot.interacts.FastIntervalSelector(scale = x_sc)

fig = bqplot.Figure(marks = [lines], axes = [x_ax, y_ax], interaction = date_selection)
display(fig)

# %%
date_selection.selected

# %%
import ipywidgets

# %%
label = ipywidgets.Label()
display(label)


# %%
def watch_selection(change):
    selected_range = illinois_results.loc[change['new'][0] : change['new'][1]]
    delta_cases = selected_range["cases"].max() - selected_range["cases"].min()
    label.value = "An increase of %s" % delta_cases
date_selection.unobserve_all()
date_selection.observe(watch_selection, ["selected"])

# %%
illinois_results.set_index("date", inplace=True)
illinois_results.loc[date_selection.selected[0] : date_selection.selected[1]]

# %%
in_range = ((illinois_results["date"] < date_selection.selected[1])
          & (illinois_results["date"] > date_selection.selected[0]))

# %%
illinois_results[in_range]["cases"]

# %%
illinois_results = states[
    states["state"] == "Illinois"
]

# %%
illinois_results.set_index("date", inplace=True)

# %%
illinois_results

# %%
state_map = bqplot.topo_load("map_data/USStatesMap.json")

# %%
cases_by_fips = states.groupby("fips")["cases"].max().to_dict()

# %%
proj = bqplot.AlbersUSA()
color_sc = bqplot.ColorScale(scheme = "BuPu")
color_ax = bqplot.ColorAxis(scale = color_sc)
map_mark = bqplot.Map(map_data = state_map, color = cases_by_fips,
                      scales = {'projection': proj,
                               'color': color_sc}
)
fig = bqplot.Figure(marks = [map_mark], axes = [color_ax])
display(fig)

# %%
label2 = ipywidgets.Label()
display(label2)


# %%
def hover_over_state(mark, hover_info):
    label2.value = "%s had %s cases" % (hover_info['data']['name'], hover_info['data']['color'])
map_mark.on_hover(hover_over_state)

# %%
bqplot.__version__

# %%
ipywidgets.VBox([
    label2,
    fig,
])

# %%
x_sc = bqplot.DateScale()
y_sc = bqplot.LinearScale()

x_ax = bqplot.Axis(scale = x_sc, label = "Date")
y_ax = bqplot.Axis(scale = y_sc, label = "Cases (cumulative)", orientation = "vertical")

lines = bqplot.Lines(x = illinois_results.index, y = illinois_results["cases"],
                    scales = {'x': x_sc, 'y': y_sc})

date_selection = bqplot.interacts.FastIntervalSelector(scale = x_sc)

line_fig = bqplot.Figure(marks = [lines], axes = [x_ax, y_ax], interaction = date_selection)

proj = bqplot.AlbersUSA()
color_sc = bqplot.ColorScale(scheme = "BuPu")
color_ax = bqplot.ColorAxis(scale = color_sc)
map_mark = bqplot.Map(map_data = state_map, color = cases_by_fips,
                      scales = {'projection': proj,
                               'color': color_sc}
)
map_fig = bqplot.Figure(marks = [map_mark], axes = [color_ax])

ipywidgets.VBox([
    line_fig,
    map_fig
])

# %%
line_fig.layout.height = "250px"
map_fig.layout.height = "400px"

# %%
states_by_date = states.set_index("date")


# %%
def change_date_selection(change):
    max_cases = states_by_date.loc[change['new'][0]:change['new'][1]].groupby("fips")["cases"].max().to_dict()
    print(max_cases)
    map_mark.color = max_cases
date_selection.unobserve_all()
date_selection.observe(change_date_selection, ["selected"])

# %%
states_by_date.loc[date_selection.selected[0] : date_selection.selected[1]].groupby("fips")["cases"].max().to_dict()

# %%
map_mark.color

# %%
