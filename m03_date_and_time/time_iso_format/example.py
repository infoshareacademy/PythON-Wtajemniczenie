from datetime import datetime, time


def run_example():
    current_time = datetime.now().time()
    print(current_time)
    print(current_time.isoformat())
    your_time_input = input("Podaj czas w formacie HH:MM:SS: ")
    your_time = time.fromisoformat(your_time_input)
    print(f"Godziny: {your_time.hour}, Minuty: {your_time.minute}, Sekundy: {your_time.second}")

    # your_time_input = input("Podaj czas w formacie HH:MM: ")
    # your_time = time.fromisoformat(your_time_input)
    # print(f"Godziny: {your_time.hour}, Minuty: {your_time.minute}, Sekundy: {your_time.second}")


if __name__ == "__main__":
    run_example()
