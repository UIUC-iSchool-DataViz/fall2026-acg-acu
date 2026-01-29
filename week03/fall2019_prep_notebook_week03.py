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
#   title: Fall2019 Prep Notebook Week03
# ---

# %%
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# %%
df = pd.read_csv("../data/building_inventory.csv",
                na_values = {'Year Acquired': 0,
                             'Year Constructed': 0,
                             'Square Footage': 0})

# %%
df.describe()

# %%
df.columns

# %%
df.groupby("Year Acquired")["Square Footage"].sum()

# %%
df.groupby("Year Acquired")["Square Footage"].describe()

# %%
stats = df.groupby("Year Acquired")["Square Footage"].describe()

# %%
stats.iloc[0]

# %%
stats.loc[1753]

# %%
stats.iloc[0:1]

# %%
stats.loc[1753:1802]

# %%
p = stats["max"].plot()
p.set_yscale("log")
p.set_ylabel("Square Footage")

# %%
plt.rcParams["figure.dpi"] = 150

# %%
p = stats["max"].plot()
p.set_yscale("log")
p.set_ylabel("Square Footage")

# %%
plt.plot(stats["min"], marker='.', linewidth=1.0, label="Min")
plt.plot(stats["max"], marker='.', linewidth=1.0, label="Max")
plt.fill_between(stats.index, stats["min"], stats["max"], color="#dddddd")
plt.yscale("log")
plt.legend()

# %%
plt.style.available

# %%
with plt.style.context("ggplot"):
    plt.plot(stats["min"], marker='.', label="Min")
    plt.plot(stats["max"], marker='.', label="Max")
    plt.fill_between(stats.index, stats["min"], stats["max"], color = "#aaaaaa")
    plt.ylabel("Square Footage")
    plt.yscale("log")
    plt.legend()

# %%
import matplotlib.transforms as mpt

# %%
with plt.style.context("ggplot"):
    plt.plot(stats["min"], marker='.', label="Min")
    plt.plot(stats["max"], marker='.', label="Max")
    plt.fill_between(stats.index, stats["min"], stats["max"], color = "#aaaaaa")
    
    plt.ylabel("Square Footage")
    plt.yscale("log")
    plt.legend()
    
    ax = plt.gca()
    plt.plot([0.5, 0.5], [0.0, 1.0], color = 'black', linewidth=2.0,
             transform = ax.transAxes)

# %%
with plt.style.context("ggplot"):
    plt.plot(stats["min"], marker='.', label="Min")
    plt.plot(stats["max"], marker='.', label="Max")
    plt.fill_between(stats.index, stats["min"], stats["max"], color = "#aaaaaa")
    
    plt.ylabel("Square Footage")
    plt.yscale("log")
    plt.legend()
    
    ax = plt.gca()
    new_transform = mpt.blended_transform_factory(ax.transData, ax.transAxes)
    plt.plot([1818, 1818], [0.0, 1.0], color = 'black', linewidth=2.0,
             transform = new_transform)

# %%
import ipywidgets

# %%
slider = ipywidgets.IntSlider(10)

# %%
slider

# %%
slider

# %%
slider.value

# %%
slider.min, slider.max

# %%
slider.min = 50

# %%
ipywidgets.IntSlider(10, min = 9, max=11)


# %%
@ipywidgets.interact(style = plt.style.available, min_x = (0.0, 10.0, 0.1))
def make_plot(style = "ggplot", min_x = 0.0):
    with plt.style.context(style):
        plt.plot([1,2,3,4], [5,3,1,4])
        plt.xlim(min_x, 15.0)


# %%
make_plot("fivethirtyeight")

# %%
plt.scatter("Year Acquired", "Year Constructed", data = df)

# %%
plt.scatter(df["Year Acquired"], df["Year Acquired"] - df["Year Constructed"])

# %%
df["Delta Time"] = df["Year Acquired"] - df["Year Constructed"]
df["Delta Time"].replace(0, np.nan, inplace=True)

# %%
plt.subplot(4, 5, 1)
plt.plot([1,2,3], [2,3,4])
plt.subplot(4, 5, 19)
plt.plot([1,2,3], [1,1,1])

# %%
michigan = np.fromfile("michigan_lld/michigan_lld.flt", dtype="f4").reshape((5365, 4201))

# %%
michigan.shape

# %%
michigan.max()

# %%
michigan.min()

# %%
michigan[michigan == -9999] = np.nan

# %%
plt.hist(michigan.flat)

# %%
np.nanmin(michigan), np.nanmax(michigan)

# %%
plt.imshow(michigan)
plt.colorbar(extend = 'both')
plt.clim(-352, 352)

# %%
plt.imshow(michigan, cmap="seismic")
plt.colorbar(extend = 'both')
plt.clim(-352, 352)

# %%
plt.imshow(michigan, cmap="jet")
plt.colorbar(extend = 'both')
plt.clim(-352, 352)

# %%
import matplotlib.colors as colors

# %%
plt.imshow(np.abs(michigan), norm = colors.LogNorm())
plt.colorbar(extend='both')

# %%
plt.imshow(michigan, norm = colors.SymLogNorm(100), cmap="terrain")
plt.colorbar(extend='both')

# %%
plt.imshow(michigan, norm = colors.SymLogNorm(100), cmap="terrain")
plt.xlim(2700, 3300)
plt.ylim(3300, 3900)
plt.colorbar(extend='both')

# %%
x0 = -88.0
y0 = 46.09
dx = 0.000833333333
dy = 0.000833333333

# %%
plt.imshow(michigan, extent = [x0, x0 + dx * michigan.shape[0],
                               y0, y0 + dy * michigan.shape[1]],
          norm = colors.SymLogNorm(10), cmap="terrain")
plt.colorbar()

# %%
y0, x0

# %%
