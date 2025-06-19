 
from main import BankAccount

class Savings(BankAccount):
    def __init__(self, customer_name, curr_balance, min_balance, acc_number, routing_number, interest_rate):
        super().__init__(customer_name, curr_balance, min_balance, acc_number, routing_number)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.current_balance * self.interest_rate
        self.current_balance += interest
        print(f"{self.customer_name}: Interest of ${interest:.2f} applied. New balance: ${self.current_balance:.2f}")