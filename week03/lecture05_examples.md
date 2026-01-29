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
    display_name: Environment (conda_conda)
    language: python
    name: conda_conda
  layout: notebook
  title: Lecture05 Examples
---

```python
%matplotlib inline
```

```python
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
```

```python
X = np.linspace(0, 4*np.pi, 1000)
Y1 = np.sin(X)
Y2 = np.cos(X)
```

```python
fig, ax = plt.subplots()
lines1 = ax.plot(X, Y1)
lines2 = ax.plot(X, Y2)
```

```python
sin_line = lines1[0]
cos_line = lines2[0]
```

```python
sin_line.properties()
sin_line.set_linestyle("-.")
```

```python
fig
```

```python
fig, ax = plt.subplots()
lines1 = ax.plot(X, Y1, linestyle = ':')
lines2 = ax.plot(X, Y2, color = "red", linewidth = 10.0)
```

```python
fig, ax = plt.subplots()
X = np.random.normal(size = 100)
Y = np.random.normal(size = 100)
ax.scatter(X, Y, marker="x")
ax.text(0.5, 0.5, "Hello!", transform = ax.transAxes)
```

```python
fig, ax = plt.subplots(1, 2)
X1 = np.linspace(0, 4.0*np.pi, 1000)
Y1 = np.sin(X1)

X2 = np.random.normal(size = 100)
Y2 = np.random.normal(size = 100)

ax[0].plot(X1, Y1)
ax[1].scatter(X, Y)

ax[0].text(0.5, 1.0, "Figure!", transform = ax[0].transAxes)
```

```python
df = pd.read_csv("building_inventory.csv",
                 na_values = {'Year Acquired': 0,
                              'Year Constructed': 0,
                              'Square Footage': 0}
                )
```

```python
footage_per_year = df.groupby("Year Acquired")["Square Footage"].sum()
```

```python
total_footage_owned = footage_per_year.cumsum()
```

```python
import matplotlib.patches as patches
import matplotlib.transforms as transforms
```

```python
fig, ax = plt.subplots(dpi = 150)
ax.plot(total_footage_owned.index, total_footage_owned)
ax.set_yscale("log")
ax.set_ylabel("Square Footage (cumulative)")
ax.set_xlabel("Year")
uiuc_annotation1 = patches.Rectangle(
    (1865, 0.0), 4, 1e7, fill = False
)
ax.add_patch(uiuc_annotation1)
uiuc_annotation2 = patches.Rectangle(
    (0.3, 0.0), 0.05, 1.0, fill = False,
    transform = ax.transAxes
)
ax.add_patch(uiuc_annotation2)
```

```python
fig, ax = plt.subplots(dpi = 150)
ax.plot(total_footage_owned.index, total_footage_owned)
ax.set_yscale("log")
ax.set_ylabel("Square Footage (cumulative)")
ax.set_xlabel("Year")
my_transform = transforms.blended_transform_factory(
    ax.transData, ax.transAxes
)
uiuc_annotation = patches.Rectangle(
    (1865, 0.0), 4, 1.0, fill = True, transform = my_transform, facecolor = "red", alpha=0.3,
)
ax.add_patch(uiuc_annotation)
```

```python
fig, ax = plt.subplots(dpi = 150)
ax.semilogy(total_footage_owned.index, total_footage_owned)
ax.set_ylabel("Square Footage (cumulative)")
ax.set_xlabel("Year")
my_transform = transforms.blended_transform_factory(
    ax.transData, ax.transAxes
)
uiuc_annotation = patches.Rectangle(
    (1865, 0.0), 4, 1.0, fill = True, transform = my_transform, facecolor = "red", alpha=0.3,
)
ax.add_patch(uiuc_annotation)
```

```python
plt.style.available
```

```python
with plt.style.context("bmh"):
    fig, ax = plt.subplots()
    X1 = np.linspace(0, 4.0*np.pi, 1000)
    Y1 = np.sin(X1)
    Y2 = np.cos(X1)

    ax.plot(X1, Y1)
    ax.plot(X1, Y2)
```

```python
with plt.style.context("ggplot"):
    fig, ax = plt.subplots()
    X1 = np.linspace(0, 4.0*np.pi, 1000)
    Y1 = np.sin(X1)
    Y2 = np.cos(X1)

    ax.plot(X1, Y1)
    ax.plot(X1, Y2)
```

```python
with plt.style.context("fivethirtyeight"):
    fig, ax = plt.subplots()
    X1 = np.linspace(0, 4.0*np.pi, 1000)
    Y1 = np.sin(X1)
    Y2 = np.cos(X1)

    ax.plot(X1, Y1)
    ax.plot(X1, Y2)
```

```python
with plt.style.context("fivethirtyeight"):
    fig, ax = plt.subplots(2, 2)
    X1 = np.linspace(0, 4.0*np.pi, 1000)
    Y1 = np.sin(X1)
    Y2 = np.cos(X1)

    ax[0,0].plot(X1, Y1)
    ax[1,1].plot(X1, Y2)
```

```python
with plt.style.context("bmh"):
    fig, ax = plt.subplots(2, 2)
    X1 = np.linspace(0, 4.0*np.pi, 1000)
    Y1 = np.sin(X1)
    Y2 = np.cos(X1)

    ax[0,0].plot(X1, Y1)
    ax[1,1].plot(X1, Y2)
```

```python
fig, ax = plt.subplots()
X1 = np.linspace(0, 4.0*np.pi, 1000)
Y1 = np.sin(X1)
Y2 = np.cos(X1)

ax.plot(X1, Y1)
ax.plot(X1, Y2)
```

```python
for tick_label in ax.yaxis.get_ticklabels():
    print(tick_label)
```

```python
for tick_line in ax.yaxis.get_ticklines():
    print(tick_line)
```

```python
ax.yaxis.set_ticks([-1, 0, 1])
```

```python
fig
```

```python
ax.xaxis.set_ticks([0, 4, 8, 12])
```

```python
fig
```

```python
ax.xaxis.set_ticks([0, np.pi, 2*np.pi, 3*np.pi, 4*np.pi])
ax.xaxis.set_ticklabels(["0", "$\pi$", "$2\pi$", "$3\pi$", "$4\pi$"])
fig
```

```python
my_ticks = ax.xaxis.get_ticklabels()
```

```python
fp = my_ticks[0].properties()['fontproperties']
```

```python
fp.get_size()
```

```python
fp.set_size(25)
```

```python
fig
```

```python
fig, ax = plt.subplots()
X1 = np.linspace(0, 4.0*np.pi, 1000)
Y1 = np.sin(X1)
Y2 = np.cos(X1)

ax.plot(X1, Y1, label=r"$\sin(\theta)$")
ax.plot(X1, Y2, label=r"$\cos(\theta)$")
ax.tick_params(axis = "both", which="major", labelsize = 25, size = 10)
ax.legend()
```

```python

```
