# GitHub Setup Instructions

Follow these steps to publish your OpenAI Agents SDK Jokester project to GitHub.

## Step 1: Create GitHub Repository

1. Go to [GitHub](https://github.com) and log in
2. Click the **+** icon in the top right, select **New repository**
3. Configure your repository:
   - **Repository name**: `openai-agents-jokester`
   - **Description**: "A lightweight demonstration of the OpenAI Agents SDK"
   - **Visibility**: Public (for portfolio) or Private
   - **DO NOT** initialize with README, .gitignore, or license (we have these)
4. Click **Create repository**

## Step 2: Initialize Local Git Repository

Open terminal in your project directory and run:

```bash
# Initialize git repository
git init

# Add all files
git add .

# Make initial commit
git commit -m "Initial commit: OpenAI Agents SDK Jokester project"

# Add remote (replace with your actual repository URL)
git remote add origin https://github.com/csg09/openai-agents-jokester.git

# Push to GitHub
git branch -M main
git push -u origin main
```

## Step 3: Verify Upload

1. Refresh your GitHub repository page
2. Verify all files are present:
   - ✓ jokester.py
   - ✓ advanced_example.py
   - ✓ README.md
   - ✓ requirements.txt
   - ✓ .gitignore
   - ✓ LICENSE
   - ✓ And other files...

3. **Important**: Check that `.env` is NOT visible (it should be ignored)

## Step 4: Customize Repository Settings

### Add Topics
1. Go to your repository page
2. Click the ⚙️ (settings gear) next to **About**
3. Add topics: `openai`, `agents`, `python`, `ai`, `machine-learning`, `sdk`

### Update README
Replace `[Your Name]` in LICENSE with your actual name

### Create a GitHub Project Link
Add this to your portfolio/resume:
```
github.com/csg09/openai-agents-jokester
```

## Step 5: Optional Enhancements

### Add Repository Description
In the **About** section, add:
- Description: "Lightweight demonstration of OpenAI Agents SDK"
- Website: Link to documentation or your portfolio
- Topics: Add relevant tags

### Enable GitHub Pages (Optional)
If you want to create a documentation site:
1. Go to Settings → Pages
2. Select source: Deploy from a branch
3. Choose `main` branch and `/docs` or `/root`

### Add Social Preview Image
Create a nice preview image (1280x640 px) showing your project:
1. Go to Settings
2. Scroll to Social preview
3. Upload image

## Troubleshooting

### "Remote origin already exists"
```bash
git remote remove origin
git remote add origin https://github.com/csg09/openai-agents-jokester.git
```

### ".env file is showing on GitHub"
If you accidentally committed `.env`:
```bash
# Remove from git tracking
git rm --cached .env

# Commit the removal
git commit -m "Remove .env from tracking"

# Push changes
git push
```

Then go to GitHub → Settings → Secrets and add `OPENAI_API_KEY` there instead.

### "Permission denied (publickey)"
Set up SSH keys or use HTTPS with personal access token:
```bash
git remote set-url origin https://github.com/csg09/openai-agents-jokester.git
```

## Next Steps

1. **Test Clone**: Clone your repo in a new directory to verify setup works
2. **Add to Portfolio**: Include link in your portfolio/resume
3. **Share**: Share your project on LinkedIn, Twitter, etc.
4. **Iterate**: Continue improving and updating as you learn more

## Security Reminder

🚨 **NEVER commit these to GitHub:**
- `.env` file with real API keys
- `__pycache__/` directories
- Virtual environment folders (`venv/`, `env/`)
- Personal credentials or tokens

Your `.gitignore` file protects you, but always double-check!

---

**Congratulations!** Your project is now on GitHub and ready to showcase! 🎉
