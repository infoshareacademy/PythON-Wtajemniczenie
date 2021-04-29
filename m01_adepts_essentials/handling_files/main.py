import csv


def run_example():
    with open("movies-data.csv", newline="") as movies_file:
        for line in movies_file:
            print(line, end="")


def run_csv_example():
    with open("movies-data.csv", newline="") as movies_file:
        csv_reader = csv.DictReader(movies_file)
        print(f"Headers: {csv_reader.fieldnames}")
        for row in csv_reader:
            print(row["Name"], row["Category"], row["Rate"])


def run_write_example():
    with open("hello-file.txt", newline="", mode="w") as hello_file:
        hello_file.write("Hello!")


if __name__ == "__main__":
    run_example()
    # run_csv_example()
    # run_write_example()
