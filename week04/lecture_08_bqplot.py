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
#   title: Dataset
# ---

# %%
# In terminal:
# pip install bqplot
# jupyter labextension list
# jupyter labextension install @jupyter-widgets/jupyterlab-manager 
# jupyter labextension install bqplot

# %%
import pandas as pd
import numpy as np
import bqplot
import traitlets
import ipywidgets

# %% [markdown]
# # Dataset
#
# [UFO dataset](https://github.com/planetsig/ufo-reports)

# %%
# # !wget https://github.com/planetsig/ufo-reports/raw/master/csv-data/ufo-scrubbed-geocoded-time-standardized.csv

# %%
ufo = pd.read_csv('ufo-scrubbed-geocoded-time-standardized.csv', 
                  names=['date_sighted', 'city', 'state', 'country',
                         'shape', 'duration', 
                         'duration_txt', 'note', 'date_reported', 
                         'latitude', 'longitude'],
                  parse_dates=['date_sighted', 'date_reported'])

ufo = ufo.reset_index().rename(columns={'index':'ufo_id'})
print(ufo.info())


# %%
def find_dirty_data(col):
    for i, val in enumerate(col):
        try:
            float(val)
        except:
            print('Row {} has dirty data: {}'.format(i, [val]))


# %%
find_dirty_data(ufo['duration'])

# %%
find_dirty_data(ufo['latitude'])

# %%
ufo = ufo.loc[~ufo.index.isin([27822, 35692, 58591, 43782])]
df = ufo.sample(n=1000, random_state=5)

# %%
df['date_sighted'] = df['date_sighted'].astype(str).str.replace('24:00', '00:00')
df['date_sighted'] = pd.to_datetime(df['date_sighted'])

df['duration'] = df['duration'].astype(float)
df['latitude'] = df['latitude'].astype(float)
df.info()

# %% [markdown]
# # Basic plot types

# %% [markdown]
# # Lines: Number of UFOs sighted in each year

# %%
df.head(2)

# %%
# Prep data
line_data = df.groupby(df['date_sighted'].dt.year)[['ufo_id']].count()
line_data

# %%
# A line plot 

# Scale
x_sc = bqplot.LinearScale()
y_sc = bqplot.LinearScale()

# Axis
x_ax = bqplot.Axis(scale=x_sc, label = 'Year Sighted')
y_ax = bqplot.Axis(scale=y_sc, label = 'UFO counts', 
                   orientation='vertical')

# Marks
lines = bqplot.Lines(x=line_data.index, y=line_data['ufo_id'], 
                     scales={'x': x_sc, 'y':y_sc})

# Fig
line_fig = bqplot.Figure(marks=[lines], axes=[x_ax, y_ax])
line_fig

# %%
# See what can be controlled in Marks
lines.traits()

# %%
# See what can be controlled in Axis
x_ax.traits()

# %%
# A line plot 
# - Add points to line
# - Change color
# - rotate x ticks
# - change x ticks text-anchor
# - x label offset
# - Add title to fig

lines.marker = 'circle'
lines.colors = ['red']
x_ax.tick_rotate = 45
x_ax.tick_style = {'text-anchor': 'start'}
x_ax.label_offset = '50'

line_fig.title = 'My Line Plot'

line_fig

# %%
# We can also do these things inline

# Scale
x_sc = bqplot.LinearScale()
y_sc = bqplot.LinearScale()

# Axis
x_ax = bqplot.Axis(scale=x_sc, label = 'Year Sighted', 
                   tick_rotate = 45)
y_ax = bqplot.Axis(scale=y_sc, label = 'UFO counts', 
                   orientation='vertical')

# Marks
lines = bqplot.Lines(x=line_data.index, y=line_data['ufo_id'], 
                     scales={'x': x_sc, 'y':y_sc}, 
                     colors = ['blue'], 
                     marker= 'circle')

# Fig
line_fig = bqplot.Figure(marks=[lines], axes=[x_ax, y_ax])
line_fig

# %% [markdown]
# # Bars: Shapes of UFOs

# %%
# Prep Data
bar_data = df.groupby(['shape'])[['ufo_id']].count()
bar_data

# %%
# A Bar Chart

# Scale
x_sc = bqplot.OrdinalScale()
y_sc = bqplot.LinearScale()

# Axis 
x_ax = bqplot.Axis(scale=x_sc, label='UFO shapes')
y_ax = bqplot.Axis(scale=y_sc, label='UFO counts', orientation='vertical')

# Marks
bars = bqplot.Bars(x=bar_data.index, y=bar_data['ufo_id'], 
                   scales={'x': x_sc, 'y':y_sc})

# Figure
bar_fig = bqplot.Figure(marks=[bars], axes=[x_ax, y_ax])
bar_fig

# %% [markdown]
# # Historgram: Duration in seconds

# %%
# A Hist

# Scale
x_sc = bqplot.LinearScale()
y_sc = bqplot.LinearScale()

# Axis
x_ax = bqplot.Axis(scale=x_sc, label='Duration in seconds')
y_ax = bqplot.Axis(scale=y_sc, label='count', orientation='vertical')

# Mark
hist = bqplot.Hist(sample=df['duration'], 
                   scales={'sample':x_sc, 'count':y_sc}, 
                   bins=50)

# Fig
hist_fig = bqplot.Figure(marks=[hist], axes=[x_ax, y_ax])
hist_fig

# %% [markdown]
# # Scatter: Year sighted and Year reported

# %%
# A basic one

# Scale
x_sc = bqplot.LinearScale()
y_sc = bqplot.LinearScale()

# Axis
x_ax = bqplot.Axis(scale=x_sc, label='Year Sighted')
y_ax = bqplot.Axis(scale=y_sc, label='Year Reported', 
                   orientation='vertical')

# Mark
scatter = bqplot.Scatter(x=df['date_sighted'].dt.year, 
                         y=df['date_reported'].dt.year,
                         scales={'x':x_sc, 'y':y_sc})

# fig
scatter_fig = bqplot.Figure(marks=[scatter], axes=[x_ax, y_ax])
scatter_fig

# %%
# A scatter plot colored by duration in seconds

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

# fig
scatter_fig = bqplot.Figure(marks=[scatter], axes=[x_ax, y_ax, c_ax])
scatter_fig

# %%
np.log10(df['duration'].max())

# %% [markdown]
# # Interaction

# %% [markdown]
# # Pan-zoom

# %%
# Add pan-zoom to line plot

# Scale
x_sc = bqplot.LinearScale()
y_sc = bqplot.LinearScale()

# Axis
x_ax = bqplot.Axis(scale=x_sc, label = 'Year Sighted', 
                   tick_rotate = 45)
y_ax = bqplot.Axis(scale=y_sc, label = 'UFO counts', 
                   orientation='vertical')

# Marks
lines = bqplot.Lines(x=line_data.index, y=line_data['ufo_id'], 
                     scales={'x': x_sc, 'y':y_sc}, 
                     colors = ['blue'], 
                     marker= 'circle')

# Interaction: pan-zoom
panzoom = bqplot.interacts.PanZoom(scales={'x': [x_sc], 
                                           'y': [y_sc]})


# Fig
line_fig = bqplot.Figure(marks=[lines], axes=[x_ax, y_ax], 
                         interaction=panzoom)
line_fig

# %% [markdown]
# # Tooltip

# %%
# See what can be controlled in lines
lines.traits()

# %%
# Add tooptip to line plot

# Scale
x_sc = bqplot.LinearScale()
y_sc = bqplot.LinearScale()

# Axis
x_ax = bqplot.Axis(scale=x_sc, label = 'Year Sighted', 
                   tick_rotate = 45)
y_ax = bqplot.Axis(scale=y_sc, label = 'UFO counts', 
                   orientation='vertical')

# Marks
lines = bqplot.Lines(x=line_data.index, y=line_data['ufo_id'], 
                     scales={'x': x_sc, 'y':y_sc}, 
                     colors = ['blue'], 
                     marker= 'circle')

# Interaction: tooltip

def add_tooltip(chart, d):
    #print(d)
    if 'y' in d['data'].keys():
        my_tooltip = ipywidgets.HTML()
        number_of_ufo = d['data']['y']
        my_tooltip.value = 'Number of UFOs: {}'.format(number_of_ufo)
        lines.tooltip = my_tooltip

lines.on_hover(add_tooltip)

# Fig
line_fig = bqplot.Figure(marks=[lines], axes=[x_ax, y_ax])
line_fig

# %% [markdown]
# # Regenerating hist: Take user input as the number of bins

# %%
# Interactively changing number of bins

# See what can be controlled in hist
hist.traits()

# %%
# Change number of bins
hist.bins = 3
hist_fig

# %%
# ipywidgets.Text
# ipywidgets.Button

text_area = ipywidgets.Text()
text_area

# %%
text_area.value

# %%
my_button = ipywidgets.Button(description='Regenerate!')
my_button

# %%
# Change number of bins by user input

# Scale
x_sc = bqplot.LinearScale()
y_sc = bqplot.LinearScale()

# Axis
x_ax = bqplot.Axis(scale=x_sc, label='Duration in seconds')
y_ax = bqplot.Axis(scale=y_sc, label='count', orientation='vertical')

# Mark
hist = bqplot.Hist(sample=df['duration'], 
                   scales={'sample':x_sc, 'count':y_sc}, 
                   bins=50)

# Interaction: User input

text_area = ipywidgets.Text()
my_button = ipywidgets.Button(description='Regenerate!')

def regenerate_func(button):
    user_input = text_area.value
    user_input = int(user_input)
    hist.bins = user_input

my_button.on_click(regenerate_func)

# Fig
hist_fig = bqplot.Figure(marks=[hist], axes=[x_ax, y_ax])
hist_fig_regen = ipywidgets.VBox([text_area, my_button, hist_fig])
hist_fig_regen

# %% [markdown]
# # Brush selection: Selet an area in a scatter plot

# %%
# Brush, along x

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
my_brush = bqplot.interacts.BrushIntervalSelector(scale=x_sc, 
                                                  marks=[scatter])

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

# %%
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

# %%
