# Testing Strategy, Test Pyramid & Automated Validation
## Project: *David Linacre - 3 AM, Two Cats & An Overdraft* (2026)

---

## 1. Test Pyramid Overview

```
      /\
     /E2E\      Browser Subagent Playback Tests (Play/Pause, Visualizer)
    /------\
   / Integr \    Audio / Video File Integrity & URL Encoding Checks
  /----------\
 / Unit Tests \   JSON Validation, Lyrics Mapping, Syntax Checks
/--------------\
```

---

## 2. Automated Test Suite (`validate_album.test.js`)

A lightweight Node.js test script executes on CI and pre-commit:
1. Validates `Tracklist.json` schema and ensures all 16 tracks have valid Keys, BPMs, and titles.
2. Checks that every track referenced in `tracks` points to a valid file on disk or valid remote URI.
3. Verifies that `ALL_LYRICS.json` contains full verses for all 16 tracks.
4. Validates that `index.html` contains 0 JavaScript syntax errors.
