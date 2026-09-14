# Contributing Guidelines

Thank you for your interest in contributing to **David Linacre - 3 AM, Two Cats & An Overdraft**!

## Ways to Contribute
1. **Bug Reports:** If you spot an issue with player playback, responsive sizing, audio visualizers, or lyric display, open an issue using the [Bug Report Template](.github/ISSUE_TEMPLATE/bug_report.yml).
2. **Lyric Suggestions & Corrections:** Notice an acoustic transcription discrepancy? Feel free to submit a pull request against `assets/lyrics/`.
3. **Accessibility Enhancements:** We are committed to maintaining WCAG 2.2 AA compliance. PRs improving screen reader UX, keyboard navigation, or color contrast are warmly welcomed.

## Development & Testing
Before submitting a PR:
```bash
# Run automated validation suite
node tests/validate_album.test.js
```
Ensure that all tests pass without errors.
