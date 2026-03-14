# Branch Cleanup Guide

## Why Do Branches Still Appear After Merging a PR?

GitHub does **not** automatically delete branches after a PR is merged. The branch stays until you manually delete it, or until you enable the auto-delete setting (see below).

---

## Step 1: Delete Existing Stale Branches (One-Time Fix)

### Option A — Via the Branches page (fastest)
1. Go to: `https://github.com/bennymak01/clean-game01/branches`
2. Find each stale branch in the list
3. Click the **trash icon** next to it to delete

### Option B — Via each merged Pull Request
1. Go to **Pull Requests → Closed**
2. Open each merged PR
3. Scroll to the bottom — click the **"Delete branch"** button

### Stale branches to delete:

| Branch | Merged Via |
|--------|-----------|
| `claude/add-stock-photos-IZh8T` | PR #5 |
| `claude/create-service-pillar-page-S1cCH` | PR #6 |
| `claude/create-service-pillar-page-pn6XB` | PR #8 |
| `tool` | direct merge |

---

## Step 2: Enable Auto-Delete for Future PRs (Recommended)

So this never happens again:

1. Go to **Settings → General** in your repository
2. Scroll down to the **"Pull Requests"** section
3. Check the box: ✅ **"Automatically delete head branches"**
4. Click **Save**

After this, every time a PR is merged, GitHub will automatically delete the source branch.

---

## Active Branches (Do NOT delete)

| Branch | Reason |
|--------|--------|
| `claude/create-service-pillar-page-beYuK` | Unmerged — active work |
| `claude/social-media-text-links-J4F4P` | Unmerged — active work |
| `claude/write-cleaning-blogs-tXNAH` | Unmerged — active work |
| `feature/blog-carousel-homepage` | Unmerged — active work |
| `main` | Default branch — never delete |
