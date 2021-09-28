import json
from typing import Any

from new_movie.movies_ui_lib.ui_lib import UILib


class UILibWrapper:
    def __init__(self, window_header: str) -> None:
        self.ui_lib = UILib(window_header)

    def print_movies_list(self, movies_data_json: str) -> None:
        movies_data = json.loads(movies_data_json)["movies"]
        adjusted_movies_data = [self._map_keys(movie_data) for movie_data in movies_data]
        parsed_data = {"movies": adjusted_movies_data}
        return self.ui_lib.print_movies_list(json.dumps(parsed_data))

    def _map_keys(self, movie_data: dict[str, Any]) -> dict[str, Any]:
        return {
            "name": movie_data["movie_name"],
            "cat": movie_data["movie_category"],
        }
