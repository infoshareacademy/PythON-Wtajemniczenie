from collections import deque


def run_example() -> None:
    sports: deque[str] = deque()
    sports.append("Kolarstwo")
    sports.append("Bieganie")

    print(sports)

    sports.appendleft("Pływanie")
    print(sports)

    sports.extendleft(["Triathlon", "Żeglarstwo"])
    print(sports)

    print(sports.popleft())
    print(sports)

    sports.rotate(3)
    print(sports)


if __name__ == '__main__':
    run_example()