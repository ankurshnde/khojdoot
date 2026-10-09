"""Robots.txt Generator."""
def generate_robots_txt(base_url: str = "http://localhost:8000") -> str:
    return f"""User-agent: *
Allow: /
Sitemap: {base_url}/sitemap.xml
"""
