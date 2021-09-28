class AccountContract:
    def __init__(self) -> None:
        self.content = ""

    def extend_content(self, content: str) -> None:
        self.content += content

    def render(self) -> str:
        return self.content
