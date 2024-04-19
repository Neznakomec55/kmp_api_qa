from dataclasses import dataclass

from builtin_types import SqlConnect
from sql_queries.keyauto import AccountUserTableQueries
from sql_queries.keyauto import AuthorizationSmsCodeTableQueries
from sql_queries.keyauto import AuthTokenTableQueries
from sql_queries.keyauto import ReferenceCityTableQueries


@dataclass
class KeyautoConnectDto:
    account_user_table: AccountUserTableQueries
    auth_token_table: AuthTokenTableQueries
    authorization_sms_code_table: AuthorizationSmsCodeTableQueries
    reference_city_table: ReferenceCityTableQueries

    def __init__(self, db_connect: SqlConnect):
        self.account_user_table = AccountUserTableQueries(db_connect)
        self.auth_token_table = AuthTokenTableQueries(db_connect)
        self.authorization_sms_code_table = AuthorizationSmsCodeTableQueries(db_connect)
        self.reference_city_table = ReferenceCityTableQueries(db_connect)
