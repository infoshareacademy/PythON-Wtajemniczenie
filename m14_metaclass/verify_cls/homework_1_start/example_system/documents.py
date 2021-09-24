from typing import ClassVar


class Document:
    TEMPLATE_PATH: ClassVar[str] = "..."


class FinanceReport(Document):
    TEMPLATE_PATH: ClassVar[str] = "/statics/documents/finance-report.html"

    def __init__(self, data: dict[str, str]) -> None:
        pass


class SalesSummary(Document):
    TEMPLATE_PATH: ClassVar[str] = "/statics/documents/sales-summary.html"

    def __init__(self, top_text: str, some_data: str) -> None:
        pass
