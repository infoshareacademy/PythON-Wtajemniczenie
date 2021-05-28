from new_movies.cinema_schedule import (
    generate_february_week_schedule,
    weekly_schedule,
    Weekday,
    sort_weekly_schedule,
)


def run_example():
    sorted_weekly_schedule = sort_weekly_schedule(weekly_schedule)
    february_week_schedule = generate_february_week_schedule(sorted_weekly_schedule)
    print("During last week of February you can watch:")
    for week_day in Weekday:
        print(f"On {week_day.name}:")
        for movie_showdatetime in february_week_schedule[week_day]:
            print(movie_showdatetime.showdatetime, movie_showdatetime.movie)


if __name__ == "__main__":
    run_example()
