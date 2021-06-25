import re
import time


def run_example():
    example_text = "To jest tekst, który ma adresy email: mikolaj@pyjazz.pl oraz JanPrzykładowy@pyjazz.pl"
    email_pattern_str = r"(\w+)@(\w+)((?:\.\w+)+)"

    start = time.perf_counter()
    email_pattern = re.compile(email_pattern_str)
    for _ in range(1_000_000):
        email_pattern.search(example_text)
        re.purge()
    end = time.perf_counter()
    print(end - start)

    start = time.perf_counter()
    for _ in range(1_000_000):
        re.search(email_pattern_str, example_text)
        # re.purge()
    end = time.perf_counter()
    print(end - start)


if __name__ == "__main__":
    run_example()
