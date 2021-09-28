from document_system.complex_form import ComplexForm


class FormBuilder:
    def __init__(self) -> None:
        self.form = ComplexForm()

    def reset(self) -> None:
        self.form = ComplexForm()

    def get_form(self) -> ComplexForm:
        return self.form

    def build_basic_personal_section(self, heading: str) -> None:
        content = f"--{heading}--\n"
        content += "First name: < >\n"
        content += "Last name: < >\n"
        self.form.extend_content(content)

    def build_email_section(self) -> None:
        self.form.extend_content("Email: < >\n")

    def build_phone_section(self) -> None:
        self.form.extend_content("Phone: < >\n")

    def build_details_section(self, heading: str) -> None:
        content = f"--{heading}--\n"
        content += "Age: < >\n"
        content += "Address: < >\n"
        self.form.extend_content(content)

    def build_ue_regulatory_info(self) -> None:
        self.form.extend_content("UE info \n")

    def build_usa_regulatory_info(self) -> None:
        self.form.extend_content("Some required in forms in USA \n")
