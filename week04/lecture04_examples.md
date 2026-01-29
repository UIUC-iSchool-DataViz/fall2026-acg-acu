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
  title: UNGRADED Workbook for In-Class
---

# UNGRADED Workbook for In-Class

This notebook is here for you to "code along" during class. 

It will not be graded, so feel free to play around!

```python
import ipympl
```

```python
import traitlets
import numpy as np
```

```python
%matplotlib ipympl
```

```python
def something():
    return 2
```

```python
class Album:
    def __init__(self, name, artist):
        self.name = name
        self.artist = artist
```

```python
ttpd = Album("The Tortured Poets' Department", "Taylor Swift")
```

```python
ttpd.name
```

```python
ttpd.artist
```

```python
ttpdtv = Album("The Tortured Poets' Department (Taylor's Version)", "Taylor Swift")
```

```python
ttpdtv.name
```

```python
ttpd.name
```

```python
ttpd.rating = "A++++++"
```

```python
ttpd.rating = 1.5
```

```python
class AlbumCollection:
    def __init__(self, albums):
        self.albums = albums
        
    def average_rating(self):
        rating = 0
        for album in self.albums:
            rating += album.rating
        return rating / len(self.albums)
```

```python
my_coll = AlbumCollection([ttpd, ttpdtv])
```

```python
my_coll.average_rating()
```

```python
import traitlets
```

```python
class MusicAlbum(traitlets.HasTraits):
    name = traitlets.Unicode()
    artist = traitlets.Unicode()
    year_released = traitlets.Int()
```

```python
speak_now = MusicAlbum(name = "Speak Now", artist = "Taylor Swift", year_released = 2010)
```

```python
speak_now.artist
```

```python
speak_now = MusicAlbum(name = "Speak Now", artist = "Taylor Swift", year_released = "2010")
```

```python
class MusicAlbum(traitlets.HasTraits):
    name = traitlets.Unicode()
    artist = traitlets.Unicode()
    year_released = traitlets.CInt()
```

```python
speak_now = MusicAlbum(name = "Speak Now", artist = "Taylor Swift", year_released = "2010")
```

```python
speak_now.year_released
```

```python
class AlbumCollection(traitlets.HasTraits):
    albums = traitlets.List(trait = traitlets.Instance(MusicAlbum))
```

```python
my_collection = AlbumCollection(albums = [speak_now])
```

```python
def name_changed(change):
    print("The name has been changed from '%s' to '%s'" % (change['old'], change['new']))
```

```python
speak_now.observe(name_changed, ['name'])
```

```python
speak_now.name = "Speak Now (Original Version)"
```

```python
red = MusicAlbum(name = "Red", artist = "Taylor Swift", year_released = 2012)
```

```python
red.name = "Red (Original Version)"
```

```python
speak_now.name = "Speak Now (Original Version)"
```

```python
class SomeObject(traitlets.HasTraits):
    name = traitlets.Unicode("Unknown")
    row = traitlets.CInt(1)


```

```python
s = SomeObject()
s.row, s.name
```

```python
import random
```

```python
class SomeObject(traitlets.HasTraits):
    name = traitlets.Unicode("Unknown")
    row = traitlets.CInt(1)

    @traitlets.default("name")
    def _default_name(self):
        return random.choice([
            "Matt", "Other Matt", "Matt Alpha", "Matt One", "Matt Prime", "Zeta Matt"
        ])
```

```python
obj1 = SomeObject()
obj2 = SomeObject()
obj3 = SomeObject()
```

```python
obj1.name, obj2.name, obj3.name
```

```python
import pandas as pd
```

```python
class MyDataFramePlot(traitlets.HasTraits):
    df = traitlets.Instance(pd.DataFrame)
    plotted_x_axis = traitlets.Unicode()
    
    @traitlets.default("plotted_x_axis")
    def _default_plotted_x_axis(self):
        return self.df["Something"].value_count(1)[0]
    

```

```python
class Student(traitlets.HasTraits):
    name = traitlets.Unicode()
    
s1 = Student(name = "Someone's Name")
s2 = Student(name = "")
```

```python
s1.name, s2.name
```

```python
traitlets.link(
    (s1, "name"),
    (s2, "name")
)
```

```python
s2.name
```

```python
s1.name = "My Name"
```

```python
s2.name
```

```python
s2.name = "No, it's my name"
```

```python
s1.name
```

```python
s3 = Student(name = "")
s4 = Student(name = "")

def from_first_to_second(value):
    return "Not actually " + value

def from_second_to_first(value):
    if value.startswith("Not actually "):
        return value[len("Not actually "):]
    else:
        return "Yes actually " + value

traitlets.link(
    (s3, "name"),
    (s4, "name"),
    (from_first_to_second, from_second_to_first)
)
```

```python
s3.name
```

```python
s4.name
```

```python
s4.name = "Not actually Matt"
```

```python
s3.name
```

```python
class KeepsAnInt(traitlets.HasTraits):
    value = traitlets.Int()
    
class KeepsAString(traitlets.HasTraits):
    value = traitlets.Unicode()


```

```python
v1 = KeepsAnInt(value = 0)
v2 = KeepsAString()

traitlets.link((v1, "value"), (v2, "value"), (str, int))
```

```python
v1.value
```

```python
v2.value
```

```python
v2.value = "2024"
```

```python
v1.value
```

```python
import ipywidgets
```

```python
@ipywidgets.interact(name = ['Weezer', 'Nerf Herder', 'Mustard Plug'])
def print_bandname(name):
    print(name)
```

```python
import matplotlib.pyplot as plt
```

```python
@ipywidgets.interact(style = plt.style.available)
def make_plot(style):
    with plt.style.context(style):
        plt.plot([1,2,3,4], [5, 6, 7, 8])
```

```python
@ipywidgets.interact(name = "Name", my_range = (0, 10, 0.1), other = [1, 2, 3, 60], v = False)
def widget_demo(name, my_range, other, v):
    print(name, my_range, other, v)
```

```python
w1 = ipywidgets.BoundedIntText(min = -10, max = 10)
```

```python
w1
```

```python
w1
```

```python
w1.value
```

```python
w2 = ipywidgets.IntSlider(min = -10, max = 10)
traitlets.link((w1, 'value'), (w2, 'value'))
```

```python
w2
```

```python
pb = ipywidgets.IntProgress(min = 0, max=100)
```

```python
pb
```

```python
import time
```

```python
for i in range(101):
    pb.value = i
    time.sleep(0.1)
```

```python
w2.value
```

```python
l = ipywidgets.Label()
```

```python
l
```

```python
l.value = "Hi"
```

```python
traitlets.link(
  (w2, "value"), (l, "value"),
  (str, int)
)
```

```python
import numpy as np
```

```python
@ipywidgets.interact(left_edge = (-10.0, 0.0, 0.1), right_edge = (0.0, 10.0, 0.1), factor = (0.1, 5, 0.01))
def make_plot(left_edge, right_edge, factor):
    x = np.mgrid[left_edge:right_edge:100j]
    y = np.sin(factor * x)
    plt.plot(x, y)
```

```python
ipywidgets.ToggleButtons(options = ["Hi", "There", "Folks"])
```

```python
ipywidgets.Checkbox(description = "Should we?")
```

```python
ipywidgets.Textarea(value = "Write your text here", description = "What are you going to do today?")
```

```python
w2
```

```python
w2.orientation = 'vertical'
```

```python
w2.description = "Something"
```

```python
w2.min = -10
```

```python
dd = ipywidgets.Dropdown(
  options = [("Red", "#ff0000"), ("Green", "#00ff00"), ("Blue", "#0000ff")]
)
```

```python
dd
```

```python
dd.value
```

```python
sm = ipywidgets.SelectMultiple(options = ["Red", "Green", "Blue"])
sm
```

```python
sm.value
```

```python
ipywidgets.RadioButtons(options = ["Red", "Green", "Blue"])
```

```python
ipywidgets.HBox([
    w2, dd, sm
])
```

```python
ipywidgets.VBox([
    w2, dd, sm
])
```

```python
ipywidgets.HBox([
    ipywidgets.VBox([
        dd, sm
    ]),
    w2,
])
```

```python
t = ipywidgets.Tab(
  [dd, w2, sm]
)
t.set_title(0, "dd")
t.set_title(1, "w2")
t.set_title(2, "sm")
```

```python
t
```

```python
cp = ipywidgets.ColorPicker()
```

```python
cp
```

```python
cp.value
```

```python
cp.disabled = False
```

```python
ipywidgets.FileUpload()
```

```python
d = ipywidgets.DatePicker()
```

```python
d
```

```python
d.value
```

```python
dt = ipywidgets.DatePicker()
```

```python
dt
```

```python
val = open("winter_scene.png", "rb").read()
```

```python
im = ipywidgets.Image(value = val)
```

```python
im
```

```python
im.value = open("stitch_reworked.png", "rb").read()
```

```python
f = ipywidgets.FileUpload()
```

```python
f
```

```python
im.value = f.value['winter_scene.png']['content']
```

```python
x = np.mgrid[0:1000000]
y = np.sin(x) * 100
```

```python
import IPython.display
```

```python
IPython.display.Markdown(r"""
# This is a markdown

All my stuff goes in here

""")
```

```python
IPython.display.HTML("<b>Hi!</b>")
```

```python
output = ipywidgets.Output()
```

```python
display(output)
```

```python
output.clear_output()
```

```python
b = ipywidgets.Button(description = "Hi")
```

```python
b
```

```python
b.button_style="info"
```

```python
b.on_click
```

```python
def clicked(event):
    print("Clicked!")
```

```python
b.on_click(clicked)
```

```python
class RandomNumberPlot(traitlets.HasTraits):
    center = traitlets.Float(0.0)
    width = traitlets.Float(10.0)
    color = traitlets.Unicode("#ff0000")
    size = traitlets.Int(256, min=1, max=256*256)
    x = traitlets.Instance(np.ndarray)
    y = traitlets.Instance(np.ndarray)
    
    @traitlets.default("x")
    def random_series_x(self):
        return np.random.normal(self.center, self.width, self.size)
    
    @traitlets.default("y")
    def random_series_y(self):
        return np.random.normal(self.center, self.width, self.size)
    
    def _ipython_display_(self):
        center = ipywidgets.FloatSlider(description = "Center")
        traitlets.link((self, 'center'), (center, 'value'))
        width = ipywidgets.FloatSlider(description = "Width")
        traitlets.link((self, 'width'), (width, "value"))
        
        size = ipywidgets.IntSlider(description = "Size",
                                    min = 1, max=256*256)
        traitlets.link((self, 'size'), (size, 'value'))
        
        color = ipywidgets.ColorPicker(description = "color")
        traitlets.link((self, 'color'), (color, 'value'))
        
        replot = ipywidgets.Button(description = "Replot")
        
        plot_output = ipywidgets.Output()
        def update_plot(event):
            self.x = self.random_series_x()
            self.y = self.random_series_y()
            plot_output.clear_output()
            with plot_output:
                fig, ax = plt.subplots()
                ax.scatter(self.x, self.y, color = self.color, s = 0.1)
        replot.on_click(update_plot)
        im = ipywidgets.Image(height = 300, width=300)
        display(
            ipywidgets.HBox([
                ipywidgets.VBox([center, width, size, color, replot], layout = {'border': '1px solid green',
                                                                                'align_items': 'center'}),
                plot_output
            ], layout = {'border': '1px solid black'})
        )
```

```python
rnp = RandomNumberPlot()
```

```python
rnp
```

```python
a = ipywidgets.VBox()
```

```python
a.layout.traits()
```

```python

```
