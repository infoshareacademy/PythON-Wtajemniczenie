import time

from bank.account import Account


def transfer_money(src_account: Account, dst_account: Account, amount: int) -> None:
    print("Rozpoczynam proces przelewu środków")
    if src_account.money_amount >= amount:
        # time.sleep(1)
        print("Pieniędzy wystarczy na przelew")
        src_account.money_amount -= amount
        dst_account.money_amount += amount
        print("Przelew został zrealizowany")
    else:
        print("Za mało pieniędzy na przelew")
        print("Przelew został ODRZUCONY")


def charge_bank_fees(account: Account, amount: int) -> None:
    print("Rozpoczynam proces obciążania konta cyklicznymi opłatami")
    if account.money_amount >= amount:
        print("Pieniędzy wystarczy na opłaty")
        account.money_amount -= amount
        print("Proces pobierania opłat zakończony sukcesem")
    else:
        print("Brak środków na pokrycie opłat!")
        print("Proces pobierania opłat NIE POWIÓDŁ się")
