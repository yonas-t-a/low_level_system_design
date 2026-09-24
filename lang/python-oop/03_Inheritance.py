class Account:
    id_pointer = 0
    def __init__(self, owner_name, balance, account_type):
        self.id_pointer +=1
        self.account_id = self.id_pointer

        self.owner_name = owner_name
        self.__balance = balance
        self.account_type = enumerate(["Saving", "Checking"])

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, amount):
        self.__balance += amount

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            raise ValueError("deposit Amount can't be negative")


    def withdraw(self, amount):
        if amount < self.balance:
            self.balance -= amount
        else:
            raise ValueError("The balance is insufficent")

    def show_balance(self):
        return self.balance

    def get_account_summery(self):
        account_id = self.account_id
        account_owner = self.owner_name
        account_balance = self.balance
        account_type = self.account_type
        print(f'Account id ={account_id} \n Owner Name = {account_owner} \n Total balance = {account_balance} \n Type = {account_type}')


class SavingAccount(Account):
    def __init__(self, owner_name, balance, account_type):
        super().__init__(owner_name, balance, account_type)
        self.interest_rate = 0.7
        self.minimum_balance = 100
    
    def apply_interest(self):
        self.balance += self.balance*self.interest_rate

    def check_minimum_balance(self):
        if self.show_balance() <= self.minimum_balance:
            return f'Warning, Your Account is less than the required minimum balance of {self.minimum_balance}'
    
    
    
class ChackingAccount(Account):
    def __init__(self, owner_name, balance, account_type):
        super().__init__(owner_name, balance, account_type)
            
    
    



    

    
        
        