class EmployeeController:
    def __init__(self, **kwargs):
        self.kwargs = kwargs  # Параметры для валидации

    def verify_name(self, employee_name):
        min_length = self.kwargs.get("min_length", 0)
        max_length = self.kwargs.get("max_length", 100)
        if not isinstance(employee_name, str):
            raise ValueError("Имя должно быть строкой")
        if not (min_length <= len(employee_name) <= max_length):
            raise ValueError(f"Имя должно быть между {min_length} и {max_length} символами")

    def verify_years_of_experience(self, years):
        min_year = self.kwargs.get("min_year", 0)
        max_year = self.kwargs.get("max_year", 100)
        if not isinstance(years, int) or years < 0:
            raise ValueError("Стаж должен быть положительным числом")
        if not (min_year <= years <= max_year):
            raise ValueError(f"Стаж должен быть между {min_year} и {max_year} лет")

    def verify_salary(self, salary):
        min_salary = self.kwargs.get("min_salary", 0)
        max_salary = self.kwargs.get("max_salary", 1000000)
        if not isinstance(salary, (int, float)) or salary < 0:
            raise ValueError("Зарплата должна быть положительным числом")
        if not (min_salary <= salary <= max_salary):
            raise ValueError(f"Зарплата должна быть между {min_salary} и {max_salary}")

    def __set_name__(self, owner, name):
        self.private_name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.private_name)

    def __set__(self, instance, value):
        # Вызов валидации в зависимости от имени атрибута
        if self.private_name == "_name":
            self.verify_name(value)
        elif self.private_name == "_years_of_experience":
            self.verify_years_of_experience(value)
        elif self.private_name == "_salary":
            self.verify_salary(value)
        setattr(instance, self.private_name, value)


class Employee:
    # Используем дескрипторы для валидации
    name = EmployeeController(min_length=3, max_length=40)
    salary = EmployeeController(min_salary=10000, max_salary=100000)
    years_of_experience = EmployeeController(min_year=1, max_year=40)

    def __init__(self, name, salary, years_of_experience):
        self.name = name
        self.salary = salary
        self.years_of_experience = years_of_experience

    # Сравнение по зарплате и стажу
    def __eq__(self, other: "Employee") -> bool:
        return (
            self.salary == other.salary
            and self.years_of_experience == other.years_of_experience
        )

    def __ne__(self, other: "Employee") -> bool:
        return not self.__eq__(other)

    def __lt__(self, other: "Employee") -> bool:
        if self.salary == other.salary:
            return self.years_of_experience < other.years_of_experience
        return self.salary < other.salary

    def __gt__(self, other: "Employee") -> bool:
        if self.salary == other.salary:
            return self.years_of_experience > other.years_of_experience
        return self.salary > other.salary

    def __le__(self, other: "Employee") -> bool:
        return self.__lt__(other) or self.__eq__(other)

    def __ge__(self, other: "Employee") -> bool:
        return self.__gt__(other) or self.__eq__(other)

    def __repr__(self):
        return f"Employee(name={self.name}, salary={self.salary}, years_of_experience={self.years_of_experience})"


# Пример использования
employee1 = Employee("John", salary=50000, years_of_experience=5)
employee2 = Employee("Jane", salary=55000, years_of_experience=4)

print(employee1 == employee2)  # False
print(employee1 > employee2)   # False (зарплата меньше, опыт больше)
print(employee1 < employee2)   # True (зарплата меньше)
