from account import Account

class CurrentAccount(Account):
    def __init__(self):
        Account.__init__(self)

current = CurrentAccount()
current.deposit(4000)
current.withdrawal(2000)
