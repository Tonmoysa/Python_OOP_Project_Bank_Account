from bank_accounts import *
Tanmoy=BankAccount(10000,'Tanmoy')
Bijo=BankAccount(20000,'Tanus Wife')
Tanmoy.getBalance()
Bijo.getBalance()
Tanmoy.depositBalance(5000)
Tanmoy.withdraw(20000)
Tanmoy.withdraw(10)
Tanmoy.transfer(10000,Bijo)

jim=Interest(1000,'Jim')
jim.getBalance()
jim.depositBalance(100)
jim.transfer(100,Tanmoy)


Blaze=SavingAccount(1000,'Blaze')
Blaze.getBalance()
Blaze.depositBalance(100)
Blaze.transfer(300,Tanmoy)
