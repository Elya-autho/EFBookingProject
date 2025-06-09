import allure
import pytest
import requests
from core.clients.api_client import APIClient
from pydantic import ValidationError
from core.models.booking import BookingResponce


@allure.feature("Test created")
@allure.story("Test created booking")
def test_created_booking(api_client, booking_dates):
    booking_data = {
            "firstname": "Jim",
            "lastname": "Brown",
            "totalprice": 111,
            "depositpaid": True,
            "bookingdates": booking_dates,
            "additionalneeds": "Breakfast"
        }
    response = api_client.create_booking(booking_data)
    try:
        BookingResponce(**response)
    except ValidationError as e:
        raise ValidationError(f"Responce validation failed {e}")

    assert response['booking']["firstname"] == booking_data["firstname"], "Имя не совпадает"
    assert response['booking']["lastname"] == booking_data["lastname"], "Фамилия не совпадает"
    assert response['booking']["totalprice"] == booking_data["totalprice"], "Сумма не совпадает"
    assert response['booking']["depositpaid"] == booking_data["depositpaid"], "Статус депозита не совпадает"
    assert response['booking']["bookingdates"]["checkin"] == booking_data["bookingdates"]["checkin"]
    assert response['booking']["bookingdates"]["checkout"] == booking_data["bookingdates"]["checkout"]
    assert response['booking']["additionalneeds"] == booking_data["additionalneeds"]
    assert response['booking']["firstname"] != ""
    assert response['booking']["lastname"] != ""
    assert response['booking']["firstname"] != "!.?"
    assert response['booking']["lastname"] != "!.?"
    assert response['booking']["totalprice"] >= 0
    assert response['booking']["depositpaid"] != str
    assert response['booking']["bookingdates"]["checkin"] != ""
    assert response['booking']["bookingdates"]["checkout"] != ""




