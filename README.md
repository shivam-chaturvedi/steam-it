# STEAM IT Foundation Website

## Deployment Instructions for Render

### Prerequisites
- A Render account
- This repository pushed to GitHub/GitLab
- Python 3.x (for build process)

### Deployment Steps

1. **Connect Repository to Render:**
   - Go to [Render Dashboard](https://dashboard.render.com/)
   - Click "New +" and select "Static Site"
   - Connect your GitHub/GitLab repository

2. **Configure Build Settings:**
   - **Build Command:** `python build.py`
   - **Publish Directory:** `build`
   - **Environment:** Static Site

3. **Alternative: Use render.yaml**
   - The included `render.yaml` file will automatically configure your deployment
   - Simply connect your repository and Render will use these settings

### Local Development

To test the build locally:

```bash
# Run build
python build.py

# Test locally (Python 3)
python -m http.server 8000

# Or if you have npm
npm run build
npm run dev
```

### Project Structure

```
├── build/              # Generated build folder (auto-created)
├── images/             # Static images
├── index.html          # Main HTML file
├── package.json        # Node.js configuration
├── build.py           # Python build script (recommended)
├── build.js           # Node.js build script (alternative)
├── build.sh           # Build script for Unix/Linux
├── build.bat          # Build script for Windows
├── render.yaml        # Render deployment configuration
├── .gitignore         # Git ignore file
└── README.md          # This file
```

### Build Process

The build process:
1. Creates a `build/` directory
2. Copies `index.html` to the build folder
3. Copies the entire `images/` folder to the build folder
4. Creates a `_redirects` file for proper routing on Render

### Notes

- The site uses Tailwind CSS via CDN, so no compilation is needed
- All fonts are loaded from Google Fonts CDN
- The build folder contains a complete static site ready for deployment
