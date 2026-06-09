choice=""
while choice!="4":
    print("1,pizza")
    print("2,burger")
    print("3,sandwich")
    print("4,exit")
    choice=input("enter your choice:")
    if choice=="1":
        print("you have ordered pizza")
    elif choice=="2":
        print("you have ordered burger")
    elif choice=="3":
        print("you have ordered sandwich")
    elif choice=="4":
        print("exiting the program")
    else:
        print("thank you for using our service")
