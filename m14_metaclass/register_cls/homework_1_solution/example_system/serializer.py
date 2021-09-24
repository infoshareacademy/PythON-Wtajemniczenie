import csv
import json

from example_system.serializable import Serializable
from example_system.serializable_registry import SerializableRegistry

PATH_TO_FILE = "serialized_objects.csv"


def serialize(obj: Serializable) -> None:
    with open(PATH_TO_FILE, mode="a") as csv_file:
        obj.to_csv(csv_file)


def deserialize() -> list[Serializable]:
    deserialized_objects = []
    with open(PATH_TO_FILE, mode="r") as csv_file:
        csv_reader = csv.reader(csv_file)
        for deserialized_data in csv_reader:
            class_name = deserialized_data[0]
            obj_cls = SerializableRegistry.registered_classes[class_name]
            obj_data = deserialized_data[1:]
            deserialized_objects.append(obj_cls(*obj_data))
    return deserialized_objects
