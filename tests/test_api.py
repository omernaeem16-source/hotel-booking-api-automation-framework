import pytest

from api.api_client import APIClient
from config import base_url, USERNAME, PASSWORD


client = APIClient(base_url)


# Fixture that creates a booking and returns its dynamically generated ID.
@pytest.fixture
def booking_id():

    booking = {
        "firstname": "Omer",
        "lastname": "Naeem",
        "totalprice": 500,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2026-10-01",
            "checkout": "2026-10-05"
        },
        "additionalneeds": "Breakfast"
    }

    response = client.create_booking(booking)

    assert response.status_code == 200

    data = response.json()

    return data["bookingid"]


# Verify that valid credentials generate an authentication token.
def test_authentication():

    token = client.get_token(USERNAME, PASSWORD)

    assert token != ""
    assert isinstance(token, str)


# Verify that a new booking can be created successfully.
def test_create_booking():

    booking = {
        "firstname": "Omer",
        "lastname": "Naeem",
        "totalprice": 500,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2026-10-01",
            "checkout": "2026-10-05"
        },
        "additionalneeds": "Breakfast"
    }

    response = client.create_booking(booking)
    booking_response = response.json()

    assert response.status_code == 200
    assert "bookingid" in booking_response
    assert booking_response["booking"]["firstname"] == booking["firstname"]
    assert booking_response["booking"]["lastname"] == booking["lastname"]


# Verify that an existing booking can be retrieved using its ID.
def test_get_booking(booking_id):

    response = client.get_booking(booking_id)
    get_response = response.json()

    assert response.status_code == 200
    assert get_response["firstname"] == "Omer"
    assert get_response["lastname"] == "Naeem"


# Verify that an existing booking can be updated successfully.
def test_update_booking(booking_id):

    updated_booking = {
        "firstname": "Omer Updated",
        "lastname": "Naeem",
        "totalprice": 750,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2026-10-02",
            "checkout": "2026-10-06"
        },
        "additionalneeds": "Breakfast and Dinner"
    }

    token = client.get_token(USERNAME, PASSWORD)

    response = client.update_booking(
        booking_id,
        updated_booking,
        token
    )

    update_response = response.json()

    assert response.status_code == 200
    assert update_response["firstname"] == "Omer Updated"
    assert update_response["lastname"] == "Naeem"
    assert update_response["totalprice"] == 750
    assert update_response["additionalneeds"] == "Breakfast and Dinner"


# Verify that an existing booking can be deleted successfully.
def test_delete_booking(booking_id):

    token = client.get_token(USERNAME, PASSWORD)

    response = client.delete_booking(booking_id, token)

    assert response.status_code == 201
    assert client.get_booking(booking_id).status_code == 404


# Verify that invalid booking IDs return a 404 response.
@pytest.mark.parametrize("invalid_id", [9999, 8888, 7777])
def test_invalid_booking_id(invalid_id):

    response = client.get_booking(invalid_id)

    assert response.status_code == 404


# Verify that invalid credential combinations are rejected.
@pytest.mark.parametrize(
    "username,password",
    [
        ("admin", "password12"),
        ("admin", "wrong123"),
        ("wrong_user", "password123")
    ]
)
def test_invalid_credentials(username, password):

    response = client.get_auth_response(username, password)

    assert response.status_code == 200
    assert response.json()["reason"] == "Bad credentials"


# Verify that updating a booking without authentication is rejected.
def test_update_without_authentication(booking_id):

    updated_booking = {
        "firstname": "Omer Updated",
        "lastname": "Naeem",
        "totalprice": 750,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2026-10-02",
            "checkout": "2026-10-06"
        },
        "additionalneeds": "Breakfast and Dinner"
    }

    response = client.update_booking_without_auth(
        booking_id,
        updated_booking
    )

    assert response.status_code == 403


# Verify that deleting a booking without authentication is rejected.
def test_delete_without_authentication(booking_id):

    response = client.delete_booking_without_auth(booking_id)

    assert response.status_code == 403


# Verify that invalid booking data is rejected by the API.
def test_invalid_booking_data():

    invalid_booking = {
        "firstname": "",
        "lastname": "",
        "totalprice": "wrong",
        "depositpaid": "yes"
    }

    response = client.create_booking(invalid_booking)

    assert response.status_code == 500