from dataclasses import dataclass


@dataclass
class RentalRequest:
    author: str
    title: str
    renter_name: str
