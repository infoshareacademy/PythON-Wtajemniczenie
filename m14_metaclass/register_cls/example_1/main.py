from example_system import serializer
from example_system.bike import Bike
from example_system.human import Human


def run_example() -> None:
    krzysztof = Human(name="Krzysztof", age=37)
    giant_bike = Bike(brand="Giant", model="Contend AR")

    krzysztof_json = serializer.serialize(krzysztof)
    print(krzysztof_json)
    bike_json = serializer.serialize(giant_bike)
    print(bike_json)

    krzysztof_deserialized = serializer.deserialize(krzysztof_json)
    print(krzysztof)
    print(krzysztof_deserialized)
    bike_deserialized = serializer.deserialize(bike_json)
    print(giant_bike)
    print(bike_deserialized)


if __name__ == "__main__":
    run_example()
