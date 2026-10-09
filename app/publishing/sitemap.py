"""Sitemap XML Generator."""
def generate_sitemap(slug: str, base_url: str = "http://localhost:8000") -> str:
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    <url>
        <loc>{base_url}/merchant/{slug}</loc>
        <changefreq>daily</changefreq>
        <priority>1.0</priority>
    </url>
</urlset>
"""
