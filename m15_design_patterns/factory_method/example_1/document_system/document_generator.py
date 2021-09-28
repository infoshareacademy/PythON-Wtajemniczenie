from enum import Enum
from typing import Protocol

from document_system.document import Document, FinanceReportPdf, FinanceReportDoc


class DocumentFormat(Enum):
    PDF = "PDF"
    DOC = "DOC"


# Jeżeli tworzenie dokumentów miałoby jakąś wspólną (pomiędzy formatami) logikę
# To zamiast Protocol moglibyśmy zastosować klasę abstrakcyjną
# I w niej umieścić tę logikę
class DocumentGenerator(Protocol):
    def generate_finance_report(self, finance_data: dict[str, str]) -> Document:
        ...


class PdfDocumentGenerator:
    def generate_finance_report(self, finance_data: dict[str, str]) -> FinanceReportPdf:
        return FinanceReportPdf(finance_data)


class DocDocumentGenerator:
    def generate_finance_report(self, finance_data: dict[str, str]) -> FinanceReportDoc:
        return FinanceReportDoc(finance_data)


def generator_by_format(document_format: DocumentFormat) -> DocumentGenerator:
    if document_format is DocumentFormat.PDF:
        return PdfDocumentGenerator()
    else:
        return DocDocumentGenerator()
