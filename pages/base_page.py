from __future__ import annotations

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from utils.settings import DEFAULT_TIMEOUT, INSIDER_HOME_URL


class BasePage:
    def __init__(self, driver: WebDriver, timeout: int = DEFAULT_TIMEOUT) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self, url: str) -> None:
        self.driver.get(url)

    def wait_for_title_contains(self, value: str) -> None:
        self.wait.until(EC.title_contains(value))

    def wait_until_visible(self, locator: tuple[str, str]):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_until_clickable(self, locator: tuple[str, str]):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def wait_until_all_visible(self, locator: tuple[str, str]):
        return self.wait.until(EC.visibility_of_all_elements_located(locator))

    def wait_until_href_is_ready(self, locator):
        def _predicate(driver):
            element = driver.find_element(*locator)
            href = element.get_attribute("href")
            if href and href != f"{INSIDER_HOME_URL}careers/#":
                return element
            return False

        return self.wait.until(_predicate)

    def is_visible(self, locator: tuple[str, str], timeout: int = 5) -> bool:
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except Exception:
            return False

    def wait_until_present(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def scroll_to(self, locator):
        element = self.wait_until_present(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        return element

    def click(self, locator: tuple[str, str]) -> None:
        self.wait_until_clickable(locator).click()

    def type(self, locator: tuple[str, str], value: str, clear: bool = True) -> None:
        element = self.wait_until_visible(locator)
        if clear:
            element.clear()
        element.send_keys(value)

    def text_of(self, locator: tuple[str, str]) -> str:
        return self.wait_until_visible(locator).text

    def elements(self, locator: tuple[str, str]):
        return self.driver.find_elements(*locator)

    def current_url(self) -> str:
        return self.driver.current_url
