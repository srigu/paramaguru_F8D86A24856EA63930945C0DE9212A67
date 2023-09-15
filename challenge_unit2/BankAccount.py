class BankAccount():
    def __init__(self,account_number,account_holder_name,initial_balance=0.0):
        self.__account_number=account_number
        self.__account_holder_name=account_holder_name
        self.__account_balance=initial_balance
    def deposit(self,amount):
        if amount > 0:
            self.__account_balance += amount
            print("Deposited:",amount,". New balance:",self.__account_balance)
        else:
            print("Invalid deposit amount")
    def withdraw(self,amount):
        if amount > 0 and amount <= self.__account_balance:
            self.__account_balance -= amount
            print("Withdraw:",amount,". New balance:",self.__account_balance)
        else:
            print("Invalid withdraw amount or insufficient balance")
    def display_balance(self):
        print("Account balance for",self.__account_holder_name,"(Account",self.__account_number,"):",self.__account_balance)


account1=BankAccount(account_number="21115678900045",account_holder_name="K.Paramaguru",initial_balance=10000.0)
account1.display_balance()
account1.deposit(5000.0)
account1.withdraw(7000.0)
account1.display_balance()
