class Message:
    def __init__(self, from_address: str, to_address: str, content: str) -> None:
        self.from_address = from_address
        self.to_address = to_address
        self.content = content
