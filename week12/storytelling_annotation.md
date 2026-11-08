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
  title: Storytelling and Annotation
---

# Storytelling and Annotation

We're going to take one chart and make it _say something_. We'll start with
the chart we'd make for ourselves -- viz for self! -- and then, step by step,
turn it into something we'd show to the public.

Our old friend, the Illinois building inventory.

```python
import altair as alt
import pandas as pd
```

```python
df = pd.read_csv("../data/building_inventory.csv")
df = df[df["Year Constructed"] > 0]
df["Decade"] = df["Year Constructed"] // 10 * 10

by_decade = (
    df[df["Decade"] >= 1880]
    .groupby("Decade")["Square Footage"]
    .sum()
    .reset_index()
)
by_decade["million_sqft"] = by_decade["Square Footage"] / 1e6
by_decade
```

## Step 0: The chart we make for ourselves

This is fine! It's a perfectly reasonable chart. But what is it _saying_?
What do you want somebody to walk away with?

```python
alt.Chart(by_decade).mark_bar().encode(
    x="Decade:O",
    y="million_sqft:Q",
)
```

## Step 1: Say the takeaway in the title

The single most effective thing you can do: make the title a _sentence_
that says what you want people to notice. "Square footage by decade" tells
me what the axes are. "Illinois built more in the 1960s than in any other
decade" tells me what to look for.

```python
title = alt.Title(
    "Illinois built more in the 1960s than in any other decade",
    subtitle="Total square footage of state-owned buildings, by decade of construction",
    anchor="start",
)

alt.Chart(by_decade, title=title).mark_bar().encode(
    x=alt.X("Decade:O", title=None),
    y=alt.Y("million_sqft:Q", title="Million square feet"),
)
```

## Step 2: Highlight the thing you're talking about

Now we use color to _point_. Everything else goes gray. Note that this is
using color for emphasis, not to encode a variable -- and the bar is also
the tallest one, so nobody has to rely on color alone to find it.

```python
highlight = alt.condition(
    alt.datum.Decade == 1960, alt.value("#c0392b"), alt.value("#b0b0b0")
)

bars = (
    alt.Chart(by_decade, title=title)
    .mark_bar()
    .encode(
        x=alt.X("Decade:O", title=None, axis=alt.Axis(labelAngle=0, labelExpr="datum.value + 's'")),
        y=alt.Y("million_sqft:Q", title="Million square feet"),
        color=highlight,
    )
)
bars
```

## Step 3: Annotate directly on the chart

Put the words right next to the thing they're about. Readers shouldn't have
to go back and forth between the chart and a caption.

Annotations in Altair are just more layers -- a `mark_text` with its own
little dataframe.

```python
notes = pd.DataFrame(
    [
        {"Decade": 1960, "million_sqft": 21.4, "note": "21 million sq. ft. -- about double the 1950s"},
        {"Decade": 2010, "million_sqft": 2.6, "note": "Only 2010-2019"},
    ]
)

annotations = (
    alt.Chart(notes)
    .mark_text(align="left", dx=22, dy=-4, fontSize=12)
    .encode(x="Decade:O", y="million_sqft:Q", text="note:N")
)

(bars + annotations).properties(width=500)
```

## Step 4: Be honest about the caveats

That 2010s bar looks like a collapse! But our data stops in 2019, and
buildings that are still being built aren't in there. We already put a
note on it -- but the more honest move might be to make it look different,
so nobody reads it as "the same kind of bar."

We'll also add a source line. Always add a source line.

```python
partial = alt.condition(alt.datum.Decade == 2010, alt.value(0.4), alt.value(1.0))

bars_honest = bars.encode(opacity=partial)

story = (
    (bars_honest + annotations)
    .properties(
        width=500,
        # This becomes the aria-label on the SVG, which is what a screen
        # reader will announce. More on this in a couple of weeks!
        description=(
            "Bar chart of total square footage of Illinois state-owned buildings by "
            "decade of construction, 1880s to 2010s. Construction rises steadily to a "
            "peak of about 21 million square feet in the 1960s, roughly double the "
            "1950s, then declines each decade. The 2010s bar only covers 2010 to 2019."
        ),
    )
    .configure_view(stroke=None)
)

story
```

Altair doesn't have a built-in "source" line, but a caption works fine in
whatever you're embedding into -- in Streamlit that's `st.caption(...)`.
In a notebook, it's just markdown:

_Source: Illinois Building Inventory, data.illinois.gov. Buildings with no
construction year recorded (289 of them) are excluded._


## Step 5: Can everybody read it?

We wrote a `description`, which helps. But a screen reader user still gets
one sentence and that's it -- they can't _explore_ the chart the way you
can with your eyes.

[maidr](https://py.maidr.ai/) (from the xability lab, right here in the
iSchool!) makes charts navigable by keyboard, and readable as text, sound
and braille. Click on the chart below (or Tab to it), use the arrow keys to
move between bars, and press **T** for text, **S** for sound and **B** for
braille. **Ctrl + /** (Command + / on a Mac) shows all the keys.

We'll spend a lot more time on this in week 14.

```python
import maidr

maidr.show(bars_honest.properties(width=500))
```

## Your turn

Take a chart you've made for your Part One exploration, and:

1. Write a title that's a sentence.
2. Highlight the one thing you want people to see.
3. Annotate it directly.
4. Write the one-paragraph description you'd want a screen reader to say.
