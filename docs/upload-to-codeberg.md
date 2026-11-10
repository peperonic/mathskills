# Uploading to Codeberg

The zip file contains the whole repository, including its history (the hidden `.git` folder).

## 1. Create an empty repository on Codeberg

1. Sign in at https://codeberg.org.
2. Click **+** (top right), then **New repository**.
3. Name: `syllabus-ib`. Tick **Make repository private**.
4. Leave "Initialize repository" (README, .gitignore, licence) **unticked**: the repository must be empty.
5. Click **Create repository**.

## 2. Make an access token (once)

Codeberg does not accept your password for git. Instead:

1. **Settings** (your avatar, top right) > **Applications** > **Manage access tokens**.
2. Name it, for example `laptop`. Under permissions, set **repository** to **Read and write**.
3. Click **Generate token** and copy it somewhere safe; Codeberg shows it only once.

## 3. Upload with git (keeps the history)

Needs git (macOS: open Terminal and type `git`, it offers to install; Windows: https://git-scm.com).

```bash
unzip syllabus-ib.zip
cd syllabus-ib
git remote add origin https://codeberg.org/YOUR-USERNAME/syllabus-ib.git
git push -u origin main
```

When git asks: **Username** is your Codeberg username, **Password** is the token from step 2.

Refresh the repository page on Codeberg: the files and the commit history are there.

## Without git

On the empty repository page, choose **Upload file** and drag in the files. Folders must be recreated by hand (type the folder name in the path field before uploading its files), and the commit history is lost. The git route is much easier.

## Moving syllabus-de from GitHub

Codeberg can copy a GitHub repository with its history:

1. **+** > **New migration** > **GitHub**.
2. URL: `https://github.com/peperonic/syllabus-de`.
3. If the GitHub repository is private, paste a GitHub token with read access (GitHub: Settings > Developer settings > Personal access tokens).
4. Tick **Make repository private** if wanted, then **Migrate repository**.

Afterwards, archive or delete the GitHub copy so that only one place gets new work.
