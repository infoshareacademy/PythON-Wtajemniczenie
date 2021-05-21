from new_movies import movies_directory, actions


def run_example():
    print(movies_directory.available_movies[0].added_at_date)
    actions.add_movie()
    print(movies_directory.available_movies[-1].added_at_date)


if __name__ == "__main__":
    run_example()
