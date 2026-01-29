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
  title: Bqplot Intro
---

```python
import bqplot
import numpy as np

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
ax_x = bqplot.Axis(scale = x_sc, label = "X Value")
ax_y = bqplot.Axis(scale = y_sc, label = "Y Value")
```

```python
fig = bqplot.Figure(marks = [lines], axes = [ax_x, ax_y])
fig
```

```python
ax_y.orientation = "vertical"
```

```python
import ipywidgets
```

```python
x_domain = ipywidgets.IntRangeSlider(min = -100, max = 200)

def update_range(change):
    x_sc.min = change["new"][0]
    x_sc.max = change["new"][1]
x_domain.observe(update_range, ["value"])

x_domain
```

```python
bx = ["A", "B", "C", "D"]
by = [100, 21, 57, 99]
```

```python
bx_sc = bqplot.OrdinalScale(domain = bx)
by_sc = bqplot.LinearScale()
```

```python
bar = bqplot.Bars(x = bx, y = by, scales = {'x': bx_sc, 'y': by_sc})
```

```python
bax_x = bqplot.Axis(scale = bx_sc)
bax_y = bqplot.Axis(scale = by_sc, orientation = 'vertical')
fig = bqplot.Figure(marks = [bar], axes = [bax_x, bax_y])
```

```python
fig
```

```python
bar.colors = ["steelblue", "red", "green", "yellow"]
```

```python
bar.opacities = [1.0]
```

```python

```

```python
interval = bqplot.interacts.FastIntervalSelector(scale = x_sc, marks = [lines])
```

```python
fig = bqplot.Figure(marks = [lines], axes = [ax_x, ax_y], interaction = interval)
fig
```

```python
interval.selected
```

```python

```
