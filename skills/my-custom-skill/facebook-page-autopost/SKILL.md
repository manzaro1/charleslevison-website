---
name: facebook-page-autopost
description: Auto-post image + caption to a Facebook Page using the Facebook Graph API (official).
homepage: https://developers.facebook.com/docs/graph-api/
metadata:
  clawdbot:
    emoji: "📘"
    requires:
      bins: ["node", "npm"]
    install: |
      This skill uses Node.js.
      Install dependencies:
        cd skills/facebook-page-autopost
        npm i
---

# facebook-page-autopost

Auto-post a photo + caption to a **Facebook Page** using the **Facebook Graph API**.

## What you need (one-time)

1. A Facebook **Page** you manage.
2. A Meta Developer app (or use Graph API Explorer) to obtain a **Page Access Token** with permissions appropriate for publishing.
3. Your **Page ID**.

> Note: Meta permissions and review requirements can change. If token creation fails, use Meta docs / Graph API Explorer to confirm the latest requirements.

## Configure

You can configure via either **system environment variables** or a local `.env` file.

### Option A: `.env` (recommended)

1. Copy `.env.example` to `.env`:
   - `cp skills/facebook-page-autopost/.env.example skills/facebook-page-autopost/.env`
2. Edit `skills/facebook-page-autopost/.env` and set:
   - `FB_PAGE_ID`
   - `FB_PAGE_ACCESS_TOKEN`
   - (optional) `FB_API_VERSION` (default: `v19.0`)

### Option B: system env vars

- `FB_PAGE_ID` (e.g. `123456789012345`)
- `FB_PAGE_ACCESS_TOKEN` (long-lived if possible)
- Optional: `FB_API_VERSION` (default: `v19.0`)

## Prepare posts

Create files under `skills/facebook-page-autopost/posts/`.

Each post is a pair:
- `YYYY-MM-DD.txt` caption text
- `YYYY-MM-DD.jpg` (or .png) image

Example:
- `posts/2026-02-22.txt`
- `posts/2026-02-22.jpg`

## Run manually

From workspace root:

```bash
node skills/facebook-page-autopost/scripts/post_today.js
```

## Schedule daily at 9:00am

Use PicoClaw `cron` to run the command daily at 09:00.

Example cron message (the agent will set this up for you):
- Command: `node .../post_today.js`

## Output

- On success: prints the created post ID and marks the post as sent by renaming files with `.sent` suffix.
- On failure: exits non-zero and prints the API error.
