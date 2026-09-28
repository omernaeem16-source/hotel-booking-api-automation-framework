import requests


class APIClient:

    def __init__(self, base_url):
        # Initialize the API client with the base URL.
        self.base_url = base_url

    def get_booking(self, booking_id):
        # Retrieve a booking using its booking ID.
        url = self.base_url + "/booking/" + str(booking_id)
        response = requests.get(url)
        return response

    def create_booking(self, new_booking):
        # Create a new booking using the provided booking data.
        url = self.base_url + "/booking"
        response = requests.post(url, json=new_booking)
        return response

    def update_booking(self, booking_id, updated_booking, token):
        # Update an existing booking using an authentication token.
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Cookie": "token=" + token
        }

        url = self.base_url + "/booking/" + str(booking_id)
        response = requests.put(
            url,
            json=updated_booking,
            headers=headers
        )
        return response

    def get_token(self, username, password):
        # Authenticate the user and return the generated token.
        data = {
            "username": username,
            "password": password
        }

        url = self.base_url + "/auth"
        response = requests.post(url, json=data)

        data = response.json()
        actual_token = data["token"]

        return actual_token

    def delete_booking(self, booking_id, token):
        # Delete an existing booking using an authentication token.
        headers = {
            "Cookie": "token=" + token
        }

        url = self.base_url + "/booking/" + str(booking_id)
        response = requests.delete(url, headers=headers)

        return response

    def get_auth_response(self, username, password):
        # Send authentication credentials and return the complete response.
        data = {
            "username": username,
            "password": password
        }

        url = self.base_url + "/auth"
        response = requests.post(url, json=data)

        return response

    def update_booking_without_auth(self, booking_id, updated_booking):
        # Attempt to update a booking without authentication.
        url = self.base_url + "/booking/" + str(booking_id)
        response = requests.put(url, json=updated_booking)

        return response

    def delete_booking_without_auth(self, booking_id):
        # Attempt to delete a booking without authentication.
        url = self.base_url + "/booking/" + str(booking_id)
        response = requests.delete(url)

        return response