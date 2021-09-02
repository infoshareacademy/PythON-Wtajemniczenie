from new_movies.exceptions import MovieAlreadySeen, InvalidRateValue


class Movie:

    MIN_ALLOWED_RATE = 1
    MAX_ALLOWED_RATE = 5

    def __init__(self, name: str, category: str) -> None:
        self.name = name
        self.category = category
        self._rates: list[int] = []
        self._viewers: list[str] = []

    def __str__(self) -> str:
        return f"{self.name} - {self.category} Movie, rate: {self.rate:.2f}"

    @property
    def rate(self) -> float:
        if len(self._viewers):
            return sum(self._rates) / len(self._viewers)
        return 0

    def vote(self, viewer_name: str, rate: int) -> None:
        if viewer_name in self._viewers:
            raise MovieAlreadySeen()
        if not self.MIN_ALLOWED_RATE <= rate <= self.MAX_ALLOWED_RATE:
            raise InvalidRateValue()

        self._viewers.append(viewer_name)
        self._rates.append(rate)
