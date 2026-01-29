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
  title: Fonts a lot bigger
---

# Fonts a lot bigger

```python
import traitlets
```

```python
class MusicAlbum(traitlets.HasTraits):
    name = traitlets.Unicode()
    artist = traitlets.Unicode()
    year = traitlets.Int()
```

```python
t1989 = MusicAlbum(name = "1989 (Taylor's Version)", artist = "Taylor Swift", year = 2023)
```

```python
t1989.name
```

```python
def name_changed(change):
    print("The name has changed from ", change['old'], " to ", change['new'])
t1989.observe(name_changed, ["name"])
```

```python
t1989.name = "1989 (Taylor's Version (Taylor's Version))"
```

```python
t1989.name
```

```python
t1989.name = "1989 (Taylor's Version)"
```

```python
import random
```

```python
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
```

```python
s1 = Student(name = "Matt")
s2 = Student(name = "Esther")
s3 = Student(name = "Unknown")
```

```python
s1.row_and_seat
```

```python
s2.row_and_seat
```

```python
s3.row_and_seat
```

```python
s4 = Student()
```

```python
traitlets.link( (s1, "name"), (s4, "name") )
```

```python
s4.name
```

```python
s1.name = "Not Matt"
```

```python
s1.name
```

```python
s4.name
```

```python
s4.name = "Matt"
```

```python
s1.name
```

```python
import ipywidgets
```

```python
@ipywidgets.interact( winner = ["Philadelphia", "Kansas City"] )
def say_winner(winner):
    print("The winner was: ", winner)
```

```python
@ipywidgets.interact( winner = ["Philadelphia", "Kansas City"], phil_score = (0, 100), kc_score = (0, 100) )
def say_winner(winner, phil_score, kc_score):
    print("The winner was: ", winner, "with a final score of ", phil_score, "to", kc_score)
```

```python
import matplotlib.pyplot as plt
```

```python
@ipywidgets.interact(style = plt.style.available)
def make_plot(style):
    with plt.style.context(style):
        plt.plot([1,2,3,4], [5,6,7,5])
```

```python
intslider = ipywidgets.IntSlider()
```

```python
intslider
```

```python
intslider.value
```

```python
intslider
```

```python
inttext = ipywidgets.IntText()
```

```python
inttext
```

```python
traitlets.link( ( inttext, "value"), (intslider, "value"))
```

```python
intslider.max = 1000
```

```python
ipywidgets.SelectionSlider(options = ["hi", "option", "choice", "thing"])
```

```python
ta = ipywidgets.Textarea()
```

```python
ta
```

```python
ta
```

```python
ipywidgets.HBox( [
  ipywidgets.Textarea(),
    ipywidgets.VBox([
        ipywidgets.IntSlider(),
        ipywidgets.IntText()
    ])
])
```

```python
ipywidgets.HTML(
    "<table><tr><td>Cell 1</td><td>Cell 2</td></tr><tr><td>Row 2 Cell 1</td><td>Row 2 Cell 2</td></tr></table>"
)
```

```python
html = ipywidgets.HTML()
```

```python
html
```

```python
ta = ipywidgets.Textarea()
```

```python
traitlets.link((ta, "value"), (html, "value"))
```

```python
ta
```

```python
button = ipywidgets.Button(description="Increment")
```

```python
pbar = ipywidgets.IntProgress()
```

```python
def increment_progress(event):
    pbar.value = pbar.value + 1
button.on_click(increment_progress)
```

```python
ipywidgets.HBox([pbar, button])
```

```python
pbar.value
```

```python
pbar.value = 90
```

```python
import time
```

```python
for i in range(101):
    pbar.value = i
    time.sleep(0.1)
```

```python
import bqplot
```

```python
import numpy as np
```

```python
x = np.mgrid[0.0:10.0:256j]
y = np.sin(x)
```

```python
x_sc = bqplot.LinearScale()
y_sc = bqplot.LinearScale()
```

```python
x_ax = bqplot.Axis(scale = x_sc)
y_ax = bqplot.Axis(scale = y_sc, orientation = 'vertical')
```

```python
lines = bqplot.Lines(x = x, y = y, scales = {'x': x_sc, 'y': y_sc})
```

```python
fig = bqplot.Figure(marks = [lines], axes = [x_ax, y_ax])
```

```python
fig
```

```python
tv = ipywidgets.Text()
```

```python
traitlets.link((tv, "value"), (x_ax, "label"))
```

```python
tv
```

```python
lines.y = np.cos(x)
```

```python
fig
```

```python
fis = bqplot.interacts.FastIntervalSelector(scale = x_sc)
```

```python
fig = bqplot.Figure(marks = [lines], axes = [x_ax, y_ax], interaction = fis)
```

```python
fig
```

```python
fis.selected
```

```python
import pandas as pd
```

```python
df = pd.read_csv("building_inventory.csv",
                 na_values = {'Year Acquired': 0, 'Year Constructed': 0},
                 parse_dates = ["Year Acquired", "Year Constructed"])
```

```python
x_sc = bqplot.DateScale()
y_sc = bqplot.LinearScale()
x_ax = bqplot.Axis(scale = x_sc)
y_ax = bqplot.Axis(scale = y_sc, orientation = 'vertical')
points = bqplot.Scatter(x = df["Year Acquired"], y = df["Square Footage"], scales = {'x': x_sc, 'y': y_sc})

fig = bqplot.Figure(marks = [points], axes = [x_ax, y_ax])
x_sc.min = df["Year Acquired"].min()

display(fig)
```

```python
h = ipywidgets.HTML()
display(h)
```

```python
fis = bqplot.interacts.FastIntervalSelector(scale = x_sc)
```

```python
fig.interaction = fis
```

```python
def on_change_selection(change):
    h.value = str(df["Square Footage"][((df["Year Acquired"] > fis.selected[0]) & (df["Year Acquired"] < fis.selected[1]))].sum())
fis.observe(on_change_selection, ["selected"])
```

```python
fis.selected
```

```python
df["Square Footage"][((df["Year Acquired"] > fis.selected[0]) & (df["Year Acquired"] < fis.selected[1]))].sum()
```

```python
fig
```

```python
ipywidgets.HBox([fig, fig])
```

```python
x_sc = bqplot.DateScale()
y_sc = bqplot.LinearScale()
x_ax = bqplot.Axis(scale = x_sc)
y_ax = bqplot.Axis(scale = y_sc, orientation = 'vertical')
points = bqplot.Scatter(x = df["Year Acquired"], y = df["Square Footage"], scales = {'x': x_sc, 'y': y_sc})
pz = bqplot.interacts.PanZoom(scales = {'x': [x_sc], 'y': [y_sc]})
fig = bqplot.Figure(marks = [points], axes = [x_ax, y_ax], interaction = pz)
x_sc.min = df["Year Acquired"].min()

display(fig)
```

```python

```
