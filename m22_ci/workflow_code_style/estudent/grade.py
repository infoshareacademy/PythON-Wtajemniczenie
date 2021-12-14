class Grade:

    FAILING_GRADE = 1

    def __init__(self, value: int) -> None:
        self.value = value

    def is_passing(self) -> bool:
        return self.value > Grade.FAILING_GRADE

    def __repr__(self) -> str:
        return str(self.value)
