#!/bin/bash

# Script to build and preview Jupyter Book locally

echo "🔨 Building Jupyter Book..."
jupyter-book build .

if [ $? -eq 0 ]; then
    echo "✅ Build successful!"
    echo "🌐 Opening book in browser..."
    
    # Detect OS and open accordingly
    if [[ "$OSTYPE" == "darwin"* ]]; then
        # macOS
        open _build/html/index.html
    elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
        # Linux
        xdg-open _build/html/index.html
    else
        echo "📂 Please open _build/html/index.html in your browser"
    fi
else
    echo "❌ Build failed. Please check the errors above."
    exit 1
fi
