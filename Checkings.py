from bank_account import BankAccount

class CheckingAccount(BankAccount):
    def __init__(self, customer_name, curr_balance, min_balance, account_num, routing_num, transfer_limit):
        super().__init__(customer_name, curr_balance, min_balance, account_num, routing_num)
        self.transfer_limit = transfer_limit

    def transfer(self, amount, recipient_account):
        if amount <= 0:
            print("Transfer amount must be positive")
        elif amount > self.transfer_limit:
            print(f"Transfer failed: amount ${amount} exceeds transfer limit of ${self.transfer_limit}")
        elif amount > self.current_balance:
            print("Transfer failed: insufficient funds")
        else:
            self.current_balance -= amount
            recipient_account.current_balance += amount
            print(f"Transferred ${amount} to {recipient_account.customer_name}. New balance: ${self.current_balance}")