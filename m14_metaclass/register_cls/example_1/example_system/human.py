from example_system.serializable import Serializable
from example_system.serializable_registry import SerializableRegistry


class Human(Serializable):
    def __init__(self, name: str, age: int) -> None:
        super().__init__(name, age)
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f"Human: {self.name}"


SerializableRegistry.register(Human)
