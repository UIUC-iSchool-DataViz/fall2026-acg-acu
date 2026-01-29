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
#   title: Some basics
# ---

# %%
# # ! pip install matplotlib
# # ! pip install pandas
# # ! pip install numpy

# %%
import matplotlib.pyplot as plt # The plotting library
import numpy as np 
import pandas as pd # Library for working with tabular data, such as CSV and TSV

# Magic command for showing plot inline
# %matplotlib inline 

# %% [markdown]
# # Some basics

# %%
# Create a figure 
# fig, ax OR plt.plot()

plt.plot() # Create an empty figure

# %%
# Create a figure 
# fig, ax OR plt.plot()
fig, ax = plt.subplots() # Create an empty figure

# %%
# Create a figure having two horizonal subplots.
fig, ax = plt.subplots(1, 2, figsize=(10, 5))

# 1 in subplots(1, 2) indicates the number of rows in the figure
# 2 in subplots(1, 2) indicates the number of colum in the figure
# figsize=(10, 5) indicates this is an 10 inch by 5 inch figure

# %%
# Create a figure having two vertical subplots.
fig, ax = plt.subplots(2, 1, figsize=(5, 10))

# 2 in subplots(2, 1) indicates the number of rows in the figure
# 1 in subplots(2, 1) indicates the number of colum in the figure
# figsize=(5, 10) indicates this is an 5 inch by 10 inch figure

# %%
# Create a figure having four subplots.
fig, ax = plt.subplots(2, 2)

# subplots(2, 2) tells matplotlib to draw a figure with 2 by 2 subplots in it.

# %%
# plot a line

x = [1, 2, 3, 4] # x coordinates
y = [4, 3, 4, 3] # y coordinates

fig, ax = plt.subplots() # Make an empty figure
ax.plot(x, y) # draw a line on the figure. The line is drawn from the x and y coordinates.

plt.show()

# %%
# plot two lines in one figure
x = [1, 2, 3, 4]
y = [4, 3, 4, 3]

y1 = [3, 3, 3, 3]

fig, ax = plt.subplots()
ax.plot(x, y) # Plot the first line using the x and y coordinates.
ax.plot(x, y1, linewidth=10) # Plot the second line using the x and y1 coordinates.

plt.show()

# %%
# plot two lines in two subplots (1*2)

fig, ax = plt.subplots(1, 2)

ax[0].plot(x, y) 
# Plot the first line using the x and y coordinates.
# here, the 0 in ax[0] picks the first axis, which is the left subplot

ax[1].plot(x, y1) 
# Plot the second line using the x and y1 coordinates.
# here, the 1 in ax[1] picks the second axis, which is the right subplot

plt.show()

# %%
# plot lines in subplots (2*2)

fig, ax = plt.subplots(2, 2)

# color= indicate the color of the line
# 'r' is red, 'b' is blue, and 'k' is black

ax[0, 0].plot(x, y, color='r') # upper left
# ax[0, 0] picks the axis at the first row (0) and the first column (0) in the figure, which is the upper left subplot.

ax[0, 1].plot(x, y1, color='b') # upper right
# ax[0, 1] picks the axis at the first row (0) and the second column (1)

ax[1, 0].plot(x, y, color='k') # lower left
# ax[1, 0] picks the axis at the second row (1) and the first column (0)

ax[1, 1].plot(x, y1, color='orange') # lower right
# ax[1, 1] picks the axis at the second row (1) and the second column (1)

plt.show()

# %% [markdown]
# # Pandas

# %%
# !wget https://uiuc-ischool-dataviz.github.io/spring2019online/week02/building_inventory.csv
    
# This is for downloading the CSV file

# %%
# Read file

df = pd.read_csv('building_inventory.csv', sep=',') 
# sep is the separator. 
# sep=',' for CSV and sep='\t' for TSV 

df.head() # Show the fisrt 5 row in the CSV file

# %%
# Number of rows and columns

df.shape # returns the number of rows and columns (n_rows, n_cols)

# %%
# Assign ID to each building

df = df.reset_index() # reset the index as a colum
df = df.rename(columns={'index':'Building ID'}) # rename the "index" colum we just reset as the name 'Building ID'
df.head()

# %%
# Summary of a DataFrame.

df.info() 

# Dtype shows the data type of each column 
# Non-Null Count shows the number of row that is not null (i.e., have values)

# %%
# Descriptive statistics of the numerical columns

df.describe()

# %%
# Covert data type

df['Zip code'] = df['Zip code'].astype(str) 
# Change the data type of 'Zip code' column from integer to string
# [] in df['Zip code'] is for selecting the 'Zip code' column

df.info()

# %%
# Missing values
df.isna().sum() 
# isna() select the rows having null values (i.e., missing values), and sum() counts the number of rows having null values.

# %%
# Unique values in a column
df['Year Acquired'].unique()

# %%
# Arithmetic operation

df['Age at Acqusition'] = df['Year Acquired'] - df['Year Constructed']
# This adds a new column 'Age at Acqusition' to the dataframe

df.head()

# %%
# Filter by relationship

fiter_1 = df['Year Acquired'] > 0 
# for selecting rows that the value in 'Year Acquired' greater than 0

fiter_2 = df['Year Constructed'] > 0
# for selecting rows that the value in 'Year Constructed' greater than 0

fiter_3 = df['Age at Acqusition'] >= 0
# for selecting rows that the value in 'Age at Acqusition' greater than or equal to 0


df_filtered = df.loc[(fiter_1)&(fiter_2)&(fiter_3)].copy()
# .loc[] select rows based on the filter (or filters) applied to the column (or columns)

# .loc[(fiter_1)&(fiter_2)&(fiter_3)] means that I select rows that satisfy all three filters.
# in other words, the selected rows meet all the three conditions:
# 1 - 'Year Acquired' is greater than 0
# 2 - 'Year Constructed' is greater than 0, and 
# 3 - 'Age at Acqusition' is greater than or equal to 0.

# .copy() is to copy the selected rows as a new dataframe

print(df.shape) # print n_rows, n_cols in the original dataframe
print(df_filtered.shape) # print n_rows, n_cols in the new dataframe (the selected one)

# %%
# Filter by relationship, set based

rows_in_2004_2006 = df.loc[df['Year Acquired'].isin([2004, 2006])]
# Filter performed on one colum, 'Year Acquired', that the year value in 'Year Acquired' is in [2004, 2006]

print(rows_in_2004_2006.shape) # n_cols, n_rows after filtering
print(rows_in_2004_2006['Year Acquired'].unique()) # unique values in the Year Acquired colum after filtering
rows_in_2004_2006.head()

# %%
# Sampling, by number
df.sample(30) # Get a sample that has 30 records.

# %% [markdown]
# # Histogram

# %%
# A hist draw from 'Age at Acquisition' column

fig, ax = plt.subplots() # make an empty figure

ax.hist(df_filtered['Age at Acqusition'], bins=5) # .hist() draws a histogram 
# .hist(df_filtered['Age at Acqusition']) draws a histogram using the 'Age at Acqusition' column
# bins=5 means 5 bins with equal width

plt.show()

# %%
# log scale

fig, ax = plt.subplots()

ax.hist(df_filtered['Age at Acqusition'], bins=10, log=True) # .hist() draw a histogram 
# .hist(df_filtered['Age at Acqusition']) draw a histogram using the 'Age at Acqusition' column
# bins=10 means 10 bins with equal width
# log=True makes the y as log scale. 

plt.show()

# %%
# non-uniform bins

fig, ax = plt.subplots()

ax.hist(df_filtered['Age at Acqusition'], bins=[0, 100, 200, 233], log=True)
# .hist() draw a histogram 
# .hist(df_filtered['Age at Acqusition']) draw a histogram using the 'Age at Acqusition' column

# bins=[0, 100, 200, 233] makes 3 bins:
# first bin incudes data values from 0 to less than 100
# second bin incudes data values from 100 to less than 200
# first bin incudes data values from 200 to 233 (233 is included.)

# log=True makes the y as log scale. 

plt.show()

# %% [markdown]
# # Bar chart

# %%
# A bar chart with groups using 'Bldg Status' column
# Group by categories, count 

print(df['Bldg Status'].unique()) # print unique values in Bldg Status colum

# Count how many bulidings belongs to each building status
df2draw = df.groupby(['Bldg Status'])[['Building ID']].count()
# .groupby() groups rows by unique values in the colum 
# .groupby(['Bldg Status']) group rows by the unique values in the Bldg Status colum
# [['Building ID']] selects the 'Building ID' column for counting the rows 
# .count() counts the non-null rows in the Building ID column

# In brief, this line of code first groups the rows by the unique values in Bldg Status colum
# then counts the number of non-null rows in the Building ID column belongs to each group
# We count the Building ID column beacuse each Building ID represents a building.


df2draw # show the result

# Explanation of the result: 
# 226 buildings have building status as Abandon
# 113 buildings have building status as In Progress
# 8523 buildings have building status as In Use

# %%
# Make a bar chart
fig, ax = plt.subplots() # Make an empty plot

ax.bar(df2draw.index, df2draw['Building ID'])
# .bar() draws a bar chart
# .bar(df2draw.index, df2draw['Building ID']) draw a bar chart in which
# Bldg Status (df2draw.index) as x
# Number of buldings (df2draw['Building ID']) as y

ax.set_xlabel('Buliding status') # Set the x label
ax.set_ylabel('Number of buildings') # Set the y label

plt.show()

# %%
fig, ax = plt.subplots()

ax.bar(df2draw.index, df2draw['Building ID'], log=True) # Same as above, but make y as log scale

ax.set_xlabel('Buliding status') # Set the x label
ax.set_ylabel('Number of buildings') # Set the y label

plt.show()

# %%
# Group by categories, sum 

df2draw = df_filtered.groupby(df_filtered['Bldg Status'])[['Square Footage']].sum()
# .groupby() groups rows by unique values in the colum 
# .groupby(['Bldg Status']) group rows by the unique values in the Bldg Status colum
# [['Square Footage']] selects the 'Square Footage' column 
# .sum() returns the sum of the values in the Square Footage column

# In brief, this line of code first groups the rows by the unique values in Bldg Status colum
# then calculate the sum of the values in the Square Footage column belongs to each group

df2draw # show the result

# %%
fig, ax = plt.subplots()

ax.bar(df2draw.index, df2draw['Square Footage'])
# .bar(df2draw.index, df2draw['Square Footage']) draw a bar chart in which
# Bldg Status (df2draw.index) as x
# Sum of Square Footage (df2draw['Square Footage']) as y

ax.set_xlabel('Building Status') # Set x label
ax.set_ylabel('Total Square Footage') # Set y label

plt.show()

# %%
# Group by categories, mean 

df2draw = df_filtered.groupby(df_filtered['Bldg Status'])[['Square Footage']].mean()
# .groupby(['Bldg Status']) group rows by the unique values in the Bldg Status colum
# [['Square Footage']] selects the 'Square Footage' column 
# .mean() returns the mean of the values in the Square Footage column

# In brief, this line of code first groups the rows by the unique values in Bldg Status colum
# then calculate the mean of the values in the Square Footage column belongs to each group

df2draw # shows the result

# %%
fig, ax = plt.subplots()

ax.bar(df2draw.index, df2draw['Square Footage'])
# .bar(df2draw.index, df2draw['Square Footage']) draw a bar chart in which
# Bldg Status (df2draw.index) as x
# Mean of Square Footage (df2draw['Square Footage']) as y

ax.set_ylabel('Mean of Square Footage') # Set x label
ax.set_xlabel('Building Status') # Set y label

plt.show()

# %% [markdown]
# # Scatter plot
# [matplotlib.markers](https://matplotlib.org/stable/api/markers_api.html)    
# [linestyle](https://matplotlib.org/stable/gallery/lines_bars_and_markers/linestyles.html)

# %%
# Draw a scatter plot by using plt.plot 
x = [1, 2, 3, 4]
y = [4, 3, 4, 2]

fig, ax = plt.subplots() # create an empty figure

ax.plot(x, y, marker='o', linestyle='') 
# marker='o' defines the markers (i.e., x and y coordinates) as circles
# linestyle='' sets the lines connecting the markers invisible. 

plt.show()

# %%
# Draw a scatter plot by using .scatter()

fig, ax = plt.subplots() # create an empty figure

ax.scatter(x, y) # .scatter() draw a scatter plot using the x and y values

plt.show()

# %%
# Without cleaning the data...

x = df['Year Constructed']
y = df['Year Acquired']

fig, ax = plt.subplots()

ax.scatter(x, y)

plt.show()

# %%
# Cleaned data

x = df_filtered['Year Constructed']
y = df_filtered['Year Acquired']

fig, ax = plt.subplots()

ax.scatter(x, y)

ax.set_xlabel('Year Constructed')
ax.set_ylabel('Year Acquired')

plt.show()

# %% [markdown]
# # Line plot

# %%
# Number of buldings along year constructed

df2draw = df_filtered.groupby(df_filtered['Year Constructed'])[['Building ID']].count()
# .groupby(['Year Constructed']) group rows by the unique values in the Year Constructed colum
# [['Building ID']] selects the 'Building ID' column 
# .count() counts the number of rows in the Building ID column belonging to each group

# In brief, this line of code first groups the rows by the unique values in Year Constructed colum
# then count the rows in the Building ID column belongs to each group (i.e., how many buldings in each group)

df2draw # Shows the result

# %%
fig, ax = plt.subplots()

ax.plot(df2draw.index, df2draw['Building ID'])
# .plot() draws the line plot
# X as years in Year Constructed (df2draw.index)
# Y as number of buildings (df2draw['Building ID'])

ax.set_xlabel('Year Constructed') # X label
ax.set_ylabel('Number of buildings') # Y label

plt.show()

# %% [markdown]
# # Color, marker, and size

# %%
# We can iterate over the groups

# .group() returns a group object
groups = df_filtered.groupby(df_filtered['Bldg Status'])
type(groups)

# %%
# We can iterate over the groups

for name, group in groups:
    print(name, type(group))
    # name are the unique values in the colum used for groupby(). In this case, names are the uinique values in Bldg Status column
    # group return the rows belonging to a group

# %%
# Color by group

groups = df_filtered.groupby(df_filtered['Bldg Status'])

fig, ax = plt.subplots(figsize=(10, 10))

colors = {'Abandon': 'red', 'In Progress': 'blue', 'In Use': 'black'} # This is a dictionay for looking up colors


for name, group in groups: # Iterate over groups
    # plot dots on scatter plot, each time plots the dots belongs to a group
    ax.scatter(group['Year Constructed'], group['Year Acquired'], color=colors[name])
    
    # group['Year Constructed'] are X values in the scatter plot
    # group['Year Acquired'] are Y values in the scatter plot
    # color= defines the color of the dots in a scatter plot
    # color=colors[name] assigns colors to dots by looking up colors given in the "colors" dictionary
    
plt.show()

# %%
# Marks by group
groups = df_filtered.groupby(df_filtered['Bldg Status'])

fig, ax = plt.subplots(figsize=(10, 10))

colors = {'Abandon': 'red', 'In Progress': 'blue', 'In Use': 'black'} # This is a dictionay for looking up colors
markers = {'Abandon': 'o', 'In Use': '^', 'In Progress': 'D'} # This is a dictionay for looking up markers

for name, group in groups:
    print(name, type(group), colors[name])
    ax.scatter(group['Year Constructed'], group['Year Acquired'], 
               color=colors[name], marker=markers[name])
    
    # group['Year Constructed'] are X values in the scatter plot
    # group['Year Acquired'] are Y values in the scatter plot
    # marker= assigns the marker to dots in a scatter plot
    # marker=markers[name] assigns markers to dots by looking up markers given in the "markers" dictionary
    
plt.show()

# %%
# Size by group

groups = df_filtered.groupby(df_filtered['Bldg Status'])

fig, ax = plt.subplots(figsize=(10, 10))

colors = {'Abandon': 'red', 'In Progress': 'blue', 'In Use': 'black'} # This is a dictionay for looking up colors
sizes = {'Abandon': 100, 'In Progress': 50, 'In Use':5} #  This is a dictionay for looking up sizes

for name, group in groups:
    print(name, type(group))
    ax.scatter(group['Year Constructed'], group['Year Acquired'], color=colors[name], s=sizes[name])
    
    # group['Year Constructed'] are X values in the scatter plot
    # group['Year Acquired'] are Y values in the scatter plot
    # s= assigns dot size
    # s=sizes[name] assigns dot size by looking up the size given in the "sizes" dictionary
    
plt.show()

# %%
