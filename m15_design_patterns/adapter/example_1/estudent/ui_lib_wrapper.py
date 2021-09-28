import json
from typing import Any

from estudent.school_ui_lib.ui_lib import UILib


class UILibWrapper:
    def __init__(self, window_header: str) -> None:
        self.ui_lib = UILib(window_header)

    def print_students_list(self, students_data_json: str) -> None:
        students_data = json.loads(students_data_json)["students"]
        camel_case_data = [
            self._map_snake_to_camel_case_dict(student_data) for student_data in students_data
        ]
        parsed_data = {"students": camel_case_data}
        return self.ui_lib.print_students_list(json.dumps(parsed_data))

    def _map_snake_to_camel_case_dict(self, json_data: dict[str, Any]) -> dict[str, Any]:
        return {self._map_snake_to_camel_case(key): value for key, value in json_data.items()}

    def _map_snake_to_camel_case(self, snake_case: str) -> str:
        snake_case_elements = snake_case.split("_")
        camel_cased_elements = [
            snake_case_element.title() for snake_case_element in snake_case_elements[1:]
        ]
        return snake_case_elements[0] + "".join(camel_cased_elements)
