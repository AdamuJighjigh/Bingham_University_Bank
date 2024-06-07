from account import Account

class StudentAccount(Account):
    def __init__(self):
        Account.__init__(self)
    def withdrawal(self, amount):
        if amount <=2000:
            super().withdrawal(amount)
        else:
            print("Withdraw limit exceeded")
def deposit(self, amount):
        if amount <= 50000:
            super().deposit(amount)
        else:
            print(" Your deposit limit exceeded!")


student = StudentAccount()
student.withdrawal(1990)
student.deposit(1000)