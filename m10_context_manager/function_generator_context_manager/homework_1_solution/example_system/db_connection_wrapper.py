from contextlib import contextmanager
from typing import Iterator

from example_system.database_connection import DatabaseConnection


@contextmanager
def db_connection_wrapper() -> Iterator[DatabaseConnection]:
    db_connection = DatabaseConnection()
    db_connection.connect()
    try:
        yield db_connection
    except Exception as error:
        db_connection.rollback()
        raise error
    else:
        db_connection.commit()
    finally:
        db_connection.close()
