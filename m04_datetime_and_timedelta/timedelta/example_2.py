from datetime import date, timedelta


def run_example():
    ala_birth_date = date(year=1990, month=3, day=5)
    bob_birth_date = date(year=1990, month=4, day=2)

    bob_ala_interval = bob_birth_date - ala_birth_date
    ala_bob_interval = ala_birth_date - bob_birth_date
    print("bob_ala_interval", bob_ala_interval)
    print("ala_bob_interval", ala_bob_interval)

    print(ala_birth_date + bob_ala_interval == bob_birth_date)
    print(bob_ala_interval, (bob_ala_interval * 5))
    print(ala_birth_date + bob_ala_interval * 5 > bob_birth_date)
    print(bob_ala_interval > timedelta(seconds=10))


if __name__ == "__main__":
    run_example()
