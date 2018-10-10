import BankAccount

if __name__ == '__main__':
    myBankAccount = BankAccount.bankAccount_Class(3000)
    print(myBankAccount)

    myBankAccount.deposit(2000)
    print(myBankAccount)

    myBankAccount.__balance = 12000
    print(myBankAccount)
