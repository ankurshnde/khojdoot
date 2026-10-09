"""
Merchant Site Publisher.
Generates self-contained static site and all machine-readable crawlable discoverability assets.
"""
import os
import json
from typing import Dict, Any
from app.config import settings
from app.website.generator import generate_website
from app.publishing.business_json import generate_business_json
from app.publishing.agentfacts import generate_agentfacts
from app.publishing.agent_card import generate_agent_card
from app.publishing.llms import generate_llms_txt, generate_llms_full_txt
from app.publishing.robots import generate_robots_txt
from app.publishing.sitemap import generate_sitemap


def publish_merchant_html(slug: str, spec: Dict[str, Any], infobin: Dict[str, Any]) -> str:
    """
    Publishes the merchant website and generates the complete discoverable asset bundle:
    - index.html (Semantic HTML with JSON-LD)
    - facts.json (Direct business attributes)
    - agentfacts.json (AgentFacts Protocol specification)
    - llms.txt (Concise context for LLMs & AI crawlers)
    - llms-full.txt (Full catalog & service detail context)
    - robots.txt (Crawler guidance pointing to sitemap)
    - sitemap.xml (SEO indexing map)
    - agent-card.json (Agent-to-Agent discovery manifest)
    """
    html = generate_website(spec, infobin)
    out_dir = os.path.join(settings.GENERATED_DIR, slug)
    os.makedirs(out_dir, exist_ok=True)

    base_url = settings.BASE_URL

    # 1. Main Website HTML
    index_path = os.path.join(out_dir, "index.html")
    with open(index_path, "w", encoding="utf-8") as f:
        f.write(html)

    # 2. facts.json
    facts_data = generate_business_json(infobin)
    with open(os.path.join(out_dir, "facts.json"), "w", encoding="utf-8") as f:
        json.dump(facts_data, f, ensure_ascii=False, indent=2)

    # 3. agentfacts.json
    agentfacts_data = generate_agentfacts(infobin)
    with open(os.path.join(out_dir, "agentfacts.json"), "w", encoding="utf-8") as f:
        json.dump(agentfacts_data, f, ensure_ascii=False, indent=2)

    # 4. agent-card.json
    agent_card_data = generate_agent_card(infobin)
    with open(os.path.join(out_dir, "agent-card.json"), "w", encoding="utf-8") as f:
        json.dump(agent_card_data, f, ensure_ascii=False, indent=2)

    # 5. llms.txt & llms-full.txt
    with open(os.path.join(out_dir, "llms.txt"), "w", encoding="utf-8") as f:
        f.write(generate_llms_txt(infobin))

    with open(os.path.join(out_dir, "llms-full.txt"), "w", encoding="utf-8") as f:
        f.write(generate_llms_full_txt(infobin))

    # 6. robots.txt & sitemap.xml
    with open(os.path.join(out_dir, "robots.txt"), "w", encoding="utf-8") as f:
        f.write(generate_robots_txt(base_url=f"{base_url}/merchant/{slug}"))

    with open(os.path.join(out_dir, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(generate_sitemap(slug=slug, base_url=base_url))

    return index_path
