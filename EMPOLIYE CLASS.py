class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print(self.name, self.salary)

class Manager(Employee):
    def bonus(self):
        print("Manager Bonus:", self.salary * 0.20)

class Developer(Employee):
    def bonus(self):
        print("Developer Bonus:", self.salary * 0.10)

m = Manager("Ram", 50000)
d = Developer("Shyam", 40000)

m.display()
m.bonus()

d.display()
d.bonus()