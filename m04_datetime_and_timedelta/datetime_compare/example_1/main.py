from book_book import user_interface


def run_example():
    user = user_interface.login()
    user_interface.select_datetime_preferences(user)
    user_interface.find_books_by_added_at_datetime(user)


if __name__ == "__main__":
    run_example()
