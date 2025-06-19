 
from bank_account import BankAccount

class SavingsAccount(BankAccount):
    def __init__(self, customer_name, curr_balance, min_balance, account_num, routing_num, interest_rate):
        super().__init__(customer_name, curr_balance, min_balance, account_num, routing_num)
        self.interest_rate = interest_rate

    def apply_interest_rate(self):
        interest= self.current_balance * (self.interest_rate / 100)
        self.current_balance += interest
        print(f"Interest of ${interest:.2f} applied. New balance: ${self.current_balance:.2f}")
