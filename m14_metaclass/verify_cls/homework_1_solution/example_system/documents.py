from typing import ClassVar, Any, Optional


class DocumentMeta(type):
    def __new__(mcs, name: str, bases: tuple[type], class_dict: dict[str, Any]) -> Any:
        if not bases:
            return super().__new__(mcs, name, bases, class_dict)
        template: Optional[str] = class_dict.get("TEMPLATE_PATH", None)
        if not template:
            raise ValueError("Document class must provide path to the template")

        if not isinstance(template, str):
            raise ValueError("Path to document template must be a str instance")

        if not template.endswith(".html"):
            raise ValueError("Document template must be html")

        if not template.startswith("/"):
            raise ValueError("Path to document template must be absolute (starts with '/')")

        return super().__new__(mcs, name, bases, class_dict)


class Document(metaclass=DocumentMeta):
    TEMPLATE_PATH: ClassVar[str] = "..."


class FinanceReport(Document):
    TEMPLATE_PATH: ClassVar[str] = "/statics/documents/finance-report.html"

    def __init__(self, data: dict[str, str]) -> None:
        pass


class SalesSummary(Document):
    TEMPLATE_PATH: ClassVar[str] = "/statics/documents/sales-summary.html"

    def __init__(self, top_text: str, some_data: str) -> None:
        pass
