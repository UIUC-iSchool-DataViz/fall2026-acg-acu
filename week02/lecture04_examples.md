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
    display_name: Environment (conda_conda)
    language: python
    name: conda_conda
  layout: notebook
  title: Examples for Lecture 4
---

# Examples for Lecture 4

We will be covering two principal areas:

 * A few types of aggregation -- counting, average, weighted average, sum
 * The "building inventory" dataset, and some simple pandas operations on it

```python
!wget https://uiuc-ischool-dataviz.github.io/spring2019online/week02/building_inventory.csv
```

```python
%matplotlib inline
```

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
```

```python
df = pd.read_csv("building_inventory.csv")
```

```python
df.columns
```

```python
df.dtypes
```

```python
df.head()
```

```python
df.describe()
```

```python
df.shape
```

```python
(df["Year Acquired"] == 0).sum()
```

```python
(df["Year Constructed"] == 0).sum()
```

```python
(df["Square Footage"] == 0).sum()
```

```python
df = pd.read_csv("building_inventory.csv", na_values={
    "Year Acquired": 0,
    "Year Constructed": 0,
    "Square Footage": 0
})
```

```python
df.describe()
```

```python
plt.plot([1,2,3,4], [5, 1, 2, 4], "-o")
```

```python
plt.rcParams["figure.dpi"] = 200
```

```python
plt.plot(df["Year Constructed"], df["Year Acquired"], '.')
plt.xlabel("Year Constructed")
plt.ylabel("Year Acquired")
```

```python
df["Age at Acquisition"] = df["Year Acquired"] - df["Year Constructed"]
```

```python
df["Age at Acquisition"].describe()
```

```python
old_buildings = df[
    df["Age at Acquisition"] >= 0
]
```

```python
plt.hist(old_buildings["Age at Acquisition"], log=True)
plt.xlabel("Age at Acquisition")
plt.ylabel("Count")
```

```python
df["Agency Name"].unique()
```

```python
df_by_agency = df.groupby("Agency Name")
```

```python
for agency_name, new_df in df_by_agency:
    print(agency_name, new_df.shape)
```

```python
df_by_agency["Square Footage"].sum()
```

```python

```

```python

```
