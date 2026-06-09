# Train Reservation System
import random

import json

try:
    from reportlab.pdfgen import canvas
except ImportError:
    canvas = None

tickets = []

 
def book_ticket():

  
    passenger = {}

   
    passenger["PNR"] = random.randint(10000,99999)

    
    passenger["Name"] = input("Enter Name : ")
    passenger["Age"] = input("Enter Age : ")
    passenger["Train"] = input("Enter Train : ")
    passenger["Coach"]= input("Enter Coach : ")
    passenger["Class"] = input("Enter ticket_class : ")
    passenger["Seat"] = input("Enter Seat_number : ")
    passenger["mobile"]= input("Eenter mobile number : ")
    
     
    tickets.append(passenger)

    print("Ticket Booked")
    print(passenger)


def search_ticket():

    pnr = int(input("Enter PNR : "))
    
    
    
    for ticket in tickets:

        
        if ticket["PNR"] == pnr:
           
         print(ticket)

          
        break

 
def cancel_ticket():

    pnr = int(input("Enter PNR : "))

    for ticket in tickets:

        if ticket["PNR"] == pnr:

            
            tickets.remove(ticket)

            print("Ticket Cancelled")

            break

 
def view_ticket():

    
    print("Total Tickets =", len(tickets))

    for ticket in tickets:
        print(ticket)


def pdf_ticket():

    pnr = int(input("Enter PNR : "))

    for ticket in tickets:

        if ticket["PNR"] == pnr:

           
            pdf= canvas.Canvas("Ticket.pdf")
            
            pdf.drawString(100,800,"TRAIN RESERVATION")
            pdf.drawString(100,780,"PNR : "+str(ticket["PNR"]))
            pdf.drawString(100,760,"Name : "+ticket["Name"])
            pdf.drawString(100,740,"Age : "+ticket["Age"])
            pdf.drawString(100,720,"Train : "+ticket["Train"])
            pdf.drawString(100,700,"Coach: "+ticket["Coach"])
            pdf.drawString(100,680,"Class : "+ticket["Class"])
            pdf.drawString(100,710,"Seat:"+ticket["Seat"])
            pdf.drawString(100,640,"mobile : "+ticket["mobile"])
            
            pdf.save()

            print("PDF Created")

            break

 
while True:

    print("\n1.Book Ticket")
    print("2.Search Ticket")
    print("3.Cancel Ticket")
    print("4.View Ticket")
    print("5.PDF Ticket")
    print("6.Exit")

    choice = int(input("Enter Choice : "))

    
    if choice == 1:
        book_ticket()

    elif choice == 2:
        search_ticket()

    elif choice == 3:
        cancel_ticket()

    elif choice == 4:
        view_ticket()

    elif choice == 5:
        pdf_ticket()

    elif choice == 6:
        print("Thank You")
        break

    else:
        print("Invalid Choice")