from datetime import datetime

from new_movies import cinema_schedule


def cinema_movies_schedule(user):
    date_and_time_format = user.datetime_preferences.value
    cinema_datetime_input = input(
        f"When would you like to visit the cinema? ({date_and_time_format.date_format}): "
    )
    cinema_date = datetime.strptime(cinema_datetime_input, date_and_time_format.date_format).date()
    weekly_schedule = cinema_schedule.schedule_for_week(
        cinema_date, cinema_schedule.weekly_schedule_template
    )
    print("During this week you can watch:")
    for schedule_for_day in weekly_schedule.values():
        for movie_showtime_info in schedule_for_day:
            _print_movie_showtime_info_formatted(
                movie_showtime_info, date_and_time_format, user.timezone
            )


def _print_movie_showtime_info_formatted(movie_showtime_info, date_and_time_format, user_timezone):
    showtime_in_user_timezone = movie_showtime_info.showdatetime.astimezone(user_timezone)
    showtime_formatted = showtime_in_user_timezone.strftime(date_and_time_format.datetime_format)
    movie_info_formatted = movie_showtime_info.movie.info_with_date_format(date_and_time_format)
    print(f"{showtime_formatted} {movie_info_formatted}")
