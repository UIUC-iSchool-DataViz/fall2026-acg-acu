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
import numpy as np
import bqplot
```

```python
import matplotlib.pyplot as plt
```

```python
x = np.random.random(size=32**3)
y = np.random.random(size=32**3)
```

```python
plt.scatter(x, y)
```

```python
x_sc = bqplot.LinearScale()
y_sc = bqplot.LinearScale()

x_ax = bqplot.Axis(scale = x_sc)
y_ax = bqplot.Axis(scale = y_sc, orientation = 'vertical')

scatter = bqplot.Scatter(x=x, y=y, scales = {'x': x_sc, 'y': y_sc}, alpha = 0.1)

figure = bqplot.Figure(marks = [], axes = [x_ax, y_ax])
display(figure)
```

```python
import traitlets
import ipywidgets
```

```python

```

```python
class MyDashboard(traitlets.HasTraits):
    x_axis = traitlets.Unicode()
    y_axis = traitlets.Unicode()
```

```python
db1 = MyDashboard(x_axis = "Time", y_axis = "Sunlight")
```

```python
db1.x_axis
```

```python
class MultiViewDashboard(traitlets.HasTraits):
    left_view = traitlets.Instance(klass=bqplot.Figure)
    right_view = traitlets.Instance(klass=bqplot.Figure)
    view = traitlets.Instance(klass=ipywidgets.Box)
    dataset = traitlets.Instance(klass=np.ndarray)
    left_y_axis = traitlets.CInt()
    right_y_axis = traitlets.CInt()
    ui_bar = traitlets.Instance(klass=ipywidgets.Box)
    
    @traitlets.observe("left_y_axis")
    def _update_left_y_axis(self, change):
        self.left_view.marks[0].y = self.dataset[:, change['new']]

    @traitlets.default("dataset")
    def _default_dataset(self):
        x = np.mgrid[0.0:12.0:256j]
        y1 = np.sin(x**2)
        y2 = np.cos(x*1.5)
        y3 = np.tan(x/2)
        return np.stack([x, y1, y2, y3], axis=-1)

    @traitlets.default("ui_bar")
    def _default_ui_bar(self):
        color = ipywidgets.ColorPicker()
        x_range = ipywidgets.FloatRangeSlider(min = 0, max = 12.0)
        x_range.value = (0, 12)
        def change_x_range(change):
            mi, ma = change['new']
            self.left_view.marks[0].scales['x'].min = mi
            self.left_view.marks[0].scales['x'].max = ma
        x_range.observe(change_x_range, 'value')
        def change_line_color(change):
            self.left_view.marks[0].colors = [change['new']]
        color.observe(change_line_color, ['value'])
        
        left_axis_select = ipywidgets.Dropdown(
            options = [("sin(x**2)", 1), ("cos(3x/2)", 2), ("tan(x/2)", 3)],
            value = 1
        )
        traitlets.link( (left_axis_select, "value"), (self, "left_y_axis") )
        
        return ipywidgets.HBox([color, x_range, left_axis_select])
    
    @traitlets.default("left_view")
    def _default_left_view(self):
        x_sc = bqplot.LinearScale()
        y_sc = bqplot.LinearScale()
        x_ax = bqplot.Axis(scale = x_sc)
        y_ax = bqplot.Axis(scale = y_sc, orientation='vertical')
        line = bqplot.Lines(x = self.dataset[:,0], y = self.dataset[:,self.left_y_axis],
                            scales = {'x': x_sc, 'y': y_sc})
        return bqplot.Figure(marks = [line], axes=[x_ax, y_ax])
    
    @traitlets.default("right_view")
    def _default_right_view(self):
        return bqplot.Figure()
    
    @traitlets.default("view")
    def _default_view(self):
        return ipywidgets.VBox([
                    self.ui_bar,
                    ipywidgets.HBox([self.left_view, self.right_view])
        ])
```

```python
mdb = MultiViewDashboard()
```

```python
mdb.view
```

```python
mdb.left_y_axis = 3
```

```python
mdb.left_view.marks[0].colors = ["#000000"]
```

```python
mdb.view
```

```python

```
