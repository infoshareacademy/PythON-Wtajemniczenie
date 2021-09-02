from typing import Protocol


class Logger(Protocol):

    def log(self, message: str) -> None: ...


class ConsoleLogger:

    def log(self, message: str) -> None:
        print(message)


class FileLogger:

    def __init__(self, file_path: str) -> None:
        self.file_path = file_path

    def log(self, message: str) -> None:
        with open(self.file_path, mode="a") as log_file:
            log_file.write(message)
            log_file.write("\n")
