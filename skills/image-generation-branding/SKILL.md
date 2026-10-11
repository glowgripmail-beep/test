---
name: image-generation-branding
description: Premium image generation for brand identity and product design references. Use for brand-kit / brand-guidelines boards, logo systems and logo concepting, identity decks, visual-world presentations (minimalist, cinematic, editorial, dark-tech, luxury, cultural, security, gaming, developer-tool, consumer-app); for website design reference images - landing pages, marketing sites, product comps, hero sections, "N sections for a website" (ONE separate horizontal image per section); and for mobile app screen concepts and flows - iOS, Android, cross-platform onboarding, auth, home, profile, settings, chat, ecommerce, fintech, health/fitness, productivity, social screens inside a clean phone mockup. Images only, no code. Triggers - brand kit, brand board, logo, identity, website mockup image, landing page design image, hero image, app screens, app mockup, onboarding flow, זהות מותג, לוגו, בורד מותג, רפרנס ויזואלי, עיצוב דף נחיתה, מסכי אפליקציה, מוקאפ.
---

# Image Generation & Branding

This skill merges three image-direction skills. Each one is kept complete, verbatim, in its own folder. This file only routes between them and lists what they share and where they disagree.

All three generate **images only** (design references, boards, screens). None of them writes implementation code; for turning images into code see `ui-web-design (part: image-to-code)`.

## Which part to read when

| Task | Read |
|---|---|
| Brand kit / brand-guidelines board, logo system, logo concept, identity deck, visual-world presentation, brand strip, contact sheet | `brandkit/GUIDE.md` |
| Logo concept methods (monogram, product action, metaphor fusion, negative space, construction geometry) | `brandkit/GUIDE.md` -> "LOGO CONCEPT METHODS" |
| Brand visual modes (dark developer, operator, nature, security, editorial/compliance, luxury, voice, cultural) | `brandkit/GUIDE.md` -> "VISUAL MODES" |
| Website / landing page / marketing site / product page / portfolio design reference images, one image per section | `imagegen-frontend-web/GUIDE.md` |
| A single website hero section image | `imagegen-frontend-web/GUIDE.md` -> "HERO COMPOSITION BIAS", §4 |
| Default section counts and site packs (4 / 8 / 12) | `imagegen-frontend-web/GUIDE.md` -> §5, §15 |
| Mobile app screen concepts, single screens, multi-screen flows (onboarding, auth, home, checkout...) | `imagegen-frontend-mobile/GUIDE.md` |
| Phone mockup framing rules | `imagegen-frontend-mobile/GUIDE.md` -> §9, §10 |
| Category bias for apps (fintech, health/fitness, productivity, social, commerce, wellness) | `imagegen-frontend-mobile/GUIDE.md` -> §33 |
| Brand + website, or brand + app, in one job | Read `brandkit/GUIDE.md` first, then the web or mobile guide; check "Conflicts between sources" below |

Each guide starts with its original description and a few general usage notes (cross-references to related skills).

Related skills: copy inside designs -> `copywriting-ads`; review after building -> `ui-web-design (part: web-design-guidelines)`; images to code -> `ui-web-design (part: image-to-code)`; store / landing-page conversion work -> `ecommerce-store-cro (part: store-design-cro)`.

## Shared rules (all three sources agree)

Summaries only; the exact wording lives in each guide.

- Premium, intentional, art-directed output; aggressively break generic AI defaults.
- One disciplined, controlled palette; accents repeat consistently; no random rainbow, no default purple-blue AI glow, no cheap neon.
- Sparse, short, readable text; no lorem ipsum, no long paragraphs, no tiny fake text.
- Imagery must be art-directed and meaningful, never stock filler or unrelated decoration.
- When several images/panels/screens are produced, they must read as one brand / product world (same palette, type, image treatment, component family).
- Avoid clutter: random floating icons, blobs, fake dashboards with pointless data, pill/badge/label overload.
- No fake brand slop (web and mobile both ban names like Acme, NovaCore, Flowbit) and no generic buzzword copy.
- References (when given) are a quality bar, not a template: do not copy exact logos, names, compositions or slogans.
- Internally choose one option per style category (theme, typography, structure, etc.) and commit to it (web §2, mobile §22, brandkit "VISUAL MODES").
- Run the source's internal quality check before output (web §17, mobile §35, brandkit "FINAL OUTPUT STANDARD").

## Conflicts between sources

Not resolved here; each side is labeled by source.

1. **One image vs. many images**
   - brandkit: "Create a complete brand world in one image." Default output is one brand-kit overview image with a 3 × 3 (or 2 × 3, 2 × 2, 1 × 3, 4 × 2) panel grid.
   - imagegen-frontend-web: "Generate one separate horizontal image PER section. Always. No exceptions." Never combine sections, never "replace several sections with one collage".
   - imagegen-frontend-mobile: generate separate screen images; "It is better to generate multiple clean readable screens than one compressed board with tiny unreadable text"; yet multiple device mockups in one composition are allowed (§10).
2. **Aspect ratio / canvas**
   - brandkit: default `4:3` or `16:10`.
   - imagegen-frontend-web: always horizontal, `16:9`, `16:10` or `21:9`.
   - imagegen-frontend-mobile: no ratio given; phone mockup centered with even canvas margins.
3. **Cropped phone mockups**
   - brandkit lists "phone corner crop" as a good mockup.
   - imagegen-frontend-mobile: "do not use awkwardly cropped device frames", "do not let the phone touch the canvas edges"; full visible device frame by default.
4. **Gradients**
   - imagegen-frontend-web: "Gradients are **allowed and encouraged** when professional and subtle" (tonal, atmospheric, vignettes, noise gradients, editorial washes).
   - brandkit: "Never make: generic startup gradients"; "no generic purple-blue AI glow unless appropriate".
   - imagegen-frontend-mobile: "avoid generic startup gradients unless they truly fit"; avoid "too many heavy gradients"; but tonal gradient fog is an allowed background treatment.
5. **Palette structure / number of accents**
   - brandkit: base color + primary accent + secondary accent + neutrals; "one accent can carry the entire system".
   - imagegen-frontend-web: 1 primary + 1 secondary + 1 accent (used sparingly) + a neutral scale.
   - imagegen-frontend-mobile: "let one or two accents do real work".
6. **Serif luxury**
   - brandkit "Luxury / Beauty / Fashion" mode: ivory / stone / espresso, serif wordmark.
   - imagegen-frontend-web lists "'luxury' that is just beige serif text" among the repetitive defaults to break.
7. **Density and art-direction dials** (web §1 vs. mobile §1)
   - VISUAL_DENSITY: web 4, mobile 3. SPACING_GENEROSITY: web 8, mobile 9. ART_DIRECTION: web 8, mobile 9. brandkit has no dials ("restrained visual density").
8. **Headline length**
   - imagegen-frontend-web: hero headline "usually read like 5-10 strong words".
   - imagegen-frontend-mobile: first screen "1 to 3 short lines for the main statement".
   - brandkit: brand essence = "One short tagline"; text limited to brand name, one tagline, one URL, one command, 2–5 section labels, short UI chips.
9. **Texture**
   - brandkit encourages halftone, grain, scanline, CRT and print texture.
   - imagegen-frontend-mobile: TEXTURE_STRENGTH 7, "do not default to perfectly sterile flat backgrounds".
   - imagegen-frontend-web lists "over-rendered noise that hides the layout" as visual slop (while allowing paper/material texture and micro-noise gradients).
10. **Iconography**
    - imagegen-frontend-mobile: avoid generic Lucide-like / developer-style icon packs; custom-feeling icon system.
    - brandkit: uses "icon row" / "UI chips" as system detail; "Dark Developer / Builder" mode leans on developer-native cues (monospace, terminal glyphs). No icon-style rule.
    - imagegen-frontend-web: no icon-style rule beyond "same icon or illustration mood" across frames.
11. **Banned fake brand names differ**
    - imagegen-frontend-web: Acme, Nexus, Flowbit, Quantumly, NovaCore.
    - imagegen-frontend-mobile: Acme, NovaCore, Flowbit, Quantix, VeloPay.
12. **Metrics / stats**
    - imagegen-frontend-web: "three identical stat columns ... unless user asked for KPIs" is slop; charts only when the site type needs them.
    - imagegen-frontend-mobile: "large hero metric card" and "compact stat strip" are allowed signature components, while "repeated stat cards with no product reason" is an AI tell.
    - brandkit: avoid "full fake dashboards with too much data"; "dashboard fragment" is fine as a mockup.
13. **Scope overlap: websites inside mobile**
    - imagegen-frontend-mobile: "This skill is not for: websites, landing pages, desktop dashboards".
    - imagegen-frontend-web: applies "Mobile-implied fidelity (even for desktop mocks)" to website comps.
14. **Code wording**
    - The kept usage note in every guide says "הקוד כאן כתוב בעיקר ל React ו Tailwind", but none of the three guides contains code; imagegen-frontend-mobile says "This skill generates images only. Do not switch into coding mode."

### Internal inconsistencies inside one source (kept verbatim, not fixed)
- imagegen-frontend-web: default "landing page" = 6 sections (HARD OUTPUT RULE, §5, §19), but §15 "DEFAULT SITE PACKS" only defines 4, 8 and 12-section packs (no 6-pack). The HARD OUTPUT RULE says "full website template" -> 8, §5 also says "marketing site" -> 8, "product page" -> 6, "portfolio" -> 6.
- imagegen-frontend-web §19 numbering repeats "5." and skips "6.".
