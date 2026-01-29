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
  title: Geopandas
---

```python
#!pip install geopandas
```

```python
import requests
import bqplot
import ipywidgets
import numpy as np
import pandas as pd

import geopandas as gpd
import matplotlib.pyplot as plt
```

# Geopandas

```python
# build in dataset
gpd.datasets.available
```

```python
# New York dataset
gdf_ny = gpd.read_file(gpd.datasets.get_path('nybb'))
gdf_ny
```

```python
# Make viz
gdf_ny.plot(figsize=(8, 8), color='green', alpha=0.5, edgecolor='k')
plt.show()
```

# Geopandas and matplotlib
- Open access datasets: https://gis-cityofchampaign.opendata.arcgis.com/search?collection=Dataset

```python
# Datasets that we are going to use:

# Council Districts
url_council = 'https://opendata.arcgis.com/datasets/1f75636917604299861fb408bbf79378_1.geojson'
# City owned properties
url_properties = 'https://opendata.arcgis.com/datasets/3ecbc7baf1a44110a98f6d4420432000_2.geojson'
# Apartments
url_apartments = 'https://opendata.arcgis.com/datasets/64154052c5a040e287bae1583d727825_8.geojson'
```

```python
# councils
gdf_councils = gpd.read_file(url_council)
gdf_councils
```

```python
gdf_councils.crs
```

```python
gdf_councils.bounds
```

```python
gdf_councils.centroid
```

```python
gdf_councils.plot(figsize=(8, 8))
```

```python
gdf_councils.boundary.plot()
```

```python
# properties file
gdf_prop = gpd.read_file(url_properties)
print(gdf_prop.info())
gdf_prop.head()
```

```python
print(gdf_prop['TYPE'].unique())
```

```python
gdf_prop.groupby(['TYPE'])[['OBJECTID']].count()
```

```python
fig, ax = plt.subplots(figsize=(8, 8))

gdf_councils.plot(ax=ax, color='grey')

filter_1 = gdf_prop['TYPE'].str.contains('Fire Station')
filter_2 = ~gdf_prop['TYPE'].isna()

gdf_prop.loc[(filter_1)&(filter_2)].plot(ax=ax, color='red')

# Zoom in
ax.set_xlim(-88.28, -88.22)
ax.set_ylim(40.10, 40.14)

plt.show()
```

```python
# Apartment file
gdf_apat = gpd.read_file(url_apartments)
print(gdf_apat.info())
gdf_apat.head()
```

```python
gdf_apat['Building_Type'].unique()
```

```python
fig, ax = plt.subplots(figsize=(8, 8))

gdf_councils.plot(ax=ax, color='grey')
gdf_apat.plot(ax=ax, column='Building_Type', cmap='tab10', legend=True)

#zoom in
ax.set_xlim(-88.26, -88.20)
ax.set_ylim(40.10, 40.14)

plt.show()
```

```python
# add interaction

building_types = gdf_apat['Building_Type'].unique().tolist()
selector = ipywidgets.SelectMultiple(options=building_types , description='Building Type')
selector
```

```python
def make_plot(selected_type):
    print('Selected Type:', selected_type)
    
    fig, ax = plt.subplots(figsize=(8, 8))

    gdf_councils.plot(ax=ax, color='grey')
    
    if len(selected_type) == 0:
        gdf_apat.plot(ax=ax, column='Building_Type', cmap='tab10', legend=True)
    else:
        gdf_apat_sel = gdf_apat.loc[gdf_apat['Building_Type'].isin(selected_type)]
        gdf_apat_sel.plot(ax=ax, column='Building_Type', cmap='tab10', legend=True)

    #zoom in
    ax.set_xlim(-88.26, -88.20)
    ax.set_ylim(40.10, 40.14)

    plt.show()

building_types = gdf_apat['Building_Type'].unique().tolist()
selector = ipywidgets.SelectMultiple(options=building_types , description='Building Type')
ipywidgets.interact(make_plot, selected_type=selector)
```

# GeoJSON and Bqplot

```python
# Map Data

council_map_data = requests.get(url_council).json()
apartment_map_data = requests.get(url_apartments).json()

# Scale
geo_sc = bqplot.Mercator(scale_factor = 200000, center=(-88.28, 40.12))

# Mark
council_map = bqplot.Map(map_data=council_map_data, 
                         scales={'projection':geo_sc})
apartment_map = bqplot.Map(map_data=apartment_map_data, 
                           scales={'projection':geo_sc})

# Fig
fig = bqplot.Figure(marks=[council_map, apartment_map])
fig
```

```python

```
