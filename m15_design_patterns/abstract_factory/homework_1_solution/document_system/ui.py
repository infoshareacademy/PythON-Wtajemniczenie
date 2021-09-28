from abc import ABC, abstractmethod
from enum import Enum
from typing import Protocol

from document_system import settings
from document_system.button import LinuxButton, WindowsButton
from document_system.text_input import WindowsInput, LinuxInput


class Renderable(Protocol):
    def render(self) -> None:
        ...


class UIType(Enum):
    LINUX = "LINUX"
    WINDOWS = "WINDOWS"


class UI(ABC):
    def __init__(self) -> None:
        self.header_text = "Default"
        self.elements: list[Renderable] = []

    @abstractmethod
    def add_button(self, button_text: str) -> None:
        ...

    @abstractmethod
    def add_input(self) -> None:
        ...

    def render(self) -> None:
        print(f"----{self.header_text}----", "\n")
        for element in self.elements:
            element.render()

        print(f"----{len(self.header_text) * '-'}----", "\n")


class LinuxUI(UI):
    def add_button(self, button_text: str) -> None:
        self.elements.append(LinuxButton(button_text))

    def add_input(self) -> None:
        self.elements.append(LinuxInput())


class WindowsUI(UI):
    def add_button(self, button_text: str) -> None:
        self.elements.append(WindowsButton(button_text))

    def add_input(self) -> None:
        self.elements.append(WindowsInput())

    def render(self) -> None:
        print("THIS IS WINDOWS!")
        super().render()


def ui_from_settings() -> UI:
    ui_type = UIType(settings.USER_UI)
    if ui_type is UIType.LINUX:
        return LinuxUI()
    else:
        return WindowsUI()
