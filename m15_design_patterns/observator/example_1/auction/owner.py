from auction import email_service


class Owner:
    def __init__(self, email: str) -> None:
        self.email = email

    def new_bid_notify(self, bidder_name: str, amount: int) -> None:
        email_service.send_email(self.email, f"New bid from {bidder_name} in your auction ({amount})")