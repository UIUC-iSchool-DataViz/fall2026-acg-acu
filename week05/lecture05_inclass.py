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
#   title: Lecture05 Inclass
# ---

# %%
import bqplot
import numpy as np

# %%
bqplot.Figure()

# %%
x = np.arange(100)
y = np.random.random(100) + 5

# %%
x_sc = bqplot.LinearScale()
y_sc = bqplot.LinearScale()

# %%
lines = bqplot.Lines(x = x, y = y, scales = {'x': x_sc, 'y': y_sc})

# %%
fig = bqplot.Figure(marks = [lines])
display(fig)

# %%
x_ax = bqplot.Axis(scale = x_sc, label = 'X Value')

# %%
fig.axes = [x_ax]

# %%
y_ax = bqplot.Axis(scale = y_sc, label = 'Y Value', orientation = 'vertical')

# %%
fig.axes.append(y_ax)

# %%
fig.axes = []
fig.axes = [x_ax, y_ax]

# %%
lines.colors = ['#ff0000']

# %%
x = ["The Wild Robot", "Deadpool vs Wolverine", "Beetlejuice Beetlejuice", "Inside Out 2"]
y = [100, 250, 10, 500]

# %%
y_sc = bqplot.LinearScale()
x_sc = bqplot.OrdinalScale()

# %%
bar = bqplot.Bars(x = x, y = y, scales = {'x': x_sc, 'y': y_sc})
x_ax = bqplot.Axis(scale = x_sc)
y_ax = bqplot.Axis(scale = y_sc, orientation = 'vertical')
fig = bqplot.Figure(marks=[bar], axes = [x_ax, y_ax])

# %%
fig

# %%
selector = bqplot.interacts.IndexSelector(scale = x_sc)

# %%
fig.interaction = selector

# %%
selector.selected

# %%
x = np.mgrid[0.0:4*np.pi:512j]
y = np.sin(x) * np.cos(x) * (0.5 + np.random.random(512))

# %%
x_sc = bqplot.LinearScale()
y_sc = bqplot.LinearScale()
x_ax = bqplot.Axis(scale = x_sc)
y_ax = bqplot.Axis(scale = y_sc, orientation = 'vertical')
lines = bqplot.Lines(x = x, y = y, scales = {'x': x_sc, 'y': y_sc})
fig = bqplot.Figure(marks = [lines], axes = [x_ax, y_ax])
display(fig)

# %%
fis = bqplot.interacts.FastIntervalSelector(scale = x_sc, marks = [lines])
fig.interaction = fis

# %%
fis.selected

# %%
fis.color = '#0000ff'

# %%
fis.selected

# %%
import ipywidgets
import traitlets

# %%
button = ipywidgets.Button(description = "Regenerate")

# %%
label = ipywidgets.Label()


# %%
def convert_selected(value):
    return "%s - %s" % (value[0], value[1])

traitlets.link((fis, 'selected'), (label, 'value'), (convert_selected, None))

# %%
ipywidgets.VBox([label, fig, button])


# %%
def regenerate(event):
    y = np.sin(x) * np.cos(x) * (0.5 + np.random.random(512))
    lines.y = y

button.on_click(regenerate)

# %%
import pandas as pd

# %%
df = pd.read_csv("building_inventory.csv", 
                na_values = {'Year Acquired': 0,
                             'Year Constructed': 0,
                             'Square Footage': 0})

# %%
gb = df.groupby(["Year Acquired", "Agency Name"])["Square Footage"].sum()

# %%
gb

# %%
gb.loc[:,"Department of Agriculture"]

# %%
x = gb.loc[:, "Department of Agriculture"].index
y = gb.loc[:, "Department of Agriculture"].values
x_sc = bqplot.LinearScale()
y_sc = bqplot.LinearScale()
x_ax = bqplot.Axis(scale = x_sc)
y_ax = bqplot.Axis(scale = y_sc, orientation = 'vertical')
lines = bqplot.Lines(x = x, y = y, scales = {'x': x_sc, 'y': y_sc})
fig = bqplot.Figure(marks = [lines], axes = [x_ax, y_ax])
display(fig)

# %%
x = gb[:, "Department of Natural Resources"].index
y = gb[:, "Department of Natural Resources"].values
lines.x = x
lines.y = y

# %%
select = ipywidgets.Select(options = df["Agency Name"].unique())

# %%
select

# %%
select.value


# %%
def change_y(event):
    new_agency = event['new']
    x = gb[:, new_agency].index
    y = gb[:, new_agency].values
    lines.x = x
    lines.y = y

select.observe(change_y, ["value"])

# %%
fis = bqplot.interacts.FastIntervalSelector(scale = x_sc, marks = [lines])
fig.interaction = fis

# %%
fis.color = '#0000ff'

# %%
label = ipywidgets.Label()


# %%
def selection_changed(event):
    if event['new'] is None: return
    agency = select.value
    start, stop = event['new']
    total = gb.loc[start:stop, agency].sum()
    label.value = "%s square feet" % (total)


# %%
fis.unobserve_all()

# %%
fis.observe(selection_changed, ["selected"])

# %%
label

# %%
