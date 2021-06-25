import re


def run_example():
    file_names = """
rozliczenie.txt
wyniki.txt
wakacje.jpg
pulpit.png
notatka.txt
    """
    text_file_pattern = re.compile(r".*.txt")
    print(text_file_pattern.finditer(file_names))
    for match in text_file_pattern.finditer(file_names):
        print(match.group())

    text_with_numbers = "N1: +48 123 456 789, N2: +123 (98)7 654 321, N3: 987 654 321, N4: 987654321"
    number_pattern = re.compile(r"(?:\+(\d{2,3})[-\s])?\(?(\d{2})\)?(\d[-\s]\d{3}[-\s]\d{3})")
    print(number_pattern.finditer(text_with_numbers))

    for match in number_pattern.finditer(text_with_numbers):
        print(match.group())
        print(20 * "-")
        for group in match.groups():
            print(group)


if __name__ == "__main__":
    run_example()
