from typing import Any
from typing import Sequence

from builtin_types import SqlConnect
from sql_queries.base_keyauto import Keyauto


class AuthTokenTableQueries(Keyauto):
    """
    Запросы для Таблицы authtoken_token
    """

    def __init__(self, connector: SqlConnect):
        super().__init__(connector)
        self.select_from_table_authorization_token_by_phone_table = None

    def select_from_table_authtoken_token_by_phone(self, phone: str) -> Sequence[Any]:
        """
        Находит все значения в таблице authtoken_token по фильтру phone
        :return: Возвращает значене последнего СМС-кода из таблицы authtoken_token
        :param phone: Значение столбца phone для поиска таблице authtoken_token
        """
        return self._base_select_all_from_table_by_one_condition(
            table=self.authtoken_token_table,
            table_column='phone',
            condition_value=phone
        )
