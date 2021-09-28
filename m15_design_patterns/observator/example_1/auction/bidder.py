from auction import email_service


class Bidder:
    def __init__(self, name: str, email: str) -> None:
        self.name = name
        self.email = email

    def new_bid_notify(self, bidder_name: str, amount: int) -> None:
        if bidder_name != self.name:
            email_service.send_email(self.email, f"{bidder_name} just proposed a better bid: {amount}")
