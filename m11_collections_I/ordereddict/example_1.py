from collections import OrderedDict


def run_example() -> None:
    elements: OrderedDict[str, int] = OrderedDict({"apple": 3, "banana": 5, "orange": 1})

    for element, quantity in elements.items():
        print(element)
    print(20 * "-")

    for element, quantity in reversed(elements.items()):
        print(element)
    print(20 * "-")

    elements.move_to_end("apple")

    for element, quantity in elements.items():
        print(element)
    print(20 * "-")

    print(elements.popitem(last=False))


if __name__ == "__main__":
    run_example()
