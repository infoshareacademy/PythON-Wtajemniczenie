from order_system import order_actions_facade


def run_example() -> None:
    print("Aktualizujemy status zamówienia")
    order_actions_facade.update_order_status(order_number="ORD-12581", new_status="COMPLETED")


if __name__ == "__main__":
    run_example()
