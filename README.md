# Sound Proofing Wizard

Expert soundproofing guides, honest product reviews, and step-by-step DIY tutorials.

**Live site:** https://brightlane.github.io/soundproofing/
**Affiliate:** TM Soundproofing (via LinkConnector)

## What This Builds

- **1,134 keyword pages** across 30+ categories
- **30 rotating blog posts** (daily AI-generated content via Claude API)
- **6 SVG infographics** rotating across all pages
- **15 essential pages** including homepage, FAQ, how-it-works, sitemap, llms.txt, RSS feed

## Features

- ✅ Daily AI blog via `ANTHROPIC_API_KEY` secret (falls back to static seed posts)
- ✅ All 6 rich schema types: Article, BreadcrumbList, FAQPage, HowTo, ItemList/AggregateRating, LocalBusiness
- ✅ 4-level breadcrumbs for geo pages (800 state + city pages)
- ✅ SearchAction schema on homepage
- ✅ TOC on every keyword page
- ✅ 8 rotating meta description variants
- ✅ 8 rotating buy-button texts (33 unique variants)
- ✅ 10 body variants + geo body (4 variants) + comparison body
- ✅ Noise level calculator in sidebar
- ✅ Share bar, author bar with microdata, trust badge
- ✅ Comprehensive llms.txt (14,000+ chars)
- ✅ Sitemap.xml with 1,173 URLs
- ✅ RSS feed with 20 items

## Setup

### 1. Create the repo

Create `brightlane/soundproofing` as a **public** repository.

### 2. Add files

Upload to repo root:
- `build.py` → `build.py`
- `deploy.yml` → `.github/workflows/deploy.yml` *(create the folders)*

### 3. Add API key secret

**Settings → Secrets and variables → Actions → New repository secret**

- Name: `ANTHROPIC_API_KEY`
- Value: your Anthropic API key

This enables daily AI-generated blog posts via Claude. Without it the build still works using static seed posts.

### 4. Enable GitHub Pages

**Settings → Pages → Source → GitHub Actions**

### 5. Deploy

Push any commit to `main`. The site builds and deploys in ~3 minutes.

## Daily Rebuild

The workflow runs at **6:00 AM UTC every day** via cron schedule. Each daily build:
1. Calls Claude API to generate a fresh soundproofing blog post on a rotating topic
2. Rotates blog post pool (30 posts, daily cycle)
3. Rebuilds all 1,179 pages with `dateModified: today`
4. Deploys fresh content automatically

## File Structure

```
build.py          ← Single-file static site generator
output/           ← Generated site (deployed to GitHub Pages)
  index.html
  guides/
    soundproofing-walls/index.html
    ... 1,133 more keyword pages
  blog/
    index.html
    rss.xml
    soundproofing-myths-debunked/index.html
    ... 29 more blog posts
  faq.html
  how-it-works.html
  about.html
  sitemap.xml
  robots.txt
  llms.txt
  og.svg
```

## Affiliate

All product links use:
```
https://www.linkconnector.com/ta.php?lc=007949109781007070&atid=TmSoundproofingWebImproved
```

Each page contains 11-12 affiliate link instances across: hero CTA, sidebar CTA, product grid (4 cards), noise calculator, bottom CTA, nav bar, footer.
