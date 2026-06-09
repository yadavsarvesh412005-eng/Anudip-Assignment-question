# 2. Student class and topper

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

def topper(students):
    return max(students, key=lambda s: s.marks)

s1 = Student("Ram", 85)
s2 = Student("Shyam", 95)
s3 = Student("Mohan", 90)

print("Topper:", topper([s1, s2, s3]).name)
