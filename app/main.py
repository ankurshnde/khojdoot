from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from app.db.connection import init_db
from app.db.crud import (
    get_shop,
    create_shop,
    update_shop,
    save_infobin,
    get_infobin,
    get_facts,
    update_status,
    get_status,
    save_provenance,
    get_provenance,
    save_photo,
    get_photos,
    save_consent,
    get_consent,
    save_website_spec,
    get_website_specs,
)

from app.routes.projects import router as projects_router
from app.routes.generate import router as generate_router
from app.routes.auth import router as auth_router


app = FastAPI(
    title="KhojDoot API",
    description="Regional-language no-code website builder",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Restrict before production
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize the database
init_db()

# Register AI generation and project routes
app.include_router(generate_router)
app.include_router(projects_router)
app.include_router(auth_router)


class Shop(BaseModel):
    sme_id: str
    slug: str
    name: str
    phone: str
    city: str
    updated_at: str


class InfoBin(BaseModel):
    bin_type: str
    data: dict


class Status(BaseModel):
    status: str


class Provenance(BaseModel):
    field_name: str
    source_type: str
    confidence: float
    confirmed: bool


class Photo(BaseModel):
    filename: str
    source: str | None = None


class Consent(BaseModel):
    consent_type: str
    approved_at: str
    payload_hash: str


class WebsiteSpec(BaseModel):
    version: int
    spec_data: dict
    validation_score: float | None = None
    status: str


@app.get("/")
def home():
    return {
        "message": "Welcome to KhojDoot API!",
        "status": "running",
    }


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/shop/{slug}")
def shop(slug: str):
    data = get_shop(slug)

    if data is None:
        return {"message": "Shop not found"}

    return dict(data)


@app.get("/b/{slug}")
def get_public_shop(slug: str, language: str = "en"):
    shop_data = get_shop(slug)

    if shop_data is None:
        return {"message": "Shop not found"}

    facts = get_facts(shop_data["id"], language)
    photos = get_photos(shop_data["id"])

    return {
        "slug": shop_data["slug"],
        "business_name": shop_data["name"],
        "city": shop_data["city"],
        "language": language,
        "facts": facts,
        "photos": [dict(photo) for photo in photos],
    }


@app.get("/b/{slug}/facts")
def get_shop_facts(slug: str, language: str = "en"):
    shop_data = get_shop(slug)

    if shop_data is None:
        return {"message": "Shop not found"}

    return get_facts(shop_data["id"], language)


@app.post("/shops")
@app.post("/smes")
def add_shop(shop: Shop):
    shop_id = create_shop(
        shop.sme_id,
        shop.slug,
        shop.name,
        shop.phone,
        shop.city,
        shop.updated_at,
    )

    return {"id": shop_id, "message": "Shop created"}


@app.put("/shops/{slug}")
def edit_shop(slug: str, shop: Shop):
    if get_shop(slug) is None:
        return {"message": "Shop not found"}

    update_shop(
        slug,
        shop.name,
        shop.phone,
        shop.city,
        shop.updated_at,
    )

    return {"message": "Shop updated"}


@app.post("/smes/{slug}/bins")
def add_infobin(slug: str, bin: InfoBin, language: str = "en"):
    shop_data = get_shop(slug)

    if shop_data is None:
        return {"message": "Shop not found"}

    save_infobin(
        shop_data["id"],
        bin.bin_type,
        language,
        bin.data,
    )

    return {
        "message": "InfoBin saved",
        "shop_id": shop_data["id"],
        "bin_type": bin.bin_type,
        "language": language,
    }


@app.get("/smes/{slug}/bins/{bin_type}")
def get_infobin_data(
    slug: str,
    bin_type: str,
    language: str = "en",
):
    shop_data = get_shop(slug)

    if shop_data is None:
        return {"message": "Shop not found"}

    data = get_infobin(
        shop_data["id"],
        bin_type,
        language,
    )

    if data is None:
        return {"message": "InfoBin not found"}

    return {
        "shop_id": shop_data["id"],
        "bin_type": bin_type,
        "language": language,
        "data": data,
    }


@app.get("/smes/{slug}/status")
def get_shop_status(slug: str):
    status = get_status(slug)

    if status is None:
        return {"message": "Shop not found"}

    return {"status": status}


@app.put("/smes/{slug}/status")
def change_shop_status(slug: str, status: Status):
    if get_shop(slug) is None:
        return {"message": "Shop not found"}

    update_status(slug, status.status)

    return {"message": "Status updated"}


@app.post("/smes/{slug}/provenance")
def add_provenance(slug: str, provenance: Provenance):
    shop_data = get_shop(slug)

    if shop_data is None:
        return {"message": "Shop not found"}

    save_provenance(
        shop_data["id"],
        provenance.field_name,
        provenance.source_type,
        provenance.confidence,
        provenance.confirmed,
    )

    return {"message": "Provenance saved"}


@app.get("/smes/{slug}/provenance")
def get_shop_provenance(slug: str):
    shop_data = get_shop(slug)

    if shop_data is None:
        return {"message": "Shop not found"}

    data = get_provenance(shop_data["id"])

    return [dict(row) for row in data]


@app.post("/smes/{slug}/photos")
def add_photo(slug: str, photo: Photo):
    shop_data = get_shop(slug)

    if shop_data is None:
        return {"message": "Shop not found"}

    save_photo(
        shop_data["id"],
        photo.filename,
        photo.source,
    )

    return {"message": "Photo saved"}


@app.get("/smes/{slug}/photos")
def get_shop_photos(slug: str):
    shop_data = get_shop(slug)

    if shop_data is None:
        return {"message": "Shop not found"}

    photos = get_photos(shop_data["id"])

    return [dict(photo) for photo in photos]


@app.post("/smes/{slug}/consent")
def add_consent(slug: str, consent: Consent):
    shop_data = get_shop(slug)

    if shop_data is None:
        return {"message": "Shop not found"}

    save_consent(
        shop_data["id"],
        consent.consent_type,
        consent.approved_at,
        consent.payload_hash,
    )

    return {"message": "Consent saved"}


@app.get("/smes/{slug}/consent")
def get_shop_consent(slug: str):
    shop_data = get_shop(slug)

    if shop_data is None:
        return {"message": "Shop not found"}

    data = get_consent(shop_data["id"])

    return [dict(row) for row in data]


@app.post("/smes/{slug}/website-spec")
def add_website_spec(slug: str, spec: WebsiteSpec):
    shop_data = get_shop(slug)

    if shop_data is None:
        return {"message": "Shop not found"}

    save_website_spec(
        shop_data["id"],
        spec.version,
        spec.spec_data,
        spec.validation_score,
        spec.status,
    )

    return {"message": "WebsiteSpec saved"}


@app.get("/smes/{slug}/website-spec")
def get_shop_website_specs(slug: str):
    shop_data = get_shop(slug)

    if shop_data is None:
        return {"message": "Shop not found"}

    return get_website_specs(shop_data["id"])
