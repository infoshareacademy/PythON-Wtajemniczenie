# Napisz wzorzec regularny dopasowujący inny wariant kodu pocztowego:
#     1. dwie wielkie litery (alfabetu łacińskiego)
#     2. myślnik
#     3. trzy znaki (dowolny z): mała lub wielka litera (alfabetu łacińskiego) lub cyfra
import re


def run_example():
    matching_examples = ["AB-000", "EE-aB8", "EE-ac8", "EE-AAA"]
    examples_without_match = ["00-000", "Aa-000", "A0-000", "AA000"]

    pattern = re.compile(r"[A-Z][A-Z]-[a-zA-Z0-9][a-zA-Z0-9][a-zA-Z0-9]")

    for example in matching_examples:
        print(pattern.findall(example))

    print(20 * "-")
    for example in examples_without_match:
        print(pattern.findall(example))


if __name__ == "__main__":
    run_example()
