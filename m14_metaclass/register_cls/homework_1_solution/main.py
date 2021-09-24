from example_system import serializer
from example_system.bike import Bike
from example_system.human import Human


def run_example() -> None:
    krzysztof = Human(name="Krzysztof", age=37)
    giant_bike = Bike(brand="Giant", model="Contend AR")

    serializer.serialize(krzysztof)
    serializer.serialize(giant_bike)

    deserialized_objects = serializer.deserialize()
    for obj in deserialized_objects:
        print(obj)

    print(krzysztof)
    print(giant_bike)


if __name__ == "__main__":
    run_example()
