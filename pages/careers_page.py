from selenium.webdriver.common.by import By
import time
from pages.base_page import BasePage
from utils.settings import INSIDER_QA_CAREERS_URL


class CareersPage(BasePage):
    QA_TEAM_BUTTON = (
        By.CSS_SELECTOR,
        '#open-roles [data-department="Quality Assurance"] a',
    )

    SEE_ALL_TEAMS_BUTTON = (By.CSS_SELECTOR, "#open-roles a.see-more")

    def load(self) -> None:
        self.open(INSIDER_QA_CAREERS_URL)

    def go_to_qa_jobs(self) -> None:

        self.scroll_to(self.SEE_ALL_TEAMS_BUTTON)
        button = self.wait_until_clickable(self.SEE_ALL_TEAMS_BUTTON)
        self.driver.execute_script("arguments[0].click();", button) # Cookies popup blocks the click so we execute script

        self.scroll_to(self.QA_TEAM_BUTTON)
        self.wait_until_href_is_ready(self.QA_TEAM_BUTTON)
        self.click(self.QA_TEAM_BUTTON)
