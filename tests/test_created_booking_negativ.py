import allure
import pytest
import requests
from requests.exceptions import HTTPError
from core.clients.api_client import APIClient
from pydantic import ValidationError
from core.models.booking import BookingResponce


@allure.feature("Test created")
@allure.story("Test created booking negativ")
def test_created_booking_negativ(api_client):
    booking_data_negative_price = {
        }

    with pytest.raises(HTTPError) as error:
        api_client.create_booking_negative(booking_data_negative_price)
    assert error.value.response.status_code == 500, (
        f"Expected status code 500, but got {error.value.response.status_code}\n"
        f"Response content: {error.value.response.text}")









