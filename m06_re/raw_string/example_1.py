import re


def run_example():
    text = "\\napis \\słowo"
    print(text)

    pattern = re.compile("\\n\w")
    pattern_2 = re.compile("\\\\n\w")
    pattern_3 = re.compile(r"\\n\w")

    print(pattern.findall(text))
    print(pattern_2.findall(text)[0])
    print(pattern_3.findall(text)[0])


if __name__ == "__main__":
    run_example()
