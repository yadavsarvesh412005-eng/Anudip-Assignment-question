#Create a class that can be used inside a for loop (__iter__)
class Numbers:
    def __init__(self):
        self.data = [10, 20, 30, 40]

    def __iter__(self):
        return iter(self.data)

n = Numbers()

for i in n:
    print(i)