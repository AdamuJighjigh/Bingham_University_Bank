from account import Account

class StudentAccount(Account):
    def __init__(self):
        Account.__init__(self)

    def withdrawal(self, amount):
        if amount <= 2000:
            super().withdrawal(amount)
        else:
            print("Amount exceeds withdrawal limit")

    def deposit(self, amount):
        if amount <= 50000:
            super().deposit(amount)
        else:
            print("amount exceeds deposit limit!")

student = StudentAccount()
student.withdrawal(1000)
student.deposit(2000)