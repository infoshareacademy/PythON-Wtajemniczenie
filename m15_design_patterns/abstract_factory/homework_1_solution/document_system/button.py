from typing import Protocol




class Button(Protocol):
    def render(self) -> None:
        ...

    def on_click(self) -> None:
        ...


class LinuxButton:
    def __init__(self, button_text: str) -> None:
        self.button_text = button_text

    def render(self) -> None:
        print(f"({self.button_text})")

    def on_click(self) -> None:
        print("Click!")


class WindowsButton:
    def __init__(self, button_text: str) -> None:
        self.button_text = button_text

    def render(self) -> None:
        print(f"[W- {self.button_text} -W]")

    def on_click(self) -> None:
        print("Click!")
