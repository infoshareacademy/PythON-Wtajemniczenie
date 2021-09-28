from typing import Protocol


class WelcomeLetter(Protocol):
    def render(self) -> str:
        ...

    def sign(self, signature: str) -> None:
        ...


class WelcomeLetterPdf:
    def __init__(self, name: str) -> None:
        self.name = name
        self.signature = ""

    def render(self) -> str:
        return f"PDF\n Witaj {self.name}! \n\n Treść listu \n {self.signature}"

    def sign(self, signature: str) -> None:
        self.signature = f"Podpisano: {signature}"


class WelcomeLetterDoc:
    def __init__(self, name: str) -> None:
        self.name = name
        self.signature = ""

    def render(self) -> str:
        return f"DOC\n Witaj {self.name}! \n\n Treść listu \n {self.signature}"

    def sign(self, signature: str) -> None:
        self.signature = f"Podpisano: {signature}-doc"
