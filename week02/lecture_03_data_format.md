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
  title: CSV
---

```python
# ! pip install matplotlib
# ! pip install numpy
# ! pip install h5py
```

```python
import json
import h5py
import numpy as np
```

# CSV

```python
!wget https://think.cs.vt.edu/corgis/datasets/csv/airlines/airlines.csv
```

```python
f = 'airlines.csv'

with open(f, 'r') as fin:
    data = fin.readlines()
    
print(len(data))
```

```python
data[0]
```

```python
data[1]
```

```python
data[2]
```

```python
data[-1]
```

```python
line = data[1].split(',')
line
```

```python
print(line[0])
```

```python
print(type(line[0]))
```

```python
print(line[6])
```

```python
print(type(line[6]))
```

# JSON

```python
!wget https://think.cs.vt.edu/corgis/datasets/json/airlines/airlines.json
```

```python
f = 'airlines.json'

with open(f, 'r') as fin:
    data = json.load(fin)

print(len(data))
```

```python
data[0]
```

```python
data[:3]
```

```python
type(data[0])
```

```python
one_record = data[0]
one_record.get('Airport')
```

```python
print(type(one_record.get('Airport')))
```

```python
total_number_of_delays = 0

for d in data:
    airport_code = d.get('Airport').get('Code')
    number_of_delay = d.get('Statistics').get('# of Delays').get('Weather')
    
    if airport_code == 'ORD':
        total_number_of_delays += number_of_delay
total_number_of_delays
```

# HDF5

```python
!wget https://raw.githubusercontent.com/TK-Hsiao/TK-Hsiao.github.io/master/data/airlines.h5
```

```python
def printname(name):
    print(name)
```

```python
hf = h5py.File('airlines.h5', 'r')
print(type(hf))
```

```python
hf.visit(printname)
```

```python
ord_airport = hf.get('ORD')
print(ord_airport)
```

```python
ord_airport.visit(printname)
```

```python
print(ord_airport.get('delays_in_2003'))
```

```python
print(np.array(ord_airport.get('delays_in_2003')))
```

```python
hf.close()
```

```python

```
