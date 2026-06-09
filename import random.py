import random

trains = {
    101: {"name": "Rajdhani Express", "seats": 50},
    102: {"name": "Shatabdi Express", "seats": 40}
}

bookings = []
#While condition:
while True:
    print("\n--- Train Reservation System ---")
    print("1. View Trains")
    print("2. Book Ticket")
    print("3. Cancel Ticket")
    print("4. View Bookings")
    print("5. Exit")

    choice = input("Enter Choice: ")
#if_elif else conditin:
    if choice == "1":
        for train_no, details in trains.items():
            print(train_no, details["name"], "Seats:", details["seats"])

    elif choice == "2":
        train_no = int(input("Enter Train Number: "))
        name = input("Enter Passenger Name: ")

        if train_no in trains and trains[train_no]["seats"] > 0:
            trains[train_no]["seats"] -= 1
            bookings.append((name, train_no))
            print("Ticket Booked Successfully!")
        else:
            print("No Seats Available!")

    elif choice == "3":
        name = input("Enter Passenger Name: ")

        for booking in bookings:
            if booking[0] == name:
                trains[booking[1]]["seats"] += 1
                bookings.remove(booking)
                print("Ticket Cancelled!")
                break
        else:
            print("Booking Not Found!")

    elif choice == "4":
        print("\nPassenger Bookings:")
        for booking in bookings:
            print("Name:", booking[0], "Train No:", booking[1])

    elif choice == "5":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")