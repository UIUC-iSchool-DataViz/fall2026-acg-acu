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
#   title: Lecture06 Examples
# ---

# %%
# %matplotlib inline

# %%
import matplotlib.pyplot as plt
import numpy as np

# %%
import PIL.Image

# %%
# !wget https://uiuc-ischool-dataviz.github.io/fall2020-BOG-BOU/week03/images/winter_scene.jpg

# %%
image = PIL.Image.open("winter_scene.jpg")

# %%
image

# %%
arr = np.array(image)

# %%
arr.shape

# %%
flat_image = arr.reshape((-1, 3))

# %%
flat_image.shape

# %%
flat_image[:10]

# %%
red_only = arr.copy()
red_only[:, :, 1] = 0
red_only[:, :, 2] = 0

green_only = arr.copy()
green_only[:, :, 0] = 0
green_only[:, :, 2] = 0

blue_only = arr.copy()
blue_only[:, :, 0] = 0
blue_only[:, :, 1] = 0

r_img = PIL.Image.fromarray(red_only)
g_img = PIL.Image.fromarray(green_only)
b_img = PIL.Image.fromarray(blue_only)

# %%
r_img

# %%
g_img

# %%
b_img

# %%
fig, ax = plt.subplots(2, 1, dpi = 300)
ax[0].imshow(arr)
ax[1].hist(flat_image[:,0], bins = np.arange(256), alpha=0.5, facecolor = 'red');
ax[1].hist(flat_image[:,1], bins = np.arange(256), alpha=0.5, facecolor = 'green');
ax[1].hist(flat_image[:,2], bins = np.arange(256), alpha=0.5, facecolor = 'blue');

# %%
# !wget https://uiuc-ischool-dataviz.github.io/spring2019online/week05/data/single_dicom.h5

# %%
import h5py

# %%
f = h5py.File("single_dicom.h5")

# %%
list(f.keys())

# %%
scan = f["scan"][:]

# %%
scan.shape

# %%
scan[18, :, :].shape

# %%
plt.rcParams["figure.dpi"] = 150

# %%
import matplotlib.colors as mc

# %%
import ipywidgets

# %%
my_norm = mc.LogNorm(vmin = 1.0, vmax = scan.max())

# %%
image = plt.imshow(scan[12,:,:], extent = [0, 1, 0, 1], norm=my_norm)
image.cmap.set_bad("white")
plt.colorbar()


# %%
@ipywidgets.interact(slice_coord = (0, 35), colormap = ["viridis", "magma", "cubehelix"])
def slice_scan(slice_coord, colormap = "viridis"):
    image = plt.imshow(scan[slice_coord,:,:], extent = [0, 1, 0, 1], norm=my_norm, cmap = colormap)
    plt.colorbar()

# %%
