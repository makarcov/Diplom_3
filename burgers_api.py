import allure
import requests

from data import Url
from data import Endpoint
from helpers import Helpers


class BurgersApi:

    @staticmethod
    @allure.step('Создаем нового пользователя')
    def create_user():
        create_user_body = Helpers.mod_create_user_body()
        response = requests.post(Url.BASE_URL + Endpoint.CREATE_USER_ENDPOINT, json=create_user_body)
        token = response.json().get("accessToken")

        return create_user_body, token

    @staticmethod
    @allure.step('Удаляем пользователя')
    def delete_user(token):
        requests.delete(Url.BASE_URL + Endpoint.DELETE_USER_ENDPOINT, headers={
            'Authorization': token
        })

    @staticmethod
    @allure.step('Создаем новый заказ')
    def create_order(token):
        body = Helpers.mod_create_order_body()
        create_order_response = requests.post(Url.BASE_URL + Endpoint.CREATE_ORDER_ENDPOINT, json=body, headers={
            'Authorization': token
        })
        number = create_order_response.json()["order"]["number"]
        return number
