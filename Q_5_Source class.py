# 10. Course class and students in multiple courses

class Course:
    def __init__(self, name, students):
        self.name = name
        self.students = students

def multiple_courses(courses):
    count = {}
    for course in courses:
        for student in course.students:
            count[student] = count.get(student, 0) + 1

    for student, num in count.items():
        if num > 1:
            print(student)

c1 = Course("Python", ["Ram", "Shyam", "Mohan"])
c2 = Course("Java", ["Ram", "Sohan"])
c3 = Course("C++", ["Shyam", "Rohan"])

multiple_courses([c1, c2, c3])