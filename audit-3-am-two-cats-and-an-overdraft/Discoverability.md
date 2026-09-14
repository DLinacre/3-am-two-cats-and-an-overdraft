# SEO, Search Engine Discoverability & Metadata Strategy
## Project: *David Linacre - 3 AM, Two Cats & An Overdraft* (2026)

---

## 1. Schema.org MusicAlbum JSON-LD Specification

To enable rich media snippets in Google Search:
```json
{
  "@context": "https://schema.org",
  "@type": "MusicAlbum",
  "name": "3 AM, Two Cats & An Overdraft (Studio Deluxe Edition)",
  "byArtist": {
    "@type": "MusicGroup",
    "name": "David Linacre"
  },
  "genre": "Lo-Fi Hip-Hop / 90s Boom-Bap / Bedroom Soul",
  "numTracks": 16,
  "datePublished": "2026-09-14",
  "image": "https://dlinacre.github.io/3-am-two-cats-and-an-overdraft/Cover.png",
  "url": "https://dlinacre.github.io/3-am-two-cats-and-an-overdraft/"
}
```

---

## 2. Crawler Access Configuration

- **`robots.txt`:** Allow all modern crawlers to index HTML, artwork, and liner notes while preventing excessive scraping of heavy MP4 binary containers.
- **`sitemap.xml`:** Declare canonical URLs for the root experience, individual lyrics, and press kit documentation.
