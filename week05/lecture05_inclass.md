---
jupyter:
  jupytext:
    cell_metadata_filter: -all
    default_lexer: ipython3
    formats: ipynb,py:percent,md
    notebook_metadata_filter: layout,title
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.16.0
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
  layout: notebook
  title: Lecture05 Inclass
---

```python
import bqplot
import numpy as np
```

```python
bqplot.Figure()
```

```python
x = np.arange(100)
y = np.random.random(100) + 5
```

```python
x_sc = bqplot.LinearScale()
y_sc = bqplot.LinearScale()
```

```python
lines = bqplot.Lines(x = x, y = y, scales = {'x': x_sc, 'y': y_sc})
```

```python
fig = bqplot.Figure(marks = [lines])
display(fig)
```

```python
x_ax = bqplot.Axis(scale = x_sc, label = 'X Value')
```

```python
fig.axes = [x_ax]
```

```python
y_ax = bqplot.Axis(scale = y_sc, label = 'Y Value', orientation = 'vertical')
```

```python
fig.axes.append(y_ax)
```

```python
fig.axes = []
fig.axes = [x_ax, y_ax]
```

```python
lines.colors = ['#ff0000']
```

```python
x = ["The Wild Robot", "Deadpool vs Wolverine", "Beetlejuice Beetlejuice", "Inside Out 2"]
y = [100, 250, 10, 500]
```

```python
y_sc = bqplot.LinearScale()
x_sc = bqplot.OrdinalScale()
```

```python
bar = bqplot.Bars(x = x, y = y, scales = {'x': x_sc, 'y': y_sc})
x_ax = bqplot.Axis(scale = x_sc)
y_ax = bqplot.Axis(scale = y_sc, orientation = 'vertical')
fig = bqplot.Figure(marks=[bar], axes = [x_ax, y_ax])
```

```python
fig
```

```python
selector = bqplot.interacts.IndexSelector(scale = x_sc)
```

```python
fig.interaction = selector
```

```python
selector.selected
```

```python
x = np.mgrid[0.0:4*np.pi:512j]
y = np.sin(x) * np.cos(x) * (0.5 + np.random.random(512))
```

```python
x_sc = bqplot.LinearScale()
y_sc = bqplot.LinearScale()
x_ax = bqplot.Axis(scale = x_sc)
y_ax = bqplot.Axis(scale = y_sc, orientation = 'vertical')
lines = bqplot.Lines(x = x, y = y, scales = {'x': x_sc, 'y': y_sc})
fig = bqplot.Figure(marks = [lines], axes = [x_ax, y_ax])
display(fig)
```

```python
fis = bqplot.interacts.FastIntervalSelector(scale = x_sc, marks = [lines])
fig.interaction = fis
```

```python
fis.selected
```

```python
fis.color = '#0000ff'
```

```python
fis.selected
```

```python
import ipywidgets
import traitlets
```

```python
button = ipywidgets.Button(description = "Regenerate")
```

```python
label = ipywidgets.Label()
```

```python
def convert_selected(value):
    return "%s - %s" % (value[0], value[1])

traitlets.link((fis, 'selected'), (label, 'value'), (convert_selected, None))
```

```python
ipywidgets.VBox([label, fig, button])
```

```python
def regenerate(event):
    y = np.sin(x) * np.cos(x) * (0.5 + np.random.random(512))
    lines.y = y

button.on_click(regenerate)
```

```python
import pandas as pd
```

```python
df = pd.read_csv("building_inventory.csv", 
                na_values = {'Year Acquired': 0,
                             'Year Constructed': 0,
                             'Square Footage': 0})
```

```python
gb = df.groupby(["Year Acquired", "Agency Name"])["Square Footage"].sum()
```

```python
gb
```

```python
gb.loc[:,"Department of Agriculture"]
```

```python
x = gb.loc[:, "Department of Agriculture"].index
y = gb.loc[:, "Department of Agriculture"].values
x_sc = bqplot.LinearScale()
y_sc = bqplot.LinearScale()
x_ax = bqplot.Axis(scale = x_sc)
y_ax = bqplot.Axis(scale = y_sc, orientation = 'vertical')
lines = bqplot.Lines(x = x, y = y, scales = {'x': x_sc, 'y': y_sc})
fig = bqplot.Figure(marks = [lines], axes = [x_ax, y_ax])
display(fig)
```

```python
x = gb[:, "Department of Natural Resources"].index
y = gb[:, "Department of Natural Resources"].values
lines.x = x
lines.y = y
```

```python
select = ipywidgets.Select(options = df["Agency Name"].unique())
```

```python
select
```

```python
select.value
```

```python
def change_y(event):
    new_agency = event['new']
    x = gb[:, new_agency].index
    y = gb[:, new_agency].values
    lines.x = x
    lines.y = y

select.observe(change_y, ["value"])
```

```python
fis = bqplot.interacts.FastIntervalSelector(scale = x_sc, marks = [lines])
fig.interaction = fis
```

```python
fis.color = '#0000ff'
```

```python
label = ipywidgets.Label()
```

```python
def selection_changed(event):
    if event['new'] is None: return
    agency = select.value
    start, stop = event['new']
    total = gb.loc[start:stop, agency].sum()
    label.value = "%s square feet" % (total)
```

```python
fis.unobserve_all()
```

```python
fis.observe(selection_changed, ["selected"])
```

```python
label
```

```python

```
