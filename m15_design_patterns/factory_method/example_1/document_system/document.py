from typing import Protocol


class Document(Protocol):
    def render(self) -> str:
        ...


class FinanceReportPdf:
    def __init__(self, finance_data: dict[str, str]) -> None:
        self.finance_data = finance_data

    def render(self) -> str:
        return "Raport Finansowy w PDF"


class FinanceReportDoc:
    def __init__(self, finance_data: dict[str, str]) -> None:
        self.finance_data = finance_data

    def render(self) -> str:
        return "Raport Finansowy w formacie doc"
