"""
Asset Generator for PHPWebSpiders Google Business Profile
Generates:
  - assets/google-business-logo.svg
  - assets/google-business-cover.svg
  - assets/google-business-logo.png
  - assets/google-business-cover.png
  - assets/preview.html (interactive viewer & canvas PNG exporter)
"""

import os
import math
import struct
import zlib

ASSETS_DIR = "/home/dkviraj/pws/phpwebspiders.github.io/assets"
os.makedirs(ASSETS_DIR, exist_ok=True)

# ==========================================
# 1. GOOGLE BUSINESS LOGO (SVG - 1024x1024)
# ==========================================
def create_logo_svg():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <defs>
    <!-- Background Gradients -->
    <radialGradient id="bg-glow" cx="50%" cy="45%" r="65%">
      <stop offset="0%" stop-color="#1e1b4b" stop-opacity="0.8"/>
      <stop offset="40%" stop-color="#0f172a" stop-opacity="0.9"/>
      <stop offset="100%" stop-color="#05050a" stop-opacity="1"/>
    </radialGradient>

    <radialGradient id="core-glow" cx="50%" cy="42%" r="35%">
      <stop offset="0%" stop-color="#6366f1" stop-opacity="0.45"/>
      <stop offset="50%" stop-color="#38bdf8" stop-opacity="0.2"/>
      <stop offset="100%" stop-color="#0a0a14" stop-opacity="0"/>
    </radialGradient>

    <!-- Brand Gradients -->
    <linearGradient id="brand-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#38bdf8"/>
      <stop offset="45%" stop-color="#818cf8"/>
      <stop offset="100%" stop-color="#c084fc"/>
    </linearGradient>

    <linearGradient id="neon-cyan-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#22d3ee"/>
      <stop offset="100%" stop-color="#3b82f6"/>
    </linearGradient>

    <linearGradient id="node-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ffffff"/>
      <stop offset="100%" stop-color="#818cf8"/>
    </linearGradient>

    <!-- Filters for Glow Effects -->
    <filter id="neon-glow" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="8" result="blur1"/>
      <feGaussianBlur stdDeviation="20" result="blur2"/>
      <feMerge>
        <feMergeNode in="blur2"/>
        <feMergeNode in="blur1"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>

    <filter id="soft-glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="4" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>

    <!-- Pattern -->
    <pattern id="grid-pattern" width="40" height="40" patternUnits="userSpaceOnUse">
      <path d="M 40 0 L 0 0 0 40" fill="none" stroke="rgba(99, 102, 241, 0.07)" stroke-width="1"/>
    </pattern>
  </defs>

  <style>
    .font-brand { font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; font-weight: 800; }
    .font-mono { font-family: 'JetBrains Mono', 'Fira Code', Consolas, monospace; font-weight: 600; }
    .font-sub { font-family: 'Inter', sans-serif; font-weight: 600; letter-spacing: 0.35em; }
  </style>

  <!-- Background -->
  <rect width="1024" height="1024" fill="#06070c"/>
  <rect width="1024" height="1024" fill="url(#bg-glow)"/>
  <rect width="1024" height="1024" fill="url(#grid-pattern)"/>
  <circle cx="512" cy="430" r="380" fill="url(#core-glow)"/>

  <!-- Outer Cyber Tech Ring -->
  <circle cx="512" cy="430" r="300" fill="none" stroke="rgba(99, 102, 241, 0.2)" stroke-width="1.5" stroke-dasharray="8 12"/>
  <circle cx="512" cy="430" r="320" fill="none" stroke="rgba(56, 189, 248, 0.15)" stroke-width="1"/>

  <!-- Outer Shield / Hexagonal Frame -->
  <polygon points="512,160 740,292 740,555 512,687 284,555 284,292"
           fill="rgba(15, 23, 42, 0.6)" stroke="url(#brand-grad)" stroke-width="3" filter="url(#soft-glow)"/>

  <!-- Radar / Web Concentric Rings -->
  <polygon points="512,230 680,327 680,521 512,618 344,521 344,327"
           fill="rgba(99, 102, 241, 0.05)" stroke="rgba(129, 140, 248, 0.3)" stroke-width="1.5"/>

  <polygon points="512,290 625,355 625,485 512,550 399,485 399,355"
           fill="rgba(56, 189, 248, 0.06)" stroke="rgba(56, 189, 248, 0.4)" stroke-width="1.5"/>

  <polygon points="512,350 575,386 575,459 512,495 449,459 449,386"
           fill="rgba(192, 132, 252, 0.1)" stroke="url(#brand-grad)" stroke-width="2"/>

  <!-- Radial Web Strands (Spider Network Axes) -->
  <g stroke="rgba(129, 140, 248, 0.45)" stroke-width="2">
    <!-- North & South -->
    <line x1="512" y1="160" x2="512" y2="687"/>
    <!-- NE & SW -->
    <line x1="740" y1="292" x2="284" y2="555"/>
    <!-- SE & NW -->
    <line x1="740" y1="555" x2="284" y2="292"/>
    <!-- Horizontal Web Lines -->
    <line x1="284" y1="423" x2="740" y2="423" stroke="rgba(56, 189, 248, 0.25)" stroke-dasharray="4 6"/>
  </g>

  <!-- Glowing Web Nodes (Hex Corners) -->
  <!-- Level 1 (Outer) -->
  <g filter="url(#neon-glow)">
    <circle cx="512" cy="160" r="6" fill="#38bdf8"/>
    <circle cx="740" cy="292" r="6" fill="#818cf8"/>
    <circle cx="740" cy="555" r="6" fill="#c084fc"/>
    <circle cx="512" cy="687" r="6" fill="#38bdf8"/>
    <circle cx="284" cy="555" r="6" fill="#818cf8"/>
    <circle cx="284" cy="292" r="6" fill="#c084fc"/>

    <!-- Level 2 (Mid) -->
    <circle cx="512" cy="230" r="4.5" fill="#ffffff"/>
    <circle cx="680" cy="327" r="4.5" fill="#38bdf8"/>
    <circle cx="680" cy="521" r="4.5" fill="#818cf8"/>
    <circle cx="512" cy="618" r="4.5" fill="#ffffff"/>
    <circle cx="344" cy="521" r="4.5" fill="#c084fc"/>
    <circle cx="344" cy="327" r="4.5" fill="#38bdf8"/>

    <!-- Level 3 (Inner) -->
    <circle cx="512" cy="290" r="3.5" fill="#38bdf8"/>
    <circle cx="625" cy="355" r="3.5" fill="#818cf8"/>
    <circle cx="625" cy="485" r="3.5" fill="#c084fc"/>
    <circle cx="512" cy="550" r="3.5" fill="#38bdf8"/>
    <circle cx="399" cy="485" r="3.5" fill="#818cf8"/>
    <circle cx="399" cy="355" r="3.5" fill="#c084fc"/>
  </g>

  <!-- Center Hexagon Core / Spider Heart -->
  <polygon points="512,385 550,407 550,451 512,473 474,451 474,407"
           fill="url(#brand-grad)" filter="url(#neon-glow)"/>

  <!-- Stylized Spider Legs / Circuit Bridges Emerging from Core -->
  <g stroke="url(#brand-grad)" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" fill="none" filter="url(#soft-glow)">
    <!-- Top Legs -->
    <path d="M 480 395 L 430 330 L 400 320"/>
    <path d="M 544 395 L 594 330 L 624 320"/>
    <!-- Upper Mid Legs -->
    <path d="M 474 415 L 390 390 L 350 410"/>
    <path d="M 550 415 L 634 390 L 674 410"/>
    <!-- Lower Mid Legs -->
    <path d="M 474 445 L 390 470 L 350 450"/>
    <path d="M 550 445 L 634 470 L 674 450"/>
    <!-- Bottom Legs -->
    <path d="M 480 465 L 430 530 L 400 540"/>
    <path d="M 544 465 L 594 530 L 624 540"/>
  </g>

  <!-- Code Brackets Overlay in Center Core -->
  <g stroke="#ffffff" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round" fill="none">
    <!-- Left bracket < -->
    <path d="M 495 418 L 485 429 L 495 440"/>
    <!-- Right bracket > -->
    <path d="M 529 418 L 539 429 L 529 440"/>
    <!-- Slash / -->
    <line x1="517" y1="416" x2="507" y2="442"/>
  </g>

  <!-- Subtle PHP Floating Tag Badge Above Emblem -->
  <g transform="translate(512, 130)">
    <rect x="-42" y="-14" width="84" height="28" rx="14" fill="#0f172a" stroke="url(#neon-cyan-grad)" stroke-width="1.5" filter="url(#soft-glow)"/>
    <text x="0" y="5" text-anchor="middle" class="font-mono" font-size="12" fill="#38bdf8" letter-spacing="2">PHP</text>
  </g>

  <!-- ================= BRAND TYPOGRAPHY ================= -->
  <!-- Main Brand Name: PHPWebSpiders -->
  <text x="512" y="785" text-anchor="middle" class="font-brand" font-size="62" letter-spacing="-0.5" filter="url(#soft-glow)">
    <tspan fill="#ffffff">PHP</tspan><tspan fill="url(#brand-grad)">WebSpiders</tspan>
  </text>

  <!-- Decorative Divider Line with Diamond Accent -->
  <g filter="url(#soft-glow)">
    <line x1="330" y1="825" x2="480" y2="825" stroke="url(#brand-grad)" stroke-width="2" stroke-linecap="round"/>
    <polygon points="512,820 517,825 512,830 507,825" fill="#38bdf8"/>
    <line x1="544" y1="825" x2="694" y2="825" stroke="url(#brand-grad)" stroke-width="2" stroke-linecap="round"/>
  </g>

  <!-- Subtitle Tagline -->
  <text x="512" y="865" text-anchor="middle" class="font-sub" font-size="16" fill="#94a3b8">
    FULL-STACK WEB SOLUTIONS
  </text>

  <!-- Bottom Tech Stack Pills -->
  <g transform="translate(512, 915)" class="font-mono" font-size="13" text-anchor="middle">
    <rect x="-260" y="-15" width="105" height="30" rx="15" fill="rgba(99, 102, 241, 0.12)" stroke="rgba(99, 102, 241, 0.3)" stroke-width="1"/>
    <text x="-207" y="5" fill="#a5b4fc">REACT</text>

    <rect x="-140" y="-15" width="115" height="30" rx="15" fill="rgba(56, 189, 248, 0.12)" stroke="rgba(56, 189, 248, 0.3)" stroke-width="1"/>
    <text x="-82" y="5" fill="#7dd3fc">NEXT.JS</text>

    <rect x="-10" y="-15" width="100" height="30" rx="15" fill="rgba(192, 132, 252, 0.12)" stroke="rgba(192, 132, 252, 0.3)" stroke-width="1"/>
    <text x="40" y="5" fill="#d8b4fe">PYTHON</text>

    <rect x="105" y="-15" width="155" height="30" rx="15" fill="rgba(52, 211, 153, 0.12)" stroke="rgba(52, 211, 153, 0.3)" stroke-width="1"/>
    <text x="182" y="5" fill="#6ee7b7">CLOUD ARCH</text>
  </g>

</svg>'''
    return svg

# ==========================================
# 2. GOOGLE BUSINESS COVER PHOTO (SVG - 1200x675 / 16:9)
# ==========================================
def create_cover_svg():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 675" width="1200" height="675">
  <defs>
    <!-- Background Gradients -->
    <radialGradient id="cov-glow-left" cx="25%" cy="50%" r="60%">
      <stop offset="0%" stop-color="#312e81" stop-opacity="0.6"/>
      <stop offset="50%" stop-color="#1e1b4b" stop-opacity="0.3"/>
      <stop offset="100%" stop-color="#07070d" stop-opacity="0"/>
    </radialGradient>

    <radialGradient id="cov-glow-right" cx="80%" cy="40%" r="50%">
      <stop offset="0%" stop-color="#0284c7" stop-opacity="0.3"/>
      <stop offset="60%" stop-color="#0f172a" stop-opacity="0.1"/>
      <stop offset="100%" stop-color="#07070d" stop-opacity="0"/>
    </radialGradient>

    <linearGradient id="cov-brand-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#38bdf8"/>
      <stop offset="50%" stop-color="#818cf8"/>
      <stop offset="100%" stop-color="#c084fc"/>
    </linearGradient>

    <linearGradient id="cov-accent-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#38bdf8"/>
      <stop offset="100%" stop-color="#818cf8"/>
    </linearGradient>

    <!-- Filters -->
    <filter id="cov-glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="8" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>

    <filter id="cov-subtle-glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>

    <!-- Grid Pattern -->
    <pattern id="cov-grid" width="48" height="48" patternUnits="userSpaceOnUse">
      <path d="M 48 0 L 0 0 0 48" fill="none" stroke="rgba(99, 102, 241, 0.05)" stroke-width="1"/>
      <circle cx="48" cy="48" r="1.5" fill="rgba(99, 102, 241, 0.15)"/>
    </pattern>
  </defs>

  <style>
    .font-brand { font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; font-weight: 800; }
    .font-sub { font-family: 'Inter', sans-serif; font-weight: 500; }
    .font-mono { font-family: 'JetBrains Mono', 'Fira Code', monospace; }
  </style>

  <!-- Deep Base Background -->
  <rect width="1200" height="675" fill="#07080e"/>
  <rect width="1200" height="675" fill="url(#cov-grid)"/>
  <rect width="1200" height="675" fill="url(#cov-glow-left)"/>
  <rect width="1200" height="675" fill="url(#cov-glow-right)"/>

  <!-- Code Streams in Background (Watermarked Elegantly) -->
  <g class="font-mono" font-size="12" fill="rgba(148, 163, 184, 0.08)" letter-spacing="1">
    <text x="60" y="90">const app = express();</text>
    <text x="60" y="115">app.use(cors({ origin: 'https://phpwebspiders.com' }));</text>
    <text x="60" y="140">async function buildDigitalFuture(spec) {</text>
    <text x="90" y="165">const architecture = await deployMicroservices(spec);</text>
    <text x="90" y="190">return optimizeConversionRate(architecture);</text>
    <text x="60" y="215">}</text>

    <text x="980" y="470">import { scalableAPI } from "cloud";</text>
    <text x="980" y="495">SELECT * FROM solutions;</text>
    <text x="980" y="520">docker-compose up -d --build</text>
    <text x="980" y="545">Status: 200 OK [Latency: 12ms]</text>
  </g>

  <!-- ================= LEFT SIDE: DYNAMIC 3D SPIDER WEB NETWORK ================= -->
  <g transform="translate(190, 335)">
    <!-- Ambient Core Glow -->
    <circle cx="0" cy="0" r="180" fill="url(#cov-brand-grad)" opacity="0.12" filter="url(#cov-glow)"/>

    <!-- Concentric Hexagons -->
    <polygon points="0,-160 138,-80 138,80 0,160 -138,80 -138,-80"
             fill="none" stroke="rgba(99, 102, 241, 0.25)" stroke-width="1.5"/>
    <polygon points="0,-115 100,-57 100,57 0,115 -100,57 -100,-57"
             fill="rgba(30, 27, 75, 0.3)" stroke="rgba(56, 189, 248, 0.4)" stroke-width="1.5"/>
    <polygon points="0,-70 60,-35 60,35 0,70 -60,35 -60,-35"
             fill="rgba(99, 102, 241, 0.2)" stroke="url(#cov-brand-grad)" stroke-width="2"/>

    <!-- Radiant Web Strands -->
    <line x1="0" y1="-160" x2="0" y2="160" stroke="rgba(129, 140, 248, 0.4)" stroke-width="1.5"/>
    <line x1="138" y1="-80" x2="-138" y2="80" stroke="rgba(129, 140, 248, 0.4)" stroke-width="1.5"/>
    <line x1="138" y1="80" x2="-138" y2="-80" stroke="rgba(129, 140, 248, 0.4)" stroke-width="1.5"/>

    <!-- Cyber Spider Legs from Core -->
    <g stroke="url(#cov-brand-grad)" stroke-width="2.5" stroke-linecap="round" fill="none" filter="url(#cov-subtle-glow)">
      <path d="M -20 -20 L -60 -50 L -90 -45"/>
      <path d="M 20 -20 L 60 -50 L 90 -45"/>
      <path d="M -25 0 L -75 0 L -105 15"/>
      <path d="M 25 0 L 75 0 L 105 15"/>
      <path d="M -20 20 L -60 50 L -90 45"/>
      <path d="M 20 20 L 60 50 L 90 45"/>
    </g>

    <!-- Center Code Icon -->
    <circle cx="0" cy="0" r="26" fill="#0f172a" stroke="url(#cov-brand-grad)" stroke-width="2.5" filter="url(#cov-glow)"/>
    <g stroke="#ffffff" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" fill="none">
      <path d="M -8 -6 L -14 0 L -8 6"/>
      <path d="M 8 -6 L 14 0 L 8 6"/>
      <line x1="3" y1="-7" x2="-3" y2="7"/>
    </g>

    <!-- Network Glowing Nodes -->
    <g filter="url(#cov-glow)">
      <circle cx="0" cy="-160" r="5" fill="#38bdf8"/>
      <circle cx="138" cy="-80" r="5" fill="#818cf8"/>
      <circle cx="138" cy="80" r="5" fill="#c084fc"/>
      <circle cx="0" cy="160" r="5" fill="#38bdf8"/>
      <circle cx="-138" cy="80" r="5" fill="#818cf8"/>
      <circle cx="-138" cy="-80" r="5" fill="#c084fc"/>

      <circle cx="100" cy="-57" r="4" fill="#38bdf8"/>
      <circle cx="100" cy="57" r="4" fill="#c084fc"/>
      <circle cx="-100" cy="57" r="4" fill="#38bdf8"/>
      <circle cx="-100" cy="-57" r="4" fill="#818cf8"/>
    </g>
  </g>

  <!-- ================= RIGHT SIDE: BRAND HEADLINE & VALUE PROPOSITION ================= -->
  <g transform="translate(420, 160)">

    <!-- Availability & Verified Badge -->
    <g transform="translate(0, 30)">
      <rect x="0" y="0" width="235" height="32" rx="16" fill="rgba(99, 102, 241, 0.12)" stroke="rgba(99, 102, 241, 0.3)" stroke-width="1.2"/>
      <circle cx="18" cy="16" r="4.5" fill="#22c55e" filter="url(#cov-subtle-glow)"/>
      <text x="32" y="21" class="font-mono" font-size="12" fill="#c7d2fe" font-weight="600" letter-spacing="1">AVAILABLE FOR PROJECTS</text>
    </g>

    <!-- Main Title: PHPWebSpiders -->
    <text x="0" y="115" class="font-brand" font-size="64" letter-spacing="-0.5" filter="url(#cov-subtle-glow)">
      <tspan fill="#ffffff">PHP</tspan><tspan fill="url(#cov-brand-grad)">WebSpiders</tspan>
    </text>

    <!-- Subtitle / Mission Statement -->
    <text x="0" y="160" class="font-sub" font-size="22" fill="#94a3b8" font-weight="500">
      Full-Stack Web Development &amp; Scalable Cloud Architectures
    </text>

    <text x="0" y="195" class="font-sub" font-size="16" fill="#64748b" font-weight="400">
      Turning complex engineering challenges into blazing-fast digital products that drive growth.
    </text>

    <!-- Key Service Feature Pills -->
    <g transform="translate(0, 245)" class="font-mono" font-size="12.5">
      <!-- Web Apps -->
      <g transform="translate(0, 0)">
        <rect x="0" y="0" width="160" height="38" rx="8" fill="rgba(15, 23, 42, 0.8)" stroke="rgba(56, 189, 248, 0.3)" stroke-width="1"/>
        <text x="20" y="24" fill="#38bdf8">⚡ React / Next.js</text>
      </g>
      <!-- Backend & APIs -->
      <g transform="translate(172, 0)">
        <rect x="0" y="0" width="180" height="38" rx="8" fill="rgba(15, 23, 42, 0.8)" stroke="rgba(129, 140, 248, 0.3)" stroke-width="1"/>
        <text x="20" y="24" fill="#818cf8">⚙ Python / Node / PHP</text>
      </g>
      <!-- SaaS & Cloud -->
      <g transform="translate(364, 0)">
        <rect x="0" y="0" width="165" height="38" rx="8" fill="rgba(15, 23, 42, 0.8)" stroke="rgba(192, 132, 252, 0.3)" stroke-width="1"/>
        <text x="20" y="24" fill="#c084fc">☁ Cloud &amp; Microservices</text>
      </g>
      <!-- Mobile Apps -->
      <g transform="translate(541, 0)">
        <rect x="0" y="0" width="160" height="38" rx="8" fill="rgba(15, 23, 42, 0.8)" stroke="rgba(52, 211, 153, 0.3)" stroke-width="1"/>
        <text x="20" y="24" fill="#34d399">📱 React Native / iOS</text>
      </g>
    </g>

    <!-- Key Metrics / Proof Points -->
    <g transform="translate(0, 325)">
      <g transform="translate(0, 0)">
        <text x="0" y="22" class="font-brand" font-size="28" fill="#ffffff">8+</text>
        <text x="45" y="20" class="font-sub" font-size="13" fill="#94a3b8">Years Experience</text>
      </g>
      <line x1="180" y1="5" x2="180" y2="28" stroke="rgba(255,255,255,0.15)"/>
      <g transform="translate(205, 0)">
        <text x="0" y="22" class="font-brand" font-size="28" fill="#ffffff">50+</text>
        <text x="60" y="20" class="font-sub" font-size="13" fill="#94a3b8">Projects Delivered</text>
      </g>
      <line x1="410" y1="5" x2="410" y2="28" stroke="rgba(255,255,255,0.15)"/>
      <g transform="translate(435, 0)">
        <text x="0" y="22" class="font-brand" font-size="28" fill="#ffffff">100%</text>
        <text x="75" y="20" class="font-sub" font-size="13" fill="#94a3b8">Client Satisfaction</text>
      </g>
    </g>
  </g>

  <!-- Border Frame Accent Line at Bottom -->
  <rect x="0" y="670" width="1200" height="5" fill="url(#cov-brand-grad)"/>

</svg>'''
    return svg

# ==========================================
# 3. INTERACTIVE HTML PREVIEW & CANVAS PNG EXPORTER
# ==========================================
def create_preview_html():
    html = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>PHPWebSpiders — Google Business Profile Assets</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&family=JetBrains+Mono:wght@500;700&display=swap" rel="stylesheet">
  <style>
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      background: #090a10;
      color: #f1f5f9;
      font-family: 'Inter', sans-serif;
      padding: 40px 20px;
      min-height: 100vh;
    }
    .container { max-width: 1200px; margin: 0 auto; }
    header { text-align: center; margin-bottom: 50px; }
    h1 { font-size: 2.4rem; font-weight: 800; margin-bottom: 12px; }
    .gradient-text {
      background: linear-gradient(135deg, #38bdf8 0%, #818cf8 50%, #c084fc 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }
    p.lead { color: #94a3b8; font-size: 1.1rem; max-width: 680px; margin: 0 auto; }
    
    .card {
      background: #12131f;
      border: 1px solid rgba(129, 140, 248, 0.2);
      border-radius: 16px;
      padding: 32px;
      margin-bottom: 40px;
      box-shadow: 0 20px 50px rgba(0,0,0,0.4);
    }
    .card-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 24px;
      flex-wrap: wrap;
      gap: 16px;
    }
    .card-title h2 { font-size: 1.4rem; font-weight: 700; }
    .card-title span { font-size: 0.85rem; color: #818cf8; font-family: 'JetBrains Mono', monospace; }

    .btn-group { display: flex; gap: 12px; }
    .btn {
      padding: 10px 20px;
      border-radius: 8px;
      font-weight: 600;
      font-size: 0.9rem;
      cursor: pointer;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      transition: all 0.2s ease;
      border: none;
    }
    .btn-primary {
      background: linear-gradient(135deg, #38bdf8, #818cf8);
      color: #06070c;
    }
    .btn-primary:hover {
      box-shadow: 0 0 25px rgba(56, 189, 248, 0.4);
      transform: translateY(-2px);
    }
    .btn-outline {
      background: rgba(255,255,255,0.06);
      color: #f1f5f9;
      border: 1px solid rgba(255,255,255,0.15);
    }
    .btn-outline:hover { background: rgba(255,255,255,0.12); }

    .preview-box {
      border-radius: 12px;
      overflow: hidden;
      border: 1px solid rgba(255,255,255,0.08);
      background: #050508;
      display: flex;
      justify-content: center;
      align-items: center;
    }
    .preview-box img, .preview-box svg {
      width: 100%;
      height: auto;
      display: block;
    }
    
    .mockup-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 32px;
      margin-top: 40px;
    }
    @media (max-width: 900px) {
      .mockup-grid { grid-template-columns: 1fr; }
    }
    .mockup-card {
      background: #10121d;
      border: 1px solid rgba(255,255,255,0.08);
      border-radius: 14px;
      padding: 24px;
      text-align: center;
    }
    .circle-avatar {
      width: 180px;
      height: 180px;
      border-radius: 50%;
      overflow: hidden;
      margin: 0 auto 20px;
      border: 3px solid #818cf8;
      box-shadow: 0 0 35px rgba(129, 140, 248, 0.35);
    }
    .circle-avatar img { width: 100%; height: 100%; object-fit: cover; }
    
    .status-pill {
      display: inline-block;
      padding: 4px 12px;
      border-radius: 20px;
      font-size: 0.75rem;
      font-weight: 600;
      background: rgba(34, 197, 94, 0.15);
      color: #4ade80;
      margin-bottom: 12px;
    }
  </style>
</head>
<body>
  <div class="container">
    <header>
      <span class="status-pill">✦ GOOGLE BUSINESS PROFILE ASSETS</span>
      <h1><span class="gradient-text">PHPWebSpiders</span> Branding Kit</h1>
      <p class="lead">High-resolution logo &amp; cover photo crafted for Google Business Profile specifications.</p>
    </header>

    <!-- SECTION 1: LOGO (1:1 SQUARE) -->
    <div class="card">
      <div class="card-header">
        <div class="card-title">
          <h2>Profile Picture / Logo</h2>
          <span>Square 1:1 • 1024 × 1024 px (SVG + PNG)</span>
        </div>
        <div class="btn-group">
          <button class="btn btn-primary" onclick="exportToPng('logo-svg', 'google-business-logo.png', 1024, 1024)">
            ⬇ Download High-Res PNG
          </button>
          <a href="google-business-logo.svg" download class="btn btn-outline">⬇ Download SVG</a>
        </div>
      </div>
      <div class="preview-box" style="max-width: 520px; margin: 0 auto;">
        <img id="logo-svg" src="google-business-logo.svg" alt="PHPWebSpiders Logo" />
      </div>
    </div>

    <!-- SECTION 2: COVER PHOTO (16:9 LANDSCAPE) -->
    <div class="card">
      <div class="card-header">
        <div class="card-title">
          <h2>Google Business Profile Cover Photo</h2>
          <span>Landscape 16:9 • 1200 × 675 px (SVG + PNG)</span>
        </div>
        <div class="btn-group">
          <button class="btn btn-primary" onclick="exportToPng('cover-svg', 'google-business-cover.png', 1200, 675)">
            ⬇ Download High-Res PNG
          </button>
          <a href="google-business-cover.svg" download class="btn btn-outline">⬇ Download SVG</a>
        </div>
      </div>
      <div class="preview-box">
        <img id="cover-svg" src="google-business-cover.svg" alt="PHPWebSpiders Cover Photo" />
      </div>
    </div>

    <!-- SECTION 3: GOOGLE MOCKUP SIMULATION -->
    <div class="mockup-grid">
      <div class="mockup-card">
        <h3 style="margin-bottom: 16px; font-size: 1.1rem; color: #94a3b8;">Circular Avatar Preview (Google Search &amp; Maps)</h3>
        <div class="circle-avatar">
          <img src="google-business-logo.svg" alt="Google Maps Circle Preview" />
        </div>
        <h4 style="font-weight: 700; font-size: 1.2rem;">PHPWebSpiders</h4>
        <p style="color: #64748b; font-size: 0.9rem; margin-top: 4px;">Software company • Noida, UP</p>
      </div>

      <div class="mockup-card">
        <h3 style="margin-bottom: 16px; font-size: 1.1rem; color: #94a3b8;">Google Business Profile Specs Checklist</h3>
        <ul style="text-align: left; list-style: none; font-size: 0.9rem; line-height: 2; padding: 10px 20px; color: #cbd5e1;">
          <li>✓ <strong>Format:</strong> PNG &amp; SVG (Google accepts PNG &amp; JPG)</li>
          <li>✓ <strong>Logo Aspect:</strong> 1:1 Square (1024×1024 &gt; min 250×250)</li>
          <li>✓ <strong>Cover Aspect:</strong> 16:9 Landscape (1200×675 &gt; min 480×270)</li>
          <li>✓ <strong>Safe Area:</strong> Critical text centered to avoid mobile crop</li>
          <li>✓ <strong>Color Harmony:</strong> Matches your website dark neon theme</li>
        </ul>
      </div>
    </div>

  </div>

  <script>
    function exportToPng(imgId, filename, width, height) {
      const img = document.getElementById(imgId);
      const canvas = document.createElement('canvas');
      canvas.width = width;
      canvas.height = height;
      const ctx = canvas.getContext('2d');
      
      const newImg = new Image();
      newImg.crossOrigin = 'anonymous';
      newImg.onload = function() {
        ctx.drawImage(newImg, 0, 0, width, height);
        const a = document.createElement('a');
        a.download = filename;
        a.href = canvas.toDataURL('image/png');
        a.click();
      };
      newImg.src = img.src;
    }
  </script>
</body>
</html>'''
    return html

# ==========================================
# 4. PYTHON PURE RASTER PNG GENERATOR
# ==========================================
def write_png(filename, width, height, rgba_data):
    raw = bytearray()
    for y in range(height):
        raw.append(0)  # filter type 0 (None)
        start = y * width * 4
        raw.extend(rgba_data[start : start + width * 4])
    compressed = zlib.compress(bytes(raw), level=9)

    def chunk(chunk_type, data):
        return (
            struct.pack(">I", len(data))
            + chunk_type
            + data
            + struct.pack(">I", zlib.crc32(chunk_type + data) & 0xFFFFFFFF)
        )

    ihdr = struct.pack(">IIBBBBB", width, height, 8, 6, 0, 0, 0)
    with open(filename, "wb") as f:
        f.write(b"\x89PNG\r\n\x1a\n")
        f.write(chunk(b"IHDR", ihdr))
        f.write(chunk(b"IDAT", compressed))
        f.write(chunk(b"IEND", b""))

def generate_raster_logo_png():
    # 720 x 720 high-res raster logo
    w, h = 720, 720
    buf = bytearray(w * h * 4)
    cx, cy = w / 2, h / 2 - 20

    # Draw background radial gradient
    for y in range(h):
        for x in range(w):
            idx = (y * w + x) * 4
            dx = x - cx
            dy = y - cy
            dist = math.sqrt(dx * dx + dy * dy)
            t = min(1.0, dist / 450.0)
            
            # Subtle radial glow from #1e1b4b (30, 27, 75) to #06070c (6, 7, 12)
            r = int(30 * (1 - t) + 6 * t)
            g = int(27 * (1 - t) + 7 * t)
            b = int(75 * (1 - t) + 12 * t)
            buf[idx] = r
            buf[idx + 1] = g
            buf[idx + 2] = b
            buf[idx + 3] = 255

    # Helper function to blend RGBA pixel
    def blend(x, y, r, g, b, a):
        if 0 <= x < w and 0 <= y < h:
            idx = (y * w + x) * 4
            alpha = a / 255.0
            inv = 1.0 - alpha
            buf[idx] = int(buf[idx] * inv + r * alpha)
            buf[idx + 1] = int(buf[idx + 1] * inv + g * alpha)
            buf[idx + 2] = int(buf[idx + 2] * inv + b * alpha)

    # Draw anti-aliased line
    def draw_line(x0, y0, x1, y1, r, g, b, a=220, width=2):
        steps = int(max(abs(x1 - x0), abs(y1 - y0)) * 2)
        if steps == 0: return
        for i in range(steps + 1):
            px = x0 + (x1 - x0) * i / steps
            py = y0 + (y1 - y0) * i / steps
            for ox in range(-width, width + 1):
                for oy in range(-width, width + 1):
                    d = math.sqrt(ox * ox + oy * oy)
                    if d <= width:
                        falloff = max(0.0, 1.0 - d / width)
                        blend(int(px + ox), int(py + oy), r, g, b, int(a * falloff))

    # Draw glowing circle/node
    def draw_node(nx, ny, radius, r, g, b):
        ir = int(radius * 2.5)
        for oy in range(-ir, ir + 1):
            for ox in range(-ir, ir + 1):
                d = math.sqrt(ox * ox + oy * oy)
                if d <= ir:
                    falloff = max(0.0, 1.0 - d / (ir)) ** 1.8
                    blend(int(nx + ox), int(ny + oy), r, g, b, int(255 * falloff))
        # Bright center
        for oy in range(-int(radius), int(radius) + 1):
            for ox in range(-int(radius), int(radius) + 1):
                d = math.sqrt(ox * ox + oy * oy)
                if d <= radius:
                    blend(int(nx + ox), int(ny + oy), 255, 255, 255, 220)

    # Draw concentric hex web rings
    radii = [210, 150, 90, 45]
    for rad in radii:
        angles = [math.radians(60 * i - 30) for i in range(6)]
        points = [(cx + rad * math.cos(a), cy + rad * math.sin(a)) for a in angles]
        for i in range(6):
            p1 = points[i]
            p2 = points[(i + 1) % 6]
            draw_line(p1[0], p1[1], p2[0], p2[1], 129, 140, 248, 140, width=1)
            if rad == radii[0]:
                # Connect outer to center
                draw_line(cx, cy, p1[0], p1[1], 99, 102, 241, 100, width=1)
                draw_node(p1[0], p1[1], 4, 56, 189, 248)
            elif rad == radii[1]:
                draw_node(p1[0], p1[1], 3, 192, 132, 252)

    # Draw spider legs from center
    leg_coords = [
        # Top-left, top-right
        ((cx - 20, cy - 15), (cx - 60, cy - 65), (cx - 95, cy - 60)),
        ((cx + 20, cy - 15), (cx + 60, cy - 65), (cx + 95, cy - 60)),
        # Mid-left, mid-right
        ((cx - 25, cy), (cx - 80, cy - 5), (cx - 110, cy + 15)),
        ((cx + 25, cy), (cx + 80, cy - 5), (cx + 110, cy + 15)),
        # Lower-left, lower-right
        ((cx - 20, cy + 15), (cx - 60, cy + 65), (cx - 95, cy + 60)),
        ((cx + 20, cy + 15), (cx + 60, cy + 65), (cx + 95, cy + 60)),
    ]
    for seg1, seg2, seg3 in leg_coords:
        draw_line(seg1[0], seg1[1], seg2[0], seg2[1], 56, 189, 248, 200, width=2)
        draw_line(seg2[0], seg2[1], seg3[0], seg3[1], 192, 132, 252, 200, width=2)
        draw_node(seg3[0], seg3[1], 3, 255, 255, 255)

    # Draw Glowing Central Core
    draw_node(cx, cy, 14, 56, 189, 248)

    out_path = os.path.join(ASSETS_DIR, "google-business-logo.png")
    write_png(out_path, w, h, buf)
    print(f"Generated: {out_path} ({w}x{h})")

def generate_raster_cover_png():
    # 1024 x 576 landscape 16:9 raster cover
    w, h = 1024, 576
    buf = bytearray(w * h * 4)
    cx, cy = 200, h / 2

    # Fill base gradient
    for y in range(h):
        for x in range(w):
            idx = (y * w + x) * 4
            # Dark tech gradient with subtle violet glow towards left
            dx = x - cx
            dy = y - cy
            dist = math.sqrt(dx * dx + dy * dy)
            t = min(1.0, dist / 600.0)
            
            r = int(35 * (1 - t) + 7 * t)
            g = int(30 * (1 - t) + 8 * t)
            b = int(85 * (1 - t) + 14 * t)
            buf[idx] = r
            buf[idx + 1] = g
            buf[idx + 2] = b
            buf[idx + 3] = 255

    def blend(x, y, r, g, b, a):
        if 0 <= x < w and 0 <= y < h:
            idx = (y * w + x) * 4
            alpha = a / 255.0
            inv = 1.0 - alpha
            buf[idx] = int(buf[idx] * inv + r * alpha)
            buf[idx + 1] = int(buf[idx + 1] * inv + g * alpha)
            buf[idx + 2] = int(buf[idx + 2] * inv + b * alpha)

    def draw_line(x0, y0, x1, y1, r, g, b, a=200, width=2):
        steps = int(max(abs(x1 - x0), abs(y1 - y0)) * 2)
        if steps == 0: return
        for i in range(steps + 1):
            px = x0 + (x1 - x0) * i / steps
            py = y0 + (y1 - y0) * i / steps
            for ox in range(-width, width + 1):
                for oy in range(-width, width + 1):
                    d = math.sqrt(ox * ox + oy * oy)
                    if d <= width:
                        falloff = max(0.0, 1.0 - d / width)
                        blend(int(px + ox), int(py + oy), r, g, b, int(a * falloff))

    def draw_node(nx, ny, radius, r, g, b):
        ir = int(radius * 2.5)
        for oy in range(-ir, ir + 1):
            for ox in range(-ir, ir + 1):
                d = math.sqrt(ox * ox + oy * oy)
                if d <= ir:
                    falloff = max(0.0, 1.0 - d / (ir)) ** 1.8
                    blend(int(nx + ox), int(ny + oy), r, g, b, int(255 * falloff))
        for oy in range(-int(radius), int(radius) + 1):
            for ox in range(-int(radius), int(radius) + 1):
                d = math.sqrt(ox * ox + oy * oy)
                if d <= radius:
                    blend(int(nx + ox), int(ny + oy), 255, 255, 255, 220)

    # Draw spider matrix on left side
    radii = [150, 100, 50]
    for rad in radii:
        angles = [math.radians(60 * i - 30) for i in range(6)]
        points = [(cx + rad * math.cos(a), cy + rad * math.sin(a)) for a in angles]
        for i in range(6):
            p1 = points[i]
            p2 = points[(i + 1) % 6]
            draw_line(p1[0], p1[1], p2[0], p2[1], 129, 140, 248, 120, width=1)
            if rad == radii[0]:
                draw_line(cx, cy, p1[0], p1[1], 99, 102, 241, 90, width=1)
                draw_node(p1[0], p1[1], 4, 56, 189, 248)
            elif rad == radii[1]:
                draw_node(p1[0], p1[1], 3, 192, 132, 252)

    draw_node(cx, cy, 12, 56, 189, 248)

    # Bottom accent gradient bar
    for x in range(w):
        for y in range(h - 4, h):
            t = x / w
            r = int(56 * (1 - t) + 192 * t)
            g = int(189 * (1 - t) + 132 * t)
            b = int(248 * (1 - t) + 252 * t)
            blend(x, y, r, g, b, 255)

    out_path = os.path.join(ASSETS_DIR, "google-business-cover.png")
    write_png(out_path, w, h, buf)
    print(f"Generated: {out_path} ({w}x{h})")

def main():
    # 1. SVGs
    logo_svg = create_logo_svg()
    with open(os.path.join(ASSETS_DIR, "google-business-logo.svg"), "w") as f:
        f.write(logo_svg)
    print("Created google-business-logo.svg")

    cover_svg = create_cover_svg()
    with open(os.path.join(ASSETS_DIR, "google-business-cover.svg"), "w") as f:
        f.write(cover_svg)
    print("Created google-business-cover.svg")

    # 2. Raster PNGs
    generate_raster_logo_png()
    generate_raster_cover_png()
    print("All assets generated successfully!")

if __name__ == "__main__":
    main()

