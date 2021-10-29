from eshop.order_2 import Order

# Zamówienie jest równe innemu gdy:
# Imię i nazwisko klienta jest takie samo
# Obydwa zawierają takie same elementy


def test_add_element():
    jan_order = Order(client_first_name="Jan", client_last_name="Nowak")
    jan_order.add_element("Rower", quantity=1, price=3_500)

    assert len(jan_order.elements) == 1
    assert jan_order.elements[0].product == "Rower"
    assert jan_order.elements[0].quantity == 1
    assert jan_order.elements[0].price == 3_500


def test_empty_orders_equality():
    jan_order = Order(client_first_name="Jan", client_last_name="Nowak")
    other_jan_order = Order(client_first_name="Jan", client_last_name="Nowak")
    ula_order = Order(client_first_name="Ula", client_last_name="Nowak")
    jan_kowalski_order = Order(client_first_name="Jan", client_last_name="Kowalski")

    assert jan_order == other_jan_order
    assert jan_order != 0
    assert jan_order != ula_order
    assert jan_order != jan_kowalski_order


def test_orders_with_different_elements_are_not_equal():
    jan_order = Order(client_first_name="Jan", client_last_name="Nowak")
    jan_order.add_element("Rower", quantity=1, price=3_500)
    other_jan_order = Order(client_first_name="Jan", client_last_name="Nowak")
    other_jan_order.add_element("Opona", quantity=2, price=50)

    assert jan_order != other_jan_order


def test_orders_with_different_number_of_elements_are_not_equal():
    jan_order = Order(client_first_name="Jan", client_last_name="Nowak")
    jan_order.add_element("Rower", quantity=1, price=3_500)
    other_jan_order = Order(client_first_name="Jan", client_last_name="Nowak")
    other_jan_order.add_element("Rower", quantity=1, price=3_500)
    other_jan_order.add_element("Opona", quantity=2, price=50)

    assert jan_order != other_jan_order
