from decimal import Decimal

from calculator import calculate_investment_results


def test_investment_equals_capital_if_no_interest():
    investment_result = calculate_investment_results(
        yearly_amount=1_000, ike_interest=Decimal(0), other_interest=Decimal(0), investing_years=1
    )
    assert investment_result == 1_000

    investment_result = calculate_investment_results(
        yearly_amount=1_000, ike_interest=Decimal(0), other_interest=Decimal(0), investing_years=4
    )
    assert investment_result == 4_000


def test_ike():
    investment_result = calculate_investment_results(
        yearly_amount=1_000, ike_interest=Decimal(5), other_interest=Decimal(0), investing_years=2
    )
    assert investment_result == int(2_050 * 1.05)
    investment_result = calculate_investment_results(
        yearly_amount=2_000, ike_interest=Decimal(10), other_interest=Decimal(5), investing_years=3
    )
    assert investment_result == int(2_0 * 1.05)
