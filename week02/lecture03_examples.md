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
  title: Lecture03 Examples
---

![]( https://uiuc-ischool-dataviz.github.io/spring2019online/week01/images/stitch_reworked.png)

```python
!wget https://uiuc-ischool-dataviz.github.io/spring2019online/week01/images/stitch_reworked.png
```

```python
import numpy as np
import matplotlib.pyplot as plt
import PIL.Image
```

```python
%matplotlib inline
```

```python
plt.plot([1, 2, 3, 5], [4, 1, 2, 9])
```

```python
im = PIL.Image.open("stitch_reworked.png")
```

```python
im
```

```python
type(im)
```

```python
im_data = np.array(im)
```

```python
im_data.shape
```

```python
im_data.dtype
```

```python
im_data[240, 210, 0]
```

```python
im_data[240, 210, :]
```

```python
im_data[ 230:240, 210, 1 ]
```

```python
arr = np.arange(100)
```

```python
arr
```

```python
arr[4:10]
```

```python
arr[:5]
```

```python
arr[4:10:2]
```

```python
arr[::-1]
```

```python
PIL.Image.fromarray(im_data[:250:-1, :, :])
```

```python
im_data.shape
```

```python
im_data.reshape(-1, im_data.shape[2]).shape
```

```python
483*430
```

```python
np.unique([1, 2, 3, 1, 1, 1])
```

```python
np.unique(im_data.reshape(-1, im_data.shape[2]), axis=0)
```

```python
plt.imshow(im_data)
```

```python
fig, ax = plt.subplots(figsize = (5,5))
ax.set_facecolor("gray")
ax.imshow(im_data)

plt.show()
```

```python

```
