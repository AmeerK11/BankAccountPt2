from BankAccountPt2.BankAccount import BankAccount
from BankAccountPt2.Savings import Savings
from BankAccountPt2.Checkings import Checkings

#John Doe opens a checking account with $1000. The minimum balance required in the account is $100.
#June Doe opens a checking account with $700. The minimum balance required in the account is $100.
my_account = Checkings("John Doe", 1000, 100, "1234", 3000)
my_account3 = Checkings("June Doe", 700, 100, "0893", 3000)
#John Doe withdraws $250.
my_account.withdraw(250)

#John Doe attempts to deposit money into his account from his friend's account. He tries to deposit $5000.
my_account.deposit(5000) #This should fail. $5000 is over the transfer limit of $3000.
my_account.print_cust_info()
print(my_account.get_account_number()) #Prints account number.

#June Doe prints her customer information and attempts to transfer money into her checking account.
my_account3.print_cust_info()
my_account3.deposit(100)


#Sally opens a saving account with an initial balance of $1000 and a minimum balance of $100 required. Her account
#number is 5678 and her interest compounds annually at 3%.

my_account2 = Savings("Sally Sue", 1000, 100, 5678, 0.03)
#Sally deposits $500.
my_account2.deposit(500)
#Sally withdraws $200.
my_account2.withdraw(200)
#A year has gone by. Sally's interest has compounded.
my_account2.interest()

#Ben opens a saving account with an initial balance of $2000 and a minimum balance of $100 required. Her account
#number is 9032 and his interest compounds annually at 5%.

my_account4 = Savings("Ben Blue", 2000, 100, 5678, 0.05)
#Ben deposits $500.
my_account4.deposit(500)
#Ben withdraws $200.
my_account4.withdraw(200)
#A year has gone by. Ben's interest has compounded.
my_account4.interest()
