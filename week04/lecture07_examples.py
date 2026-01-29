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
#     display_name: Environment (conda_conda)
#     language: python
#     name: conda_conda
#   layout: notebook
#   title: Lecture07 Examples
# ---

# %%
import traitlets
import ipywidgets


# %%
class Band(traitlets.HasTraits):
    name = traitlets.Unicode()
    age = traitlets.Int()


# %%
weezer = Band(name = "Weezer", age = 26)

# %%
weezer.name

# %%
weezer.age

# %%
weezer.name


# %%
def name_changed(change):
    print("Band name has changed from {} to {}".format(
        change['old'], change['new']))


# %%
weezer.observe(name_changed, ['name'])

# %%
weezer.name

# %%
weezer.name = "White Stripes"

# %%
weezer.unobserve_all()


# %%
def trait_changed(change):
    print("The trait {name} has changed from {old} to {new}".format(
        **change))


# %%
weezer = Band(name = "Weezer", age = 26)
weezer.observe(trait_changed, ['name', 'age'])

# %%
weezer.age = 10

# %%
weezer.name = "Something Else"

# %%
weezer.name = "Something Else"


# %%
class Record(traitlets.HasTraits):
    band_name = traitlets.Unicode()


# %%
some_record = Record(band_name = "")

# %%
traitlets.link( (weezer, 'name'), (some_record, 'band_name') )

# %%
some_record.band_name

# %%
weezer.name = "Weezer"

# %%
some_record.band_name

# %%
some_record.band_name = "TMBG"


# %%
@ipywidgets.interact(name = ['Weezer', 'Nerf Herder', 'Mustard Plug'],
                    age = (0, 100, 5),
                    message = "hi")
def print_bandname(name = "Mustard Plug", age = 10, message = "hi"):
    print(name, age, message)


# %%
fs = ipywidgets.FloatSlider()

# %%
display(fs)

# %%
fs.max = 50

# %%
fs.min = 10.

# %%
display(fs)

# %%
fs.value


# %%
def print_value(change):
    print("Trait changed from {old} to {new}".format(**change))
fs.observe(print_value, ['value'])

# %%
fs.unobserve_all()

# %%
ipywidgets.IntRangeSlider()

# %%
log_slider = ipywidgets.FloatLogSlider()

# %%
display(log_slider)

# %%
log_slider.value = 1e3

# %%
pbar = ipywidgets.FloatProgress()

# %%
display(pbar)

# %%
import time

# %%
for i in range(100):
    pbar.value = i
    time.sleep(0.1)

# %%
bft = ipywidgets.BoundedFloatText(min = 25.0, max = 53.0, value = 25.1)

# %%
bft

# %%
traitlets.link((bft, 'value'), (log_slider, 'value'))

# %%
my_display = ipywidgets.HTML()

# %%
my_display

# %%
my_display.value = "hi there <b>this is bold</b>"

# %%
text_entry = ipywidgets.Textarea()
text_display = ipywidgets.HTML()

traitlets.link( (text_entry, "value"), (text_display, "value") )

# %%
display(text_entry)

# %%
display(text_display)

# %%
ipywidgets.HBox([text_entry, text_display])

# %%
ipywidgets.VBox([text_entry, text_display])

# %%
ipywidgets.HBox([
    ipywidgets.VBox([text_entry, text_display]),
    ipywidgets.IntSlider()
])

# %%
slider = ipywidgets.SelectionSlider(options = ["Weezer", "Nerf Herder", "Mustard Plug"])

# %%
slider

# %%
slider.index

# %%
slider.value

# %%
rb = ipywidgets.RadioButtons(options = ["This", "That", "The Other"])
display(rb)

# %%
rb.index

# %%
rb.value

# %%
ipywidgets.Checkbox(description="Enabled")


# %%
@ipywidgets.interact(message = ipywidgets.Textarea())
def print_message(message):
    print(message)


# %%
button = ipywidgets.Button(description = "Does Something")
display(button)


# %%
def button_clicked(obj):
    print(obj)
button.on_click(button_clicked)


# %%
class SomeRandomValue(traitlets.HasTraits):
    value1 = traitlets.Float()
    value2 = traitlets.Float()
srv = SomeRandomValue()

# %%
button1 = ipywidgets.Button(description = "Change value1")
button2 = ipywidgets.Button(description = "Change value2")

# %%
value1_floatslider = ipywidgets.FloatSlider()
value2_floatslider = ipywidgets.FloatSlider()

# %%
ipywidgets.HBox([
    ipywidgets.VBox([button1, button2]),
    ipywidgets.VBox([value1_floatslider, value2_floatslider])
])

# %%
import random


# %%
def change_value1(button):
    srv.value1 = random.randrange(0.0, 100.0)
def change_value2(button):
    srv.value2 = random.randrange(0.0, 100.0)


# %%
srv.value1, srv.value2

# %%
button1.on_click(change_value1)
button2.on_click(change_value2)

# %%
srv.value1

# %%
srv.value2

# %%
traitlets.link( (value1_floatslider, 'value'), (srv, 'value1') )
traitlets.link( (value2_floatslider, 'value'), (srv, 'value2') )

# %%
ipywidgets.ColorPicker()

# %%
ipywidgets.Controller()

# %%
ipywidgets.Video()

# %%
ipywidgets.Play()

# %%
# %matplotlib inline

# %%
import matplotlib.pyplot as plt

# %%
import numpy as np

# %%
x = np.random.random(size = 10000)
y = np.random.normal(size = 10000)


# %%
@ipywidgets.interact(n = (10, 1000))
def make_plot(n = 100):
    plt.scatter(x[:n], y[:n])


# %%
import h5py
f = h5py.File("single_dicom.h5", mode = "r")
scan = f["scan"][:]

# %%
fig, ax = plt.subplots(2,2, dpi = 150)

@ipywidgets.interact( x_ind = (0, scan.shape[0]),
                      y_ind = (0, scan.shape[1]),
                      z_ind = (0, scan.shape[2]))
def sliceit(x_ind = 18, y_ind = 256, z_ind = 256):
    ax[0,0].imshow(scan[x_ind,:,:], extent = [0.0, 1.0, 0.0, 1.0])
    ax[1,0].imshow(scan[:,y_ind,:], extent = [0.0, 1.0, 0.0, 1.0])
    ax[0,1].imshow(scan[:,:,z_ind], extent = [0.0, 1.0, 0.0, 1.0])
    ax[1,1].clear()
    return fig

# %%
