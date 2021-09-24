import json
from typing import Any, cast, Type

from example_system.serializable_registry import SerializableRegistry


class MetaSerializableRegistration(type):
    def __new__(mcs, name: str, bases: tuple[type], class_dict: dict[str, Any]) -> Any:
        cls = cast(Type[Serializable], super().__new__(mcs, name, bases, class_dict))
        SerializableRegistry.register(cls)
        return cls


class Serializable:
    def __init__(self, *args: Any) -> None:
        self.args = args

    def to_json(self) -> str:
        return json.dumps({"cls_name": self.__class__.__name__, "data": self.args})


class RegisteredSerializable(Serializable, metaclass=MetaSerializableRegistration):
    pass
