from typing import Sequence

from tax_calculator.income import Taxable


def calculate_overall_tax_value(incomes: Sequence[Taxable]) -> int:
    return sum([income.tax_value() for income in incomes])
