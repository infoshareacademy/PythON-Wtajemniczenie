from document_system.document_generator import generator_by_format, DocumentFormat


def workflow_1(document_format: DocumentFormat) -> list[str]:
    print("Wykonuję jakąś pracę")
    print("Oprócz tego generuję paczkę dokumentów dla użytkownika")
    document_generator = generator_by_format(document_format)
    finance_report = document_generator.generate_finance_report(finance_data={})
    welcome_letter = document_generator.generate_welcome_letter(name="Mikołaj")
    welcome_letter.sign("Jan Nowak")
    return [finance_report.render(), welcome_letter.render()]


def workflow_2(dst_email: str, document_format: DocumentFormat) -> None:
    print("Generuję raport finansowy i wysyłam go mailem")
    document_generator = generator_by_format(document_format)
    finance_report = document_generator.generate_finance_report(finance_data={})
    rendered_document = finance_report.render()
    print(f"Wysyłam do {dst_email} raport finansowy: {rendered_document}")
