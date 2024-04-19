from typing import Any
from typing import Sequence

from sql_queries.base_keyauto import Keyauto


class AuthorizationSmsCodeTableQueries(Keyauto):
    """
    Запросы для Таблицы authorization_smscode
    """

    def select_from_table_authorization_sms_code_by_phone(self, phone: str) -> Sequence[Any]:
        """
        Находит все значения в таблице authorization_smscode по фильтру phone

        :param phone: Значение столбца phone для поиска таблице authorization_smscode
        :return: Возвращает значенеи последнего СМС-кода из таблицы authorization_smscode  по номеру телефона
        """
        return self._base_select_all_from_table_by_one_condition(
            table=self.authorization_sms_code_table,
            table_column='phone',
            condition_value=phone
        )
