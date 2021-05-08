def words_connector(connect_char):
    def connect(text):
        return text.replace(" ", connect_char)
    return connect


def run_example():
    hyphen_connector = words_connector("-")
    plus_connector = words_connector("+")
    pipe_connector = words_connector("|")

    text = "Today the weather is really beautiful"
    print(text)
    print(hyphen_connector(text))
    print(plus_connector(text))
    print(pipe_connector(text))


if __name__ == '__main__':
    run_example()
