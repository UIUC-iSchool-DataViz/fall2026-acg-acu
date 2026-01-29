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
  title: Ipywidgets Intro
---

```python
import traitlets
```

```python
class MusicAlbum:
    pass

simple_album = MusicAlbum()
simple_album.year_released = 2010
simple_album.artist = "Taylor Swift"
simple_album.name = "Speak Now"
```

```python
simple_album.year_released = "fourteen years ago"
```

```python
simple_album.year_released
```

```python
class MusicAlbum(traitlets.HasTraits):
    year_released = traitlets.Int()
    artist = traitlets.Unicode()
    name = traitlets.Unicode()
```

```python
speak_now = MusicAlbum(artist = "Taylor Swift", name = "Speak Now", year_released = 2010)
```

```python
speak_now.artist
```

```python
speak_now.year_released = "fourteen years ago"
```

```python
def show_change(change):
    print("Changed {name} from {old} to {new}".format(**change))
speak_now.observe(show_change, ["name", "year_released", "artist"])
```

```python
speak_now.year_released = 2011
```

```python
speak_now.year_released = 2023
speak_now.name = speak_now.name + " (Taylor's Version)"
```

```python
speak_now.year_released
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
    height = traitlets.Unicode("average")
    group_name = traitlets.Unicode()

    @traitlets.default("row_and_seat")
    def random(self):
        return (random.choice("ABCDEFG"),
                random.randint(1, 15))
```

```python
s1, s2, s3 = Student(), Student(), Student()
```

```python
s1.row_and_seat, s2.row_and_seat, s3.row_and_seat
```

```python
s1.height
```

```python
s4 = Student(row_and_seat = ('B', 1), height = "tall" )
```

```python
s4.row_and_seat, s4.height
```

```python
s4.traits()
```

```python
s1.group_name
```

```python
s2.group_name
```

```python
traitlets.link( (s1, "group_name"), (s2, "group_name") )
```

```python
s1.group_name = "The Mongooses"
```

```python
s1.group_name
```

```python
s2.group_name
```

```python
s2.group_name = "Universe A"
```

```python
s2.group_name
```

```python
s1.group_name
```

```python
class Group(traitlets.HasTraits):
    name = traitlets.Unicode()
g = Group(name = "Universe One")
```

```python
traitlets.link( (s3, "group_name"), (g, "name"))
```

```python
s3.group_name
```

```python
g.name
```

```python
g.name = "Universe One"
```

```python
s3.group_name
```

```python
def print_band_name(name):
    print("Band name is ", name)
```

```python
print_band_name("The Hives")
```

```python
print_band_name("Project")
```

```python
import ipywidgets
```

```python
@ipywidgets.interact(name = ["The Hives", "The Kingsmen", "The Breeders"])
def print_band_name(name):
    print("Band name is ", name)
```

```python
@ipywidgets.interact(name = "stuff")
def print_band_name(name):
    print("Band name is ", name)
```

```python
@ipywidgets.interact(divisor = (1, 100, .1))
def divide_by_divisor(divisor):
    print("Some value ", 217, "divided by", divisor, " = ", 217 / divisor)
```

```python
import matplotlib.pyplot as plt
```

```python
plt.style.available
```

```python
@ipywidgets.interact(style = plt.style.available)
def example_plot(style):
    with plt.style.context(style):
        plt.plot([1, 2, 5.3, 9], [4, 2.1, 9, 0.4])
```

```python
int_slider = ipywidgets.IntSlider(min = -100, max = 101)
```

```python
int_slider
```

```python
int_slider.min, int_slider.max
```

```python
int_slider.value
```

```python
bounded_int = ipywidgets.BoundedIntText(min = -100, max = 101)
```

```python
bounded_int
```

```python
traitlets.link((int_slider, 'value'), (bounded_int, 'value'))
```

```python
irs = ipywidgets.IntRangeSlider(min = -1000)
```

```python
irs.value
```

```python
@ipywidgets.interact(bounds = irs)
def show_bounds(bounds):
    print("Spanning ", bounds[0], "to", bounds[1])
```

```python
cp = ipywidgets.ColorPicker()
cp
```

```python
cp.value
```

```python
ipywidgets.DatePicker()
```

```python
ipywidgets.Controller()
```

```python
html = ipywidgets.HTML()
```

```python
html
```

```python
ta = ipywidgets.Textarea()
ta
```

```python
ta
```

```python
ta.value
```

```python
traitlets.link((html, "value"), (ta, "value"))
```

```python
sliders = [ipywidgets.IntSlider() for _ in range(10)]
```

```python
ipywidgets.HBox(sliders)
```

```python
ipywidgets.VBox(sliders)
```

```python
our_display = ipywidgets.HTML()
```

```python
our_display
```

```python
traitlets.link((speak_now, "name"), (our_display, "value"))
```

```python
speak_now.name = "Speak Now (Taylor's Version (Taylor's Version))"
```

```python
my_button = ipywidgets.Button(description = "Click on me!")
```

```python
my_button
```

```python
class Counter(traitlets.HasTraits):
    num_clicks = traitlets.Int()
```

```python
counter = Counter()

def click_button(b):
    counter.num_clicks += 1

my_button.on_click(click_button)
```

```python
counter.num_clicks
```

```python

```

```python
l = ipywidgets.Label()
traitlets.link((counter, "num_clicks"), (l, "value"), (lambda a: str(a), lambda a: int(a)))
```

```python
l
```

```python
l.value = "15"
```

```python
counter.num_clicks
```

```python

```
