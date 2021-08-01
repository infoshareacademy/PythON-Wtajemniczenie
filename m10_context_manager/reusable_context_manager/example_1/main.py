from new_movies.logger import Logger


def some_work_with_error() -> None:
    print("Some work")
    raise ValueError("We have a problem!")


def some_work() -> None:
    print("Just some work")


def run_example() -> None:
    logger = Logger()
    with logger:
        logger.info_log("Start system...")
        some_work()

    try:
        with logger:
            logger.info_log("Will do something risky")
            some_work_with_error()
    except ValueError:
        pass

    logger.save_logs()


if __name__ == "__main__":
    run_example()
