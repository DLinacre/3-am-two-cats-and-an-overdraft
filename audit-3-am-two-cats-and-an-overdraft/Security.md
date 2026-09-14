# Defensive Security & Privacy Audit
## Project: *David Linacre - 3 AM, Two Cats & An Overdraft* (2026)

---

## 1. Threat Modeling & Attack Surface

The application is statically hosted on GitHub Pages:
- **No Server-Side Scripts:** Zero SQL injection or remote code execution risks.
- **Zero Third-Party Trackers:** No analytics beacons, tracking cookies, or advertising SDKs.
- **Client-Side Secrets:** No API keys or credentials exposed in client-side bundles.

---

## 2. Hardening Measures Implemented

1. **Content Security Policy (CSP):**
   ```html
   <meta http-equiv="Content-Security-Policy" content="default-src 'self'; script-src 'self' 'unsafe-inline'; style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; font-src 'self' https://fonts.gstatic.com; media-src 'self'; img-src 'self' data:;">
   ```
2. **Subresource Hygiene:** External fonts locked to secure Google CDN endpoints with preconnect directives.
3. **Security Policy:** Added `SECURITY.md` defining response protocols for reported defects.
