# PyPI Publishing Setup Guide

## Step 1: Setup TestPyPI Trusted Publisher (OIDC)

Go to https://test.pypi.org/manage/account/publishing/

### Add Pending Publisher

Fill in the form with:

- **TestPyPI Project Name**: `boilerpy`
- **Owner**: `Faizgeeky`
- **Repository name**: `boilerpy`
- **Workflow name**: `publish.yml`
- **Environment name**: `testpypi`

Click "Add" to save.

## Step 2: Setup Real PyPI Trusted Publisher

Go to https://pypi.org/manage/account/publishing/

### Add Pending Publisher

Fill in the same details:

- **PyPI Project Name**: `boilerpy`
- **Owner**: `Faizgeeky`
- **Repository name**: `boilerpy`
- **Workflow name**: `publish.yml`
- **Environment name**: `pypi`

Click "Add" to save.

## Step 3: Create GitHub Environments

Go to your repo settings: https://github.com/Faizgeeky/boilerpy/settings/environments

### Create TestPyPI Environment

1. Click "New environment"
2. Name: `testpypi`
3. Click "Configure environment"
4. (Optional) Add protection rules if you want

### Create PyPI Environment

1. Click "New environment"
2. Name: `pypi`
3. Click "Configure environment"
4. Add protection rule: "Required reviewers" (yourself)
   - This ensures you manually approve before publishing to real PyPI

## Step 4: Create a GitHub Release

Once trusted publishers are set up, publish your package:

```bash
# Create a git tag
git tag v0.1.0
git push origin v0.1.0
```

Then go to GitHub: https://github.com/Faizgeeky/boilerpy/releases/new

1. Choose tag: `v0.1.0`
2. Release title: `v0.1.0 - Initial Release`
3. Description:
   ```markdown
   ## 🎉 Initial Release

   ### Features
   - ✨ Interactive FastAPI project scaffolding
   - 🚀 3 production-ready templates (API, Auth, SQL)
   - 📦 Clean architecture with best practices
   - 🎯 Simple CLI: `bpy init fastapi`

   ### Installation
   ```bash
   pip install boilerpy
   # or
   pipx install boilerpy
   ```

   ### Usage
   ```bash
   bpy list              # List templates
   bpy init fastapi      # Create new project
   ```
   ```

4. Click "Publish release"

This will automatically trigger the GitHub Actions workflow that will:
1. Build the package
2. Publish to TestPyPI (automatic)
3. Wait for your approval
4. Publish to real PyPI (after approval)

## Step 5: Manual Publishing (Alternative)

If you prefer to publish manually without GitHub Actions:

```bash
# Install tools
pip install build twine

# Build package
python -m build

# Upload to TestPyPI first
twine upload --repository testpypi dist/*

# Test installation
pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ boilerpy

# If it works, upload to real PyPI
twine upload dist/*
```

## Summary

**Automatic (Recommended):**
1. Setup trusted publishers on TestPyPI and PyPI
2. Create GitHub environments
3. Create a git tag and GitHub release
4. GitHub Actions handles everything

**Manual:**
1. Build with `python -m build`
2. Upload with `twine upload dist/*`

Choose whichever method you prefer!
