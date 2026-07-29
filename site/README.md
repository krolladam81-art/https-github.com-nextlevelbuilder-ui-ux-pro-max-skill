# Vermont Junk Removal & Hauling — Website

Single-page static site (no build step). Open `index.html` directly in a
browser, or serve the `site/` folder with any static host (Netlify, GitHub
Pages, S3, etc.).

## Before you launch

1. **Drop in your real logo**: save it as `site/assets/logo.png` (square,
   transparent background works best, 500×500px+). The page already points
   at that path — until the file exists it falls back to a CSS-drawn
   placeholder that mimics your license-plate mark.
2. **Phone number**: replace every `(802) 555-0192` / `+18025550192`
   placeholder in `index.html` with your real number (search-and-replace
   both the display text and the `tel:` / `sms:` links).
3. **Email**: replace `hello@vermontjunk.com` in the footer.
4. **Pricing**: the numbers in the Pricing section ($89 / $219 / $399) are
   placeholders — set them to your real starting prices.
5. **Service area towns**: edit the `<ul class="town-list">` list to match
   where you actually run routes.
6. **Reviews**: swap the three placeholder testimonials for real customer
   quotes once you have them (never publish invented reviews as real).

## Structure

- `index.html` — all page content/sections
- `styles.css` — design tokens (colors/fonts/spacing) + layout, light/dark aware
- `script.js` — sets the footer copyright year
- `assets/favicon.svg` — placeholder tab icon
- `assets/logo.png` — **add this yourself**, your real logo goes here
