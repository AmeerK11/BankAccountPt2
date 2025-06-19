from Savings import SavingsAccount
from bank_account import BankAccount
from Checkings import CheckingAccount


def main():
    print("\n--- Savings Account ---")
    alice = SavingsAccount("Alice", 1000, 100, "SA123", "RT001", 2.5)

    bob = SavingsAccount("Bob", 500, 50, "SA456", "RT002", 3.0)

    alice.deposit(200)
    alice.apply_interest_rate()
    alice.withdraw(100)
    alice.print_cust_info()

    bob.apply_interest_rate()
    bob.print_cust_info()


    print("\n--- Checking Account ---")
    charlie = CheckingAccount("Charlie", 1000, 100, "CA001", "RT005", 300)
    dana = CheckingAccount("Dana", 500, 50, "CA002", "RT006", 500)

    charlie.transfer(350, dana)  # Should fail (over limit)
    charlie.transfer(250, dana)  # Should succeed

    charlie.print_cust_info()
    dana.print_cust_info()

    """
    
    Part 1

    print("\n--- Regular Bank Account ---")
    account1 = BankAccount("Alice", 1000, 100)
    account2 = BankAccount("Bob", 500, 50,)

    account1.deposit(200)
    account1.withdraw(1100)
    account1.withdraw(100) # Should Trigger Violation as balance would be 100
    account1.print_cust_info()

    print()

    account2.deposit(50)
    account2.withdraw(600) # Should Trigger Violation
    account2.withdraw(100)
    account2.print_cust_info()
    """
if __name__ == "__main__":
    main()
