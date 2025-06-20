from bank_account import BankAccount

class Savings(BankAccount):
    def __init__(self, acct, routing, balance, rate):
        super().__init__(acct, routing, balance)
        self.rate = rate

    def incr(self):
        self.deposit(self.balance * self.rate)
class Checking(BankAccount):
    def __init__(self, acct, routing, balance, LIMIT):
        super.__init__(acct, routing, balance)
        self.LIMIT = LIMIT
    def withdraw(self, amount):
        if amount <= self.current_balance + self.LIMIT:
            self.current_balance -= amount
        else:
            print("Overdraft limit exceeded")