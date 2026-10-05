---
title: Viz Platforms and more Vega-lite
layout: lecture
tags:
  - platforms
  - vega-lite
  - web
  - javascript
description: >-
  We start with a mechanism for comparing visualization engines.  Then, we go over more details of using vega-lite and how to embed vega-lite visualizations in a web page.
---


## Evaluating Visualization Engines

- Costs
- Functionality
- Aesthetics

---

## Choices

- Can I get ahold of this software?
- Do I install it, or do I use it on a server?
- What's the user interface like?
- Is it declarative or is it procedural?

---

## License: Software

- What can you do with the software?
- Can you study the software?
- Who can you share it with?
- Who can you give your derivative works to?

---

## License: Software

- Copyleft: share and share-alike
- Non-copyleft: share, but don't necessarily need to share-alike
- https://choosealicense.com/

---

## License: Data

- What can you do with the data?
- How do you credit that data?
- Can the data be redistributed, remixed, modified?
- http://opendefinition.org/guide/data/
- https://theodi.org/guides/publishers-guide-open-data-licensing

---

## Accessibility

- Is the software installed locally on your machine?
- Is it hosted at a local or remote instance?
- Who owns the visualizations, and how is access to them controlled?

---

## Interface

How do you interact with the software?

- Declarative: how do you want the plot to look?
- Procedural: what are the steps to make the plot look that way?

---

## Example Declarative

```python
Chart(df).mark_bar().encode(
    X('precipitation', bin=True),
    Y('count(*):Q')
)
```

(From [Altair Docs](https://altair-viz.github.io/tutorials/exploring-weather.html))

<!-- .slide: data-background-image="images/altair_example01.png" data-background-size="30% auto" data-background-position="right 20% bottom 20%" -->

notes:

The background image is a bar chart titled "Number of Records" vs
"BIN(precipitation)".  Precipitation values are binned in increments of 5, and
the bar heights fall off sharply after the first bin -- the vast majority of
records have precipitation near zero, with only a handful of taller
precipitation events.

---

## Evaluation: Costs

The "cost" of software is not exclusively the number of dollars you place on the counter when you get a big cardboard box with marketing blurbs on the side.

Think about cost in several ways:

- Monetary cost for *you* to use the software
- Monetary cost for *someone else* to view your creations
- Temporal cost of setting up
- Cognitive cost for learning and using the system (documentation matters!)
- Transmission cost for sharing your creations

---

## Evaluation: Aesthetics

Visualization is trendy.

When you construct something, think about the different ways it will be interpreted:

- How will the viewer understand the story of the data?
- What will the _message_ of the visualization be?
- Does the visualization say something about you and your handling of the data or utilization of tools?


---

## More vega-lite

Today we will fill out more components of our understanding of vega-lite.  Last
week we discussed marks and encodings.  This week we will continue with marks,
adding on transformations and selections.

Recall that vega-lite is defined in a JSON specification.  This specification will typically take a form similar to this:

```json
{
  "data": .. ,
  "transform": [ .. ],
  "mark": .. ,
  "params": .. ,
  "encoding": .. ,
  "config": ..
}
```


---

## vega-lite marks

vega-lite has numerous different `mark` types.  We can break these down by the type of data they can represent.  We will only consider "primitive" marks today.

- `area` & `line`
- `bar` & `rect`
- `point` & `circle` & `square`
- `arc` (pie/donut charts)
- `rule` & `text`
- `tick`
- `geoshape`

We will demonstrate several of these using our datasets, but first we need to learn how to transform data.


---

## vega-lite transformations

At the `view`-level of your definition, you can specify transformations that modify, filter, aggregate, or reshape the data.

At the top level, we specify a transformation as a *list* -- transforms are applied in order, and each one can build on the fields created by the ones before it.

The types of transformations we will cover today are `filter`, `calculate`, `bin`, `aggregate`, `window`, and `fold`.


---

## vega-lite filtering

We apply a `filter` transform by specifying the field to filter on and the filtering characteristic.  This can be a selection, an expression, or a logical definition.  We will address selection and expression filtering later.


---


## vega-lite filtering

A logical filtering operation might look like one of these:

```json
"transform": [
  {"filter": {
      "field": "eye_color", "oneOf": ["blue", "brown"]
      }
  },
  {"filter": {"field": "age", "lte": 100 }
  }
]
```

We can use `lt`, `gt`, `lte`, `gte`, `eq`, `oneOf`, `range` and `valid`.


---

## vega-lite calculate

We can also compute a new field using the `calculate` transform.  This is an expression that is evaluated on every data point, which is supplied as the variable `datum` to the expression.

```json
"transform": [
  {"calculate": "datum.age / 7", "as": "dog_years"}
]
```

---

## vega-lite binning

`bin` is usually something you ask for right on an encoding channel (`"bin": true`), but you can also run it as its own transform step to produce a reusable field -- handy when you want the binned field in a tooltip, or in more than one encoding.

```json
"transform": [
  {"bin": true, "field": "IMDB Rating", "as": "rating_bin"}
]
```

---

## vega-lite aggregate

`aggregate` collapses rows into summary statistics, optionally grouped by one or more fields. This is the same aggregation you can do inline on an encoding (`"aggregate": "sum"`), but as a transform it runs once and the result is available to every encoding and every downstream transform.

```json
"transform": [
  {
    "aggregate": [
      {"op": "sum", "field": "Square Footage", "as": "total_by_agency"}
    ],
    "groupby": ["Agency Name"]
  }
]
```

---

## vega-lite window

`window` computes a value across a *sliding or cumulative* set of rows -- running totals, ranks, lags -- rather than collapsing them like `aggregate` does. You still get one output row per input row, just with a new field attached.

```json
"transform": [
  {
    "window": [
      {"op": "rank", "field": "total_by_agency", "as": "agency_rank"}
    ],
    "sort": [{"field": "total_by_agency", "order": "descending"}]
  }
]
```

This is how we build "top-N" charts: compute a rank with `window`, then `filter` on `datum.agency_rank <= n`.

---

## vega-lite reshaping: fold

So far every transform has added a *column*. `fold` instead reshapes wide data into long (tidy) data -- it takes several fields and stacks them into `key`/`value` pairs, which is often what an encoding needs.

```json
"transform": [
  {"fold": ["Square Footage", "Rentable Square Footage"], "as": ["metric", "amount"]}
]
```

Its counterpart, `pivot`, does the reverse -- turning the distinct values of one field into new columns.

---

## vega-lite params

Modern vega-lite unifies interactivity under a single top-level `params` list.  Every param has a *name* -- this seems to be the most common stumbling block.  You get to choose the name!

A param is one of two things:

- A **selection** param -- it records what the viewer clicked, hovered, or dragged.
- A **variable** param -- it just holds a value, which you can bind to a widget or use in an expression.

We use params in one of a few ways.

- We can conditionally encode data -- for instance, change visibility, alpha, or color.
- We can use a selection as input for filtering data.  Typically this is done with one plot showing unfiltered data and another using a filter from that selection.
- We can scale a domain, or pan/zoom it, based on a selection.
- We can bind a variable param to an input widget and reference it in a `calculate` or `filter` expression.

---

## vega-lite selection types

There are two types of selection, specified with `select`:

- `point` -- selecting discrete marks (a single click, or shift-click for several). This replaces the old `single`/`multi` selection types from vega-lite 4.
- `interval` -- a drag-to-brush selection over a continuous range of values along one or more encodings.

We will focus on the `interval` selection, but will also see `point` in the examples.

---

## vega-lite interval selection

We can define a box-based selector that operates along the x axis by specifying which encoding it is linked to.  Here, we name it `valrange`, but we can choose whatever name we like.

```json
"params": [{
    "name": "valrange",
    "select": {"type": "interval", "encodings": ["x"]}
    }]
```

Let's try this.

---

## vega-lite point selection

A `point` selection lets the viewer click individual marks (bars, points, etc) rather than drag a region.  It is what you want for "click a bar to highlight it" interactions.

```json
"params": [{
    "name": "picked",
    "select": "point"
    }]
```

Both selection types are used the same way downstream: as a `{"param": "name"}` reference inside a `filter` transform or a `condition` encoding.

---

## vega-lite nearest-point selection

Adding `"nearest": true` to a `point` selection snaps it to the closest datum along the hovered axis, even if the cursor isn't exactly on a mark -- this is the standard recipe for crosshair/tooltip interactions on a line chart.

```json
"params": [{
    "name": "hover",
    "select": {
      "type": "point",
      "fields": ["Year Acquired"],
      "nearest": true,
      "on": "pointerover",
      "clear": "pointerout"
    }
    }]
```

Pair it with a transparent, large `point` mark to give the mouse something easy to target, then `filter` the other layers (a highlighted point, a `rule`, a `text` label) on `{"param": "hover", "empty": false}` so they only appear once something is hovered.

---

## vega-lite parameter types: widget-bound variables

A variable param doesn't select anything from the chart -- it just holds a value, given a starting `value` and optionally `bind` to a UI widget vega-embed generates for you.

```json
"params": [{
    "name": "rank_wanted",
    "value": 5,
    "bind": {"input": "range", "min": 0, "max": 10, "step": 1, "name": "Rank Wanted"}
    }]
```

Besides `"range"`, `bind.input` can be `"checkbox"`, `"radio"`, `"select"`, or any HTML input type. The current value is available anywhere as `rank_wanted`, e.g. in `{"filter": "datum.agency_rank <= rank_wanted"}`.

---

## vega-lite parameter types: binding to scales

An `interval` selection can also be bound directly to the chart's scales instead of (or in addition to) an encoding, which turns it into pan-and-zoom:

```json
"params": [{
    "name": "panzoom",
    "select": "interval",
    "bind": "scales"
    }]
```

No `filter` transform needed here -- binding to `"scales"` updates the axis domains directly as the viewer drags and scrolls.

---

## Using vega-lite with your own data

We will utilize Jupyterlab to visualize data using vega-lite, including our Building Inventory, after we prepare it.

We will edit files ending in `.vg`, and they can access files we prepare in notebooks.


---

## Embedding vega-lite

You must include the correct javascript includes to embed vega-lite in the `<head>` section of your HTML.  For instance:

```html
 <script src="https://cdn.jsdelivr.net/npm/vega@6.4.0/build/vega.min.js"
        integrity="sha256-j2o1h8+NT0LH4IEg4+sF0GfnRtVU450tz1KswL1boo8=" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/vega-lite@6.4.3/build/vega-lite.min.js"
        integrity="sha256-NamCHfg4glsFpqc+lBS1h0ehsYMhWDhY7ZA8Zjk6XH4=" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/vega-embed@7.3.0/build/vega-embed.min.js"
        integrity="sha256-sUVcq6L7GnL7RgJboLoTFuLbx/DdQKP2BAFyv5wIupE=" crossorigin="anonymous"></script>
```

---

## Embedding vega-lite

Embedding vega-lite requires identification of a DOM element within which to place your visualization as well as providing the specification of that visualization.  For example, we can define a `<div>` like so:

```html
<div id="viz">
</div>
```

And then we can utilize the `vegaEmbed` function like so:

```javascript
vegaEmbed('#viz', vlSpec);
```

---

## Datasets

This week we will use a dataset from [FiveThirtyEight](https://fivethirtyeight.com/), specifically from their [datasets repository](https://github.com/fivethirtyeight/data/).

Please take care to abide by their licensing terms (CC-BY 4.0).

Candidate datasets:

- [librarians](https://github.com/fivethirtyeight/data/tree/master/librarians) (2014)
- [bachelorette](https://github.com/fivethirtyeight/data/tree/master/bachelorette)
- [comic-characters](https://github.com/fivethirtyeight/data/tree/master/comic-characters)
- [bob-ross](https://github.com/fivethirtyeight/data/tree/master/bob-ross)
