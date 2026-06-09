# 1. Rectangle class and largest area

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

def largest_rectangle(rectangles):
    return max(rectangles, key=lambda r: r.area())

r1 = Rectangle(5, 4)
r2 = Rectangle(8, 3)
r3 = Rectangle(6, 2)

largest = largest_rectangle([r1, r2, r3])
print("Largest Area:", largest.area())
