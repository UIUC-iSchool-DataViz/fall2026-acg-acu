---
title: Storytelling, SciViz, Streamlit and D3
layout: lecture
tags:
  - storytelling
  - annotation
  - scientific
  - streamlit
  - d3
  - javascript
description: >-
  Making viz that says something, what makes scientific data "different," building and deploying Streamlit apps, and an introduction to D3.
date: 2026-11-09
---

# Storytelling, SciViz, Streamlit, and D3

---

# Final Project

Your final project, to be completed in (assigned) groups, is to build a semi-realtime "observatory" of data. You can find a few different possibilities for the data, but I want to encourage you to think of data related to things like:

- Earthquakes
- Space weather, rocks and satellites
- Weather
- Political events and news
- Nothing directly COVID related

---

# Final Project: Phases

Your final project will have three phases, each of which will have a component for you to turn in. The second and third components will be turned in as a group, but the first component will be individually graded.

**Before beginning, clear your dataset with me and Yilin.**

Some places to look for dataset ideas:

- [Awesome Public Datasets](https://github.com/awesomedata/awesome-public-datasets)
- [Public APIs](https://github.com/public-apis/public-apis)
- [Awesome JSON](https://github.com/jdorfman/awesome-json-datasets)

---

# Final Project: Part One

The first part of your project will be to _explore_ the data; this is worth **30 points out of 100**. You are to turn in a Jupyter notebook that includes every single cell and step you took in exploring the data. This is an example of the "visualization for self" process. This means you might take shortcuts, you might make mistakes, and you might make really, really awful visualizations.

Showing that you explored the data individually (even if you did it while talking to a collaborator or classmate) is enough to satisfy this portion of the project.

Download the data. Dig in to it. Look at it. Find interesting things. Experiment. Make plots, make summary statistics, and make it familiar to yourself.

---

# Final Project: Part Two

The second component of your project will be to design your "observatory." Note that this is _pseudo_ realtime. It does not need to _automatically_ update its data; a refresh button, or requiring a page reload, is sufficient. This is worth **40 points out of 100**.

This could consist of drawings, prototypes of web pages or notebooks, and the code necessary to build the different components. This component is _scaffolding_, not the final product. It should be thought of as the "viz for peers" stage of the process. You can submit drawings (including photos of drawings), jamboards, notebooks (which you _are_ allowed to clean up), and stages of prototypes.

You should walk me through the process of how you built your observatory, and it does not need to be a linear, successes-only process.

This will include your in-class presentation of the work. You will also have five minutes, as a _group_, to present your work in class. This presentation needs to include the final product, as well as a summary of any stumbling blocks you might have had, and a little bit of the process. These presentations will be on the 7th of December, the final class date.

---

# Final Project: Part Three

The final component of your project will be a deployment of your work online. This will be worth **30 points out of 100**.

This should be a Streamlit app deployed on [Streamlit Community Cloud](https://streamlit.io/cloud), which we will demonstrate later today. (It's free, and it deploys right from a GitHub repo.) It should be fully-executable and need to include a mechanism for "checking for new data."

---

# Final Project Summary

| Points | Description                                                          | Requires Code |
| ------ | -------------------------------------------------------------------- | ------------- |
| 30     | Your own exploration of a dataset.                                   | Yes           |
| 40     | You and your group designing, then presenting your design, to class. | No            |
| 30     | A final deployment of your project on Streamlit Community Cloud.     | Yes           |

- You will use _your own datasets_ for part 1. This is **on your own**.
- Your group will choose from those datasets for parts 2 and 3.
- Part 3 will be a Streamlit app, deployed on Streamlit Community Cloud.

---

## Classes of Visualization

1. Viz for Self
1. Viz for Colleagues
1. Viz for Others

---

## Viz for Self

We can think of this as telling a story to yourself.

You can take shortcuts -- you can skip labels, colors, and so on, _sort of_. You just have to make sure you're not lying to yourself.

![Why would we lie to ourselves?](images/why_lie.gif)

---

## Viz for Self

How do we explore data?

- What characteristic of data influence how you visualize it?
- What information do you have that would be visually interesting?
- What information do you _not_ have that you need in order to understand the importance of the data?

<div class="r-stack">
<p class="fragment fade-in-then-out">Example: A banking database where each record is a bank transaction and the fields include date, deposit or withdrawal amount, customer id, and the interest rate of the account.</p>
<p class="fragment fade-in-then-out">Example: A spreadsheet of experimental crop growth measurements where each record is a measurement, and the fields include date, plant species, plant id number, number of leaves, plant height, number of internodes, and average leaf length.</p>
<p class="fragment fade-in-then-out">Example: A computational simulation of a galaxy where each record is a timestep in the evolution of the 3D grid, and the fields include time, X position, Y position, Z position, gas density, gas temperature, gas metallicity, and number of stars.</p>
</div>

---

## Viz for Self

What do you want to get out of visualization for yourself?

- Do you want to find meaning?
- Do you want to understand how to guide further visualizations?
- Is the story you want to tell already known to you?
- What **shortcuts** can you take?

---

## Viz for Experts

To design a visualization for experts, you need to analyze how they process information.

- What do they know?
- What conventions will they assume?
- Are they able to fill in the blanks of information?

---

## Viz for Experts

<iframe width="1024" height="576"
src="https://www.youtube.com/embed/FG1NNH7Kmok?rel=0" frameborder="0"
allow="encrypted-media" allowfullscreen></iframe>

notes:
This is from Chris Havlin, and it's vorticity of a tornado

---

## Viz for Experts

![](images/sci_canup.png)

notes:
Here's a series of visualizations made by or for domain experts that I just had lying around on my laptop.

What are some things you notice they have in common?

---

## Viz for Experts

![](images/sci_flu.png)

notes:
Here's a series of visualizations made by or for domain experts that I just had lying around on my laptop.

What are some things you notice they have in common?

---

## Viz for Experts

![](images/sci_genes.png)

notes:
Here's a series of visualizations made by or for domain experts that I just had lying around on my laptop.

What are some things you notice they have in common?

---

## Viz for Experts

Experts often want to interrogate the data themselves.

How can they do that?

- Linked Dashboards
- Side-by-side comparison plots
- Text annotation with specific values listed
- Color bar annotation

notes:
ask students - other ideas? what about interactivity? (Interactivity needs to be decent)

---

## Viz for Experts

Experts are looking to isolate variables to make scientific conclusions.

How can we make visualizations more analytical?

- Reduce the dimensionality of the image (slices)
- Viewpoint from "outside the box"
- Extremely high contrast color choices (or highlight different features)

notes:
ask students - other ideas? What about animated data?

---

## Viz for the Public

This is what you're most accustomed to, because usually YOU are the public.

Communicating information to the public is an entire field, and I encourage you to take IS457 - Data Storytelling for a more comprehensive discussion.

---

## Storytelling and Annotation

So what makes a viz for the public _work_? A lot of it comes down to one thing:

**Tell people what you want them to see.**

You've spent hours with your data. Your reader has spent about eight seconds. They don't know what's interesting yet -- that's your job.

(This is also the FDV chapter on [telling a story](https://clauswilke.com/dataviz/telling-a-story.html) from last week's reading.)

---

## Title as a Sentence

The single most effective thing you can do:

- "Square footage by decade" tells me what the axes are.
- "Illinois built more in the 1960s than in any other decade" tells me what to look for.

Put the takeaway in the title. Put the description of the axes in the subtitle.

```python
title = alt.Title(
    "Illinois built more in the 1960s than in any other decade",
    subtitle="Total square footage of state-owned buildings, by decade",
    anchor="start",
)
alt.Chart(df, title=title).mark_bar()...
```

---

## Highlight, Then Gray Out

Use color to _point_ at something, not just to decorate.

```python
color = alt.condition(alt.datum.Decade == 1960,
                      alt.value("#c0392b"), alt.value("#b0b0b0"))
```

Everything that isn't the story goes gray.

And: don't make color the _only_ way to find the thing. Here, it's also the tallest bar, and it's also got a label on it. (About 1 in 12 men has some form of color vision deficiency. Remember week 3!)

---

## Annotate Directly

Put the words right next to the thing they're about. No legends to decode, no "see figure caption."

In Altair, annotations are just another layer:

```python
notes = pd.DataFrame([
    {"Decade": 1960, "million_sqft": 21.4,
     "note": "21 million sq. ft. -- about double the 1950s"},
])
annotations = alt.Chart(notes).mark_text(align="left", dx=22).encode(
    x="Decade:O", y="million_sqft:Q", text="note:N")

bars + annotations
```

---

## Be Honest About the Caveats

![](images/storytelling_final.png)

That 2010s bar looks like a collapse! But the data stops in 2019. So we fade it out _and_ label it.

Annotations aren't just for the exciting part -- they're also for the part that might mislead.

note:
also -- always have a source line.  st.caption in streamlit, or just text underneath.

---

## Structure: Martini Glass

A lot of good public-facing viz follows the "martini glass" shape:

1. **The stem:** you lead. Here is the thing, here is why it matters, here is what to notice.
2. **The bowl:** then you let go. Here are the controls, go explore.

Your final project is a great place for this! Start with a few annotated, opinionated charts, _then_ hand them the interactive dashboard.

---

## Example: Storytelling and Annotation

`storytelling_annotation.ipynb` walks through all of this, step by step, starting with the "viz for self" version and ending with something you'd publish.

It also ends with a sneak preview of something we'll spend a lot more time on in a couple of weeks: making sure the chart works for people who can't _see_ it.

---

## Scientific Visualization

What characterizes "scientific" visualization?

- Spatial organization - distance metrics
- Dimensionality reduction or mapping
- Multiple overlapping quantities with implicit or explicit extent

---

## Scientific Visualization - Data Representations

<div class="multiCol">
<div class="col">
<div class="fig-container" data-style="height: 600px;" data-file="figures/blank_axes.html" data-markdown=true>
</div>
</div>
<div class="col" data-markdown=true>

Commonly, data will be represented in "scientific visualization" through one of a few mechanisms:

- Discrete points
- Volume-filling information
- Meshed values

</div>
</div>

---

## Discrete Points: Data

<div class="multiCol">
<div class="col">
<div class="fig-container" data-style="height: 600px;" data-file="figures/scatter.html" data-markdown=true>
</div>
</div>
<div class="col" data-markdown=true>

- Associated field values
- May have extent
- Values can be either
  - Locally defined
  - Integrated over neighbors

</div>
</div>

---

## Discrete Points: Density Estimates

- Searching
  - Quadtree
  - kD-tree
- Integration
  - Kernels
  - Nearest-neighbor

---

## Discrete Points: Techniques

<div class="multiCol">
<div class="col">
<div class="fig-container" data-style="height: 600px;" data-file="figures/discrete_tech.html" data-markdown=true>
</div>
</div>
<div class="col" data-markdown=true>

- Associated field values
- May have extent
- Values can be either
  - Locally defined
  - Integrated over neighbors

</div>
</div>

---

## Volume data: strategies

To analyze volume data, typically we conduct one or more of these operations:

- Select data based on spatial or non-spatial criteria
- Reduce the dimensionality of that data either along spatial or other axes
- Aggregate data

This can include operations such as volume rendering, axial projection, histogramming/binning and resampling.

---

## Big-ish Data

How do we deal with data that is too large to fit into memory?

- Can we cycle our operations?
- Can we use tools to cycle operations?

---

## Operations

Some operations we can manually cycle through, storing only reductions in memory rather than the full dataset.

Clear candidates:

- Mean
- Extrema
- Histograms and "binning"

Is this the same as incremental updates to a dataset?

(What about the median?)

---

## Streamlit, Continued

Last week we got a quick taste of [Streamlit](https://streamlit.io/). Today we're going to dig in a little more, because this is what you'll be building Part Three of your final project in.

We'll go through three examples, and then we'll deploy one.

All of the examples live in the `week12/streamlit/` directory of the course repo.

---

## Running the Examples

If you've got the course repo checked out:

```bash
uv sync --extra notebooks
uv run streamlit run week12/streamlit/01_hello_streamlit.py
```

Otherwise, `pip install streamlit altair pandas requests` and then:

```bash
streamlit run 01_hello_streamlit.py
```

This will pop open a browser tab. Leave it open! When you save changes to the file, Streamlit will notice and offer to re-run it.

---

## The Streamlit Mental Model

This is the one thing to really internalize:

**Every time somebody touches a widget, Streamlit re-runs your _entire script_, top to bottom.**

```python
import streamlit as st

n = st.slider("How many?", 1, 100, 10)
st.write(f"You picked {n}")
```

`st.slider` just returns a number. No callbacks, no `.observe()`, no linking traitlets together.

note:
compare this with what we did with bqplot -- there we built the figure once and then wired up observers to change it.  Here we just rebuild everything, every time.  This is wasteful!  But it's also *really* easy to reason about.

---

## Example 1: Hello, Streamlit

`01_hello_streamlit.py`

- `st.write`, the "do what I mean" function
- sliders, checkboxes and buttons
- the quick built-in charts (`st.line_chart`, `st.bar_chart`)
- `st.sidebar` and `st.columns` for layout
- `st.session_state` for things that need to survive a re-run

note:
the button counter is the one to really look at -- if you use a regular variable it resets every time the script re-runs.  session_state is where things go that you want to keep around.

---

## Caching

Since the whole script re-runs every time, we really don't want to re-load our data every time.

```python
@st.cache_data
def load_data():
    return pd.read_csv("building_inventory.csv")
```

The first time, it actually runs. Every time after that, Streamlit hands you back the same result.

You can also give it a `ttl` -- "time to live" -- so that it expires:

```python
@st.cache_data(ttl=300)  # 5 minutes
def load_quakes():
    ...
```

---

## Example 2: Building Inventory (Again!)

`02_building_inventory.py`

Our old friend. This is basically the bqplot dashboard we built, but in Streamlit:

- controls in the sidebar
- an Altair (vega-lite!) scatter plot with an interval selection
- a bar chart and a table that react to that selection

---

## Linking and Brushing in Streamlit

Altair charts are vega-lite under the hood, so we can add selections like we did before. The new part is getting the selection _back into Python_:

```python
brush = alt.selection_interval(name="brush", encodings=["x"])
chart = alt.Chart(df).mark_circle().encode(...).add_params(brush)

event = st.altair_chart(chart, on_select="rerun")
event.selection["brush"]  # {'Year Constructed': [1950.2, 1971.8]}
```

`on_select="rerun"` means: when the selection changes, re-run the script and tell me what got selected.

note:
this is the same interval selection we wrote by hand in the vega-lite JSON a few weeks ago.  Now we just get to use it from Python.

---

## Example 3: An Earthquake Observatory

`03_earthquake_observatory.py`

This one is a tiny version of what your final project is asking for! It pulls the [USGS earthquake feed](https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php), which updates every minute or so.

- GeoJSON into a dataframe (we've seen this before)
- `st.map` for a quick-and-dirty map
- a histogram and a scatter in Altair
- **checking for new data**

---

## Checking for New Data

Two ways to do it. A button that clears the cache:

```python
if st.button("Check for new data"):
    load_quakes.clear()
```

Or, a _fragment_ that re-runs itself on a timer:

```python
@st.fragment(run_every="60s")
def observatory():
    ...
```

A fragment re-runs _just that function_, not the whole script. This is the Streamlit version of what we did last week with vega-lite changesets.

Either one satisfies the "checking for new data" requirement. A button is totally fine!

---

## Deploying: Streamlit Community Cloud

[Streamlit Community Cloud](https://streamlit.io/cloud) is free, and it deploys right out of a GitHub repo.

1. Put your app in a **public** GitHub repo.
2. Add a `requirements.txt` listing every package you import (see `week12/streamlit/requirements.txt`).
3. Go to [share.streamlit.io](https://share.streamlit.io) and sign in with GitHub.
4. "Create app," then pick your repo, branch and the path to your `.py` file.
5. You get a `something.streamlit.app` URL. That's what you submit!

Every time you push to that branch, it'll redeploy.

note:
the #1 thing that goes wrong here is a missing package in requirements.txt.  If it works on your machine and not on the cloud, check that first.

---

## Deploying: Some Gotchas

- **requirements.txt.** If you `import` it, it needs to be in there.
- **Data files.** Paths are relative to the root of your repo, not to wherever you happened to run it. Keep data files small (remember GitHub's size limits!) or load them from a URL.
- **Secrets.** Do _not_ commit API keys. Use `st.secrets` and the "Secrets" setting in the app dashboard.
- **Sleeping.** Apps that nobody visits for a while go to sleep, and take a little bit to wake back up. Load yours up before you present it!

---

## Try It

Take the dataset you're using for Part One, and:

1. Make a Streamlit app that loads it (with caching!)
2. Add at least one widget that changes what's shown
3. If you're feeling ambitious, deploy it

This doesn't have to be pretty. This is viz for self!

---

## A Little Bit of D3

We're going to learn a very small bit of [d3.js](https://d3js.org/).

We will utilize D3 on [starboard.gg](https://starboard.gg). We do this by including it from a CDN, as we did for vega last time:

<code>
&lt;script src="https://d3js.org/d3.v7.min.js"&gt;&lt;/script&gt;
</code>

---

## Concepts in d3: outline

The basic concepts here we will convey, focusing on _static_ visualizations:

- `.select()` and `.selectAll()`
- `.enter()`
- `.attr()` and `.style()`
- `d3.scaleLinear()`

---

## Concepts in d3: data and elements

When we manipulate items in d3, we connect the concept of a data item to an element in a document.

Typically, this will be an element in an SVG -- for instance, a `line`,
`circle`, `rect` or `text` element.

Our typical workflow:

1. Select all items of a specific criteria
1. Bind these items to a set of data
1. Update, append or remove items based on their corresponding item.

---

## Concepts in d3: accessors and setters

We will very frequently run into the case where we call something, and supply a _function_ to it, rather than supplying a value. For instance, _both_ of these calls to `attr` are valid in a typical d3 workflow:

```javascript
.attr("cx", 1.0)

// or

.attr("cx", d => d.x)
```

In one, we are setting the value static; in the other, we base the value on the datapoint supplied.

---

## Concepts in d3: Let's make circles

For our first exploration, let's just make some circles. I will demonstrate this in Starboard, but here is the key snippet of code:

```
var dataset = [ {'x': 100, 'y': 200, 'radius': 15},
                {'x': 150, 'y': 300, 'radius': 30} ];
svg.selectAll("circle").data(dataset).enter()
   .append("circle")
   .attr("cx", d => d.x)
   .attr("cy", d => d.y)
   .attr("r", d => d.radius)
   .style("fill", "black");
```

What does this do?

---

## Concepts in d3: Objects

We will mostly use the objects

- [`rect`](https://developer.mozilla.org/en-US/docs/Web/SVG/Element/rect) -- which has `x`, `y`, `width` and `height`
- [`circle`](https://developer.mozilla.org/en-US/docs/Web/SVG/Element/circle) -- which has `cx`, `cy`, and `r`
- [`line`](https://developer.mozilla.org/en-US/docs/Web/SVG/Element/line) -- which has `x1`, `x2`, `y1` and `y2`.

Each of these objects can be controlled in style, appearance, position, etc, according to standard SVG and CSS rules.

Let's experiment!

---

## Concepts in d3: Scaling

To map from a given range to a different range in a linear fashion, we can construct a linear scale:

```javascript
var xScale = d3.scaleLinear().range([0, 100]).domain([0.0, 1.0]);
```

This is now an object we can use to map the values 0 .. 1 to 0 .. 100. This is useful for, among other things, computing the position of a given value:

```javascript
.attr("cx", d => xScale(d.x))
```

---

## More D3 Next Week

That's the core of it: select, bind, set attributes, scale.

Next week we'll pick back up with events, transitions, brushing and paths.

---

## Group Time

The rest of today is yours.

- Find your group, if you haven't yet (sign-up deadline is on Canvas!)
- Talk through your Part One datasets -- which one(s) will you use for Parts Two and Three?
- **Come clear your dataset with me or Yilin before you leave.**
