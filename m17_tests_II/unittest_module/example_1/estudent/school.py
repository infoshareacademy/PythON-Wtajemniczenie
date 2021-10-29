from estudent.student import Student


class School:
    MAX_STUDENTS_NUMBER = 20

    def __init__(self, name: str, students: list[Student]) -> None:
        self.name = name
        self.students = students
        self._promote_lucky_students()

    def _promote_lucky_students(self) -> None:
        for index, student in enumerate(self.students):
            if index % 3 == 0:
                student.promote()

    def __str__(self) -> str:
        students = ""
        for student in self.students:
            students += "\n"
            students += str(student)

        return f"Szkoła: {self.name}, z {len(self.students)} uczniami: {students}"

    def assign_student(self, student: Student) -> None:
        if len(self.students) < School.MAX_STUDENTS_NUMBER:
            self.students.append(student)
        else:
            raise ValueError("Nie ma już miejsca!")

