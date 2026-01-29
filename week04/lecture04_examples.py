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
#   title: UNGRADED Workbook for In-Class
# ---

# %% [markdown]
# # UNGRADED Workbook for In-Class
#
# This notebook is here for you to "code along" during class. 
#
# It will not be graded, so feel free to play around!

# %%
import ipympl

# %%
import traitlets
import numpy as np


# %%
# %matplotlib ipympl

# %%
def something():
    return 2


# %%
class Album:
    def __init__(self, name, artist):
        self.name = name
        self.artist = artist


# %%
ttpd = Album("The Tortured Poets' Department", "Taylor Swift")

# %%
ttpd.name

# %%
ttpd.artist

# %%
ttpdtv = Album("The Tortured Poets' Department (Taylor's Version)", "Taylor Swift")

# %%
ttpdtv.name

# %%
ttpd.name

# %%
ttpd.rating = "A++++++"

# %%
ttpd.rating = 1.5


# %%
class AlbumCollection:
    def __init__(self, albums):
        self.albums = albums
        
    def average_rating(self):
        rating = 0
        for album in self.albums:
            rating += album.rating
        return rating / len(self.albums)


# %%
my_coll = AlbumCollection([ttpd, ttpdtv])

# %%
my_coll.average_rating()

# %%
import traitlets


# %%
class MusicAlbum(traitlets.HasTraits):
    name = traitlets.Unicode()
    artist = traitlets.Unicode()
    year_released = traitlets.Int()


# %%
speak_now = MusicAlbum(name = "Speak Now", artist = "Taylor Swift", year_released = 2010)

# %%
speak_now.artist

# %%
speak_now = MusicAlbum(name = "Speak Now", artist = "Taylor Swift", year_released = "2010")


# %%
class MusicAlbum(traitlets.HasTraits):
    name = traitlets.Unicode()
    artist = traitlets.Unicode()
    year_released = traitlets.CInt()


# %%
speak_now = MusicAlbum(name = "Speak Now", artist = "Taylor Swift", year_released = "2010")

# %%
speak_now.year_released


# %%
class AlbumCollection(traitlets.HasTraits):
    albums = traitlets.List(trait = traitlets.Instance(MusicAlbum))


# %%
my_collection = AlbumCollection(albums = [speak_now])


# %%
def name_changed(change):
    print("The name has been changed from '%s' to '%s'" % (change['old'], change['new']))


# %%
speak_now.observe(name_changed, ['name'])

# %%
speak_now.name = "Speak Now (Original Version)"

# %%
red = MusicAlbum(name = "Red", artist = "Taylor Swift", year_released = 2012)

# %%
red.name = "Red (Original Version)"

# %%
speak_now.name = "Speak Now (Original Version)"


# %%
class SomeObject(traitlets.HasTraits):
    name = traitlets.Unicode("Unknown")
    row = traitlets.CInt(1)



# %%
s = SomeObject()
s.row, s.name

# %%
import random


# %%
class SomeObject(traitlets.HasTraits):
    name = traitlets.Unicode("Unknown")
    row = traitlets.CInt(1)

    @traitlets.default("name")
    def _default_name(self):
        return random.choice([
            "Matt", "Other Matt", "Matt Alpha", "Matt One", "Matt Prime", "Zeta Matt"
        ])


# %%
obj1 = SomeObject()
obj2 = SomeObject()
obj3 = SomeObject()

# %%
obj1.name, obj2.name, obj3.name

# %%
import pandas as pd


# %%
class MyDataFramePlot(traitlets.HasTraits):
    df = traitlets.Instance(pd.DataFrame)
    plotted_x_axis = traitlets.Unicode()
    
    @traitlets.default("plotted_x_axis")
    def _default_plotted_x_axis(self):
        return self.df["Something"].value_count(1)[0]
    


# %%
class Student(traitlets.HasTraits):
    name = traitlets.Unicode()
    
s1 = Student(name = "Someone's Name")
s2 = Student(name = "")

# %%
s1.name, s2.name

# %%
traitlets.link(
    (s1, "name"),
    (s2, "name")
)

# %%
s2.name

# %%
s1.name = "My Name"

# %%
s2.name

# %%
s2.name = "No, it's my name"

# %%
s1.name

# %%
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

# %%
s3.name

# %%
s4.name

# %%
s4.name = "Not actually Matt"

# %%
s3.name


# %%
class KeepsAnInt(traitlets.HasTraits):
    value = traitlets.Int()
    
class KeepsAString(traitlets.HasTraits):
    value = traitlets.Unicode()



# %%
v1 = KeepsAnInt(value = 0)
v2 = KeepsAString()

traitlets.link((v1, "value"), (v2, "value"), (str, int))

# %%
v1.value

# %%
v2.value

# %%
v2.value = "2024"

# %%
v1.value

# %%
import ipywidgets


# %%
@ipywidgets.interact(name = ['Weezer', 'Nerf Herder', 'Mustard Plug'])
def print_bandname(name):
    print(name)


# %%
import matplotlib.pyplot as plt


# %%
@ipywidgets.interact(style = plt.style.available)
def make_plot(style):
    with plt.style.context(style):
        plt.plot([1,2,3,4], [5, 6, 7, 8])


# %%
@ipywidgets.interact(name = "Name", my_range = (0, 10, 0.1), other = [1, 2, 3, 60], v = False)
def widget_demo(name, my_range, other, v):
    print(name, my_range, other, v)


# %%
w1 = ipywidgets.BoundedIntText(min = -10, max = 10)

# %%
w1

# %%
w1

# %%
w1.value

# %%
w2 = ipywidgets.IntSlider(min = -10, max = 10)
traitlets.link((w1, 'value'), (w2, 'value'))

# %%
w2

# %%
pb = ipywidgets.IntProgress(min = 0, max=100)

# %%
pb

# %%
import time

# %%
for i in range(101):
    pb.value = i
    time.sleep(0.1)

# %%
w2.value

# %%
l = ipywidgets.Label()

# %%
l

# %%
l.value = "Hi"

# %%
traitlets.link(
  (w2, "value"), (l, "value"),
  (str, int)
)

# %%
import numpy as np


# %%
@ipywidgets.interact(left_edge = (-10.0, 0.0, 0.1), right_edge = (0.0, 10.0, 0.1), factor = (0.1, 5, 0.01))
def make_plot(left_edge, right_edge, factor):
    x = np.mgrid[left_edge:right_edge:100j]
    y = np.sin(factor * x)
    plt.plot(x, y)


# %%
ipywidgets.ToggleButtons(options = ["Hi", "There", "Folks"])

# %%
ipywidgets.Checkbox(description = "Should we?")

# %%
ipywidgets.Textarea(value = "Write your text here", description = "What are you going to do today?")

# %%
w2

# %%
w2.orientation = 'vertical'

# %%
w2.description = "Something"

# %%
w2.min = -10

# %%
dd = ipywidgets.Dropdown(
  options = [("Red", "#ff0000"), ("Green", "#00ff00"), ("Blue", "#0000ff")]
)

# %%
dd

# %%
dd.value

# %%
sm = ipywidgets.SelectMultiple(options = ["Red", "Green", "Blue"])
sm

# %%
sm.value

# %%
ipywidgets.RadioButtons(options = ["Red", "Green", "Blue"])

# %%
ipywidgets.HBox([
    w2, dd, sm
])

# %%
ipywidgets.VBox([
    w2, dd, sm
])

# %%
ipywidgets.HBox([
    ipywidgets.VBox([
        dd, sm
    ]),
    w2,
])

# %%
t = ipywidgets.Tab(
  [dd, w2, sm]
)
t.set_title(0, "dd")
t.set_title(1, "w2")
t.set_title(2, "sm")

# %%
t

# %%
cp = ipywidgets.ColorPicker()

# %%
# cp

# %%
cp.value

# %%
cp.disabled = False

# %%
ipywidgets.FileUpload()

# %%
d = ipywidgets.DatePicker()

# %%
d

# %%
d.value

# %%
dt = ipywidgets.DatePicker()

# %%
dt

# %%
val = open("winter_scene.png", "rb").read()

# %%
im = ipywidgets.Image(value = val)

# %%
im

# %%
im.value = open("stitch_reworked.png", "rb").read()

# %%
f = ipywidgets.FileUpload()

# %%
f

# %%
im.value = f.value['winter_scene.png']['content']

# %%
x = np.mgrid[0:1000000]
y = np.sin(x) * 100

# %%
import IPython.display

# %%
IPython.display.Markdown(r"""
# This is a markdown

All my stuff goes in here

""")

# %%
IPython.display.HTML("<b>Hi!</b>")

# %%
output = ipywidgets.Output()

# %%
display(output)

# %%
output.clear_output()

# %%
b = ipywidgets.Button(description = "Hi")

# %%
b

# %%
b.button_style="info"

# %%
b.on_click


# %%
def clicked(event):
    print("Clicked!")


# %%
b.on_click(clicked)


# %%
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


# %%
rnp = RandomNumberPlot()

# %%
rnp

# %%
a = ipywidgets.VBox()

# %%
a.layout.traits()

# %%
