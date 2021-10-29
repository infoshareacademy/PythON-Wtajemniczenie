from dataclasses import dataclass


@dataclass
class Vehicle:
    name: str
    model: str
    max_speed: int
