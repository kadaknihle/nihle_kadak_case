from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
SCREENSHOT_DIR = BASE_DIR / "reports" / "screenshots"
SCREENSHOT_DIR.mkdir(parents=True, exist_ok=True)

DEFAULT_TIMEOUT = 8

INSIDER_HOME_URL = "https://insiderone.com/"
INSIDER_QA_CAREERS_URL = "https://insiderone.com/careers/quality-assurance/"
EXPECTED_LOCATIONS = ["Istanbul, Turkiye", "Istanbul"]
EXPECTED_DEPARTMENTS = ["Quality Assurance", "QA"]

PETSTORE_BASE_URL = "https://petstore.swagger.io/v2"
