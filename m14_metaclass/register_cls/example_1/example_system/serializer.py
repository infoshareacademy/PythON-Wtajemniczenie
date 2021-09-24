import json

from example_system.serializable import Serializable
from example_system.serializable_registry import SerializableRegistry


def serialize(obj: Serializable) -> str:
    return obj.to_json()


def deserialize(serialized_data: str) -> Serializable:
    deserialized_data = json.loads(serialized_data)
    class_name = deserialized_data["cls_name"]
    obj_cls = SerializableRegistry.registered_classes[class_name]
    return obj_cls(*deserialized_data["data"])
