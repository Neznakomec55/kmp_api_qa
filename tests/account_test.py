from endpoint_objects import AccountEndpoint
# from sql_queries.keyauto import AccountUserTableQueries
from settings import ADMIN_LOGIN
from transfer_data.tables import KeyautoConnectDto


class TestAccount:
    """
    Тесты для авторизации.
    """

    # def test_user_info(self, get_user_info_testing_dto, keyauto_connect: KeyautoConnectDto) -> None:
        # """
        # Тест получения данных о пользователе.
        # :return: UserInfoTesting.
        # """
        # AccountEndpoint.user_info_testing()
        # keyauto_connect.account_user_table.select_from_table_account_user_by_phone(
            # phone=ADMIN_LOGIN
        # )

    def test_account_profile(self, get_user_profile_dto, keyauto_connect: KeyautoConnectDto, return_data=None) -> None:
        """
        Формирование данных для получения информацуии о пользователе

        :return: Данные для запроса.
        """
        print()
        AccountEndpoint.user_profile()
        print()
        keyauto_connect.account_user_table.select_from_table_account_user_by_phone(
            phone=ADMIN_LOGIN
        )
        print()
        # AccountEndpoint.city()
        # keyauto_connect.reference_city_table.select_from_table_reference_city_by_id(
            # city_id=return_data.id
        # )
