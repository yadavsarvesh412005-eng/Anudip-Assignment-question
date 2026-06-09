#Create a generator that yields squares of numbers
def squares(n):
    for i in range(1, n + 1):
        yield i * i

for x in squares(5):
    print(x)