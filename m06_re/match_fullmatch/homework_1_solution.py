# Wykorzystując wcześniej napisane wyrażenie regularne dopasowujące adres email napisz program,
# który wczyta od użytkownika adres email a następnie wypisze jego poszczególne elementy:
#     1. Nazwę
#     2. Domenę
#     3. Rozszerzenie domeny
import re


def run_example():
    email_pattern = re.compile(r"(\w+)@(\w+)((?:\.\w+)+)")
    email = ask_for_email()
    email_match = email_pattern.fullmatch(email)
    print_email_details(email_match)


def ask_for_email():
    return input("Podaj swój adres email: ")


def print_email_details(email_match):
    if email_match is None:
        print("Ten adres email nie jest poprawny!")
        return

    print(f"Twój adres email to: {email_match.group()}. Składa się z:")
    print(f"Nazwy: {email_match.group(1)}")
    print(f"Domeny: {email_match.group(2)}")
    print(f"Rozszerzenia domeny: {email_match.group(3)}")


if __name__ == "__main__":
    run_example()
