class ComplexForm:
    def __init__(self,) -> None:
        self.content = ""

    def extend_content(self, contend: str) -> None:
        self.content += contend

    def render(self) -> str:
        return self.content
