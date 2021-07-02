from __future__ import annotations


class Student:
    def __init__(self, first_name: str, last_name: str) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.promoted = False

    def __str__(self) -> str:
        return f"Student: {self.first_name} {self.last_name}, promowany: {self.promoted}"

    def promote(self) -> None:
        self.promoted = True
