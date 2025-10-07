# Jupyter Book Setup Guide

This repository is configured to publish your lecture notes as a web-based book using Jupyter Book and GitHub Pages.

## 🚀 Quick Start

### Local Setup

1. **Install Jupyter Book** (if not already installed):
   ```bash
   pip install -U jupyter-book ghp-import
   ```

2. **Build the book locally**:
   ```bash
   jupyter-book build .
   ```

3. **View the book**:
   Open `_build/html/index.html` in your browser, or run:
   ```bash
   open _build/html/index.html  # macOS
   ```

### Publishing to GitHub Pages

#### First Time Setup

1. **Enable GitHub Pages** for your repository:
   - Go to your repository on GitHub
   - Navigate to `Settings` → `Pages`
   - Under "Build and deployment":
     - Source: Select `GitHub Actions`
   - Save the settings

2. **Push your changes**:
   ```bash
   git add .
   git commit -m "Setup Jupyter Book"
   git push origin main
   ```

3. **Wait for deployment**:
   - Go to the `Actions` tab in your GitHub repository
   - Watch the "Deploy Jupyter Book to GitHub Pages" workflow
   - Once complete, your book will be available at:
     `https://harrison-li.github.io/Computational-materials-notes/`

#### Automatic Deployment

Once set up, every push to the `main` branch will automatically rebuild and deploy your book!

## 📝 Customization

### Editing the Table of Contents

Edit `_toc.yml` to change the structure of your book:
- Add/remove chapters
- Reorganize sections
- Change titles

### Editing Book Configuration

Edit `_config.yml` to customize:
- Book title and author
- Theme and styling
- Math rendering options
- Repository links

### Adding New Content

1. Add your Markdown files to the appropriate folder
2. Update `_toc.yml` to include the new file
3. Build and deploy

## 🎨 Features Enabled

- ✅ **Math Support**: LaTeX equations with MathJax
- ✅ **MyST Markdown**: Enhanced markdown features
- ✅ **Code Highlighting**: Syntax highlighting for code blocks
- ✅ **Citations**: BibTeX support (add references to `references.bib`)
- ✅ **GitHub Integration**: Links to edit pages and open issues
- ✅ **Search**: Full-text search functionality
- ✅ **Responsive Design**: Mobile-friendly layout

## 📚 Learn More

- [Jupyter Book Documentation](https://jupyterbook.org/)
- [MyST Markdown Guide](https://myst-parser.readthedocs.io/)
- [Sphinx Book Theme](https://sphinx-book-theme.readthedocs.io/)

## 🐛 Troubleshooting

### Build Errors

If you encounter build errors:

1. Check that all files referenced in `_toc.yml` exist
2. Ensure Markdown files have proper formatting
3. Check the build logs in GitHub Actions

### Math Not Rendering

- Ensure you're using proper LaTeX syntax
- Use `$...$` for inline math
- Use `$$...$$` for display math

### Images Not Showing

- Use relative paths from the root directory
- Example: `![alt text](ML/assets/image-name.png)`

## 🤝 Contributing

Feel free to open issues or submit pull requests to improve the notes!
