from __future__ import annotations
from typing import Protocol, Any, Type

from example_system import config
from example_system.message import Message


def email_sender_provider() -> Type[EmailSender]:
    if config.TEST_ENV:
        return MockyEmailSender
    return RemoteEmailSender


class EmailSender(Protocol):
    def send_message(self, message: Message) -> None:
        ...


class RemoteEmailSender:

    HOST = "..."

    def __init__(self) -> None:
        self.connection = self._connect_with_remote_server()

    def send_message(self, message: Message) -> None:
        print("Send message for real")
        # self.connection.send(message)

    def _connect_with_remote_server(self) -> Any:
        return None


class MockyEmailSender:
    def send_message(self, message: Message) -> None:
        print("Mock email sending: ")
        print(f"FROM: {message.from_address}")
        print(f"TO: {message.to_address}")
        print(f"Content: {message.content}")
        print(20 * "-")
