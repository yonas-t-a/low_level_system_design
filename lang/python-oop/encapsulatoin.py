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

    # python getter
    @property
    def balance(self):
        return self.__balance

    # python setter
    @balance.setter
    def balance(self, value):
        self.__balance = value



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
    print(account.balance)
    account.withdraw(3000)
    print(account.balance)

    account.balance = 7687
    print(account.balance)


        