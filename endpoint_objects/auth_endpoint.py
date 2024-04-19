from dataclasses import asdict
from json import loads
from time import sleep
from typing import Dict
from typing import Union

from requests import post
from requests import delete
from requests.auth import HTTPBasicAuth

from data_transfer_object.auth import GetAuthToken
from data_transfer_object.auth import SendSms
from endpoint_objects.base_endpoint_object import BaseEndpointObject
from settings import BETWEEN_SMS_CODE_REQUEST_TIMEOUT
from settings import CREATED
from settings import GET_TOKEN_URL
from settings import LOGOUT_URL
from settings import SEND_SMS_URL


class AuthEndpoint(BaseEndpointObject):
    """
    Реализация запросов к группе Auth.
    """

    has_requested_sms = False

    @classmethod
    def login(cls, data: GetAuthToken) -> str:
        """
        Получение токена

        :param data: Данные для авторизации.
        :return: Токен.
        """
        response = post(url=GET_TOKEN_URL, json=asdict(data))
        cls.base_response_check(response, status_code=201)
        response_data = loads(response.content)
        cls._check_token_response(response_data)
        return response_data.get('token')

    @classmethod
    def _check_token_response(cls, response_data: Dict[str, Union[str, bool]]) -> None:
        """
        Проверка ответа на запрос токена.

        :param response_data: Данные ответа
        {
            "token": "123456asdf"
        }
        :return: None.
        """
        # response_data.get('token')
        assert isinstance(response_data.get('token'), str) and response_data.get('token'), \
            f'Поле "token" не заполнено или не является строкой: {response_data}'

    @classmethod
    def send_sms(cls, data: SendSms) -> None:
        """
        Отправка запроса на СМС.

        :param data: Данные с номером телефона для получения СМС.
        :return: None.
        """
        if cls.has_requested_sms:
            sleep(BETWEEN_SMS_CODE_REQUEST_TIMEOUT)  # сон после запроса на отправку СМС
            cls.has_requested_sms = False
        response = post(url=SEND_SMS_URL, json=asdict(data))
        cls.base_response_check(response, status_code=CREATED)
        cls.has_requested_sms = True
        sleep(BETWEEN_SMS_CODE_REQUEST_TIMEOUT)  # сон после запроса на отправку СМС
        cls.has_requested_sms = False

    @classmethod
    def logout(cls, auth: HTTPBasicAuth) -> None:
        """
        Выход из системы

        :param auth: Токен авторизации.
        :return: None.
        """
        response = delete(url=LOGOUT_URL, auth=auth)
        cls.base_response_check(response, 204)
