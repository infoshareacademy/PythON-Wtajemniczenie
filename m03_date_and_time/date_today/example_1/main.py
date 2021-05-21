from book_book import books_directory, user_interface


def run_example():
    user_interface.add_new_book()
    print("Data dodania: ", books_directory.available_books[-1].added_at_date)
    user_interface.add_new_book()
    print("Data dodania: ", books_directory.available_books[-1].added_at_date)


if __name__ == "__main__":
    run_example()
