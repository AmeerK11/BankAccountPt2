from BankAccountPt2.BankAccount import BankAccount
class Savings(BankAccount):

    def __init__(self, customer_name, curr_balance, min_balance, account_number, interest_rate):
         super().__init__(customer_name, curr_balance, min_balance)
         self.__account_number = account_number
         self.__interest_rate = interest_rate

    def interest(self):
         self.curr_balance = self._curr_balance + (self._curr_balance * self.__interest_rate)
         print("Interest added. Current Balance: $" + str(self.curr_balance))

    def get_account_number(self):
        return self.__account_number