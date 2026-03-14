from dataclasses import dataclass
from typing import List

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from utils.settings import EXPECTED_DEPARTMENTS, EXPECTED_LOCATIONS


@dataclass(frozen=True)
class JobCard:
    title: str
    location: str


class LeverJobsPage(BasePage):
    LOCATION_FILTER_BUTTON = (
        By.XPATH,
        "//div[contains(@class,'filter-button') and normalize-space()='Location']",
    )
    LOCATION_OPTIONS = (By.CSS_SELECTOR, ".filter-popup li")
    JOB_CARDS = (By.CSS_SELECTOR, ".posting[data-qa-posting-id]")
    ALL_JOBS_TITLE = (By.CSS_SELECTOR, ".posting-category-title")
    APPLY_BUTTON = (By.CSS_SELECTOR, ".postings-btn")

    def load(self) -> None:
        self.wait_for_title_contains("Insider One")

    def filter_jobs(self, location: str) -> None:

        old_first_card = self.wait_until_all_visible(self.JOB_CARDS)[0]

        self.wait_until_clickable(self.LOCATION_FILTER_BUTTON).click()

        locationOptions = self.driver.find_elements(*self.LOCATION_OPTIONS)

        for locationOption in locationOptions:
            if locationOption.text.strip() == location.strip():
                print(f"Selecting location filter: {locationOption.text}")
                self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", locationOption)
                self.wait_until_clickable(locationOption).click()
                break

        self.wait.until(EC.staleness_of(old_first_card))

    def get_all_jobs_title(self) -> str:
        return self.wait_until_visible(self.ALL_JOBS_TITLE).text.lower()

    def get_jobs(self) -> List[JobCard]:
        cards = []
        for card in self.wait_until_all_visible(self.JOB_CARDS):
            title = card.find_element(By.CSS_SELECTOR, "[data-qa='posting-name']").text
            location = card.find_element(By.CSS_SELECTOR, ".sort-by-location").text
            cards.append(JobCard(title=title, location=location))
        return cards

    def open_first_job(self) -> None:
        first_job_link = self.wait_until_clickable((By.CSS_SELECTOR, "[data-qa='btn-apply']"))
        first_job_link.click()

    def click_apply_button(self) -> None:
        self.wait_until_clickable(self.APPLY_BUTTON).click()