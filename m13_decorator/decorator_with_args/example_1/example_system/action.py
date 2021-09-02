from example_system.info_logger import info_logger
from example_system.logger import ConsoleLogger, FileLogger


# @info_logger(FileLogger("logs.txt"))
@info_logger(ConsoleLogger())
def create_order(user: str) -> None:
    print(f"Creating order for user: {user}....")
