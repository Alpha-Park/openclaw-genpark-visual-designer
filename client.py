# -*- coding: utf-8 -*-
"""
OpenClaw GenPark Visual Designer Client
Pure Python Standard Library (Zero External Dependencies)
Implements Golden Ratio (phi = 1.618) typography scale hierarchy,
WCAG 2.1 relative luminance color contrast ratio auditing, and triadic color harmony generation.
"""

import math
from typing import Dict, Any, List, Optional, Tuple

class OpenClawGenParkVisualDesigner:
    """
    Algorithmic UI design system, typography scale, and color harmony engine.
    """

    def __init__(self):
        self.phi = (1.0 + math.sqrt(5.0)) / 2.0  # 1.6180339887...

    def calculate_golden_ratio_typography_scale(
        self,
        base_font_size_px: float = 16.0,
        scale_ratio: Optional[float] = None
    ) -> Dict[str, Any]:
        """
        Calculates modular typography scale based on Golden Ratio phi or custom geometric ratio:
          Font_Size = Base * (Ratio ^ Step)
        """
        r = scale_ratio if scale_ratio is not None else self.phi

        scale = {
            "display": round(base_font_size_px * (r ** 3), 1),
            "h1": round(base_font_size_px * (r ** 2), 1),
            "h2": round(base_font_size_px * (r ** 1.5), 1),
            "h3": round(base_font_size_px * r, 1),
            "body": round(base_font_size_px, 1),
            "small": round(base_font_size_px / r, 1),
            "caption": round(base_font_size_px / (r ** 1.5), 1)
        }

        line_heights = {
            k: round(v * 1.35, 1) if v > 24 else round(v * 1.5, 1)
            for k, v in scale.items()
        }

        return {
            "base_font_size_px": base_font_size_px,
            "scale_ratio": round(r, 4),
            "typography_hierarchy_px": scale,
            "line_heights_px": line_heights
        }

    def _hex_to_rgb(self, hex_str: str) -> Tuple[int, int, int]:
        clean = hex_str.lstrip("#")
        if len(clean) == 3:
            clean = "".join([c * 2 for c in clean])
        val = int(clean, 16)
        return ((val >> 16) & 255, (val >> 8) & 255, val & 255)

    def _relative_luminance(self, r: int, g: int, b: int) -> float:
        """
        Calculates sRGB relative luminance according to WCAG 2.1 specs:
          C_srgb = C / 255.0
          C_lin = C_srgb / 12.92 if C_srgb <= 0.03928 else ((C_srgb + 0.055) / 1.055) ^ 2.4
          L = 0.2126 * R_lin + 0.7152 * G_lin + 0.0722 * B_lin
        """
        def to_lin(c):
            c_s = c / 255.0
            return c_s / 12.92 if c_s <= 0.03928 else ((c_s + 0.055) / 1.055) ** 2.4

        return 0.2126 * to_lin(r) + 0.7152 * to_lin(g) + 0.0722 * to_lin(b)

    def evaluate_wcag_color_contrast_ratio(
        self,
        foreground_hex: str,
        background_hex: str
    ) -> Dict[str, Any]:
        """
        Calculates WCAG 2.1 color contrast ratio:
          Contrast = (L1 + 0.05) / (L2 + 0.05) where L1 > L2
        Evaluates AA (4.5:1), AAA (7.0:1), and Large Text (3.0:1).
        """
        r1, g1, b1 = self._hex_to_rgb(foreground_hex)
        r2, g2, b2 = self._hex_to_rgb(background_hex)

        lum1 = self._relative_luminance(r1, g1, b1)
        lum2 = self._relative_luminance(r2, g2, b2)

        lighter = max(lum1, lum2)
        darker = min(lum1, lum2)

        contrast = (lighter + 0.05) / (darker + 0.05)
        contrast = round(contrast, 2)

        pass_aa_normal = contrast >= 4.5
        pass_aa_large = contrast >= 3.0
        pass_aaa_normal = contrast >= 7.0
        pass_aaa_large = contrast >= 4.5

        return {
            "foreground_hex": foreground_hex,
            "background_hex": background_hex,
            "contrast_ratio": contrast,
            "wcag_aa_normal": pass_aa_normal,
            "wcag_aa_large": pass_aa_large,
            "wcag_aaa_normal": pass_aaa_normal,
            "wcag_aaa_large": pass_aaa_large,
            "compliance_rating": "AAA_EXCELLENT" if pass_aaa_normal else ("AA_COMPLIANT" if pass_aa_normal else "FAIL_INSUFFICIENT_CONTRAST")
        }

    def generate_triadic_color_palette(
        self,
        seed_hue_degrees: float = 210.0,
        saturation: float = 0.8,
        lightness: float = 0.5
    ) -> Dict[str, Any]:
        """
        Generates 3 harmonized triadic color hues on the color wheel:
          H1 = seed, H2 = (seed + 120) % 360, H3 = (seed + 240) % 360
        Converts HSL to Hex.
        """
        def hsl_to_hex(h, s, l):
            c = (1.0 - abs(2.0 * l - 1.0)) * s
            x = c * (1.0 - abs((h / 60.0) % 2.0 - 1.0))
            m = l - c / 2.0

            if 0 <= h < 60:
                r1, g1, b1 = c, x, 0
            elif 60 <= h < 120:
                r1, g1, b1 = x, c, 0
            elif 120 <= h < 180:
                r1, g1, b1 = 0, c, x
            elif 180 <= h < 240:
                r1, g1, b1 = 0, x, c
            elif 240 <= h < 300:
                r1, g1, b1 = x, 0, c
            else:
                r1, g1, b1 = c, 0, x

            r = round((r1 + m) * 255)
            g = round((g1 + m) * 255)
            b = round((b1 + m) * 255)
            return f"#{r:02x}{g:02x}{b:02x}"

        h1 = seed_hue_degrees % 360.0
        h2 = (seed_hue_degrees + 120.0) % 360.0
        h3 = (seed_hue_degrees + 240.0) % 360.0

        return {
            "primary_hex": hsl_to_hex(h1, saturation, lightness),
            "secondary_hex": hsl_to_hex(h2, saturation, lightness),
            "accent_hex": hsl_to_hex(h3, saturation, lightness),
            "triadic_hues_deg": [round(h1, 1), round(h2, 1), round(h3, 1)]
        }
