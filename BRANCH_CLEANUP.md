# Branch Cleanup Report

## Stale Branches Pending Deletion (Already Merged)

The following branches have been fully merged and are no longer needed. Run the commands below as a repo admin to remove them:

| Branch | Merged Via | Status |
|--------|-----------|--------|
| `claude/add-stock-photos-IZh8T` | PR #5 | Merged — pending deletion |
| `claude/create-service-pillar-page-S1cCH` | PR #6 | Merged — pending deletion |
| `claude/create-service-pillar-page-pn6XB` | PR #8 | Merged — pending deletion |
| `tool` | direct merge | Merged — pending deletion |

### Delete Commands (run as repo admin)

```bash
git push origin --delete claude/add-stock-photos-IZh8T
git push origin --delete claude/create-service-pillar-page-S1cCH
git push origin --delete claude/create-service-pillar-page-pn6XB
git push origin --delete tool
```

Or via GitHub UI: **Settings → Branches** or on the Pull Requests page, click **Delete branch** next to each closed/merged PR.

## Branches to Keep (Active / Unmerged)

| Branch | Reason |
|--------|--------|
| `claude/create-service-pillar-page-beYuK` | Has unmerged commits |
| `claude/social-media-text-links-J4F4P` | Active |
| `claude/write-cleaning-blogs-tXNAH` | Active |
| `feature/blog-carousel-homepage` | Active |
| `main` | Remote default branch |
