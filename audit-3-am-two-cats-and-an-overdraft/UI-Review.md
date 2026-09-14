# User Interface (UI) & Visual Design Review
## Project: *David Linacre - 3 AM, Two Cats & An Overdraft* (2026)

---

## 1. Color Palette & Design Tokens

The dark studio aesthetic captures the feeling of a late-night recording session:

```css
:root {
  --bg-primary: #08090d;           /* Deep midnight void */
  --bg-surface: #10121a;           /* Rack unit chassis */
  --bg-card: rgba(18, 22, 34, 0.75); /* Frosted studio glass */
  --bg-card-hover: rgba(30, 36, 54, 0.9);
  --accent: #f59e0b;               /* Warm vacuum tube amber */
  --accent-glow: rgba(245, 158, 11, 0.4);
  --accent-bright: #fbbf24;        /* Golden needle meter */
  --text-main: #f8fafc;            /* Crisp paper white */
  --text-muted: #94a3b8;           /* Faded console gray */
  --text-dim: #64748b;             /* Dim studio ambient */
  --border: rgba(255, 255, 255, 0.08);
  --border-accent: rgba(245, 158, 11, 0.35);
  --radius: 18px;
}
```

---

## 2. Typography Hierarchy

1. **Header & Body Font:** `Plus Jakarta Sans` (weights: 300, 400, 500, 600, 700, 800)
   - Provides clean, geometric, high-legibility modern styling.
2. **Metadata & Technical Font:** `JetBrains Mono` (weights: 400, 500, 600)
   - Accurately renders musical BPM, Keys (e.g. `D♭ Major`), durations (`02:20`), and audio format badges.

---

## 3. Visualizer Canvas Optimization

The visualizer canvas operates at the bottom of the video player window.
- **Bar Count:** 64 frequency bands derived from `analyser.frequencyBinCount` (fftSize: 128).
- **Gradient Fill:** Linear vertical gradient fading from `rgba(245, 158, 11, 0.95)` at peak down to `rgba(245, 158, 11, 0.05)` at baseline.
- **Recommended Polish:** Add subtle glow filter `ctx.shadowColor = 'rgba(245, 158, 11, 0.6)'` and `ctx.shadowBlur = 8` on high-transient kicks.
