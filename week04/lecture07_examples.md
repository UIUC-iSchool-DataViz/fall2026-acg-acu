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
    display_name: Environment (conda_conda)
    language: python
    name: conda_conda
  layout: notebook
  title: Lecture07 Examples
---

```python
import traitlets
import ipywidgets
```

```python
class Band(traitlets.HasTraits):
    name = traitlets.Unicode()
    age = traitlets.Int()
```

```python
weezer = Band(name = "Weezer", age = 26)
```

```python
weezer.name
```

```python
weezer.age
```

```python
weezer.name
```

```python
def name_changed(change):
    print("Band name has changed from {} to {}".format(
        change['old'], change['new']))
```

```python
weezer.observe(name_changed, ['name'])
```

```python
weezer.name
```

```python
weezer.name = "White Stripes"
```

```python
weezer.unobserve_all()
```

```python
def trait_changed(change):
    print("The trait {name} has changed from {old} to {new}".format(
        **change))
```

```python
weezer = Band(name = "Weezer", age = 26)
weezer.observe(trait_changed, ['name', 'age'])
```

```python
weezer.age = 10
```

```python
weezer.name = "Something Else"
```

```python
weezer.name = "Something Else"
```

```python
class Record(traitlets.HasTraits):
    band_name = traitlets.Unicode()
```

```python
some_record = Record(band_name = "")
```

```python
traitlets.link( (weezer, 'name'), (some_record, 'band_name') )
```

```python
some_record.band_name
```

```python
weezer.name = "Weezer"
```

```python
some_record.band_name
```

```python
some_record.band_name = "TMBG"
```

```python
@ipywidgets.interact(name = ['Weezer', 'Nerf Herder', 'Mustard Plug'],
                    age = (0, 100, 5),
                    message = "hi")
def print_bandname(name = "Mustard Plug", age = 10, message = "hi"):
    print(name, age, message)
```

```python
fs = ipywidgets.FloatSlider()
```

```python
display(fs)
```

```python
fs.max = 50
```

```python
fs.min = 10.
```

```python
display(fs)
```

```python
fs.value
```

```python
def print_value(change):
    print("Trait changed from {old} to {new}".format(**change))
fs.observe(print_value, ['value'])
```

```python
fs.unobserve_all()
```

```python
ipywidgets.IntRangeSlider()
```

```python
log_slider = ipywidgets.FloatLogSlider()
```

```python
display(log_slider)
```

```python
log_slider.value = 1e3
```

```python
pbar = ipywidgets.FloatProgress()
```

```python
display(pbar)
```

```python
import time
```

```python
for i in range(100):
    pbar.value = i
    time.sleep(0.1)
```

```python
bft = ipywidgets.BoundedFloatText(min = 25.0, max = 53.0, value = 25.1)
```

```python
bft
```

```python
traitlets.link((bft, 'value'), (log_slider, 'value'))
```

```python
my_display = ipywidgets.HTML()
```

```python
my_display
```

```python
my_display.value = "hi there <b>this is bold</b>"
```

```python
text_entry = ipywidgets.Textarea()
text_display = ipywidgets.HTML()

traitlets.link( (text_entry, "value"), (text_display, "value") )
```

```python
display(text_entry)
```

```python
display(text_display)
```

```python
ipywidgets.HBox([text_entry, text_display])
```

```python
ipywidgets.VBox([text_entry, text_display])
```

```python
ipywidgets.HBox([
    ipywidgets.VBox([text_entry, text_display]),
    ipywidgets.IntSlider()
])
```

```python
slider = ipywidgets.SelectionSlider(options = ["Weezer", "Nerf Herder", "Mustard Plug"])
```

```python
slider
```

```python
slider.index
```

```python
slider.value
```

```python
rb = ipywidgets.RadioButtons(options = ["This", "That", "The Other"])
display(rb)
```

```python
rb.index
```

```python
rb.value
```

```python
ipywidgets.Checkbox(description="Enabled")
```

```python
@ipywidgets.interact(message = ipywidgets.Textarea())
def print_message(message):
    print(message)
```

```python
button = ipywidgets.Button(description = "Does Something")
display(button)
```

```python
def button_clicked(obj):
    print(obj)
button.on_click(button_clicked)
```

```python
class SomeRandomValue(traitlets.HasTraits):
    value1 = traitlets.Float()
    value2 = traitlets.Float()
srv = SomeRandomValue()
```

```python
button1 = ipywidgets.Button(description = "Change value1")
button2 = ipywidgets.Button(description = "Change value2")
```

```python
value1_floatslider = ipywidgets.FloatSlider()
value2_floatslider = ipywidgets.FloatSlider()
```

```python
ipywidgets.HBox([
    ipywidgets.VBox([button1, button2]),
    ipywidgets.VBox([value1_floatslider, value2_floatslider])
])
```

```python
import random
```

```python
def change_value1(button):
    srv.value1 = random.randrange(0.0, 100.0)
def change_value2(button):
    srv.value2 = random.randrange(0.0, 100.0)
```

```python
srv.value1, srv.value2
```

```python
button1.on_click(change_value1)
button2.on_click(change_value2)
```

```python
srv.value1
```

```python
srv.value2
```

```python
traitlets.link( (value1_floatslider, 'value'), (srv, 'value1') )
traitlets.link( (value2_floatslider, 'value'), (srv, 'value2') )
```

```python
ipywidgets.ColorPicker()
```

```python
ipywidgets.Controller()
```

```python
ipywidgets.Video()
```

```python
ipywidgets.Play()
```

```python
%matplotlib inline
```

```python
import matplotlib.pyplot as plt
```

```python
import numpy as np
```

```python
x = np.random.random(size = 10000)
y = np.random.normal(size = 10000)
```

```python
@ipywidgets.interact(n = (10, 1000))
def make_plot(n = 100):
    plt.scatter(x[:n], y[:n])
```

```python
import h5py
f = h5py.File("single_dicom.h5", mode = "r")
scan = f["scan"][:]
```

```python
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
```

```python

```
