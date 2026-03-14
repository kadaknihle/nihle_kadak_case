from typing import Any

import requests

from utils.settings import PETSTORE_BASE_URL


class PetStoreClient:
    def __init__(self, base_url: str = PETSTORE_BASE_URL) -> None:
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({"Content-Type": "application/json"})

    def create_pet(self, payload: dict[str, Any]) -> requests.Response:
        return self.session.post(f"{self.base_url}/pet", json=payload)

    def get_pet(self, pet_id: int) -> requests.Response:
        return self.session.get(f"{self.base_url}/pet/{pet_id}")

    def update_pet(self, payload: dict[str, Any]) -> requests.Response:
        return self.session.put(f"{self.base_url}/pet", json=payload)

    def delete_pet(self, pet_id: int) -> requests.Response:
        return self.session.delete(f"{self.base_url}/pet/{pet_id}")
