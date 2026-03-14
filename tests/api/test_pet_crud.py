import random

import pytest


@pytest.fixture
def pet_request() -> dict:
    pet_id = random.randint(1, 10)
    return {
        "id": pet_id,
        "category": {"id": 1, "name": "dogs"},
        "name": f"insider-qa-pet-{pet_id}",
        "photoUrls": ["https://example.com/pet.png"],
        "tags": [{"id": 1, "name": "insider"}],
        "status": "available",
    }


@pytest.mark.api
def test_pet_crud_happy_path(petstore_client, pet_request):

    create_response = petstore_client.create_pet(pet_request)
    assert create_response.status_code == 200

    get_response = petstore_client.get_pet(pet_request["id"])
    assert get_response.status_code == 200
    assert get_response.json()["name"] == pet_request["name"]

    updated_request = pet_request.copy()
    updated_request["status"] = "sold"
    update_response = petstore_client.update_pet(updated_request)
    assert update_response.status_code == 200
    assert update_response.json()["status"] == "sold"

    confirm_response = petstore_client.get_pet(pet_request["id"])
    assert confirm_response.status_code == 200
    confirm_body = confirm_response.json()
    assert confirm_body["name"] == updated_request["name"]
    assert confirm_body["status"] == "sold"

    delete_response = petstore_client.delete_pet(pet_request["id"])
    assert delete_response.status_code == 200

    get_deleted_response = petstore_client.get_pet(pet_request["id"])
    assert get_deleted_response.status_code == 404


@pytest.mark.api
def test_get_non_existing_pet_returns_not_found(petstore_client):
    response = petstore_client.get_pet(9999999999)
    assert response.status_code == 404


@pytest.mark.api
def test_get_pet_with_invalid_id_returns_bad_request(petstore_client):
    response = petstore_client.get_pet(-1)
    assert response.status_code == 404
