from urllib.parse import quote_plus

from locust import HttpUser, between, task


class N11SearchUser(HttpUser):
    host = "https://www.n11.com"
    wait_time = between(1, 2)

    # Using headers to simulate real user (still, n11.com returns 403 for automated requests, so this is just for the assignment)
    default_headers = {
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:148.0) Gecko/20100101 Firefox/148.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Sec-GPC": "1",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "Priority": "u=0, i",
        "Referer": "https://www.n11.com/"
    }

    def on_start(self) -> None: # Get homepage on start
        with self.client.get(
            "/", 
            name="homepage",
            headers=self.default_headers, 
            catch_response=True
        ) as response:
            if response.status_code != 200:
                response.failure(f"Unexpected status code: {response.status_code}")
            else:
                response.success()
                return

    def search(self, term: str, search_name: str) -> None:

        encoded_term = quote_plus(term) # URL-encode of search term
        print(encoded_term)

        with self.client.get(
            f"/arama?q={encoded_term}",
            name=search_name,
            headers=self.default_headers,
            catch_response=True,
        ) as response:
            if response.status_code != 200:
                response.failure(f"Unexpected status code: {response.status_code}")
            elif encoded_term not in response.url:
                response.failure(f"Not navigated to search page for search: {encoded_term}")
            else:
                response.success()
                return

    @task
    def search_category(self) -> None:
        term = "bilgisayar"
        self.search(term, search_name="search_category")

    @task
    def search_item(self) -> None:
        term = "Lenovo IdeaPad Slim 3 15IAN8"
        self.search(term, search_name="search_item")

    @task
    def search_non_existing(self) -> None:
        term = "lfkjh"
        self.search(term, search_name="search_non_existing")

    @task
    def search_invalid_input(self) -> None:
        term = "^+%&/()@é"
        self.search(term, search_name="search_invalid_input")

    @task
    def search_empty_input(self) -> None:
        term = " "
        self.search(term, search_name="search_empty_input")

    @task
    def search_long_input(self) -> None:
        term = "a" * 256
        self.search(term, search_name="search_long_input")

    @task
    def search_pages(self) -> None:
        for page in range(1, 3):
            with self.client.get(
                f"/arama?q=araba&pg={page}",
                name=f"search_category_page_{page}",
                headers=self.default_headers,
                catch_response=True,
            ) as response:
                if response.status_code != 200:
                    response.failure(f"Unexpected status code: {response.status_code} on page {page}")
                else:
                    response.success()