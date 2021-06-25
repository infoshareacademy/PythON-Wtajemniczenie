import re


def run_example():
    text = "N1: +48 123 456 789, N2: +123 (98)7 654 321, N3: 987 654 321, N4: 987654321"
    verbose_pattern = re.compile(r"""(?:\+(\d{2,3})[-\s])?      # Numer kierunkowy do kraju
                                     \(?(\d{2})\)?              # Numer kierunkowy do miasta 
                                     (\d[-\s]\d{3}[-\s]\d{3})   # Pozostała część numeru """, flags=re.VERBOSE)

    print(verbose_pattern.findall(text))


if __name__ == "__main__":
    run_example()
