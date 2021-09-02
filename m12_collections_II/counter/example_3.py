from collections import Counter


def run_example() -> None:
    my_fruits_store = Counter({"apple": 5, "banana": 2, "orange": 4})
    your_fruits_store = Counter({"apple": 3, "plum": 10, "pineapple": 3})
    print(my_fruits_store)
    print(your_fruits_store)
    print(20 * "-")

    print(my_fruits_store + your_fruits_store)
    print(20 * "-")
    print(my_fruits_store - your_fruits_store)
    print(20 * "-")
    # min(my_fruits_store[...], your_fruits_store[...])
    print(my_fruits_store & your_fruits_store)
    print(20 * "-")
    # max(my_fruits_store[...], your_fruits_store[...])
    print(my_fruits_store | your_fruits_store)
    print(20 * "-")

    my_fruits_store.subtract({"apple": 10})
    print(my_fruits_store)
    print(+my_fruits_store)
    print(-my_fruits_store)
    print(20 * "-")


if __name__ == "__main__":
    run_example()
