from __future__ import annotations

from typing import Any


class Tasks:

    def __init__(self) -> None:
        self.major_tasks: list[str] = []
        self.minor_tasks: list[str] = []

    def add_major_task(self, task: str) -> None:
        self.major_tasks.append(task)

    def add_minor_task(self, task: str) -> None:
        self.minor_tasks.append(task)

    def major_tasks_for_today(self) -> Any:
        ...

    def __iter__(self) -> TasksIterator:
        return TasksIterator(self.major_tasks, self.minor_tasks)


class TasksIterator:

    def __init__(self, major_tasks: list[str], minor_tasks: list[str]) -> None:
        self.major_tasks = major_tasks
        self.minor_tasks = minor_tasks
        self.major_tasks_index = 0
        self.minor_tasks_index = 0

    def __iter__(self) -> TasksIterator:
        return self

    def __next__(self) -> str:
        while self.major_tasks_index < len(self.major_tasks):
            element_to_return = self.major_tasks[self.major_tasks_index]
            self.major_tasks_index += 1
            return element_to_return

        while self.minor_tasks_index < len(self.minor_tasks):
            element_to_return = self.minor_tasks[self.minor_tasks_index]
            self.minor_tasks_index += 1
            return element_to_return

        raise StopIteration()


def run_example() -> None:
    home_tasks = Tasks()
    home_tasks.add_major_task("Ugotować obiad")
    home_tasks.add_major_task("Zrobić zakupy")
    home_tasks.add_minor_task("Wytrzeć kurze")

    office_tasks = Tasks()
    office_tasks.add_major_task("Spotkanie z klientem")
    office_tasks.add_major_task("Kickoff projektu")
    office_tasks.add_minor_task("Notatka ze spotkania")
    office_tasks.add_minor_task("Uporządkowanie plików")

    for task in home_tasks:
        print(task)

    for task in office_tasks:
        print(task)


if __name__ == '__main__':
    run_example()