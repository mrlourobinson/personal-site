# Screenshot Tool for Projects

This Python script takes full-page screenshots of all URLs listed in `projects.json` at both desktop (1100px) and mobile (iPhone 14) sizes.

## Setup

1. Install Python dependencies:
```bash
pip install -r requirements.txt
```

2. Install Playwright browsers:
```bash
playwright install chromium
```

## Usage

Simply run the script:
```bash
python screenshot_urls.py
```

The script will:
- Read all URLs from `projects.json`
- Create a `screenshots/` directory with two subdirectories:
  - `screenshots/desktop/` - Desktop screenshots (1100px wide)
  - `screenshots/mobile/` - Mobile screenshots (iPhone 14 size: 390x844)
- Save each screenshot with the URL slug as the filename

For example, the URL:
```
https://edition.cnn.com/interactive/2025/08/05/world/north-korea-it-worker-scheme-vis-intl-hnk/index.html
```

Will be saved as:
- `screenshots/desktop/north-korea-it-worker-scheme-vis-intl-hnk.png`
- `screenshots/mobile/north-korea-it-worker-scheme-vis-intl-hnk.png`

## Features

- **Full-page screenshots**: Captures the entire scrollable page, not just the viewport
- **Lazy-load triggering**: Scrolls to the bottom to trigger lazy-loaded content, then back to top
- **Cookie banner removal**: Automatically detects and removes cookie consent popups
- **Extended load times**: Waits for content to fully load including embedded graphics
- **Network idle waiting**: Waits for network activity to settle before capturing
- **Mobile emulation**: Properly emulates iPhone 14 with touch support and correct user agent
- **Error handling**: Continues processing if individual URLs fail
- **Progress tracking**: Shows real-time progress as it processes each URL

## Configuration

You can modify viewport sizes in the script:
- Desktop: `desktop_viewport` (default: 1100x800)
- Mobile: `mobile_viewport` (default: 390x844 for iPhone 14)

