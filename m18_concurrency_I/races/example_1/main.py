import time

import threading

from bank.account import Account
from bank.actions import transfer_money, charge_bank_fees


def run_example() -> None:
    jan_account = Account(holder="Jan", money_amount=1_000)
    alicja_account = Account(holder="Alicja", money_amount=1_000)

    print(jan_account)
    print(alicja_account)

    threading.Thread(target=transfer_money, args=(jan_account, alicja_account, 1_000)).start()
    threading.Thread(target=charge_bank_fees, args=(jan_account, 500)).start()

    time.sleep(5)

    print(jan_account)
    print(alicja_account)


if __name__ == "__main__":
    run_example()
