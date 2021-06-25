# 4. Napisz wyrażenie regularne dopasowujące adres strony internetowej.
#     1. Rozpoczyna się on nazwą protokołu (http lub https)
#     2. następie występuje dwukropek i dwa znaki slash (/)
#     3. trzy litery w
#     4. kropka
#     5. Nazwa strony będąca ciągiem dowolnych znaków alfanumerycznych
#     6. Kropka
#     7. Rozszerzenie domeny czyli ciąg dowolnych znaków alfanumerycznych

import re


def run_example():
    matching_examples = ["https://www.PyJazz.pl", "http://www.pyjazz.com"]
    examples_without_match = ["www.pyjazz.pl", "https://www.pyjazz"]

    pattern = re.compile(r"https?://www\.\w+\.\w+")

    for example in matching_examples:
        print(pattern.findall(example))

    print(20 * "-")
    for example in examples_without_match:
        print(pattern.findall(example))


if __name__ == "__main__":
    run_example()
