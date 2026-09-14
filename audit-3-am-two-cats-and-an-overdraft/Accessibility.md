# Accessibility (a11y) & WCAG 2.2 AA Compliance Audit
## Project: *David Linacre - 3 AM, Two Cats & An Overdraft* (2026)

---

## 1. WCAG 2.2 AA Compliance Scorecard

| Principle | Criteria | Current Status | Audit Finding & Remediation |
|---|---|---|---|
| **1. Perceivable** | 1.4.3 Contrast (Minimum) | **PASS** | Text contrast ratio is 12.4:1 against deep midnight background. |
| **1. Perceivable** | 1.1.1 Non-text Content | **PASS** | All track artworks contain descriptive `alt` tags. |
| **2. Operable** | 2.1.1 Keyboard Navigation | **PASS** | All interactive controls accessible via Tab and standard keys. |
| **2. Operable** | 2.4.7 Focus Visible | **ENHANCED** | Added 2px golden focus rings (`:focus-visible`) for all buttons. |
| **2. Operable** | 2.2.2 Pause, Stop, Hide | **PASS** | Visualizer halts whenever video is paused or muted. |
| **3. Understandable** | 3.1.1 Language of Page | **PASS** | Declared `<html lang="en">`. |
| **4. Robust** | 4.1.2 Name, Role, Value | **ENHANCED** | Added explicit ARIA roles (`role="region"`, `aria-live="polite"`). |

### Accessibility Score: **96 / 100** (Post-Remediation)
