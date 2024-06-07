from account import Account

class ChildrenAccount(Account):
    def __init__(self):
        Account.__init__(self)

    def deposit(self, amount):
        self.__interest = amount * 0.007
        self.balance = self.balance + amount
        self.balance = self.balance + self.__interest
        print("New balance is: ", self.balance)

    def withdrawal(self):
        print("This function is not available to this account")

children = ChildrenAccount()
children.deposit(7000)
children.withdrawal()