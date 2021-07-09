from typing import Sequence
from typing import Union

from tax_calculator.income import Income, EmploymentIncome, SelfEmploymentIncome, InvestmentIncome


def calculate_overall_tax_value(incomes: Sequence[Income]) -> int:
    return sum([income.tax_value() for income in incomes])


# def calculate_overall_tax_value(
#     incomes: Sequence[Union[EmploymentIncome, SelfEmploymentIncome, InvestmentIncome]]
# ) -> int:
#     return sum([income.tax_value() for income in incomes])
