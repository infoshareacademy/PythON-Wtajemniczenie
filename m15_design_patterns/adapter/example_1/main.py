from estudent.students_directory import get_students_data
from estudent.ui_lib_wrapper import UILibWrapper


def run_example() -> None:
    students_data = get_students_data()
    ui_lib = UILibWrapper(window_header="Lista uczniów")
    ui_lib.print_students_list(students_data)


if __name__ == "__main__":
    run_example()
