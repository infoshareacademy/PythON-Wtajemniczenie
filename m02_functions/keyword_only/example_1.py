def run_example():
    loan_amount = int(input("Podaj wartość kredytu: "))
    property_value = int(input("Podaj wartość nieruchomości: "))

    is_affordable = check_affordability(loan_amount, property_value)
    print_results(is_affordable)


def check_affordability(loan_amount, property_value):
    loan_to_value = loan_amount / property_value
    return loan_to_value <= 0.8


def print_results(is_affordable):
    if is_affordable:
        print("Możesz wziąć kredyt!")
    else:
        print("Niestety nie możesz wziąć kredytu...")


if __name__ == "__main__":
    run_example()
