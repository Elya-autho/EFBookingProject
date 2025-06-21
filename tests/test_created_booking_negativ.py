import allure
import pytest
import requests
from requests.exceptions import HTTPError
from core.clients.api_client import APIClient
from pydantic import ValidationError
from core.models.booking import BookingResponce


@allure.feature("Test created")
@allure.story("Test created booking negativ")
def test_created_booking_negativ(api_client, booking_dates):
    booking_data_negative_price = {
        }

    response = api_client.create_booking_negativ(booking_data_negative_price)
    try:
        BookingResponce(**response)
    except ValidationError as e:
        raise ValidationError(f"Responce validation failed {e}")
    with pytest.raises(HTTPError):
         api_client.create_booking_negativ(booking_data_negative_price)






