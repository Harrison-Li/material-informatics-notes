# 📘 Jupyter Book Quick Commands

## Build & Preview

```bash
# Build the book
jupyter-book build .

# Clean previous builds
jupyter-book clean .

# Clean and rebuild
jupyter-book clean . && jupyter-book build .

# Open the book in browser (macOS)
open _build/html/index.html

# Open the book in browser (Linux)
xdg-open _build/html/index.html
```

## Common Tasks

### Add a New Page

1. Create your Markdown file (e.g., `new-topic.md`)
2. Add it to `_toc.yml`:
   ```yaml
   - file: path/to/new-topic
     title: Your Title
   ```
3. Rebuild: `jupyter-book build .`

### Update Configuration

Edit `_config.yml` then rebuild.

### Add Citations

1. Add BibTeX entries to `references.bib`
2. Cite in your markdown: `{cite}`keyname``
3. Add bibliography: `{bibliography}``

## Git Workflow

```bash
# After making changes
git add .
git commit -m "Update notes"
git push origin main

# GitHub Actions will automatically build and deploy
```

## URLs

- **Live Book**: https://harrison-li.github.io/Computational-materials-notes/
- **Repository**: https://github.com/Harrison-Li/Computational-materials-notes
- **GitHub Actions**: https://github.com/Harrison-Li/Computational-materials-notes/actions
