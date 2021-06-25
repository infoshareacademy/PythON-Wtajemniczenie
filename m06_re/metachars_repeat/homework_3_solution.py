# Napisz wyrażenie regularne dopasowujące adres mailowy. Składa się on z nazwy, domeny  oraz rozszerzenia.
# Nazwa i domena rozdzielone są znakiem małpy (@). Nazwa to ciąg dowolnych znaków alfanumerycznych.
# Domena i rozszerzenia są rozdzielone kropką. Każde z nich to dowolny ciąg znaków alfanumerycznych.
# Zarówno nazwa, domena jak i rozszerzenie musi posiadać co najmniej jeden znak.

import re


def run_example():
    matching_examples = ["nazwa@domena.com", "nAzWa@dOmEnA.PL"]
    examples_without_match = ["nazwa@domenacom", "nazwadomena.com", "nazwa@.com", "@domena.com"]

    pattern = re.compile(r"\w+@\w+\.\w+")

    for example in matching_examples:
        print(pattern.findall(example))

    print(20 * "-")
    for example in examples_without_match:
        print(pattern.findall(example))


if __name__ == "__main__":
    run_example()
