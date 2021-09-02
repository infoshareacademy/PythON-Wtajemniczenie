from collections import Counter


def run_example() -> None:
    fruits = Counter({"apple": 3, "banana": 2, "orange": 4})
    vegetables: Counter[str] = Counter(tomato=2, carrot=4)
    print(fruits)
    print(vegetables)

    print(20 * "-")
    for fruit, quantity in fruits.items():
        print(f"{fruit} -> {quantity}")

    print(20 * "-")
    for fruit in fruits.elements():
        print(fruit)
    print(20 * "-")

    print(fruits.most_common(1))
    print(fruits.most_common())

    print(20 * "-")
    fruits_order = Counter({"apple": 1, "banana": 1, "orange": 10})
    fruits.subtract(fruits_order)
    print(fruits)

    print(20 * "-")
    monday_supply = Counter({"plum": 10, "orange": 10})
    fruits.update(monday_supply)
    print(fruits)


if __name__ == "__main__":
    run_example()
