class Student:
    def __init__(self, name, marks):
        if not isinstance(marks, dict):
            raise ValueError("Marks must be a dictionary")
        self.name = name
        self.marks = marks

    def total_marks(self):
        return sum(self.marks.values())

    def average_marks(self):
        return self.total_marks() / len(self.marks)

    def grade(self):
        avg = self.average_marks()
        if avg >= 90:
            return "A+"
        elif avg >= 70:
            return "A"
        elif avg >= 60:
            return "B"
        elif avg >= 50:
            return "C"
        else:
            return "F"


# --- Manual test runner (without pytest) ---
def run_tests():
    try:
        s = Student("John", {"Math": 80, "Science": 70, "English": 90})
        assert s.total_marks() == 240
        print("test_student.py::test_total_marks PASSED")

        assert s.average_marks() == 80.0
        print("test_student.py::test_average_marks PASSED")

        s = Student("Alice", {"Math": 95, "Science": 92, "English": 90})
        assert s.grade() == "A+"
        print("test_student.py::test_grade_Aplus PASSED")

        s = Student("Bob", {"Math": 80, "Science": 75, "English": 70})
        assert s.grade() == "A"
        print("test_student.py::test_grade_A PASSED")

        s = Student("Charlie", {"Math": 65, "Science": 60, "English": 55})
        assert s.grade() == "B"
        print("test_student.py::test_grade_B PASSED")

        s = Student("David", {"Math": 55, "Science": 50, "English": 45})
        assert s.grade() == "C"
        print("test_student.py::test_grade_C PASSED")

        s = Student("Eve", {"Math": 40, "Science": 35, "English": 30})
        assert s.grade() == "F"
        print("test_student.py::test_grade_F PASSED")

        try:
            Student("Invalid", None)
        except ValueError:
            print("test_student.py::test_invalid_marks PASSED")

    except AssertionError as e:
        print("FAILED:", e)


if __name__ == "__main__":
    run_tests()
