from main import BankAccount

class Checkings(BankAccount):
    def __init__(self, customer_name, current_balance, min_balance, acc_number, routing_number, transfer_limit):
        super().__init__(customer_name, current_balance, min_balance, acc_number, routing_number)
        self.transfer_limit = transfer_limit

    def transfer(self, amount, target_account):
        if amount <= 0:
            print("Transfer amount must be positive")
        elif amount > self.transfer_limit:
            print("Transfer amount exceeds limit")
        elif self.current_balance - amount < self.min_balance:
            print("Transfer amount exceeds minimum balance")
        else:
            self.current_balance -= amount
            target_account.transfer_amount += amount
            print(f"{self.customer_name}: Transferred ${amount} to {target_account.customer_name}")
