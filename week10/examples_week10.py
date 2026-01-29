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
#   title: Examples Week10
# ---

# %%
import bqplot
import json
import numpy as np
import pandas as pd

# %%
tree_data = json.load(open("../workspace/champaign_trees.geojson", "r"))

# %%
tree_data.keys()

# %%
tree_data['type']

# %%
len(tree_data['features'])

# %%
tree_data['features'][0]

# %%
sc_map = bqplot.AlbersUSA()
sc_color = bqplot.ColorScale()
us_map = bqplot.Map(map_data = bqplot.topo_load("map_data/USStatesMap.json"),
                           scales = {'projection': sc_map,
                                    "color": sc_color},
                    colors = {"default_color": "black"},
                    color = {_:_ for _ in np.arange(100)})

fig = bqplot.Figure(marks = [us_map])

display(fig)

# %%
import ipywidgets

# %%
l = ipywidgets.Label()
def change_label(event):
    l.value = str(event['new'])

champaign_map.observe(change_label, ["selected"])
l

# %%

# %%
legislators = pd.read_csv("../workspace/legislators_historical.csv")

# %%
legislators_terms = pd.read_csv("../workspace/legislators_historical_terms.csv")

# %%
fips = pd.read_csv("../workspace/state_fips_master.csv")

# %%
legislators_terms.state

# %%
fips_lookup = {row['state_abbr']: row['fips'] for _, row in fips.iterrows()}

# %%
legislators_fips = legislators_terms.replace({"state": fips_lookup})

# %%
colors = dict(legislators_fips.groupby("state").count()["bioguide"])

# %%
sc_map = bqplot.AlbersUSA()
sc_color = bqplot.ColorScale(scheme = "Blues")
us_map = bqplot.Map(map_data = bqplot.topo_load("map_data/USStatesMap.json"),
                           scales = {'projection': sc_map,
                                    "color": sc_color},
                    colors = {"default_color": "black"},
                    color = colors)

fig = bqplot.Figure(marks = [us_map])

display(fig)

# %%
