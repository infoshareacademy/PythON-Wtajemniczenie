from example_system.serializable import RegisteredSerializable


class Human(RegisteredSerializable):
    def __init__(self, name: str, age: int) -> None:
        super().__init__(name, age)
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f"Human: {self.name}"
