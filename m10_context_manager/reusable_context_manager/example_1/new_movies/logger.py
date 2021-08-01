from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from types import TracebackType
from typing import Optional, Type

from new_movies.logs_service import LogsService


class LogLevel(Enum):
    ERROR = "ERROR"
    INFO = "INFO"


@dataclass
class Log:
    level: LogLevel
    message: str
    timestamp: datetime

    def __str__(self) -> str:
        return f"[{self.level.value}][{self.timestamp.isoformat()}]: {self.message}"


class Logger:
    def __init__(self) -> None:
        self.logs: list[Log] = []

    def __enter__(self) -> Logger:
        return self

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_val: Optional[BaseException],
        exc_tb: Optional[TracebackType],
    ) -> None:
        if exc_val:
            self.error_log(exc_val)

    def info_log(self, message: str) -> None:
        self.logs.append(Log(
            level=LogLevel.INFO,
            message=message,
            timestamp=datetime.now()
        ))

    def error_log(self, message: str) -> None:
        self.logs.append(Log(
            level=LogLevel.ERROR,
            message=message,
            timestamp=datetime.now()
        ))

    def save_logs(self) -> None:
        logs_pack = [str(log) for log in self.logs]
        LogsService().send_logs(logs_pack)

