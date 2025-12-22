"""
Image Optimization Script for Hungry-Hippo
Converts source images to AVIF, WebP, and optimized JPG formats

Usage:
    python app/scripts/optimize_images.py <input_image> <output_prefix>

Example:
    python app/scripts/optimize_images.py source_images/hero.jpg app/static/images/hero
"""

from PIL import Image
import pillow_avif
import sys
import os

def optimize_image(input_path, output_prefix):
    """
    Convert image to AVIF, WebP, and optimized JPG

    Args:
        input_path: Path to source image
        output_prefix: Output filename without extension
    """
    if not os.path.exists(input_path):
        print(f"Error: Input file '{input_path}' not found")
        sys.exit(1)

    print(f"Loading image: {input_path}")
    img = Image.open(input_path)

    # Create output directory if it doesn't exist
    output_dir = os.path.dirname(output_prefix)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Created directory: {output_dir}")

    # AVIF (best compression)
    avif_path = f"{output_prefix}.avif"
    print(f"Creating AVIF: {avif_path}")
    img.save(
        avif_path,
        format="AVIF",
        quality=75,
        speed=4  # 0=slowest/best, 10=fastest/worst
    )
    avif_size = os.path.getsize(avif_path) / 1024
    print(f"  ✓ AVIF saved: {avif_size:.1f}KB")

    # WebP (fallback)
    webp_path = f"{output_prefix}.webp"
    print(f"Creating WebP: {webp_path}")
    img.save(
        webp_path,
        format="WebP",
        quality=80,
        method=6  # 0=fast, 6=slower/better
    )
    webp_size = os.path.getsize(webp_path) / 1024
    print(f"  ✓ WebP saved: {webp_size:.1f}KB")

    # JPG (baseline)
    jpg_path = f"{output_prefix}.jpg"
    print(f"Creating JPG: {jpg_path}")
    img.save(
        jpg_path,
        format="JPEG",
        quality=85,
        optimize=True,
        progressive=True
    )
    jpg_size = os.path.getsize(jpg_path) / 1024
    print(f"  ✓ JPG saved: {jpg_size:.1f}KB")

    print(f"\nOptimization complete!")
    print(f"Total size reduction: {jpg_size:.1f}KB (JPG) → {avif_size:.1f}KB (AVIF)")
    print(f"Savings: {((jpg_size - avif_size) / jpg_size * 100):.1f}%")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python optimize_images.py <input_image> <output_prefix>")
        print("Example: python optimize_images.py source/hero.jpg static/images/hero")
        sys.exit(1)

    input_path = sys.argv[1]
    output_prefix = sys.argv[2]

    optimize_image(input_path, output_prefix)
