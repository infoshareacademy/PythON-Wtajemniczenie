from typing import Protocol


class Report(Protocol):
    def render(self) -> str:
        ...

    def generate_summary(self) -> str:
        ...


class FinanceReportPdf:
    def __init__(self, finance_data: dict[str, str]) -> None:
        self.finance_data = finance_data

    def render(self) -> str:
        return "Raport Finansowy w PDF"

    def generate_summary(self) -> str:
        return "PDF-Summary: 10"


class FinanceReportDoc:
    def __init__(self, finance_data: dict[str, str]) -> None:
        self.finance_data = finance_data

    def render(self) -> str:
        return "Raport Finansowy w formacie doc"

    def generate_summary(self) -> str:
        return "DOC-Summary: 10"
