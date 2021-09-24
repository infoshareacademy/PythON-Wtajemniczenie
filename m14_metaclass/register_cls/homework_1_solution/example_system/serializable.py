import csv
import json
from typing import Any, cast, Type, TextIO

from example_system.serializable_registry import SerializableRegistry


class MetaSerializableRegistration(type):
    def __new__(mcs, name: str, bases: tuple[type], class_dict: dict[str, Any]) -> Any:
        cls = cast(Type[Serializable], super().__new__(mcs, name, bases, class_dict))
        SerializableRegistry.register(cls)
        return cls


class Serializable:
    def __init__(self, *args: Any) -> None:
        self.args = args

    def to_csv(self, output_file: TextIO) -> None:
        csv_writer = csv.writer(output_file)
        csv_writer.writerow((self.__class__.__name__, *self.args))


class RegisteredSerializable(Serializable, metaclass=MetaSerializableRegistration):
    pass
