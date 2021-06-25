import re


def run_example():
    number_at_begin_txt = "+48 123 456 789 <- to jest numer"
    number_pattern = re.compile(r"\+(\d{2})((?: \d{3}){3})")
    number_match = number_pattern.match(number_at_begin_txt)
    # Całe dopasowanie
    print(number_match.group())
    print(number_match.group(0))

    # Poszczególne grupy
    print("Grupa 1:", number_match.group(1))
    print("Grupa 2:", number_match.group(2))

    # print("Grupa 1:", number_match[1])
    # print("Grupa 2:", number_match[2])
    #
    # for group_number, group in enumerate(number_match.groups()):
    #     print(f"Grupa {group_number + 1}:", group)

    # Pozycja znalezionych dopasowań
    # print(number_match.start(), number_match.end())
    # print(number_match.start(1), number_match.end(1))
    # print(number_match.start(2), number_match.end(2))

    # Brak dopasowania
    # number_at_end_txt = "To jest numer -> +48 123 456 789"
    # number_match = number_pattern.match(number_at_end_txt)
    # print(number_match)


if __name__ == "__main__":
    run_example()
