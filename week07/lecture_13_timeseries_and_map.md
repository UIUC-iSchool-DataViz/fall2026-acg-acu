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
  title: UFO dataset
---

```python
import pandas as pd
import numpy as np
import bqplot
import traitlets
import ipywidgets
```

```python
buildings = pd.read_csv("building_inventory.csv", 
                        na_values={"Year Acquired": 0,
                                   "Year Constructed": 0,
                                   "Square Footage": 0})

buildings.info()
```

```python
# Show values in Year Acquired column
buildings.head()[['Year Acquired']]
```

```python
# Convert without format
buildings_cp = buildings.copy()
buildings_cp['Year Acquired'] = pd.to_datetime(buildings_cp['Year Acquired'])
buildings_cp.head()[['Year Acquired']]
```

```python
buildings_cp['Year Acquired'].dt.year.tolist()[:3]
```

```python
buildings_cp['Year Acquired'].dt.microsecond.tolist()[:3]
```

```python
# Convert with format
buildings['Year Acquired'] = pd.to_datetime(buildings['Year Acquired'], 
                                            format='%Y')
print(buildings['Year Acquired'].dtype)
buildings.head()[['Year Acquired']]
```

```python
# Extract the year from the date object, Note the datatype
buildings['Year Acquired'] = buildings['Year Acquired'].dt.year
print(buildings['Year Acquired'].dtype)
buildings.head()[['Year Acquired']]
```

# UFO dataset

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
df['duration'] = df['duration'].astype(float)
df['latitude'] = df['latitude'].astype(float)
df['date_sighted'] = pd.to_datetime(df['date_sighted'])

print(df.info())
df.head()
```

# Time-series data

```python
# prep data: Number of UFOs sighted in each month
# https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#offset-aliases

line_data = df.groupby(pd.Grouper(key='date_sighted', 
                                  freq='M'))[['ufo_id']].count()
line_data
```

```python
# Check if grouped result is correct
df.loc[df['date_sighted'].dt.year == 1955]
```

```python
line_data.loc[line_data.index.year == 1955]
```

## Parameter: X lim

```python
# range slider for years
my_slider = ipywidgets.SelectionRangeSlider(options=line_data.index.year,
                                            description='Year Range', 
                                            layout={'width':"600px"})
my_slider
```

```python
my_slider.value
```

```python
# A line plot + displayed the selected year window

# Scale
x_sc = bqplot.DateScale()
y_sc = bqplot.LinearScale()

# Axis
x_ax = bqplot.Axis(scale=x_sc, label='Date Sighted')
y_ax = bqplot.Axis(scale=y_sc, label='UFO counts', 
                   orientation='vertical')

# Mark
lines = bqplot.Lines(x=line_data.index, 
                     y=line_data['ufo_id'], 
                     scales={'x':x_sc, 'y':y_sc})

# Interaction
my_slider = ipywidgets.SelectionRangeSlider(options=line_data.index.year,
                                            description='Year Range', 
                                            layout={'width':"600px"})

def slider_func(change):
    yr_range = my_slider.value
    #print(yr_range)
    
    yr_start, yr_end = yr_range
    
    filter_1 = line_data.index.year >= yr_start
    filter_2 = line_data.index.year <= yr_end
    
    line_data_selected = line_data.loc[(filter_1)&(filter_2)]
    
    lines.x = line_data_selected.index
    lines.y = line_data_selected['ufo_id']

my_slider.observe(slider_func, 'value')

# Fig
line_fig = bqplot.Figure(marks=[lines], axes=[x_ax, y_ax])
line_fig.layout.height='200px'
line_fig_slider = ipywidgets.VBox([my_slider, line_fig])
line_fig_slider
```

# Heatmap and click selected

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
# Scale
x_sc = bqplot.OrdinalScale()
y_sc = bqplot.OrdinalScale()

clr = np.log10(heatmap_data)
c_sc = bqplot.ColorScale(scheme='BuPu', min=np.nanmin(clr) , max=np.nanmax(clr))

# Axis
x_ax = bqplot.Axis(scale=x_sc, label='Country')
y_ax = bqplot.Axis(scale=y_sc, label='Year Reported', orientation='vertical')
c_ax = bqplot.ColorAxis(scale=c_sc, side='right')

# Marks
heatmap = bqplot.GridHeatMap(column=heatmap_data.columns,
                             row=heatmap_data.index,
                             scales={'column':x_sc, 'row':y_sc, 'color':c_sc}, 
                             color=clr)

# Fig
heatmap_fig = bqplot.Figure(marks=[heatmap], axes=[x_ax, y_ax, c_ax])
heatmap_fig
```

```python
# Heatmap with click and select that shows the UFO counts in each month

# Left plot: heatmap
# Scale
x_sc = bqplot.OrdinalScale()
y_sc = bqplot.OrdinalScale()

clr = np.log10(heatmap_data)
c_sc = bqplot.ColorScale(scheme='BuPu', min=np.nanmin(clr) , max=np.nanmax(clr))

# Axis
x_ax = bqplot.Axis(scale=x_sc, label='Country')
y_ax = bqplot.Axis(scale=y_sc, label='Year Reported', orientation='vertical')
c_ax = bqplot.ColorAxis(scale=c_sc, side='right')

# Marks
heatmap = bqplot.GridHeatMap(column=heatmap_data.columns,
                             row=heatmap_data.index,
                             scales={'column':x_sc, 'row':y_sc, 'color':c_sc}, 
                             color=clr, 
                             interactions={'click':'select'}, 
                             selected_style={'fill':'green'})


# Right plot: line plot

# Scale 
x_sc_r = bqplot.DateScale()
y_sc_r = bqplot.LinearScale()

# Axis
x_ax_r = bqplot.Axis(scale=x_sc_r, label='Month')
y_ax_r = bqplot.Axis(scale=y_sc_r, label='UFO counts', 
                     orientation='vertical')

# Mark
lines = bqplot.Lines(scales={'x':x_sc_r, 'y':y_sc_r})


# Interaction:

def observe_func(change):
    selected_cell = heatmap.selected
    print(selected_cell)
    
    selected_row, selected_col = selected_cell[0]
    
    years = heatmap_data.index.tolist()
    countries = heatmap_data.columns.tolist()
    
    selected_yr = years[selected_row]
    selected_country = countries[selected_col]
    
    print(selected_yr, selected_country)
    
    filter_1 = df['date_reported'].dt.year == selected_yr
    filter_2 = df['country'] == selected_country
    
    df_selected = df.loc[(filter_1)&(filter_2)]
    
    df_selected_g = df_selected.groupby(pd.Grouper(key='date_reported', 
                                                   freq='M'))[['ufo_id']].count()
    
    lines.x = df_selected_g.index
    lines.y = df_selected_g['ufo_id']

heatmap.observe(observe_func, 'selected')


# Fig
heatmap_fig = bqplot.Figure(marks=[heatmap], axes=[x_ax, y_ax, c_ax])
line_fig = bqplot.Figure(marks=[lines], axes=[x_ax_r, y_ax_r], 
                         title='UFO counts by month in the selected year and country')

heatmap_fig.layout.width = '500px'
line_fig.layout.width = '500px'

# Dashboard
my_dashboard = ipywidgets.HBox([heatmap_fig, line_fig])
my_dashboard
```

# Maps

```python
# US map data
us_map_data = bqplot.topo_load('map_data/USStatesMap.json')
us_map_data.keys()
```

```python
# Data of one state
us_map_data['objects']['subunits']['geometries'][0]
```

```python
# US Map with tooltip

# Data
us_map_data = bqplot.topo_load('map_data/USStatesMap.json')

# Scale
geo_sc = bqplot.AlbersUSA()

# Axis

# Mark
us_map = bqplot.Map(map_data = us_map_data, 
                    scales={'projection':geo_sc})


# Interaction: tooltip
us_map.tooltip = bqplot.Tooltip(fields=['id', 'name'])

# Fig
us_map_fig = bqplot.Figure(marks=[us_map], 
                           fig_margin={'top':0, 'bottom':0, 'left':0, 'right':0})
us_map_fig
```

```python
# World Map with tooltip

# Data
world_map_data = bqplot.topo_load('map_data/WorldMap.json')

# Scale
world_geo_sc = bqplot.Mercator()

# Axis

# Mark
world_map = bqplot.Map(map_data=world_map_data, 
                       scales={'projection': world_geo_sc})

# Interaction
world_map.tooltip = bqplot.Tooltip(fields=['id', 'name'])

# Fig
world_map_fig = bqplot.Figure(marks=[world_map],
                              fig_margin={'top':0, 'left':0, 'bottom':0, 'right':0})
world_map_fig
```

# US Map with customized colors

```python
df.head()
```

```python
!wget https://gist.githubusercontent.com/dantonnoriega/bf1acd2290e15b91e6710b6fd3be0a53/raw/11d15233327c8080c9646c7e1f23052659db251d/us-state-ansi-fips.csv
```

```python
# Values in the us-state-ansi-fips.csv
# rename column names and clean values

states_df = pd.read_csv('us-state-ansi-fips.csv')
states_df.columns = ['name_full', 'fips', 'name_abbr']
states_df['name_full'] = states_df['name_full'].str.strip()
states_df['name_abbr'] = states_df['name_abbr'].str.strip().str.lower()
states_df
```

```python
# FIPS and state names in the US State map data
for entry in us_map_data['objects']['subunits']['geometries']:
    fips = entry['id']
    print(fips, entry['properties'])
```

## Coropleth map

```python
states_df.head()
```

```python
states_df.loc[states_df['fips']==1]['name_abbr'].tolist()[0]
```

```python
# Color map by number of UFOs sighted in states
clr_prep = df.loc[df['country']=='us'].groupby(['state'])[['ufo_id']].count()
#clr_prep

clr = {}
for entry in us_map_data['objects']['subunits']['geometries']:
    fips = entry['id'] 
    if fips not in [72, 78]:
        state_abbr = states_df.loc[states_df['fips']==fips]['name_abbr'].tolist()[0]
        state_clr = clr_prep.loc[clr_prep.index==state_abbr]['ufo_id'].tolist()[0]
        
        clr[fips] = state_clr

clr
```

```python
# Color: number of UFOs sighted in states
# Data
us_map_data = bqplot.topo_load('map_data/USStatesMap.json')

# Scale
geo_sc = bqplot.AlbersUSA()
clr_sc = bqplot.ColorScale(scheme='Oranges')

# Axis
clr_ax = bqplot.ColorAxis(scale=clr_sc, side='top')

# Mark
us_map = bqplot.Map(map_data = us_map_data, 
                    scales={'projection':geo_sc, 'color':clr_sc}, 
                    color = clr)

# Fig
us_map_fig = bqplot.Figure(marks=[us_map], axes=[clr_ax], 
                           fig_margin={'top':0, 'bottom':0, 'left':0, 'right':0})
us_map_fig
```

## A Dashboard showing duration in seconds by years in the selected state

```python
# Click select + sum of duration in seconds (all the selected states are combined)

# Left plot
# Scale
geo_sc = bqplot.AlbersUSA()
clr_sc = bqplot.ColorScale(scheme='Oranges')

# Axis
clr_ax = bqplot.ColorAxis(scale=clr_sc, side='top')

# Mark
us_map = bqplot.Map(map_data = us_map_data, 
                    scales={'projection':geo_sc, 'color':clr_sc}, 
                    color = clr, 
                    interactions ={'click': 'select'}, 
                    selected_styles={'selected_fill':'green'})

# Right: Line plot
# Scale
x_sc = bqplot.LinearScale()
y_sc = bqplot.LinearScale()

# Axis
x_ax = bqplot.Axis(scale=x_sc, label='Years')
y_ax = bqplot.Axis(scale=y_sc, label='Sum of duration in seconds', orientation='vertical')

# Marks
lines = bqplot.Lines(scales={'x':x_sc, 'y':y_sc})


# Interaction
def select_func(change):
    selected_fips = us_map.selected
    print(selected_fips)
    
    if selected_fips is not None:
    
        state_abbrs = states_df.loc[states_df['fips'].isin(selected_fips)]['name_abbr'].tolist()
        print(state_abbrs)

        df_selected = df.loc[(df['country']=='us')&(df['state'].isin(state_abbrs))]
        df_selected_g = df_selected.groupby(df_selected['date_sighted'].dt.year)[['duration']].sum()

        lines.x = df_selected_g.index
        lines.y = df_selected_g['duration']
    
    else:
        lines.x = []
        lines.y = []

us_map.observe(select_func, 'selected')

# Fig
us_map_fig = bqplot.Figure(marks=[us_map], axes=[clr_ax], 
                           fig_margin={'top':0, 'bottom':0, 'left':0, 'right':0})
line_fig = bqplot.Figure(marks=[lines], axes=[x_ax, y_ax])

us_map_fig.layout.width = '500px'
line_fig.layout.width = '500px'

# Dashboard
my_dashboard = ipywidgets.HBox([us_map_fig, line_fig])
my_dashboard
```

```python
df_selected = df.loc[(df['country']=='us')&(df['state'].isin(['nm', 'tx']))]
df_selected_g = df_selected.groupby(df_selected['date_sighted'].dt.year)[['duration']].sum()
df_selected_g
```

```python
# Click select + sum of duration in seconds (the selected states presented as seperated lines)
# Left plot
# Scale
geo_sc = bqplot.AlbersUSA()
clr_sc = bqplot.ColorScale(scheme='Oranges')

# Axis
clr_ax = bqplot.ColorAxis(scale=clr_sc, side='top')

# Mark
us_map = bqplot.Map(map_data = us_map_data, 
                    scales={'projection':geo_sc, 'color':clr_sc}, 
                    color = clr, 
                    interactions ={'click': 'select'}, 
                    selected_styles={'selected_fill':'green'})

# Right: Line plot
# Scale
x_sc = bqplot.LinearScale()
y_sc = bqplot.LinearScale()

# Axis
x_ax = bqplot.Axis(scale=x_sc, label='Years')
y_ax = bqplot.Axis(scale=y_sc, label='Sum of duration in seconds', orientation='vertical')

# Marks
lines = bqplot.Lines(scales={'x':x_sc, 'y':y_sc}, 
                     display_legend=True)


# Interaction
def select_func(change):
    selected_fips = us_map.selected
    print(selected_fips)
    
    if selected_fips is not None:
    
        state_abbrs = states_df.loc[states_df['fips'].isin(selected_fips)]['name_abbr'].tolist()
        print(state_abbrs)

        line_x_vals = []
        line_y_vals = []
        legend_lbl = []
        
        for state_abbr in state_abbrs:
            df_selected = df.loc[(df['country']=='us')&(df['state']==state_abbr)]
            df_selected_g = df_selected.groupby(df_selected['date_sighted'].dt.year)[['duration']].sum()
            
            x_val_4_a_line = df_selected_g.index.tolist()
            y_val_4_a_line = df_selected_g['duration'].tolist()
            
            line_x_vals.append(x_val_4_a_line)
            line_y_vals.append(y_val_4_a_line)
            
            state_full = states_df.loc[states_df['name_abbr']==state_abbr]['name_full'].tolist()[0]
            legend_lbl.append(state_full)
            
        lines.x = line_x_vals
        lines.y = line_y_vals
        lines.labels = legend_lbl
    
    else:
        lines.x = []
        lines.y = []

us_map.observe(select_func, 'selected')

# Fig
us_map_fig = bqplot.Figure(marks=[us_map], axes=[clr_ax], 
                           fig_margin={'top':0, 'bottom':0, 'left':0, 'right':0})
line_fig = bqplot.Figure(marks=[lines], axes=[x_ax, y_ax], 
                         legend_location='top-left', 
                         legend_style={'fill':'white'})

us_map_fig.layout.width = '500px'
line_fig.layout.width = '500px'

# Dashboard
my_dashboard = ipywidgets.HBox([us_map_fig, line_fig])
my_dashboard
```

## A Dashboard with three plots


[Matplotlib colormap](https://matplotlib.org/stable/tutorials/colors/colormaps.html)

```
OrdinalColorScale()

ordinal_schemes = {
    'Set2': 8,
    'Accent': 8,
    'Set1': 9,
    'Set3': 12,
    'Dark2': 8,
    'Paired': 12,
    'Pastel2': 8,
    'Pastel1': 9,
}
```

```python
# Click select + sum of duration in seconds (the selected states are in seperated lines) + stacked bars by shapes

# Top plot : Map
# Scale
geo_sc = bqplot.AlbersUSA()
clr_sc = bqplot.ColorScale(scheme='Oranges')

# Axis
clr_ax = bqplot.ColorAxis(scale=clr_sc, side='top')

# Mark
us_map = bqplot.Map(map_data = us_map_data, 
                    scales={'projection':geo_sc, 'color':clr_sc}, 
                    color = clr, 
                    interactions ={'click': 'select'}, 
                    selected_styles={'selected_fill':'green'})

# Bottom, Left Line plot
# Scale
x_sc = bqplot.LinearScale()
y_sc = bqplot.LinearScale()

subplot_c_sc = bqplot.OrdinalColorScale(scheme='Dark2')

# Axis
x_ax = bqplot.Axis(scale=x_sc, label='Years')
y_ax = bqplot.Axis(scale=y_sc, label='Sum of duration in seconds', orientation='vertical')

# Marks
lines = bqplot.Lines(scales={'x':x_sc, 'y':y_sc, 'color':subplot_c_sc}, 
                     display_legend=True)

# Bottom, Left: Stacked bar
# Scale
x_sc_r = bqplot.OrdinalScale()
y_sc_r = bqplot.LinearScale()

# Axis
x_ax_r = bqplot.Axis(scale=x_sc_r, label='UFO shapes')
y_ax_r = bqplot.Axis(scale=y_sc_r, label='UFO counts', orientation='vertical')

# Mark
bars = bqplot.Bars(scales={'x':x_sc_r, 'y':y_sc_r, 'color': subplot_c_sc}, 
                   type='stacked', color_mode='element', 
                   display_legend=True, 
                   base=0)


# Interaction
def select_func(change):
    selected_fips = us_map.selected
    print(selected_fips)
    
    if selected_fips is not None:
    
        state_abbrs = states_df.loc[states_df['fips'].isin(selected_fips)]['name_abbr'].tolist()
        print(state_abbrs)
        
        subplot_clrs = np.arange(1, len(state_abbrs)+1)

        line_x_vals = []
        line_y_vals = []
        legend_lbl = []
        
        # Line plot
        for state_abbr in state_abbrs:
            df_selected = df.loc[(df['country']=='us')&(df['state']==state_abbr)]
            df_selected_g = df_selected.groupby(df_selected['date_sighted'].dt.year)[['duration']].sum()
            
            x_val_4_a_line = df_selected_g.index.tolist()
            y_val_4_a_line = df_selected_g['duration'].tolist()
            
            line_x_vals.append(x_val_4_a_line)
            line_y_vals.append(y_val_4_a_line)
            
            state_full = states_df.loc[states_df['name_abbr']==state_abbr]['name_full'].tolist()[0]
            legend_lbl.append(state_full)
            
        lines.x = line_x_vals
        lines.y = line_y_vals
        lines.labels = legend_lbl
        lines.color = subplot_clrs
        
        # Bar chart
        bar_y_vals = []
        
        df_selected_bar = df.loc[(df['country']=='us')&(df['state'].isin(state_abbrs))]
        df_selected_bar_g = df_selected_bar.groupby(['state', 'shape'])[['ufo_id']].count()
        df_selected_bar_g = df_selected_bar_g.reset_index()
        
        shapes = df_selected_bar_g['shape'].unique().tolist()
        
        for state_abbr in state_abbrs:
            state_y_vals = []
            for shape in shapes:
                filter_1 = df_selected_bar_g['state'] == state_abbr
                filter_2 = df_selected_bar_g['shape'] == shape
                
                selected_y_val = df_selected_bar_g.loc[(filter_1)&(filter_2)]
                
                y_val = 0
                if selected_y_val.shape[0] > 0:
                    y_val = selected_y_val['ufo_id'].tolist()[0]
                
                state_y_vals.append(y_val)
        
            bar_y_vals.append(state_y_vals)
        
        print(shapes)
        print(bar_y_vals)
        bars.x = shapes
        bars.y = bar_y_vals
        bars.labels = legend_lbl
        bars.color = subplot_clrs
    
    else:
        lines.x = []
        lines.y = []
        
        bars.x = []
        bars.y = []

us_map.observe(select_func, 'selected')

# Fig
us_map_fig = bqplot.Figure(marks=[us_map], axes=[clr_ax], 
                           fig_margin={'top':0, 'bottom':0, 'left':0, 'right':0})
line_fig = bqplot.Figure(marks=[lines], axes=[x_ax, y_ax], 
                         legend_location='top-left', 
                         legend_style={'fill':'white'})
bar_fig = bqplot.Figure(marks=[bars], axes=[x_ax_r, y_ax_r], 
                        legend_location='top-left', 
                        legend_style={'fill':'white'})

#us_map_fig.layout.width = '500px'
line_fig.layout.width = '500px'
bar_fig.layout.width = '500px'
# Dashboard
bottom_panel = ipywidgets.HBox([line_fig, bar_fig])
my_dashboard = ipywidgets.VBox([us_map_fig, bottom_panel])
my_dashboard
```

```python
df_selected_bar = df.loc[(df['country']=='us')&(df['state'].isin(['il', 'az']))]
df_selected_bar_g = df_selected_bar.groupby(['state', 'shape'])[['ufo_id']].count()
df_selected_bar_g = df_selected_bar_g.reset_index()
df_selected_bar_g
```

```python
filter_1 = df_selected_bar_g['state'] == 'il'
filter_2 = df_selected_bar_g['shape'] == 'chevron'
df_selected_bar_g.loc[(filter_1)&(filter_2)]
```

```python

```
