from shop.order import Order


def run_example() -> None:
    my_order = Order()
    my_order.add_element("ciastka", quantity=2)
    my_order.add_element("czekolada")
    my_order.add_element("chleb")
    my_order.add_element("ziemniaki", quantity=4)

    my_order.remove_element("ciastka")
    my_order.add_element("chleb")

    second_order = Order()
    second_order.add_element("jabłko")
    second_order.add_element("pomidor")
    second_order.add_element("pomarańcza")

    my_order.merge_orders(second_order)
    print(my_order)


if __name__ == "__main__":
    run_example()
