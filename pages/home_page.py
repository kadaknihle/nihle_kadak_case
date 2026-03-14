from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from utils.settings import INSIDER_HOME_URL


class HomePage(BasePage):
    HERO_SECTION = (By.CSS_SELECTOR, 'section[class*="homepage-hero"]')
    SOCIAL_PROOF_SECTION = (By.CSS_SELECTOR, 'section[class*="homepage-social-proof"]')
    CORE_DIFFERENTIATORS_SECTION = (By.CSS_SELECTOR, 'section[class*="homepage-core-differentiators"]')
    CAPABILITIES_SECTION = (By.CSS_SELECTOR, 'section[class*="homepage-capabilities"]')
    INSIDER_ONE_AI_SECTION = (By.CSS_SELECTOR, 'section[class*="homepage-insider-one-ai"]')
    CHANNELS_SECTION = (By.CSS_SELECTOR, 'section[class*="homepage-channels"]')
    CASE_STUDY_SECTION = (By.CSS_SELECTOR, 'section[class*="homepage-case-study"]')
    ANALYST_SECTION = (By.CSS_SELECTOR, 'section[class*="homepage-analyst"]')
    INTEGRATIONS_SECTION = (By.CSS_SELECTOR, 'section[class*="homepage-integrations"]')
    RESOURCES_SECTION = (By.CSS_SELECTOR, 'section[class*="homepage-resources"]')
    CALL_TO_ACTION_SECTION = (By.CSS_SELECTOR, 'section[class*="homepage-call-to-action"]')
    FOOTER = (By.ID, "footer")
    NAVIGATION = (By.ID, "navigation")

    def load(self) -> None:
        self.open(INSIDER_HOME_URL)

    def wait_until_ready(self) -> None:
        self.wait_for_title_contains("Insider One")

        mainBlocks = [
            self.HERO_SECTION,
            self.SOCIAL_PROOF_SECTION,
            self.CORE_DIFFERENTIATORS_SECTION,
            self.CAPABILITIES_SECTION,
            self.INSIDER_ONE_AI_SECTION,
            self.CHANNELS_SECTION,
            self.CASE_STUDY_SECTION,
            self.ANALYST_SECTION,
            self.INTEGRATIONS_SECTION,
            self.RESOURCES_SECTION,
            self.CALL_TO_ACTION_SECTION,
            self.FOOTER,
            self.NAVIGATION,
        ]

        for locator in mainBlocks:
            self.scroll_to(locator)
            self.wait_until_visible(locator)
