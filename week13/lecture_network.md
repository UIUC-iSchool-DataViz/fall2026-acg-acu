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
  title: Drawing a network using Bqplot
---

```python
#!pip install igraph
```

```python
import igraph
import bqplot
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import ipywidgets
```

## Example: Force-directed graph is not deterministic

```python
n_nodes = 10
edges = [[0, 1], [0, 2], [0, 3], [2, 3], [1, 3], [3, 4], [3, 5], [3, 7], 
         [4, 5], [6, 7], [7, 8], [8, 9]]
network = igraph.Graph(n=n_nodes, edges=edges)
network.vs['name'] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

fig, ax = plt.subplots(figsize=(5, 5))
igraph.plot(network, 
            target=ax, 
            layout='fr',
            vertex_label=network.vs['name'], 
            vertex_color='grey', 
            vertex_size=0.5)

plt.show()
```

```python
# Compared to ring layout

fig, ax = plt.subplots(figsize=(5, 5))
igraph.plot(network, 
            target=ax, 
            layout='circle',
            vertex_label=network.vs['name'], 
            vertex_color='grey', 
            vertex_size=0.5)

plt.show()
```

# Drawing a network using Bqplot

```python
# Only nodes

# Node data
node_data = [
    {'label':'Batman', 'shape':'circle', 'is_villain':False}, # A node
    {'label':'Superman', 'shape':'circle', 'is_villain':False},
    {'label':'Aquaman', 'shape':'circle', 'is_villain':False},
    {'label':'Joker', 'shape':'rect', 'is_villain':True},
    {'label':'Riddler', 'shape':'rect', 'is_villain':True},
    {'label':'Ivy', 'shape':'rect', 'is_villain':True},
]

# Network 
dc_net = bqplot.Graph(node_data=node_data)

# Fig
fig = bqplot.Figure(marks=[dc_net])
fig
```

```python
# Add tooltip and set colors
#dc_net.traits()

dc_net.colors = ['blue', 'blue', 'blue', 'red', 'red', 'red']

dc_tooltip = bqplot.Tooltip(fields=['is_villain'])
dc_net.tooltip = dc_tooltip

fig
```

```python
# Add edges between the good characters

edge_data = [
    {'source':0, 'target':1}, # a connection from node 0 to node 1
    {'source':0, 'target':2},
    {'source':1, 'target':2},
]

dc_net.link_data = edge_data

fig
```

```python
# make links as straight lines
dc_net.link_type = 'line'
fig
```

```python
# make graph as undirected
dc_net.directed = False
fig
```

```python
# Putting things together

# Nodes and edges

node_data = [
    {'label':'Batman', 'shape':'circle', 'is_villain':False}, # A node
    {'label':'Superman', 'shape':'circle', 'is_villain':False},
    {'label':'Aquaman', 'shape':'circle', 'is_villain':False},
    {'label':'Joker', 'shape':'rect', 'is_villain':True},
    {'label':'Riddler', 'shape':'rect', 'is_villain':True},
    {'label':'Ivy', 'shape':'rect', 'is_villain':True},
]

edge_data = [
    {'source':0, 'target':1}, # a connection from node 0 to node 1
    {'source':0, 'target':2},
    {'source':1, 'target':2},
]

# Network 
dc_net = bqplot.Graph(node_data=node_data, 
                      link_data=edge_data, 
                      colors = ['blue', 'blue', 'blue', 'red', 'red', 'red'], 
                      link_type='line', 
                      directed=False, 
                      tooltip = bqplot.Tooltip(fields=['is_villain']))

# Fig
fig = bqplot.Figure(marks=[dc_net])
fig
```

# iGraph basics

```python
# Construct a undirected network
n_node = 4
edges = [[0, 1], [0, 2]]
undirected_net = igraph.Graph(n=n_node, edges=edges)
print(undirected_net)
```

```python
# Construct a directed network
n_node = 4
edges = [[0, 1], [0, 2]]
directed_net = igraph.Graph(n=n_node, edges=edges, directed=True)
print(directed_net)
```

```python
# Adjacency Matrix - Undirected
print(undirected_net.get_adjacency())
```

```python
# Adjacency Matrix - directed
print(directed_net.get_adjacency())
```

```python
# Add node
undirected_net.add_vertices(2)
print(undirected_net)
```

```python
# Add edge
undirected_net.add_edges([[3, 4]])
print(undirected_net)
```

```python
# Plot the network
fig, ax = plt.subplots(figsize=(5, 5))
igraph.plot(undirected_net, 
            target=ax)
plt.show()
```

```python
# Node and edge attributes. For example, get Node IDs
print(undirected_net.vs)
print(undirected_net.vs.indices)
print(undirected_net.es)
```

```python
# Get edge list
undirected_net.get_edgelist()
```

```python
# Add attributes
undirected_net.vs['names'] = ['batman', 'superman', 'aquaman', 'joker', 'riddler', 'ivy']
undirected_net.vs['age'] = [40, 100, 35, 25, 45, 30]
undirected_net.vs['is_villain'] = [False, False, False, True, True, True]
print(undirected_net)
```

```python
# Access attribute values
undirected_net.vs['names']
```

```python
# Setting colors, size, etc by attributes

fig, ax = plt.subplots(figsize=(5, 5))
igraph.plot(undirected_net, 
            target=ax, 
            vertex_label = undirected_net.vs['names'], 
            vertex_size = [age/100 for age in undirected_net.vs['age']])

plt.show()
```

# iGraph and Pandas

```python
!wget https://databank.illinois.edu/datafiles/1dvfq/download -O article_attr.csv
!wget https://databank.illinois.edu/datafiles/5r2ds/download -O inclusion_net.csv
```

```python
# Edge file
edge_file = pd.read_csv('inclusion_net.csv')
edge_file
```

```python
# Nodes and Node attribute file
node_file = pd.read_csv('article_attr.csv')
node_file
```

```python
# Generate nodes and edges from dataframe
nodes = node_file[['ID']].to_dict('records')
edges = edge_file.to_dict('records')
print('First 3 nodes:', nodes[:3])
print('First 3 edges:', edges[:3])
```

```python
# Build a network
net = igraph.Graph.DictList(vertices = nodes, 
                            edges = edges, 
                            vertex_name_attr = 'ID', 
                            edge_foreign_keys = ('citing_ID', 'cited_ID'), 
                            directed=True)
print(net)
```

```python
# Plot the net
fig, ax = plt.subplots(figsize=(10, 10))
igraph.plot(net,
            layout='fr',
            target=ax, 
            edge_arrow_size = 0.03)
plt.show()
```

```python
# Add node attributes
net.vs['publication_type'] = node_file['Type']
net.vs['publication_year'] = node_file['year']
print(net)
```

```python
# Color by publication_type
node_clr = []
for pt in net.vs['publication_type']:
    if pt == 'Systematic Review':
        node_clr.append('red')
    else:
        node_clr.append('yellow')
        
fig, ax = plt.subplots(figsize=(10, 10))
igraph.plot(net,
            layout='fr',
            target=ax, 
            edge_arrow_size = 0.03, 
            vertex_color = node_clr)
plt.show()
```

```python
# Node size by ciation counts
net.vs['citation_count'] = net.degree(mode='in')

fig, ax = plt.subplots(figsize=(10, 10))
igraph.plot(net,
            layout='fr',
            target=ax, 
            edge_arrow_size = 0.03, 
            vertex_color = node_clr, 
            vertex_label = net.vs['ID'], 
            vertex_size = [np.log(c+1)/2 for c in net.vs['citation_count']])
plt.show()
```

# Get subgraph

```python
# Select Nodes in the node file: Systematic reviews published in 2011
filter_py = node_file['year'] == 2011
filter_pt = node_file['Type'] == 'Systematic Review'
selected_nodes = node_file[(filter_py)&(filter_pt)]['ID'].tolist()
print(selected_nodes)
```

```python
# Selected edges by the nodes
selected_egdes = net.es.select(citing_ID_in = selected_nodes)
print(selected_egdes)
for e in selected_egdes:
    print(e)
```

```python
# Get subgraph
sub_net = net.subgraph_edges(selected_egdes)
print(sub_net)
```

```python
# Plot the subgraph
# Nodes labelled by publication year
# Edges colored by the citing source

edge_clr = []
for e in sub_net.get_edgelist():
    if e[0] == 0:
        edge_clr.append('blue')
    else:
        edge_clr.append('orange')
        
fig, ax = plt.subplots(figsize=(10, 10))
igraph.plot(sub_net, 
            target=ax, 
            edge_color = edge_clr, 
            vertex_label = sub_net.vs['publication_type'])
plt.show()
```

```python

```
