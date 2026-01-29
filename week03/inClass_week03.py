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
#   title: In Class Notebook, Week 03
# ---

# %% [markdown]
# # In Class Notebook, Week 03

# %% [markdown]
# You can access this notebook in near-realy time by going here:
#
# https://github.com/UIUC-iSchool-DataViz/is445_bcubcg_fall2023/blob/master/week03/inClass_week03.ipynb 
#
# Or by pasting that URL into the nbviewer interface for a plain-text rendering:
#
# https://kokes.github.io/nbviewer.js/viewer.html

# %%
import pandas as pd

# %%
buildings = pd.read_csv('https://github.com/UIUC-iSchool-DataViz/is445_data/raw/main/building_inventory.csv')

# %%
buildings

# %%
buildings.index

# %%
buildings.iloc[5:8]

# %%
buildings.iloc[5:8]["Agency Name"]

# %%
buildings['Agency Name'].nunique()

# %%
buildings['Bldg Status'].unique()

# %%
buildings.describe() # for R users this is like the "summary"

# %%
buildings['Square Footage'] == 0

# %%
buildings.loc[buildings['Square Footage']==0]

# %%
import matplotlib.pyplot as plt

# %%
buildings['Square Footage'].plot()
plt.show()

# %%
buildings['Square Footage'].plot(figsize=(10,3))
plt.show()

# %%
buildings.plot(x='Address', y='Square Footage', figsize=(10,3), rot=90)
plt.show()

# %%
ax = buildings.plot(x='Year Acquired', y='Square Footage', 
                    figsize=(10,3),kind='scatter')
ax.set_xlim(1750,2020)
plt.show()

# %%
buildings = pd.read_csv('https://github.com/UIUC-iSchool-DataViz/is445_data/raw/main/building_inventory.csv',
                       na_values = {'Square Footage':0,
                                   'Year Acquired':0,
                                   'Year Constructed':0})

# %%
ax = buildings.plot(x='Year Acquired', y='Square Footage', 
                    figsize=(10,3),kind='scatter')
#ax.set_xlim(1750,2020)
plt.show()

# %%
buildings.describe()

# %%
buildings['Bldg Status'].unique()

# %%
buildings.groupby('Bldg Status')

# %%
for group in buildings.groupby('Bldg Status'):
    print(group)

# %%
for group_name, group_df in buildings.groupby('Bldg Status'):
    print(group_name, group_df.shape)

# %%
buildings2 = buildings.sort_values("Year Constructed")

# %%
buildings2.iloc[0]

# %%
agg = buildings.groupby("Year Acquired")['Square Footage'].sum()
# for each Year Acquired, what is the total (sum) of the Square Footage

#agg = buildings.groupby("Year Acquired")['Square Footage'].mean()
# for each Year Acquired, what is the average (mean) of the Square Footage

# %%
agg

# %%
type(agg)

# %%
type(buildings)

# %%
agg.index

# %%
agg.values

# %%
fig, ax = plt.subplots(figsize=(15,4))

ax.plot(agg.index, agg.values)
ax.set_xlabel('Year Constructed')
ax.set_ylabel('Total (sum) Square Footage')

plt.show()

# %%
agg.plot()

# %%
stats = buildings.groupby('Year Acquired')['Square Footage'].describe()

# %%
stats

# %%
type(stats)

# %%
stats.plot(y='count')

# %%
stats.columns

# %%
buildings

# %%
buildings['Zip code'].value_counts()

# %%
buildings['Zip code'].value_counts().iloc[0:5]

# %%
buildings['Zip code'].value_counts().iloc[0:5].index # 5 most common zipcodes in my dataframe

# %%
most_common_zips = buildings['Zip code'].value_counts().iloc[0:5].index
most_common_zips

# %%
# Check out the ".isin" function for some examples that might be useful <-- HINT

# %%
gb1 = buildings.groupby('Bldg Status')['Year Acquired'].min()

# %%
gb1

# %%
fig_gb1, ax_gb1 = plt.subplots()
gb1.plot(kind='bar', ax=ax_gb1)
plt.show()

# %%
fig_gb1, ax_gb1 = plt.subplots()
ax_gb1.bar(gb1.index, gb1.values)
plt.show()

# %%
# ax_gb1.bar?

# %%
