---
title: Build Your Viz for the Public
layout: lecture
tags:
  - streamlit
  - final-project
  - deployment
  - presentations
  - llms
description: >-
  A workshop: turning your project into a Streamlit app for the public,
  deploying it before you leave today, planning your presentation and video,
  and taking a hard look at what AI tools do to your charts.
date: 2026-11-16
---

# Build Your Viz for the Public

For the rest of today, we're going to build.

1. **From notebook to app** -- a template you can steal
2. **Deploy it today** -- every group leaves with a URL
3. **Presenting your work** -- five minutes, and a video
4. **AI tools and your charts** -- what they get wrong, and our policy
5. **Group time**

---

# From Notebook to App

---

## The Template

`week13/streamlit/part3_template.py` is a skeleton for Part 3. It runs as-is, with the Illinois building inventory, but it's meant to be gutted and filled with _your_ data.

```bash
uv run streamlit run week13/streamlit/part3_template.py
```

Look for the `CHANGE THIS` comments. Those are the parts that are yours.

---

## The Structure: A Martini Glass

Remember from week 12? You lead, and then you let go.

| Tab | What goes in it |
| --- | --- |
| **The Story** | The main point in words, computed from the data, plus one or two annotated charts |
| **Explore** | Controls and charts to poke at |
| **Data** | The table, and a download button |
| **About** | Where the data comes from, what you did to it, who made it |

```python
story, explore, data, about = st.tabs(["The Story", "Explore", "Data", "About"])

with story:
    st.markdown(summary)
    render_maidr(story_chart)
```

---

## Loading Your Data

Put your data file in your repo, next to your script.

```python
DATA_FILE = pathlib.Path(__file__).parent / "my_data.csv"

@st.cache_data
def load_data():
    raw = pd.read_csv(DATA_FILE)
    df = raw[raw["Year Constructed"] > 0]   # your cleaning goes here
    return df, len(raw) - len(df)
```

- Paths relative to `__file__` work the same on your laptop and in the cloud
- Do your cleaning _once_, here -- and keep track of what you threw away, so you can say so in the About tab
- Too big for GitHub? Aggregate it first, and commit the smaller file

---

## If Your Data Comes from an API

Your repo is public. If you commit an API key, assume somebody has it.

**Locally**, in `.streamlit/secrets.toml` (which is in our `.gitignore`):

```toml
MY_API_KEY = "abc123"
```

**On Streamlit Community Cloud**, paste the same thing into your app's _Settings → Secrets_.

**In your code:** `st.secrets["MY_API_KEY"]`

note:
if somebody does commit a key: revoke it and make a new one.  deleting the commit doesn't help, it's already out there.

---

## The Story Is Computed (From the Data)

```python
first = by_agency.iloc[0]
st.markdown(
    f"The **{first['Agency Name']}** alone has "
    f"**{first['Square Footage'] / total:.0%}** of it."
)
```

The same goes for the chart title: `f"The {first['Agency Name']} has more building space than any other agency"`.

If you typed the numbers in by hand, they'd go stale the moment you changed your cleaning. Computed, they can't.

---

## Things We Found Building These Examples

Every one of these silently made a chart worse, with no error message:

- **Bars in alphabetical order.** `sort="-x"` gets ignored once you layer a text label on top of a bar chart. Pass the order explicitly.
- **`width="container"` comes out zero pixels wide** inside `render_maidr`. Use a number.
- **Time axes read aloud as milliseconds.** maidr announced "time is 1,793,952,000,000." A text label like "1960s" or "Tue 3 PM" fixes it.
- **Maps read aloud as ID numbers.** "id is 2" is Alaska. Pair a map with a sorted bar chart.

The lesson: **look at it, and listen to it.** Every time.

---

# Deploy It Today

---

## Why Today?

Because the first time you deploy should not be the night before presentations.

Things that go wrong on deploy, that never go wrong on your laptop:

- A package missing from `requirements.txt`
- A data file at a path that only exists on your machine
- A data file too big for GitHub
- An API key that's in your `secrets.toml` but not in the cloud's Secrets

We want to find all of these _while Yilin and I are in the room_.

---

## Deploying, Step by Step

1. Make a **public** GitHub repo for your group.
2. Copy in `part3_template.py` and `requirements.txt` from `week13/streamlit/`, and your data file.
3. Commit and push.
4. Go to [share.streamlit.io](https://share.streamlit.io), sign in with GitHub, and **Create app**.
5. Pick your repo, branch, and `part3_template.py`.
6. Wait a couple of minutes, and you've got a `something.streamlit.app` URL.

**Before you leave:** send your app's URL to me and Yilin.

It doesn't have to be finished. It just has to be _deployed_. Then every push after this is just an update.

---

## If It Breaks

Click **Manage app** in the bottom right of your deployed app to see the logs.

- `ModuleNotFoundError` → add it to `requirements.txt`
- `FileNotFoundError` → is the file committed? Is the path relative to your script?
- `StreamlitSecretNotFoundError` or `KeyError` → add the key under Settings → Secrets
- Works locally, but the cloud is out of memory → load less data, or aggregate it first

Still stuck? Grab one of us.

---

# Presenting Your Work

---

## Five Minutes Is Not Very Long

On December 7, each group gets **five minutes**. Here's a shape that works:

1. **The point** (30 seconds) -- your one sentence. Say it first!
2. **The data** (30 seconds) -- what it is, where it came from, who it's for
3. **The story** (2 minutes) -- walk through your Story tab, then show one thing in Explore
4. **One decision** (1 minute) -- something from your Part 1 notebook that you changed for the public, and why. Stumbling blocks count!
5. **What's next** (30 seconds) -- what you'd do with more time

Don't show code. Don't read the screen to us.

note:
the "one decision" part is my favorite part of these -- seeing the viz-for-self version next to the public version.

---

## Live Demos Go Wrong

- **Wake your app up first.** Apps on Community Cloud go to sleep when nobody visits, and take a minute to wake up. Open it before class.
- **Have screenshots** in case the Wi-Fi or the app doesn't cooperate.
- **Zoom in** in your browser. What's readable on your laptop is not readable from the back of the room.
- **One person drives**, so nobody is saying "no, click the other one."
- **Practice with a timer.** Everybody runs long the first time.

---

## The Video

Your group also submits a video. The requirements (length, what to cover) are on Canvas.

- Show the **app**, not slides about the app
- Record your screen and talk over it -- the same shape as the presentation works fine
- **Turn on captions**, and fix the automatic ones. They will get your dataset's jargon wrong!
- Watch it once all the way through before you submit it

Remember: we're about to spend a whole class on accessibility. Your video is part of your project, too.

---

## Try It (5 minutes)

With your group:

1. Write down your **one sentence**. Not a topic ("building ownership"), a claim ("the University of Illinois owns a quarter of the state's building space").
2. Say it out loud to the group next to you.
3. They tell you what they think your project is about. Does it match?

---

# AI Tools and Your Charts

---

## You're Using Them

Many of you are probably using ChatGPT, Claude, Copilot and friends to write plotting code. That's allowed in this class, within [the policy in the syllabus](../syllabus.html). So let's talk about using them _well_.

These tools are very good at producing a chart that _runs_. They are much less good at producing a chart that's _right_.

---

## Try It (10 minutes)

With your group:

1. Give an LLM the column names of your dataset and ask it for a Streamlit chart that answers a question you care about.
2. Run what it gives you.
3. Now critique it, using what we've learned this semester:

- Does it actually answer the question?
- **Are the numbers right?** Check one or two against pandas yourself.
- Did it invent a column, or a unit, or a fact?
- Is the title a sentence that says something? Are the axes labeled, with units?
- If it's a map: is it a rate, or a population map?
- Do the colors pass 3:1? Is color the only encoding?
- What does it sound like in maidr?

---

## What We Usually Find

Some of the most common problems:

- Default colors and default titles ("Square Footage by Agency Name")
- Axes that start somewhere misleading, or a log scale nobody asked for
- A plausible-looking aggregation that's subtly wrong (a mean of means, a sum that should be a count)
- Confident text about the data that the data doesn't support
- Nothing at all for accessibility

None of these throw an error. You have to _look_.

---

## Our Policy, in Practice

From the syllabus: you can use LLMs, but if you do, you need to include:

- **Which LLM, and when** you used it
- **The prompt** you gave it
- **Your validation plan** -- for code, your own tests showing it does what you think, and a few sentences on how those tests relate to the prompt

For your final project, put this in your **About** tab, or in a `LLM_USAGE.md` in your repo.

Honestly? Writing the validation plan is how you'll catch the mistakes in the last slide.

---

# Group Time

---

## Before You Leave

- [ ] Your group's app is deployed, and you've sent us the URL
- [ ] You've started swapping in your own data
- [ ] Your one sentence is written down
- [ ] You've roughed out who presents which part
- [ ] If you used an LLM today, you wrote down the prompt

**Next time (November 30):** we go deep on accessibility, and you'll audit your app. Presentations are **December 7**!
