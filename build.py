import os
import shutil
from pathlib import Path

def create_build():
    # Create build directory
    build_dir = Path('build')
    
    # Remove existing build directory if it exists
    if build_dir.exists():
        shutil.rmtree(build_dir)
    
    # Create new build directory
    build_dir.mkdir()
    
    # Copy index.html
    shutil.copy2('index.html', build_dir / 'index.html')
    
    # Copy images directory
    if Path('images').exists():
        shutil.copytree('images', build_dir / 'images')
    
    # Create _redirects file for Render
    with open(build_dir / '_redirects', 'w') as f:
        f.write('/*    /index.html   200\n')
    
    print('Build completed successfully!')
    print('Files copied to build/ directory')
    
    # List contents of build directory
    print('\nBuild directory contents:')
    for item in build_dir.iterdir():
        print(f"  {item.name}")

if __name__ == '__main__':
    create_build()
