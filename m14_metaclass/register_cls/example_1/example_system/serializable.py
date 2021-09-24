import json
from typing import Any


class Serializable:

    def __init__(self, *args: Any) -> None:
        self.args = args

    def to_json(self) -> str:
        return json.dumps({
            "cls_name": self.__class__.__name__,
            "data": self.args
        })
