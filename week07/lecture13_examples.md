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
  title: Lecture13 Examples
---

```python
import pandas as pd
import numpy as np
```

```python
df = pd.read_csv("building_inventory.csv", na_values = {
    "Year Acquired": 0,
    "Year Constructed": 0,
    "Square Footage": 0
})
```

```python
df["Year Acquired"] = pd.to_datetime(df["Year Acquired"], format = "%Y")
df["Year Constructed"] = pd.to_datetime(df["Year Constructed"], format = "%Y")
```

```python
y_a = df["Year Acquired"]
```

```python
df.groupby("Year Acquired")["Square Footage"].sum().plot()
```

```python
!rm -f us-counties.csv ; wget https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv
```

```python
!rm -f us-states.csv ; wget https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv
```

```python
states = pd.read_csv("us-states.csv", parse_dates = ["date"])
```

```python
states.dtypes
```

```python
states["state"] == "Washington"
```

```python
states[states["state"] == "Washington"]
```

```python
pd.to_datetime(states["date"])
```

```python
illinois_results = states[states["state"] == "Illinois"]
```

```python
import bqplot
```

```python
x_sc = bqplot.DateScale()
y_sc = bqplot.LinearScale()

x_ax = bqplot.Axis(scale = x_sc, label = "Date")
y_ax = bqplot.Axis(scale = y_sc, orientation = 'vertical', label = "Cases (cumulative)")

lines = bqplot.Lines(x = illinois_results["date"], y = illinois_results["cases"],
                     scales = {'x': x_sc, 'y': y_sc})

fig = bqplot.Figure(marks = [lines], axes = [x_ax, y_ax])
display(fig)
```

```python
x_sc = bqplot.DateScale()
y_sc = bqplot.LinearScale()

x_ax = bqplot.Axis(scale = x_sc, label = "Date")
y_ax = bqplot.Axis(scale = y_sc, orientation = 'vertical', label = "Cases (cumulative)")

lines = bqplot.Lines(x = illinois_results["date"], y = illinois_results["cases"],
                     scales = {'x': x_sc, 'y': y_sc})

date_selection = bqplot.interacts.FastIntervalSelector(scale = x_sc)

fig = bqplot.Figure(marks = [lines], axes = [x_ax, y_ax], interaction = date_selection)
display(fig)
```

```python
states
```

```python
proj = bqplot.AlbersUSA()
mark = bqplot.Map(map_data = bqplot.topo_load("map_data/USStatesMap.json"),
                  scales = {'projection': proj})
fig = bqplot.Figure(marks = [mark])
display(fig)
```

```python
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
```

```python
counties = pd.read_csv("us-counties.csv", parse_dates = ["date"],
                       dtype = {'fips': pd.Int32Dtype()})
```

```python
illinois_by_county = counties[counties["state"] == "Illinois"]
```

```python
case_counts = illinois_by_county.groupby("fips")["cases"].max().to_dict()

proj = bqplot.AlbersUSA()
color_sc = bqplot.ColorScale(scheme = "BuPu")
color_ax = bqplot.ColorAxis(scale = color_sc, label = 'Case Count')

mark = bqplot.Map(map_data = bqplot.topo_load("map_data/USCountiesMap.json"),
                  scales = {'projection': proj, 'color': color_sc},
                  color = case_counts)
fig = bqplot.Figure(marks = [mark], axes = [color_ax])
display(fig)
```

```python
import ipywidgets
v = ipywidgets.Label()
display(v)
```

```python
def hover_over_county(name, value):
    v.value = "%s" % (value)
```

```python
mark.on_hover(hover_over_county)
```

```python

```
