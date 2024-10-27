class Student:
    def __init__(self, namee, grades: list):
        self.namee = namee
        self.grades = grades

    def average_grade(self):
        return sum(self.grades) / len(self.grades)

    def verify_grades(self, grades):
        if not isinstance(grades, list):
            raise ValueError("grades must be list")
        if not all(isinstance(grade, int) and 0 <= grade <= 100 for grade in grades):
            raise ValueError("grade must be between 0 and 100")

    def __eq__(self, other):
        self.verify_grades(other.grades)
        return self.average_grade() == other.average_grade()

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        self.verify_grades(other.grades)
        return self.average_grade() < other.average_grade()

    def __gt__(self, other):
        return not self.__lt__(other)


student1 = Student("Alice", [90, 80, 89])
student2 = Student("Bob", [85, 75, 95])

print(student1 == student2)  # False
print(student1 > student2)  # True
print(student1 < student2)  # False
