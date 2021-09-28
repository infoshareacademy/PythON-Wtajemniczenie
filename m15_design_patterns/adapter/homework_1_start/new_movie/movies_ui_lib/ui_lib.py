import json


class UILib:

    def __init__(self, window_header: str) -> None:
        self.window_header = window_header

    def print_movies_list(self, movies_data_json: str) -> None:
        print(f"{10 * '-'}{self.window_header}{10*'-'}")

        movies_data = json.loads(movies_data_json)["movies"]

        for index, movie_data in enumerate(movies_data):
            index_str = str(index + 1)
            if index + 1 < 10:
                index_str = "0" + index_str

            print(f"{index_str}. {movie_data['name']} <{movie_data['cat']}>")
