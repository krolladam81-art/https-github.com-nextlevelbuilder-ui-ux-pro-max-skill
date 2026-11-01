"""Single source of truth for business facts (NAP + trust signals).

Every page, the JSON-LD schema, llms.txt and the sitemap read from here, so
the name / phone / service area stay identical everywhere — consistency is
what Google and AI assistants use to decide they trust a local business.

Anything marked TODO is a value only the owner can confirm. Leave it as None
and the site simply omits it (nothing fake is ever published).
"""

SITE_URL = "https://www.vermontjunk.com"

BUSINESS = {
    "name": "Vermont Junk",
    "legal_name": "Vermont Junk LLC",
    "tagline": "Southern Vermont's local junk removal & cleanout crew",
    "phone_display": "1-888-802-JUNK",
    "phone_digits": "(888) 802-5865",
    "phone_e164": "+18888025865",
    "email": "info@vermontjunk.com",
    # Service-area business: GBP hides the street address, so we publish
    # town / ZIP only. Must match the Google Business Profile exactly.
    "locality": "Bondville",
    "town": "Winhall",
    "region": "VT",
    "postal_code": "05340",
    "country": "US",
    "geo": {"lat": 43.1626, "lng": -72.9126},  # Bondville village center
    "usdot": "7245571",
    "owners": "Adam & Lindsay",
    "founder_person": "Adam Kroll",
    "guarantee": "On time, or $100 off",
    # TODO(owner): fill these in — they are omitted from the site until set.
    "founded_year": None,          # e.g. 2023
    "hours": None,                 # e.g. [("Mo-Sa", "07:00", "19:00")]
    "google_reviews_url": None,    # "https://g.page/r/XXXX/review"
    "google_maps_url": None,       # your GBP share link
    "google_rating": None,         # e.g. 4.9  (ONLY real numbers from GBP)
    "google_review_count": None,   # e.g. 37
    "same_as": [
        # Add every real profile URL — this is how AI assistants connect
        # the website to the same business everywhere else.
        # "https://www.facebook.com/vermontjunk",
        # "https://www.instagram.com/vermontjunk",
        # "https://www.yelp.com/biz/vermont-junk-bondville",
        # "https://www.bbb.org/...",
        # "https://nextdoor.com/pages/vermont-junk-bondville-vt/",
    ],
}

# Tracking IDs — leave None until you have them; script.js no-ops safely.
TRACKING = {
    "ga4_id": None,                 # "G-XXXXXXX"
    "google_ads_id": None,          # "AW-XXXXXXXXX"
    "ads_call_label": None,         # conversion label for website phone clicks
    "ads_form_label": None,         # conversion label for quote form submits
    "meta_pixel_id": None,          # for retargeting-only Meta campaigns
}

TRUST_POINTS = [
    ("On-time guarantee", "If our crew is late for your arrival window, you get $100 off. In writing, every job."),
    ("Woman-owned & family-run", "A local family business based in Winhall — not a franchise call center."),
    ("Fully insured", "Business insurance including workers' comp. Certificate of insurance available on request for HOAs and property managers."),
    ("USDOT registered", "Registered interstate carrier, USDOT #7245571."),
    ("Upfront pricing", "A firm quote before we lift anything. No surprise fees after loading."),
    ("Donate & recycle first", "Usable furniture goes to local re-use partners like Habitat for Humanity ReStore before anything goes to the landfill."),
]

# Honest price ranges taken from Vermont Junk's own 2026 job records.
# Update as your pricing changes — these appear on service pages + FAQ.
PRICE_RANGES = {
    "single": ("$230", "$750", "single large items (sofa, freezer, piano, appliance)"),
    "garage": ("$800", "$3,250", "garage cleanouts"),
    "basement": ("$1,400", "$6,100", "basement cleanouts"),
    "house": ("$2,650", "$9,900+", "whole-house and estate cleanouts"),
}
