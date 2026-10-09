# 🚀 ANTIGRAVITY.md — Team Execution & Agent Playbook

> **TEMPORARY COLLABORATION FILE**  
> *Notice:* Delete this file after all team members have synced their code and the live hackathon prototype is operational.

---

## 🤖 Instructions for the Antigravity AI Agent

When your user opens this repository and introduces themselves (e.g., *"I am Abhishek"* or *"I am Gayatri"*):
1. **Find their assigned section below.**
2. **Strictly respect their file boundaries.** Do **NOT** modify files owned by another teammate without their permission.
3. **Follow the Shared Standards** to guarantee zero merge conflicts and seamless integration.

---

## 🌐 Shared Technical Standards (Mandatory for Everyone)

1. **Framework & Language**: Python 3.11+ / FastAPI / SQLite / Pydantic v2.
2. **Pydantic v2 Convention**: Always use `model.model_dump()` (do NOT use deprecated `.dict()`).
3. **Database Location**: SQLite database is located at `./data/khoj_doot.db`.
4. **Zero-Conflict Rule**: Only write code in your designated module directory. Do not rename shared contract functions.
5. **Git Protocol**: Always pull before pushing:
   ```bash
   git pull origin main
   ```

---

## 👥 Person-by-Person Execution Playbooks

---

### 1. 👑 Ankur — Tech Lead / System Architect
* **Owned Files & Folders**:
  - `app/harness/` (`workflow.py`, `graph.py`, `state.py`, `memory.py`, `nodes/`, `skills/`, `tools/`)
  - `app/schemas/` (`infobin.py`, `provenance.py`, `website_spec.py`)
  - Overall system contracts and pipeline integration
* **Immediate Tasks for Ankur's Agent**:
  1. **Implement Real LangGraph**: Replace the sequential procedural stub in `app/harness/graph.py` with a compiled `StateGraph` from the `langgraph` package.
  2. **Checkpointer & State**: Wire `MemorySaver` checkpointer to preserve state across Checkpoint 1 (Approval) and Checkpoint 2 (Preview/Edit).
  3. **Maintain Shared Contracts**: Ensure `execute_workflow(request_context)` in `app/harness/workflow.py` maintains its contract with Abhishek's FastAPI routes.

---

### 2. ⚡ Abhishek — Backend / FastAPI Engineer
* **Owned Files & Folders**:
  - `app/main.py`
  - `app/routes/` (`merchants.py`, `website.py`, `assets.py`, `auth.py`)
  - `app/config.py`
* **Immediate Tasks for Abhishek's Agent**:
  1. **Voice Note Ingestion Endpoint**: Add `POST /api/merchants/{slug}/voice` in `merchants.py` that receives `.wav`/`.ogg` audio files and calls `transcribe_audio()` in `app/ai/sarvam.py`.
  2. **API Error Handling & Middleware**: Ensure all endpoints return structured JSON with descriptive HTTP status codes and CORS headers.
  3. **Swagger UI Validation**: Open `http://localhost:8000/docs` and test all endpoints:
     - `/api/auth/send-otp` & `/api/auth/verify-otp`
     - `/api/merchants/{slug}/chat`
     - `/api/website/{slug}/edit` & `/api/website/{slug}/publish`

---

### 3. 💾 Shantanu — Database / Persistence Engineer
* **Owned Files & Folders**:
  - `app/db/` (`database.py`, `models.py`, `crud.py`)
* **Immediate Tasks for Shantanu's Agent**:
  1. **Schema Integrity**: Ensure the 6 tables (`shops`, `bins`, `photos`, `provenance`, `consent_records`, `website_specs`) initialize properly without locking SQLite.
  2. **CRUD Query Helpers**: Add any missing helper functions in `app/db/crud.py`:
     - Query merchant by phone or slug
     - Fetch full history of consent records for legal compliance
     - Fetch photo filenames with correct base paths
  3. **Performance**: Add indices on `shops(slug)` and `bins(shop_id, bin_type)` for sub-millisecond retrieval.

---

### 4. 🧠 Paksha — AI & Audio/Vision Engineer
* **Owned Files & Folders**:
  - `app/ai/` (`sarvam.py`, `gemini.py`)
  - `app/harness/skills/`
* **Immediate Tasks for Paksha's Agent**:
  1. **Real Gemini Extraction Prompt**: Replace hardcoded regex in `extract_infobin_from_text()` with live Gemini API structured JSON generation using Pydantic's `InfoBin` schema.
  2. **Multimodal Menu Vision**: In `extract_from_image()`, pass uploaded rate-card photos to Gemini Flash multimodal API to parse handwritten prices and dishes.
  3. **Sarvam Audio Pipeline**: Ensure `transcribe_audio()` handles regional Marathi (`mr-IN`) voice notes cleanly, with fallback to Hindi or English if needed.

---

### 5. 🎨 Gayatri — Frontend & Website Engine Engineer
* **Owned Files & Folders**:
  - `app/website/` (`generator.py`, `patcher.py`, `preview.py`, `components/`)
  - `app/templates/` (`upload.html`, `card.html`, `labs.html`)
* **Immediate Tasks for Gayatri's Agent**:
  1. **Polish UI Components**: Enhance CSS and layout in `app/website/components/` (`hero.py`, `products.py`, `location.py`, `contact.py`, `footer.py`) for maximum visual impact during demo.
  2. **Expand Conversational Patcher**: In `app/website/patcher.py`, add support for more edit commands (e.g. changing colors, updating prices, toggling sections on/off).
  3. **Frontend Wiring**: In `app/templates/upload.html`, wire the form submit button to trigger `/api/merchants/{slug}/chat` and display the generated preview cleanly.

---

### 6. 🧪 Sakshi — QA / Validation & Benchmark Engineer
* **Owned Files & Folders**:
  - `app/validation/` (`business.py`, `website.py`)
  - `data/shops.json`
  - `docs/` (`DEMO-CHECKLIST.md`, `FIELD-MAPPING.md`)
* **Immediate Tasks for Sakshi's Agent**:
  1. **Edge-Case Validation**: Expand `app/validation/business.py` to catch incomplete merchant records (missing phone numbers, zero items, invalid locations).
  2. **8-Point Scorecard Verification**: Ensure `validate_website_html()` accurately grades generated sites and produces clear failure reasons if any section is missing.
  3. **Demo Rehearsal**: Follow `docs/DEMO-CHECKLIST.md` step-by-step using data from `data/shops.json` to verify the live hackathon presentation flow.

---

## 🎯 Quick Command to Run the Prototype

```bash
uvicorn app.main:app --reload --port 8000
```
- **Interactive API Docs**: `http://localhost:8000/docs`
- **Merchant Onboarding**: `http://localhost:8000/upload`
- **Khoj Card**: `http://localhost:8000/merchant/sunita-tiffin-service/card`
- **Labs Telemetry**: `http://localhost:8000/labs`
- **Published Website**: `http://localhost:8000/merchant/sunita-tiffin-service`
