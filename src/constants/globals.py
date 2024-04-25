from pathlib import Path

SEARCH_URL = "https://jsearch.p.rapidapi.com/search"
PROJECT_DIR = Path(*Path(__file__).parts[:-3]).__str__()
DATA_DIR = Path(PROJECT_DIR, "data", "raw")
PROCESSED_DIR = Path(PROJECT_DIR, "data", "processed")

# KEYWORDS = []

with open(Path(PROJECT_DIR, "src", "constants", "keywords.txt"), "r") as f:
    KEYWORDS = f.readlines()
    KEYWORDS = [keyword.strip("\n") for keyword in KEYWORDS]
