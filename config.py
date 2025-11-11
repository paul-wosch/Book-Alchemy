"""Provide global constants for the project."""
from pathlib import Path

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
