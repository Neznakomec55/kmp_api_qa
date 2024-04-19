from pytest import fixture

from builtin_types import SqlConnect
from transfer_data.tables import KeyautoConnectDto

from settings import KMP_DB_TWO_URL


@fixture(scope='session')
def keyauto_connect() -> KeyautoConnectDto:
    """
    Возвращает объект DTO с наборами методов для взаимодействия через SQL-Alchemy с таблицами ka_integration_dms

    :return: Объект DTO с наборами методов для взаимодействия через SQL-Alchemy с таблицами ka_integration_dms
    """
    db_connect = SqlConnect(KMP_DB_TWO_URL)
    yield KeyautoConnectDto(db_connect)
    db_connect.close_db_connection()

# @fixture(scope='session')
# def keyauto_connect_account() -> AccountUserTableQueries:
# """
# Возвращает объект DTO с наборами методов для взаимодействия через SQL-Alchemy с таблицами ka_integration_dms

# :return: Объект DTO с наборами методов для взаимодействия через SQL-Alchemy с таблицами ka_integration_dms
# """
# db_connect = SqlConnect(KMP_DB_TWO_URL)
# yield AccountUserTableQueries(db_connect)
# db_connect.close_db_connection()
