from example_system.serializable import RegisteredSerializable


class Bike(RegisteredSerializable):
    def __init__(self, brand: str, model: str) -> None:
        super().__init__(brand, model)
        self.brand = brand
        self.model = model

    def __str__(self) -> str:
        return f"Bike: {self.brand} {self.model}"
