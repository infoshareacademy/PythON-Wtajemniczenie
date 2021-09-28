from document_system.actions import workflow_1, workflow_2
from document_system.document_generator import DocumentFormat


def run_example() -> None:
    finance_report_pdf = workflow_1(DocumentFormat.PDF)
    print(finance_report_pdf)
    print(20 * "-")

    finance_report_doc = workflow_1(DocumentFormat.DOC)
    print(finance_report_doc)
    print(20 * "-")

    workflow_2(dst_email="example@...", document_format=DocumentFormat.PDF)
    print(20 * "-")


if __name__ == "__main__":
    run_example()
