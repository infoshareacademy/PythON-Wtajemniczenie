from datetime import date

from tickets_ordering.exceptions import NoPriceAvailable
from tickets_ordering.prices_schedule import PRICES_SCHEDULE


def order_tickets(tickets_number):
    try:
        price = calculate_price_per_ticket()
    except NoPriceAvailable:
        tickets_no_longer_available()
    else:
        total_price = price * tickets_number
        proceed_to_payment(total_price)


def calculate_price_per_ticket():
    current_date = date.today()
    for price_switch_moment in PRICES_SCHEDULE:
        if current_date <= price_switch_moment.price_switch_date:
            return price_switch_moment.price_up_to_moment
    raise NoPriceAvailable()


def tickets_no_longer_available():
    print("Niestety sprzedaż biletów na to wydarzenie została zakończona")


def proceed_to_payment(price):
    print(f"Do zapłaty: {price}")
