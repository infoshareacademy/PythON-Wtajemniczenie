import threading

import time

from bank.account import Account


print_lock = threading.Lock()

def transfer_money(src_account: Account, dst_account: Account, amount: int) -> None:
    with print_lock:
        print("Rozpoczynam proces przelewu środków")
        with src_account.money_lock:
            if src_account.money_amount >= amount:
                time.sleep(3)
                print("Pieniędzy wystarczy na przelew")
                src_account.money_amount -= amount
                dst_account.money_amount += amount
                print("Przelew został zrealizowany")
            else:
                print("Za mało pieniędzy na przelew")
                print("Przelew został ODRZUCONY")


def charge_bank_fees(account: Account, amount: int) -> None:
    with print_lock:
        print("Rozpoczynam proces obciążania konta cyklicznymi opłatami")
        with account.money_lock:
            if account.money_amount >= amount:
                print("Pieniędzy wystarczy na opłaty")
                account.money_amount -= amount
                print("Proces pobierania opłat zakończony sukcesem")
            else:
                print("Brak środków na pokrycie opłat!")
                print("Proces pobierania opłat NIE POWIÓDŁ się")
