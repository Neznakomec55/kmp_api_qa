from typing import Any
from typing import Sequence


from sql_queries.base_keyauto import Keyauto


class ReferenceCityTableQueries(Keyauto):
    """
    Запросы для Таблицы reference_city
    """

    def select_from_table_reference_city_by_id(self, city_id: str) -> Sequence[Any]:
        """
        Находит все значения в таблице authtoken_token по фильтру id
        :return: Возвращает значене последнего id из таблицы reference_city
        :param city_id: Значение столбца id для поиска таблицы reference_city
        """
        return self._base_select_all_from_table_by_one_condition(
            table=self.reference_city_table,
            table_column='Id',
            condition_value=city_id
        )
