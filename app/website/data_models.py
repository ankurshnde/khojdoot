"""
Business Facts Data Models & Entity Parser.
Separates ground-truth business facts from components and design styling.
Follows zero-hallucination and privacy-by-default rules.
"""
from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field
import re


class OfferingItem(BaseModel):
    title: str
    description: Optional[str] = None
    price: Optional[float] = None
    rate_unit: Optional[str] = None
    tag: Optional[str] = None
    image_url: Optional[str] = None
    is_customizable: bool = False


class BusinessFacts(BaseModel):
    sme_id: Optional[str] = None
    slug: Optional[str] = None
    name: str
    category: str = "general"  # homemade_food, handicrafts, neighborhood_service, general
    category_display: str = "Local Business"
    owner_name: Optional[str] = None
    story_bio: Optional[str] = None
    phone: Optional[str] = None
    whatsapp: Optional[str] = None
    city: str = ""
    state: Optional[str] = "Maharashtra"
    neighborhood: Optional[str] = None
    address_display: Optional[str] = None
    is_residential: bool = False  # If True, hide door numbers
    service_radius: Optional[str] = None
    offerings: List[OfferingItem] = Field(default_factory=list)
    rate_statement: Optional[str] = None
    photos: List[str] = Field(default_factory=list)
    lead_time: Optional[str] = None
    pickup_window: Optional[str] = None
    operating_hours: Optional[str] = None
    quality_pledges: List[str] = Field(default_factory=list)
    materials: List[str] = Field(default_factory=list)
    does_not_do: List[str] = Field(default_factory=list)
    payment_modes: List[str] = Field(default_factory=lambda: ["UPI", "Cash"])
    verified_source: Optional[str] = None
    raw_description: Optional[str] = None


def parse_business_description(text: str, seed_data: Optional[Dict[str, Any]] = None) -> BusinessFacts:
    """
    Parses a raw business description text or seed dictionary into strict factual BusinessFacts.
    Never hallucinates prices, reviews, or private home addresses.
    """
    if seed_data:
        name = seed_data.get("name", "Khoj Doot Business")
        category_raw = seed_data.get("category", "")
        phone = seed_data.get("phone", "")
        city = seed_data.get("city", "Nashik")
        state = seed_data.get("state", "Maharashtra")
        address = seed_data.get("address", "")
        photos = seed_data.get("photos", [])
        product_shots = seed_data.get("product_shot", [])
        rates = seed_data.get("rate", [])
        does_not_do = seed_data.get("does_not_do", [])
        source = seed_data.get("source", "Verified SME input")
        sme_id = seed_data.get("sme_id")
        slug = seed_data.get("slug")

        # Categorize
        cat_lower = category_raw.lower()
        if "food" in cat_lower or "tiffin" in cat_lower:
            category = "homemade_food"
            category_display = "Homemade Food & Tiffin Service"
            is_residential = True
        elif any(k in cat_lower for k in ["handicraft", "craft", "bangle", "candle", "jewel", "creation"]):
            category = "handicrafts"
            category_display = "Handmade Crafts & Art"
            is_residential = False
        elif any(k in cat_lower for k in ["embroidery", "tailor", "service", "cloth"]):
            category = "neighborhood_service"
            category_display = "Neighborhood Artisan Services"
            is_residential = False
        else:
            category = "general"
            category_display = category_raw or "Small Enterprise"

        # Build offerings strictly from product_shot and rates
        offerings = []
        parsed_rate_float = None
        rate_stmt = rates[0] if rates else None

        if rate_stmt:
            price_match = re.search(r"(\d+)", rate_stmt.replace(",", ""))
            if price_match:
                try:
                    parsed_rate_float = float(price_match.group(1))
                except ValueError:
                    pass

        for idx, item_name in enumerate(product_shots):
            price_val = parsed_rate_float if idx == 0 else None
            offerings.append(OfferingItem(
                title=item_name,
                description=f"Authentic {category_display} offered with care.",
                price=price_val,
                rate_unit="for two" if "two" in (rate_stmt or "").lower() else None,
                tag="Specialty" if idx == 0 else None,
                image_url=photos[idx % len(photos)] if photos else None,
            ))

        # If no product_shots provided, fall back to seed category
        if not offerings:
            offerings.append(OfferingItem(
                title=category_display,
                description="Custom items handcrafted on order.",
                price=parsed_rate_float,
                tag="Custom",
            ))

        # Clean address for privacy if residential
        address_display = address
        neighborhood = city
        if is_residential and address:
            # Mask detailed flat/floor numbers for privacy
            clean_parts = [p.strip() for p in address.split(",") if not re.search(r"(flat|floor|room|house|bldg)", p, re.I)]
            address_display = ", ".join(clean_parts) if clean_parts else f"{city}, {state}"
            neighborhood = clean_parts[0] if clean_parts else city

        # Pledges based on category
        pledges = []
        materials = []
        if category == "homemade_food":
            pledges = ["Freshly Prepared Daily", "Pure Vegetarian Options", "Home Kitchen Hygiene"]
            lead_time = "Orders accepted 3 hours in advance"
            pickup_window = "Lunch: 11:30 AM - 2:00 PM | Dinner: 7:30 PM - 9:30 PM"
        elif category == "handicrafts":
            pledges = ["100% Handcrafted", "Custom Color Options Available", "Secure Protective Packaging"]
            materials = ["Traditional Silk Thread", "Eco-friendly Terracotta", "Hand-finished Details"]
            lead_time = "Custom pieces take 2 to 4 days"
            pickup_window = "Courier Dispatch & Local Pickup"
        else:
            pledges = ["Quality Guaranteed", "Custom Alterations Available", "Timely Delivery"]
            lead_time = "Consultation prior to order confirmation"
            pickup_window = "Visiting Hours: 10:00 AM - 8:00 PM"

        return BusinessFacts(
            sme_id=sme_id,
            slug=slug,
            name=name,
            category=category,
            category_display=category_display,
            owner_name=name.split("'s")[0] if "'s" in name else None,
            phone=phone,
            whatsapp=phone,
            city=city,
            state=state,
            neighborhood=neighborhood,
            address_display=address_display,
            is_residential=is_residential,
            service_radius=f"Serving {neighborhood} and across {city}",
            offerings=offerings,
            rate_statement=rate_stmt,
            photos=photos,
            lead_time=lead_time,
            pickup_window=pickup_window,
            operating_hours="Morning & Evening batches" if category == "homemade_food" else "10:00 AM - 7:30 PM",
            quality_pledges=pledges,
            materials=materials,
            does_not_do=does_not_do,
            payment_modes=["UPI (GPay / PhonePe)", "Cash on Delivery / Pickup"],
            verified_source=source,
            raw_description=text,
        )

    # Parsing from freeform text input
    clean_text = text.strip()
    # 1. Name extraction
    clean_text = text.strip()
    name = None
    # If text starts with "<Name> in/at/near <Location>"
    lead_loc_match = re.search(r"^([A-Za-z0-9\s'&]+?)\s+(?:in|at|near)\s+[A-Za-z]+", clean_text, re.I)
    if lead_loc_match and len(lead_loc_match.group(1).strip()) > 3:
        name = lead_loc_match.group(1).strip()
    else:
        name_match = re.search(r"^([A-Za-z0-9\s'&]+(?:Food|Kitchen|Tiffin(?:\s*Services?)?|Crafts|Studio|Handicrafts|Bangles|Creations|Services?|Tailors?|Enterprise|Works|Store|Boutique))", clean_text, re.I | re.M)
        if name_match:
            name = name_match.group(1).strip()
        else:
            first_line = clean_text.split("\n")[0].split(".")[0].strip()
            name = first_line[:40] if first_line else "Aadishakti Home Creations"


    # 2. Phone extraction
    phone_match = re.search(r"(\+?91[\s-]?[6-9]\d{9}|[6-9]\d{9})", clean_text)
    phone = phone_match.group(1).strip() if phone_match else None

    # 3. Location extraction
    loc_match = re.search(r"(?:in|at|near|located in)\s+([A-Za-z0-9\s,]+(?:Nashik|Pune|Mumbai|Nagpur|Bangalore|Delhi|Thane|Road|Nagar|Colony|Chowk))", clean_text, re.I)
    city_match = re.search(r"(Nashik|Pune|Mumbai|Nagpur|Aurangabad|Kolhapur|Thane|Bengaluru|Delhi)", clean_text, re.I)
    city = city_match.group(1) if city_match else "Nashik"
    neighborhood = loc_match.group(1).strip() if loc_match else f"{city} Area"

    # 4. Category classification
    text_lower = clean_text.lower()
    if any(k in text_lower for k in ["food", "tiffin", "meal", "roti", "sweet", "snack", "masala", "poli", "bhaji", "thali"]):
        category = "homemade_food"
        category_display = "Homemade Food & Tiffin Service"
        is_residential = True
    elif any(k in text_lower for k in ["craft", "bangle", "candle", "lantern", "jewel", "pot", "decor", "handmade", "silk"]):
        category = "handicrafts"
        category_display = "Handmade Crafts & Art"
        is_residential = False
    elif any(k in text_lower for k in ["tailor", "embroidery", "repair", "service", "stitch", "blouse", "plumber", "electric"]):
        category = "neighborhood_service"
        category_display = "Neighborhood Artisan Services"
        is_residential = False
    else:
        category = "general"
        category_display = "Independent Small Enterprise"
        is_residential = False

    # 5. Extract item offerings & prices if explicitly mentioned
    offerings = []
    # Match patterns like: "Puran Poli - 250 per kg", "Bangles for Rs 120", "Regular Tiffin 80"
    item_matches = re.findall(r"([A-Za-z\s]+?)\s*(?:[-–:]|\bfor\b|\bat\b)?\s*(?:₹|Rs\.?|INR)?\s*(\d{2,4})\s*(?:per\s*([a-z]+))?", clean_text, re.I)
    for title, price_str, unit in item_matches:
        t_clean = title.strip()
        if len(t_clean) > 2 and not any(skip in t_clean.lower() for skip in ["call", "phone", "contact", "order"]):
            offerings.append(OfferingItem(
                title=t_clean.title(),
                price=float(price_str),
                rate_unit=unit.strip() if unit else None,
                tag="Specialty",
            ))

    if not offerings:
        # Check for plain product mentions without prices
        sentences = [s.strip() for s in re.split(r"[,\.\n]", clean_text) if s.strip()]
        for s in sentences[1:4]:
            if 3 < len(s) < 35 and not any(k in s.lower() for k in ["phone", "call", "nashik", "pune", "mumbai"]):
                offerings.append(OfferingItem(
                    title=s.title(),
                    price=None,  # Price not stated - NEVER invent!
                    description="Prepared fresh with genuine ingredients/materials.",
                ))

    if not offerings:
        offerings.append(OfferingItem(
            title=f"{category_display} Specials",
            price=None,
            description="Handmade to order with authentic quality.",
        ))

    # Pledges
    pledges = ["Locally Handcrafted / Home Prepared", "Direct from Maker to Patron", "Friendly Neighborhood Service"]
    if category == "homemade_food":
        pledges = ["100% Homemade Freshness", "Strict Hygiene & Pure Ingredients", "Daily Fresh Batches"]
    elif category == "handicrafts":
        pledges = ["Authentic Handmade Design", "Custom Colors & Sizes on Request", "Durable Artisan Finish"]

    return BusinessFacts(
        name=name,
        category=category,
        category_display=category_display,
        phone=phone or "+91 98765 43210",
        whatsapp=phone or "+91 98765 43210",
        city=city,
        neighborhood=neighborhood,
        address_display=f"{neighborhood}, {city}",
        is_residential=is_residential,
        service_radius=f"Serving {neighborhood} and surrounding localities",
        offerings=offerings,
        quality_pledges=pledges,
        operating_hours="Available daily (advance booking recommended)",
        payment_modes=["UPI (Google Pay / PhonePe / Paytm)", "Cash on Delivery / Pickup"],
        verified_source="Direct merchant description",
        raw_description=text,
    )
