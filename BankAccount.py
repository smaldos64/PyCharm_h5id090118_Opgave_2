
class bankAccount_Class():
    def __init__(self, amount = 2000):
        self.__balance = amount

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if self.__balance - amount >= 0:
            self.__balance -= amount;
        else:
            print("Overtræk er ikke tilladt i min bank !!!")

    def __str__(self):
        return ("Indestående på kontoen er : %s kr" % str(self.__balance))