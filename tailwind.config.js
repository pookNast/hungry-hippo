/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./app/templates/**/*.html",
    "./app/static/js/**/*.js",
  ],
  theme: {
    extend: {
      // Emergency Modernism Color System (oklch only)
      colors: {
        // Emergency Red
        'emergency': 'oklch(0.45 0.19 25)',
        'emergency-hover': 'oklch(0.38 0.21 25)',
        'emergency-active': 'oklch(0.32 0.18 25)',

        // Neutral Palette (chroma ≤ 0.03)
        'neutral': {
          50: 'oklch(0.98 0.01 90)',
          100: 'oklch(0.95 0.01 90)',
          200: 'oklch(0.90 0.02 90)',
          300: 'oklch(0.80 0.02 90)',
          400: 'oklch(0.65 0.02 90)',
          500: 'oklch(0.50 0.02 90)',
          600: 'oklch(0.40 0.02 90)',
          700: 'oklch(0.30 0.02 90)',
          800: 'oklch(0.25 0.02 90)',
          900: 'oklch(0.15 0.01 90)',
        },

        // Accent Navy
        'accent-navy': 'oklch(0.35 0.025 260)',
        'accent-navy-hover': 'oklch(0.30 0.03 260)',
      },

      // Typography Scale (1.2 modular)
      fontSize: {
        'xs': 'clamp(0.75rem, 0.7rem + 0.25vw, 0.875rem)',
        'sm': 'clamp(0.875rem, 0.8rem + 0.3vw, 1rem)',
        'base': 'clamp(1rem, 0.95rem + 0.35vw, 1.125rem)',
        'lg': 'clamp(1.125rem, 1.05rem + 0.4vw, 1.25rem)',
        'xl': 'clamp(1.25rem, 1.15rem + 0.5vw, 1.5rem)',
        '2xl': 'clamp(1.5rem, 1.35rem + 0.7vw, 1.875rem)',
        '3xl': 'clamp(1.875rem, 1.65rem + 1vw, 2.25rem)',
        '4xl': 'clamp(2.25rem, 1.95rem + 1.3vw, 3rem)',
        '5xl': 'clamp(3rem, 2.5rem + 2vw, 4rem)',
        '6xl': 'clamp(3.75rem, 3rem + 3vw, 5rem)',
        '7xl': 'clamp(4.5rem, 3.5rem + 4vw, 6rem)',
      },

      // Font Families
      fontFamily: {
        'sans': ['Inter Variable', '-apple-system', 'BlinkMacSystemFont', 'Segoe UI', 'sans-serif'],
        'display': ['Epilogue', 'Inter Variable', 'sans-serif'],
        'mono': ['JetBrains Mono', 'Courier New', 'monospace'],
      },

      // Touch Target Spacing
      spacing: {
        'tap-min': '56px',           // WCAG AAA minimum
        'tap-mobile': '64px',         // Emergency CTA mobile
        'tap-desktop': '88px',        // Emergency CTA desktop
      },

      // Custom Border Radius (not default rounded-lg)
      borderRadius: {
        'none': '0',
        'sm': '0.25rem',
        'DEFAULT': '0.5rem',
        'md': '0.625rem',
        'lg': '0.75rem',
        'xl': '1rem',
        '2xl': '1.5rem',
        'full': '9999px',
      },

      // Custom Shadows (not default shadow-md)
      boxShadow: {
        'sm': '0 1px 2px 0 oklch(0 0 0 / 0.05)',
        'DEFAULT': '0 2px 8px 0 oklch(0 0 0 / 0.08)',
        'md': '0 4px 12px 0 oklch(0 0 0 / 0.10)',
        'lg': '0 8px 24px 0 oklch(0 0 0 / 0.12)',
        'xl': '0 12px 32px 0 oklch(0 0 0 / 0.15)',
        '2xl': '0 20px 48px 0 oklch(0 0 0 / 0.18)',
        'emergency': '0 8px 24px 0 oklch(0.45 0.19 25 / 0.25)',
        'none': 'none',
      },

      // Spring Physics Animations
      transitionTimingFunction: {
        'spring-smooth': 'cubic-bezier(0.34, 1.56, 0.64, 1)',
        'spring-bounce': 'cubic-bezier(0.68, -0.55, 0.265, 1.55)',
      },

      // Custom Animations
      keyframes: {
        'pulse-subtle': {
          '0%, 100%': { opacity: '1' },
          '50%': { opacity: '0.9' },
        },
        'badge-pulse': {
          '0%': { boxShadow: '0 0 0 0 oklch(0.45 0.19 25 / 0.7)' },
          '70%': { boxShadow: '0 0 0 8px oklch(0.45 0.19 25 / 0)' },
          '100%': { boxShadow: '0 0 0 0 oklch(0.45 0.19 25 / 0)' },
        },
      },
      animation: {
        'pulse-subtle': 'pulse-subtle 2s cubic-bezier(0.4, 0, 0.6, 1) infinite',
        'badge-pulse': 'badge-pulse 2s cubic-bezier(0.4, 0, 0.6, 1) infinite',
      },
    },
  },
  plugins: [
    // Forms plugin for better form styling
    require('@tailwindcss/forms'),

    // Typography plugin for prose content
    require('@tailwindcss/typography'),

    // Custom plugin for focus-visible styles
    function({ addUtilities }) {
      addUtilities({
        '.focus-ring': {
          '@apply focus-visible:outline-none focus-visible:ring-4 focus-visible:ring-emergency focus-visible:ring-offset-2': {},
        },
        '.emergency-cta': {
          cursor: 'crosshair',
        },
      })
    },
  ],
}
