
from collections import ChainMap


def run_example() -> None:
    basic_config = {"key_A": "BASIC_A_VALUE", "key_B": "BASIC_B_VALUE"}
    override_config = {"key_A": "NEW_A_VALUE", "key_C": "ADDITIONAL_C_VALUE"}

    config = ChainMap(override_config, basic_config)
    print(config["key_A"])
    print(config["key_B"])
    print(config["key_C"])


if __name__ == "__main__":
    run_example()
