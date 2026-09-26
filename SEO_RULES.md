# Homepage SEO rules and publishing checklist

This document explains the reasoning applied to the `index.html` prototype. The three named reference files (`iptvcanada.html`, `smartiptvtv.html`, and `omniptv.html`) were not present in the repository, so no source text or design was copied. The observations below are limited to the patterns supplied in the project brief and must not be read as an independent audit of those sites.

## 1–3. Observed patterns, adopted rules, and implementation

| Reference | Observed pattern from brief | Rule adopted | Exact implementation |
|---|---|---|---|
| IPTVV Canada | Product, country and opening message are aligned; commercial vocabulary and geographic facts support the visitor. | State the product and Canadian market once, early and clearly. Use service language only where it helps the buying decision. Show CAD and expose unknown operational facts. | `<title>`, `<meta name="description">`, hero `<h1>` and opening paragraph; the `#plans` price labels; the four-item `.trust-strip`; distinct `#included`, `#devices`, `#setup`, `#practical` and `#faq` sections. |
| SmartIPTVTV | The page is arranged around plan choice, inclusions, device support and concurrent viewing. Plan detail is easy to scan. | Put decision information before general benefits, compare terms in a real table, and separate installation from concurrent streams. | `#plans` has three `<article>` cards with `<h3>` names plus a captioned comparison `<table>`; `#included` explains service categories; `#devices` includes the “One account…” `<h3>` clarification. |
| OmniIPTV | Visitors receive practical explanations of service operation, setup, connectivity and troubleshooting. Questions are grouped. | Answer pre-purchase and setup questions on-page. Do not imply nonexistent guides. Keep media descriptions concise. | `#setup` ordered steps, `#practical` speed/support/troubleshooting content and grouped `#faq` disclosure controls. The mock device visual uses a short `aria-label`; decorative components use `aria-hidden="true"`. No fake guide links are present. |

## 4. Patterns rejected and why

- **Keyword-density targets:** rejected because frequency is not a substitute for relevance or clarity. The counts below describe the completed HTML; they did not drive the copy.
- **Repeated keyword headings and city lists:** rejected because they create redundant sections and do not help a visitor compare or set up a service.
- **Competitor-length matching:** rejected because every section should answer a distinct question; filler would weaken the buying journey.
- **Invented proof:** rejected. The page contains no fabricated reviews, ratings, customer totals, channel totals, licences or guarantees.
- **Unverified commercial claims:** rejected. Unknown prices, catalogue details, connections, availability, activation, support, renewal, payment and refund details are visibly labelled `[TO CONFIRM]`.
- **Fake guide and policy links:** rejected. The prototype uses working in-page anchors and email actions only; future resources are listed below rather than linked.
- **Structured data without verified facts:** rejected. No Product, Offer, Review, AggregateRating, FAQPage or Organization JSON-LD is included. Visible FAQ content alone does not justify promising rich results.
- **Keyword-heavy alternative text:** rejected. The interface illustration has one concise accessible label, while decorative marks and icons are hidden from assistive technology.

## 5. Finished-homepage keyword table

Counts are case-insensitive, measured against visible text in `index.html` (HTML tags removed) and include singular phrases inside longer phrases. They are descriptive snapshots, not optimization targets. Re-run the included verification command after editing.

| Phrase | Purpose | Primary section | Measured occurrence count |
|---|---|---|---:|
| IPTV Canada | Primary product-and-market topic | Title, hero H1 | 2 |
| Canadian IPTV | Natural market-specific variant | Hero opening copy | 2 |
| IPTV service | Explain the product category | Hero opening copy | 1 |
| IPTV provider | Explain provider expectations | Subscription inclusions | 1 |
| subscription | Describe purchase, activation and access | Hero, plans, inclusions, setup, FAQ | 8 |
| plans | Navigation and plan choice | Navigation, hero, plans, final CTA | 8 |
| simultaneous screens | Clarify concurrent use | Plans, devices, FAQ | 7 |
| setup | Explain onboarding and help | Navigation, plans, inclusions, devices, setup, footer | 6 |

Suggested count check:

```bash
python3 - <<'PY'
from html.parser import HTMLParser
from pathlib import Path
class Text(HTMLParser):
    def __init__(self): super().__init__(); self.parts=[]
    def handle_data(self, data): self.parts.append(data)
p=Text(); p.feed(Path('index.html').read_text()); text=' '.join(p.parts).lower()
for phrase in ['iptv canada','canadian iptv','iptv service','iptv provider','subscription','plans','simultaneous screens','setup']:
    print(f'{phrase}: {text.count(phrase)}')
PY
```

Any future phrase ideas should be treated as hypotheses until checked against real query data in Semrush or Google Search Console.

## 6. Missing business facts and pre-publication checks

### Replace or verify

- `[BRAND NAME]`, the logo letter, legal business name and copyright owner.
- `[YOUR-DOMAIN.example]` in the canonical URL, Open Graph URL and Open Graph image URL.
- The nonexistent `og-cover.jpg`; produce and validate a real social sharing image before retaining that metadata.
- Placeholder `sales@example.com` and `support@example.com` mailboxes, or connect buttons to a secure, tested checkout and support workflow.
- CAD plan prices, taxes, billing frequency, accepted payment methods and checkout security.
- Service availability within Canada, catalogue/content rights, programme-guide coverage and on-demand availability.
- Supported device brands, models, OS versions, applications and approved download sources.
- Per-plan installation limits, simultaneous screens, household/location rules and extra-connection charges.
- Activation timing and delivery method; support channels, hours, response targets and supported languages.
- Minimum/recommended bandwidth for each promised resolution, VPN behaviour and troubleshooting escalation.
- Trial, cancellation, renewal and refund terms, plus privacy, terms of service and acceptable-use pages.
- Accessibility, legal and content-licensing review by qualified parties.

### Future guide ideas (not links)

Create these only after instructions are tested on actually supported devices: smart-TV setup; Fire TV/Android TV setup; Apple device setup; playlist/credential safety; home-network troubleshooting. Once real pages exist, add contextual links from `#devices`, `#setup` or `#practical` rather than creating empty destinations.

### Completed static checks

- One `<h1>` is present and the heading order uses section `<h2>` and topic/card `<h3>` elements.
- Navigation includes a skip link, labelled primary navigation, keyboard-operable anchors and an accessible mobile menu button.
- All internal fragment destinations exist; email actions are syntactically valid but still use documented placeholder mailboxes.
- Title, description, canonical, Open Graph type/locale/title/description/URL/image and mobile viewport metadata are present.
- There are no `<img>` elements requiring width, height, lazy loading or `alt`; the CSS-drawn informative visual has a concise accessible label and its decorative children are not exposed.
- The responsive layout has breakpoints at 900 px and 600 px, horizontal overflow handling for the comparison table and reduced-motion support.
- No JSON-LD is included because the visible business and commercial facts remain unverified.

### Still requires live testing

- Replace every placeholder, then test checkout, payment, email delivery, activation and customer-support flows end to end.
- Test responsive behaviour and keyboard/screen-reader use in current Safari, Chrome, Firefox and Edge on real phones, tablets, computers and supported TV browsers.
- Validate the production HTML, metadata, canonical URL, social image rendering, redirects, TLS, page speed and crawl/index controls on the configured domain.
- Check the final copy and commercial terms against actual service operations and obtain legal/content-rights approval.
- Recount keywords only as an editorial record after final copy changes; do not use the counts as targets.

## Final SEO principle

“Clear product-and-market targeting, useful buying information, relevant practical answers, natural keyword usage and accurate technical markup.”
