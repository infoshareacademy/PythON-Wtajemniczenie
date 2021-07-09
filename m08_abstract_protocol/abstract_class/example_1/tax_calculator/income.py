from tax_calculator.frequency import Frequency


class Income:

    TAX_RATE = 0.17

    def __init__(self, value: int) -> None:
        self.value = value

    def tax_value(self) -> int:
        return int(self.value * self.TAX_RATE)


class EmploymentIncome:

    TAX_RATE = 0.17
    TAX_FREE_AMOUNT = 1000

    def __init__(self, value: int) -> None:
        self.value = value

    def tax_value(self) -> int:
        value_to_be_taxed = max(self.value - self.TAX_FREE_AMOUNT, 0)
        return int(value_to_be_taxed * self.TAX_RATE)


class SelfEmploymentIncome:

    TAX_RATE = 0.19

    def __init__(self, value: int) -> None:
        self.value = value

    def tax_value(self) -> int:
        return int(self.value * self.TAX_RATE)


class InvestmentIncome:

    TAX_RATE = 0.19
    WEEKS_IN_YEAR = 52
    MONTHS_IN_YEAR = 12
    QUARTERS_IN_YEAR = 4

    def __init__(self, value: int, frequency: Frequency) -> None:
        self.value = value
        self.frequency = frequency

    def tax_value(self) -> int:
        return int(self.monthly_income * self.TAX_RATE)

    @property
    def monthly_income(self) -> int:
        if self.frequency is Frequency.WEEKLY:
            return int(self.value * self.WEEKS_IN_YEAR / self.MONTHS_IN_YEAR)
        elif self.frequency is Frequency.QUARTERLY:
            return int(self.value * self.QUARTERS_IN_YEAR / self.MONTHS_IN_YEAR)
        elif self.frequency is Frequency.ANNUALLY:
            return int(self.value / self.MONTHS_IN_YEAR)
        return self.value
