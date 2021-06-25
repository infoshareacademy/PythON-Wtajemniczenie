# Napisz funkcje która przyjmie tekst zawierający potencjalnie wiele różnych adresów email
# a następnie wypisze każdy z nich (z podziałem na nazwę, domenę i rozszerzenie).
# Wykorzystaj metodę findall
import re


def run_example():
    example_text = "To jest tekst, który ma adresy email: mikolaj@pyjazz.com oraz JanPrzykładowy@pyjazz.pl"
    find_all_emails(example_text)


def find_all_emails(text):
    email_pattern = re.compile(r"(\w+)@(\w+)((?:\.\w+)+)")
    email_matches = email_pattern.findall(text)
    for email_match in email_matches:
        print_email_details(email_match)


def print_email_details(email_match):
    print(20 * "-")
    print(f"Adres email:")
    print(f"Nazwa: {email_match[0]}")
    print(f"Domena: {email_match[1]}")
    print(f"Rozszerzenie domeny: {email_match[2]}")


if __name__ == "__main__":
    run_example()
