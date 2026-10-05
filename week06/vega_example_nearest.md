---
title: Nearest-point hover
description: Hovering over a line chart highlights and labels the nearest point
layout: vegalite_example
---

{
  "$schema": "https://vega.github.io/schema/vega-lite/v6.json",
  "data": {
    "url": "https://raw.githubusercontent.com/UIUC-iSchool-DataViz/is445_data/main/building_inventory.csv"
  },
  "width": 600,
  "height": 400,
  "transform": [
    {
      "aggregate": [
        {"op": "sum", "field": "Square Footage", "as": "total_square_footage"}
      ],
      "groupby": ["Year Acquired"]
    }
  ],
  "layer": [
    {
      "mark": "line",
      "encoding": {
        "x": {"field": "Year Acquired", "type": "temporal"},
        "y": {"field": "total_square_footage", "type": "quantitative"}
      }
    },
    {
      "params": [
        {
          "name": "hover",
          "select": {
            "type": "point",
            "fields": ["Year Acquired"],
            "nearest": true,
            "on": "pointerover",
            "clear": "pointerout"
          }
        }
      ],
      "mark": {"type": "point", "opacity": 0, "size": 400},
      "encoding": {
        "x": {"field": "Year Acquired", "type": "temporal"},
        "y": {"field": "total_square_footage", "type": "quantitative"}
      }
    },
    {
      "transform": [{"filter": {"param": "hover", "empty": false}}],
      "mark": "point",
      "encoding": {
        "x": {"field": "Year Acquired", "type": "temporal"},
        "y": {"field": "total_square_footage", "type": "quantitative"}
      }
    },
    {
      "transform": [{"filter": {"param": "hover", "empty": false}}],
      "mark": {"type": "rule", "color": "gray"},
      "encoding": {
        "x": {"field": "Year Acquired", "type": "temporal"}
      }
    },
    {
      "transform": [{"filter": {"param": "hover", "empty": false}}],
      "mark": {"type": "text", "align": "left", "dx": 6, "dy": -6},
      "encoding": {
        "x": {"field": "Year Acquired", "type": "temporal"},
        "y": {"field": "total_square_footage", "type": "quantitative"},
        "text": {"field": "total_square_footage", "type": "quantitative", "format": ".3s"}
      }
    }
  ]
}
