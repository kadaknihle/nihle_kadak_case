import pytest

from pages.careers_page import CareersPage
from pages.home_page import HomePage
from pages.lever_jobs_page import LeverJobsPage
from utils.settings import EXPECTED_DEPARTMENTS, EXPECTED_LOCATIONS


@pytest.mark.ui
def test_insider_qa_jobs_flow(driver):
    home_page = HomePage(driver)
    home_page.load()
    home_page.wait_until_ready()

    careers_page = CareersPage(driver)
    careers_page.load()
    careers_page.go_to_qa_jobs()

    jobs_page = LeverJobsPage(driver)
    jobs_page.load()
    assert EXPECTED_DEPARTMENTS[0].lower() in jobs_page.get_all_jobs_title()
    jobs_page.filter_jobs(EXPECTED_LOCATIONS[0])
    jobs = jobs_page.get_jobs()

    print(jobs)

    for job in jobs:
        assert any(dept.lower() in job.title.lower() for dept in EXPECTED_DEPARTMENTS), (
            f"Unexpected position title: {job.title.lower()}"
        )
        assert any(location.lower() in job.location.lower() for location in EXPECTED_LOCATIONS), (
            f"Unexpected location value: {job.location.lower()}"
        )

    jobs_page.open_first_job()
    jobs_page.click_apply_button()

    assert "/apply" in driver.current_url, "Expected application form URL to include '/apply'."
