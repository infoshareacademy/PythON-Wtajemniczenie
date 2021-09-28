from dataclasses import dataclass


@dataclass
class Product:
    name: str

    def __str__(self) -> str:
        return self.name
