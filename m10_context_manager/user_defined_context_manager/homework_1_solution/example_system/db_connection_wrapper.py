from types import TracebackType
from typing import Optional, Type

from example_system.database_connection import DatabaseConnection


class DBConnectionWrapper:

    def __init__(self) -> None:
        self.db_connection = DatabaseConnection()

    def __enter__(self) -> DatabaseConnection:
        self.db_connection.connect()
        return self.db_connection

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_val: Optional[BaseException],
        exc_tb: Optional[TracebackType],
    ) -> None:
        if exc_type:
            self.db_connection.rollback()
        else:
            self.db_connection.commit()
        self.db_connection.close()
