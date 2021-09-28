import json


class UILib:

    def __init__(self, window_header: str) -> None:
        self.window_header = window_header

    def print_students_list(self, students_data_json: str) -> None:
        print(f"{10 * '-'}{self.window_header}{10*'-'}")

        students_data = json.loads(students_data_json)["students"]

        for index, student_data in enumerate(students_data):
            index_str = str(index + 1)
            if index + 1 < 10:
                index_str = "0" + index_str

            print(f"{index_str}. {student_data['firstName']} {student_data['lastName']}")
