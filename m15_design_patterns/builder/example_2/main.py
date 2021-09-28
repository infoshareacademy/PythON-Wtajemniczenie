from document_system.contract_builder import ContractBuilder


def run_example() -> None:
    contract_builder = ContractBuilder()
    contract_builder.build_welcome_page(first_name="Mikołaj", last_name="Lewandowski")
    contract_builder.build_personal_info(first_name="Mikołaj", last_name="Lewandowski")
    contract_builder.build_saving_promotion_info()
    my_account_contract = contract_builder.get_contract()
    print(20 * "-")
    print(my_account_contract.render())
    print(20 * "-")

    contract_builder.reset()
    contract_builder.build_welcome_page(first_name="Jan", last_name="Kowalski")
    contract_builder.build_company_info(company_name="Kodzik i spółka")
    contract_builder.build_debit_card_info()
    company_account_contract = contract_builder.get_contract()
    print(company_account_contract.render())
    print(20 * "-")


if __name__ == "__main__":
    run_example()
