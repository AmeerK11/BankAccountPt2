from BankAccountPt2.BankAccount import BankAccount
from BankAccountPt2.Savings import Savings
from BankAccountPt2.Checkings import Checkings

#John Doe opens a checking account with $1000. The minimum balance required in the account is $100.
my_account = Checkings("John Doe", 1000, 100, 1234, 3000)

#John Doe withdraws $250.
my_account.withdraw(250)

#John Doe attempts to deposit money into his account from his friend's account. He tries to deposit $5000.
my_account.deposit(5000) #This should fail. $5000 is over the transfer limit of $3000.
my_account.print_cust_info()
print(my_account.get_account_number()) #Prints account number.

#Sally opens a saving account with an initial balance of $1000 and a minimum balance of $100 required. Her account
#number is 5678 and her interest compounds annually at 3%.

my_account2 = Savings("Sally Sue", 1000, 100, 5678, 0.03)
#Sally deposits $500.
my_account2.deposit(500)
#Sally withdraws $200.
my_account2.withdraw(200)
#A year has gone by. Sally's interest has compounded.
my_account2.interest()
