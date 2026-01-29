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
  title: Prep Notebook Week03 01
---

```python
%matplotlib inline
```

```python
import matplotlib.pyplot as plt
import numpy as np
import csv, json
plt.rcParams["figure.figsize"] = (12,12)
```

```python
ega_palette = {
    0:  (0x00, 0x00, 0x00),
    1:  (0x00, 0x00, 0xAA),
    2:  (0x00, 0xAA, 0x00),
    3:  (0x00, 0xAA, 0xAA),
    4:  (0xAA, 0x00, 0x00),
    5:  (0xAA, 0x00, 0xAA),
    6:  (0xAA, 0x55, 0x00),
    7:  (0xAA, 0xAA, 0xAA),
    8:  (0x55, 0x55, 0x55),
    9:  (0x55, 0x55, 0xFF),
    10: (0x55, 0xFF, 0x55),
    11: (0x55, 0xFF, 0xFF),
    12: (0xFF, 0x55, 0x55),
    13: (0xFF, 0x55, 0xFF),
    14: (0xFF, 0xFF, 0x55),
    15: (0xFF, 0xFF, 0xFF),
}
```

```python
im = np.zeros((16, 4), dtype="uint8")
im[:,3] = 255
for i in ega_palette:
    im[i,:3] = ega_palette[i]
im2 = im.reshape((4,4,4))
```

```python
plt.imshow(im2, interpolation="nearest")
```

```python
plt.style.available
```

```python
import ipywidgets
import numpy as np

def make_cardiod(a = 0.5, style="classic"):
    theta = np.mgrid[0.0:2.0*np.pi:1000j]
    r = a**3 * np.sin(theta-2)**2 + 4 * np.cos(2*theta-5)
    with plt.style.context(style):
        plt.polar(r, theta,)
```

```python
ipywidgets.interact(make_cardiod, a = (0.0, 10.0, 0.01), style = sorted(plt.style.available))
```

```python
colors = ["#{0:02x}{1:02x}{2:02x}".format(*_) for _ in im.tolist()]
colors
```

```python
cycle = plt.cycler("colors", colors)
```

```python
plt.scatter([1,2,3,4], [2,3,4,5])
plt.scatter([1,2,3,4], [1,2,3,4])
plt.scatter([1,2,3,4], [3,4,5,6])
```

```python
with plt.style.context("seaborn"):
    plt.scatter([1,2,3,4], [2,3,4,5])
    plt.scatter([1,2,3,4], [1,2,3,4])
    plt.scatter([1,2,3,4], [3,4,5,6])
```

```python
plt.scatter([1,2,3,4], [2,3,4,5])
plt.scatter([1,2,3,4], [1,2,3,4])
plt.scatter([1,2,3,4], [3,4,5,6])
```

```python
print(colors)
```

```python
plt.rcParams.keys()
```

```python
with plt.style.context({'axes.prop_cycle': plt.cycler('color', colors),
                       'xtick.labelsize': 20, 'figure.facecolor': "#AAAAAA"}):
    plt.plot([1,2,3,4], [2,3,4,5])
    plt.plot([1,2,3,4], [1,2,3,4])
    plt.plot([1,2,3,4], [3,4,5,6])
```

```python
with plt.style.context(["seaborn", 
                       {'axes.prop_cycle': plt.cycler('color', colors),
                       'xtick.labelsize': 20}]):
    plt.plot([1,2,3,4], [2,3,4,5])
    plt.plot([1,2,3,4], [1,2,3,4])
    plt.plot([1,2,3,4], [3,4,5,6])
```

```python

```
