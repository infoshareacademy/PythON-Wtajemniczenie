from document_system.account_contract import AccountContract


class ContractBuilder:
    def __init__(self) -> None:
        self.account_contract = AccountContract()

    def reset(self) -> None:
        self.account_contract = AccountContract()

    def build_welcome_page(self, first_name: str, last_name: str) -> None:
        self.account_contract.extend_content(
            f"Umowa o konto pomiędzy bankiem a {first_name} {last_name} \n\n"
        )

    def build_personal_info(self, first_name: str, last_name: str) -> None:
        self.account_contract.extend_content(
            f"Konto zakładane jest dla osoby fizycznej {first_name} {last_name} \n"
        )

    def build_company_info(self, company_name: str) -> None:
        self.account_contract.extend_content(f"Konto zakładane jest dla firmy {company_name} \n")

    def build_debit_card_info(self) -> None:
        self.account_contract.extend_content(f"Warunki dla karty debetowej... \n")

    def build_saving_promotion_info(self) -> None:
        self.account_contract.extend_content(f"Promocja na konto oszczędnościowe: ... \n")

    def get_contract(self) -> AccountContract:
        return self.account_contract
