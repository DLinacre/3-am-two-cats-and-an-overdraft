# Assumptions, Verifiable Evidence & Identified Gaps
## Project: *David Linacre - 3 AM, Two Cats & An Overdraft* (2026)

---

## 1. Verified Facts (Ground Truth from Repository & Environment)

1. **Hardware & Environment:**
   - Operating System: Windows 11 on host workstation.
   - Storage: Local album directory located at `D:\Desktop\David Linacre - 3 AM, Two Cats & An Overdraft (2026) [Deluxe Edition]` (NTFS junctioned to `C:\Users\KingL\Desktop\...`).
   - GPU: NVIDIA GeForce RTX 3070 Ti (8GB VRAM), actively running ComfyUI neural diffusion.
2. **Audio/Video Media Files (As of September 14, 2026):**
   - Tracks 01 through 10 are completely rendered as 1080p MP4 files with real-time waveform visualizers and mastered 320 kbps AAC audio.
   - File sizes range between 10 MB and 25 MB per track.
   - Tracks 11 through 16 are queued in the autonomous pipeline (`run_album_autonomous_pipeline.py`).
3. **Repository & Hosting:**
   - GitHub Repository: `https://github.com/DLinacre/3-am-two-cats-and-an-overdraft`
   - Active Branch: `main`
   - Live Deployment: GitHub Pages at `https://dlinacre.github.io/3-am-two-cats-and-an-overdraft/`
   - Local Web Server: Python HTTP server on port 8089 (`http://localhost:8089/`).
4. **Art Assets:**
   - 16 custom square track covers (`assets/tracks/Track_01.png` through `Track_16.png`).
   - High-res master album cover (`Cover.png`) and landscape banners (`banner.png`, `assets/github_banner.png`).
   - Vector badges: `studio_master_badge.svg`, `golden_era_badge.svg`, `two_cats_icon.svg`.

---

## 2. Unverifiable Items & Explicit Gaps

1. **External Commercial Metrics:**
   - *Status:* **Not currently verifiable from available evidence.**
   - *Details:* Spotify/Apple Music stream counts, sales figures, Patreon subscriber numbers, or ad revenue are not tracked in this repository.
2. **Third-Party Copyright Clearances:**
   - *Status:* **Not currently verifiable from available evidence.**
   - *Details:* All vocals and musical backings are generated via local neural diffusion (MiniMax Music 3 DiT) with original lyrical prompts written by David Linacre. Commercial distribution rights depend on the underlying model's open weights license.
3. **User Engagement Analytics:**
   - *Status:* **Not currently verifiable from available evidence.**
   - *Details:* `index.html` currently contains zero telemetry, Google Analytics, or tracking cookies, preserving 100% user privacy.
