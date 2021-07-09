from typing import Sequence

from tax_calculator.income import Income


def calculate_overall_tax_value(incomes: Sequence[Income]) -> int:
    return sum([income.tax_value() for income in incomes])

