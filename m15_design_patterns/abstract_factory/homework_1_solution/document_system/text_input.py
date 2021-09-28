from typing import Protocol


class Input(Protocol):
    def render(self) -> None:
        ...

    def on_key_pressed(self, key: str) -> None:
        ...


class LinuxInput:
    INPUT_SIZE = 10

    def __init__(self) -> None:
        self.text = ""

    def render(self) -> None:
        spacing = self.INPUT_SIZE - 2 - len(self.text)
        print(self.INPUT_SIZE * "-")
        print(f"|{spacing * ' '}|")
        print(self.INPUT_SIZE * "-")

    def on_key_pressed(self, key: str) -> None:
        self.text += key


class WindowsInput:
    INPUT_SIZE = 14

    def __init__(self) -> None:
        self.text = ""

    def render(self) -> None:
        spacing = self.INPUT_SIZE - 2 - len(self.text)
        print(self.INPUT_SIZE * "=")
        print(f"[{spacing * ' '}]")
        print(self.INPUT_SIZE * "=")

    def on_key_pressed(self, key: str) -> None:
        self.text += key
