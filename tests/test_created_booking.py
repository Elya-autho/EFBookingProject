import allure
import pytest
import requests
from core.clients.api_client import APIClient


@allure.feature("Test created")
@allure.story("Test created booking")
def test_created_booking(api_client, booking_data):
    with allure.step("Отправка запроса на создание бронирования"):
        response = api_client.create_booking(booking_data)
