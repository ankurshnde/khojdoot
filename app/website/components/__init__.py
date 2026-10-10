"""KhojDoot Bounded Website Components Library.
Adheres to docs/DESIGN.md & PS-29 Regional Architecture.
"""
from app.website.components.hero import render_hero
from app.website.components.products import render_products
from app.website.components.location import render_location
from app.website.components.contact import render_contact
from app.website.components.footer import render_footer
from app.website.components.fab import render_fab

__all__ = [
    "render_hero",
    "render_products",
    "render_location",
    "render_contact",
    "render_footer",
    "render_fab",
]
