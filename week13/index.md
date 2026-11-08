---
layout: week
visible: true
icon: undraw_monitor_iqpq.svg
notitle: true
tags:
  - uncertainty
  - small-multiples
  - d3
  - streamlit
  - deployment
examples:
  - filename: uncertainty_small_multiples
    type: ipynb
    title: Uncertainty and Small Multiples
    description: Error bars (and what they mean), distributions, small multiples, and what survives when you make them accessible with maidr
  - filename: streamlit/observatory_template.py
    type: streamlit
    title: Observatory Template (Streamlit)
    description: A skeleton for your final project -- story, explore, data and about tabs, cached API loading, secrets, maidr charts. Runs as-is with Open-Meteo weather data.
  - filename: streamlit/requirements.txt
    type: text
    title: requirements.txt for the template
    description: Copy this into your repo alongside the template to deploy on Streamlit Community Cloud
  - filename: lecture_network
    type: ipynb
    title: Network Visualization with bqplot
    description: Drawing a force-directed network graph and comparing it to a ring layout, using igraph and bqplot
---

# Validation, Uncertainty, Small Multiples, and D3

This week we discussed how to determine if a visualization is effective (and
for whom!), how to show uncertainty, and how to use small multiples. From a
technical standpoint we worked to develop dynamic D3 visualizations and
interactivity in those visualizations. Then we built our observatories: every
group started from a Streamlit template and deployed it to Streamlit Community
Cloud before leaving.
