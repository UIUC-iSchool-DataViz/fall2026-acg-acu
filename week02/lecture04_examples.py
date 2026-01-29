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
#   title: Examples for Lecture 4
# ---

# %% [markdown]
# # Examples for Lecture 4
#
# We will be covering two principal areas:
#
#  * A few types of aggregation -- counting, average, weighted average, sum
#  * The "building inventory" dataset, and some simple pandas operations on it

# %%
# !wget https://uiuc-ischool-dataviz.github.io/spring2019online/week02/building_inventory.csv

# %%
# %matplotlib inline

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# %%
df = pd.read_csv("building_inventory.csv")

# %%
df.columns

# %%
df.dtypes

# %%
df.head()

# %%
df.describe()

# %%
df.shape

# %%
(df["Year Acquired"] == 0).sum()

# %%
(df["Year Constructed"] == 0).sum()

# %%
(df["Square Footage"] == 0).sum()

# %%
df = pd.read_csv("building_inventory.csv", na_values={
    "Year Acquired": 0,
    "Year Constructed": 0,
    "Square Footage": 0
})

# %%
df.describe()

# %%
plt.plot([1,2,3,4], [5, 1, 2, 4], "-o")

# %%
plt.rcParams["figure.dpi"] = 200

# %%
plt.plot(df["Year Constructed"], df["Year Acquired"], '.')
plt.xlabel("Year Constructed")
plt.ylabel("Year Acquired")

# %%
df["Age at Acquisition"] = df["Year Acquired"] - df["Year Constructed"]

# %%
df["Age at Acquisition"].describe()

# %%
old_buildings = df[
    df["Age at Acquisition"] >= 0
]

# %%
plt.hist(old_buildings["Age at Acquisition"], log=True)
plt.xlabel("Age at Acquisition")
plt.ylabel("Count")

# %%
df["Agency Name"].unique()

# %%
df_by_agency = df.groupby("Agency Name")

# %%
for agency_name, new_df in df_by_agency:
    print(agency_name, new_df.shape)

# %%
df_by_agency["Square Footage"].sum()

# %%

# %%
