from enum import Enum
from typing import Protocol

from document_system.reports import FinanceReportPdf, FinanceReportDoc, Report
from document_system.welcome_letter import WelcomeLetter, WelcomeLetterPdf, WelcomeLetterDoc


class DocumentFormat(Enum):
    PDF = "PDF"
    DOC = "DOC"


class DocumentGenerator(Protocol):
    def generate_finance_report(self, finance_data: dict[str, str]) -> Report:
        ...

    def generate_welcome_letter(self, name: str) -> WelcomeLetter:
        ...


class PdfDocumentGenerator:
    def generate_finance_report(self, finance_data: dict[str, str]) -> FinanceReportPdf:
        return FinanceReportPdf(finance_data)

    def generate_welcome_letter(self, name: str) -> WelcomeLetterPdf:
        return WelcomeLetterPdf(name)


class DocDocumentGenerator:
    def generate_finance_report(self, finance_data: dict[str, str]) -> FinanceReportDoc:
        return FinanceReportDoc(finance_data)

    def generate_welcome_letter(self, name: str) -> WelcomeLetterDoc:
        return WelcomeLetterDoc(name)


def generator_by_format(document_format: DocumentFormat) -> DocumentGenerator:
    if document_format is DocumentFormat.PDF:
        return PdfDocumentGenerator()
    else:
        return DocDocumentGenerator()
