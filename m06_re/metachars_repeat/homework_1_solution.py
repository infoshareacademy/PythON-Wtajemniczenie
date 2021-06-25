# Zmodyfikuj rozwiązanie zadania dopasowującego polski kod pocztowy wykorzystując metaznaki powtórzeń.

import re


def run_example():
    matching_examples = ["00-000", "65-197"]
    examples_without_match = ["0-000", "65197", "00a111", "00-14", "aa-bbb"]

    pattern = re.compile(r"\d{2}-\d{3}")

    for example in matching_examples:
        print(pattern.findall(example))

    print(20 * "-")
    for example in examples_without_match:
        print(pattern.findall(example))


if __name__ == "__main__":
    run_example()
