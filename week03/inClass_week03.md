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
    display_name: Python 3 (ipykernel)
    language: python
    name: python3
  layout: notebook
  title: In Class Notebook, Week 03
---

# In Class Notebook, Week 03


You can access this notebook in near-realy time by going here:

https://github.com/UIUC-iSchool-DataViz/is445_bcubcg_fall2023/blob/master/week03/inClass_week03.ipynb 

Or by pasting that URL into the nbviewer interface for a plain-text rendering:

https://kokes.github.io/nbviewer.js/viewer.html

```python
import pandas as pd
```

```python
buildings = pd.read_csv('https://github.com/UIUC-iSchool-DataViz/is445_data/raw/main/building_inventory.csv')
```

```python
buildings
```

```python
buildings.index
```

```python
buildings.iloc[5:8]
```

```python
buildings.iloc[5:8]["Agency Name"]
```

```python
buildings['Agency Name'].nunique()
```

```python
buildings['Bldg Status'].unique()
```

```python
buildings.describe() # for R users this is like the "summary"
```

```python
buildings['Square Footage'] == 0
```

```python
buildings.loc[buildings['Square Footage']==0]
```

```python
import matplotlib.pyplot as plt
```

```python
buildings['Square Footage'].plot()
plt.show()
```

```python
buildings['Square Footage'].plot(figsize=(10,3))
plt.show()
```

```python
buildings.plot(x='Address', y='Square Footage', figsize=(10,3), rot=90)
plt.show()
```

```python
ax = buildings.plot(x='Year Acquired', y='Square Footage', 
                    figsize=(10,3),kind='scatter')
ax.set_xlim(1750,2020)
plt.show()
```

```python
buildings = pd.read_csv('https://github.com/UIUC-iSchool-DataViz/is445_data/raw/main/building_inventory.csv',
                       na_values = {'Square Footage':0,
                                   'Year Acquired':0,
                                   'Year Constructed':0})
```

```python
ax = buildings.plot(x='Year Acquired', y='Square Footage', 
                    figsize=(10,3),kind='scatter')
#ax.set_xlim(1750,2020)
plt.show()
```

```python
buildings.describe()
```

```python
buildings['Bldg Status'].unique()
```

```python
buildings.groupby('Bldg Status')
```

```python
for group in buildings.groupby('Bldg Status'):
    print(group)
```

```python
for group_name, group_df in buildings.groupby('Bldg Status'):
    print(group_name, group_df.shape)
```

```python
buildings2 = buildings.sort_values("Year Constructed")
```

```python
buildings2.iloc[0]
```

```python
agg = buildings.groupby("Year Acquired")['Square Footage'].sum()
# for each Year Acquired, what is the total (sum) of the Square Footage

#agg = buildings.groupby("Year Acquired")['Square Footage'].mean()
# for each Year Acquired, what is the average (mean) of the Square Footage
```

```python
agg
```

```python
type(agg)
```

```python
type(buildings)
```

```python
agg.index
```

```python
agg.values
```

```python
fig, ax = plt.subplots(figsize=(15,4))

ax.plot(agg.index, agg.values)
ax.set_xlabel('Year Constructed')
ax.set_ylabel('Total (sum) Square Footage')

plt.show()
```

```python
agg.plot()
```

```python
stats = buildings.groupby('Year Acquired')['Square Footage'].describe()
```

```python
stats
```

```python
type(stats)
```

```python
stats.plot(y='count')
```

```python
stats.columns
```

```python
buildings
```

```python
buildings['Zip code'].value_counts()
```

```python
buildings['Zip code'].value_counts().iloc[0:5]
```

```python
buildings['Zip code'].value_counts().iloc[0:5].index # 5 most common zipcodes in my dataframe
```

```python
most_common_zips = buildings['Zip code'].value_counts().iloc[0:5].index
most_common_zips
```

```python
# Check out the ".isin" function for some examples that might be useful <-- HINT
```

```python
gb1 = buildings.groupby('Bldg Status')['Year Acquired'].min()
```

```python
gb1
```

```python
fig_gb1, ax_gb1 = plt.subplots()
gb1.plot(kind='bar', ax=ax_gb1)
plt.show()
```

```python
fig_gb1, ax_gb1 = plt.subplots()
ax_gb1.bar(gb1.index, gb1.values)
plt.show()
```

```python
ax_gb1.bar?
```

```python

```
