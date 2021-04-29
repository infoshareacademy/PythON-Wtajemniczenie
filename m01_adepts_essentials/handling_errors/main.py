from new_movies.exceptions import InvalidRateValue
from new_movies.movie import Movie


def run_zero_divide_example():
    funny_movie = Movie("Funny Movie", "Comedy")
    print(funny_movie.rate)


def run_custom_error_example():
    funny_movie = Movie("Funny Movie", "Comedy")
    funny_movie.vote(viewer_name="Mikołaj", rate=10)


def run_error_handling_example():
    funny_movie = Movie("Funny Movie", "Comedy")
    viewer_name = input("What is your name? ")

    while True:
        rate = int(input("Rate the movie (1-5): "))
        try:
            funny_movie.vote(viewer_name, rate)
        except InvalidRateValue as error:
            print(error)
            print("Try again...")
        else:
            print("Your vote has been saved")
            break
        finally:
            print("It's great that you are voting!")


if __name__ == "__main__":
    # run_zero_divide_example()
    # run_custom_error_example()
    run_error_handling_example()
dict().update()