from shopping_system import payment_facade


def run_example() -> None:
    print("Realizujemy płatność za zamówienie")
    payment_facade.pay_for_order(dollars=120, cents=40)


if __name__ == "__main__":
    run_example()
