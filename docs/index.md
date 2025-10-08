---
sd_hide_title: true
---

# 🔎 Overview

::::{grid}
:reverse:
:gutter: 3 4 4 4
:margin: 1 2 1 2

:::{grid-item}
:columns: 12 4 4 4

```{image} _static/logo-square.svg
:width: 200px
:class: sd-m-auto
:name: landing-page-logo
```

:::

:::{grid-item}
:columns: 12 8 8 8
:child-align: justify
:class: sd-fs-5

```{rubric} MyST - Markedly Structured Text - Parser
```

A Sphinx and Docutils extension to parse MyST,
a rich and extensible flavour of Markdown for authoring technical and scientific documentation.

````{div} sd-d-flex-row
```{button-ref} intro
:ref-type: doc
:color: primary
:class: sd-rounded-pill sd-mr-3

Get Started
```

```{button-ref} live-preview
:ref-type: doc
:color: secondary
:class: sd-rounded-pill

Live Demo
```
````

:::

::::

---

::::{grid} 1 2 2 3
:gutter: 1 1 1 2

:::{grid-item-card} {octicon}`markdown;1.5em;sd-mr-1` CommonMark-plus
:link: syntax/core
:link-type: ref

MyST extends the CommonMark syntax specification, to support technical authoring features such as tables and footnotes.

+++
[Learn more »](syntax/core)
:::

:::{grid-item-card} {octicon}`plug;1.5em;sd-mr-1` Sphinx compatible
:link: roles-directives
:link-type: ref

Use the MyST role and directive syntax to harness the full capability of Sphinx, such as admonitions and figures, and all existing Sphinx extensions.

+++
[Learn more »](roles-directives)
:::

:::{grid-item-card} {octicon}`tools;1.5em;sd-mr-1` Highly configurable
:link: configuration
:link-type: doc

MyST-parser can be configured at both the global and individual document level,
to modify parsing behaviour and access extended syntax features.

+++
[Learn more »](configuration)
:::

::::

---

```{rubric} Additional resources
```

[MyST-Markdown VS Code extension](https://marketplace.visualstudio.com/items?itemName=ExecutableBookProject.myst-highlight)
: For MyST extended syntax highlighting and authoring tools.

[Convert existing ReStructuredText files to Markdown][rst-to-myst]
: Use the [rst-to-myst] CLI or [the MySTyc interactive web interface](https://astrojuanlu.github.io/mystyc/).

[markdown-it-py]
: A CommonMark-compliant and extensible Markdown parser, used by MyST-Parser to parse source text to tokens.

```{rubric} Acknowledgements
```

The MyST markdown language and MyST parser are both supported by the open community,
[The Executable Book Project](https://executablebooks.org).

```{toctree}
:hidden:
README.md
live-preview.md
```

```{toctree}
:hidden:
:caption: Machine learning

ML/Applied math.md
ML/Denoising Diffusion Probabilistic Models.md
ML/Dimensionality Reduction.md
ML/Introduction to Deep learning.md
ML/Sequence model.md
ML/Transformer.md
ML/VAE.md
ML/Variational Inference with Normalizing Flows.md
ML/Transfer learning.md
```

```{toctree}
:hidden:
:caption: ML for Materials
ML For Materials/Deep tensor neural network (DTNN).md
ML For Materials/GemNet Universal Directional Graph Neural Networks for Molecules.md
ML For Materials/JT-VAE_handwritten_derivation_view.md
ML For Materials/Junction Tree VAE.md
ML For Materials/Material informatics.md
ML For Materials/MolGAN An implicit generative model for small molecular graphs.md
ML For Materials/MolGPT.md
```

```{toctree}
:hidden:
:caption: Python
Python/Coding Practices.md
Python/creating-reading-and-writing_view.md
Python/Data visualization.md
Python/indexing-selecting-assigning_view.md
Python/Pandas.md
Python/Python Tutorial.md
```

[commonmark]: https://commonmark.org/
[github-ci]: https://github.com/Harrison-Li/Computational-materials-notes/workflows/continuous-integration/badge.svg?branch=main
[github-link]: https://github.com/Harrison-Li/Computational-materials-notes
[github-badge]: https://img.shields.io/github/stars/Harrison-Li/Computational-materials-notes?label=github
[site-link]: https://harrison-li.github.io/Computational-materials-notes/
[markdown-it-py]: https://markdown-it-py.readthedocs.io/
[markdown-it]: https://markdown-it.github.io/
[rst-to-myst]: https://rst-to-myst.readthedocs.io
