from collections import defaultdict


def load_movies_by_category() -> dict[str, list[str]]:
    movies: dict[str, list[str]] = defaultdict(list)
    with open("movies.txt") as movies_file:
        for line in movies_file:
            movie_data = line.split(" - ")
            movie_name = movie_data[0]
            category = movie_data[1]
            movies[category].append(movie_name)
    return movies


def run_example() -> None:
    movies_by_category = load_movies_by_category()
    for category, movies in movies_by_category.items():
        print(f"Category: {category}", end="")
        for movie in movies:
            print(f"---> {movie}")


if __name__ == "__main__":
    run_example()
