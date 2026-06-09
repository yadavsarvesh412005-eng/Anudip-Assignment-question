#Create a generator that reads a file line by line

#Suppose data.txt contains:

#Hello
#Iterator
#Generator
def read_file(filename):
    with open(filename, "r") as file:
        for line in file:
            yield line.strip()

for line in read_file("data.txt"):
    print(line)