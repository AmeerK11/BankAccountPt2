from bank_account import BankAccount

class Savings(BankAccount):
    def __init__(self, customer_name, account_num, routing_num, current_balance, min_balance, rate):
        super().__init__(customer_name, current_balance, min_balance, account_num, routing_num)
        self.rate = rate

    def incr(self):
        intr = self.current_balance * self.rate
        self.deposit(intr)
class Checking(BankAccount):
    def __init__(self, customer_name, account_num, routing_num, current_balance, min_balance, LIMIT):
        super().__init__(customer_name, current_balance, min_balance, account_num, routing_num)
        self.LIMIT = LIMIT
    def withdraw(self, amount):
        if amount <= self.current_balance + self.LIMIT:
            self.current_balance -= amount
        else:
            print("Overdraft limit exceeded")