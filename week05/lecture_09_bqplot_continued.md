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
  title: Dataset
---

```python
import pandas as pd
import numpy as np
import bqplot
import traitlets
import ipywidgets
```

# Dataset

[UFO dataset](https://github.com/planetsig/ufo-reports)

```python
#!wget https://github.com/planetsig/ufo-reports/raw/master/csv-data/ufo-scrubbed-geocoded-time-standardized.csv
```

```python
ufo = pd.read_csv('ufo-scrubbed-geocoded-time-standardized.csv', 
                  names=['date_sighted', 'city', 'state', 'country',
                         'shape', 'duration', 
                         'duration_txt', 'note', 'date_reported', 
                         'latitude', 'longitude'],
                  parse_dates=['date_sighted', 'date_reported'])
ufo = ufo.reset_index().rename(columns={'index':'ufo_id'})
print(ufo.shape)

ufo = ufo.loc[~ufo.index.isin([27822, 35692, 58591, 43782])] # Ignore dirty data for now

df = ufo.sample(n=1000, random_state=5).reset_index(drop=True)

df['date_sighted'] = df['date_sighted'].str.replace('24:00', '00:00') 
df['date_sighted'] = pd.to_datetime(df['date_sighted'])

df['duration'] = df['duration'].astype(float)
df['latitude'] = df['latitude'].astype(float)
print(df.info())

df.head(2)
```

# Last week: BrushIntervalSelector
 - Select an area by X or by Y

```python
# Brush, along y

# Scale
x_sc = bqplot.LinearScale()
y_sc = bqplot.LinearScale()

clr = np.log10(df['duration'])
c_sc = bqplot.ColorScale(scheme='Oranges', 
                         min= np.nanmin(clr) , 
                         max= np.nanmax(clr))

# Axis
x_ax = bqplot.Axis(scale=x_sc, label='Year Sighted')
y_ax = bqplot.Axis(scale=y_sc, label='Year Reported', 
                   orientation='vertical')

c_ax = bqplot.ColorAxis(scale=c_sc, side='right')

# Mark
scatter = bqplot.Scatter(x=df['date_sighted'].dt.year, 
                         y=df['date_reported'].dt.year,
                         scales={'x':x_sc, 'y':y_sc, 
                                 'color':c_sc}, 
                         color=clr)


# Interaction: Brush
my_brush = bqplot.interacts.BrushIntervalSelector(scale=y_sc, 
                                                  marks=[scatter], 
                                                  orientation='vertical')

selected_range = ipywidgets.HTML()
num_of_points_selected = ipywidgets.HTML()
def select_func(change):
    my_brush_selected = my_brush.selected
    scatter_selected = scatter.selected
    
    selected_range.value = 'selected range: {}'.format(my_brush_selected)
    num_of_points_selected.value = 'number of selected points: {}'.format(len(scatter_selected))
    #print('my_brush_selected:', my_brush_selected)
    #print('scatter_selected:', scatter_selected)


my_brush.observe(select_func, 'selected')

# fig
scatter_fig = bqplot.Figure(marks=[scatter], axes=[x_ax, y_ax, c_ax], 
                            interaction=my_brush)
scatter_fig_annotated = ipywidgets.VBox([selected_range, 
                                         num_of_points_selected, 
                                         scatter_fig])
scatter_fig_annotated
```

# BrushSelector: Select by X and Y

```python
# Brush, 2D

# Scale
x_sc = bqplot.LinearScale()
y_sc = bqplot.LinearScale()

clr = np.log10(df['duration'])
c_sc = bqplot.ColorScale(scheme='Oranges', 
                         min= np.nanmin(clr) , 
                         max= np.nanmax(clr))

# Axis
x_ax = bqplot.Axis(scale=x_sc, label='Year Sighted')
y_ax = bqplot.Axis(scale=y_sc, label='Year Reported', 
                   orientation='vertical')

c_ax = bqplot.ColorAxis(scale=c_sc, side='right')

# Mark
scatter = bqplot.Scatter(x=df['date_sighted'].dt.year, 
                         y=df['date_reported'].dt.year,
                         scales={'x':x_sc, 'y':y_sc, 
                                 'color':c_sc}, 
                         color=clr)


# Interaction: Brush
my_brush = bqplot.interacts.BrushSelector(x_scale=x_sc, 
                                          y_scale=y_sc, 
                                          marks=[scatter])

#selected_range = ipywidgets.HTML()
#num_of_points_selected = ipywidgets.HTML()

selected_range_x = ipywidgets.HTML()
selected_range_y = ipywidgets.HTML()
def select_func(change):
    my_brush_selected = my_brush.selected
    scatter_selected = scatter.selected
    
    my_brush_selected_x = my_brush.selected_x
    my_brush_selected_y = my_brush.selected_y
    
    selected_range_x.value = 'Selected X range: {}'.format(my_brush_selected_x)
    selected_range_y.value = 'Selected Y range: {}'.format(my_brush_selected_y)
    
    #selected_range.value = 'selected range: {}'.format(my_brush_selected)
    #num_of_points_selected.value = 'number of selected points: {}'.format(len(scatter_selected))
    #print('my_brush_selected:', my_brush_selected)
    #print('scatter_selected:', scatter_selected)


my_brush.observe(select_func, 'selected')

# fig
scatter_fig = bqplot.Figure(marks=[scatter], axes=[x_ax, y_ax, c_ax], 
                            interaction=my_brush)
scatter_fig_annotated = ipywidgets.VBox([selected_range_x, 
                                         selected_range_y, 
                                         scatter_fig])
scatter_fig_annotated
```

# Linking & Brushing
- Left Scatter: year scatter plot
- Right Scatter: longitude and latitude

```python
# Left Scatter: Year Scatter

# Scale
x_sc = bqplot.LinearScale()
y_sc = bqplot.LinearScale()

clr = np.log10(df['duration'])
c_sc = bqplot.ColorScale(scheme='Oranges', 
                         min= np.nanmin(clr) , 
                         max= np.nanmax(clr))

# Axis
x_ax = bqplot.Axis(scale=x_sc, label='Year Sighted')
y_ax = bqplot.Axis(scale=y_sc, label='Year Reported', 
                   orientation='vertical')

c_ax = bqplot.ColorAxis(scale=c_sc, side='right')

# Mark
scatter = bqplot.Scatter(x=df['date_sighted'].dt.year, 
                         y=df['date_reported'].dt.year,
                         scales={'x':x_sc, 'y':y_sc, 
                                 'color':c_sc}, 
                         color=clr)


# Right plot: Scatter of longitude & latitude
# Scale
x_sc_r = bqplot.LinearScale()
y_sc_r = bqplot.LinearScale()

# Axis
x_ax_r = bqplot.Axis(scale=x_sc_r, label='Longitude')
y_ax_r = bqplot.Axis(scale=y_sc_r, label='Latitude', 
                     orientation='vertical')

# Mark
loc_scatter = bqplot.Scatter(x=df['longitude'], 
                             y=df['latitude'], 
                             scales={'x':x_sc_r, 
                                     'y':y_sc_r})


# Interaction: Brush
my_brush = bqplot.interacts.BrushSelector(x_scale=x_sc, 
                                          y_scale=y_sc, 
                                          marks=[scatter])

#selected_range = ipywidgets.HTML()
#num_of_points_selected = ipywidgets.HTML()

selected_range_x = ipywidgets.HTML()
selected_range_y = ipywidgets.HTML()
def select_func(change):
    my_brush_selected = my_brush.selected
    scatter_selected = scatter.selected
    
    my_brush_selected_x = my_brush.selected_x
    my_brush_selected_y = my_brush.selected_y
    
    if my_brush_selected_x is not None and my_brush_selected_y is not None:
    
        selected_range_x.value = 'Selected X range: {}'.format(my_brush_selected_x)
        selected_range_y.value = 'Selected Y range: {}'.format(my_brush_selected_y)

        #selected_range.value = 'selected range: {}'.format(my_brush_selected)
        #num_of_points_selected.value = 'number of selected points: {}'.format(len(scatter_selected))
        #print('my_brush_selected:', my_brush_selected)
        #print('scatter_selected:', scatter_selected)

        x_from, x_to = my_brush_selected_x
        y_from, y_to = my_brush_selected_y

        filter_1 = df['date_sighted'].dt.year >= x_from
        filter_2 = df['date_sighted'].dt.year <= x_to

        filter_3 = df['date_reported'].dt.year >= y_from
        filter_4 = df['date_reported'].dt.year <= y_to

        df_selected = df.loc[(filter_1)&(filter_2)&(filter_3)&(filter_4)]

        loc_scatter.x = df_selected['longitude']
        loc_scatter.y = df_selected['latitude']
        
    else:
        loc_scatter.x = df['longitude']
        loc_scatter.y = df['latitude']


my_brush.observe(select_func, 'selected')

# fig
scatter_fig = bqplot.Figure(marks=[scatter], axes=[x_ax, y_ax, c_ax], 
                            interaction=my_brush)
scatter_fig_annotated = ipywidgets.VBox([selected_range_x, 
                                         selected_range_y, 
                                         scatter_fig])
loc_scatter_fig = bqplot.Figure(marks=[loc_scatter], 
                                axes=[x_ax_r, y_ax_r])

scatter_fig_annotated.layout.width = '500px'
loc_scatter_fig.layout.width = '500px'

# Dashboard
my_dashboard = ipywidgets.HBox([scatter_fig_annotated, 
                                loc_scatter_fig])
my_dashboard
```

# DateScale

```python
# UFOs sigthed in 2000 and their durations in seconds

df_selected = df.loc[df['date_reported'].dt.year==2000]

# Scale
x_sc = bqplot.DateScale()
y_sc = bqplot.LinearScale()

# Axis
x_ax = bqplot.Axis(scale=x_sc, label='Date reported')
y_ax = bqplot.Axis(scale=y_sc, label='Duration in seconds', orientation='vertical')

# Marks
scatter = bqplot.Scatter(x=df_selected['date_reported'], 
                         y=df_selected['duration'], 
                         scales={'x':x_sc, 'y':y_sc})

# Fig
scatter_fig = bqplot.Figure(marks=[scatter], axes=[x_ax, y_ax])
scatter_fig
```

```python
df_selected.head(2)
```

# Heatmap and click select

```python
# Prep data: UFOs reported in different years and countries
heatmap_data = df.groupby([df['date_reported'].dt.year, 'country'])[['ufo_id']].count()
heatmap_data = heatmap_data.reset_index()
heatmap_data = heatmap_data.pivot(index='date_reported', 
                                  columns='country', 
                                  values='ufo_id')
heatmap_data
```

```python
# Heatmap without interactivity

clr = np.log10(heatmap_data)

# Scale
x_sc = bqplot.OrdinalScale()
y_sc = bqplot.OrdinalScale()
c_sc = bqplot.ColorScale(scheme='BuPu', min=np.nanmin(clr), max=np.nanmax(clr))



# Axis
x_ax = bqplot.Axis(scale=x_sc, label='Country')
y_ax = bqplot.Axis(scale=y_sc, label='Year reported', orientation='vertical')
c_ax = bqplot.ColorAxis(scale=c_sc, side='right')

# Mark
heatmap = bqplot.GridHeatMap(row=heatmap_data.index, 
                             column=heatmap_data.columns,
                             scales={'row':y_sc, 'column':x_sc, 'color':c_sc}, 
                             color=clr)

# Fig
heatmap_fig = bqplot.Figure(marks=[heatmap], axes=[x_ax, y_ax, c_ax])
heatmap_fig
```

```python

```
