from new_movies import movies_directory


def run_example() -> None:
    movies = movies_directory.load_available_movies()
    for movie in movies:
        print(movie)


if __name__ == "__main__":
    run_example()
