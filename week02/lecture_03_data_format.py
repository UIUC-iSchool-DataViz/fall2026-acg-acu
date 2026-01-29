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
#   title: CSV
# ---

# %%
# # ! pip install matplotlib
# # ! pip install numpy
# # ! pip install h5py

# %%
import json
import h5py
import numpy as np

# %% [markdown]
# # CSV

# %%
# !wget https://think.cs.vt.edu/corgis/datasets/csv/airlines/airlines.csv

# %%
f = 'airlines.csv'

with open(f, 'r') as fin:
    data = fin.readlines()
    
print(len(data))

# %%
data[0]

# %%
data[1]

# %%
data[2]

# %%
data[-1]

# %%
line = data[1].split(',')
line

# %%
print(line[0])

# %%
print(type(line[0]))

# %%
print(line[6])

# %%
print(type(line[6]))

# %% [markdown]
# # JSON

# %%
# !wget https://think.cs.vt.edu/corgis/datasets/json/airlines/airlines.json

# %%
f = 'airlines.json'

with open(f, 'r') as fin:
    data = json.load(fin)

print(len(data))

# %%
data[0]

# %%
data[:3]

# %%
type(data[0])

# %%
one_record = data[0]
one_record.get('Airport')

# %%
print(type(one_record.get('Airport')))

# %%
total_number_of_delays = 0

for d in data:
    airport_code = d.get('Airport').get('Code')
    number_of_delay = d.get('Statistics').get('# of Delays').get('Weather')
    
    if airport_code == 'ORD':
        total_number_of_delays += number_of_delay
total_number_of_delays


# %% [markdown]
# # HDF5

# %%
# !wget https://raw.githubusercontent.com/TK-Hsiao/TK-Hsiao.github.io/master/data/airlines.h5

# %%
def printname(name):
    print(name)


# %%
hf = h5py.File('airlines.h5', 'r')
print(type(hf))

# %%
hf.visit(printname)

# %%
ord_airport = hf.get('ORD')
print(ord_airport)

# %%
ord_airport.visit(printname)

# %%
print(ord_airport.get('delays_in_2003'))

# %%
print(np.array(ord_airport.get('delays_in_2003')))

# %%
hf.close()

# %%
