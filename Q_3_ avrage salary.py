# 7. Employee class and average salary

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

def average_salary(employees):
    return sum(e.salary for e in employees) / len(employees)

e1 = Employee("A", 30000)
e2 = Employee("B", 40000)
e3 = Employee("C", 50000)

print("Average Salary:", average_salary([e1, e2, e3]))
