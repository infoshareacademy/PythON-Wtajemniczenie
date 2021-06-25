import re
import time


def run_example():
    example_text = "To jest tekst, który ma adresy email: mikolaj@pyjazz.pl oraz JanPrzykładowy@pyjazz.pl"
    email_pattern_str = r"mikolaj@pyjazz.pl"
    email_pattern_str_complex = r"(\w+)@(\w+)((?:\.\w+)+)"

    start = time.perf_counter()
    email_pattern = re.compile(email_pattern_str)
    # email_pattern = re.compile(email_pattern_str_complex)
    for _ in range(10_000_000):
        email_pattern.search(example_text)
    end = time.perf_counter()
    print(end - start)

    start = time.perf_counter()
    for _ in range(10_000_000):
        example_text.find(email_pattern_str)
    end = time.perf_counter()
    print(end - start)


if __name__ == "__main__":
    run_example()
