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
  title: Inclass Week03 Previous
---

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
```

```python
#!wget https://raw.githubusercontent.com/UIUC-iSchool-DataViz/is445_data/main/building_inventory.csv
```

```python
df = pd.read_csv("building_inventory.csv", na_values = {'Year Acquired': 0, 'Year Constructed': 0},
                parse_dates=["Year Acquired", "Year Constructed"])
```

```python
df.describe()
```

```python
#!wget https://github.com/UIUC-iSchool-DataViz/is445_data/raw/main/michigan_lld.flt
```

```python
arr = np.fromfile("michigan_lld.flt", dtype="<f4")
```

```python
data = arr.reshape((-1, 4201))
```

```python
data[data < -9998] = np.nan
```

```python
plt.imshow(data)
plt.show()
```

```python
data.shape
```

```python
plt.imshow(data[::10,::10])
plt.colorbar()
plt.show()
```

```python
fig, ax = plt.subplots(1, 1)
ax.set_title("Axes Title")
```

```python
fig, ax = plt.subplots(2, 2)
fig.suptitle("Figure Title")
ax[0, 0].set_title("Axes [0, 0] Title")
ax[0, 1].set_title("Axes [0, 1] Title")
ax[1, 0].set_title("Axes [1, 0] Title")
ax[1, 1].set_title("Axes [1, 1] Title")
```

```python
ax0 = ax[0,0]
```

```python
ax0.patches
```

```python
ax0.lines
```

```python
ax0.images
```

```python
ax0.transAxes, ax0.transData
```

```python
import matplotlib.patches as patches
```

```python
fig, ax = plt.subplots(1, 1)
ax.plot( [1, 2, 3, 4, 5], [0.1, 0.4, 0.3, 0.2, 0.9])
circle1 = patches.Circle( (3.0, 0.7), radius = 0.1, facecolor = 'red')
circle2 = patches.Circle( (0.75, 0.25), radius = 0.1, facecolor = 'blue',
                        transform = ax.transAxes)
ax.add_patch(circle1)
ax.add_patch(circle2)
```

```python
fig
```

```python
df
```

```python
agg = df.groupby("Year Acquired")["Square Footage"].sum()
```

```python
start = agg.index[agg.argmax()]
end = agg.index[agg.argmax() + 10]
```

```python
fig, ax = plt.subplots(1, 1)
ax.plot(agg.index, agg.values)
r = patches.Rectangle( (start, 0), end - start, 4e6, facecolor = "blue", alpha = 0.3)
ax.add_patch(r)
```

```python
import matplotlib.transforms as tf
```

```python
fig, ax = plt.subplots(1, 1)
ax.plot(agg.index, agg.values)
new_transform = tf.blended_transform_factory(ax.transData, ax.transAxes)
r = patches.Rectangle( (start, 0.0), end - start, 1.0,
                      facecolor = "blue", alpha = 0.3,
                      transform = new_transform)
ax.add_patch(r)
```

```python
fig, ax = plt.subplots(1, 1)
ax.plot(agg.index, agg.values)
new_transform = tf.blended_transform_factory(ax.transData, ax.transAxes)
r = patches.Rectangle( (start, 0.0), end - start, 1.0,
                      facecolor = "blue", alpha = 0.3,
                      transform = new_transform)
ax.add_patch(r)
ax.set_ylim(-100, 1e7)
```

```python
ax.spines['left'].set_color("red")
```

```python
fig
```

```python
ax.xaxis.set_label_text("Hello")
fig
```

```python
ax.xaxis.label.set_rotation(90)
```

```python
fig
```

```python
x = np.mgrid[0.0:24:256j]
y = np.sin(x) + np.cos(x/5)**2
```

```python
fig, ax = plt.subplots(1,1)
ax.plot(x, y, "red")
```

```python
ax.get_xticks()
ax.set_xticks( [0, 10, 25] )
fig
```

```python
ax.get_xticks()
ax.set_xticks( [np.pi, 2*np.pi, 6*np.pi] )
ax.set_xticklabels( ["$\pi$", "$2\pi$", "$6\pi$"] )
fig
```

```python
x = np.mgrid[0.0:24:2048j]
y = np.sin(x) + np.cos(x/5)**2 + np.cos(x*20) * 0.1
```

```python
fig, ax = plt.subplots(1, 1, dpi=300)
ax.plot(x, y)
inset = ax.inset_axes([0.75, 0.75, 0.15, 0.15])
inset.plot(x, y)
inset.set_xlim(0.5, 0.6)
inset.autoscale(axis="y")
```

```python
with plt.style.context("petroff10"):
    fig, ax = plt.subplots(1, 1)
    ax.plot(x, y)
```

```python
x, y = np.mgrid[-0.5:0.5:128j, -0.5:0.5:128j]
```

```python
r = (x*x + y+y)
```

```python
r.shape
```

```python
plt.imshow(r, origin='lower')
plt.colorbar()
plt.set_cmap("coolwarm")
```

```python

```
