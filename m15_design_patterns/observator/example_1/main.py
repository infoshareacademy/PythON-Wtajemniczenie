import time

from auction.auction import Auction
from auction.bidder import Bidder
from auction.owner import Owner
from auction.product import Product


def run_example() -> None:
    old_painting = Product(name="Old Painting")
    painting_owner = Owner(email="paiting.owner@pyjazz.pl")

    ala_bidder = Bidder(name="Ala", email="ala@pyjazz.pl")
    olaf_bidder = Bidder(name="Olaf", email="olaf@pyjazz.pl")

    # Rozpoczynamy aukcje
    auction = Auction(product=old_painting, min_bid=100)
    auction.subscribe_for_bid_updates(painting_owner)
    time.sleep(2)

    # Dołącza licytująca - po przekazaniu pierwszej oferty zapisuje się na informacje o nowych ofertach
    auction.new_bid(ala_bidder, amount=120)
    auction.subscribe_for_bid_updates(ala_bidder)
    time.sleep(2)

    # Dołącza licytujący - po przekazaniu pierwszej oferty zapisuje się na informacje o nowych ofertach
    auction.new_bid(olaf_bidder, amount=150)
    auction.subscribe_for_bid_updates(olaf_bidder)
    time.sleep(2)

    # Licytacja trwa
    auction.new_bid(ala_bidder, amount=200)
    time.sleep(2)
    auction.new_bid(olaf_bidder, amount=220)
    time.sleep(2)
    auction.new_bid(ala_bidder, amount=350)
    time.sleep(2)

    auction.finish()


if __name__ == "__main__":
    run_example()
