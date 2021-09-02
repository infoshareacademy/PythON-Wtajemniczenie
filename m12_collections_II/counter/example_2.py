from collections import Counter


def run_example() -> None:
    fruits = Counter({"apple": 3, "banana": 2, "orange": 4})
    print(fruits["plum"])
    fruits["plum"] += 1
    print(fruits)
    print(20 * "-")

    fruits["apple"] = 0
    for fruit, quantity in fruits.items():
        print(f"{fruit} -> {quantity}")
    print(20 * "-")

    del fruits["apple"]
    for fruit, quantity in fruits.items():
        print(f"{fruit} -> {quantity}")


if __name__ == "__main__":
    run_example()
