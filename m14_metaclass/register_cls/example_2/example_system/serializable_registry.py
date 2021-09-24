from __future__ import annotations
from typing import ClassVar, Type, TYPE_CHECKING


if TYPE_CHECKING:
    from example_system.serializable import Serializable


class SerializableRegistry:
    registered_classes: ClassVar[dict[str, Type[Serializable]]] = {}

    @classmethod
    def register(cls, cls_type: Type[Serializable]) -> None:
        cls.registered_classes[cls_type.__name__] = cls_type
