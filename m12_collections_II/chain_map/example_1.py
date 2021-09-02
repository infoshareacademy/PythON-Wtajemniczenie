
from collections import ChainMap


def run_example() -> None:
    class_a_grades = {"Jan": 4, "Aleksandra": 5, "Mikołaj": 3, "Joanna": 4}
    class_b_grades = {"Jacek": 4, "Witold": 5, "Anna": 3, "Bożena": 4}
    students_results = ChainMap(class_a_grades, class_b_grades)
    for student, grade in students_results.items():
        print(f"{student} ---> {grade}")

    print(20 * "-")
    class_b_grades["Jacek"] = 5
    for student, grade in students_results.items():
        print(f"{student} ---> {grade}")

    print(students_results["Mikołaj"])


if __name__ == "__main__":
    run_example()
