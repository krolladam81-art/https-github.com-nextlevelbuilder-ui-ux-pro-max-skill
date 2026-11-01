# vermontjunk.com — multi-page site

A static site with **51 indexable pages**: a homepage, 16 service pages (estate
cleanouts, whole-house, demolition, construction debris, barns, vacation homes,
and more), 28 town pages, plus pricing, about, FAQ and contact. No framework and
nothing to install. Python 3 generates all of it.

```
site/
  build.py            ← run this to regenerate public/
  src/business.py     ← name, phone, guarantee, prices, tracking IDs (edit here first)
  src/services.py     ← all service page content
  src/towns.py        ← all town page content + real recent jobs
  src/styles.css, src/script.js
  public/             ← the generated website (what gets deployed)
  netlify.toml
```

```bash
python3 site/build.py
```

## How this follows the Google Ads / agency recommendations

| Recommendation | Where it lives |
|---|---|
| Measure the **whole** lead journey, not only calls from ads | `script.js` fires a conversion on every website phone tap, text tap and form submit (GA4 + Google Ads + dataLayer) |
| Push **booked customers** back to Google | The quote form stores `gclid` / `gbraid` / `wbraid` + UTMs for 90 days and sends them with every lead, ready for an offline-conversion upload |
| Focus on high-value work | Each priority service has its own page (estate, whole-house, demolition, C&D, barns, vacation homes), so ad groups can point to a matching landing page and not the homepage |
| Tight geo | Town pages cover only the towns in the ad campaigns and the 2026 job log |
| Meta = retargeting with proof and trust | Meta pixel slot (`meta_pixel_id`), plus trust content on every page (guarantee, insured, USDOT, woman-owned, real jobs) |
| Fix website conversion flow (SEO/CRO proposal) | A quote form above the fold, a sticky mobile Call/Text/Quote bar, and click-to-call on every page |

## Building trust with Google and AI assistants (ChatGPT, Claude, Perplexity, Gemini)

- **Same business details everywhere:** name, phone and service area all come from one file.
- **Structured data (JSON-LD) on every page:** LocalBusiness, Service, FAQPage, BreadcrumbList.
- **`/llms.txt`:** a plain-language fact sheet written for AI crawlers.
- **`robots.txt`:** explicitly lets GPTBot, ClaudeBot, PerplexityBot, Google-Extended and others crawl the site.
- **"At a glance" facts block and direct-answer FAQs:** short, quotable answers that AI tools tend to pull from.
- **Real price ranges and real recent jobs** (anonymized from the 2026 P&L). Specific, checkable facts carry more weight than marketing copy.
- **Each town page is genuinely different**, so Google won't treat them as doorway pages.

## Before launch — owner checklist

1. **Confirm the details in `src/business.py`:**
   - The price ranges, taken from the 2026 job log. You decide whether to publish them.
   - That "Adam & Lindsay / woman-owned" is worded the way you want.
   - The insurance wording.
2. **Fill in the TODOs in `src/business.py`:**
   - `founded_year`
   - `hours`
   - `google_reviews_url`
   - `google_rating` / `google_review_count`. Use only real numbers from your Google Business Profile; this turns on review stars in search results.
   - `same_as`: your Facebook, Instagram, Yelp, BBB and Nextdoor URLs. This is a big trust signal for AI assistants.
3. **Fill in the tracking IDs in `TRACKING`:**
   - GA4 ID
   - Google Ads ID, plus two conversion labels: website call and form
   - Meta Pixel ID
   - Then re-run `build.py`.
4. **Texting:** the "Text us photos" buttons open a text to 1-888-802-JUNK. Make sure SMS is enabled on that number (toll-free texting needs verification in Quo/OpenPhone). If it isn't, remove `sms_link` calls or point them at a local number.
5. **Google Business Profile:** set the website to `https://www.vermontjunk.com`. Make sure the business name, phone and service-area towns match this site exactly.
6. **Google Ads:** change Final URLs from the homepage to the matching page, for example:
   - Estate ad group → `/services/estate-cleanouts/`
   - Stratton & Bondville → `/junk-removal/stratton-vt/`
7. **Reviews:** never add made-up testimonials. Once real Google reviews exist, quote a few on the site with first name and town.
8. **Photos:** add real before/after job photos. They help conversion, Meta retargeting and AI image results.

## Deploy

**Netlify (recommended):**
- New site from this repo, with base directory `site`. `netlify.toml` handles the rest.
- The quote form works automatically through Netlify Forms. Submissions show up in the Netlify dashboard, and you can set up email notifications to info@vermontjunk.com.

**After deploy:**
- Point the vermontjunk.com DNS away from GoDaddy Website Builder to Netlify.
- Submit `https://www.vermontjunk.com/sitemap.xml` in Google Search Console and Bing Webmaster Tools.
- Add any old GoDaddy URLs to `public/_redirects`.
