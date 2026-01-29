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
  title: Examples Week 03
---

```python
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
```

```python
df = pd.read_csv("../data/building_inventory.csv",
                na_values = {'Year Acquired': 0,
                             'Year Constructed': 0,
                             'Square Footage': 0})
```

```python
df.describe()
```

```python
df.columns
```

```python
df.groupby("Year Acquired")["Square Footage"].sum()
```

```python
df.groupby("Year Acquired")["Square Footage"].describe()
```

```python
stats = df.groupby("Year Acquired")["Square Footage"].describe()
```

```python
stats.iloc[0]
```

```python
stats.loc[1753]
```

```python
stats.iloc[0:1]
```

```python
stats.loc[1753:1802]
```

```python
p = stats["max"].plot()
p.set_yscale("log")
p.set_ylabel("Square Footage")
```

```python
plt.rcParams["figure.dpi"] = 150
```

```python
p = stats["max"].plot()
p.set_yscale("log")
p.set_ylabel("Square Footage")
```

```python
plt.plot(stats["min"], marker='.', linewidth=1.0, label="Min")
plt.plot(stats["max"], marker='.', linewidth=1.0, label="Max")
plt.fill_between(stats.index, stats["min"], stats["max"], color="#dddddd")
plt.yscale("log")
plt.legend()
```

```python
plt.style.available
```

```python
with plt.style.context("ggplot"):
    plt.plot(stats["min"], marker='.', label="Min")
    plt.plot(stats["max"], marker='.', label="Max")
    plt.fill_between(stats.index, stats["min"], stats["max"], color = "#aaaaaa")
    plt.ylabel("Square Footage")
    plt.yscale("log")
    plt.legend()
```

```python
import matplotlib.transforms as mpt
```

```python
with plt.style.context("ggplot"):
    plt.plot(stats["min"], marker='.', label="Min")
    plt.plot(stats["max"], marker='.', label="Max")
    plt.fill_between(stats.index, stats["min"], stats["max"], color = "#aaaaaa")
    
    plt.ylabel("Square Footage")
    plt.yscale("log")
    plt.legend()
    
    ax = plt.gca()
    plt.plot([0.5, 0.5], [0.0, 1.0], color = 'black', linewidth=2.0,
             transform = ax.transAxes)
```

```python
with plt.style.context("ggplot"):
    plt.plot(stats["min"], marker='.', label="Min")
    plt.plot(stats["max"], marker='.', label="Max")
    plt.fill_between(stats.index, stats["min"], stats["max"], color = "#aaaaaa")
    
    plt.ylabel("Square Footage")
    plt.yscale("log")
    plt.legend()
    
    ax = plt.gca()
    new_transform = mpt.blended_transform_factory(ax.transData, ax.transAxes)
    plt.plot([1818, 1818], [0.0, 1.0], color = 'black', linewidth=2.0,
             transform = new_transform)
```

```python
import ipywidgets
```

```python
slider = ipywidgets.IntSlider(10)
```

```python
slider
```

```python
slider
```

```python
slider.value
```

```python
slider.min, slider.max
```

```python
slider.min = 50
```

```python
ipywidgets.IntSlider(10, min = 9, max=11)
```

```python
@ipywidgets.interact(style = plt.style.available, min_x = (0.0, 10.0, 0.1))
def make_plot(style = "ggplot", min_x = 0.0):
    with plt.style.context(style):
        plt.plot([1,2,3,4], [5,3,1,4])
        plt.xlim(min_x, 15.0)
```

```python
make_plot("fivethirtyeight")
```

```python
plt.scatter("Year Acquired", "Year Constructed", data = df)
```

```python
plt.scatter(df["Year Acquired"], df["Year Acquired"] - df["Year Constructed"])
```

```python
df["Delta Time"] = df["Year Acquired"] - df["Year Constructed"]
df["Delta Time"].replace(0, np.nan, inplace=True)
```

```python
plt.subplot(4, 5, 1)
plt.plot([1,2,3], [2,3,4])
plt.subplot(4, 5, 19)
plt.plot([1,2,3], [1,1,1])
```

```python
michigan = np.fromfile("michigan_lld/michigan_lld.flt", dtype="f4").reshape((5365, 4201))
```

```python
michigan.shape
```

```python
michigan.max()
```

```python
michigan.min()
```

```python
michigan[michigan == -9999] = np.nan
```

```python
plt.hist(michigan.flat)
```

```python
np.nanmin(michigan), np.nanmax(michigan)
```

```python
plt.imshow(michigan)
plt.colorbar(extend = 'both')
plt.clim(-352, 352)
```

```python
plt.imshow(michigan, cmap="seismic")
plt.colorbar(extend = 'both')
plt.clim(-352, 352)
```

```python
plt.imshow(michigan, cmap="jet")
plt.colorbar(extend = 'both')
plt.clim(-352, 352)
```

```python
import matplotlib.colors as colors
```

```python
plt.imshow(np.abs(michigan), norm = colors.LogNorm())
plt.colorbar(extend='both')
```

```python
plt.imshow(michigan, norm = colors.SymLogNorm(100), cmap="terrain")
plt.colorbar(extend='both')
```

```python
plt.imshow(michigan, norm = colors.SymLogNorm(100), cmap="terrain")
plt.xlim(2700, 3300)
plt.ylim(3300, 3900)
plt.colorbar(extend='both')
```

```python
x0 = -88.0
y0 = 46.09
dx = 0.000833333333
dy = 0.000833333333
```

```python
plt.imshow(michigan, extent = [x0, x0 + dx * michigan.shape[0],
                               y0, y0 + dy * michigan.shape[1]],
          norm = colors.SymLogNorm(10), cmap="terrain")
plt.colorbar()
```

```python
y0, x0
```

```python

```
