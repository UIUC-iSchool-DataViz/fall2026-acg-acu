---
title: Scaling, Colors, and Colormaps
layout: lecture
tags:
  - scaling
  - colors
  - colormaps
  - transformations
description: >-
  How are values transformed from 0's and 1's into values we can manipulate and understand?  When we draw something on a screen, how do we represent that internally, and how is that translated into pixels?  What operations can we do on data? How do colors work?  What are the different ways we can map colors to values?  What should we keep in mind when doing this?
date: 2026-09-14
---

## Scaling Data

---

## Transformations

We will need to transform data in order to apply consistent visual encoding.
There are many reasons we may need to accomplish this, including color mapping,
applying units, and co-registration or normalization of data.

One of the most important transformations we will have is that of an [Affine transformation](https://en.wikipedia.org/wiki/Affine_transformation). This is a transformation that preserves:

- Collinearity
- Parallellism
- Convexity
- Ratios of parallel lines
- Barycenters of point sets

---

## Transformations

Affine transformations satisfy:

$ \vec{y} = A\vec{x} + \vec{b} $

<!-- .slide: data-background-image="images/affine_1.svg" data-background-size="30% auto" data-background-position="right 20% bottom 50%" -->

---

## Transformations

Affine transformations satisfy:

$ \vec{y} = A\vec{x} + \vec{b} $

We can use these to accomplish:

- Shifts

<!-- .slide: data-background-image="images/affine_2.svg" data-background-size="30% auto" data-background-position="right 20% bottom 50%" -->

---

## Transformations

Affine transformations satisfy:

$ \vec{y} = A\vec{x} + \vec{b} $

We can use these to accomplish:

- Shifts
- Rotations

<!-- .slide: data-background-image="images/affine_3.svg" data-background-size="30% auto" data-background-position="right 20% bottom 50%" -->

---

## Transformations

Affine transformations satisfy:

$ \vec{y} = A\vec{x} + \vec{b} $

We can use these to accomplish:

- Shifts
- Rotations
- Scaling

<!-- .slide: data-background-image="images/affine_4.svg" data-background-size="30% auto" data-background-position="right 20% bottom 50%" -->

---

## Transformations

<div class="col" data-markdown=true>

In this figure, we can adjust the mixing vectors and the offset. What do you notice about colinear points and parallel lines?

<div class="fig-container" data-style="height: 600px;" data-file="figures/affine_transformation.html" data-markdown=true>
</div>

---

## Scales and Scaling

Displaying a quantity requires assigning to it a given representation.
A common mechanism for doing this is to vary the color of a particular region
or set of display units with respect to the quantity expressed in those units.

In mathematical notation, we first "normalize" our data value by assigning to a
range:

$g(v) \rightarrow v' \in [0, 1]$

and then, given a color mapping function, assign to this a given color:

$f(v') \rightarrow (R, G, B)$

---

## Scales and Scaling

Group discussion:

- How is this similar to or different from our discussions of "binning" and
  histogramming?
- What are some functions we can use for $g(v)$?
- What are some considerations we need to take into account for variable
  bins?

---

<!-- .slide: data-background-image="https://upload.wikimedia.org/wikipedia/commons/e/e8/1414_Rods_and_Cones.jpg" data-background-size="auto 75%" data-background-position="right 30% bottom 50%"-->

## How Do Colors Work?

<div class="left" data-markdown=true>

Rods (low-light) and cones (color) mediate vision. Humans have about 20 times
as many rods (120 million) as cones (6 million).

Roughly speaking, cones see in the colors red, green and blue.

By OpenStax College [CC BY 3.0](http://creativecommons.org/licenses/by/3.0),
via Wikimedia Commons

</div>

---

## Color Responsivity Function

<!-- .slide: data-background-image="images/resp.png" data-background-size="auto 75%" -->

---

## "Naming" Colors

<img src="images/hereIsAColor_nohexnohsvhorgb.png" height="600"/>

notes: so, we talk about how colors are named in different systems, and we'll cover the most basic here

---

## "Naming" Colors

<img src="images/hereIsAColor_nohexnohsv_a.png" height="600"/>

notes: since we have RGB rods and cones, we might think the most natural way to represent this is with RGB colors

This color wheel doesn't give an accurate depiction of all the colors in RGB space
(since the space is actually 3d), but it is often
what you'll see out in the real world, and its pretty easy to see where our example color lies.

This is the representation you played with in the HW for this past week.

---

## "Naming" Colors

<img src="images/hereIsAColor_nohex_a.png" height="600"/>

notes: another representation is Hue, Saturation, and Value

This depiction of HSV is in 3D here, and while its easier to visualize how colors change in the space, its
also hard to accurately mark where our specific one is.

---

## "Naming" Colors

<img src="images/hereIsAColor_allAnn.png" height="600"/>

notes: here is another example - you'll see these codes a lot of you do html programming, but its another way to
specify colors with HEX numbers. You'll note our color isn't listed here, but in a longer table it would be.

Hexadecimal only shows 16 million colors, RGB as uncompressed floats can theoretically represent quite a bit more (but there's a limitation of what monitors can display)

R = 2^8
G = 2^8
B = 2^8

RGB = 2^24 = 16 million

hexadecimal = 16^6 = 16 million

---

## "Naming" Colors: R,G,B Mapping

<img src="images/mandrillRGB.gif" width="600"/>

notes:
the mandrill image was an early color standardization image established by the Dept of Defense

Here we split it into its R, G, & B components

we can see different parts of this image are highlighted with specific colors -- red nose, blue/green cheeks/side of nose

---

## "Naming" Colors: R,G,B Mapping - Its limitations

<table><tr>
<td><img src="images/sRGB.gif" width="300"/></br>sRGB - graphics RGB</td>
<td><img src="images/CIELAB.gif" width="300"/></br>CIELAB - human RGB perception</td>
</tr></table>

notes:
this unified space of colors that works on most displays and printers is NOT the full range of human perception.

on the left we see the color space available on a typical laptop screen, on the right we see the full range of what a human can see -- this space is larger

---

## HSV Wheel

![HSV Wheel](./images/HSVcylinder.png)<!-- .element: width="500" -->

https://commons.wikimedia.org/wiki/File:HSV_color_solid_cylinder.png

By HSV_color_solid_cylinder.png: SharkD derivative work: SharkD Talk \[CC BY-SA 3.0
(http://creativecommons.org/licenses/by-sa/3.0) or GFDL
(http://www.gnu.org/copyleft/fdl.html)\], via Wikimedia Commons

---

## "Naming" Colors: HSV

<img src="images/mandrillHSV.gif" width="500"/>
(Cycle is though (1) H to change color, (2) S to change to grayscale, (3) V black to white)

notes:
This video scans through different hues, which are the part of the rainbow you want

Then different saturations, which is how vibrant or gray the colors are

Then different values, which is how bright or dark the colors are.

Allow to run first and then comment.

---

## "Naming" Colors: HSV

<img src="https://miro.medium.com/max/964/1*B2d44wTBqfygLEZ8ZTJXzg.png">

notes:
You might have actually played around with this system before if you've ever used a "color" picker app.

Here we see we have picked a "H" for Hue as red

We choose 50% saturation - i.e. how much of the color is in there where minimum is none of the color (gray)

We also choose 50% "L" which is sometimes called "V" for Luminiance which controls white-to-black

And here is one more channel = A for opacity. Note that "A" sort of overlaps with both Saturation and Luminance so its usually not used to encode anything if we are using the others.

---

## "Naming" Colors: HSV

<div class="fig-container" data-style="height: 650px;" data-file="figures/hsv_space.html" data-markdown=true>
</div>

---

## "Naming" Colors: Beyond HTML HEX - Specific Names

<table><tr>
<td><img src="images/htmlColors.png" width="550"/></br>HTML</td>
<td><img src="images/matplotlibColors.png" width="550"/></br>matplotlib</td>
</tr></table>

notes:
It's worth noting that "color words" are not consistent across languages or cultures. Color is a product of culture.

---

## "Naming" Colors: Summary

- Color spaces
  - HSV (Hue, saturation, value)
  - [CIELAB](https://en.wikipedia.org/wiki/CIELAB_color_space)
  - sRGB, Adobe sRGB
- RGB triplets, sometimes compressed into hexadecimel ("#00FFAA", etc)
- List of colors by name
  - [Web](https://www.w3schools.com/colors/colors_names.asp)
  - [matplotlib](https://matplotlib.org/2.0.2/examples/color/named_colors.html)

note:
coding environments will often provide "named" colors if you're more interested in simplicity than flexible design

HSV is typically a color space used by color designers.

sRGB "standard RGB" is a color space that was standardized to unify different monitors and printers.

CIELAB is the color space that covers the average of human vision.

---

## Importance of Color

Which image has the red dot?

notes:

why is color important? to see why...

lets play a game -- which image has a red dot? yell out left or right

we'll see a series of images

---

## Importance of Color

Which image has the red dot?

<!-- .slide: class="two-floating-elements" -->

<div class="left">
  <img src="https://www.csc2.ncsu.edu/faculty/healey/PP/figs/colour_P.gif">
</div>

<div class="right">
 <img src="https://www.csc2.ncsu.edu/faculty/healey/PP/figs/colour_A.gif">
</div>

---

## Importance of Color

Which image has the red dot?

<!-- .slide: class="two-floating-elements" -->

<div class="left">
  <img src="https://www.csc2.ncsu.edu/faculty/healey/PP/figs/shape_A.gif">
</div>

<div class="right">
 <img src="https://www.csc2.ncsu.edu/faculty/healey/PP/figs/shape_P.gif">
</div>

---

## Importance of Color

Which image has the red dot?

<!-- .slide: class="two-floating-elements" -->

<div class="left">
  <img src="https://www.csc2.ncsu.edu/faculty/healey/PP/figs/conjoin_A.gif">
</div>

<div class="right">
 <img src="https://www.csc2.ncsu.edu/faculty/healey/PP/figs/conjoin_P.gif">
</div>

---

## Importance of Color

[https://www.csc2.ncsu.edu/faculty/healey/PP/#jscript_search](https://www.csc2.ncsu.edu/faculty/healey/PP/#jscript_search)

Color makes use of our "preattentive" visual cortex processing power -- we are able to detect color _before_ our attention focuses.

notes:
which was the easiest one to do of these 3 images?

we can make thinks more/less complex with this game (that is part of your optional reading for this week)

---

## Color maps as Visual Encoding

Color maps encode a data attribute as a color.

---

## Color maps as Visual Encoding

Color maps encode a data attribute as a color.

<img src="images/pbn_pallet_long.png" width="600"/>

<table><tr>
<td><img src="images/pbn_outline.png" width="400"</td>
<td><img src="http://3.bp.blogspot.com/_jxQyBncYPVE/TUFd8rPodoI/AAAAAAAAHuM/1NnmDWI_Poc/s1600/corgilobster.jpg" width="400"/></td>
</tr></table>

notes:
you can think of it like a paint by numbers

Here I give you outlines of sections of the page that have data values, here the numbers 1-13 and I assign them a "palette" of colors.

---

## Color maps as Visual Encoding

Color maps encode a data attribute as a color.

<img src="images/pbn_pallet_long.png" width="600"/>

<table><tr>
<td><img src="images/pbn_outline.png" width="400"/></td>
<td><img src="images/pbn_filled.png" width="400"/></td>
</tr></table>

notes:
Then I "paint" these colors on to make an image from my data

---

## Color maps as Visual Encoding

Color maps encode a data attribute as a color.

<table><tr>
<td>Colormap</br><img src="images/pbn_filled_noborder.png" height="500"/></td>
<td>Photo</br><img src="images/lobsterCorgi_orig.png" height="500"/></td>
</tr></table>

notes:
Here I cheated a little bit and used a photo to generate my paint by numbers, so I get something back that looks like its photo

But note that these images are generated in very different ways

The colormap one was generated by a list of color values and instructions

The photo is generated by RGB color combinations at every pixel

---

## Color Palettes

<img src="https://web.natur.cuni.cz/~langhamr/lectures/vtfg1/mapinfo_2/barvy/S12-fullstructureClean.gif" width="600">

Brewer, 1999

notes:
different kinds of color palettes can be used to describe different types of data

Here is a nice way of mapping out our options. For example, binary (T/F or Y/N) is pretty easy to encode with 2 colors or luminance.

If we have 3 categories, we can choose different hues for qualatative data.

If we have sequential data, like height maps we can choose differences in Hues or luminance.

When we start combining them though, it can get a little more confusing -- for example diverging + sequential is a bit hard to parse

---

## Color Palettes

- Colorbrewer Categories
  - Sequential
  - Diverging
  - Qualitative
- Resources:
- colorbrewer.org
- palettable (package)

---

## Sequential Colormaps

![blues discrete colormap](images/blues_discrete.png)

![blues continuous colormap](images/blues_continuous.png)

---

## Diverging Colormaps

![spectral discrete colormap](images/spectral_discrete.png)

![spectral continuous colormap](images/spectral_continuous.png)

---

## Qualitative Colormaps

![discrete set1 of colors](images/set1_discrete.png)

![continuous set1 of colors](images/set1_continuous.png)

(See? Works better as discrete!)

---

## It's full of colors

https://commons.wikimedia.org/wiki/File:16777216colors.png

---

## Palette Mapping

![](images/set1_discrete.png)

Assign each value to a specific color or element.

---

## Color Mapping

$f(v) \\rightarrow (R, G, B)$

We can also re-map:

$f(v') \\rightarrow (R, G, B)$

$v' = f(v)$

For instance, with logs or squares.

---

## Color Mapping: Linear Mapping

We map from a range of values to (0, 1):

$ v' = (v - v_0)/(v_1 - v_0) $

---

## Colormaps: `gray`

<!-- .slide: data-background-image="images/gray_colors.png" data-background-size="auto 75%" -->

---

## Colormaps: `gray`

<!-- .slide: data-background-image="images/gray_3d.png" data-background-size="auto 75%" -->

---

## Colormaps: `gist_stern`

<!-- .slide: data-background-image="images/gist_stern_colors.png" data-background-size="auto 75%" -->

---

## Colormaps: `gist_stern`

<!-- .slide: data-background-image="images/gist_stern_3d.png" data-background-size="auto 75%" -->

---

## Colormaps: `jet`

<!-- .slide: data-background-image="images/jet_colors.png" data-background-size="auto 75%" -->

---

## Colormaps: `jet`

<!-- .slide: data-background-image="images/jet_3d.png" data-background-size="auto 75%" -->

---

## Colormaps: `magma`

<!-- .slide: data-background-image="images/magma_colors.png" data-background-size="auto 75%" -->

---

## Colormaps: `magma`

<!-- .slide: data-background-image="images/magma_3d.png" data-background-size="auto 75%" -->

---

## Colormaps: `viridis`

<!-- .slide: data-background-image="images/viridis_colors.png" data-background-size="auto 75%" -->

---

## Colormaps: `viridis`

<!-- .slide: data-background-image="images/viridis_3d.png" data-background-size="auto 75%" -->

---

## Image Coloring

<div class="fig-container" data-style="height: 600px;" data-file="figures/example_coloring_image.html" data-markdown=true>
</div>

---

## Colormapping Images

<div class="fig-container" data-style="height: 640px;" data-file="figures/apply_colormap.html" data-markdown=true>
</div>

---

## Color Blindness

<img src="images/colorBlind.png" width="800"/>

notes:
these are not the only types of color blindness, just the types where one of the three types of cone are missing. Sometimes that third cone is just "anomalous", and sometimes more than one cone is missing, but it's much rarer.

You can see that designing for a color blind person can be difficult if you put all the information into one cone. You catch a wider audience by using the colors between the cones, like yellow, cyan, and magenta.

protanopia = no red
deuteranopia = no green
trianopia = no blue

---

## Color Blindness

http://enchroma.com/test/instructions/

---

## Color Blindness - But wait!

http://enchroma.com/test/instructions/

There's more: https://nakeddata.org/2021/01/22/accessible-data-visualisation-beyond-colour-blindness/

Frank Elavksy (Staff Data Visualization Engineer + Designer on the Data Visualization team at Visa Inc.):

- High contrast text
- High contrast elements
- Using texture, shape, units
- Designing with zoom/magnification
- Using Hierarchy and Focus
- Using annotations or guides

notes: the focus on colorblindness in data visualization is at the expense of much more prevalent considerations like designing for low-vision folks

Elvansky suggests these other considerations are also extremely important to consider for folks that are visually impaired, a much larger portion of the population than those with colorblindness that are often ignored

---

## Other methods of visual encoding

<table><tr>
<td><img src="https://www.csc2.ncsu.edu/faculty/healey/PP/figs/tg_size.gif"/></br>Size</td>
<td><img src="https://www.csc2.ncsu.edu/faculty/healey/PP/figs/tg_den.gif"/></br>Density</td>
<td><img src="https://www.csc2.ncsu.edu/faculty/healey/PP/figs/tg_curve.gif"/></br>Curvature</td>
</tr></table>

Check out [sc2.ncsu.edu/faculty/healey/PP](sc2.ncsu.edu/faculty/healey/PP) for more examples and research.

---

## Other methods of visual encoding

Motion is another channel, but is _very_ attention-grabbing.

<table><tr>
<td><img src="https://www.csc2.ncsu.edu/faculty/healey/PP/figs/tg_flick.gif"/></br>Flicker</td>
<td><img src="https://www.csc2.ncsu.edu/faculty/healey/PP/figs/tg_vel.gif"/></br>Velocity</td>
<td><img src="https://www.csc2.ncsu.edu/faculty/healey/PP/figs/tg_dir.gif"/></br>Direction</td>
</tr></table>

Check out [https://www.csc2.ncsu.edu/faculty/healey/PP/](https://www.csc2.ncsu.edu/faculty/healey/PP/) for more examples and research.

---

## Color as a Perception Channel

<!-- .slide: data-background-image="images/vad_slides_p51.png" data-background-size="auto 75%" -->

notes:
color hue, luminance and saturation make use of different "perception channels" listed here

there are others that we intuatively use, like position, length, tilt, area, ect

These are ordered in terms of which are more effective to use -- i.e. which our brains has a better means of tracking -- for both numerical & ordered categorical data (ordered) and categorcial data that is ordinal (no obvious ordering)

---

## Color as a Perception Channel

<!-- .slide: data-background-image="images/stevensLaw.png" data-background-size="auto 75%" -->

notes:
without going into too much detail, this has to do with how different stimuli map to human perception -- often it is highly non-linear

For example, our sensation of electric shock is far more sensitive than just linear, but brightness is far less sensitive

Length is the most linear -- which is why bar charts are so effective for transfering information!

---

## Colormaps: Loading Data

Colormaps in Python - with the Michigan data and the scan data, we'll evaluate:

- How to choose a colormap
- What are some good "bounds" for that colormap
- How do we set our color normalizations and transformations?

---

# To Python!

Let's also play with Pandas!

notes:
what we'll do is start of with some pandas stuff, since that will be useful for the HW and then circle back to color map stuffs

---

## Back to Matplotlib

We will explore our first visualization concepts using matplotlib.

Please be sure to see the "cheat sheets" affiliated with this, which can be found at:

[github.com/matplotlib/cheatsheets/](https://github.com/matplotlib/cheatsheets/)

and which have been duplicated in this repository.

---

## How Does Matplotlib Place Elements

Matplotlib has three primary methods of specifying coordinates, each of which is represented by a different **transformation**.

- **data** coordinates
- **axes** coordinates
- **figure** coordinates

These are not exhaustive! Other transformations exist, such as for the display units, specifying things in inches, and also sub-figure systems.

---

## Matplotlib Coordinate Systems

<!-- .slide: data-background-image="images/matplotlib-coordinates.svg" data-background-size="auto 75%" -->

---

## Specifying Coordinates

We often want to utilize non-data coordinate systems

- Annotations
- Markup
- Positioning of axes and subplots
