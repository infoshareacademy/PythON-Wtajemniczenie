from example_system.db_connection_wrapper import DBConnectionWrapper


def process_data() -> None:
    pass


def process_data_with_error() -> None:
    raise Exception("Something went wrong")


def run_example() -> None:
    with DBConnectionWrapper() as db_connection:
        db_connection.execute("SELECT * FROM USERS;")
        db_connection.execute("SELECT * FROM CUSTOMERS;")
        db_connection.execute("INSERT ...")
        process_data()

    with DBConnectionWrapper() as db_connection:
        db_connection.execute("SELECT * FROM USERS;")
        db_connection.execute("SELECT * FROM CUSTOMERS;")
        db_connection.execute("INSERT ...")
        process_data_with_error()


if __name__ == "__main__":
    run_example()
