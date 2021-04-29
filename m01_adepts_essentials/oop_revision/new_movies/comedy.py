from new_movies.movie import Movie


class Comedy(Movie):

    AVAILABLE_CATEGORIES = ["Komedia"]

    def __init__(self, name):
        super().__init__(name, category="Komedia")
