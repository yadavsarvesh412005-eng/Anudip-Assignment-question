attempt=0
while attempt<3:
    password=input("enter the password:")
    if password=="@yadav124":
        print("login successful")
        break
    else:
        print("incorrect password")
        attempt+=1
    if attempt==3:
        print("account locked")
        