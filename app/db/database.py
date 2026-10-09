"""
Database Connection & Initialization.
Owner: Shantanu (Database / Persistence)
"""
import sqlite3
import os
from app.config import settings


def get_db_path() -> str:
    path = settings.DATABASE_PATH
    os.makedirs(os.path.dirname(path), exist_ok=True)
    return path


def get_connection():
    conn = sqlite3.connect(get_db_path())
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    """Initializes the 6 relational tables defined in TRD v2.0."""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.executescript("""
    CREATE TABLE IF NOT EXISTS shops (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        sme_id TEXT,
        slug TEXT UNIQUE NOT NULL,
        name TEXT NOT NULL,
        phone TEXT,
        city TEXT,
        status TEXT DEFAULT 'draft',
        created_at TEXT,
        updated_at TEXT
    );

    CREATE TABLE IF NOT EXISTS bins (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        shop_id INTEGER NOT NULL,
        bin_type TEXT NOT NULL,
        data TEXT NOT NULL,
        FOREIGN KEY (shop_id) REFERENCES shops(id)
    );

    CREATE TABLE IF NOT EXISTS photos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        shop_id INTEGER NOT NULL,
        filename TEXT NOT NULL,
        source TEXT,
        FOREIGN KEY (shop_id) REFERENCES shops(id)
    );

    CREATE TABLE IF NOT EXISTS provenance (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        shop_id INTEGER NOT NULL,
        field_name TEXT NOT NULL,
        source_type TEXT NOT NULL,
        confidence REAL,
        confirmed INTEGER DEFAULT 0,
        FOREIGN KEY (shop_id) REFERENCES shops(id)
    );

    CREATE TABLE IF NOT EXISTS consent_records (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        shop_id INTEGER NOT NULL,
        consent_type TEXT NOT NULL,
        approved_at TEXT NOT NULL,
        payload_hash TEXT,
        FOREIGN KEY (shop_id) REFERENCES shops(id)
    );

    CREATE TABLE IF NOT EXISTS website_specs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        shop_id INTEGER NOT NULL,
        version INTEGER DEFAULT 1,
        spec_data TEXT NOT NULL,
        validation_score REAL DEFAULT 0.0,
        status TEXT DEFAULT 'generated',
        FOREIGN KEY (shop_id) REFERENCES shops(id)
    );
    """)

    conn.commit()
    conn.close()
