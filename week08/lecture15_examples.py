# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: -all
#     default_lexer: ipython3
#     formats: ipynb,py:percent,md
#     notebook_metadata_filter: layout,title
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.18.1
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
#   layout: notebook
#   title: Lecture15 Examples
# ---

# %%
import cartopy
import matplotlib.pyplot as plt

# %%
fig = plt.figure()
ax = fig.add_subplot(111, projection=cartopy.crs.Mollweide())
ax.coastlines()

# %%
fig = plt.figure()
ax = fig.add_subplot(111, projection=cartopy.crs.Mollweide(central_longitude=180))
ax.coastlines()

# %%
fig = plt.figure()
ax = fig.add_subplot(111, projection=cartopy.crs.Orthographic())
ax.coastlines()

# %%
fig = plt.figure()
ax = fig.add_subplot(111, projection=cartopy.crs.PlateCarree())
ax.coastlines()
ax.gridlines()

# %%
c_lat, c_lon = 40.1164, -88.2434
a_lat, a_lon = -18.8792, 47.5079
fig = plt.figure(dpi=150)
ax = fig.add_subplot(111, projection=cartopy.crs.PlateCarree())
ax.scatter([c_lon, a_lon], [c_lat, a_lat])
ax.coastlines()
ax.gridlines()
ax.set_global()

# %%
c_lat, c_lon = 40.1164, -88.2434
a_lat, a_lon = -18.8792, 47.5079
fig = plt.figure(dpi=150)
ax = fig.add_subplot(111, projection=cartopy.crs.Mollweide())
ax.plot([c_lon, a_lon], [c_lat, a_lat], transform=cartopy.crs.PlateCarree())
ax.plot([c_lon, a_lon], [c_lat, a_lat], transform=cartopy.crs.Geodetic())
ax.coastlines()
ax.gridlines()
ax.set_global()

# %%
import numpy as np
vals = np.random.random((128, 128))

# %%
plt.imshow(vals)

# %%
c_lat, c_lon = 40.1164, -88.2434
a_lat, a_lon = -18.8792, 47.5079
fig = plt.figure(dpi=150)
ax = fig.add_subplot(111, projection=cartopy.crs.Mollweide())
ax.plot([c_lon, a_lon], [c_lat, a_lat], transform=cartopy.crs.PlateCarree())
ax.plot([c_lon, a_lon], [c_lat, a_lat], transform=cartopy.crs.Geodetic())
ax.imshow(vals, extent = [-60, -30, 30, 60], transform = cartopy.crs.PlateCarree())
ax.coastlines()
ax.gridlines()
ax.set_global()

# %%
import pandas as pd

# %%
# !rm -f us-counties.csv ; wget https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv

# %%
# !rm -f us-states.csv ; wget https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv

# %%
states = pd.read_csv("us-states.csv", parse_dates = ["date"])

# %%
import bqplot

# %%
proj = bqplot.AlbersUSA()
mark = bqplot.Map(map_data = bqplot.topo_load("map_data/USStatesMap.json"),
                  scales = {'projection': proj})
fig = bqplot.Figure(marks = [mark])
display(fig)

# %%
case_counts = states.groupby("fips")["cases"].max().to_dict()

proj = bqplot.AlbersUSA()
color_sc = bqplot.ColorScale(scheme = "viridis")
color_ax = bqplot.ColorAxis(scale = color_sc, label = 'Case Count')

mark = bqplot.Map(map_data = bqplot.topo_load("map_data/USStatesMap.json"),
                  scales = {'projection': proj, 'color': color_sc},
                  color = case_counts)
fig = bqplot.Figure(marks = [mark], axes = [color_ax])
display(fig)

# %%
total_cases = states.groupby("date").sum()

# %%
total_cases["cases"]

# %%
x_sc = bqplot.DateScale()
y_sc = bqplot.LogScale()

x_ax = bqplot.Axis(scale = x_sc)
y_ax = bqplot.Axis(scale = y_sc, orientation='vertical')

lines = bqplot.Lines(x = total_cases.index, y = total_cases["cases"],
                     scales = {'x': x_sc, 'y': y_sc})

interval_selector = bqplot.interacts.FastIntervalSelector(scale = x_sc)

fig = bqplot.Figure(marks = [lines], axes = [x_ax, y_ax], interaction = interval_selector)
display(fig)

# %%
interval_selector.selected

# %%
total_cases.loc[interval_selector.selected[0]:interval_selector.selected[1]]

# %%
