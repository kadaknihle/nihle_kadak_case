from datetime import datetime
from pathlib import Path

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from api.pet_client import PetStoreClient
from utils.settings import SCREENSHOT_DIR


def pytest_addoption(parser: pytest.Parser) -> None:
    parser.addoption("--browser", action="store", default="chrome", choices=["chrome", "firefox"])

@pytest.fixture(scope="session")
def browser_name(request: pytest.FixtureRequest) -> str:
    return request.config.getoption("--browser")

@pytest.fixture
def driver(request: pytest.FixtureRequest, browser_name: str):
    if browser_name == "firefox":
        options = FirefoxOptions()
        web_driver = webdriver.Firefox(options=options)
    else:
        options = ChromeOptions()
        web_driver = webdriver.Chrome(options=options)

    web_driver.maximize_window()
    web_driver.implicitly_wait(0)
    request.node.driver = web_driver
    yield web_driver
    web_driver.quit()


@pytest.fixture(scope="session")
def petstore_client() -> PetStoreClient:
    return PetStoreClient()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item: pytest.Item, call: pytest.CallInfo):
    outcome = yield
    report = outcome.get_result()

    if report.passed:
        return

    web_driver = getattr(item, "driver", None)
    if web_driver is None:
        return

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    screenshot_path = Path(SCREENSHOT_DIR) / f"{item.name}_{timestamp}.png"
    web_driver.save_screenshot(screenshot_path)
    report.sections.append(("screenshot", f"Saved screenshot to: {screenshot_path}"))