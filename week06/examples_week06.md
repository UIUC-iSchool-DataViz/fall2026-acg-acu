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
  title: Examples Week06
---

```python
import bqplot.market_map
import bqplot
import numpy as np
import pandas as pd
```

```python
df = pd.read_csv("../data/building_inventory.csv",
            na_values = {'Year Acquired': 0, 'Year Constructed': 0, 'Square Footage': 0}
)
```

```python
import ipywidgets
```

```python
building_gb = df.groupby("Congressional Full Name").agg(
    {'Square Footage': ['count', 'sum']}
)['Square Footage']

color_scale = bqplot.ColorScale(scheme = "Blues")
color_axis = bqplot.ColorAxis(scale = color_scale, label = "Total Building Count")

my_map = bqplot.market_map.MarketMap(
    names = building_gb.index.values,
    ref_data = building_gb,
    color = building_gb['sum'],
    tooltip_fields = ['sum', 'count'],
    tooltip_format = ['.1f', '.1f'],
    scales = {'color': color_scale},
    axes = [color_axis]
)

year_acquisition = df.groupby("Year Acquired").sum()["Square Footage"]

x_sc = bqplot.LinearScale()
y_sc = bqplot.LogScale()
x_ax = bqplot.Axis(scale = x_sc)
y_ax = bqplot.Axis(scale = y_sc, orientation = 'vertical')

base_line = np.add.accumulate(year_acquisition.values)

acquired_footage = bqplot.Lines(x = year_acquisition.index.values,
                                y = base_line,
                                scales = {'x': x_sc, 'y': y_sc}
)

def update_footage(event):
    new_selection = event['new']
    if len(new_selection) == 0:
        new_df = df
    else:
        new_df = df[df['Congressional Full Name'].isin(new_selection)]
    new_ac = new_df.groupby("Year Acquired").sum()["Square Footage"]
    acquired_footage.x = new_ac.index.values
    acquired_footage.y = np.add.accumulate(new_ac.values)

my_map.observe(update_footage, ['selected'])

fig = bqplot.Figure(marks = [acquired_footage], axes = [x_ax, y_ax])

display(ipywidgets.VBox([my_map, fig]))
```

```python
building_gb = df.groupby("Congressional Full Name").agg(
    {'Square Footage': ['count', 'sum']}
)['Square Footage']

color_scale = bqplot.ColorScale(scheme = "Blues")
color_axis = bqplot.ColorAxis(scale = color_scale, label = "Total Building Count")

my_map = bqplot.market_map.MarketMap(
    names = building_gb.index.values,
    ref_data = building_gb,
    color = building_gb['sum'],
    tooltip_fields = ['sum', 'count'],
    tooltip_format = ['.1f', '.1f'],
    scales = {'color': color_scale},
    axes = [color_axis]
)

year_acquisition = df.groupby("Year Acquired").sum()["Square Footage"]

x_sc = bqplot.LinearScale()
y_sc = bqplot.LogScale()
x_ax = bqplot.Axis(scale = x_sc)
y_ax = bqplot.Axis(scale = y_sc, orientation = 'vertical')

base_line = np.add.accumulate(year_acquisition.values)

acquired_footage = bqplot.Lines(x = year_acquisition.index.values,
                                y = base_line,
                                scales = {'x': x_sc, 'y': y_sc}
)

fast_int_sel = bqplot.interacts.FastIntervalSelector(scale = x_sc)
fig = bqplot.Figure(marks = [acquired_footage], axes = [x_ax, y_ax],
                    interaction = fast_int_sel)
mi, ma = building_gb['sum'].min(), building_gb['sum'].max()
def update_colors(event):
    if len(event['new']) == 0:
        range_df = df
    else:
        range_df = df[(df['Year Acquired'] < event['new'][1])
                     &(df['Year Acquired'] > event['new'][0])]
    range_gb = range_df.groupby("Congressional Full Name").agg(
                        {'Square Footage': ['count', 'sum']}
                    )['Square Footage']
    my_map.color = range_gb['sum']
    color_scale.min = mi
    color_scale.max = ma
fast_int_sel.observe(update_colors, ['selected'])
    
display(ipywidgets.VBox([my_map, fig]))
```

```python

```
