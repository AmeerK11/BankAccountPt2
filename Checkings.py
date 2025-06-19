from BankAccountPt2.BankAccount import BankAccount
class Checkings(BankAccount):

    def __init__(self, customer_name, curr_balance, min_balance, account_number, transfer_limit):
         super().__init__(customer_name, curr_balance, min_balance)
         self.__account_number = account_number
         self.__transfer_limit = transfer_limit

    def deposit(self, amount):
        if (amount > self.__transfer_limit):
             print(f"Deposit failed. ${amount} over ${self.__transfer_limit}.")
        if amount > 0:
            self.curr_balance += amount
            print(f"Desposited ${amount}. New balance: ${self.curr_balance}")
        else:
            print("Deposit amount must be positive")


    def get_account_number(self):
        return self.__account_number