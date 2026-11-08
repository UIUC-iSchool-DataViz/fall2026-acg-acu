---
title: Svelte on PrairieLearn
layout: lecture
tags:
  - javascript
  - svelte
  - d3
description: >-
  We went over how to test out Svelte on PrairieLearn
# Retired Fall 2026 (replaced by "Build Your Observatory"); kept for reference.
date: 2026-11-16
---

---

# Installing Dependencies

1. Launch VS Code workspace
1. In terminal, type: `conda install -y nodejs`
1. Now, we follow the [Skeleton.dev](https://skeleton.dev) [instructions](https://www.skeleton.dev/docs/get-started/installation/vite-svelte) for `vite` + `svelte`.

---

# Initializing Svelte App

We will now create a new Svelte app -- note, this is not the same as a SvelteKit app!

```
npm create vite@latest viz-in-svelte -- --template svelte-ts
cd viz-in-svelte
npm install
npm i -D @skeletonlabs/skeleton @skeletonlabs/skeleton-svelte
npm install tailwindcss @tailwindcss/vite
```

---

# Initializing our Skeleton Template

Now, we have to add the `tailwindcss` to our `vite` plugin. (What's `vite`, you say?!) This goes in `vite.config.js`.

```typescript
import { defineConfig } from "vite";
import { svelte } from "@vitejs/vite-plugin-svelte";
import tailwindcss from "@tailwindcss/vite";

export default defineConfig({
  plugins: [
    tailwindcss(),
    svelte(), // <-- Must come after Tailwind
  ],
  server: { allowedHosts: ["us.prairielearn.com"] },
  base: "./",
});
```

---

# Add our CSS to our page

Now, we modify the file `src/app.css` to include the stylesheets:

```css
@import "tailwindcss";

@import "@skeletonlabs/skeleton";
@import "@skeletonlabs/skeleton/optional/presets";
@import "@skeletonlabs/skeleton/themes/cerberus";

@source '../node_modules/@skeletonlabs/skeleton-svelte/dist';
```

And add `data-theme="cerberus"` to the `<html>` opening tag in `index.html`.

---

# Now we Svelte!

Recall a few things about Svelte:

- We write inside `.svelte` files, which include a `<script>` section at the top, and then below that the HTML-ish code for display.
- Our logic is applied inside curly brackets: `{` and `}`.
- To include a variable, or execute javascript code, write it as a statement inside brackets.
- To use logic or iteration: `{#each dataArray as dataElement}` followed by `{/each}`.
- Conditionals use `{#if}`, `{:else if}`, `{:else}` and `{/if}`.

---

# Binding Variables

We bind variables either by utilizing `bind:` to prefix an attribute:

```html
<input bind:value="{someVariable}" />
```

Or, if the variable name matches the attribute (i.e., `value`), we can just write `{value}`:

```html
<input {value} />
```

If we don't bind, this is unidirectional.

---

# Reactive Sections

We can write sections of code that will execute whenever a "dependency" variable in them changes inside a `$` section. For instance, imagine we wanted to recalculate a `height` variable based on a `width` variable.
Inside our `<script lang="ts">` section, we would write:

```
$: height = width * 2;
```

Svelte will process this whenever `width` changes, and update.

---

# Vega-Lite

Now, let's install vega-lite as a Svelte component and see what we can do!

```
npm install svelte-vega --save
```

This gives us access to the `<VegaLite>` component, which we can specify specifications and data to.

---

# Serving on PrairieLearn

Once we've installed our components, run:

```
npm run build
```

and in a different terminal, run:

```
npm run preview
```
