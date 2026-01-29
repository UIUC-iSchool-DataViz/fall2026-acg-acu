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
#   title: Ipywidgets Intro
# ---

# %%
import traitlets


# %%
class MusicAlbum:
    pass

simple_album = MusicAlbum()
simple_album.year_released = 2010
simple_album.artist = "Taylor Swift"
simple_album.name = "Speak Now"

# %%
simple_album.year_released = "fourteen years ago"

# %%
simple_album.year_released


# %%
class MusicAlbum(traitlets.HasTraits):
    year_released = traitlets.Int()
    artist = traitlets.Unicode()
    name = traitlets.Unicode()


# %%
speak_now = MusicAlbum(artist = "Taylor Swift", name = "Speak Now", year_released = 2010)

# %%
speak_now.artist

# %%
speak_now.year_released = "fourteen years ago"


# %%
def show_change(change):
    print("Changed {name} from {old} to {new}".format(**change))
speak_now.observe(show_change, ["name", "year_released", "artist"])

# %%
speak_now.year_released = 2011

# %%
speak_now.year_released = 2023
speak_now.name = speak_now.name + " (Taylor's Version)"

# %%
speak_now.year_released

# %%
import random


# %%
class Student(traitlets.HasTraits):
    name = traitlets.Unicode()
    row_and_seat = traitlets.Tuple(
                        traitlets.Unicode(),
                        traitlets.Int()
                    )
    height = traitlets.Unicode("average")
    group_name = traitlets.Unicode()

    @traitlets.default("row_and_seat")
    def random(self):
        return (random.choice("ABCDEFG"),
                random.randint(1, 15))


# %%
s1, s2, s3 = Student(), Student(), Student()

# %%
s1.row_and_seat, s2.row_and_seat, s3.row_and_seat

# %%
s1.height

# %%
s4 = Student(row_and_seat = ('B', 1), height = "tall" )

# %%
s4.row_and_seat, s4.height

# %%
s4.traits()

# %%
s1.group_name

# %%
s2.group_name

# %%
traitlets.link( (s1, "group_name"), (s2, "group_name") )

# %%
s1.group_name = "The Mongooses"

# %%
s1.group_name

# %%
s2.group_name

# %%
s2.group_name = "Universe A"

# %%
s2.group_name

# %%
s1.group_name


# %%
class Group(traitlets.HasTraits):
    name = traitlets.Unicode()
g = Group(name = "Universe One")

# %%
traitlets.link( (s3, "group_name"), (g, "name"))

# %%
s3.group_name

# %%
g.name

# %%
g.name = "Universe One"

# %%
s3.group_name


# %%
def print_band_name(name):
    print("Band name is ", name)


# %%
print_band_name("The Hives")

# %%
print_band_name("Project")

# %%
import ipywidgets


# %%
@ipywidgets.interact(name = ["The Hives", "The Kingsmen", "The Breeders"])
def print_band_name(name):
    print("Band name is ", name)


# %%
@ipywidgets.interact(name = "stuff")
def print_band_name(name):
    print("Band name is ", name)


# %%
@ipywidgets.interact(divisor = (1, 100, .1))
def divide_by_divisor(divisor):
    print("Some value ", 217, "divided by", divisor, " = ", 217 / divisor)


# %%
import matplotlib.pyplot as plt

# %%
plt.style.available


# %%
@ipywidgets.interact(style = plt.style.available)
def example_plot(style):
    with plt.style.context(style):
        plt.plot([1, 2, 5.3, 9], [4, 2.1, 9, 0.4])


# %%
int_slider = ipywidgets.IntSlider(min = -100, max = 101)

# %%
int_slider

# %%
int_slider.min, int_slider.max

# %%
int_slider.value

# %%
bounded_int = ipywidgets.BoundedIntText(min = -100, max = 101)

# %%
bounded_int

# %%
traitlets.link((int_slider, 'value'), (bounded_int, 'value'))

# %%
irs = ipywidgets.IntRangeSlider(min = -1000)

# %%
irs.value


# %%
@ipywidgets.interact(bounds = irs)
def show_bounds(bounds):
    print("Spanning ", bounds[0], "to", bounds[1])


# %%
cp = ipywidgets.ColorPicker()
# cp

# %%
cp.value

# %%
ipywidgets.DatePicker()

# %%
ipywidgets.Controller()

# %%
html = ipywidgets.HTML()

# %%
html

# %%
ta = ipywidgets.Textarea()
ta

# %%
ta

# %%
ta.value

# %%
traitlets.link((html, "value"), (ta, "value"))

# %%
sliders = [ipywidgets.IntSlider() for _ in range(10)]

# %%
ipywidgets.HBox(sliders)

# %%
ipywidgets.VBox(sliders)

# %%
our_display = ipywidgets.HTML()

# %%
our_display

# %%
traitlets.link((speak_now, "name"), (our_display, "value"))

# %%
speak_now.name = "Speak Now (Taylor's Version (Taylor's Version))"

# %%
my_button = ipywidgets.Button(description = "Click on me!")

# %%
my_button


# %%
class Counter(traitlets.HasTraits):
    num_clicks = traitlets.Int()


# %%
counter = Counter()

def click_button(b):
    counter.num_clicks += 1

my_button.on_click(click_button)

# %%
counter.num_clicks

# %%

# %%
l = ipywidgets.Label()
traitlets.link((counter, "num_clicks"), (l, "value"), (lambda a: str(a), lambda a: int(a)))

# %%
l

# %%
l.value = "15"

# %%
counter.num_clicks

# %%
