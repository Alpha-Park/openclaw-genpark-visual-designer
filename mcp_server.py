# -*- coding: utf-8 -*-
"""
OpenClaw GenPark Visual Designer MCP Server
FastMCP standard interface for golden ratio typography, WCAG contrast auditing, and triadic palette generation.
"""

import json
from typing import Dict, Any, Optional
from client import OpenClawGenParkVisualDesigner

try:
    from mcp.server.fastmcp import FastMCP
    mcp = FastMCP("openclaw-genpark-visual-designer")
except ImportError:
    class MockFastMCP:
        def __init__(self, name):
            self.name = name
        def tool(self):
            def decorator(f):
                return f
            return decorator
    mcp = MockFastMCP("openclaw-genpark-visual-designer")

designer = OpenClawGenParkVisualDesigner()

@mcp.tool()
def calculate_golden_ratio_typography_scale(
    base_font_size_px: float = 16.0,
    scale_ratio: Optional[float] = None
) -> str:
    """
    Calculates modular typography scale based on Golden Ratio phi.
    """
    res = designer.calculate_golden_ratio_typography_scale(base_font_size_px, scale_ratio)
    return json.dumps(res, indent=2)

@mcp.tool()
def evaluate_wcag_color_contrast_ratio(
    foreground_hex: str,
    background_hex: str
) -> str:
    """
    Calculates WCAG 2.1 color contrast ratio and evaluates AA/AAA compliance.
    """
    res = designer.evaluate_wcag_color_contrast_ratio(foreground_hex, background_hex)
    return json.dumps(res, indent=2)

@mcp.tool()
def generate_triadic_color_palette(
    seed_hue_degrees: float = 210.0,
    saturation: float = 0.8,
    lightness: float = 0.5
) -> str:
    """
    Generates 3 harmonized triadic color hues on the color wheel.
    """
    res = designer.generate_triadic_color_palette(seed_hue_degrees, saturation, lightness)
    return json.dumps(res, indent=2)

def main():
    print("Testing Visual Designer:")
    print(evaluate_wcag_color_contrast_ratio("#000000", "#ffffff"))

if __name__ == "__main__":
    main()
