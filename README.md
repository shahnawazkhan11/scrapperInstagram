# Instagram Hashtag Video Scraper & Downloader

This project allows you to **automatically fetch and download Instagram videos** (posts or reels) from a given hashtag using `Selenium` and `yt_dlp`.



---

## 📌 Features

- Login to Instagram with your credentials using Selenium.
- Scrape video post/reel links from any public hashtag page.
- Download all videos using `yt_dlp`.
- Skips posts with no video or age restriction.
- Avoids redownloading already-downloaded videos using `downloaded.txt`.

---

## 🛠️ Requirements

- Python 3.x
- Chrome browser
- ChromeDriver (must match your Chrome version)

### Python Dependencies

```bash
pip install selenium yt_dlp
