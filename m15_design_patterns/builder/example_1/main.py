from document_system.account_contract import AccountContract, AccountType


def run_example() -> None:
    my_account_contract = AccountContract(
        first_name="Mikołaj",
        last_name="Lewandowski",
        account_type=AccountType.PERSONAL,
        company_name=None,
        debit_card_selected=False,
        saving_promotion=True,
    )
    print(20 * "-")
    print(my_account_contract.render())
    print(20 * "-")

    company_account_contract = AccountContract(
        first_name="Jan",
        last_name="Kowalski",
        account_type=AccountType.COMPANY,
        company_name="Kodzik i spółka",
        debit_card_selected=True,
        saving_promotion=False,
    )
    print(company_account_contract.render())
    print(20 * "-")


if __name__ == "__main__":
    run_example()
