# KhojDoot (खोजदूत)

> **Regional-Language No-Code Website Creation Platform**  
> *Problem Statement:* PS-29  
> *Target:* Hackathon MVP

---

## 1. Project Overview

KhojDoot enables non-technical small and medium business owners to describe their business and website requirements in their regional language (text, voice note, or rate-card photos). KhojDoot interprets the requirement, builds a structured presentation model, synthesizes a responsive website via a component-based coding engine, enforces deterministic quality validation, and publishes both a **human-facing website** and **machine-readable agentic-web assets**.

---

## 2. Repository File Structure

```text
khojdoot/
│
├── app/
│   ├── main.py
│   │
│   ├── routes/
│   │   ├── merchants.py
│   │   ├── website.py
│   │   └── assets.py
│   │
│   ├── harness/
│   │   ├── workflow.py
│   │   ├── graph.py
│   │   ├── state.py
│   │   ├── memory.py
│   │   │
│   │   ├── nodes/
│   │   │   ├── requirement_understanding.py
│   │   │   ├── information_extraction.py
│   │   │   ├── infobin_validation.py
│   │   │   ├── approval.py
│   │   │   ├── spec_generation.py
│   │   │   ├── website_generation.py
│   │   │   └── website_validation.py
│   │   │
│   │   ├── skills/
│   │   │   ├── requirement_understanding/
│   │   │   │   └── SKILL.md
│   │   │   ├── information_extraction/
│   │   │   │   └── SKILL.md
│   │   │   ├── website_generation/
│   │   │   │   └── SKILL.md
│   │   │   └── validation/
│   │   │       └── SKILL.md
│   │   │
│   │   └── tools/
│   │       ├── merchant.py
│   │       ├── infobin.py
│   │       ├── website.py
│   │       └── publishing.py
│   │
│   ├── ai/
│   │   ├── sarvam.py
│   │   └── gemini.py
│   │
│   ├── schemas/
│   │   ├── infobin.py
│   │   ├── provenance.py
│   │   └── website_spec.py
│   │
│   ├── validation/
│   │   ├── business.py
│   │   └── website.py
│   │
│   ├── website/
│   │   ├── generator.py
│   │   ├── coding_model.py
│   │   ├── patcher.py
│   │   ├── preview.py
│   │   └── components/
│   │       ├── hero.py
│   │       ├── products.py
│   │       ├── location.py
│   │       ├── contact.py
│   │       └── footer.py
│   │
│   ├── publishing/
│   │   ├── merchant_site.py
│   │   ├── agentfacts.py
│   │   ├── agent_card.py
│   │   ├── business_json.py
│   │   ├── jsonld.py
│   │   ├── llms.py
│   │   ├── sitemap.py
│   │   └── robots.py
│   │
│   ├── db/
│   │   ├── database.py
│   │   ├── models.py
│   │   └── crud.py
│   │
│   └── config.py
│
├── tests/
│   ├── test_infobin.py
│   ├── test_harness.py
│   ├── test_website.py
│   └── test_publishing.py
│
├── data/
│   └── .gitkeep
│
├── generated/
│   └── .gitkeep
│
├── .env
├── .env.example
├── .gitignore
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md
```

---

## 3. Team Member Tasks & File Ownership

All team members must write and maintain code strictly within their designated modules to avoid merge conflicts:

| Team Member | Role | Assigned Files & Directories | Core Responsibilities |
|---|---|---|---|
| **Ankur** | **Tech Lead & System Architect** | `app/harness/`, `app/schemas/`, `app/website/coding_model.py`, overall wiring | Core LangGraph orchestration, contracts, end-to-end integration |
| **Abhishek** | **Backend & FastAPI Engineer** | `app/main.py`, `app/routes/` (`merchants.py`, `website.py`, `assets.py`), `Dockerfile` | API routing, request validation, middleware, server deployment |
| **Shantanu** | **Database & Persistence** | `app/db/` (`database.py`, `models.py`, `crud.py`) | SQLite 6-table schema, records, query optimization |
| **Paksha** | **AI & Design Technical Support** | `app/ai/` (`sarvam.py`, `gemini.py`), skills | Speech-to-Text, entity extraction, prompt engineering |
| **Gayatri** | **Frontend & Website Engine** | `app/website/` (`generator.py`, `patcher.py`, `preview.py`, `components/`) | UI components, live preview, conversational editing loop |
| **Sakshi** | **QA & Validation Support** | `app/validation/`, `tests/` | Pydantic rules, 8-point website validation suite, test cases |

---

## 4. Quick Start

### 1. Install Dependencies
```bash
python -m venv venv
# On Windows:
.\venv\Scripts\activate
# On Linux/macOS:
source venv/bin/activate

pip install -r requirements.txt
```

### 2. Environment Variables
Copy `.env.example` to `.env` and fill in API keys:
```bash
cp .env.example .env
```

### 3. Run Development Server
```bash
uvicorn app.main:app --reload --port 8000
```
- Interactive Docs: http://localhost:8000/docs
- Health Check: http://localhost:8000/health
- Sample Merchant Site: http://localhost:8000/merchant/sunita-tiffin-service

### 4. Run Test Suite
```bash
pytest
```
