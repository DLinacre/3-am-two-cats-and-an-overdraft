# User Experience (UX) & Interaction Audit
## Project: *David Linacre - 3 AM, Two Cats & An Overdraft* (2026)

---

## 1. Journey Analysis & Friction Points

### Journey 1: First-Time Visitor Onboarding
- **Current Experience:** User visits URL; player loads with Track 01 active. Audio requires a user click due to browser autoplay policies.
- **Problem:** If a user clicks play without interacting with the audio context first, the Web Audio API audio graph may remain suspended in Safari/Chrome.
- **Recommended Experience:** Provide a prominent, warm, inviting "Enter Studio (3 AM)" overlay modal on first visit that unlocks the AudioContext with full user intent, immediately starting the rain and Rhodes intro.

### Journey 2: Track Switching & Discovery
- **Current Experience:** Clicking any track row instantly switches the video source and renders the lyrics.
- **Problem:** If a track is clicked while in studio synthesis, the previous build showed no visual indication of why audio did not immediately play.
- **Recommended Experience:** Clearly differentiate between `Mastered` and `In Studio` tracks with color-coded status badges, and provide smooth crossfades between songs.

### Journey 3: Lyric Reading & Sing-Along
- **Current Experience:** Tab toggle switches the sidebar from playlist to plain text lyrics.
- **Problem:** The lyric block is a single static text container requiring manual vertical scrolling.
- **Recommended Experience:** Add auto-scroll or karaoke-style highlight highlighting current verse blocks as the timecode advances.

---

## 2. Keyboard & Touch Ergonomics

| Key / Control | Current State | UX Assessment | Modernization Recommendation |
|---|---|---|---|
| `Space` | Play / Pause | Intuitive | Preserve |
| `Arrow Right` | Skip +5 sec | Responsive | Add +10s on Shift+Right |
| `Arrow Left` | Back -5 sec | Responsive | Add -10s on Shift+Left |
| `M` | Mute Toggle | Functional | Add smooth volume slider |
| `F` | Fullscreen | Functional | Ensure exit prompt is clean |
| `L` | Toggle Lyrics | Functional | Add auto-focus to active lyric line |
| `1`–`9` | Not Mapped | Opportunity | Map numbers 1-9 to direct track shortcuts |
