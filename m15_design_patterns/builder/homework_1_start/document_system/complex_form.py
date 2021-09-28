from enum import Enum
from typing import Optional


class FormType(Enum):
    UE = "UE"
    USA = "USA"


class ComplexForm:
    def __init__(
        self,
        personal_section_heading: str,
        email_input: bool,
        phone_input: bool,
        details_section: bool,
        details_section_heading: Optional[str],
        form_type: FormType,
    ) -> None:
        self.content = self._personal_section(personal_section_heading, email_input, phone_input)

        if details_section:
            if not details_section_heading:
                details_section_heading = "Details"
            self.content += self._details_section(details_section_heading)

        if form_type is FormType.UE:
            self.content += self._ue_regulatory_info()
        else:
            self.content += self._usa_regulatory_info()

    def _personal_section(
        self, personal_section_heading: str, email_input: bool, phone_input: bool
    ) -> str:
        content = f"--{personal_section_heading}--\n"
        content += "First name: < >\n"
        content += "Last name: < >\n"
        if email_input:
            content += "Email: < >\n"
        if phone_input:
            content += "Phone: < >\n"
        return content

    def _details_section(self, details_section_heading: str) -> str:
        content = f"--{details_section_heading}--\n"
        content += "Age: < >\n"
        content += "Address: < >\n"
        return content

    def _ue_regulatory_info(self) -> str:
        return f"UE info \n"

    def _usa_regulatory_info(self) -> str:
        return f"Some required in forms in USA \n"

    def render(self) -> str:
        return self.content
