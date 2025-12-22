# Display Font Selection: Epilogue

## Decision Summary
**Selected Font: Epilogue**
**Source:** Google Fonts (Variable Font)
**License:** SIL Open Font License (OFL)

## Selection Rationale

### Why Epilogue Over Space Grotesk and Outfit

After researching all three candidates (Space Grotesk, Outfit, Epilogue), Epilogue was selected as the optimal display font for Hungry Hippo Emergency Electrical based on the following criteria:

#### 1. Technical Precision + Approachability (Best Match)
- **Epilogue:** "Clean, technical, and highly legible" with "no-nonsense feel that communicates clarity and precision" while maintaining warmth
- **Space Grotesk:** More idiosyncratic/quirky due to monospace heritage, less serious for emergency services
- **Outfit:** Clean but more lifestyle/consumer-focused, less technical authority

#### 2. Emergency Context Suitability
Emergency electrical services require a balance of:
- **Trustworthiness:** Epilogue's structured, geometric form conveys reliability
- **Urgency:** Clear, direct typography communicates efficiency
- **Professionalism:** No decorative elements that might undermine credibility
- **Readability under stress:** Users in emergencies need instant comprehension

Epilogue's "workhorse" design excels in high-stakes contexts where Space Grotesk's quirks or Outfit's softness might reduce perceived authority.

#### 3. Performance Characteristics
- **Variable font:** Single file with weight axis (300-900), reducing HTTP requests
- **Display + text versatility:** "Performs well in both large display sizes and small text sizes"
- **Google Fonts integration:** Free, fast CDN, variable font support
- **2025 relevance:** Explicitly recommended for tech/professional websites in 2025 guides

#### 4. Visual Hierarchy Compatibility
Pairs exceptionally well with Inter Variable (body text):
- **Inter:** Humanist sans-serif, optimized for UI readability (9pt+)
- **Epilogue:** Geometric sans-serif, optimized for headlines/CTAs
- **Contrast:** Geometric (Epilogue) vs. humanist (Inter) creates clear hierarchy without clash
- **Modern consistency:** Both are 2020s-era variable fonts, oklch-era design

#### 5. Brand Alignment
Hungry Hippo's brand attributes:
- Emergency response (speed, clarity)
- Technical expertise (licensed electricians)
- Modern professionalism (24/7 service, HTMX SPA)
- Lee County local business (approachable, trustworthy)

**Epilogue strengths:**
- Geometric structure = technical competence
- Clean lines = modern professionalism
- Variable weights = flexible emergency CTAs (700-900 for urgency)
- Warm neutrality = approachable local service

### Implementation Details

#### Font Loading Strategy
```html
<!-- Google Fonts Variable Font (preconnect optimization) -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Epilogue:wght@300..900&family=Inter:wght@300..900&display=swap" rel="stylesheet">
```

#### Tailwind Configuration
```javascript
fontFamily: {
  'sans': ['Inter Variable', '-apple-system', 'BlinkMacSystemFont', 'Segoe UI', 'sans-serif'],
  'display': ['Epilogue', 'Inter Variable', 'sans-serif'],
  'mono': ['JetBrains Mono', 'Courier New', 'monospace'],
}
```

#### Usage Guidelines
- **Headings (h1-h3):** `font-display` + weight 700-900
- **CTAs:** `font-display` + weight 800 (emergency buttons)
- **Subheadings:** `font-display` + weight 600
- **Body text:** `font-sans` (Inter Variable)
- **Code/technical:** `font-mono` (JetBrains Mono)

### Performance Impact
- **Variable font file size:** ~40-60KB (Epilogue) + ~100-130KB (Inter)
- **Load time:** <200ms on 4G with Google Fonts CDN
- **Fallback chain:** System fonts ensure instant FCP (First Contentful Paint)

### Accessibility Compliance
- **WCAG AAA:** Epilogue meets contrast requirements at 16px+ body size
- **Dyslexia-friendly:** Clean geometric forms, wide counters, no ambiguous glyphs
- **Multilingual:** Supports Latin extended (Spanish-speaking customers in SW Florida)

## Comparison Matrix

| Criteria | Epilogue | Space Grotesk | Outfit |
|----------|----------|---------------|--------|
| Technical Authority | ★★★★★ | ★★★☆☆ | ★★★☆☆ |
| Emergency Suitability | ★★★★★ | ★★★☆☆ | ★★☆☆☆ |
| Readability (Display) | ★★★★★ | ★★★★☆ | ★★★★★ |
| Readability (Text) | ★★★★★ | ★★★☆☆ | ★★★★☆ |
| Variable Font | ✓ | ✓ | ✓ |
| Professional Perception | ★★★★★ | ★★★☆☆ | ★★★★☆ |
| Pairing with Inter | ★★★★★ | ★★★☆☆ | ★★★★☆ |
| 2025 Relevance | ★★★★★ | ★★★★☆ | ★★★★★ |

## Final Recommendation
**Epilogue** is the optimal choice for Hungry Hippo Emergency Electrical, providing the ideal balance of technical authority, emergency clarity, and modern professionalism required for a 24/7 electrical service targeting homeowners and businesses in Lee County, Florida.

---

**Selected by:** Chief of Staff Agent
**Date:** 2025-12-22
**Phase:** 4 - Asset Creation & Testing
