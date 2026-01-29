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
#     display_name: Environment (conda_conda)
#     language: python
#     name: conda_conda
#   layout: notebook
#   title: Lecture09 Examples
# ---

# %%
import bqplot
import numpy as np

# %%
x = np.arange(100)
y = np.random.random(100) + 5

x_sc = bqplot.LinearScale()
y_sc = bqplot.LinearScale()

lines = bqplot.Lines(x = x, y = y,
                    scales = {'x': x_sc, 'y': y_sc})

ax_x = bqplot.Axis(scale = x_sc, label = 'X Value')
ax_y = bqplot.Axis(scale = y_sc, label = 'Y Value',
                   
                   orientation = 'vertical')

fig = bqplot.Figure(marks = [lines], axes = [ax_x, ax_y])
display(fig)

# %%
x = np.arange(100)
y = x**2 + np.random.random(100) * 10

x_sc = bqplot.LinearScale()
y_sc = bqplot.LogScale()
lines = bqplot.Lines(x = x, y = y, scales = {'x': x_sc, 'y': y_sc})
ax_x = bqplot.Axis(scale = x_sc, label = 'X Value')
ax_y = bqplot.Axis(scale = y_sc, label = 'Y Value', orientation = 'vertical')
fig = bqplot.Figure(marks = [lines], axes = [ax_x, ax_y])
display(fig)

# %%
x = np.arange(100)
y = np.random.random(100) + 5

x_sc = bqplot.LinearScale()
y_sc = bqplot.LinearScale()

lines = bqplot.Lines(x = x, y = y, scales = {'x': x_sc, 'y': y_sc})

ax_x = bqplot.Axis(scale = x_sc, label = 'X Value')
ax_y = bqplot.Axis(scale = y_sc, label = 'Y Value', orientation = 'vertical')

pan_zoom = bqplot.PanZoom(scales = {'x': [x_sc], 'y': [y_sc]})

fig = bqplot.Figure(marks = [lines], axes = [ax_x, ax_y], interaction = pan_zoom)
display(fig)

# %%
x = np.arange(100)
y = np.random.random(100) + 5

x_sc = bqplot.LinearScale()
y_sc = bqplot.LinearScale()

lines = bqplot.Lines(x = x, y = y, scales = {'x': x_sc, 'y': y_sc})

ax_x = bqplot.Axis(scale = x_sc, label = 'X Value')
ax_y = bqplot.Axis(scale = y_sc, label = 'Y Value', orientation = 'vertical')

interval_selector = bqplot.interacts.FastIntervalSelector(scale = x_sc)

fig = bqplot.Figure(marks = [lines], axes = [ax_x, ax_y], interaction = interval_selector)
display(fig)

# %%
import ipywidgets
import traitlets

# %%
x = np.arange(100)
y = np.random.random(100) + 5

x_sc = bqplot.LinearScale()
y_sc = bqplot.LinearScale()

lines = bqplot.Lines(x = x, y = y, scales = {'x': x_sc, 'y': y_sc})

ax_x = bqplot.Axis(scale = x_sc, label = 'X Value')
ax_y = bqplot.Axis(scale = y_sc, label = 'Y Value', orientation = 'vertical')

interval_selector = bqplot.interacts.FastIntervalSelector(scale = x_sc)

label_lower = ipywidgets.Label("Lower Limit:")
label_upper = ipywidgets.Label("Upper Limit:")

def on_change_selected(change):
    if change['new'].size < 2: return
    lower = change['new'][0]
    upper = change['new'][1]
    
    label_lower.value = "Lower Limit: %s" % lower
    label_upper.value = "Upper Limit: %s" % upper

interval_selector.observe(on_change_selected, ['selected'])

fig = bqplot.Figure(marks = [lines], axes = [ax_x, ax_y], interaction = interval_selector)
display(ipywidgets.VBox([label_lower, label_upper, fig]))

# %%
x = np.arange(100)
y1 = np.random.random(100) + 5
y2 = x**2 + np.random.random(100) * 10

x_sc = bqplot.LinearScale()
y1_sc = bqplot.LinearScale()
y2_sc = bqplot.LogScale()

lines1 = bqplot.Lines(x = x, y = y1, scales = {'x': x_sc, 'y': y1_sc})
lines2 = bqplot.Lines(x = x, y = y2, scales = {'x': x_sc, 'y': y2_sc})

ax_x = bqplot.Axis(scale = x_sc, label = 'X Value')
ax_y1 = bqplot.Axis(scale = y1_sc, label = 'Y Value', orientation = 'vertical')
ax_y2 = bqplot.Axis(scale = y2_sc, label = 'Y Value', orientation = 'vertical')

interval_selector = bqplot.interacts.FastIntervalSelector(scale = x_sc)

label_lower = ipywidgets.Label("Lower Limit:")
label_upper = ipywidgets.Label("Upper Limit:")

def on_change_selected(change):
    if change['new'].size < 2: return
    lower = change['new'][0]
    upper = change['new'][1]
    
    label_lower.value = "Lower Limit: %s" % lower
    label_upper.value = "Upper Limit: %s" % upper

interval_selector.observe(on_change_selected, ['selected'])

fig1 = bqplot.Figure(marks = [lines1], axes = [ax_x, ax_y1], interaction = interval_selector)
fig2 = bqplot.Figure(marks = [lines2], axes = [ax_x, ax_y2], interaction = interval_selector)
display(ipywidgets.VBox([label_lower, label_upper, ipywidgets.HBox([fig1, fig2])]))

# %%
x = np.arange(100)
y1 = np.random.random(100) + 5
y2 = x**2 + np.random.random(100) * 10

x_sc = bqplot.LinearScale()
y1_sc = bqplot.LinearScale()
y2_sc = bqplot.LogScale()

lines1 = bqplot.Lines(x = x, y = y1, scales = {'x': x_sc, 'y': y1_sc})
lines2 = bqplot.Lines(x = x, y = y2, scales = {'x': x_sc, 'y': y2_sc})

ax_x = bqplot.Axis(scale = x_sc, label = 'X Value')
ax_y1 = bqplot.Axis(scale = y1_sc, label = 'Y Value', orientation = 'vertical')
ax_y2 = bqplot.Axis(scale = y2_sc, label = 'Y Value', orientation = 'vertical')

interval_selector = bqplot.interacts.FastIntervalSelector(scale = x_sc)

label_lower = ipywidgets.Label("Lower Limit:")
label_upper = ipywidgets.Label("Upper Limit:")

def on_change_selected(change):
    if change['new'].size < 2: return
    lower = change['new'][0]
    upper = change['new'][1]
    
    label_lower.value = "Lower Limit: %s" % lower
    label_upper.value = "Upper Limit: %s" % upper
    
    selected_points = (x > lower) & (x < upper)


interval_selector.observe(on_change_selected, ['selected'])

fig1 = bqplot.Figure(marks = [lines1], axes = [ax_x, ax_y1], interaction = interval_selector)
fig2 = bqplot.Figure(marks = [lines2], axes = [ax_x, ax_y2], interaction = interval_selector)

scatter = bqplot.Scatter(x = y1, y = y2, scales = {'x': y1_sc, 'y': y2_sc})
ax_y3 = bqplot.Axis(scale = y1_sc)
ax_y4 = bqplot.Axis(scale = y2_sc, orientation = 'vertical')
fig3 = bqplot.Figure(marks = [scatter], axes = [ax_y3, ax_y4])

display(ipywidgets.VBox([label_lower, label_upper,
                         ipywidgets.HBox([fig1, fig2]),
                         fig3]))

# %%
x = np.arange(100)
y1 = np.random.random(100) + 5
y2 = x**2 + np.random.random(100) * 10

x_sc = bqplot.LinearScale()
y1_sc = bqplot.LinearScale()
y2_sc = bqplot.LogScale()

lines1 = bqplot.Lines(x = x, y = y1, scales = {'x': x_sc, 'y': y1_sc})
lines2 = bqplot.Lines(x = x, y = y2, scales = {'x': x_sc, 'y': y2_sc})

ax_x = bqplot.Axis(scale = x_sc, label = 'X Value')
ax_y1 = bqplot.Axis(scale = y1_sc, label = 'Y Value', orientation = 'vertical')
ax_y2 = bqplot.Axis(scale = y2_sc, label = 'Y Value', orientation = 'vertical')

interval_selector = bqplot.interacts.FastIntervalSelector(scale = x_sc)

label_lower = ipywidgets.Label("Lower Limit:")
label_upper = ipywidgets.Label("Upper Limit:")

def on_change_selected(change):
    if change['new'].size < 2: return
    lower = change['new'][0]
    upper = change['new'][1]
    
    label_lower.value = "Lower Limit: %s" % lower
    label_upper.value = "Upper Limit: %s" % upper
    
    selected_points = (x > lower) & (x < upper)
    scatter.selected = np.where(selected_points)[0].tolist()

interval_selector.observe(on_change_selected, ['selected'])

fig1 = bqplot.Figure(marks = [lines1], axes = [ax_x, ax_y1], interaction = interval_selector)
fig2 = bqplot.Figure(marks = [lines2], axes = [ax_x, ax_y2], interaction = interval_selector)

scatter = bqplot.Scatter(x = y1, y = y2, scales = {'x': y1_sc, 'y': y2_sc})
scatter.selected_style = {'fill': 'orange'}
ax_y3 = bqplot.Axis(scale = y1_sc)
ax_y4 = bqplot.Axis(scale = y2_sc, orientation = 'vertical')
fig3 = bqplot.Figure(marks = [scatter], axes = [ax_y3, ax_y4])

display(ipywidgets.VBox([label_lower, label_upper,
                         ipywidgets.HBox([fig1, fig3]),
                         fig2]))

# %%
scatter.selected_style = {'stroke': 'black', 'fill': 'orange'}

# %%
