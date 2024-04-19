from sqlalchemy import Table

from builtin_types import SqlConnect
from sql_queries.base_queries import BaseQueries


class Keyauto(BaseQueries):
    """
    Базовый класс для наследования Таблиц для базы keyauto
    """
    def __init__(self, connector: SqlConnect):
        super().__init__(connector)

        self.authorization_sms_code_table = Table('authorization_smscode', self._meta, autoload=True)
        self.authtoken_token_table = Table('authtoken_token', self._meta, autoload=True)
        self.account_user_table = Table('account_user', self._meta, autoload=True)
        self.reference_city_table = Table('reference_city', self._meta, autoload=True)
