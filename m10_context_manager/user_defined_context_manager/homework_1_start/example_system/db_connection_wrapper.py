from types import TracebackType
from typing import Optional, Type

from example_system.database_connection import DatabaseConnection


class DBConnectionWrapper:
    # TODO: Implement context manager here

    def __enter__(self) -> DatabaseConnection:
        pass

    def __exit__(
            self,
            exc_type: Optional[Type[BaseException]],
            exc_val: Optional[BaseException],
            exc_tb: Optional[TracebackType],
    ) -> None:
        pass
