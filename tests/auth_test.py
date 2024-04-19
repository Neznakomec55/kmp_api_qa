from datetime import timedelta

from endpoint_objects.auth_endpoint import AuthEndpoint
from settings import KMP_API_STAGE_AUTH
from transfer_data.tables import KeyautoConnectDto
from utils import get_current_datetime


class TestAuth:
    """
    Тесты для авторизации.
    """

    def test_send_sms(self, get_send_sms_dto, keyauto_connect: KeyautoConnectDto) -> None:
        """
        Тест отправки запроса на СМС.

        :param get_send_sms_dto: Данные для запроса отправки СМС.
        :return: None.
        """

        current_datetime = get_current_datetime()
        AuthEndpoint.send_sms(get_send_sms_dto)
        data = keyauto_connect.authorization_sms_code_table.select_from_table_authorization_sms_code_by_phone(
            phone=get_send_sms_dto.phone
        )[-1]
        assert current_datetime - data[1] < timedelta(seconds=30)

    def test_get_token(self, get_token_dto) -> None:
        """
         Тест на получение токена авторизации.

         :return: None.
         """
        AuthEndpoint.login(get_token_dto)

    def test_logout(self) -> None:
        """
        Выход из аккаунта.

        :return: None.
        """
        AuthEndpoint.logout(KMP_API_STAGE_AUTH)
