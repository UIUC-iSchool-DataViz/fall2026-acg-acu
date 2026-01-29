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
  title: Lecture06 Examples
---

```python
%matplotlib inline
```

```python
import matplotlib.pyplot as plt
import numpy as np
```

```python
import PIL.Image
```

```python
!wget https://uiuc-ischool-dataviz.github.io/fall2020-BOG-BOU/week03/images/winter_scene.jpg
```

```python
image = PIL.Image.open("winter_scene.jpg")
```

```python
image
```

```python
arr = np.array(image)
```

```python
arr.shape
```

```python
flat_image = arr.reshape((-1, 3))
```

```python
flat_image.shape
```

```python
flat_image[:10]
```

```python
red_only = arr.copy()
red_only[:, :, 1] = 0
red_only[:, :, 2] = 0

green_only = arr.copy()
green_only[:, :, 0] = 0
green_only[:, :, 2] = 0

blue_only = arr.copy()
blue_only[:, :, 0] = 0
blue_only[:, :, 1] = 0

r_img = PIL.Image.fromarray(red_only)
g_img = PIL.Image.fromarray(green_only)
b_img = PIL.Image.fromarray(blue_only)
```

```python
r_img
```

```python
g_img
```

```python
b_img
```

```python
fig, ax = plt.subplots(2, 1, dpi = 300)
ax[0].imshow(arr)
ax[1].hist(flat_image[:,0], bins = np.arange(256), alpha=0.5, facecolor = 'red');
ax[1].hist(flat_image[:,1], bins = np.arange(256), alpha=0.5, facecolor = 'green');
ax[1].hist(flat_image[:,2], bins = np.arange(256), alpha=0.5, facecolor = 'blue');
```

```python
!wget https://uiuc-ischool-dataviz.github.io/spring2019online/week05/data/single_dicom.h5
```

```python
import h5py
```

```python
f = h5py.File("single_dicom.h5")
```

```python
list(f.keys())
```

```python
scan = f["scan"][:]
```

```python
scan.shape
```

```python
scan[18, :, :].shape
```

```python
plt.rcParams["figure.dpi"] = 150
```

```python
import matplotlib.colors as mc
```

```python
import ipywidgets
```

```python
my_norm = mc.LogNorm(vmin = 1.0, vmax = scan.max())
```

```python
image = plt.imshow(scan[12,:,:], extent = [0, 1, 0, 1], norm=my_norm)
image.cmap.set_bad("white")
plt.colorbar()
```

```python
@ipywidgets.interact(slice_coord = (0, 35), colormap = ["viridis", "magma", "cubehelix"])
def slice_scan(slice_coord, colormap = "viridis"):
    image = plt.imshow(scan[slice_coord,:,:], extent = [0, 1, 0, 1], norm=my_norm, cmap = colormap)
    plt.colorbar()
```

```python

```
