#Create your own iterator for even numbers
class EvenNumbers:
    def __init__(self, limit):
        self.limit = limit
        self.num = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= self.limit:
            value = self.num
            self.num += 2
            return value
        else:
            raise StopIteration

e = EvenNumbers(10)

for i in e:
    print(i)