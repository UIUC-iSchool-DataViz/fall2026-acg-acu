---
jupyter:
  jupytext:
    cell_metadata_filter: -all
    formats: ipynb,py:percent,md
    notebook_metadata_filter: layout,title
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.19.5
  kernelspec:
    display_name: Python 3 (ipykernel)
    language: python
    name: python3
  layout: notebook
  title: Uncertainty and Small Multiples
---

# Uncertainty and Small Multiples

Two things today, both of which come up in pretty much every real dataset:

1. **Uncertainty.** Your numbers are never exact. How do you show that?
2. **Small multiples.** You've got too many things to fit on one chart. Now what?

And for both of them, we'll check: can somebody who can't _see_ the chart
still get the point? (Spoiler: it depends a lot on how you make it.)

Building inventory, one more time.

```python
import altair as alt
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# We're going to hand Altair all ~7,000 raw rows so that *it* can compute
# the error bars. That's more than its default limit of 5,000.
alt.data_transformers.disable_max_rows()
```

```python
df = pd.read_csv("../data/building_inventory.csv")
df = df[df["Year Constructed"] > 0]

top_agencies = df["Agency Name"].value_counts().index[:6]
df = df[df["Agency Name"].isin(top_agencies)]
df["Agency"] = df["Agency Name"].str.replace("Department of ", "Dept. of ")
df["Decade"] = df["Year Constructed"] // 10 * 10
len(df)
```

## Part 1: Uncertainty

### The chart everybody makes

"Which agency has the biggest buildings?" Average square footage, as a bar
chart. Done!

...but is the difference between Corrections and Human Services _real_? Is
it big compared to how much buildings vary within an agency? We have no
idea from this chart.

```python
alt.Chart(df).mark_bar().encode(
    x=alt.X("mean(Square Footage):Q", title="Average square footage"),
    y=alt.Y("Agency:N", sort="-x", title=None),
)
```

### Adding error bars

Vega-lite will compute these for us. `extent="ci"` is a 95% confidence
interval on the mean, computed by bootstrapping.

Notice we switched from bars to points. Bars imply "everything from zero up
to here," which isn't really what a mean with an interval is saying.

```python
base = alt.Chart(df).encode(y=alt.Y("Agency:N", sort="-x", title=None))

means = base.mark_point(filled=True, size=60, color="black").encode(
    x=alt.X("mean(Square Footage):Q", title="Average square footage")
)
ci = base.mark_errorbar(extent="ci").encode(
    x=alt.X("Square Footage:Q", title="Average square footage")
)

(ci + means).properties(title="Average building size, with 95% confidence intervals")
```

### "Error bars" can mean four different things

This is the one that bites people. The exact same data, four different
kinds of "error bar". This time we'll compute them ourselves in pandas, so
we can see exactly what each one is.

(Why not let vega-lite do it, like above? Because if you put several
`mark_errorbar` charts on the same data into one `hconcat`/`vconcat`,
vega-lite currently mixes up their calculations and draws the wrong
intervals -- with no error! Another good reason to check your charts
against numbers you computed yourself.)

```python
stats = df.groupby("Agency")["Square Footage"].agg(
    mean="mean", sem="sem", sd="std", median="median",
    q1=lambda s: s.quantile(0.25), q3=lambda s: s.quantile(0.75),
).reset_index()

intervals = pd.concat([
    stats.assign(kind="95% confidence interval of the mean", center=stats["mean"],
                 lo=stats["mean"] - 1.96 * stats["sem"], hi=stats["mean"] + 1.96 * stats["sem"]),
    stats.assign(kind="Mean ± standard error", center=stats["mean"],
                 lo=stats["mean"] - stats["sem"], hi=stats["mean"] + stats["sem"]),
    stats.assign(kind="Mean ± standard deviation", center=stats["mean"],
                 lo=stats["mean"] - stats["sd"], hi=stats["mean"] + stats["sd"]),
    stats.assign(kind="Median and interquartile range", center=stats["median"],
                 lo=stats["q1"], hi=stats["q3"]),
])

interval_base = alt.Chart().encode(y=alt.Y("Agency:N", title=None))
rules = interval_base.mark_rule().encode(
    x=alt.X("lo:Q", title="Square footage"), x2="hi:Q"
)
centers = interval_base.mark_point(filled=True, color="black").encode(x="center:Q")

alt.layer(rules, centers, data=intervals).properties(width=250, height=150).facet(
    facet=alt.Facet("kind:N", title=None), columns=2
).resolve_scale(x="independent")
```

The confidence interval and standard error tell you about how sure we are
of the _average_. The standard deviation and IQR tell you about how spread
out the _buildings_ are. Those are really different questions!

Also: look at "mean ± standard deviation." It goes _negative_. There's no
such thing as a building with negative square feet! That's a sign that the
mean and standard deviation are the wrong summary for skewed data like this.

**Always say what your error bars are.** In the title, the subtitle, the
caption, somewhere.


### Sometimes, just show the distribution

Square footage is _really_ skewed -- a few enormous buildings and a whole
lot of sheds. (Natural Resources has a median of 240 square feet!) The mean
isn't a great summary here at all. When you can, show the whole
distribution, so people can see the uncertainty for themselves.

```python
alt.Chart(df).mark_boxplot(extent="min-max").encode(
    x=alt.X("Square Footage:Q", scale=alt.Scale(type="log"), title="Square footage (log scale)"),
    y=alt.Y("Agency:N", title=None),
).properties(title="Building sizes vary enormously within every agency")
```

### Can everybody read the uncertainty?

Let's try making these accessible with [maidr](https://py.maidr.ai/).
Click (or Tab) into a chart, and use the arrow keys; press **T** for text
and **S** for sound.

First, a bar chart with error bars, via seaborn.

```python
import maidr

fig, ax = plt.subplots(figsize=(7, 4))
sns.barplot(data=df, x="Square Footage", y="Agency", errorbar=("ci", 95), ax=ax)
ax.set_title("Average building size, with 95% confidence intervals")
maidr.show(fig)
```

Arrow through that. You'll hear the _bars_... and nothing about the error
bars. The uncertainty is just _gone_ for a screen reader user, and nothing
tells them it's missing.

Now, the same information as a point plot:

```python
fig, ax = plt.subplots(figsize=(7, 4))
sns.pointplot(
    data=df, x="Square Footage", y="Agency", errorbar=("ci", 95), linestyle="none", ax=ax
)
ax.set_title("Average building size, with 95% confidence intervals")
maidr.show(fig)
```

This one maidr reads as an _error bar_ chart, and you can hear the
interval for each agency.

The lesson isn't "never use bar charts." It's: **check**. Tools will
quietly drop things. And when the uncertainty matters, put it in words
too -- "between X and Y square feet" -- not just in the picture.


## Part 2: Small Multiples

### The spaghetti chart

When did each agency build its buildings? One line per agency:

```python
by_decade = df.groupby(["Agency", "Decade"]).size().reset_index(name="Buildings")

alt.Chart(by_decade).mark_line(point=True).encode(
    x=alt.X("Decade:O"),
    y="Buildings:Q",
    color="Agency:N",
).properties(width=500)
```

Six colors, lots of crossing lines, and you have to keep going back to the
legend. (And six colors is already pushing it for anybody with a color
vision deficiency.)

### Small multiples

Instead: one little chart per agency, all on the same scale, all in the
same place. Your eye can compare _shapes_ without decoding any colors.

```python
alt.Chart(by_decade).mark_line(point=True).encode(
    x=alt.X("Decade:O", axis=alt.Axis(labelAngle=-90)),
    y="Buildings:Q",
).properties(width=180, height=100).facet(
    facet=alt.Facet("Agency:N", title=None), columns=3
)
```

### Shared or independent scales?

With a shared y-axis, you can compare _across_ panels (Natural Resources
built a lot more buildings than the University of Illinois). With
independent axes, you can see the _shape_ of each one (when did the U of I
build?) but comparisons across panels become misleading.

Neither is wrong! But it's a choice, and you should make it on purpose.

```python
alt.Chart(by_decade).mark_line(point=True).encode(
    x=alt.X("Decade:O", axis=alt.Axis(labelAngle=-90)),
    y="Buildings:Q",
).properties(width=180, height=100).facet(
    facet=alt.Facet("Agency:N", title=None), columns=3
).resolve_scale(y="independent")
```

<!-- #region -->
### Small multiples and accessibility

If we hand that faceted Altair chart to maidr, it refuses:

```python
maidr.show(faceted_chart)
# TypeError: maidr cannot find a figure for alt.FacetChart(...)
```

But if we build the same small multiples with matplotlib subplots, maidr
reads each panel as its own line plot. Press **Ctrl + /** (Command + / on a
Mac) inside the chart to see how to move between panels.
<!-- #endregion -->

```python
fig, axes = plt.subplots(2, 3, figsize=(10, 5), sharex=True, sharey=True)
for ax, (agency, group) in zip(axes.flat, by_decade.groupby("Agency")):
    ax.plot(group["Decade"], group["Buildings"], marker="o")
    ax.set_title(agency, fontsize=9)
fig.supxlabel("Decade constructed")
fig.supylabel("Buildings")
fig.suptitle("When each agency built its buildings")
fig.tight_layout()
maidr.show(fig)
```

## Your turn

Take a chart from your Part One exploration:

1. What's uncertain about it? Add an error bar or show the distribution --
   and say what the error bars mean.
2. Is there a variable you could split it into small multiples by?
3. Run it through `maidr.show()`. What survives? What gets lost?
