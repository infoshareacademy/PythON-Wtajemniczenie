from galactic import swapi_client


def run_example() -> None:
    for _ in range(20):
        luke = swapi_client.get_person_data(person_id=1)
        print(luke["name"])

    for _ in range(20):
        c_3po = swapi_client.get_person_data(person_id=2)
        print(c_3po["name"])

    # for _ in range(20):
    #     luke = swapi_client.get_person_data(person_id=1)
    #     print(luke["name"])
    #     c_3po = swapi_client.get_person_data(person_id=2)
    #     print(c_3po["name"])


if __name__ == "__main__":
    run_example()
