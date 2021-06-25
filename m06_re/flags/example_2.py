import re


def run_example():
    text = """Ala ma kota. 
Kot nazywa się Mruczek i jest bardzo wesołym zwierzakiem.
Mruczek ma 5 lat."""

    first_word_pattern = re.compile(r"^\w+")
    print(first_word_pattern.findall(text))

    first_word_each_line_pattern = re.compile(r"^\w+", flags=re.MULTILINE)
    print(first_word_each_line_pattern.findall(text))

    case_insensitive_multiline_pattern = re.compile(r"^kot", flags=re.I | re.M)
    print(case_insensitive_multiline_pattern.findall(text))


if __name__ == "__main__":
    run_example()
