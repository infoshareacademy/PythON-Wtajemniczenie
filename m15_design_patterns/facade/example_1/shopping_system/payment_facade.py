from shopping_system.payment_api import utilities as payment_api_utilities
from shopping_system.payment_api.gold_provider import GoldProvider
from shopping_system.payment_api.green_provider import GreenProvider


def pay_for_order(dollars: int, cents: int) -> None:
    login = "LOAD_FROM_ENV"
    password = "LOAD_FROM_ENV"
    currency_code = payment_api_utilities.get_currency_system_code("USD")
    gold_provider = GoldProvider(login, password)
    if gold_provider.is_available():
        gold_provider.pay_with_usd(currency_code, dollars, cents)
    else:
        green_provider = GreenProvider()
        api_key = "LOAD_FROM_ENV"
        green_provider.connect(api_key)
        amount_in_cents = 100 * dollars + cents
        green_provider.pay_with_usd(currency_code, amount_in_cents)
