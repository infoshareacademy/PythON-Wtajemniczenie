from typing import Sequence
from typing import Union

from tax_calculator import calculation
from tax_calculator.frequency import Frequency
from tax_calculator.income import Income, EmploymentIncome, SelfEmploymentIncome, InvestmentIncome


def run_example() -> None:
    employment_income = Income(value=3500)
    self_employment_income = Income(value=1500)
    investment_income = Income(value=450)
    all_incomes = [employment_income, self_employment_income, investment_income]
    tax_to_be_paid = calculation.calculate_overall_tax_value(all_incomes)
    print(tax_to_be_paid)

    # employment_income = EmploymentIncome(value=3500)
    # self_employment_income = SelfEmploymentIncome(value=1500)
    # investment_income = InvestmentIncome(value=450, frequency=Frequency.MONTHLY)
    # all_incomes = [employment_income, self_employment_income, investment_income]
    # # all_incomes: Sequence[Union[EmploymentIncome, SelfEmploymentIncome, InvestmentIncome]] = [employment_income, self_employment_income, investment_income]
    # tax_to_be_paid = calculation.calculate_overall_tax_value(all_incomes)
    # print(tax_to_be_paid)


if __name__ == "__main__":
    run_example()
