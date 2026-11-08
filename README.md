# Course Template

This repository is a template for managing coursework using GitHub pages. It
uses the theme [dinky](https://github.com/pages-themes/dinky),
[nbviewer.js](https://github.com/kokes/nbviewer.js), and
[reveal.js](https://revealjs.com/) for presenting material.

For each week of class, create a subdirectory `weekZZ` (where `ZZ` is the week
of the class) and place any `.ipynb` and `.md` files in that directory.
Lectures can utilize the layout `lecture`, which will present them in revealjs.

## Notes on Course Materials

As of Fall 2020, this section and the [section developed in parallel by Jill
Naiman](https://github.com/UIUC-iSchool-DataViz/is445AOG_fall2020/) have
diverged somewhat. Occasionally, contributions will be passed back and forth
and the commit message history may not reflect the original authorship.

These two repositories have been developed in collaboration, and authorship is
shared between Matthew Turk and Jill Naiman.

## Development

### Python environment

This repository's own tooling (jupytext, pre-commit, doit, the link checker,
and optionally the packages needed to run the course notebooks) is managed
with [`uv`](https://docs.astral.sh/uv/). No manual virtualenv or conda setup
is needed:

```bash
uv sync                    # tooling only (jupytext, pre-commit, doit, ...)
uv sync --extra notebooks  # also installs the full notebook stack (pandas, bqplot, geopandas, ...)
uv run jupyter lab         # run notebooks locally (requires the notebooks extra)
```

### Jupytext and Pre-commit

This repository uses `jupytext` to manage Jupyter notebooks. This allows us to
store notebooks as markdown files, which are easier to diff and merge. We use
`pre-commit` to automatically sync the `.ipynb` and `.md` files.

To set this up:

1.  Install the git hooks:
    ```bash
    uv run pre-commit install
    ```

### Adding a New Notebook

To add a new notebook to the repository:

1.  Create your notebook as usual (e.g., `my_notebook.ipynb`).
2.  Pair the notebook with the markdown and percent-script formats configured
    in `jupytext.toml`, using `jupytext`:
    ```bash
    uv run jupytext --set-formats ipynb,py:percent,md my_notebook.ipynb
    ```
3.  Stage the files for commit.
    ```bash
    git add my_notebook.ipynb my_notebook.md
    ```
4.  Commit your changes. The `pre-commit` hook should ensure consistency.
