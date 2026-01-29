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
  title: Examples Week10
---

```python
import bqplot
import json
import numpy as np
import pandas as pd
```

```python
tree_data = json.load(open("../workspace/champaign_trees.geojson", "r"))
```

```python
tree_data.keys()
```

```python
tree_data['type']
```

```python
len(tree_data['features'])
```

```python
tree_data['features'][0]
```

```python
sc_map = bqplot.AlbersUSA()
sc_color = bqplot.ColorScale()
us_map = bqplot.Map(map_data = bqplot.topo_load("map_data/USStatesMap.json"),
                           scales = {'projection': sc_map,
                                    "color": sc_color},
                    colors = {"default_color": "black"},
                    color = {_:_ for _ in np.arange(100)})

fig = bqplot.Figure(marks = [us_map])

display(fig)
```

```python
import ipywidgets
```

```python
l = ipywidgets.Label()
def change_label(event):
    l.value = str(event['new'])

champaign_map.observe(change_label, ["selected"])
l
```

```python

```

```python
legislators = pd.read_csv("../workspace/legislators_historical.csv")
```

```python
legislators_terms = pd.read_csv("../workspace/legislators_historical_terms.csv")
```

```python
fips = pd.read_csv("../workspace/state_fips_master.csv")
```

```python
legislators_terms.state
```

```python
fips_lookup = {row['state_abbr']: row['fips'] for _, row in fips.iterrows()}
```

```python
legislators_fips = legislators_terms.replace({"state": fips_lookup})
```

```python
colors = dict(legislators_fips.groupby("state").count()["bioguide"])
```

```python
sc_map = bqplot.AlbersUSA()
sc_color = bqplot.ColorScale(scheme = "Blues")
us_map = bqplot.Map(map_data = bqplot.topo_load("map_data/USStatesMap.json"),
                           scales = {'projection': sc_map,
                                    "color": sc_color},
                    colors = {"default_color": "black"},
                    color = colors)

fig = bqplot.Figure(marks = [us_map])

display(fig)
```

```python

```
