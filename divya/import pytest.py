import pytest
from student_management import Student

def test_total_marks():
    s = Student("John", {"Math": 80, "Science": 70, "English": 90})
    assert s.total_marks() == 240

def test_average_marks():
    s = Student("John", {"Math": 80, "Science": 70, "English": 90})
    assert s.average_marks() == pytest.approx(80.0)

def test_grade_Aplus():
    s = Student("Alice", {"Math": 95, "Science": 92, "English": 90})
    assert s.grade() == "A+"

def test_grade_A():
    s = Student("Bob", {"Math": 80, "Science": 75, "English": 70})
    assert s.grade() == "A"

def test_grade_B():
    s = Student("Charlie", {"Math": 65, "Science": 60, "English": 55})
    assert s.grade() == "B"

def test_grade_C():
    s = Student("David", {"Math": 55, "Science": 50, "English": 45})
    assert s.grade() == "C"

def test_grade_F():
    s = Student("Eve", {"Math": 40, "Science": 35, "English": 30})
    assert s.grade() == "F"

def test_invalid_marks():
    with pytest.raises(ValueError):
        Student("Invalid", None)
