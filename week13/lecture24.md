---
title: Build Your Observatory
layout: lecture
tags:
  - streamlit
  - final-project
  - deployment
  - llms
description: >-
  A workshop: turning your prototype into a Streamlit app, deploying it before
  you leave today, and taking a hard look at what AI tools do to your charts.
date: 2026-11-16
---

# Build Your Observatory

For the rest of today, we're going to build.

1. **From prototype to app** -- a template you can steal
2. **Deploy it today** -- every group leaves with a URL
3. **AI tools and your charts** -- what they get wrong, and our policy
4. **Group time**

---

# From Prototype to App

---

## The Template

`week13/streamlit/observatory_template.py` is a skeleton for Part Three. It runs as-is, with weather forecasts from [Open-Meteo](https://open-meteo.com/) (free, no API key), but it's meant to be gutted and filled with _your_ data.

```bash
uv run streamlit run week13/streamlit/observatory_template.py
```

Look for the `CHANGE THIS` comments. Those are the parts that are yours.

---

## The Structure: A Martini Glass

Remember from week 12? You lead, and then you let go.

| Tab | What goes in it |
| --- | --- |
| **The Story** | The main point in words, generated from the data, plus one or two annotated charts |
| **Explore** | Controls and charts to poke at |
| **Data** | The table, and a download button |
| **About** | Where the data comes from, how it updates, who made it |

```python
story, explore, data, about = st.tabs(["The Story", "Explore", "Data", "About"])

with story:
    st.markdown(summary)
    render_maidr(story_chart)
```

---

## Loading Your Data

Whatever your data is, get it into a tidy dataframe: one row per observation, one column per variable.

```python
@st.cache_data(ttl=600)
def load_data(lat, lon):
    response = requests.get("https://api.open-meteo.com/v1/forecast", params={...})
    response.raise_for_status()  # fail loudly if the API is down
    return pd.DataFrame(response.json()["hourly"])
```

- `ttl` -- be polite to whoever is serving your data
- `raise_for_status()` -- an error message beats a mysteriously empty chart
- plus a **Check for new data** button that calls `load_data.clear()`

---

## API Keys: Never in Your Code

Your repo is public. If you commit a key, assume somebody has it.

**Locally**, in `.streamlit/secrets.toml` (which is in our `.gitignore`):

```toml
MY_API_KEY = "abc123"
```

**On Streamlit Community Cloud**, paste the same thing into your app's _Settings → Secrets_.

**In your code:**

```python
api_key = st.secrets["MY_API_KEY"]
```

note:
if somebody does commit a key: revoke it and make a new one.  deleting the commit doesn't help, it's already out there.

---

## The Story Writes Itself (From the Data)

```python
warmest = future.loc[future["temperature_2m"].idxmax()]
st.markdown(
    f"It's {current['temperature_2m']:.0f}°F in {place} right now. "
    f"It'll be warmest on {when(warmest['time'])} ({warmest['temperature_2m']:.0f}°F)."
)
```

The same goes for the chart title: `f"It'll get as warm as {high}°F by {day}"`.

When the data changes, the story changes with it. That's what makes it an _observatory_.

---

## Things We Found Building the Template

Every one of these silently made the app worse, with no error message:

- **Charts 2,400 pixels wide.** 120 hourly labels on an ordinal axis, and Altair gives each one 20 pixels. Set a `width`.
- **`width="container"` comes out zero pixels wide** inside `render_maidr`. Use a number.
- **Time axes read aloud as milliseconds.** maidr announced "time is 1,793,952,000,000." A text label like "Tue 3 PM" fixed it.
- **`%-I` in `strftime`** (hour without a leading zero) works on Mac and Linux, and crashes on Windows.

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
2. Copy in `observatory_template.py` and `requirements.txt` from `week13/streamlit/`.
3. Commit and push.
4. Go to [share.streamlit.io](https://share.streamlit.io), sign in with GitHub, and **Create app**.
5. Pick your repo, branch, and `observatory_template.py`.
6. Wait a couple of minutes, and you've got a `something.streamlit.app` URL.

**Before you leave:** send your app's URL to me and Yilin.

It doesn't have to be _your_ data yet. It just has to be _deployed_. Then every push after this is just an update.

---

## If It Breaks

Click **Manage app** in the bottom right of your deployed app to see the logs.

- `ModuleNotFoundError` → add it to `requirements.txt`
- `FileNotFoundError` → paths are relative to the root of your repo
- `StreamlitSecretNotFoundError` or `KeyError` → add the key under Settings → Secrets
- Works locally, but the cloud is out of memory → load less data, or aggregate it first

Still stuck? Grab one of us.

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
- Do the colors pass 3:1? Is color the only encoding?
- Does it show uncertainty, if there is some?
- What does it sound like in maidr?

---

## What We Usually Find

Some of the most common problems:

- Default colors and default titles ("Temperature by Time")
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
- [ ] You know what your "story" is -- one sentence, written down
- [ ] If you used an LLM today, you wrote down the prompt

**Next time (November 30):** we go deep on accessibility, and you'll audit your app. Presentations are **December 7**!
