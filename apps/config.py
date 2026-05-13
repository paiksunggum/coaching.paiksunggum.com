import os
from pathlib import Path

from dotenv import find_dotenv, load_dotenv

_backend_root = Path(__file__).resolve().parent.parent
load_dotenv(_backend_root / ".env")
load_dotenv(find_dotenv(usecwd=True), override=False)

database_url: str | None = (os.getenv("DATABASE_URL") or "").strip() or None
