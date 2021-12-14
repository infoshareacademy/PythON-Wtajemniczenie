from dataclasses import dataclass


@dataclass
class Book:
    author: str
    title: str
    is_available: bool = True

