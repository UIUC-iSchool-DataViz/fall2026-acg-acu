---
layout: week
visible: true
icon: undraw_researching_22gp.svg
notitle: true
tags:
  - python
  - workflows
  - accessibility
  - maidr
examples:
  - filename: accessible_viz
    type: ipynb
    title: Accessible Visualization
    description: Color and contrast, redundant encoding, alt text, data tables, and exploring charts by keyboard, sound and braille with maidr
  - filename: streamlit/accessible_observatory.py
    type: streamlit
    title: Accessible Earthquake Observatory
    description: The week 12 observatory redone with render_maidr, a generated text summary, a data table, and opt-in auto-refresh
---

# Putting It All Together, for Everybody

So how do we take all our components and jam them together into something we
can use over and over again? And how do we make sure that everybody -- not
just people who can see our charts the way we do -- can actually use them?

To run the Streamlit example: `uv run streamlit run week14/streamlit/accessible_observatory.py`
from the course repo, or download it and `pip install "maidr[streamlit,altair]"` first.
