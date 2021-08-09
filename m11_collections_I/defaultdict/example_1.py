from collections import defaultdict


def standard_dict_example() -> None:
    food_resource = ["apple", "orange", "apple", "tomato", "tomato", "apple", "carrot"]
    food_quantity: dict[str, int] = {}
    for food in food_resource:
        if food not in food_quantity:
            food_quantity[food] = 0
        food_quantity[food] += 1

    print(food_quantity)
    # print(food_quantity["avocado"])


def default_dict_example() -> None:
    food_resource = ["apple", "orange", "apple", "tomato", "tomato", "apple", "carrot"]
    food_quantity: dict[str, int] = defaultdict(lambda: 0)
    for food in food_resource:
        food_quantity[food] += 1

    print(food_quantity)
    print(food_quantity["avocado"])


def run_example() -> None:
    standard_dict_example()
    default_dict_example()


if __name__ == "__main__":
    run_example()
