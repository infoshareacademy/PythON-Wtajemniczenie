from book_book import user_interface


def run_example():
    user = user_interface.login()
    user_interface.select_datetime_preferences(user)
    user_interface.add_new_book(user)
    user_interface.print_available_books(user)


if __name__ == "__main__":
    run_example()
