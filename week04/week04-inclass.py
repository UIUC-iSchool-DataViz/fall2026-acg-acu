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
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
#   layout: notebook
#   title: Fonts a lot bigger
# ---

# %% [markdown]
# # Fonts a lot bigger

# %%
import traitlets


# %%
class MusicAlbum(traitlets.HasTraits):
    name = traitlets.Unicode()
    artist = traitlets.Unicode()
    year = traitlets.Int()


# %%
t1989 = MusicAlbum(name = "1989 (Taylor's Version)", artist = "Taylor Swift", year = 2023)

# %%
t1989.name


# %%
def name_changed(change):
    print("The name has changed from ", change['old'], " to ", change['new'])
t1989.observe(name_changed, ["name"])

# %%
t1989.name = "1989 (Taylor's Version (Taylor's Version))"

# %%
t1989.name

# %%
t1989.name = "1989 (Taylor's Version)"

# %%
import random


# %%
class Student(traitlets.HasTraits):
    name = traitlets.Unicode()
    row_and_seat = traitlets.Tuple(
                        traitlets.Unicode(),
                        traitlets.Int()
                    )

    @traitlets.default("row_and_seat")
    def random(self):
        return (random.choice("ABCDEFG"),
                random.randint(1, 15))


# %%
s1 = Student(name = "Matt")
s2 = Student(name = "Esther")
s3 = Student(name = "Unknown")

# %%
s1.row_and_seat

# %%
s2.row_and_seat

# %%
s3.row_and_seat

# %%
s4 = Student()

# %%
traitlets.link( (s1, "name"), (s4, "name") )

# %%
s4.name

# %%
s1.name = "Not Matt"

# %%
s1.name

# %%
s4.name

# %%
s4.name = "Matt"

# %%
s1.name

# %%
import ipywidgets


# %%
@ipywidgets.interact( winner = ["Philadelphia", "Kansas City"] )
def say_winner(winner):
    print("The winner was: ", winner)


# %%
@ipywidgets.interact( winner = ["Philadelphia", "Kansas City"], phil_score = (0, 100), kc_score = (0, 100) )
def say_winner(winner, phil_score, kc_score):
    print("The winner was: ", winner, "with a final score of ", phil_score, "to", kc_score)


# %%
import matplotlib.pyplot as plt


# %%
@ipywidgets.interact(style = plt.style.available)
def make_plot(style):
    with plt.style.context(style):
        plt.plot([1,2,3,4], [5,6,7,5])


# %%
intslider = ipywidgets.IntSlider()

# %%
intslider

# %%
intslider.value

# %%
intslider

# %%
inttext = ipywidgets.IntText()

# %%
inttext

# %%
traitlets.link( ( inttext, "value"), (intslider, "value"))

# %%
intslider.max = 1000

# %%
ipywidgets.SelectionSlider(options = ["hi", "option", "choice", "thing"])

# %%
ta = ipywidgets.Textarea()

# %%
ta

# %%
ta

# %%
ipywidgets.HBox( [
  ipywidgets.Textarea(),
    ipywidgets.VBox([
        ipywidgets.IntSlider(),
        ipywidgets.IntText()
    ])
])

# %%
ipywidgets.HTML(
    "<table><tr><td>Cell 1</td><td>Cell 2</td></tr><tr><td>Row 2 Cell 1</td><td>Row 2 Cell 2</td></tr></table>"
)

# %%
html = ipywidgets.HTML()

# %%
html

# %%
ta = ipywidgets.Textarea()

# %%
traitlets.link((ta, "value"), (html, "value"))

# %%
ta

# %%
button = ipywidgets.Button(description="Increment")

# %%
pbar = ipywidgets.IntProgress()


# %%
def increment_progress(event):
    pbar.value = pbar.value + 1
button.on_click(increment_progress)

# %%
ipywidgets.HBox([pbar, button])

# %%
pbar.value

# %%
pbar.value = 90

# %%
import time

# %%
for i in range(101):
    pbar.value = i
    time.sleep(0.1)

# %%
import bqplot

# %%
import numpy as np

# %%
x = np.mgrid[0.0:10.0:256j]
y = np.sin(x)

# %%
x_sc = bqplot.LinearScale()
y_sc = bqplot.LinearScale()

# %%
x_ax = bqplot.Axis(scale = x_sc)
y_ax = bqplot.Axis(scale = y_sc, orientation = 'vertical')

# %%
lines = bqplot.Lines(x = x, y = y, scales = {'x': x_sc, 'y': y_sc})

# %%
fig = bqplot.Figure(marks = [lines], axes = [x_ax, y_ax])

# %%
fig

# %%
tv = ipywidgets.Text()

# %%
traitlets.link((tv, "value"), (x_ax, "label"))

# %%
tv

# %%
lines.y = np.cos(x)

# %%
fig

# %%
fis = bqplot.interacts.FastIntervalSelector(scale = x_sc)

# %%
fig = bqplot.Figure(marks = [lines], axes = [x_ax, y_ax], interaction = fis)

# %%
fig

# %%
fis.selected

# %%
import pandas as pd

# %%
df = pd.read_csv("building_inventory.csv",
                 na_values = {'Year Acquired': 0, 'Year Constructed': 0},
                 parse_dates = ["Year Acquired", "Year Constructed"])

# %%
x_sc = bqplot.DateScale()
y_sc = bqplot.LinearScale()
x_ax = bqplot.Axis(scale = x_sc)
y_ax = bqplot.Axis(scale = y_sc, orientation = 'vertical')
points = bqplot.Scatter(x = df["Year Acquired"], y = df["Square Footage"], scales = {'x': x_sc, 'y': y_sc})

fig = bqplot.Figure(marks = [points], axes = [x_ax, y_ax])
x_sc.min = df["Year Acquired"].min()

display(fig)

# %%
h = ipywidgets.HTML()
display(h)

# %%
fis = bqplot.interacts.FastIntervalSelector(scale = x_sc)

# %%
fig.interaction = fis


# %%
def on_change_selection(change):
    h.value = str(df["Square Footage"][((df["Year Acquired"] > fis.selected[0]) & (df["Year Acquired"] < fis.selected[1]))].sum())
fis.observe(on_change_selection, ["selected"])

# %%
fis.selected

# %%
df["Square Footage"][((df["Year Acquired"] > fis.selected[0]) & (df["Year Acquired"] < fis.selected[1]))].sum()

# %%
fig

# %%
ipywidgets.HBox([fig, fig])

# %%
x_sc = bqplot.DateScale()
y_sc = bqplot.LinearScale()
x_ax = bqplot.Axis(scale = x_sc)
y_ax = bqplot.Axis(scale = y_sc, orientation = 'vertical')
points = bqplot.Scatter(x = df["Year Acquired"], y = df["Square Footage"], scales = {'x': x_sc, 'y': y_sc})
pz = bqplot.interacts.PanZoom(scales = {'x': [x_sc], 'y': [y_sc]})
fig = bqplot.Figure(marks = [points], axes = [x_ax, y_ax], interaction = pz)
x_sc.min = df["Year Acquired"].min()

display(fig)

# %%
