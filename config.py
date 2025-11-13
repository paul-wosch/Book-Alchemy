"""Provide global constants for the project."""
from dotenv import dotenv_values
from pathlib import Path
import secrets

PROJECT_ROOT = Path(__file__).resolve().parent

DATA_DIR = Path("data")
DATA_PATH = (PROJECT_ROOT / DATA_DIR).resolve()
# Ensure data folder is created if not existing
DATA_PATH.mkdir(exist_ok=True)

DB_FILE = Path("library.sqlite")
DB_FILE_PATH = (DATA_PATH / DB_FILE).resolve()

STATIC_DIR = Path("static")
STATIC_PATH = (PROJECT_ROOT / STATIC_DIR).resolve()
TEMPLATES_DIR = Path("templates")
TEMPLATES_PATH = (PROJECT_ROOT / TEMPLATES_DIR).resolve()

DOTENV_FILE = Path(".env")
DOTENV_FILE_PATH = (PROJECT_ROOT / DOTENV_FILE).resolve()
# if .env or key in .env does not exist create one using `secrets.token_hex(16)`
FLASK_SECRET_KEY = dotenv_values(DOTENV_FILE_PATH).get("FLASK_SECRET_KEY", None)

# Ensure .env exists and contains a secret key
if not FLASK_SECRET_KEY:  # covers None and ""
    FLASK_SECRET_KEY = secrets.token_hex(16)
    # Ensure file exists
    if not DOTENV_FILE_PATH.exists():
        DOTENV_FILE_PATH.touch()
    # Update or append the key line
    lines = []
    if DOTENV_FILE_PATH.read_text(encoding="utf-8").strip():
        # Replace existing empty line if present
        for line in DOTENV_FILE_PATH.read_text(encoding="utf-8").splitlines():
            if line.startswith("FLASK_SECRET_KEY="):
                lines.append(f"FLASK_SECRET_KEY={FLASK_SECRET_KEY}")
            else:
                lines.append(line)
    else:
        lines.append(f"FLASK_SECRET_KEY={FLASK_SECRET_KEY}")
    DOTENV_FILE_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    """Print global constants."""
    files_and_paths = {"PROJECT_ROOT": PROJECT_ROOT,
                       "DATA_DIR": DATA_DIR,
                       "DATA_PATH": DATA_PATH,
                       "DB_FILE": DB_FILE,
                       "DB_FILE_PATH": DB_FILE_PATH,
                       "STATIC_DIR": STATIC_DIR,
                       "STATIC_PATH": STATIC_PATH,
                       "TEMPLATES_DIR": TEMPLATES_DIR,
                       "TEMPLATES_PATH": TEMPLATES_PATH
                       }

    print("Current file and path resolutions:\n")
    for label, file_path in files_and_paths.items():
        print(f"{label}: {file_path}")


if __name__ == "__main__":
    main()
