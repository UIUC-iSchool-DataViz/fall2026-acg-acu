---
title: Choosing Charts
layout: lecture
tags:
  - vega-lite
  - choosing-charts
description: >-
  We go over some types of visualization and finish our COVID lab discussion.
---

# Finish our lab and choosing viz

---

## Final Project

There are three components, turned in the last three weeks of class.

You will have three general components:

1. Viz for Self (Due Apr 17 - individual)
1. Viz for Peers (Due Apr 25 - group)
1. Viz for Others (Due Apr 29 (for feedback), May 8 (final) - part group/part individual)

Be aware:
 * **NO** extensions for these assignments.
 * There is a group-submission option (sign up open, closes next week!).

note:
just some reminders about the final project

there are NO extensions available -- you can't use one of your HW extensions for these components

also, parts 2 & 3 will be in a group, however you will pick your own groups AND you can be in a group of 1 if you want 

**go to where groups are in student view on Canvas**


---

## Groups (Parts 2 & 3)

* Group size: maximum 4, minimum 1 (i.e. doing the final on your own)
* Ask group members before you join a group!
* Sign up on Canvas under `People` $\rightarrow$ `Groups`
* Want to find a group?  Check out the **`#find-a-final-project-group`** channel on Slack 
* **Group sign-up closes April 15**


---

## Final Project: Part 1 -- Individual

Submit in a Jupyter notebook.

 * Identify a dataset to explore.
   * This will be iterative!  You probably won't get one you like on the first
     try.
   * Check out sources like [data.world](https://data.world/),
     [data.illinois.gov](https://data.illinois.gov/),
     [data.gov](https://data.gov/),
     [developer.marvel.com](https://developer.marvel.com/),
     [IDB](https://databank.illinois.edu/), etc.
   * or the dataset doc that [lives right here](https://docs.google.com/document/d/15UJinT5XokAHXd9fQAYD8f6d3vEkR6kJMq8kswmkOhY/edit?usp=sharing)
 * Explore the dataset in a Jupyter notebook.  Make sure you include things that did and did not work.
 * Summarize the characteristics of the dataset in words: what does it
   represent, what are the fields/columns/rows, what data types are they, etc
   
note:
this will be the overview in general if you are doing an individual submission, for group we'll look at the requirements in a moment on the Canvas page

---

## Final Project: Part 1 -- Individual (cont)

Your datasets need to be submitted as well.  To do this, include this
information in your Jupyter notebook:

 * What is the "name" of the dataset?
 * Where did you obtain it?
 * Where can we obtain it?  (i.e., URL)
 * What is the license of the dataset?  What are we allowed to do with it?
 * How big is it in file size and in items?
 * Make a simple plot showing a relationship of interest.  You can use matplotlib or pandas (or other). Don't worry about colors, labels or anything else of that nature!

Be aware: You *must* make a plan for large datasets (larger than GitHub's upload limits).


---

## Final Project: Part 1 -- Individual (cont, cont)

You can share raw data sets and sources, ask questions about reading/modifying the dataset and post code to do so **that isn't working**.

Please do not share processed or cleaned datasets online.

---

## Final Project: Part 2

Submit in a Jupyter notebook.  

Be aware:
 * This should use the *same dataset* as Part 1.
 * Dashboard requirement (like Lab #5 with `bqplot`)

See Assignment description for more details. (You can see a PDF of a draft of the assignment on Canvas + rubric now, the full assignment will be come visible after groups are uploaded.)

note:
This part of the project will be like Lab #5 (which we know is a toughy!) -- if you didn't do well on Lab #5 and want to walk through how to approach this problem feel free to pop by office hours (mine or the TA's) and we'll walk you through it (any office hours should do, we all have the solutions :D )

Heads up that you can't really see any of this assignment on PL until you are in a group, but there is a PDF of an old version from last it was taught on a Canvas Module, 

---

## Final Project: Part 3

Visualization for the public -- see Assignment description for more details.

You will submit this as your final project and get some feedback -- both from the instructors and in the forum from your peers.

You will also provide feedback for 3 other students/groups (more on this later).

Your group will also submit a video discussing your work as part of this submission.

notes:
Heads up that like with Part 2, you can't really see any of this assignment on PL until you are in a group, but there is a PDF of an old version from last it was taught on a Canvas Module, just note some things will change sine we are doing streamlit instead of starboard.  

In addition to starboard becoming streamlit, the rubrics will change a bit.

Also be aware that your group will be required to submit a video discussing your work.  More info on this in a few weeks!






---

## Final Project: Part 3 (cont)

You will submit a link to a github pages site or webpage/app that you/your group has constructed.

This component will include a "for others" visualization that is deeply
narrative with appropriate interactive (or static) content which is sharable on a
website.

Some possible ways to approach this:

 * Jekyll+Altair (see template)
 * Raw HTML + Javascript
 * ~~Starboard website~~ Streamlit app
 * We will *not* be accepting jupyter notebooks/mybinder links this semester


---

## Technology vs Technique

The last few weeks, we have focused strongly on the technology behind visualizations.

We're going to spend a bit of time at the start of each class working on the _techniques_ behind the visualizations.

Today, we want to ask the question: how do we compare the elements that compose a whole?

---

## Composition

Don't use a pie chart.

<!-- .slide: data-background-image="images/piechart.png" data-background-size="auto 65%" data-background-position="right 50% bottom 50%" -->

notes:
pie charts force you to analyze things by area or angle, which are multidimensional attributes that are easy to confuse.

which is the most popular zoo animal in this pie chart? Elephants, otters, or lions?

---

## Composition

Don't use a pie chart.

<!-- .slide: data-background-image="images/piechartlabels.png" data-background-size="auto 65%" data-background-position="right 50% bottom 50%" -->

notes:
we can make a marginal improvement by labeling the values.

But we wouldn't be doing visualization if we were interested in just reading text.

---

## Composition

Don't use a pie chart.

<!-- .slide: data-background-image="images/3dpiechart.png" data-background-size="auto 65%" data-background-position="right 50% bottom 50%" -->

notes:
And if 2-dimensional area is difficult to understand, then 3-dimensional volume is even worse.

3 dimensional values violate the principle of proportional ink, which states that:

The sizes of shaded areas in a visualization need to be proportional to the data values they represent.

---

## Alternatives

<!-- .slide: data-background-image="images/donutchart.png" data-background-size="auto 65%" data-background-position="right 50% bottom 50%" -->

notes:
Some people will try to sell you on a modified version of a pie chart called a donut chart that has a hole in the middle. This is a slight improvement because it helps you see the values in the circle as 1-dimensional arc length instead of area.

But circles are still hard to decipher.

---

## Alternatives

<!-- .slide: data-background-image="images/treemap.png" data-background-size="auto 65%" data-background-position="right 50% bottom 50%" -->

notes:
We can reduce some of the confusion associated with using circles by creating proportional _rectangular_ area. Now we can compare along the dimensions of height and width for certain values.

But area is still problematic because it asks us to compare two dimensions - width and height - simultaneously.

---

## Alternatives

<!-- .slide: data-background-image="images/barchart.png" data-background-size="auto 65%" data-background-position="right 50% bottom 50%" -->

notes:
you can show comparitive values more effectively with a bar chart though. These values are easily compared along just one dimension.

---

## Alternatives

<!-- .slide: data-background-image="images/waterfallchart.png" data-background-size="auto 65%" data-background-position="right 50% bottom 50%" -->

notes:
there are really quite a few alternatives. There are many ways to show data stacking up progressively. This waterfall chart shows how each value is part of a whole, which was sort of the idea of the pie chart.

---

## Comparison

<!-- .slide: data-background-image="images/columnchart.png" data-background-size="auto 65%" data-background-position="right 50% bottom 50%" -->

notes:
to compare values from multiple sources, you could use collected columns

---

## Comparison

<!-- .slide: data-background-image="images/stackedcolumnchart.png" data-background-size="auto 65%" data-background-position="right 50% bottom 50%" -->

notes:
Or to show they're part of a whole, use a stacked column chart

---

## Comparison

<!-- .slide: data-background-image="images/stackedareachart.png" data-background-size="auto 65%" data-background-position="right 50% bottom 50%" -->

notes:
or to show a time-series, use connected lines that stack on top of each other to show area across the whole canvass. This shows you trends and specific vertical values.

---

## Comparison

This is not a good idea.

![](images/comparepiecharts.png)

---

## Hierarchical data

<!-- .slide: data-background-image="images/hierarchical_zoos.png" data-background-size="auto 65%" data-background-position="right 50% bottom 50%" -->

notes:
Sometimes we want to show data in a proportion and show connections.
This often happens for hierarcical data.

Here in this example we want to show proportions of land based mammals that
are popular at the zoo and then as we move out we subdivide by the individual
animal species.

## Hierarchical data: example packages

- Sunbursts (e.g., [snakeviz](https://jiffyclub.github.io/snakeviz/) )
- Nested box area (e.g., [callgrind](https://kcachegrind.github.io/html/Home.html) ) - for
  showing flowchart like structures for things like code programs

<div class="multiCol" data-markdown=true>

<div class="col" data-markdown=true>

![](images/sunburst.png)

</div><div class="col" data-markdown=true>

![](images/callgrind.gif)

</div> </div>

---

## Putting this Together

We can now put this together to construct a COVID-19 dashboard.

It must have these characteristics:

- Linking states to county-level visualizations
- Supplemental information about states, including an image
- Time series for national cases

How can we utilize our transforms, filters and view composition to this end?

---

## Today

1. GeoJSON format
1. More advanced vega-lite
1. Introduction to Altair

---

## GeoJSON I - Intro

http://geojson.org/ and http://geojson.io/

```json
{
  "type": "Feature",
  "geometry": {
    "type": "Point",
    "coordinates": [125.6, 10.1]
  },
  "properties": {
    "name": "Dinagat Islands"
  }
}
```

---

## GeoJSON II - Primitive Types

GeoJSON defines several primitive types:

- `Point` with associated `coordinates` (single set of two)
- `LineString` with associated `coordinates` that are lists of two items each
- `Polygon` with holes able to be cut out of it

Multi-part types are defined out of these.

---

## GeoJSON III - MultiPart Types

These are combined into multi-part types as follows:

- `MultiPoint`
- `MultiLineString`
- `MultiPolygon`

---

## More vega-lite

- vega-lite
  - transforming data
  - filtering data
- types of marks
  - arc
  - trail
  - image
  - geoshape
- encodings
  - tooltips


---

## Transforming

There are several `transform` options that we have not yet explored in detail.

- `fold`
- `flatten`
- `lookup`
- `window`
- `aggregate`


---

## Transform: `fold`

"`fold`"-ing a dataset transforms it by *expanding* to include additional keys,
to enable an additional parameter for selection.  For instance, if we have a
dataset of the form:

```json
[ {'name': ..., 'prop1': ..., 'prop2': ...}, ... ]
```

we can apply a `fold` of `prop1` and `prop2` to obtain:

```json
[ {'key': 'prop1', 'value': ..., 'name': ..., 'prop1': ..., 'prop2': ...},
  {'key': 'prop2', 'value': ..., 'name': ..., 'prop1': ..., 'prop2': ...} ]
```


---

## Transform: `flatten`

This operates similarly to `fold`, except that the inputs for `prop1` and
`prop2` are allowed to be arrays.  This produces a new set of rows in the
output data, one for each element in the corresponding arrays.

(This is less likely to be useful for input CSV data.)


---

## Transform: `lookup`

Occasionally we will want to use keys for lookup, based on other data rows.  We
can look up either in a named data source or in a fully-specified inline
datasource.

```json
{ "lookup": "primaryKey",
  "from": {
    "data": {"name": "referenceData"}
    "key": "keyInReference",
    "fields": ["prop1", "prop2"],
  }
}
```


---

## Transform: `window`

A `window` transform lets us perform an operation on a set of multiple rows in our dataset.  *Crucially* we can also specify the *order* that they are processed in.  It is defined like this:

```json
  "window": [{
	  "op": ...,
	  "field": ...,
	  "param": ...,
	  "as": ...
  }],
  "sort": [
	{"field": ..., "order": ...}
  ],
  "ignorePeers": ...,
  "groupby": [
	"..."
  ],
  "frame": [...,...]
```

(We will demonstrate this!)


---

## Aggregate Transforms

We have seen the `aggregate` transform before:

```json
{
  "transform": [
    {
      "type": "aggregate",
      "fields": ["state"],
      "ops": ["count"],
      "as": ["state_count"]
    }
  ]
}
```

This creates a new aggregated dataset, with `state` and `state_count`.

---

## Aggregate with Groupby

We can also groupby, and perform (for instance) the maximum value among all the states.

```json
{
  "transform": [
    {
      "type": "aggregate",
      "fields": ["cases"],
      "ops": ["max"],
      "groupby": ["state"],
      "as": ["max_cases"]
    }
  ]
}
```

Now, we get for each `state` the maximum number of cases.

The `joinaggregate` operation may also be useful in this situation.

---

## Filtering

- ranking
- parameters


---

## Marks

- `arc`
- `trail`
- `image`
- `geoshape`

---

## Arc Mark

The arc mark is typically used for displaying radial plots, such as pie or donut charts.

```json
{ 
  "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
  "data": {
    "values": [
      {"category": "A", "value": 1},
      {"category": "B", "value": 4},
      {"category": "C", "value": 12},
      {"category": "D", "value": 10},
      {"category": "E", "value": 1},
      {"category": "F", "value": 5}
    ]
  },
  "mark": "arc",
  "encoding": {
    "theta": {"field": "value", "type": "quantitative"},
    "color": {"field": "category", "type": "nominal"}
  }
}  "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
```

See also the `arc` configuration, which includes `radius` and `radius2`.

---

## Trail Mark

The `trail` mark can display lines with variable widths.

```json
{
  "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
  "data": {
    "sequence": {
      "start": 0,
      "stop": 15.0,
      "step": 0.05,
      "as": "x"
    }
  },
  "transform": [
    {"calculate": "cos(datum.x)", "as": "y"},
    {"calculate": "pow(sin(datum.x), 2) + 0.1", "as": "w"}
  ],
  "mark": "trail",
  "encoding": {
    "x": {"field": "x", "type": "quantitative"},
    "y": {"field": "y", "type": "quantitative"},
    "size": {"field": "w", "type": "quantitative"}
  }
}
```

---

## Image Mark

We'll do more with this one later, but you can use it to display an image at a particular location and from a particular URL.

From the vega-lite docs:

```json
{
  "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
  "data": {
    "values": [
      {"x": 0.5, "y": 0.5, "img": "data/ffox.png"},
      {"x": 1.5, "y": 1.5, "img": "data/gimp.png"},
      {"x": 2.5, "y": 2.5, "img": "data/7zip.png"}
    ]
  },
  "mark": {"type": "image", "width": 50, "height": 50},
  "encoding": {
    "x": {"field": "x", "type": "quantitative"},
    "y": {"field": "y", "type": "quantitative"},
    "url": {"field": "img", "type": "nominal"}
  }
}
```

---

## Geoshape Mark

For `geoshape` marks, we need to specify a `projection` as well as a dataset in **TopoJSON** format.  Converting between GeoJSON and TopoJSON can be tricky at times, but is tractable.

```json
{
  "data": {
    "url": "data/us-10m.json",
    "format": {
      "type": "topojson",
      "feature": "counties"
    }
  },
  "projection": {
    "type": "albersUsa"
  },
  "mark": "geoshape",
  ...
}
```

---

## Encoding Channels

- latitude / longitude
- color
- text / tooltip / href

---

## Altair

To our notebooks!
