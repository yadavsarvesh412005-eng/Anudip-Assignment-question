total=0
for i in range(5):
    marks=int(input("enter marks"))
    total+=marks
percentage=total/5
if percentage>=90:
    Grade="A"
elif percentage>=60:
    Grade="B"
else:
    Grade="C"
print("percentage=",percentage)
print("Grade=",Grade)


