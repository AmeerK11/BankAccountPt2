from BankAccountPt2.BankAccount import BankAccount
class Checkings(BankAccount):

    def __init__(self, customer_name, curr_balance, min_balance, account_number, transfer_limit):
         super().__init__(customer_name, curr_balance, min_balance)
         self.__account_number = account_number
         self.__transfer_limit = transfer_limit

    def deposit(self, amount):
        if (amount > self.__transfer_limit):
             print(f"Deposit failed. ${amount} is over the transfer limit of ${self.__transfer_limit}.")
        elif amount > 0:
            self._curr_balance += amount
            print(f"Deposited ${amount}. New balance: ${self._curr_balance}")
        else:
            print("Deposit amount must be positive")


    def get_account_number(self):
        return self.__account_number