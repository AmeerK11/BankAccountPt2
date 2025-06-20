class BankAccount:
    bank_title = "Le Bank National Bank"

    def __init__(self, customer_name, curr_balance, min_balance, account_num, routing_num):
        self.customer_name = customer_name
        self.current_balance = curr_balance
        self.min_bal = min_balance
        self._account_number = account_num
        self.__routing_number = routing_num

    def deposit(self, amount):
        if amount > 0:
            self.current_balance += amount
            print(f"Deposited ${amount}. New balance: ${self.current_balance}")
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):
        if self.current_balance - amount < self.min_bal:
            print(f"Cannot withdraw ${amount}. Minimum balance requirement of ${self.min_bal} would be violated")
        elif amount > 0:
            self.current_balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.current_balance}")
        else:
            print("Withdrawal amount must be positive")

    def print_cust_info(self):
        print(f"\nBank: {BankAccount.bank_title}")
        print(f"Customer Name: {self.customer_name}")
        print(f"Current Balance: ${self.current_balance}")
        print(f"Minimum Required Balance: ${self.min_bal}")
        print(f"Account Number (protected): {self._account_number}")
        print(f"Routing Number (private): {self.__routing_number}")
