from bank_account import BankAccount
from accounts import Savings, Checking

def main():
    acct = BankAccount("Teej", 1245.0, 0.0, "2345", "234")
    sav = Savings("Teej", "234", "1245", 1000.0, 100.0, .08)

    print("Initial Savings Balance: ", sav.print_cust_info())
    sav.incr()
    print("After Interest:", sav.print_cust_info())

if __name__ == "__main__":
    main()