from datetime import datetime

from new_movies import cinema_schedule
from new_movies.cinema_schedule import Weekday


def cinema_movies_schedule(user):
    date_and_time_format = user.datetime_preferences.value
    cinema_datetime_input = input(
        f"When would you like to visit the cinema? ({date_and_time_format.datetime_format}): "
    )
    cinema_datetime = datetime.strptime(cinema_datetime_input, date_and_time_format.datetime_format)
    cinema_time = cinema_datetime.time()
    weekday_number = cinema_datetime.isoweekday()
    weekday = Weekday(weekday_number)
    movies_at_weekday = cinema_schedule.get_movies_showtime_by_weekday(weekday)
    print("This day you can watch:")
    for movie_showtime in movies_at_weekday:
        if cinema_time <= movie_showtime.showtime:
            showtime_formatted = movie_showtime.showtime.strftime(date_and_time_format.time_format)
            movie_info_formatted = movie_showtime.movie.info_with_date_format(date_and_time_format)
            print(f"{showtime_formatted} {movie_info_formatted}")
