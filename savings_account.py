from account import Account

class SavingsAccount(Account):
    def __init__(self):
        Account.__init__(self)

    def deposit(self, amount):
        self.balance = self.balance + amount
        rate = self.balance * (0.005)
        self.balance = self.balance + rate
        print("New balance is: ", self.balance)

    def withdrawal(self, amount):
        if amount <= 700000:
            super().withdrawal(amount)
        else:
            print("Amount exceeds withdrawal limit", self.__interest_rate)

savings = SavingsAccount()
savings.withdrawal(1000)
savings.deposit(0)