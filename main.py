class BankAccount:
    def __init__(self, account_number, initial_balance):
        self.__account_number = account_number
        self.__balance = initial_balance
        

    def get_account_number(self):
        return  self.__account_number

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Cannot deposit zero or negative funds")
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Cannot withdraw zero or negative funds")
        elif self.__balance < amount:
            raise ValueError("Insufficient funds")
        self.__balance -= amount

def main():

    account_1 = BankAccount(3123233312, 3525)
    print(f"Your account number is: {account_1.get_account_number()}")
    print(f"Your account balance is: {account_1.get_balance()}$")

main()