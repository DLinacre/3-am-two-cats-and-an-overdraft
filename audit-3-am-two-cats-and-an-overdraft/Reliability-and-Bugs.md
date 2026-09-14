# Reliability, Defect Tracker & Bug Remediation
## Project: *David Linacre - 3 AM, Two Cats & An Overdraft* (2026)

---

## Defect Matrix

### Defect 01: Critical Inline Script Parsing Crash
- **Severity:** 🔴 **CRITICAL**
- **Evidence:** Browser console error `Uncaught SyntaxError: Invalid or unexpected token` on line 21; playlist remained empty.
- **Root Cause:** Raw literal newlines inside double-quoted JavaScript string literals in `lyricsData`.
- **Remediation:** Replaced inline string literals with properly escaped JSON serialization. Validated with `new Function()`.
- **Validation:** 100% verified locally on port 8089 and live on GitHub Pages.

### Defect 02: Markdown Unicode Character Corruption
- **Severity:** 🟡 **MEDIUM**
- **Evidence:** `README.md` contained corrupted section headers `## ?? About the Album`.
- **Root Cause:** PowerShell script writing UTF-8 output using default Windows code page without UTF-8 encoding flag.
- **Remediation:** Re-encoded all documentation using explicit UTF-8 encoding.
- **Validation:** Clean header rendering verified in GitHub markdown viewer.

### Defect 03: Video Fallback on Unrendered Tracks
- **Severity:** 🟠 **HIGH**
- **Evidence:** Clicking an in-progress track (Tracks 11–16) halted playback without feedback.
- **Root Cause:** Absence of `<video>` error event listeners.
- **Remediation:** Added `video.addEventListener('error')` fallback to track 01 with an informative UI banner.
- **Validation:** Smooth fallback verified via automated browser testing.
