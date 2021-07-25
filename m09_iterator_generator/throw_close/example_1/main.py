from typing import Generator

from example_system.database_coonnection import DatabaseConnection, QueryResults, QueryError


def db_connector(connection_str: str) -> Generator[QueryResults, str, None]:
    connection = DatabaseConnection(connection_str)
    try:
        query_result = QueryResults()
        while True:
            query = yield query_result
            query_result = connection.execute(query)
    except QueryError as error:
        print(f"Error logging: {error}")
    finally:
        connection.close()


def run_example() -> None:
    db = db_connector("postgresql://...")
    next(db)

    select_result = db.send("SELECT ...")
    insert_result = db.send("INSERT ...")

    print(select_result)
    print(insert_result)
    db.close()
    print("Do some work")


if __name__ == "__main__":
    run_example()
