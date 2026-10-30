# -*- coding: utf-8 -*-
from client import OpenClawGenParkVisualDesigner

designer = OpenClawGenParkVisualDesigner()

# 1. Golden Ratio Typography
typo = designer.calculate_golden_ratio_typography_scale(base_font_size_px=16.0)
print(f"Golden Ratio Typography: Base={typo['base_font_size_px']}px (Ratio={typo['scale_ratio']})")
for tag, sz in typo['typography_hierarchy_px'].items():
    print(f"  {tag.upper()}: {sz}px (Line Height: {typo['line_heights_px'][tag]}px)")

# 2. WCAG Contrast Check
contrast = designer.evaluate_wcag_color_contrast_ratio("#1e293b", "#ffffff")
print()
print(f"WCAG Contrast: Ratio={contrast['contrast_ratio']}:1 ({contrast['compliance_rating']}, AA={contrast['wcag_aa_normal']}, AAA={contrast['wcag_aaa_normal']})")

# 3. Triadic Harmony Palette
triad = designer.generate_triadic_color_palette(seed_hue_degrees=215.0, saturation=0.85, lightness=0.48)
print()
print(f"Triadic Palette: Primary={triad['primary_hex']}, Secondary={triad['secondary_hex']}, Accent={triad['accent_hex']}")
