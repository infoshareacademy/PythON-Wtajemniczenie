from typing import Optional, Protocol

from auction.bidder import Bidder
from auction.product import Product


class AuctionObserver(Protocol):
    def new_bid_notify(self, bidder_name: str, amount: int) -> None:
        ...


class Auction:
    def __init__(self, product: Product, min_bid: int):
        self.product = product
        self.highest_bid = min_bid
        self.current_winner: Optional[Bidder] = None
        self.subscribers: list[AuctionObserver] = []
        print(f"{product} auction is open!")

    def new_bid(self, bidder: Bidder, amount: int) -> None:
        if self.highest_bid >= amount:
            raise ValueError(f"New bid must be higher then {self.highest_bid}")

        self.current_winner = bidder
        for subscriber in self.subscribers:
            subscriber.new_bid_notify(bidder.name, amount)

    def finish(self) -> None:
        if self.current_winner:
            print(f"Auction closed, the winner is {self.current_winner.name}")
        else:
            print("Auction closed, no winner")

    def subscribe_for_bid_updates(self, observer: AuctionObserver) -> None:
        self.subscribers.append(observer)

    def unsubscribe_from_bid_updates(self, observer: AuctionObserver) -> None:
        self.subscribers.remove(observer)
