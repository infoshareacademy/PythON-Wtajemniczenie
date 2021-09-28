from document_system.document_generator import generator_by_format, DocumentFormat


def workflow_1(document_format: DocumentFormat) -> str:
    print("Wykonuję jakąś pracę")
    print("Oprócz tego generuję raport finansowy dla użytkownika")
    document_generator = generator_by_format(document_format)
    finance_report = document_generator.generate_finance_report(finance_data={})
    return finance_report.render()


def workflow_2(dst_email: str, document_format: DocumentFormat) -> None:
    print("Generuję raport finansowy i wysyłam go mailem")
    document_generator = generator_by_format(document_format)
    finance_report = document_generator.generate_finance_report(finance_data={})
    rendered_document = finance_report.render()
    print(f"Wysyłam do {dst_email} raport finansowy: {rendered_document}")
