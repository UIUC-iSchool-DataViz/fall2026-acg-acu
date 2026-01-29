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
#   title: Lecture03 Examples
# ---

# %% [markdown]
# ![]( https://uiuc-ischool-dataviz.github.io/spring2019online/week01/images/stitch_reworked.png)

# %%
# !wget https://uiuc-ischool-dataviz.github.io/spring2019online/week01/images/stitch_reworked.png

# %%
import numpy as np
import matplotlib.pyplot as plt
import PIL.Image

# %%
# %matplotlib inline

# %%
plt.plot([1, 2, 3, 5], [4, 1, 2, 9])

# %%
im = PIL.Image.open("stitch_reworked.png")

# %%
im

# %%
type(im)

# %%
im_data = np.array(im)

# %%
im_data.shape

# %%
im_data.dtype

# %%
im_data[240, 210, 0]

# %%
im_data[240, 210, :]

# %%
im_data[ 230:240, 210, 1 ]

# %%
arr = np.arange(100)

# %%
arr

# %%
arr[4:10]

# %%
arr[:5]

# %%
arr[4:10:2]

# %%
arr[::-1]

# %%
PIL.Image.fromarray(im_data[:250:-1, :, :])

# %%
im_data.shape

# %%
im_data.reshape(-1, im_data.shape[2]).shape

# %%
483*430

# %%
np.unique([1, 2, 3, 1, 1, 1])

# %%
np.unique(im_data.reshape(-1, im_data.shape[2]), axis=0)

# %%
plt.imshow(im_data)

# %%
fig, ax = plt.subplots(figsize = (5,5))
ax.set_facecolor("gray")
ax.imshow(im_data)

plt.show()

# %%
