from book_book import user_interface


def run_example():
    user_interface.print_available_books()
    user_interface.add_new_book()
    user_interface.print_available_books()


if __name__ == "__main__":
    run_example()
