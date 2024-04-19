from typing import Any
from typing import Sequence

from sqlalchemy.sql import select

from sql_queries.base_keyauto import Keyauto


class AccountUserTableQueries(Keyauto):
    """
    Запросы для Таблицы account_user
    """

    def select_from_table_account_user_by_phone(self, phone: str) -> Sequence[Any]:
        """
        Находит все значения в таблице authorization_smscode по фильтру phone

        :param phone: Значение столбца phone для поиска таблице authorization_smscode
        :return: Возвращает значенеи последнего СМС-кода из таблицы authorization_smscode  по номеру телефона
        """
        return self._base_select_all_from_table_by_one_condition(
            table=self.account_user_table,
            table_column='phone',
            condition_value=phone
        )[0]

    def select_account_user_join_reference_city_by_id(self, city_id: int) -> Sequence[Any]:
        """
        Возврат данных из таблиц Account и Reference City при помощи left join по city_id
        :return: возврат результата select left join запроса
        """
        join_query = self.reference_city_table \
            .join(self.account_user_table, self.reference_city_table.c.Id == self.account_user_table.c.CityId) \

        sql_query = select(
            self.reference_city_table.c.CityId,
        ).select_from(
            join_query
        ).where(self.reference_city_table.c.Id == city_id)

        return self._execute_script_by_alchemy(sql_query).fetchone()
