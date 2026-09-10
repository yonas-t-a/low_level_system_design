class BankAccount:
    def __init__(self, balance, localCUR=True):
        self.__balance = balance
        self._localCUR = localCUR

    def depoite(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):
        print(self.__balance)

if __name__ == "__main__":
    account =  BankAccount(5000, True)
    try:
        print(account.__balance) # This will Rise AttributeError
    except AttributeError as e:
        print(e)
    print(account._localCUR)

    # But we can acess balance with the following method 
    print(account._BankAccount__balance)

    account.depoite(5000)
    account.get_balance()
    account.withdraw(3000)
    account.get_balance()

        