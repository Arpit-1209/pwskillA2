class Employee:
    employee_count = 0

    def __init__(self, name):
        self.name = name
        Employee.employee_count += 1

    @classmethod
    def get_employee_count(cls):
        return cls.employee_count

emp1 = Employee("John")
emp2 = Employee("Jane")
print(Employee.get_employee_count())  # Output: 2
