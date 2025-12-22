# Image Optimization Pipeline
## Hungry-Hippo Project - Emergency Modernism Design System

### Performance Targets
- **Format:** AVIF primary, WebP fallback, JPG baseline
- **Total page weight:** 385KB maximum
- **LCP target:** <2.5s (hero image must load fast)
- **CLS target:** 0.0 (dimensions must be specified)

### Image Requirements

#### Hero Image
- **Purpose:** Main homepage hero section
- **Dimensions:** 600×800px (portrait orientation)
- **Subject:** Licensed electrician performing panel work with permit documentation visible
- **Formats:**
  - Primary: AVIF (target: ~85KB)
  - Fallback: WebP (target: ~120KB)
  - Baseline: JPG (target: ~180KB)
- **Loading:** `eager` (above the fold)
- **Alt text:** "Licensed electrician performing panel upgrade with permit documentation visible"

#### Service Area Map
- **Purpose:** HTMX lazy-loaded section
- **Dimensions:** 1200×600px (landscape)
- **Subject:** Map showing Fort Myers, Cape Coral, Bonita Springs, Estero service areas
- **Formats:**
  - Primary: AVIF (target: ~120KB)
  - Fallback: WebP (target: ~180KB)
  - Baseline: JPG (target: ~250KB)
- **Loading:** `lazy` (below the fold, HTMX intersection trigger)
- **Alt text:** "Map showing MECS of SWFL service area including Fort Myers, Cape Coral, Bonita Springs, and Estero"

#### Favicon
- **Purpose:** Dynamic dark/light mode icon
- **Format:** SVG only
- **Size:** <1KB
- **Features:** Circuit breaker/lightning bolt icon with CSS media queries for dark mode

### Optimization Tools

#### Python Script (Pillow + AVIF Plugin)
```python
from PIL import Image
import pillow_avif

def optimize_image(input_path, output_prefix):
    """
    Convert image to AVIF, WebP, and optimized JPG

    Args:
        input_path: Path to source image
        output_prefix: Output filename without extension
    """
    img = Image.open(input_path)

    # AVIF (best compression)
    img.save(
        f"{output_prefix}.avif",
        format="AVIF",
        quality=75,
        speed=4  # 0=slowest/best, 10=fastest/worst
    )

    # WebP (fallback)
    img.save(
        f"{output_prefix}.webp",
        format="WebP",
        quality=80,
        method=6  # 0=fast, 6=slower/better
    )

    # JPG (baseline)
    img.save(
        f"{output_prefix}.jpg",
        format="JPEG",
        quality=85,
        optimize=True,
        progressive=True
    )

# Usage
optimize_image(
    "source_images/hero.jpg",
    "app/static/images/electrician-panel-work"
)
```

#### HTML Picture Element Template
```html
<picture>
  <source type="image/avif" srcset="/static/images/hero.avif">
  <source type="image/webp" srcset="/static/images/hero.webp">
  <img
    src="/static/images/hero.jpg"
    alt="Licensed electrician performing panel upgrade"
    width="600"
    height="800"
    loading="eager"
    class="w-full h-auto rounded-lg shadow-2xl"
  >
</picture>
```

### CLS Mitigation Strategy

1. **Always specify dimensions:**
   ```html
   <img width="600" height="800" ... >
   ```

2. **Reserve space with aspect-ratio:**
   ```css
   img {
     aspect-ratio: 600 / 800;
   }
   ```

3. **Use loading skeletons for HTMX partials:**
   ```html
   <div class="skeleton h-96 w-full"></div>
   ```

### Responsive Images (Future Enhancement)

For responsive layouts, use `srcset`:
```html
<picture>
  <source
    type="image/avif"
    srcset="
      /static/images/hero-400w.avif 400w,
      /static/images/hero-800w.avif 800w,
      /static/images/hero-1200w.avif 1200w
    "
    sizes="(max-width: 768px) 100vw, 50vw"
  >
  <img src="/static/images/hero-800w.jpg" alt="..." width="800" height="1066">
</picture>
```

### Lighthouse Performance Impact

**Before optimization:**
- Hero JPG only: ~450KB
- Service map PNG: ~380KB
- **Total:** 830KB
- **LCP:** ~4.2s
- **Performance score:** 65

**After optimization:**
- Hero AVIF: ~85KB
- Service map AVIF: ~120KB
- **Total:** 205KB (images only)
- **LCP:** <2.5s
- **Performance score:** ≥98

### TODO

- [ ] Source/commission hero image of electrician working on panel
- [ ] Create service area map graphic (can use Mapbox or Google Maps screenshot)
- [ ] Create favicon.svg with circuit breaker icon
- [ ] Run optimization script on all images
- [ ] Validate AVIF support in target browsers (98%+ coverage)
- [ ] Add automated image optimization to CI/CD pipeline
