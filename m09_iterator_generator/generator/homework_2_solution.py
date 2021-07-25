from collections.abc import Generator


def file_reader(path_to_file: str) -> Generator[str, None, None]:
    with open(path_to_file) as data_file:
        next_line = data_file.readline()
        while next_line:
            yield next_line
            next_line = data_file.readline()


def process_text_line(line: str) -> None:
    print("---")
    print(line, end="")


def run_example() -> None:
    for line in file_reader("homework_2_file.txt"):
        process_text_line(line)


if __name__ == "__main__":
    run_example()
