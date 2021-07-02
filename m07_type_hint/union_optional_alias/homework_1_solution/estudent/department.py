from estudent.student import Student


class Department:

    def __init__(self, letter_identifier: str, year: int) -> None:
        self.letter_identifier = letter_identifier
        self.year = year
        self.students: list[Student] = []

    def assign_student(self, student: Student) -> bool:
        self.students.append(student)
        return True

    def __str__(self) -> str:
        return f"Klasa {self.year}{self.letter_identifier}, {len(self.students)} uczniów"


class SizeLimitedDepartment(Department):

    MAX_STUDENTS = 15

    def assign_student(self, student: Student) -> bool:
        if len(self.students) < SizeLimitedDepartment.MAX_STUDENTS:
            self.students.append(student)
            return True
        else:
            print("Nie ma już miejsca")
            return False
