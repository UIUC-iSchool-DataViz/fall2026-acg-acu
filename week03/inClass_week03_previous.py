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
#   title: Inclass Week03 Previous
# ---

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# %%
# #!wget https://raw.githubusercontent.com/UIUC-iSchool-DataViz/is445_data/main/building_inventory.csv

# %%
df = pd.read_csv("building_inventory.csv", na_values = {'Year Acquired': 0, 'Year Constructed': 0},
                parse_dates=["Year Acquired", "Year Constructed"])

# %%
df.describe()

# %%
# #!wget https://github.com/UIUC-iSchool-DataViz/is445_data/raw/main/michigan_lld.flt

# %%
arr = np.fromfile("michigan_lld.flt", dtype="<f4")

# %%
data = arr.reshape((-1, 4201))

# %%
data[data < -9998] = np.nan

# %%
plt.imshow(data)
plt.show()

# %%
data.shape

# %%
plt.imshow(data[::10,::10])
plt.colorbar()
plt.show()

# %%
fig, ax = plt.subplots(1, 1)
ax.set_title("Axes Title")

# %%
fig, ax = plt.subplots(2, 2)
fig.suptitle("Figure Title")
ax[0, 0].set_title("Axes [0, 0] Title")
ax[0, 1].set_title("Axes [0, 1] Title")
ax[1, 0].set_title("Axes [1, 0] Title")
ax[1, 1].set_title("Axes [1, 1] Title")

# %%
ax0 = ax[0,0]

# %%
ax0.patches

# %%
ax0.lines

# %%
ax0.images

# %%
ax0.transAxes, ax0.transData

# %%
import matplotlib.patches as patches

# %%
fig, ax = plt.subplots(1, 1)
ax.plot( [1, 2, 3, 4, 5], [0.1, 0.4, 0.3, 0.2, 0.9])
circle1 = patches.Circle( (3.0, 0.7), radius = 0.1, facecolor = 'red')
circle2 = patches.Circle( (0.75, 0.25), radius = 0.1, facecolor = 'blue',
                        transform = ax.transAxes)
ax.add_patch(circle1)
ax.add_patch(circle2)

# %%
fig

# %%
df

# %%
agg = df.groupby("Year Acquired")["Square Footage"].sum()

# %%
start = agg.index[agg.argmax()]
end = agg.index[agg.argmax() + 10]

# %%
fig, ax = plt.subplots(1, 1)
ax.plot(agg.index, agg.values)
r = patches.Rectangle( (start, 0), end - start, 4e6, facecolor = "blue", alpha = 0.3)
ax.add_patch(r)

# %%
import matplotlib.transforms as tf

# %%
fig, ax = plt.subplots(1, 1)
ax.plot(agg.index, agg.values)
new_transform = tf.blended_transform_factory(ax.transData, ax.transAxes)
r = patches.Rectangle( (start, 0.0), end - start, 1.0,
                      facecolor = "blue", alpha = 0.3,
                      transform = new_transform)
ax.add_patch(r)

# %%
fig, ax = plt.subplots(1, 1)
ax.plot(agg.index, agg.values)
new_transform = tf.blended_transform_factory(ax.transData, ax.transAxes)
r = patches.Rectangle( (start, 0.0), end - start, 1.0,
                      facecolor = "blue", alpha = 0.3,
                      transform = new_transform)
ax.add_patch(r)
ax.set_ylim(-100, 1e7)

# %%
ax.spines['left'].set_color("red")

# %%
fig

# %%
ax.xaxis.set_label_text("Hello")
fig

# %%
ax.xaxis.label.set_rotation(90)

# %%
fig

# %%
x = np.mgrid[0.0:24:256j]
y = np.sin(x) + np.cos(x/5)**2

# %%
fig, ax = plt.subplots(1,1)
ax.plot(x, y, "red")

# %%
ax.get_xticks()
ax.set_xticks( [0, 10, 25] )
fig

# %%
ax.get_xticks()
ax.set_xticks( [np.pi, 2*np.pi, 6*np.pi] )
ax.set_xticklabels( ["$\pi$", "$2\pi$", "$6\pi$"] )
fig

# %%
x = np.mgrid[0.0:24:2048j]
y = np.sin(x) + np.cos(x/5)**2 + np.cos(x*20) * 0.1

# %%
fig, ax = plt.subplots(1, 1, dpi=300)
ax.plot(x, y)
inset = ax.inset_axes([0.75, 0.75, 0.15, 0.15])
inset.plot(x, y)
inset.set_xlim(0.5, 0.6)
inset.autoscale(axis="y")

# %%
with plt.style.context("petroff10"):
    fig, ax = plt.subplots(1, 1)
    ax.plot(x, y)

# %%
x, y = np.mgrid[-0.5:0.5:128j, -0.5:0.5:128j]

# %%
r = (x*x + y+y)

# %%
r.shape

# %%
plt.imshow(r, origin='lower')
plt.colorbar()
plt.set_cmap("coolwarm")

# %%
