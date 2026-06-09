class Account:
    def __init__(self, balance):
        self.balance = balance

    def show_balance(self):
        print("Balance:", self.balance)

class SavingsAccount(Account):
    def interest(self):
        print("Interest:", self.balance * 0.05)

class CurrentAccount(Account):
    def service_charge(self):
        print("Service Charge:", self.balance * 0.02)

s = SavingsAccount(10000)
c = CurrentAccount(10000)

s.show_balance()
s.interest()

c.show_balance()
c.service_charge()