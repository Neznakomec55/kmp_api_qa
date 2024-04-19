from typing import Any
from typing import Sequence

from sqlalchemy import Table
from sqlalchemy.sql import delete
from sqlalchemy.sql import select
from sqlalchemy.sql.base import Executable

from sqlalchemy import CursorResult
from builtin_types import SqlConnect


class BaseQueries:
    """
    Базовые запросы на SQL Alchemy
    """
    def __init__(self, connector: SqlConnect):
        self._sql_connect = connector
        self._meta = self._sql_connect.get_db_metadata()

    def _execute_script_by_alchemy(self, sql_query: Executable) -> CursorResult[Any]:
        """
        Выполнение запроса SQL при помощи синтаксиса Alchemy без подтверждения (без коммита).
        :param sql_query: SQL запрос в виде синтаксиса Alchemy.
        :return CursorResult: Возвращает ответ от базы данных в виде объекта CursorResult.
        """
        return self._sql_connect.execute_script_by_alchemy(sql_query)

    def _execute_script_by_alchemy_with_commit(self, sql_query: Executable) -> CursorResult[Any]:
        """
        Выполнение запроса SQL при помощи синтаксиса Alchemy с подтверждением (с коммитом).
        :param sql_query: SQL запрос в виде синтаксиса Alchemy.
        :return CursorResult: Возвращает ответ от базы данных в виде объекта CursorResult.
        """
        return self._sql_connect.execute_script_by_alchemy_with_commit(sql_query)

    def _base_select_all_from_table_by_one_condition(
            self,
            table: Table,
            table_column: str,
            condition_value: str
    ) -> Sequence[Any]:
        """
        Выполняет SQL SELECT-запрос по одному условию поиска
        (SELECT * FROM <table> WHERE <table>.<column> = '<condition_value>')
        :param table: Таблица для выборки
        :param table_column: Название колонки для поиска по условию
        :param condition_value: Значения условия выборки
        :return: Возвращает все значения из таблицы по условию поиска
        """
        if condition_value.isdigit():
            condition_value = int(condition_value)

        sql_query = select(table).where(table.c[table_column] == condition_value)
        return self._execute_script_by_alchemy(sql_query).fetchall()

    def _base_select_one_from_table_by_one_condition_get_dict(
            self,
            table: Table,
            table_column: str,
            condition_value: str
    ) -> Sequence[Any]:
        """
        Выполняет SQL SELECT-запрос по одному условию поиска
        (SELECT <table>.<column> AS <table>_<column> FROM <table> WHERE <table>.<column> = '<condition_value>')
        :param table: Таблица для выборки
        :param table_column: Название колонки для поиска по условию
        :param condition_value: Значения условия выборки
        :return: Возвращает одно значения из таблицы по условию поиска
        """
        if condition_value.isdigit():
            condition_value = int(condition_value)

        label_column = f'{table.name}_{table_column}'
        sql_query = select(
            table.c[table_column].label(label_column)
        ).where(table.c[table_column] == condition_value)
        return self._execute_script_by_alchemy(sql_query).fetchone()

    def _base_delete_from_table_by_one_condition(
            self,
            table: Table,
            table_column: str,
            condition_value: str
    ) -> None:
        """
        Выполняет SQL DELETE-запрос по одному условию поиска
        (DELETE FROM <table> WHERE <table>.<column> = '<condition_value>')
        :param table: Таблица выполнения запроса
        :param table_column: Название колонки для поиска по условию
        :param condition_value: Значения условия выборки
        :return: None
        """
        if condition_value.isdigit():
            condition_value = int(condition_value)

        sql_query = delete(table).where(table.c[table_column] == condition_value)
        self._execute_script_by_alchemy_with_commit(sql_query)
