#!/usr/bin/env python3
"""Static site generator for vermontjunk.com — no dependencies.

    python3 site/build.py          # writes everything into site/public/

Edit content in site/src/{business,services,towns}.py, then re-run.
"""
import json
import shutil
import sys
from datetime import date
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "src"))

from business import BUSINESS as B, SITE_URL, TRACKING, TRUST_POINTS, PRICE_RANGES  # noqa: E402
from services import SERVICES, SERVICE_BY_SLUG  # noqa: E402
from towns import TOWNS, TOWN_BY_SLUG, TIER_COPY  # noqa: E402

OUT = ROOT / "public"
TODAY = date.today().isoformat()
BIZ_ID = f"{SITE_URL}/#business"


def e(s):
    return escape(str(s), quote=True)


# ------------------------------------------------------------------ icons
ICONS = {
    "phone": '<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z"/>',
    "check": '<path d="M20 6 9 17l-5-5"/>',
    "clock": '<circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/>',
    "shield": '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="m9 12 2 2 4-4"/>',
    "truck": '<path d="M10 17h4V5H2v12h3"/><path d="M14 8h4l4 4v5h-3"/><circle cx="7.5" cy="17.5" r="2.5"/><circle cx="16.5" cy="17.5" r="2.5"/>',
    "home": '<path d="m3 10 9-7 9 7v10a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><path d="M9 22V12h6v10"/>',
    "leaf": '<path d="M11 20A7 7 0 0 1 9.8 6.1C15.5 5 17 4.5 19 2c1 2 2 4.2 2 8 0 5.5-4.8 10-10 10z"/><path d="M2 21c0-3 1.9-5.4 5.1-6"/>',
    "hammer": '<path d="m15 12-8.5 8.5a2.1 2.1 0 0 1-3-3L12 9"/><path d="M17.6 15 22 10.6l-4.6-4.6-1.4 1.4-2-2L12.6 4 10 6.6l2 2-1.4 1.4z"/>',
    "pin": '<path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0z"/><circle cx="12" cy="10" r="3"/>',
    "msg": '<path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>',
    "arrow": '<path d="M5 12h14"/><path d="m12 5 7 7-7 7"/>',
    "dollar": '<path d="M12 2v20"/><path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/>',
    "users": '<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.9"/><path d="M16 3.1a4 4 0 0 1 0 7.8"/>',
    "box": '<path d="M21 8 12 3 3 8v8l9 5 9-5z"/><path d="m3 8 9 5 9-5"/><path d="M12 13v8"/>',
    "star": '<path d="m12 2 3.1 6.3 6.9 1-5 4.9 1.2 6.8L12 17.8 5.8 21l1.2-6.8-5-4.9 6.9-1z"/>',
    "camera": '<path d="M14.5 4h-5L7 7H4a2 2 0 0 0-2 2v9a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V9a2 2 0 0 0-2-2h-3z"/><circle cx="12" cy="13" r="3"/>',
    "menu": '<path d="M4 6h16M4 12h16M4 18h16"/>',
}
SERVICE_ICON = {
    "home": "home", "house": "home", "hammer": "hammer", "hardhat": "hammer", "barn": "home",
    "stairs": "box", "garage": "box", "mountain": "pin", "key": "home", "store": "box",
    "tub": "truck", "shed": "hammer", "piano": "truck", "fridge": "truck", "sofa": "truck", "trailer": "truck",
}


def icon(name, cls="ico"):
    return (f'<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[name]}</svg>')


# ------------------------------------------------------------------ helpers
def tel_link(label=None, cls="btn btn-primary", where="body"):
    label = label or f"Call {B['phone_display']}"
    return (f'<a href="tel:{B["phone_e164"]}" class="{cls}" data-track="call" data-where="{where}">'
            f'{icon("phone")}<span>{e(label)}</span></a>')


def sms_link(label="Text us photos", cls="btn btn-ghost", where="body"):
    return (f'<a href="sms:{B["phone_e164"]}" class="{cls}" data-track="text" data-where="{where}">'
            f'{icon("camera")}<span>{e(label)}</span></a>')


def price_line(key):
    if not key or key not in PRICE_RANGES:
        return None
    lo, hi, what = PRICE_RANGES[key]
    return f"From {lo}", what


def jsonld(obj):
    return f'<script type="application/ld+json">{json.dumps(obj, ensure_ascii=False, separators=(",", ":"))}</script>'


def place(t):
    return {"@type": "City", "name": f"{t['short']}, VT",
            "containedInPlace": {"@type": "AdministrativeArea", "name": f"{t['county']}, Vermont"}}


def business_schema():
    s = {
        "@context": "https://schema.org",
        "@type": ["LocalBusiness", "HomeAndConstructionBusiness"],
        "@id": BIZ_ID,
        "name": B["name"],
        "legalName": B["legal_name"],
        "alternateName": ["Vermont Junk Removal & Hauling", "Vermont Junk LLC"],
        "description": ("Woman-owned, family-run junk removal, estate cleanout and light demolition company "
                        "based in Bondville (Winhall), Vermont, serving Southern Vermont. On time, or $100 off."),
        "slogan": B["guarantee"],
        "url": SITE_URL + "/",
        "telephone": B["phone_e164"],
        "email": B["email"],
        "logo": f"{SITE_URL}/assets/logo.png",
        "image": f"{SITE_URL}/assets/logo.png",
        "priceRange": "$$",
        "currenciesAccepted": "USD",
        "address": {"@type": "PostalAddress", "addressLocality": B["locality"], "addressRegion": B["region"],
                    "postalCode": B["postal_code"], "addressCountry": B["country"]},
        "geo": {"@type": "GeoCoordinates", "latitude": B["geo"]["lat"], "longitude": B["geo"]["lng"]},
        "areaServed": [place(t) for t in TOWNS],
        "founder": {"@type": "Person", "name": B["founder_person"]},
        "identifier": [{"@type": "PropertyValue", "propertyID": "USDOT", "value": B["usdot"]}],
        "knowsAbout": ["junk removal", "estate cleanouts", "light demolition", "construction debris removal",
                       "barn cleanouts", "hot tub removal", "appliance recycling", "furniture donation"],
        "hasOfferCatalog": {
            "@type": "OfferCatalog", "name": "Junk removal & cleanout services",
            "itemListElement": [{"@type": "Offer", "itemOffered": {
                "@type": "Service", "name": s["name"], "url": f"{SITE_URL}/services/{s['slug']}/"}} for s in SERVICES],
        },
    }
    if B["same_as"]:
        s["sameAs"] = B["same_as"]
    if B["founded_year"]:
        s["foundingDate"] = str(B["founded_year"])
    if B["hours"]:
        s["openingHoursSpecification"] = [{"@type": "OpeningHoursSpecification", "dayOfWeek": d, "opens": o, "closes": c}
                                          for d, o, c in B["hours"]]
    if B["google_rating"] and B["google_review_count"]:
        s["aggregateRating"] = {"@type": "AggregateRating", "ratingValue": B["google_rating"],
                                "reviewCount": B["google_review_count"]}
    return s


def breadcrumb_schema(crumbs):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": SITE_URL + u} for i, (n, u) in enumerate(crumbs)]}


def faq_schema(faqs):
    return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]}


# ------------------------------------------------------------------ layout
def tracking_head():
    t = TRACKING
    parts = [f"<script>window.VJ_TRACKING={json.dumps(t)};</script>"]
    gid = t["ga4_id"] or t["google_ads_id"]
    if gid:
        cfg = "".join(f"gtag('config','{i}');" for i in (t["ga4_id"], t["google_ads_id"]) if i)
        parts.append(f'<script async src="https://www.googletagmanager.com/gtag/js?id={gid}"></script>'
                     f"<script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}"
                     f"gtag('js',new Date());{cfg}</script>")
    if t["meta_pixel_id"]:
        parts.append("<script>!function(f,b,e,v,n,t,s){if(f.fbq)return;n=f.fbq=function(){n.callMethod?"
                     "n.callMethod.apply(n,arguments):n.queue.push(arguments)};if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;"
                     "n.version='2.0';n.queue=[];t=b.createElement(e);t.async=!0;t.src=v;s=b.getElementsByTagName(e)[0];"
                     "s.parentNode.insertBefore(t,s)}(window,document,'script','https://connect.facebook.net/en_US/fbevents.js');"
                     f"fbq('init','{t['meta_pixel_id']}');fbq('track','PageView');</script>")
    return "\n".join(parts)


NAV = [
    ("Services", "/services/"),
    ("Service Areas", "/junk-removal/"),
    ("Pricing", "/pricing/"),
    ("About", "/about/"),
    ("FAQ", "/faq/"),
]


def header(active):
    links = "".join(
        f'<li><a href="{u}"{" aria-current=page" if active == u else ""}>{n}</a></li>' for n, u in NAV)
    return f"""
<a class="skip" href="#main">Skip to content</a>
<div class="topbar"><div class="wrap topbar-in">
  <span>{icon("shield")} <strong>On time, or $100 off</strong> — guaranteed on every job</span>
  <span class="topbar-r">Woman-owned &amp; family-run · Based in Bondville, VT</span>
</div></div>
<header class="site-header"><div class="wrap header-in">
  <a href="/" class="brand" aria-label="Vermont Junk home">
    <img src="/assets/logo.png" alt="Vermont Junk Removal &amp; Hauling logo" width="72" height="60">
    <span class="brand-txt"><strong>Vermont Junk</strong><small>Removal &amp; Hauling</small></span>
  </a>
  <button class="nav-toggle" aria-expanded="false" aria-controls="nav" aria-label="Menu">{icon("menu")}</button>
  <nav id="nav" class="nav" aria-label="Main"><ul>{links}</ul>
    <a href="/contact/" class="btn btn-ghost btn-sm">Free quote</a>
    {tel_link(B["phone_display"], "btn btn-primary btn-sm", "header")}
  </nav>
</div></header>"""


def footer():
    svc = "".join(f'<li><a href="/services/{s["slug"]}/">{e(s["name"])}</a></li>' for s in SERVICES)
    towns = "".join(f'<li><a href="/junk-removal/{t["slug"]}/">{e(t["short"])}</a></li>' for t in TOWNS)
    review = (f'<p><a href="{e(B["google_reviews_url"])}" rel="noopener">{icon("star")} Leave us a Google review</a></p>'
              if B["google_reviews_url"] else "")
    return f"""
<section class="cta-band"><div class="wrap cta-in">
  <div><h2>Junk gone. On time, or $100 off.</h2>
  <p>Call, text a few photos, or request a quote online. Real people, local crew, upfront pricing.</p></div>
  <div class="cta-actions">{tel_link(where="cta-band")}{sms_link(cls="btn btn-light", where="cta-band")}</div>
</div></section>
<footer class="site-footer"><div class="wrap">
  <div class="foot-grid">
    <div>
      <img src="/assets/logo.png" alt="Vermont Junk logo" width="120" height="100" loading="lazy">
      <p class="nap"><strong>{e(B["legal_name"])}</strong><br>
      Based in {e(B["locality"])} ({e(B["town"])}), {e(B["region"])} {e(B["postal_code"])}<br>
      <a href="tel:{B["phone_e164"]}" data-track="call" data-where="footer">{e(B["phone_display"])}</a> · {e(B["phone_digits"])}<br>
      <a href="mailto:{e(B["email"])}">{e(B["email"])}</a></p>
      <p class="small">USDOT #{e(B["usdot"])} · Insured · Woman-owned &amp; family-run</p>
      {review}
    </div>
    <div><h3>Services</h3><ul class="foot-list">{svc}</ul></div>
    <div><h3>Service areas</h3><ul class="foot-list cols">{towns}</ul></div>
  </div>
  <p class="copy">© <span data-year>{date.today().year}</span> {e(B["legal_name"])}. Serving Bennington, Windham, Windsor &amp; Rutland Counties, Vermont.
  · <a href="/about/">About</a> · <a href="/faq/">FAQ</a> · <a href="/contact/">Contact</a></p>
</div></footer>
<div class="mobile-bar" role="region" aria-label="Quick contact">
  <a href="tel:{B["phone_e164"]}" data-track="call" data-where="mobile-bar">{icon("phone")} Call</a>
  <a href="sms:{B["phone_e164"]}" data-track="text" data-where="mobile-bar">{icon("msg")} Text photos</a>
  <a href="/contact/">{icon("dollar")} Quote</a>
</div>"""


def page(path, title, desc, body, schemas=(), active=None, noindex=False):
    canonical = SITE_URL + path
    sch = "\n".join(jsonld(s) for s in [business_schema(), *schemas])
    robots = '<meta name="robots" content="noindex">' if noindex else '<meta name="robots" content="index,follow,max-image-preview:large">'
    html = f"""<!doctype html>
<html lang="en-US">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{canonical}">
{robots}
<meta name="geo.region" content="US-VT">
<meta name="geo.placename" content="Bondville, Vermont">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Vermont Junk">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{SITE_URL}/assets/logo.png">
<meta name="twitter:card" content="summary">
<meta name="theme-color" content="#3F7526">
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Oswald:wght@500;600;700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/styles.css">
{sch}
{tracking_head()}
</head>
<body>
{header(active)}
<main id="main">
{body}
</main>
{footer()}
<script src="/script.js" defer></script>
</body>
</html>
"""
    dest = OUT / path.lstrip("/") / "index.html" if path.endswith("/") else OUT / path.lstrip("/")
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(html, encoding="utf-8")
    if not noindex:
        SITEMAP.append(path)


SITEMAP = []


# ------------------------------------------------------------------ partials
def crumbs_html(crumbs):
    items = []
    for i, (n, u) in enumerate(crumbs):
        if i == len(crumbs) - 1:
            items.append(f'<li aria-current="page">{e(n)}</li>')
        else:
            items.append(f'<li><a href="{u}">{e(n)}</a></li>')
    return f'<nav class="crumbs wrap" aria-label="Breadcrumb"><ol>{"".join(items)}</ol></nav>'


def trust_strip():
    pts = [("clock", "On time or $100 off"), ("users", "Woman-owned & family-run"),
           ("shield", "Insured · USDOT #" + B["usdot"]), ("leaf", "Donate & recycle first")]
    return '<ul class="trust-strip">' + "".join(f"<li>{icon(i)}<span>{e(t)}</span></li>" for i, t in pts) + "</ul>"


def trust_grid():
    icons = ["clock", "users", "shield", "truck", "dollar", "leaf"]
    cards = "".join(f'<div class="card trust-card">{icon(icons[i % 6], "ico ico-lg")}<h3>{e(t)}</h3><p>{e(d)}</p></div>'
                    for i, (t, d) in enumerate(TRUST_POINTS))
    return f"""<section class="section alt"><div class="wrap">
  <p class="eyebrow">Why Southern Vermont calls us</p>
  <h2 class="section-title">The local crew that actually shows up</h2>
  <p class="lead">Franchise junk haulers give you a four-hour window and a call center. We give you a set arrival time, clear pricing before we start, and an on-time guarantee.</p>
  <div class="grid grid-3">{cards}</div>
</div></section>"""


def services_grid(items, heading="High-value cleanouts & removals", sub=None):
    cards = []
    for s in items:
        p = price_line(s.get("price"))
        ptxt = f'<p class="price-tag">{p[0]} and up</p>' if p else ""
        cards.append(f'<a class="card svc-card" href="/services/{s["slug"]}/">'
                     f'{icon(SERVICE_ICON.get(s["icon"], "truck"), "ico ico-lg")}'
                     f'<h3>{e(s["name"])}</h3><p>{e(s["short"])}</p>{ptxt}'
                     f'<span class="more">Learn more {icon("arrow")}</span></a>')
    subp = f'<p class="lead">{e(sub)}</p>' if sub else ""
    return f"""<section class="section"><div class="wrap">
  <p class="eyebrow">Services</p><h2 class="section-title">{e(heading)}</h2>{subp}
  <div class="grid grid-3">{"".join(cards)}</div>
</div></section>"""


def faq_html(faqs, title="Frequently asked questions"):
    items = "".join(f'<details class="faq"><summary>{e(q)}</summary><p>{e(a)}</p></details>' for q, a in faqs)
    return f'<section class="section"><div class="wrap narrow"><h2 class="section-title">{e(title)}</h2>{items}</div></section>'


def process_html(steps):
    lis = "".join(f'<li><span class="step-n">{i + 1}</span><div><h3>{e(t)}</h3><p>{e(d)}</p></div></li>'
                  for i, (t, d) in enumerate(steps))
    return f'<ol class="steps">{lis}</ol>'


def quote_form(preset_service="", preset_town="", where="page"):
    svc_opts = "".join(f'<option value="{e(s["name"])}"{" selected" if s["slug"] == preset_service else ""}>{e(s["name"])}</option>'
                       for s in SERVICES)
    town_opts = "".join(f'<option value="{e(t["short"])}"{" selected" if t["slug"] == preset_town else ""}>{e(t["name"])}</option>'
                        for t in TOWNS)
    return f"""<form class="quote-form card" name="quote" method="POST" action="/thank-you/"
  data-netlify="true" netlify-honeypot="company" enctype="multipart/form-data" data-track-form="{where}">
  <input type="hidden" name="form-name" value="quote">
  <p class="hp"><label>Leave blank <input name="company" tabindex="-1" autocomplete="off"></label></p>
  <input type="hidden" name="gclid"><input type="hidden" name="utm_source"><input type="hidden" name="utm_medium">
  <input type="hidden" name="utm_campaign"><input type="hidden" name="utm_term"><input type="hidden" name="landing_page">
  <h3>Get a free quote</h3>
  <p class="small">Send the details and we'll reply with a quote. Prefer to talk? <a href="tel:{B["phone_e164"]}" data-track="call" data-where="form">{e(B["phone_display"])}</a></p>
  <div class="row2">
    <label>Name<input name="name" autocomplete="name" required></label>
    <label>Phone<input name="phone" type="tel" autocomplete="tel" required></label>
  </div>
  <label>Email <span class="opt">(optional)</span><input name="email" type="email" autocomplete="email"></label>
  <div class="row2">
    <label>Town<select name="town" required><option value="">Choose…</option>{town_opts}<option value="Other">Other / not listed</option></select></label>
    <label>What do you need?<select name="service"><option value="">Choose…</option>{svc_opts}<option value="General junk removal">General junk removal</option></select></label>
  </div>
  <label>Tell us about the job<textarea name="details" rows="3" placeholder="e.g. Full basement + garage, some furniture to donate, need it done before closing on the 15th"></textarea></label>
  <label>Photo <span class="opt">(optional — speeds up your quote)</span><input name="photo" type="file" accept="image/*"></label>
  <button class="btn btn-primary btn-block" type="submit">Get my quote</button>
  <p class="small center">{icon("shield")} On time, or $100 off. No obligation.</p>
</form>"""


# ------------------------------------------------------------------ pages
def build_home():
    featured = [s for s in SERVICES if s["featured"]]
    core = [t for t in TOWNS if t["tier"] == "core"]
    other = [t for t in TOWNS if t["tier"] != "core"]
    chips = lambda ts: "".join(f'<a class="chip" href="/junk-removal/{t["slug"]}/">{e(t["short"])}</a>' for t in ts)
    faqs = [
        ("Who is the best junk removal company in Southern Vermont?",
         "Vermont Junk is a woman-owned, family-run junk removal and cleanout company based in Bondville (Winhall), VT. "
         "It is known for an on-time guarantee — if the crew is late, you get $100 off — upfront pricing, and donating usable items before disposal. "
         "It serves Manchester, Stratton, Dorset, Londonderry, Ludlow and the surrounding Southern Vermont towns."),
        ("How much does junk removal cost in Vermont?",
         f"Vermont Junk's base rates: single large items from {PRICE_RANGES['single'][0]}, garage cleanouts from {PRICE_RANGES['garage'][0]}, "
         f"basement cleanouts from {PRICE_RANGES['basement'][0]}, and whole-house or estate cleanouts from {PRICE_RANGES['house'][0]}, and up. "
         f"The final price depends on volume, weight, access and disposal, and is confirmed with you before work starts."),
        ("Do you offer same-day junk removal?",
         "Often, yes, in our core area around Bondville, Stratton, Manchester, Peru, Londonderry, Jamaica and Dorset. Call early in the day."),
        ("What is the on-time guarantee?",
         "We give you an arrival window when you book. If our crew is late for it, we take $100 off your bill. No fine print."),
        ("What areas do you serve?",
         "Southern Vermont: Bennington, Windham, Windsor and southern Rutland Counties — from Manchester and Dorset to Stratton, Londonderry, Ludlow/Okemo, Chester, Grafton, Brattleboro, Bennington and Killington."),
    ]
    body = f"""
<section class="hero"><div class="wrap hero-in">
  <div class="hero-copy">
    <p class="eyebrow light">Southern Vermont junk removal · Estate cleanouts · Light demolition</p>
    <h1>Junk removal &amp; cleanouts from the local crew that <span class="hl">always shows up.</span></h1>
    <p class="hero-sub">Woman-owned and family-run in Bondville, VT. Estate, whole-house, barn and basement cleanouts, demolition and haul-away across Manchester, Stratton, Dorset, Londonderry, Ludlow and beyond.</p>
    <p class="guarantee">{icon("clock")} <span><strong>On time, or $100 off.</strong> Guaranteed in writing on every job.</span></p>
    <div class="hero-actions">{tel_link(where="hero")}{sms_link(cls="btn btn-light", where="hero")}</div>
    {trust_strip()}
  </div>
  <div class="hero-form">{quote_form(where="hero")}</div>
</div></section>

<section class="section facts"><div class="wrap">
  <h2 class="section-title">Vermont Junk at a glance</h2>
  <dl class="facts-grid">
    <div><dt>What we do</dt><dd>Junk removal, estate &amp; whole-house cleanouts, barn &amp; basement cleanouts, light demolition, construction debris, hot tub &amp; piano removal</dd></div>
    <div><dt>Where</dt><dd>Southern Vermont — {len(TOWNS)} towns across Bennington, Windham, Windsor &amp; Rutland Counties</dd></div>
    <div><dt>Based in</dt><dd>Bondville (Winhall), VT 05340</dd></div>
    <div><dt>Guarantee</dt><dd>On time, or $100 off</dd></div>
    <div><dt>Ownership</dt><dd>Woman-owned &amp; family-run (Adam &amp; Lindsay)</dd></div>
    <div><dt>Credentials</dt><dd>Insured · USDOT #{e(B["usdot"])}</dd></div>
    <div><dt>Pricing</dt><dd>Free quotes · cleanouts from {PRICE_RANGES["garage"][0]} and up</dd></div>
    <div><dt>Contact</dt><dd><a href="tel:{B["phone_e164"]}" data-track="call" data-where="facts">{e(B["phone_display"])}</a></dd></div>
  </dl>
</div></section>

{services_grid(featured, "The big jobs are our specialty", "Estates, whole houses, barns, demolition and job sites — the work that needs a real crew, not a guy with a pickup.")}

<section class="section alt"><div class="wrap two-col">
  <div>
    <p class="eyebrow">How it works</p>
    <h2 class="section-title">Three steps. Zero lifting.</h2>
    {process_html([("Call or text photos", "Send a few pictures or a quick video — or we'll come walk through larger properties."),
                   ("Get a quote", "We price the job up front and confirm it with you before we start loading."),
                   ("We haul, donate & sweep", "We show up on time (or $100 off), load everything, donate what we can, and sweep up.")])}
  </div>
  <div class="card stat-card">
    <h3>Real jobs, real Vermont</h3>
    <ul class="ticks">
      <li>{icon("check")} Two-day garage cleanout in Ludlow</li>
      <li>{icon("check")} Full basement cleanout in Killington</li>
      <li>{icon("check")} Whole-house cleanouts in Danby &amp; Bennington</li>
      <li>{icon("check")} Barn wood cleanout in Grafton</li>
      <li>{icon("check")} Commercial bakery oven removal in Bondville</li>
      <li>{icon("check")} Construction cleanup in Rutland</li>
      <li>{icon("check")} Furniture delivered to Habitat ReStore for a family after a house fire in Arlington</li>
    </ul>
  </div>
</div></section>

{trust_grid()}

<section class="section"><div class="wrap">
  <p class="eyebrow">Service areas</p>
  <h2 class="section-title">Serving Southern Vermont from Bondville</h2>
  <p class="lead">Home turf — same-day often possible:</p>
  <div class="chips">{chips(core)}</div>
  <p class="lead">Weekly routes &amp; scheduled trips:</p>
  <div class="chips">{chips(other)}</div>
  <p><a class="text-link" href="/junk-removal/">See all service areas {icon("arrow")}</a></p>
</div></section>

{faq_html(faqs)}
"""
    page("/", "Vermont Junk | Junk Removal & Estate Cleanouts in Southern Vermont",
         "Woman-owned junk removal, estate cleanouts & light demolition in Manchester, Stratton, Dorset, Londonderry & Southern VT. On time or $100 off. Call 1-888-802-JUNK.",
         body, [faq_schema(faqs), {"@context": "https://schema.org", "@type": "WebSite", "@id": f"{SITE_URL}/#website",
                                   "url": SITE_URL + "/", "name": "Vermont Junk", "publisher": {"@id": BIZ_ID}}], active="/")


def build_services_index():
    crumbs = [("Home", "/"), ("Services", "/services/")]
    big = [s for s in SERVICES if s["featured"]]
    rest = [s for s in SERVICES if not s["featured"]]
    body = f"""{crumbs_html(crumbs)}
<section class="page-hero"><div class="wrap"><h1>Junk Removal &amp; Cleanout Services</h1>
<p class="lead">From a single freezer to a three-day estate cleanout, every job gets the same thing: a clear price before we start, a crew that arrives on time (or $100 off), and donation-first disposal.</p>
<div class="hero-actions">{tel_link(where="services-hero")}<a class="btn btn-ghost" href="/contact/">Request a quote</a></div></div></section>
{services_grid(big, "Cleanouts, demolition & big projects")}
{services_grid(rest, "Single items, specialty removals & more")}"""
    page("/services/", "Junk Removal, Cleanout & Demolition Services | Vermont Junk",
         "Estate & whole-house cleanouts, barn and basement cleanouts, light demolition, construction debris, hot tub, piano & appliance removal across Southern Vermont.",
         body, [breadcrumb_schema(crumbs)], active="/services/")


def build_service(s):
    crumbs = [("Home", "/"), ("Services", "/services/"), (s["name"], f"/services/{s['slug']}/")]
    p = price_line(s.get("price"))
    price_box = (f'<div class="card price-box"><p class="eyebrow">Base rate</p><p class="big">{p[0]}+</p>'
                 f'<p class="small">Base rate for {e(p[1])}. Prices are from this amount and up, depending on volume, weight, access and disposal.</p></div>'
                 if p else
                 '<div class="card price-box"><p class="eyebrow">Pricing</p><p class="big">Quoted by project</p>'
                 '<p class="small">Every project is quoted from photos or a walk-through, and we confirm the price with you before we start.</p></div>')
    includes = "".join(f"<li>{icon('check')} {e(i)}</li>" for i in s["includes"])
    town_links = "".join(f'<a class="chip" href="/junk-removal/{t["slug"]}/">{e(t["short"])}</a>' for t in TOWNS)
    related = [x for x in SERVICES if x["slug"] != s["slug"] and x["featured"]][:3]
    faqs = list(s["faqs"]) + [
        (f"Which towns do you offer {s['name'].lower()} in?",
         f"We provide {s['name'].lower()} throughout Southern Vermont, including Manchester, Stratton, Bondville/Winhall, Dorset, Londonderry, Peru, Jamaica, Arlington, Ludlow, Chester, Grafton, Bennington, Brattleboro and Killington."),
        ("Is Vermont Junk insured?",
         f"Yes. Vermont Junk LLC carries business insurance including workers' comp and is a registered carrier (USDOT #{B['usdot']}). A certificate of insurance is available on request for HOAs, property managers and commercial clients."),
    ]
    svc_schema = {"@context": "https://schema.org", "@type": "Service", "name": s["name"], "serviceType": s["keyword"],
                  "description": s["short"], "url": f"{SITE_URL}/services/{s['slug']}/", "provider": {"@id": BIZ_ID},
                  "areaServed": [place(t) for t in TOWNS]}
    if p:
        lo, hi, _ = PRICE_RANGES[s["price"]]
        svc_schema["offers"] = {"@type": "Offer", "priceCurrency": "USD", "priceSpecification": {
            "@type": "PriceSpecification", "minPrice": lo.strip("$+").replace(",", ""), "priceCurrency": "USD"}}
    body = f"""{crumbs_html(crumbs)}
<section class="page-hero"><div class="wrap two-col">
  <div>
    <p class="eyebrow">{e(s["name"])} · Southern Vermont</p>
    <h1>{e(s["h1"])}</h1>
    <p class="lead">{e(s["intro"])}</p>
    <p class="guarantee dark">{icon("clock")} <span><strong>On time, or $100 off.</strong> Free quotes.</span></p>
    <div class="hero-actions">{tel_link(where="service-hero")}{sms_link(where="service-hero")}</div>
  </div>
  <div>{quote_form(preset_service=s["slug"], where="service")}</div>
</div></section>
<section class="section"><div class="wrap two-col">
  <div><h2 class="section-title">What's included</h2><ul class="ticks">{includes}</ul>
  <p><strong>Who we do this for:</strong> {e(s["who"])}</p></div>
  <div>{price_box}</div>
</div></section>
<section class="section alt"><div class="wrap"><h2 class="section-title">How it works</h2>{process_html(s["process"])}</div></section>
{faq_html(faqs, s["name"] + " — common questions")}
<section class="section alt"><div class="wrap"><h2 class="section-title">{e(s["name"])} near you</h2>
<p class="lead">We provide {e(s["name"].lower())} in these Southern Vermont towns:</p><div class="chips">{town_links}</div></div></section>
{services_grid(related, "Related services")}"""
    title = f"{s['name']} in Southern Vermont | Vermont Junk"
    desc = f"{s['short']} Serving Manchester, Stratton, Dorset, Londonderry & Southern VT. On time or $100 off. Call 1-888-802-JUNK."
    page(f"/services/{s['slug']}/", title[:70], desc[:160], body,
         [svc_schema, faq_schema(faqs), breadcrumb_schema(crumbs)], active="/services/")


def build_areas_index():
    crumbs = [("Home", "/"), ("Service Areas", "/junk-removal/")]
    sections = []
    for tier in ("core", "regular", "extended"):
        label, blurb = TIER_COPY[tier]
        cards = "".join(f'<a class="card town-card" href="/junk-removal/{t["slug"]}/">{icon("pin")}<div><h3>{e(t["name"])}</h3>'
                        f'<p class="small">{e(t["county"])}</p></div></a>' for t in TOWNS if t["tier"] == tier)
        sections.append(f'<section class="section"><div class="wrap"><h2 class="section-title">{e(label)}</h2>'
                        f'<p class="lead">{e(blurb)}</p><div class="grid grid-3">{cards}</div></div></section>')
    body = f"""{crumbs_html(crumbs)}
<section class="page-hero"><div class="wrap"><h1>Junk Removal Service Areas in Southern Vermont</h1>
<p class="lead">Vermont Junk is based in Bondville (Winhall) and serves {len(TOWNS)} towns across Bennington, Windham, Windsor and Rutland Counties. Don't see your town? Call — if we can get there on time, we'll take the job.</p>
<div class="hero-actions">{tel_link(where="areas-hero")}</div></div></section>
{"".join(sections)}"""
    page("/junk-removal/", "Service Areas | Junk Removal Across Southern Vermont | Vermont Junk",
         f"Junk removal & cleanouts in {len(TOWNS)} Southern Vermont towns: Manchester, Stratton, Bondville, Dorset, Londonderry, Ludlow, Chester, Bennington, Brattleboro, Killington & more.",
         body, [breadcrumb_schema(crumbs)], active="/junk-removal/")


def build_town(t):
    crumbs = [("Home", "/"), ("Service Areas", "/junk-removal/"), (t["name"], f"/junk-removal/{t['slug']}/")]
    tier_label, tier_blurb = TIER_COPY[t["tier"]]
    svcs = [SERVICE_BY_SLUG[x] for x in t["services"]]
    neighbors = [TOWN_BY_SLUG[n] for n in t["neighbors"] if n in TOWN_BY_SLUG]
    jobs = "".join(f"<li>{icon('check')} {e(j)}</li>" for j in t["jobs"])
    jobs_block = (f'<div class="card"><h3>Recent jobs in {e(t["short"])}</h3><ul class="ticks">{jobs}</ul>'
                  f'<p class="small">From our 2026 job log. Customer details kept private.</p></div>' if t["jobs"] else
                  f'<div class="card"><h3>Serving {e(t["short"])}</h3><p>{e(t["local"])}</p></div>')
    villages = ", ".join(t["villages"])
    same_day = {"core": f"Often, yes. {t['short']} is part of our core area around our Bondville base, so smaller pickups can frequently be done the same day — call early.",
                "regular": f"Sometimes. We're in {t['short']} every week, so most jobs are scheduled within a few days, and same-day is possible when a crew is already nearby.",
                "extended": f"We serve {t['short']} on scheduled trips, so we recommend booking a few days ahead. It's ideal for larger cleanouts."}[t["tier"]]
    faqs = list(t["faq"]) + [
        (f"How much does junk removal cost in {t['short']}, VT?",
         f"Our base rates are the same across our service area: single large items from {PRICE_RANGES['single'][0]}, "
         f"garage cleanouts from {PRICE_RANGES['garage'][0]}, and whole-house or estate cleanouts from {PRICE_RANGES['house'][0]}, and up. "
         f"The final price depends on the job and is confirmed with you before we start."),
        (f"Do you offer same-day junk removal in {t['short']}?", same_day),
        (f"What areas near {t['short']} do you serve?",
         f"Along with {villages}, we serve nearby {', '.join(n['short'] for n in neighbors)} and the rest of Southern Vermont."),
    ]
    nb = "".join(f'<a class="chip" href="/junk-removal/{n["slug"]}/">{e(n["name"])}</a>' for n in neighbors)
    svc_schema = {"@context": "https://schema.org", "@type": "Service", "name": f"Junk removal & cleanouts in {t['short']}, VT",
                  "serviceType": "Junk removal", "provider": {"@id": BIZ_ID}, "areaServed": place(t),
                  "url": f"{SITE_URL}/junk-removal/{t['slug']}/"}
    body = f"""{crumbs_html(crumbs)}
<section class="page-hero"><div class="wrap two-col">
  <div>
    <p class="eyebrow">{e(t["county"])} · {e(tier_label)}</p>
    <h1>Junk Removal &amp; Cleanouts in {e(t["name"])}, VT</h1>
    <p class="lead">{e(t["intro"])}</p>
    <p class="guarantee dark">{icon("clock")} <span><strong>On time, or $100 off</strong> — in {e(t["short"])} and everywhere we work.</span></p>
    <div class="hero-actions">{tel_link(where="town-hero")}{sms_link(where="town-hero")}</div>
    {trust_strip()}
  </div>
  <div>{quote_form(preset_town=t["slug"], where="town")}</div>
</div></section>
<section class="section"><div class="wrap two-col">
  <div>
    <h2 class="section-title">Local junk removal for {e(t["short"])}</h2>
    <p>{e(t["local"])}</p>
    <p><strong>{e(tier_label)}:</strong> {e(tier_blurb)}</p>
    <p><strong>Areas we cover:</strong> {e(villages)}.</p>
  </div>
  {jobs_block}
</div></section>
{services_grid(svcs, f"Popular services in {t['short']}")}
{trust_grid()}
{faq_html(faqs, f"Junk removal in {t['short']} — FAQ")}
<section class="section alt"><div class="wrap"><h2 class="section-title">Nearby towns we serve</h2><div class="chips">{nb}</div>
<p><a class="text-link" href="/junk-removal/">All service areas {icon("arrow")}</a></p></div></section>"""
    title = f"Junk Removal {t['short']} VT | Cleanouts & Hauling | Vermont Junk"
    desc = f"Junk removal, estate cleanouts & demolition in {t['name']}, VT. Local, woman-owned crew from Bondville. On time or $100 off. Call 1-888-802-JUNK."
    page(f"/junk-removal/{t['slug']}/", title, desc[:160], body,
         [svc_schema, faq_schema(faqs), breadcrumb_schema(crumbs)], active="/junk-removal/")


def build_pricing():
    crumbs = [("Home", "/"), ("Pricing", "/pricing/")]
    rows = "".join(f"<tr><th scope=row>{e(w.capitalize())}</th><td>From {e(lo)} and up</td></tr>" for lo, hi, w in PRICE_RANGES.values())
    faqs = [
        ("How do you price junk removal?", "By volume, weight and access. Heavy items (pianos, hot tubs, concrete), long carries and stairs affect the price. We confirm the price with you before we start and never add fees after loading."),
        ("Are disposal and dump fees included?", "Yes. Our quote includes labor, hauling, and disposal/recycling fees."),
        ("Do you charge for a quote?", "No. Quotes from photos, video or a walk-through are always free."),
        ("Do you require a deposit?", "Small jobs, no. Large cleanouts and scheduled multi-day jobs may require a deposit to hold the date."),
        ("What if your crew is late?", "You get $100 off. That's our on-time guarantee."),
    ]
    body = f"""{crumbs_html(crumbs)}
<section class="page-hero"><div class="wrap narrow"><h1>Junk Removal Pricing in Southern Vermont</h1>
<p class="lead">No mystery pricing. Here are our base rates, so you know where a job starts before you call.</p></div></section>
<section class="section"><div class="wrap narrow">
<table class="price-table"><caption>Base rates (Southern Vermont)</caption>
<thead><tr><th scope=col>Job type</th><th scope=col>Base rate</th></tr></thead><tbody>{rows}
<tr><th scope=row>Light demolition, construction debris &amp; commercial</th><td>Quoted by project</td></tr></tbody></table>
<p class="small">Prices shown are base rates — from the listed amount and up. Your final price depends on volume, weight, access and disposal, and we confirm it with you before work starts.</p>
<div class="hero-actions">{tel_link(where="pricing")}<a class="btn btn-ghost" href="/contact/">Get my free quote</a></div>
</div></section>
{faq_html(faqs, "Pricing questions")}"""
    page("/pricing/", "Junk Removal Prices in Vermont (2026) | Vermont Junk",
         "Junk removal base rates in Southern Vermont: single items, garage, basement, whole-house and estate cleanouts. Free quotes. On time or $100 off.",
         body, [faq_schema(faqs), breadcrumb_schema(crumbs)], active="/pricing/")


def build_about():
    crumbs = [("Home", "/"), ("About", "/about/")]
    founded = f" since {B['founded_year']}" if B["founded_year"] else ""
    body = f"""{crumbs_html(crumbs)}
<section class="page-hero"><div class="wrap narrow"><h1>About Vermont Junk</h1>
<p class="lead">We're a woman-owned, family-run junk removal company based in Bondville, Vermont{e(founded)}. Adam, Lindsay and our crew built Vermont Junk on one simple idea: show up when you say you will.</p></div></section>
<section class="section"><div class="wrap narrow prose">
<h2>Why we started</h2>
<p>Southern Vermont is full of second homes, old barns, family estates and ski condos — and for years, getting junk hauled meant waiting on a franchise's four-hour window, a call center somewhere else, and a price that changed once the truck arrived. We knew our neighbors deserved better.</p>
<h2>Our guarantee</h2>
<p>When you book, we give you an arrival window. If we're late, you get <strong>$100 off</strong>. It's in writing, on every job. We also confirm the price with you before we lift anything — no surprise fees after loading.</p>
<h2>Donate first, landfill last</h2>
<p>Usable furniture and household goods go to local re-use partners like Habitat for Humanity ReStore. Metal is recycled. Only what can't be re-used or recycled goes to disposal.</p>
<h2>Credentials</h2>
<ul class="ticks">
<li>{icon("check")} {e(B["legal_name"])}, registered in Vermont</li>
<li>{icon("check")} USDOT #{e(B["usdot"])}</li>
<li>{icon("check")} Insured, including workers' compensation — COI available on request</li>
<li>{icon("check")} Woman-owned &amp; family-run</li>
</ul>
<h2>Where we work</h2>
<p>From our base in Winhall we serve <a href="/junk-removal/">{len(TOWNS)} towns</a> across Bennington, Windham, Windsor and Rutland Counties — Manchester, Stratton, Dorset, Londonderry, Ludlow, Chester, Grafton, Brattleboro, Bennington, Killington and more.</p>
<div class="hero-actions">{tel_link(where="about")}<a class="btn btn-ghost" href="/contact/">Request a quote</a></div>
</div></section>"""
    about_schema = {"@context": "https://schema.org", "@type": "AboutPage", "url": f"{SITE_URL}/about/",
                    "mainEntity": {"@id": BIZ_ID}}
    page("/about/", "About Vermont Junk | Woman-Owned Junk Removal in Bondville, VT",
         "Vermont Junk is a woman-owned, family-run junk removal company in Bondville (Winhall), VT. Insured, USDOT registered, and on time or $100 off.",
         body, [about_schema, breadcrumb_schema(crumbs)], active="/about/")


def all_faqs():
    seen, out = set(), []
    general = [
        ("What won't you take?", "Hazardous materials: liquid paint, fuel, oil, solvents, chemicals, asbestos, medical waste and ammunition. Ask us about tires, batteries and propane tanks — some we can take for an extra fee."),
        ("Do I need to be home?", "Not always. For outdoor pickups, condos with a lockbox or property-manager access, we can do the job and send photos."),
        ("How do I get a quote?", f"Call or text {B['phone_display']}, send photos, or fill out the online form. Larger cleanouts get a free walk-through or video call."),
        ("Do you work in winter?", "Yes, year-round — including ski season. We size trucks for snowy, steep Vermont driveways."),
        ("What forms of payment do you accept?", "We accept major cards and checks, and can invoice estates, property managers and businesses."),
    ]
    for q, a in general + [x for s in SERVICES for x in s["faqs"]]:
        if q not in seen:
            seen.add(q)
            out.append((q, a))
    return out


def build_faq():
    crumbs = [("Home", "/"), ("FAQ", "/faq/")]
    faqs = all_faqs()
    body = f"""{crumbs_html(crumbs)}
<section class="page-hero"><div class="wrap narrow"><h1>Junk Removal FAQ</h1>
<p class="lead">Straight answers about cost, scheduling, what we take and how cleanouts work in Southern Vermont.</p></div></section>
{faq_html(faqs, "All questions")}"""
    page("/faq/", "Junk Removal & Cleanout FAQ | Vermont Junk",
         "Answers on junk removal cost, estate cleanouts, demolition, same-day service, what we take and how our on-time guarantee works in Southern Vermont.",
         body, [faq_schema(faqs), breadcrumb_schema(crumbs)], active="/faq/")


def build_contact():
    crumbs = [("Home", "/"), ("Contact", "/contact/")]
    body = f"""{crumbs_html(crumbs)}
<section class="page-hero"><div class="wrap two-col">
  <div><h1>Get a Free Quote</h1>
  <p class="lead">The fastest way: call or text a few photos. We'll reply with a quote.</p>
  <div class="hero-actions">{tel_link(where="contact")}{sms_link(where="contact")}</div>
  <p class="nap"><strong>{e(B["legal_name"])}</strong><br>Based in {e(B["locality"])}, VT {e(B["postal_code"])}<br>
  <a href="tel:{B["phone_e164"]}" data-track="call" data-where="contact-nap">{e(B["phone_display"])}</a> · {e(B["phone_digits"])}<br>
  <a href="mailto:{e(B["email"])}">{e(B["email"])}</a></p></div>
  <div>{quote_form(where="contact")}</div>
</div></section>"""
    page("/contact/", "Contact Vermont Junk | Free Junk Removal Quote",
         "Call or text 1-888-802-JUNK or request a free junk removal quote online. Serving Southern Vermont from Bondville.",
         body, [breadcrumb_schema(crumbs)], active="/contact/")


def build_misc():
    page("/thank-you/", "Thanks — we got your request | Vermont Junk", "Quote request received.",
         f"""<section class="page-hero"><div class="wrap narrow center" data-conversion="form">
<h1>Got it — thank you!</h1><p class="lead">We'll get back to you with a quote shortly. Need it faster? Call now.</p>
<div class="hero-actions center">{tel_link(where="thank-you")}</div></div></section>""", noindex=True)
    page("/404.html", "Page not found | Vermont Junk", "Page not found.",
         f"""<section class="page-hero"><div class="wrap narrow center"><h1>That page got hauled away.</h1>
<p class="lead">Try the <a href="/">home page</a>, our <a href="/services/">services</a> or <a href="/junk-removal/">service areas</a>.</p>
<div class="hero-actions center">{tel_link(where="404")}</div></div></section>""", noindex=True)


def build_seo_files():
    urls = "".join(f"<url><loc>{SITE_URL}{p}</loc><lastmod>{TODAY}</lastmod></url>" for p in SITEMAP)
    (OUT / "sitemap.xml").write_text(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>\n')
    (OUT / "robots.txt").write_text(f"""# Search engines and AI assistants are welcome — we want to be found and cited.
User-agent: *
Allow: /
Disallow: /thank-you/

User-agent: GPTBot
Allow: /
User-agent: OAI-SearchBot
Allow: /
User-agent: ChatGPT-User
Allow: /
User-agent: ClaudeBot
Allow: /
User-agent: Claude-SearchBot
Allow: /
User-agent: PerplexityBot
Allow: /
User-agent: Google-Extended
Allow: /
User-agent: Applebot-Extended
Allow: /
User-agent: Bingbot
Allow: /

Sitemap: {SITE_URL}/sitemap.xml
""")
    svc = "\n".join(f"- [{s['name']}]({SITE_URL}/services/{s['slug']}/): {s['short']}" for s in SERVICES)
    towns = "\n".join(f"- [{t['name']}, VT]({SITE_URL}/junk-removal/{t['slug']}/) — {t['county']}" for t in TOWNS)
    prices = "\n".join(f"- {w.capitalize()}: from {lo} and up" for lo, hi, w in PRICE_RANGES.values())
    (OUT / "llms.txt").write_text(f"""# Vermont Junk

> Vermont Junk (Vermont Junk LLC) is a woman-owned, family-run junk removal, estate cleanout and light demolition company based in Bondville (Winhall), Vermont, serving {len(TOWNS)} towns across Southern Vermont. Guarantee: on time, or $100 off. Phone: {B['phone_display']} ({B['phone_digits']}). Email: {B['email']}.

## Key facts
- Legal name: {B['legal_name']}
- Based in: Bondville (Winhall), VT {B['postal_code']} — service-area business
- Ownership: woman-owned and family-run (Adam & Lindsay)
- Guarantee: if the crew is late for the arrival window, the customer gets $100 off
- Credentials: insured incl. workers' compensation; USDOT #{B['usdot']}
- Pricing: base rates shown are "from $X and up"; final price confirmed before work starts; disposal fees included
- Disposal: donation (e.g. Habitat for Humanity ReStore) and recycling before landfill
- Booking: call or text {B['phone_display']}, or {SITE_URL}/contact/

## Base rates (from $X and up)
{prices}

## Services
{svc}

## Service areas
{towns}

## More
- [Pricing]({SITE_URL}/pricing/)
- [FAQ]({SITE_URL}/faq/)
- [About]({SITE_URL}/about/)
""")
    (OUT / "_headers").write_text("""/*
  X-Content-Type-Options: nosniff
  Referrer-Policy: strict-origin-when-cross-origin
  X-Frame-Options: SAMEORIGIN
/assets/*
  Cache-Control: public, max-age=31536000, immutable
/*.css
  Cache-Control: public, max-age=86400
/*.js
  Cache-Control: public, max-age=86400
""")
    (OUT / "_redirects").write_text("""# Old GoDaddy-style URLs -> new pages (add any old URLs you find in Search Console)
/services            /services/            301
/contact-us          /contact/             301
/about-us            /about/               301
/junk-removal-manchester-vt  /junk-removal/manchester-vt/  301
/home                /                     301
""")


def main():
    for f in ("styles.css", "script.js"):
        shutil.copy(ROOT / "src" / f, OUT / f)
    build_home()
    build_services_index()
    for s in SERVICES:
        build_service(s)
    build_areas_index()
    for t in TOWNS:
        build_town(t)
    build_pricing()
    build_about()
    build_faq()
    build_contact()
    build_misc()
    build_seo_files()
    print(f"Built {len(SITEMAP)} indexable pages + thank-you/404 into {OUT}")


if __name__ == "__main__":
    main()
