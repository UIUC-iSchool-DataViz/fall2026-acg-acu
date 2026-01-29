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
    display_name: Environment (conda_is590dv-default)
    language: python
    name: conda_is590dv-default
  layout: notebook
  title: Prep Notebook Week08
---

```python
%matplotlib inline
```

```python
import cartopy
import pandas as pd
import matplotlib.pyplot as plt
```

```python
plt.rcParams["figure.dpi"] = 300
```

```python
states = cartopy.io.shapereader.natural_earth(resolution='110m', category='cultural',
                                    name='admin_1_states_provinces_lakes_shp')
```

```python
reader = cartopy.io.shapereader.Reader(states)
```

```python
fig = plt.figure()
ax = fig.add_subplot(111, projection = cartopy.crs.PlateCarree())
ax.coastlines()
plt.title("Equirectangular");
```

```python
ny_lon, ny_lat = -75, 43
```

```python
def make_proj(proj_name):
    fig = plt.figure()
    proj = getattr(cartopy.crs, proj_name)
    ax = fig.add_subplot(111, projection = proj())
    ax.gridlines()
    ax.coastlines()
    ax.set_global()
    plt.title(proj_name)
    plt.savefig("images/{}.png".format(proj_name.lower()))
    ax.tissot(500, alpha=0.25, facecolor='red')
    plt.savefig("images/{}_tissot.png".format(proj_name.lower()))
```

```python
for proj in ["Mercator", "PlateCarree", "Gnomonic", "TransverseMercator", "LambertCylindrical", "Mollweide", "Sinusoidal"]:
    make_proj(proj)
    print("Done with", proj)
```

```python
champaign_lat, champaign_lon = 40.1164, -88.2434
antananarivo_lat, antananarivo_lon = -18.8792, 47.5079
```

```python
fig = plt.figure()
ax = fig.add_subplot(111, projection = cartopy.crs.PlateCarree())
ax.gridlines()
ax.coastlines()
ax.set_global()
ax.plot([champaign_lon, antananarivo_lon], [champaign_lat, antananarivo_lat], transform = cartopy.crs.PlateCarree())
ax.plot([champaign_lon, antananarivo_lon], [champaign_lat, antananarivo_lat], transform = cartopy.crs.Geodetic())
```

```python
fig = plt.figure()
ax = fig.add_subplot(111, projection = cartopy.crs.Mollweide())
ax.gridlines()
ax.coastlines()
ax.set_global()
ax.plot([champaign_lon, antananarivo_lon], [champaign_lat, antananarivo_lat], transform = cartopy.crs.PlateCarree())
ax.plot([champaign_lon, antananarivo_lon], [champaign_lat, antananarivo_lat], transform = cartopy.crs.Geodetic())
```

```python

```
