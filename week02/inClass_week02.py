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
#   title: UNGRADED Workbook for In-Class
# ---

# %% [markdown]
# # UNGRADED Workbook for In-Class
#
# This notebook is here for you to "code along" during class. 
#
# It will not be graded, so feel free to play around!

# %%
# %matplotlib inline

# %%
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# %%
import PIL.Image as Image

# %%
im = Image.open("stitch_reworked.png")

# %%
im

# %%
a = 1

# %%
print(a)

# %%
b = "Hello there"

# %%
b

# %%
print(b)

# %%
im_data = np.array(im)

# %%
im_data

# %%
im_data.shape

# %%
np.unique(im_data)

# %%
channel_labels = ["R", "G", "B", "A"]
for i in range(im_data.shape[2]):
    print('channel=', channel_labels[i],
         'unique values=', np.unique(im_data[:,:,i]))

# %%
im_data.shape

# %%
im_data[:,:,1].shape

# %%
im_data[10:-10,::3,:3].shape

# %%
im_reshaped = im_data.reshape((-1, 4))

# %%
im_reshaped.shape

# %%
np.sum(im_reshaped, axis=1)

# %%
np.sum(im_reshaped, axis=0)

# %%
np.unique(im_reshaped, axis=0)

# %%
hex(126), hex(22), hex(33)

# %%
fig, ax = plt.subplots(figsize=(10, 10))

# %%
ax.imshow(im_data)

# %%
fig

# %%
ax.imshow(im_data, origin='lower')

# %%
fig

# %%
fig, ax = plt.subplots(figsize=(10,10))
ax.imshow(im_data * 0 + 125)
ax.imshow(im_data)
plt.show()

# %%
im_data[:,:,0] == 255

# %%
reds_good_mask = im_data[:,:,0] == 255
greens_good_mask = im_data[:,:,1] == 255
blues_good_mask = im_data[:,:,2] == 255
alphas_good_mask = im_data[:,:,3] == 255

# %%
pixel_good_mask = (reds_good_mask & greens_good_mask & blues_good_mask & alphas_good_mask)

# %%
pixel_good_mask.sum()

# %%
pixel_good_mask.size

# %%
~pixel_good_mask

# %%
pixel_mask_bad = ( (im_data[:,:,0] == 126)
                  & (im_data[:,:,1] == 22)
                  & (im_data[:,:,2] == 33)
                  & (im_data[:,:,3] == 255))

# %%
pixel_mask_bad.sum()

# %%
ngood = pixel_good_mask.sum()
nbad = pixel_mask_bad.sum()

# %%
ngood / (ngood + nbad)

# %%
nbad / (ngood + nbad)

# %%
total = ngood + nbad

# %%
fig, ax = plt.subplots(figsize=(8,8))

ax.bar([1], nbad/total, [0.5], color='maroon', label = 'badness')
ax.bar([1], ngood/total, [0.5], color='steelblue', label = 'goodness', bottom = nbad / total)
ax.set_xlim(0.0, 2.0)
ax.xaxis.set_visible(False)
ax.legend()
fig

# %%
import csv

# %%
f = open("building_inventory.csv", "r")

# %%
f.seek(0)

# %%
f.seek(100)

# %%
f.read(10)

# %%
f.seek(0)
for record in csv.reader(f):
    print(record)

# %%
f.seek(0)
reader = csv.reader(f)
header = next(reader)

# %%
data = {}
for column in header:
    data[column] = []

# %%
arr1 = ["hi", "there", "my", "friends"]
arr2 = [2, 5, 3, 7]

for word, num in zip(arr1, arr2):
    print(word, num, len(word) == num)

# %%
f.seek(0)
reader = csv.reader(f)
header = next(reader)

data = {}
for column in header:
    data[column] = []

for row in reader:
    for value, column in zip(row, header):
        data[column].append(value)

# %%
data.keys()

# %%
import collections

# %%
agency_counter = collections.Counter(data['Agency Name'])

# %%
# agency_counter.most_common?

# %%
agency_counter.most_common(10)

# %%
fig, ax = plt.subplots(figsize=(10,6))

names = []
counts = []

for agency, num in agency_counter.most_common(10):
    names.append(agency)
    counts.append(num)

ax.bar(names, counts)
fig.autofmt_xdate(rotation=90)

# %%
