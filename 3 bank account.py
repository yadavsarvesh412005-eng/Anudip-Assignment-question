# 3. BankAccount class and transfer money

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

def transfer(sender, receiver, amount):
    if sender.balance >= amount:
        sender.balance -= amount
        receiver.balance += amount
        print("Transfer Successful")
    else:
        print("Insufficient Balance")

a1 = BankAccount("Amit", 5000)
a2 = BankAccount("Ravi", 3000)

transfer(a1, a2, 2000)
print(a1.balance, a2.balance)
