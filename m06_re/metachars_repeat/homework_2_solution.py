# Wykorzystując metaznaki powtórzeń zmodyfikuj rozwiązanie zadania dopasowującego “inny kod pocztowy”:
#   dwie wielkie litery (alfabetu łacińskiego),
#   opcjonalny myślnik,
#   trzy znaki (dowolny z): mała lub wielka litera (alfabetu łacińskiego lub symbole narodowe) lub cyfra

import re


def run_example():
    matching_examples = ["AB-000", "EE-aB8", "EE-ac8", "EE-AAA", "AA000"]
    examples_without_match = ["00-000", "Aa-000", "A0-000"]

    pattern = re.compile(r"[A-Z]{2}-?\w{3}")

    for example in matching_examples:
        print(pattern.findall(example))

    print(20 * "-")
    for example in examples_without_match:
        print(pattern.findall(example))


if __name__ == "__main__":
    run_example()
