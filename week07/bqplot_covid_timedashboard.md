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
    display_name: Python 3 (ipykernel)
    language: python
    name: python3
  layout: notebook
  title: Bqplot Covid Timedashboard
---

```python
import pandas as pd
```

```python
df = pd.read_csv("https://raw.githubusercontent.com/nytimes/covid-19-data/refs/heads/master/us-states.csv",
                parse_dates=["date"])
```

```python
df
```

```python
df.dtypes
```

```python
cases_by_date = df.set_index("date")
```

```python
cases_by_date.iloc[10]
```

```python
cases_by_date.loc["January 01, 2022":"February 28, 2023"]
```

```python
us_cases_by_date = cases_by_date.groupby("date")["cases"].sum()
us_cases_by_date
```

```python
import bqplot
```

```python
us_cases_by_date.values
```

```python
import numpy as np
```

```python
x_sc = bqplot.DateScale()
y_sc = bqplot.LinearScale()

x_ax = bqplot.Axis(scale = x_sc)
y_ax = bqplot.Axis(scale = y_sc, orientation = 'vertical')

pan_zoom = bqplot.interacts.PanZoom(scales = {'x': [x_sc], 'y': [y_sc]})

line = bqplot.Lines(x = us_cases_by_date.index, y = us_cases_by_date.values, scales = {'x': x_sc, 'y': y_sc})
figure = bqplot.Figure(marks = [line], axes = [x_ax, y_ax], interaction = pan_zoom)
display(figure)
```

```python
us_state_map = bqplot.topo_load("map_data/USStatesMap.json")
```

```python
proj_scale = bqplot.AlbersUSA()
color_scale = bqplot.ColorScale()

color_axis = bqplot.ColorAxis(scale = color_scale)

map_mark = bqplot.Map(map_data = us_state_map,
                      color = cases_by_date.groupby("fips")["cases"].max().to_dict(),
                      scales = {'projection': proj_scale, 'color': color_scale})

figure = bqplot.Figure(marks = [map_mark], axes = [color_axis])
display(figure)
```

```python
import ipywidgets
```

```python
x_sc = bqplot.DateScale()
y_sc = bqplot.LinearScale()

x_ax = bqplot.Axis(scale = x_sc)
y_ax = bqplot.Axis(scale = y_sc, orientation = 'vertical')

pan_zoom = bqplot.interacts.PanZoom(scales = {'x': [x_sc], 'y': [y_sc]})

line = bqplot.Lines(x = us_cases_by_date.index, y = us_cases_by_date.values, scales = {'x': x_sc, 'y': y_sc})
line_figure = bqplot.Figure(marks = [line], axes = [x_ax, y_ax], interaction = pan_zoom)

proj_scale = bqplot.AlbersUSA()
color_scale = bqplot.ColorScale()

color_axis = bqplot.ColorAxis(scale = color_scale)

map_mark = bqplot.Map(map_data = us_state_map,
                      color = cases_by_date.groupby("fips")["cases"].max().to_dict(),
                      scales = {'projection': proj_scale, 'color': color_scale})

map_figure = bqplot.Figure(marks = [map_mark], axes = [color_axis])

date_picker = ipywidgets.DatePicker()

def on_pick_date(change):
    new_date = pd.to_datetime(change['new'])
    map_mark.color = cases_by_date.loc[new_date].groupby("fips")["cases"].max().to_dict()

date_picker.observe(on_pick_date, ["value"])

hb = ipywidgets.VBox([date_picker, ipywidgets.HBox([line_figure, map_figure])])

map_figure.layout.width = '50%'
line_figure.layout.width = '50%'
hb.layout.width = '100%'
hb.layout.height = '100%'
hb
```

```python
x_sc = bqplot.DateScale()
y_sc = bqplot.LinearScale()

x_ax = bqplot.Axis(scale = x_sc)
y_ax = bqplot.Axis(scale = y_sc, orientation = 'vertical')

fi_sel = bqplot.interacts.FastIntervalSelector(scale = x_sc)

line = bqplot.Lines(x = us_cases_by_date.index, y = us_cases_by_date.values, scales = {'x': x_sc, 'y': y_sc})
line_figure = bqplot.Figure(marks = [line], axes = [x_ax, y_ax], interaction = fi_sel)

def change_selection(change):
    if change['new'] is not None and change['new'].size > 0:
        start, stop = change['new']
        values = cases_by_date.loc[pd.to_datetime(start):pd.to_datetime(stop)].groupby("fips")
        v1 = values["cases"].min()
        v2 = values["cases"].max()
        delta_cases.value = f"Difference of {(v2 - v1).sum():0.2e}"
        map_mark.color = (v2 - v1).to_dict()

delta_cases = ipywidgets.Label()

fi_sel.observe(change_selection, "selected")

proj_scale = bqplot.AlbersUSA()
color_scale = bqplot.ColorScale()

color_axis = bqplot.ColorAxis(scale = color_scale)

map_mark = bqplot.Map(map_data = us_state_map,
                      color = cases_by_date.groupby("fips")["cases"].max().to_dict(),
                      scales = {'projection': proj_scale, 'color': color_scale})

map_figure = bqplot.Figure(marks = [map_mark], axes = [color_axis])

hb = ipywidgets.VBox([delta_cases, ipywidgets.HBox([line_figure, map_figure])])

map_figure.layout.width = '50%'
line_figure.layout.width = '50%'
hb.layout.width = '100%'
hb.layout.height = '100%'
hb
```

```python
fi_sel.selected
```

```python

```
