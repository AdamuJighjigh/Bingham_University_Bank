class Account:
    def __init__(self):
        self.balance = 50000
        self.__interest_rate = (0.5/100)
        self.__id_number = 'DG57895'
        self.__interest = (0.7/100)
        print("Starting balance: ", self.balance)

    def set_id_number(self, new_id_number):
        self.__id_number = new_id_number


    def get_interest_rate(self):
        return self.__interest_rate

    def get_interest(self):
        return self.__interest

    def deposit(self, amount):
        self.balance = amount + self.balance
        print("New balance: ", self.balance)

    def withdrawal(self, amount):
        self.balance = self.balance - amount
        print("Withdrawal balance is: ", self.balance)

customer = Account()
customer.withdrawal(2000)