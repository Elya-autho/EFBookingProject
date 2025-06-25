import allure
import pytest
import requests
from core.clients.api_client import APIClient


@allure.feature("Test created")
@allure.story("Test created booking")
def test_created_booking(api_client, booking_data):
    with allure.step("Отправка запроса на создание бронирования"):
        response = api_client.create_booking(booking_data)
    with allure.step("Проверка кода ответа"):
        assert response.status_code == 201, f"Ожидался код 201, получен {response.status_code}"
    with allure.step("Проверка структуры ответа"):
        response_data = response.json
        assert response_data["firstname"] == booking_data["firstname"], "Имя не совпадает"
        assert response_data["lastname"] == booking_data["lastname"], "Фамилия не совпадает"
        assert response_data["totalprice"] == booking_data["totalprice"], "Сумма не совпадает"
        assert response_data["depositpaid"] == booking_data["depositpaid"], "Статус депозита не совпадает"
    with allure.step("Проверка дат бронирования"):
        assert "bookingdates" in response_data, "Отсутствует блок bookingdates в ответе"
        assert response_data["bookingdates"]["checkin"] == booking_data["bookingdates"]["checkin"], \
            f"Дата заезда не совпадает. Ожидалось: {booking_data['bookingdates']['checkin']}, Получено: {response_data['bookingdates']['checkin']}"
        assert response_data["bookingdates"]["checkout"] == booking_data["bookingdates"]["checkout"], \
            f"Дата выезда не совпадает. Ожидалось: {booking_data['bookingdates']['checkout']}, Получено: {response_data['bookingdates']['checkout']}"

    with allure.step("Проверка additionalneeds"):
        assert "additionalneeds" in response_data, "Отсутствует поле additionalneeds в ответе"
        assert response_data["additionalneeds"] == booking_data["additionalneeds"], \
            f"Дополнительные пожелания не совпадают. Ожидалось: {booking_data['additionalneeds']}, Получено: {response_data['additionalneeds']}"
