class BankAccount:
    bank_title = "Le Bank National Bank"

    def __init__(self, customer_name, curr_balance, min_balance):
        self.customer_name = customer_name
        self.current_balance = curr_balance
        self.min_bal = min_balance

    def deposit(self, amount):
        if amount > 0:
            self.current_balance += amount
            print(f"Desposited ${amount}. New balance: ${self.current_balance}")
        else:
            print("Deposit amount must be positive")
    def withdraw(self, amount):
        if self.current_balance - amount < self.min_bal:
            print(f"Cannot withdraw ${amount}. Minimum balance requirement of ${self.min_bal} would be violated")
        elif amount > 0:
            self.current_balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.current_balance}")
        else:
            print("Wihtdrawl amount must be postive")
    def print_cust_info(self):
        print(f"Bank: {BankAccount.bank_title}")
        print(f"Customer Name: ${self.customer_name}")
        print(f"Current balance: ${self.current_balance}")
        print(f"Minimum Required Balance: ${self.min_bal}")

account1 = BankAccount("Alice", 1000, 100)
account2 = BankAccount("Bob", 500, 50)

account1.deposit(200)
account1.withdraw(1100) 
account1.withdraw(100) # Should Trigger Violation as balance would be 100
account1.print_cust_info()

print()

account2.deposit(50)
account2.withdraw(600) # Should Trigger Violation
account2.withdraw(100)
account2.print_cust_info()
