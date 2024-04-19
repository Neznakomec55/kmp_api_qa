from typing import Any

from sqlalchemy import create_engine
from sqlalchemy import CursorResult
from sqlalchemy import MetaData
from sqlalchemy.sql.base import Executable


class SqlConnect:
    def __init__(self, connection_url: str):
        """
        Создание подключения к БД.
        """
        engine = create_engine(connection_url)
        self._connect = engine.connect()

        self._metadata = MetaData()
        self._metadata.reflect(bind=engine)

    def close_db_connection(self) -> None:
        """
        Закрытие соединения с БД.
        :return: None
        """
        self._connect.close()

    def get_db_metadata(self) -> MetaData:
        """
        Возвращает Метадату
        :return: None
        """
        return self._metadata

    def _commit_execute_sql_query(self) -> None:
        """
        Подтверждение SQL запроса
        :return: None
        """
        self._connect.commit()

    def execute_script_by_alchemy(self, sql_query: Executable) -> CursorResult[Any]:
        """
        Выполнение запроса SQL при помощи синтаксиса Alchemy без подтверждения (без коммита).
        :param sql_query: SQL запрос в виде синтаксиса Alchemy.
        :return: Список строк, возвращённых запросом.
        """
        return self._connect.execute(sql_query)

    def execute_script_by_alchemy_with_commit(self, sql_query: Executable) -> CursorResult[Any]:
        """
        Выполнение запроса SQL при помощи синтаксиса Alchemy с подтверждением (с коммитом).
        :param sql_query: SQL запрос в виде синтаксиса Alchemy.
        :return: Список строк, возвращённых запросом
        """
        result = self.execute_script_by_alchemy(sql_query)
        self._commit_execute_sql_query()
        return result
