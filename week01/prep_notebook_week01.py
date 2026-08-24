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
#       jupytext_version: 1.19.5
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
#   layout: notebook
#   title: Prep Notebook Week01
# ---

# %%
# %matplotlib inline

# %%
import matplotlib
import matplotlib.pyplot as plt
import datetime
matplotlib.rcParams["font.family"] = "Questrial"

# %%
import numpy as np

# %%
years = [2729, 2699, 2613, 2583, 2562, 2530, 2501, 2490, 2470, 2400]
# 2714-2719 Choking
# 2322-2329 Acid
seasons = [[2714, 2719], [2322, 2329]]

# %%
values = [1 for _ in years]

def make_plot(capstyle, lw=20.0, ms=100):
    fig, ax = plt.subplots(figsize=(18,2), dpi=400)
    for s in seasons:
        ax.plot(s, [1]*len(s), c='#1f77b4', marker='', ls='-', lw=lw, solid_joinstyle="bevel",
                solid_capstyle=capstyle)
    sp = ax.scatter(years, [1]*len(years), edgecolor='#ff7f0e',
               marker='o', s=ms, facecolor='', lw=3.0)

    ax.xaxis.set_minor_locator(matplotlib.ticker.MultipleLocator(100))
    ax.xaxis.set_minor_locator(matplotlib.ticker.MultipleLocator(20))   
    fig.autofmt_xdate()

    # everything after this is turning off stuff that's plotted by default

    ax.yaxis.set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.xaxis.set_ticks_position('bottom')
    ax.xaxis.set_tick_params(labelsize='xx-large', size=10)
    ax.xaxis.set_tick_params(which='minor', size=5)

    ax.get_yaxis().set_ticklabels([])

    plt.xlim(2300, 2800)
    plt.ylim(0.9, 1.1)
    plt.show()


# %%
make_plot("butt")

# %%
make_plot("projecting")

# %%
make_plot("round")


# %%
# GDP from https://fred.stlouisfed.org/series/GDP

# %%
def converter(v):
    return np.datetime64(v.decode("ascii"), 'D')

with open("Downloads/GDP.csv", "r") as f:
    data = np.loadtxt(f, skiprows=1, delimiter=",", converters = {0: converter},
                     dtype=np.dtype([("date", "datetime64[D]"), ("val", np.float64)]))


# %%
def make_gdp_plot(style):
    with plt.style.context(style):
        fig, ax = plt.subplots(figsize=(10, 8))
        ax.set_title("Style: %s" % style)
        ax.plot_date(data["date"].astype(datetime.datetime), data["val"], '-')
        plt.show()


# %%
for v in data["date"][240:260]: print(v)

# %%
for v in data["val"][240:260]: print(v)

# %%
horizontal = matplotlib.patches.Wedge([0.0, 0.0], 1.0, 90 - (210/2.0), 90 + (210/2.0), lw=2.0, facecolor="#1f77b4", edgecolor="#000000")
binoc = matplotlib.patches.Wedge([0.0, 0.0], 1.0, 90 - (114/2.0), 90 + (114/2.0), width=0.25, lw=2.0, facecolor="#ff7f0e", edgecolor="#000000")
arrow = matplotlib.patches.Arrow(-1.10, 0.0, 0.0, 0.75, width=0.25, edgecolor="#000000", facecolor="#aaaaaa", label="forward")

fig, ax = plt.subplots(figsize=(10, 7), dpi=300)

plt.text(-1.22, 0.35, "Forward", rotation=90, fontsize="xx-large")

ax.add_patch(horizontal)
#ax.add_patch(binoc_outline)
ax.add_patch(binoc)
ax.add_patch(arrow)
ax.set_xlim(-1.25, 1.25)
ax.set_ylim(-0.5, 1.25)

ax.legend([horizontal, binoc], ["Total FOV", "Binocular FOV"], fontsize="x-large")

ax.set_xticks([])
ax.set_yticks([])
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_visible(False)
plt.show()

# %%
vertical = matplotlib.patches.Wedge([0.0, 0.0], 1.0, 0 - (150/2.0), 0 + (150/2.0), lw=2.0, facecolor="#1f77b4", edgecolor="#000000")
forward_arrow = matplotlib.patches.Arrow(0.0, -1.10, 0.75, 0.0, width=0.25, edgecolor="#000000", facecolor="#aaaaaa", label="forward")
up_arrow = matplotlib.patches.Arrow(-0.1, 0.0, 0.0, 0.75, width=0.25, edgecolor="#000000", facecolor="#aaaaaa", label="forward")

fig, ax = plt.subplots(figsize=(7, 10), dpi=300)

plt.text(-0.22, 0.35, "Up", rotation=90, fontsize="xx-large", family="Questrial")
plt.text(0.15, -1.05, "Forward", rotation=0, fontsize="xx-large")

ax.add_patch(vertical)
ax.add_patch(forward_arrow)
ax.add_patch(up_arrow)
ax.set_xlim(-0.5, 1.25)
ax.set_ylim(-1.25, 1.25)

ax.set_xticks([])
ax.set_yticks([])
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_visible(False)
plt.show()

# %%
import PIL.Image as Image
data = np.array(Image.open("stitch_badness_level_reworked.png", "r"))

# %%
np.unique(data[:,:,0])

# %%
ngood = (data[:,:,0] == 255).sum()
nbad = (data[:,:,0] == 153).sum()
total = ngood + nbad
badness = nbad / total
goodness = ngood/  total
print(badness, goodness)

p1 = plt.bar([1], badness, [0.5], color='#991620')
p2 = plt.bar([1], goodness, [0.5], bottom=badness)
plt.xlim(0.0, 2.0)

# %%
# 372 pixels for full height, 72 for goodness
goodness_apparent = 79./362.

# %%
print(goodness_apparent)

# %%
ngood

# %%
nbad

# %%
1.0-goodness_apparent

# %%
