from dataclasses import dataclass
from datetime import timedelta, datetime
from zoneinfo import ZoneInfo

from new_movies import configuration


@dataclass
class AuthContext:
    failed_login_attempt = 0
    previous_attempt_datetime = None
    current_attempt_datetime = None

    @property
    def lock_time(self) -> timedelta:
        if self.failed_login_attempt >= configuration.AUTH_FAILED_EXTENDED_LIMIT:
            return configuration.AUTH_FAILED_LOCK_TIME * 2
        elif self.failed_login_attempt >= configuration.AUTH_FAILED_LIMIT:
            return configuration.AUTH_FAILED_LOCK_TIME
        return timedelta()

    def register_login_attempt(self) -> None:
        self.previous_attempt_datetime = self.current_attempt_datetime
        self.current_attempt_datetime = datetime.now(tz=ZoneInfo("UTC"))

    def should_reject_attempt_due_to_lock_time(self) -> bool:
        if self.current_attempt_datetime is None or self.previous_attempt_datetime is None:
            return False

        return self.current_attempt_datetime - self.previous_attempt_datetime < self.lock_time

    def register_failed_login_attempt(self) -> None:
        self.failed_login_attempt += 1

    def is_failures_limit_exceeded(self) -> bool:
        return self.failed_login_attempt >= configuration.AUTH_FAILED_LIMIT
