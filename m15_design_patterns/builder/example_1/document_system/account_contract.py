from enum import Enum
from typing import Optional


class AccountType(Enum):
    PERSONAL = "PERSONAL"
    COMPANY = "COMPANY"


class AccountContract:
    def __init__(
        self,
        first_name: str,
        last_name: str,
        account_type: AccountType,
        company_name: Optional[str],
        debit_card_selected: bool,
        saving_promotion: bool,
    ) -> None:
        self.content = self._welcome_page(first_name, last_name)
        if account_type is AccountType.PERSONAL:
            self.content += self._personal_info(first_name, last_name)
        else:
            if not company_name:
                raise ValueError("Company name is required for company contract")
            self.content += self._company_info(company_name)

        if debit_card_selected:
            self.content += self._debit_card_info()

        if saving_promotion:
            self.content += self._saving_promotion_info()

    def _welcome_page(self, first_name: str, last_name: str) -> str:
        return f"Umowa o konto pomiędzy bankiem a {first_name} {last_name} \n\n"

    def _personal_info(self, first_name: str, last_name: str) -> str:
        return f"Konto zakładane jest dla osoby fizycznej {first_name} {last_name} \n"

    def _company_info(self, company_name: str) -> str:
        return f"Konto zakładane jest dla firmy {company_name} \n"

    def _debit_card_info(self) -> str:
        return f"Warunki dla karty debetowej... \n"

    def _saving_promotion_info(self) -> str:
        return f"Promocja na konto oszczędnościowe: ... \n"

    def render(self) -> str:
        return self.content
