from new_movies.exceptions import MovieAlreadySeen, InvalidRateValue


class Movie:

    AVAILABLE_CATEGORIES = ["Comedy", "Horror"]

    def __init__(self, name, category):
        self.name = name
        self._validate_category(category)
        self._category = category
        self._rates = []
        self.__viewers = []

    def __str__(self):
        return f"{self.name} - {self.category} Movie, rate: {self.rate}"

    @property
    def rate(self):
        return sum(self._rates) / len(self.__viewers)
        # if len(self.__viewers):
        #     return sum(self._rates) / len(self.__viewers)
        # return 0

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        self._validate_category(value)
        self._category = value

    def vote(self, viewer_name, rate):
        if viewer_name in self.__viewers:
            raise MovieAlreadySeen()
        if not 0 < rate < 6:
            raise InvalidRateValue()

        self.__viewers.append(viewer_name)
        self._rates.append(rate)

    @classmethod
    def _validate_category(cls, category):
        if category not in cls.AVAILABLE_CATEGORIES:
            raise ValueError(f"Category: '{category}' is not available")
