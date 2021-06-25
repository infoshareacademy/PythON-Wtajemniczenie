import re


def run_example():
    text = "Ala ma kota. Kot nazywa się Mruczek i jest bardzo wesołym zwierzakiem."

    case_sensitive_pattern = re.compile(r"kot")
    print(case_sensitive_pattern.findall(text))

    case_insensitive_pattern = re.compile(r"kot", flags=re.I)
    # case_insensitive_pattern = re.compile(r"kot", flags=re.IGNORECASE)
    print(case_insensitive_pattern.findall(text))


if __name__ == "__main__":
    run_example()
