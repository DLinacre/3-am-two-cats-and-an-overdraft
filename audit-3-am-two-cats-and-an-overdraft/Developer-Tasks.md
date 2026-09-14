# GitHub-Ready Developer Tasks & Implementation Issues
## Project: *David Linacre - 3 AM, Two Cats & An Overdraft* (2026)

---

### Task 01: Deploy Automated CI Workflow for Album Validation
- **Title:** `ci: implement GitHub Actions workflow for HTML, JS, and JSON validation`
- **Description:** Establish an automated GitHub Actions workflow (`.github/workflows/ci.yml`) that validates JSON syntax, checks for broken media links, and validates JavaScript syntax on every push and pull request.
- **Acceptance Criteria:**
  - Workflow runs on `push` and `pull_request` to `main`.
  - Executes `node tests/validate_album.test.js`.
  - Fails build if any JSON file is invalid or if `index.html` has syntax errors.
- **Priority:** 🔴 CRITICAL | **Effort:** S | **Owner:** DevOps

---

### Task 02: Implement Comprehensive WCAG 2.2 AA Accessibility Enhancements
- **Title:** `a11y: implement ARIA landmarks, focus rings, and reduced-motion controls`
- **Description:** Enhance `index.html` to achieve 100% WCAG 2.2 AA compliance for visually impaired users and screen-reader navigation.
- **Acceptance Criteria:**
  - All transport buttons have explicit `aria-label` tags.
  - Playlist container has `role="list"` and track items have `role="listitem"`.
  - `@media (prefers-reduced-motion: reduce)` halts canvas visualizer animations.
  - Golden high-contrast `:focus-visible` rings render on keyboard navigation.
- **Priority:** 🟠 HIGH | **Effort:** M | **Owner:** Frontend

---

### Task 03: Inject Schema.org MusicAlbum JSON-LD Structured Data
- **Title:** `seo: add Schema.org MusicAlbum and MusicRecording structured data`
- **Description:** Provide search engines with machine-readable metadata detailing David Linacre as artist, all 16 tracks, durations, and streaming links.
- **Acceptance Criteria:**
  - Google Rich Results Test validates JSON-LD without errors.
  - OpenGraph and Twitter Card preview tags verified.
- **Priority:** 🟠 HIGH | **Effort:** S | **Owner:** SEO
