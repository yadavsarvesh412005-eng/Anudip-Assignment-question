#Create a reverse iterator for a list
class ReverseList:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration

        self.index -= 1
        return self.data[self.index]

lst = [10, 20, 30, 40, 50]

for i in ReverseList(lst):
    print(i)