from new_movies.comedy import Comedy
from new_movies.movie import Movie
from new_movies.ranking_generator import RankingGenerator


def run_movie_example():
    funny_movie = Movie("Funny Movie", "Comedy")
    funny_movie.vote("Mikołaj", rate=5)
    funny_movie.vote("Alicja", rate=4)
    print(funny_movie)

    print(funny_movie._rates)
    # print(funny_movie.__viewers)
    # print(funny_movie._Movie__viewers)


def run_ranking_example():
    funny_movie = Movie("Funny Movie", "Comedy")
    funny_movie.vote("Mikołaj", rate=5)
    funny_movie.vote("Alicja", rate=4)

    scary_movie = Movie("Scary House", "Horror")
    scary_movie.vote("Mikołaj", rate=3)
    scary_movie.vote("Alicja", rate=4)

    RankingGenerator.generate_ranking([funny_movie, scary_movie])


def run_comedy_example():
    # funny_movie = Movie("Funny Movie", "Comedy")
    funny_movie = Comedy("Funny Movie")
    funny_movie.vote("Mikołaj", rate=5)
    funny_movie.vote("Alicja", rate=4)

    # funny_movie.category = "Horror"

    print(funny_movie)


if __name__ == "__main__":
    run_movie_example()
    # run_ranking_example()
    # run_comedy_example()
