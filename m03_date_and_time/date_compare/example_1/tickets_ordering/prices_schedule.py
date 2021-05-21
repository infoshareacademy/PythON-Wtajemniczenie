from dataclasses import dataclass
from datetime import date


@dataclass
class PriceSwitchMoment:
    price_switch_date: date
    price_up_to_moment: int


PRICES_SCHEDULE = [
    PriceSwitchMoment(price_switch_date=date(year=2021, month=1, day=31), price_up_to_moment=150),
    PriceSwitchMoment(price_switch_date=date(year=2021, month=4, day=30), price_up_to_moment=250),
    PriceSwitchMoment(price_switch_date=date(year=2021, month=6, day=30), price_up_to_moment=350),
    PriceSwitchMoment(price_switch_date=date(year=2021, month=7, day=15), price_up_to_moment=500),
]
