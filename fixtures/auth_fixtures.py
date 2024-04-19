from pytest import fixture

from data_transfer_object.auth import SendSms
from data_transfer_object.auth import GetAuthToken
from endpoint_objects.auth_endpoint import AuthEndpoint
from settings import ADMIN_LOGIN
from transfer_data.tables import KeyautoConnectDto


@fixture
def get_send_sms_dto() -> SendSms:
    """
    Формирование объекта данных для запроса отправки СМС.

    :return: Данные для запроса.
    """

    return SendSms(
        phone=ADMIN_LOGIN
    )



@fixture
def get_token_dto(get_send_sms_dto, keyauto_connect: KeyautoConnectDto) -> GetAuthToken:
    """
    Сборка DTO для запроса получения токена авторизации.

    :return: DTO с данными для запроса токена.
    """
    AuthEndpoint.send_sms(get_send_sms_dto)
    data = keyauto_connect.authorization_sms_code_table.select_from_table_authorization_sms_code_by_phone(
        phone=get_send_sms_dto.phone
    )[-1]
    return GetAuthToken(
        phone=get_send_sms_dto.phone,
        code=data[6],
        consent=True
    )


@fixture
def get_authentication(get_token_dto) -> str:
    """
    Авторизация пользователя.

    :return: Токен авторизации.
    """
    return AuthEndpoint.login(get_token_dto)
