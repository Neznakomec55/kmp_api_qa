from json import loads
from typing import Dict, Optional, Union
# from unittest import result
from requests import get

# from data_transfer_object.account import UserInfoTest
from endpoint_objects.base_endpoint_object import BaseEndpointObject
from settings import KMP_API_STAGE_AUTH, PROFILE_URL
from settings import USER_INFO_TESTING_URL


class AccountEndpoint(BaseEndpointObject):
    """
    Реализация запросов к группе Account.
    """

    # @classmethod
    # def get_notification_summary(cls) -> None:
    # """
    # Отправка запроса для чего ???

    #: return: None.
    # """
    # TODO переделать
    # with step(f'Отправка запроса методом GET'):
    # response = get(
    # url=NOTIFICATION_SUMMARY_URL,
    # auth=KMP_API_STAGE_AUTH
    # )
    # cls.base_response_check(response)

    @classmethod
    def user_profile(cls) -> Dict[str, Optional[Union[str, int, bool]]]:
        """
        Получение данных о профиле пользователя.

        :return: Данные о пользователе:
        {
            "name": str,
            "birthday": str,
            "email": str,
            "city": {
                 "id": int,
                 "name": str
            },
            "consent": bool,
            "validated": bool,
            "deletion_date": str
        }
        """
        print()
        data = get(url=PROFILE_URL, auth=KMP_API_STAGE_AUTH)
        print()
        cls.base_response_check(data)
        data = loads(data.text)
        print()
        # cls._check_profile_data(data)
        # return data

    @classmethod
    def _check_profile_data(cls, data: Dict[str, Optional[Union[str, int, bool]]], response_data=None) -> None:
        """
        Проверка Полученных данных.

        :param data: Данные:
        {
            "name": str,
            "birthday": str,
            "email": str,
            "city": {
                 "id": int,
                 "name": str
            },
            "consent": bool,
            "validated": bool,
            "deletion_date": str
        }
        :return: None.
        """
        # TODO описать проверку
        # проверка успешности запроса
        # assert isinstance(result.get('status_code'), str)
        assert response_data('status_code')
        # проверка валидности профиля
        if id:
            is_valid_id = data.get('id') and isinstance(data.get('id'), str)
            assert response_data.get('id')

    @classmethod
    def user_info_testing(cls) -> Dict[str, Optional[Union[str, int, bool]]]:
        """
        Получение данных о профиле пользователя.

        :param: DTO для запроса данных о пользователе.
        :return: Данные о пользователе:
        {
            "id": int,
            "eid": str,
            "phone": str,
            "name": str,
            "birthday": str
            "email": str,
            "city_eid": str,
            "date_joined": str
        }
        """
        # print()
        response = get(url=USER_INFO_TESTING_URL, auth=KMP_API_STAGE_AUTH)
        # print()
        cls.base_response_check(response)
        data = loads(response.text)
        cls._check_profile_data(data)
        return data
