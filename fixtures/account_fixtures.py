from pytest import fixture

from data_transfer_object.account import UserProfile, City
from data_transfer_object.account import UserInfoTest
from endpoint_objects.account_endpoint import AccountEndpoint
from settings import ADMIN_LOGIN
from transfer_data.tables import KeyautoConnectDto


@fixture
def get_user_info_testing_dto(keyauto_connect: KeyautoConnectDto) -> UserInfoTest:
    """
     Формирование данных для получения информацуии о пользователе

     :return: Данные для запроса.
     """
    AccountEndpoint.user_info_testing()
    return_data = keyauto_connect.account_user_table.select_from_table_account_user_by_phone(
        phone=ADMIN_LOGIN
    )

    return UserInfoTest(
        id=return_data.id,
        eid=return_data.eid,
        phone=return_data.phone,
        name=return_data.name,
        birthday=return_data.birthday,
        email=return_data.email,
        city_eid=return_data.city_eid,
        date_joined=return_data.date_joined
    )


@fixture
def get_user_profile_dto(keyauto_connect: KeyautoConnectDto) -> UserProfile:
    """
    Формирование данных для получения информацуии о пользователе

    :return: Данные для запроса.
    """
    print()
    AccountEndpoint.user_profile()
    print()
    return_data = keyauto_connect.account_user_table.select_from_table_account_user_by_phone(
        phone=ADMIN_LOGIN
    )
    print()
    return UserProfile(
        user_id=return_data.id,
        phone=return_data.phone,
        name=return_data.name,
        birthday=return_data.birthday,
        email=return_data.email,
        city=return_data.city_id,
        consent=True,
        validated=True,
        send_service_push=True,
        deletion_date=return_data.deletion_date
    )
    print()

    # AccountEndpoint.city()
    # return_data = keyauto_connect.reference_city_table.select_from_table_reference_city_by_id(
        # city_id=return_data.id
    # )

    # return City(
        # city_id=return_data.id,
        # city_name=return_data.name
    # )


