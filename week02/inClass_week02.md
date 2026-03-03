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
%matplotlib inline
```

```python
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
```

```python
import PIL.Image as Image
```

```python
im = Image.open("stitch_reworked.png")
```

```python
im
```

```python
a = 1
```

```python
print(a)
```

```python
b = "Hello there"
```

```python
b
```

```python
print(b)
```

```python
im_data = np.array(im)
```

```python
im_data
```

```python
im_data.shape
```

```python
np.unique(im_data)
```

```python
channel_labels = ["R", "G", "B", "A"]
for i in range(im_data.shape[2]):
    print('channel=', channel_labels[i],
         'unique values=', np.unique(im_data[:,:,i]))
```

```python
im_data.shape
```

```python
im_data[:,:,1].shape
```

```python
im_data[10:-10,::3,:3].shape
```

```python
im_reshaped = im_data.reshape((-1, 4))
```

```python
im_reshaped.shape
```

```python
np.sum(im_reshaped, axis=1)
```

```python
np.sum(im_reshaped, axis=0)
```

```python
np.unique(im_reshaped, axis=0)
```

```python
hex(126), hex(22), hex(33)
```

```python
fig, ax = plt.subplots(figsize=(10, 10))
```

```python
ax.imshow(im_data)
```

```python
fig
```

```python
ax.imshow(im_data, origin='lower')
```

```python
fig
```

```python
fig, ax = plt.subplots(figsize=(10,10))
ax.imshow(im_data * 0 + 125)
ax.imshow(im_data)
plt.show()
```

```python
im_data[:,:,0] == 255
```

```python
reds_good_mask = im_data[:,:,0] == 255
greens_good_mask = im_data[:,:,1] == 255
blues_good_mask = im_data[:,:,2] == 255
alphas_good_mask = im_data[:,:,3] == 255
```

```python
pixel_good_mask = (reds_good_mask & greens_good_mask & blues_good_mask & alphas_good_mask)
```

```python
pixel_good_mask.sum()
```

```python
pixel_good_mask.size
```

```python
~pixel_good_mask
```

```python
pixel_mask_bad = ( (im_data[:,:,0] == 126)
                  & (im_data[:,:,1] == 22)
                  & (im_data[:,:,2] == 33)
                  & (im_data[:,:,3] == 255))
```

```python
pixel_mask_bad.sum()
```

```python
ngood = pixel_good_mask.sum()
nbad = pixel_mask_bad.sum()
```

```python
ngood / (ngood + nbad)
```

```python
nbad / (ngood + nbad)
```

```python
total = ngood + nbad
```

```python
fig, ax = plt.subplots(figsize=(8,8))

ax.bar([1], nbad/total, [0.5], color='maroon', label = 'badness')
ax.bar([1], ngood/total, [0.5], color='steelblue', label = 'goodness', bottom = nbad / total)
ax.set_xlim(0.0, 2.0)
ax.xaxis.set_visible(False)
ax.legend()
fig
```

```python
import csv
```

```python
f = open("building_inventory.csv", "r")
```

```python
f.seek(0)
```

```python
f.seek(100)
```

```python
f.read(10)
```

```python
f.seek(0)
for record in csv.reader(f):
    print(record)
```

```python
f.seek(0)
reader = csv.reader(f)
header = next(reader)
```

```python
data = {}
for column in header:
    data[column] = []
```

```python
arr1 = ["hi", "there", "my", "friends"]
arr2 = [2, 5, 3, 7]

for word, num in zip(arr1, arr2):
    print(word, num, len(word) == num)
```

```python
f.seek(0)
reader = csv.reader(f)
header = next(reader)

data = {}
for column in header:
    data[column] = []

for row in reader:
    for value, column in zip(row, header):
        data[column].append(value)
```

```python
data.keys()
```

```python
import collections
```

```python
agency_counter = collections.Counter(data['Agency Name'])
```

```python
agency_counter.most_common?
```

```python
agency_counter.most_common(10)
```

```python
fig, ax = plt.subplots(figsize=(10,6))

names = []
counts = []

for agency, num in agency_counter.most_common(10):
    names.append(agency)
    counts.append(num)

ax.bar(names, counts)
fig.autofmt_xdate(rotation=90)
```

```python

```
