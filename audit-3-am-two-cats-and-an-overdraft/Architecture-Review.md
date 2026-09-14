# Technical Architecture & Modernization Review
## Project: *David Linacre - 3 AM, Two Cats & An Overdraft* (2026)

---

## 1. Current Architecture Topology

The application operates as a client-side single-page multimedia player:

```mermaid
graph TD
    User([User Browser]) -->|HTTP GET| GH[GitHub Pages / Local Port 8089]
    GH --> HTML[index.html]
    HTML --> CSS[Embedded CSS3 Tokens]
    HTML --> JS[Embedded Player & Visualizer JS Engine]
    HTML --> Video[HTML5 Video Element]
    Video --> WebAudio[Web Audio API AnalyserNode]
    WebAudio --> Canvas[Canvas 2D Spectrum Visualizer]
    HTML --> Assets[Assets Directory]
    Assets --> Tracks[Track Artwork PNGs 1-16]
    Assets --> Lyrics[ALL_LYRICS.json]
    Assets --> Badges[Studio & Master Vector SVGs]
    HTML --> MP4s[Master 1080p MP4 Videos 01-16]
```

### Architectural Strengths
1. **Zero Runtime Dependencies:** Does not require React, Vue, Webpack, or Vite to function in production.
2. **Instant Cold Start:** Initial DOM loads in < 50ms over standard HTTP.
3. **Isolated Media Pipelines:** Media assets are self-contained with relative URIs.

### Architectural Bottlenecks
1. **Monolithic Inlining:** Marked by embedding 700+ lines of JavaScript and 400+ lines of CSS directly inside `index.html`.
2. **Data Model Triplication:** Track metadata is defined in `Tracklist.json`, mirrored inside `index.html`, and repeated in individual text files.

---

## 2. Recommended Modern Modular Architecture

```
/
├── index.html                  # Clean semantic HTML shell
├── manifest.json               # PWA Progressive Web App Manifest
├── css/
│   ├── main.css               # Design tokens & base styles
│   ├── player.css             # Transport controls & video layout
│   └── visualizer.css         # Canvas positioning & ambient glow
├── js/
│   ├── app.js                 # Entry point (ES module)
│   ├── tracks.js              # Tracklist state & dynamic fetcher
│   ├── player.js              # HTML5 media controller & hotkeys
│   ├── visualizer.js          # Web Audio API & Canvas spectrum loop
│   └── lyrics.js              # Lyric renderer & timecode sync
└── assets/
    ├── tracks/                # Track 01-16 Artworks
    ├── lyrics/                # Raw txt & consolidated ALL_LYRICS.json
    └── icons/                 # PWA icons & badges
```
