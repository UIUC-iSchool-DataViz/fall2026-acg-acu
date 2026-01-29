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
#   title: Week04-Inclass-02
# ---

# %%
import traitlets
import ipywidgets

# %%
a = ipywidgets.IntSlider()
b = ipywidgets.IntText()
traitlets.link((a, 'value'), (b, 'value'))

# %%
a

# %%
b

# %%
import numpy as np
import matplotlib.pyplot as plt

# %%
np.mgrid[0.0:10.0:0.5]

# %%
np.mgrid[0.0:1.0:4j]

# %%
np.mgrid[0.0:10.0:256j]

# %%
x = np.mgrid[0.0:10.0:256j]
y = np.sin(1 * x)

# %%
plt.plot(x, y)


# %%
@ipywidgets.interact( factor = ( 0.0, 2.5, 0.1) )
def make_plot(factor):
    x = np.mgrid[0.0:10.0:256j]
    y = np.sin(factor * x)
    plt.plot(x, y)


# %%
fw = ipywidgets.FloatText()


# %%
@ipywidgets.interact( factor = fw, color = ipywidgets.ColorPicker(), file = ipywidgets.FileUpload() )
def make_plot(factor, color):
    x = np.mgrid[0.0:10.0:256j]
    y = np.sin(factor * x)
    plt.plot(x, y, c = color)


# %%
fw.value = 9.5

# %%
ipywidgets.ColorPicker()

# %%
fup = ipywidgets.FileUpload()

# %%
fup

# %%
fup.value

# %%
dp = ipywidgets.DatePicker()

# %%
dp

# %%
dp.value

# %%
hb = ipywidgets.HBox([ ipywidgets.FileUpload(), ipywidgets.IntSlider() ])

# %%
hb

# %%
hb.layout.border = '1px solid black'


# %%
class SimpleTraitlets(traitlets.HasTraits):
    my_name = traitlets.Unicode()


# %%
st = SimpleTraitlets(name = "Hi")

# %%
st.traits()

# %%
hb.layout.traits()

# %%
hb.layout.justify_content = 'center'

# %%
hb

# %%
fw.value = 10


# %%
class MySineGraph(traitlets.HasTraits):
    offset = traitlets.Float()
    factor = traitlets.Float()

    def _ipython_display_(self):
        x = np.mgrid[0.0:10.0:256j]
        y = np.sin(x*self.factor + self.offset)
        plt.plot(x, y)


# %%
import io

# %%
b = io.BytesIO()
plt.savefig(b)

# %%
b.seek(0)
ipywidgets.Image(value = b.read())

# %%
msg = MySineGraph(offset = 0.0, factor = 2.0)

# %%
msg


# %%
class MySineGraph(traitlets.HasTraits):
    offset = traitlets.Float()
    factor = traitlets.Float()
    image = traitlets.Bytes()

    def make_plot(self):
        x = np.mgrid[0.0:10.0:256j]
        y = np.sin(x*self.factor + self.offset)
        plt.plot(x, y)
        b = io.BytesIO()
        plt.savefig(b)
        b.seek(0)
        self.image = b.read()
    
    def _ipython_display_(self):
        im = ipywidgets.Image()
        traitlets.link((self, 'image'), (im, 'value'))
        display(im)


# %%
msg = MySineGraph()

# %%
msg

# %%
msg.make_plot()


# %%
class MySineGraph(traitlets.HasTraits):
    offset = traitlets.Float()
    factor = traitlets.Float()
    image = traitlets.Bytes()

    @traitlets.observe('factor', 'offset')
    def _plot_changed(self, change):
        x = np.mgrid[0.0:10.0:256j]
        y = np.sin(x*self.factor + self.offset)
        plt.clf()
        plt.plot(x, y)
        b = io.BytesIO()
        plt.savefig(b)
        b.seek(0)
        self.image = b.read()
    
    def _ipython_display_(self):
        im = ipywidgets.Image()
        traitlets.link((self, 'image'), (im, 'value'))
        display(im)


# %%
msg = MySineGraph(factor = 1.0, offset = 0.0)

# %%
msg

# %%
msg.factor = 2.0

# %%
msg.factor = 2.0

# %%
import bqplot


# %%

# %%
class MySineGraph(traitlets.HasTraits):
    factor = traitlets.Float()
    offset = traitlets.Float()
    n = traitlets.Int(256)
    figure = traitlets.Instance(bqplot.Figure)

    @traitlets.default("figure")
    def _default_figure(self):
        x_sc = bqplot.LinearScale()
        y_sc = bqplot.LinearScale()
        x_ax = bqplot.Axis(scale = x_sc)
        y_ax = bqplot.Axis(scale = y_sc, orientation = 'vertical')

        mark = bqplot.Lines(x = [], y = [], scales = {'x': x_sc, 'y': y_sc})
        fig = bqplot.Figure(marks = [mark], axes = [x_ax, y_ax])
        return fig

    @traitlets.observe("factor", "offset", "n")
    def _change_factor_offset(self, change):
        x = np.mgrid[0.0:10.0:1j * self.n]
        y = np.sin(self.factor * x + self.offset)
        self.figure.marks[0].x = x
        self.figure.marks[0].y = y
    
    def _ipython_display_(self):
        display(self.figure)


# %%
msg = MySineGraph(factor = 1.0, offset = 0.0)

# %%
msg

# %%
msg.factor = 4

# %%
fs = ipywidgets.FloatSlider()
traitlets.link((fs, 'value'), (msg, 'factor'))
fs

# %%
ns = ipywidgets.IntSlider(min = 1, max = 2048)
traitlets.link((ns, 'value'), (msg, 'n'))
ns

# %%
