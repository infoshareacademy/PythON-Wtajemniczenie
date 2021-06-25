#  Zmodyfikuj rozwiązanie pierwszego zadania wykorzystując metodę finditer.
#  Do wypisywanych wyników dodaj informacje o całym dopasowanym adresie
#  oraz o jego pozycji (indeks początkowy i końcowy pełnego dopasowania).
import re


def run_example():
    example_text = "To jest tekst, który ma adresy email: mikolaj@pyjazz.com oraz JanPrzykładowy@pyjazz.pl"
    find_all_emails(example_text)


def find_all_emails(text):
    email_pattern = re.compile(r"(\w+)@(\w+)((?:\.\w+)+)")
    for email_match in email_pattern.finditer(text):
        print_email_details(email_match)


def print_email_details(email_match):
    print(20 * "-")
    print(f"Adres email: {email_match.group()} znaleziony na indeksach od: {email_match.start()} do {email_match.end()}")
    print("Składa się z:")
    print(f"Nazwy: {email_match.group(1)}")
    print(f"Domeny: {email_match.group(2)}")
    print(f"Rozszerzenia domeny: {email_match.group(3)}")


if __name__ == "__main__":
    run_example()
