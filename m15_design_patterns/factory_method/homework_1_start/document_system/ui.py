from abc import ABC, abstractmethod
from enum import Enum


from document_system import settings
from document_system.button import Renderable


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

    def render(self) -> None:
        print(f"----{self.header_text}----", "\n")
        for element in self.elements:
            element.render()

        print(f"----{len(self.header_text) * '-'}----", "\n")


def ui_from_settings() -> UI:
    ui_type = UIType(settings.USER_UI)
    if ui_type is UIType.LINUX:
        return ...
    else:
        return ...
