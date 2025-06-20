from bank_account import BankAccount
from accounts import Savings, Checking

def main():
    acct = BankAccount("Teej", 1245, 0, "2345", "234")
    sav = Savings("123", "234", 1245, .08)
    chk = Checking("2333", "4545", 500)

    print("Initial Savings Balance: ", sav.print_cust_info())
    sav.incr()
    print("After Interest:", sav.print_cust_info())

    print("\nInitial Checking Info:", chk.print_cust_info())
    chk.withdraw(550) # should trigger violation
    print("\nAfter Withdraw Checking Info:", chk.print_cust_info())
if __name__ == "__main__":
    main()